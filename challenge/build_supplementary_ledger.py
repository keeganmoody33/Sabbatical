"""Build the adversarial supplementary ledger: a row-grain reconciliation.

This supersedes the company-grain comparison in `reconcile.py`, which was a
deliberate weakening and turned out to be too coarse to adjudicate anything.
Company presence answers "did both datasets see this employer". It cannot
answer "does this specific record exist on both sides, and if the two disagree,
which one is right", which is the only question that changes a census.

Row grain is available and was not used. The workbook's `Thread/Dedup Key` is
`Company + Role + Date`, 353 values, zero duplicates. That is a record
identifier, and it joins to `company_canonical + role_as_listed + date_applied`
on this side.

THE LEDGER IS A FULL OUTER JOIN. Every workbook record gets a row. Every
repository record with no workbook counterpart gets a row too, because a
reconciliation that only walks one side measures what the challenger found and
says nothing about what it missed.

MATCHING MIRRORS THE CENSUS MATCHER, INCLUDING ITS REFUSAL. Four ordered tiers,
stopping at the first that yields exactly one candidate, and a tier producing
more than one resolves to `ambiguous` rather than guessing. The direction of
error here is the census matcher's, not `reconcile.py`'s: a wrong row-level
match asserts a disagreement or an agreement that does not exist, so refusing is
safer than merging.

EVERY ROW CARRIES A DISPOSITION AND A REASON. A reconciliation whose output is
prose cannot be audited, and the first version of `CHALLENGE.md` asserted counts
that nothing recomputed. Each disposition below is a decision someone can
overturn by pointing at the row.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adjudication"))
sys.path.insert(0, str(ROOT / "challenge"))

from _common import INTERVIEW_TYPES, is_excluded_event, iso_date, load_csv  # noqa: E402
from ingest_platform import roles_equivalent  # noqa: E402
from reconcile import OPPORTUNITY_CATEGORIES, company_key, equivalent  # noqa: E402

CHALLENGE = ROOT / "challenge"
ADJ = ROOT / "adjudication"

# Tier 1 requires the dates to agree closely. The workbook's date is "date of
# first contact or application", which is not always the submission date, so the
# window is wider than the 7-day duplicate rule but still tight enough that two
# unrelated applications to one company rarely fall inside it.
TIER1_WINDOW_DAYS = 30


def parse_key(key: str) -> tuple[str, str, str]:
    """`Company + Role + Date` into its three parts.

    Split from the right, because company names contain ' + ' (Block+Tackle)
    and roles do not reliably avoid it either. The date is always last and the
    role always second to last.
    """
    parts = [p.strip() for p in key.split(" + ")]
    if len(parts) < 3:
        return (parts[0] if parts else "", "", "")
    return (" + ".join(parts[:-2]), parts[-2], parts[-1])


def day_gap(left: str, right: str) -> int | None:
    a, b = iso_date((left or "")[:10]), iso_date((right or "")[:10])
    if a is None or b is None:
        return None
    return abs((a - b).days)


def load_workbook() -> list[dict]:
    source = {
        r["Thread/Dedup Key"]: r["Normalized Source Category"]
        for r in load_csv(CHALLENGE / "checkpoint__source_classification.csv")
    }
    resolution = {
        r["Thread/Dedup Key"]: r["Role Title Resolution"]
        for r in load_csv(CHALLENGE / "checkpoint__role_classification.csv")
    }
    rows = []
    for r in load_csv(CHALLENGE / "checkpoint__ledger.csv"):
        key = r["Thread/Dedup Key"]
        _company, _role, key_date = parse_key(key)
        rows.append(
            {
                "key": key,
                "company": r["Company"],
                "company_key": company_key(r["Company"]),
                "role": r["Role/Title"],
                "date": r["Date of first contact or application"] or key_date,
                "status": r["Current/Final Status"],
                "interview_count": r["Interview Count"],
                "category": source.get(key, "UNMAPPED"),
                "resolution": resolution.get(key, ""),
                "origin": r["Origin/Source"],
            }
        )
    return rows


def load_repository() -> list[dict]:
    """Census rows plus the opportunity register, so a workbook record matching
    an opportunity reads as a register disagreement rather than as missing."""
    census = {r["application_id"]: r for r in load_csv(ADJ / "applications__adjudicated.csv")}
    rows = []
    for r in load_csv(ADJ / "applications__full_census.csv"):
        rows.append({**r, "_side": "census"})
    seen = {r["application_id"] for r in rows}
    # Opportunity rows never enter the census files, so read them from the
    # coder tables. Cursor first, then bravo for anything cursor did not hold.
    for coder in ("cursor", "bravo"):
        for r in load_csv(ROOT / "coding" / coder / f"applications__{coder}.csv"):
            if r.get("register") == "opportunity" and r["application_id"] not in seen:
                seen.add(r["application_id"])
                rows.append({**r, "_side": "opportunity"})
    for r in rows:
        r["company_key"] = company_key(r["company_canonical"])
        r["_in_census_223"] = r["application_id"] in census
    return rows


def match(workbook: list[dict], repository: list[dict]) -> dict[str, tuple[dict | None, str, list[str]]]:
    """Workbook key to (repository row, match tier, candidate ids).

    Four ordered tiers. A tier returning more than one candidate stops the
    cascade and returns `ambiguous` with every candidate named, on the census
    matcher's rule: a refusal you cannot find later is not conservative.
    """
    by_company: dict[str, list[dict]] = defaultdict(list)
    for r in repository:
        by_company[r["company_key"]].append(r)

    out: dict[str, tuple[dict | None, str, list[str]]] = {}
    for w in workbook:
        candidates = by_company.get(w["company_key"], [])
        if not candidates:
            # Company keys can differ by a legal suffix the stripper missed.
            loose = [r for r in repository if equivalent(w["company_key"], r["company_key"])]
            candidates = loose
        if not candidates:
            out[w["key"]] = (None, "no_company_match", [])
            continue

        tiers = [
            (
                "exact_company_role_date",
                [
                    c for c in candidates
                    if roles_equivalent(w["role"], c["role_as_listed"])
                    and (g := day_gap(w["date"], c["date_applied"])) is not None
                    and g <= TIER1_WINDOW_DAYS
                ],
            ),
            (
                "company_and_role",
                [c for c in candidates if roles_equivalent(w["role"], c["role_as_listed"])],
            ),
            (
                "company_and_unspecified_role",
                [c for c in candidates if c["role_as_listed"] == "unspecified"],
            ),
            ("company_only", candidates),
        ]
        for tier_name, hits in tiers:
            if len(hits) == 1:
                out[w["key"]] = (hits[0], tier_name, [hits[0]["application_id"]])
                break
            if len(hits) > 1:
                out[w["key"]] = (None, f"ambiguous_at_{tier_name}", [c["application_id"] for c in hits])
                break
        else:
            out[w["key"]] = (None, "no_match", [])
    return out


def disposition(w: dict, r: dict | None, tier: str, backfilled: set[str], export_companies: set[str]) -> tuple[str, str]:
    """The decision on this row, and why. This is the adjudication."""
    if r is None:
        if tier.startswith("ambiguous"):
            return ("open_ambiguous", "Matches more than one repository row. Refused rather than guessed.")
        if w["category"] in OPPORTUNITY_CATEGORIES:
            return (
                "declined_opportunity_register",
                "Recruiter or marketplace origin with no submission by the applicant. "
                "Opportunity register here, and never an application denominator.",
            )
        if w["company_key"] in export_companies:
            return (
                "adopted_freeze3_export",
                "Arrived in the census through the LinkedIn formal export ingested at Freeze 3.",
            )
        return (
            "open_workbook_only",
            "The workbook holds this record and this corpus has no counterpart. "
            "Needs an artifact before it can enter the census.",
        )

    if r["_side"] == "opportunity":
        return (
            "register_disagreement",
            f"The workbook counts this record. Here it is `{r['application_id']}` in the opportunity "
            "register, because no submission artifact establishes that the applicant applied.",
        )

    if r["application_id"] in backfilled:
        return (
            "adopted_freeze31_title",
            "Role title backfilled at Freeze 3.1 from this repository's own platform artifacts. "
            "The workbook gives the same title independently.",
        )

    if w["role"] and r["role_as_listed"] == "unspecified":
        return (
            "declined_outside_evidence_title",
            f"The workbook resolves the title as `{w['role']}` from evidence not in this corpus "
            f"({w['resolution'] or 'route unstated'}). It establishes that the company had an opening "
            "by that name in that period, not which opening was applied to.",
        )

    return ("agreed", "Both datasets hold this record and place it in the application register.")


def main() -> None:
    workbook = load_workbook()
    repository = load_repository()
    matches = match(workbook, repository)

    backfilled = {r["application_id"] for r in load_csv(ADJ / "title_backfill.csv")}
    export_companies = {
        company_key(r["Company"])
        for r in load_csv(ROOT / "artifacts/platform/linkedin_job_applications_export.csv")
    }

    rows: list[dict] = []
    matched_ids: set[str] = set()

    for w in workbook:
        r, tier, candidates = matches[w["key"]]
        verdict, reason = disposition(w, r, tier, backfilled, export_companies)
        if r is not None:
            matched_ids.add(r["application_id"])
        rows.append(
            {
                "side": "both" if r is not None else "workbook_only",
                "workbook_key": w["key"],
                "workbook_company": w["company"],
                "workbook_role": w["role"],
                "workbook_date": w["date"],
                "workbook_status": w["status"],
                "workbook_category": w["category"],
                "workbook_title_resolution": w["resolution"],
                "application_id": r["application_id"] if r else "",
                "repository_role": r["role_as_listed"] if r else "",
                "repository_register": (r["register"] if r else ""),
                "repository_evidence_tier": r["evidence_tier"] if r else "",
                "repository_terminal_outcome": r["terminal_outcome"] if r else "",
                "in_census_223": ("yes" if r and r["_in_census_223"] else "no") if r else "",
                "match_tier": tier,
                "candidate_application_ids": ";".join(candidates) if tier.startswith("ambiguous") else "",
                "disposition": verdict,
                "disposition_reason": reason,
            }
        )

    # The reverse direction. A reconciliation that walks one side only measures
    # what the challenger found and is silent on what it missed.
    for r in repository:
        if r["application_id"] in matched_ids:
            continue
        in_census = r["_in_census_223"]
        rows.append(
            {
                "side": "repository_only",
                "workbook_key": "",
                "workbook_company": "",
                "workbook_role": "",
                "workbook_date": "",
                "workbook_status": "",
                "workbook_category": "",
                "workbook_title_resolution": "",
                "application_id": r["application_id"],
                "repository_role": r["role_as_listed"],
                "repository_register": r["register"],
                "repository_evidence_tier": r["evidence_tier"],
                "repository_terminal_outcome": r["terminal_outcome"],
                "in_census_223": "yes" if in_census else "no",
                "match_tier": "",
                "candidate_application_ids": "",
                "disposition": "repository_only_census" if in_census else "repository_only_non_census",
                "disposition_reason": (
                    "Held here with employer-side or platform evidence and absent from the workbook."
                    if in_census
                    else "Opportunity register or platform-only row here, absent from the workbook."
                ),
            }
        )

    fields = list(rows[0].keys())
    path = CHALLENGE / "supplementary_ledger.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (r["side"], r["workbook_company"] or r["application_id"])))
    print(f"wrote {path.relative_to(ROOT)} ({len(rows)} rows)")

    print(f"\nworkbook records: {len(workbook)}   repository records: {len(repository)}")
    print("\nmatch tiers:")
    for k, v in Counter(r["match_tier"] for r in rows if r["match_tier"]).most_common():
        print(f"  {v:4d}  {k}")
    print("\ndispositions:")
    for k, v in Counter(r["disposition"] for r in rows).most_common():
        print(f"  {v:4d}  {k}")


if __name__ == "__main__":
    main()
