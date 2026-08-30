"""Reconcile the checkpoint workbook against this repository's census.

The workbook is an independent reconstruction of the same fifteen months,
holding 353 records where this repository holds 298. It saw a different source
set, so it is NOT a third blind coder and no kappa is computed against it. It is
a challenger: the useful question is not "do they agree" but "what does each one
have that the other does not, and who is right in each direction".

This script answers that mechanically and writes the evidence to
`challenge/reconciliation__companies.csv`. The narrative reading is in
`challenge/CHALLENGE.md`.

The comparison is at COMPANY grain, not row grain, and that is a deliberate
weakening. The two datasets use different units: this repository counts
application cycles keyed `company + role + cycle`, while the workbook counts
"reconstructed application-process records", a unit its own summary sheet admits
"may still exceed the number of unique employer requisitions". Matching those
row to row would manufacture agreement or disagreement out of a units mismatch.
Company presence is the coarsest claim both datasets actually make, and it is
enough to answer the coverage question, which is the one that matters.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adjudication"))

from _common import INTERVIEW_TYPES, is_excluded_event, load_csv  # noqa: E402
from ingest_platform import norm_company  # noqa: E402

CHALLENGE = ROOT / "challenge"
ADJ = ROOT / "adjudication"

# Legal and descriptive suffixes that differ between the two datasets for the
# same employer. `norm_company` in the matcher only strips punctuation, and
# company aliasing at Freeze 1 was done by hand during adjudication, so this
# comparison needs its own equivalence step.
#
# The direction of error matters here and runs opposite to the census matcher.
# There, a wrong merge destroys a record, so the matcher refuses. Here, an
# unmerged pair invents a coverage gap that does not exist and overstates the
# challenge, so this step merges aggressively and every residual gap is listed
# in full for inspection rather than being reported as a bare count.
SUFFIX_TOKENS = (
    "incorporated", "corporation", "technologies", "technology", "industries",
    "software", "holdings", "solutions", "systems", "labs", "group", "inc",
    "llc", "ltd", "corp", "com", "co", "io", "ai",
)

# True renames and acquisitions, where no string rule can connect the two.
# Taken from the alias merges already recorded in adjudication/ADJUDICATION.md.
COMPANY_ALIASES = {
    "cursor": "anysphere",
    "everyto": "every",
    "thehogycf25": "thehog",
    # Prefix equivalence needs the shorter key to be at least MIN_PREFIX long,
    # so a three-character canonical name can never match its own longer form.
    # Found by the supplementary ledger, which reported Exa Labs as workbook-only
    # while `exa|growth-lead|c1` sat in the census. ADJUDICATION.md already
    # records "Exa / Exa Labs" as a hand alias merge, so this restates a
    # decision rather than making a new one.
    "exalabs": "exa",
}

MIN_PREFIX = 4


def company_key(name: str) -> str:
    """Normalize, strip trailing legal and descriptive suffixes, alias twice.

    The alias table is consulted BEFORE and AFTER stripping. Before, so a rename
    keyed on the raw form ("cursor" to "anysphere") fires. After, because
    stripping can leave a form the raw lookup never saw: "Exa Labs Inc." reaches
    "exalabs" only once "inc" is gone, and an alias keyed on the raw
    "exalabsinc" would never match it.
    """
    key = COMPANY_ALIASES.get(norm_company(name), norm_company(name))
    changed = True
    while changed and len(key) > MIN_PREFIX:
        changed = False
        for suffix in SUFFIX_TOKENS:
            if key.endswith(suffix) and len(key) - len(suffix) >= MIN_PREFIX:
                key, changed = key[: -len(suffix)], True
                break
    return COMPANY_ALIASES.get(key, key)


def equivalent(left: str, right: str) -> bool:
    """One key is an ordered prefix of the other, the rule the matcher already
    uses on role titles, applied to company names."""
    if left == right:
        return True
    shorter, longer = sorted((left, right), key=len)
    return len(shorter) >= MIN_PREFIX and longer.startswith(shorter)


def resolve(unmatched: set[str], candidates: set[str]) -> tuple[dict[str, str], set[str]]:
    """Match each unmatched key against the candidate side by prefix equivalence.

    Returns the resolved pairs and the keys that stayed genuinely unmatched.
    A key matching more than one candidate is still resolved here, because the
    question is presence rather than identity: if it matches anything, the
    company is not missing.
    """
    resolved, residual = {}, set()
    for key in unmatched:
        hits = [c for c in candidates if equivalent(key, c)]
        if hits:
            resolved[key] = sorted(hits, key=len)[0]
        else:
            residual.add(key)
    return resolved, residual


# Workbook source categories that are opportunity-register under this
# repository's two-register rule: no submission by the applicant, so they can
# never enter an application denominator here however the workbook counts them.
OPPORTUNITY_CATEGORIES = {
    "LinkedIn recruiter/person outreach",
    "Recruiter outbound / intermediary",
    "LinkedIn cold outreach",
    "Cold outreach I initiated",
    "Recruiting marketplace",
    "Mercor",
    "Talent marketplace",
    "Referral",
    "Community-sourced",
}


def load_challenge(name: str) -> list[dict]:
    return load_csv(CHALLENGE / name)


def company_sets() -> tuple[dict, dict, dict]:
    census = load_csv(ADJ / "applications__adjudicated.csv")
    full = load_csv(ADJ / "applications__full_census.csv")
    ledger = load_challenge("checkpoint__ledger.csv")
    source = {r["Thread/Dedup Key"]: r["Normalized Source Category"] for r in load_challenge("checkpoint__source_classification.csv")}
    for row in ledger:
        row["_category"] = source.get(row["Thread/Dedup Key"], "UNMAPPED")
        row["_norm"] = company_key(row["Company"])
    return (
        {company_key(r["company_canonical"]): r for r in census},
        {company_key(r["company_canonical"]): r for r in full},
        ledger,
    )


def main() -> None:
    census_by_company, full_by_company, ledger = company_sets()

    ledger_by_company: dict[str, list[dict]] = defaultdict(list)
    for row in ledger:
        ledger_by_company[row["_norm"]].append(row)

    # Split the workbook by whether its rows could ever be applications here.
    application_side = {
        c: rows for c, rows in ledger_by_company.items()
        if any(r["_category"] not in OPPORTUNITY_CATEGORIES for r in rows)
    }
    opportunity_only = {
        c: rows for c, rows in ledger_by_company.items() if c not in application_side
    }

    repo_keys, wb_keys = set(full_by_company), set(ledger_by_company)

    # Exact key match first, then prefix equivalence for the residue.
    wb_unmatched = {c for c in application_side} - repo_keys
    wb_resolved, only_workbook_set = resolve(wb_unmatched, repo_keys)
    repo_unmatched = repo_keys - wb_keys
    repo_resolved, only_repo_set = resolve(repo_unmatched, wb_keys)

    only_workbook = sorted(only_workbook_set)
    only_repo = sorted(only_repo_set)
    in_both = sorted((set(application_side) & repo_keys) | set(wb_resolved))
    print(f"  resolved by prefix equivalence: {len(wb_resolved)} workbook, {len(repo_resolved)} repository")

    print("=== Company coverage, application-capable rows only ===")
    print(f"  workbook companies (application-capable) : {len(application_side)}")
    print(f"  workbook companies (opportunity only)    : {len(opportunity_only)}")
    print(f"  repository full-census companies         : {len(full_by_company)}")
    print(f"  in both                                  : {len(in_both)}")
    print(f"  workbook only, a coverage gap here       : {len(only_workbook)}")
    print(f"  repository only, a coverage gap there    : {len(only_repo)}")

    rows_out = []
    for company in sorted(set(ledger_by_company) | set(full_by_company)):
        wb_rows = ledger_by_company.get(company, [])
        in_wb = bool(wb_rows)
        in_repo = company in full_by_company
        app_capable = company in application_side
        if in_wb and in_repo:
            verdict = "both"
        elif in_wb and company in wb_resolved:
            verdict = "both_via_alias"
        elif in_repo and company in repo_resolved:
            verdict = "both_via_alias"
        elif in_wb and app_capable:
            verdict = "workbook_only_application"
        elif in_wb:
            verdict = "workbook_only_opportunity"
        else:
            verdict = "repository_only"
        rows_out.append(
            {
                "company_normalized": company,
                "in_workbook": "yes" if in_wb else "no",
                "in_repository_full_census": "yes" if in_repo else "no",
                "workbook_rows": len(wb_rows),
                "workbook_categories": "; ".join(sorted({r["_category"] for r in wb_rows})),
                "repository_register": full_by_company[company]["register"] if in_repo else "",
                "repository_evidence_class": full_by_company[company]["evidence_class"] if in_repo else "",
                "verdict": verdict,
            }
        )

    path = CHALLENGE / "reconciliation__companies.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_out[0]))
        writer.writeheader()
        writer.writerows(rows_out)
    print(f"\nwrote {path.relative_to(ROOT)} ({len(rows_out)} rows)")

    # --- The LinkedIn export against the paged scrape it supersedes -----------
    export = load_csv(ROOT / "artifacts/platform/linkedin_job_applications_export.csv")
    scrape = load_csv(ROOT / "artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv")
    export_companies = {company_key(r["Company"]) for r in export}
    scrape_companies = {company_key(r["company"]) for r in scrape if r["company"]}
    print("\n=== LinkedIn: formal export against the paged scrape ===")
    print(f"  export rows, exact dates and job IDs : {len(export)}")
    print(f"  scrape rows, relative stamps         : {len(scrape)}")
    print(f"  scrape companies missing from export : {len(scrape_companies - export_companies)}")
    print(f"  export companies missing from scrape : {len(export_companies - scrape_companies)}")
    export_new, _ = resolve(export_companies - set(full_by_company), set(full_by_company))
    print(f"  export companies absent from the 298 : {len(export_companies - set(full_by_company)) - len(export_new)} after alias resolution")

    # --- Capture recapture: what the export does and does not deliver ---------
    # The protocol restricts the estimator to LinkedIn rows submitted through an
    # external ATS rather than Easy Apply. The export carries no such flag.
    downstream = [r for r in ledger if "downstream confirmation" in r["Origin/Source"] and r["Origin/Source"].startswith("LinkedIn application")]
    linkedin_only = [r for r in ledger if r["Origin/Source"].strip() == "LinkedIn application"]
    print("\n=== Capture recapture stratum ===")
    print(f"  LinkedIn rows with downstream employer-side confirmation : {len(downstream)}")
    print(f"  LinkedIn rows with no employer-side confirmation         : {len(linkedin_only)}")
    print("  Easy Apply flag present in the export                    : no")
    print("  => the second group mixes Easy Apply (structurally invisible to")
    print("     ATS mail) with rows Gmail retrieval simply missed. Those two")
    print("     are what the estimator must separate, so it stays unmeasured.")

    # --- Outcome model ------------------------------------------------------
    print("\n=== Outcome model, the two datasets disagree by construction ===")
    print("  workbook :", dict(Counter(r["Current/Final Status"] for r in ledger).most_common()))
    census = load_csv(ADJ / "applications__adjudicated.csv")
    print("  repository:", dict(Counter(r["terminal_outcome"] for r in census).most_common()))

    # --- Interviews ---------------------------------------------------------
    interviewed = {
        e["application_id"]
        for coder in ("cursor", "bravo")
        for e in load_csv(ROOT / "coding" / coder / f"events__{coder}.csv")
        if e["event_type"] in INTERVIEW_TYPES and not is_excluded_event(e)
    }
    census_ids = {r["application_id"] for r in census}
    print("\n=== Interviews ===")
    print(f"  repository, derived from events on census rows : {len(interviewed & census_ids)}")
    print("  workbook Interview Count column                 :", dict(Counter(r["Interview Count"] for r in ledger).most_common()))

    # --- Origin -------------------------------------------------------------
    known_repo = sum(1 for r in census if r["discovery_source"] != "unknown")
    print("\n=== Origin coverage ===")
    print(f"  repository census rows with a known origin : {known_repo} of {len(census)}")
    print(f"  workbook rows with a normalized category   : {sum(1 for r in ledger if r['_category'] not in ('', 'UNMAPPED'))} of {len(ledger)}")


if __name__ == "__main__":
    main()
