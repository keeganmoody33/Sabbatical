"""Apply named adjudication decisions. Do not edit coder CSVs."""

from __future__ import annotations

import csv
from pathlib import Path

from _common import EVENT_EXCLUSIONS, is_excluded_event
from ingest_platform import norm_company, role_lane as derive_role_lane

ROOT = Path(__file__).resolve().parents[1]
INTERVIEW_TYPES = {
    "recruiter_screen",
    "hiring_manager_interview",
    "panel",
    "technical_exercise",
    "final_round",
}


def load_apps(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_events(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def key(row: dict[str, str]) -> str:
    company = (row.get("company_canonical") or "").strip().lower()
    role = (row.get("role_as_listed") or "").strip().lower()
    cycle = (row.get("cycle") or "1").strip() or "1"
    return f"{company}|{role}|c{cycle}"


# Platform artifacts that carry a role title. Both are committed inputs, not
# pipeline outputs, so they are readable at census-build time.
TITLE_SOURCES = [
    ("artifacts/platform/linkedin_job_applications_export.csv", "Company", "Role/Title"),
    ("artifacts/platform/jobright_applications_log.csv", "Company", "Role Applied For"),
]


def platform_titles() -> dict[str, tuple[str, str]]:
    """Company to (title, source file), for companies with exactly one title.

    A receipt that omits the role is coded `unspecified` and never guessed, per
    counting rule 8, and that was correct: the Gmail artifact genuinely does not
    name it. But the platform exports sitting in `artifacts/platform/` DO name
    it for some of those same companies, and the census was never reading them.
    A title present in the committed corpus and absent from the census is a gap
    in this pipeline, not an admitted unknown.

    A company carrying more than one distinct platform title is REFUSED rather
    than guessed at, on the same rule the record matcher uses: if you cannot
    state which opening a row is, you cannot name it.
    """
    seen: dict[str, set[str]] = {}
    origin: dict[str, tuple[str, str]] = {}
    for rel, company_col, title_col in TITLE_SOURCES:
        path = ROOT / rel
        if not path.exists():
            continue
        for row in load_apps(path):
            company = norm_company(row.get(company_col, ""))
            title = (row.get(title_col) or "").strip()
            if not company or not title:
                continue
            seen.setdefault(company, set()).add(title)
            origin.setdefault(company, (title, path.name))
    return {c: origin[c] for c, titles in seen.items() if len(titles) == 1}


def main() -> None:
    bravo = {key(r): r for r in load_apps(ROOT / "coding/bravo/applications__bravo.csv")}
    cursor = {key(r): r for r in load_apps(ROOT / "coding/cursor/applications__cursor.csv")}
    both = set(bravo) & set(cursor)
    both_app = [
        k
        for k in both
        if bravo[k].get("register") == "application"
        and cursor[k].get("register") == "application"
    ]

    # Merges: same process, different keys. Take the cursor row when it exists.
    merge_cursor_keys = [
        "anduril industries|technical operations engineer, launched effects|c1",
        "attentive|gtm engineer|c1",
        "hartleyco|founding gtm|c1",
        "exa|growth lead|c1",
        "ibm|manager, applied ai & gtm systems|c1",
        "manifold ai|growth marketing manager|c1",
        "tekion|senior manager inside sales|c1",
        "valsoft|gtm engineer, dockmaster|c1",
    ]
    cursor_uniques_include = [
        "agroknow|north america sales|c1",
        "classet|head of gtm|c1",
        "jobmail.io|growth lead|c1",
        "stellar substitute|unspecified|c1",
        "switchyards|digital product builder|c1",
    ]
    bravo_uniques_include = [
        "glean|gtm engineer, marketing|c1",
        "jobright.ai|product manager (early career)|c1",
    ]

    # Freeze 3 register reversals, 2026-08-30.
    #
    # These two were the ONLY include-or-exclude disagreements between the blind
    # coders, the pair that produced the include kappa of 0.7452. Both were
    # adjudicated to the opportunity register on one stated ground: no submission
    # artifact existed anywhere in the corpus.
    #
    # The LinkedIn formal export, ingested at Freeze 3, contains a submission row
    # for each, both dated before the process events already coded here:
    #   The Hog   applied 2026-06-04, interview invitation 2026-06-15, gap 11 days
    #   BX Studio applied 2026-04-06, employer acknowledgment 2026-04-08, gap 2 days
    #
    # The RULE is unchanged and is the same one that sent them out: an interview
    # with no submission does not mint an application row. Its premise is now
    # false, so the rule reverses the outcome by itself. This is what the
    # `what_would_promote_it` column on every exclusion exists for.
    #
    # Each row is taken from the coder who read it as an application, so the
    # surviving row is a real coder's judgement rather than one assembled here.
    # See challenge/CHALLENGE.md section 1.2.
    freeze3_reversals = [
        ("the hog|gtm engineer|c1", cursor, "cursor_unique"),
        ("bx studio|unspecified|c1", bravo, "bravo_unique"),
    ]

    # Terminal outcomes corrected after coding, by name and with a reason.
    # application_id -> (terminal_outcome, terminal_outcome_date, reason)
    terminal_overrides = {
        "weave|business-development-manager|c1": (
            "rejected_no_interview",
            "2025-07-31",
            "The interview belonged to a separate opening, so this application was "
            "declined without one. Reverts to bravo's coding; cursor and bravo "
            "disagreed on this field and adjudication did not cover it.",
        ),
    }

    titles = platform_titles()
    backfilled: list[dict[str, str]] = []
    census_rows: list[dict[str, str]] = []
    seen = set()

    def add(row: dict[str, str], source: str, decision: str) -> None:
        k = key(row)
        if k in seen:
            return
        seen.add(k)
        out = dict(row)
        override = terminal_overrides.get(out.get("application_id", ""))
        if override:
            outcome, outcome_date, _ = override
            out["terminal_outcome"] = outcome
            out["terminal_outcome_date"] = outcome_date
            out["terminal_outcome_precision"] = "exact"
            decision = "adjudicated_terminal_outcome"
        # Backfill a role title from the platform artifacts when the Gmail
        # receipt omitted one. application_id is NOT regenerated: the events
        # tables join on it, so a new slug would orphan every event on the row.
        # The id keeps the slug it was coded with, and role_title_source records
        # that the title and the id no longer agree.
        out["role_title_source"] = ""
        if out.get("role_as_listed") == "unspecified":
            found = titles.get(norm_company(out.get("company_canonical", "")))
            if found:
                title, source_file = found
                lane, modifier = derive_role_lane(title)
                out["role_as_listed"] = title
                out["role_lane"] = lane
                out["gtm_modifier"] = modifier if lane == "explicit_gtm_engineering" else ""
                # Corroborated across two artifacts is exactly evidence tier B.
                out["evidence_tier"] = "B"
                out["role_title_source"] = source_file
                out["notes"] = (out.get("notes", "") + f" Role title backfilled from {source_file}; the Gmail receipt omitted it. application_id retains its original slug.").strip()
                backfilled.append({
                    "application_id": out["application_id"],
                    "company_canonical": out["company_canonical"],
                    "role_as_listed": title,
                    "role_lane": lane,
                    "source_file": source_file,
                })
                decision = decision + "+title_backfill"
        out["adjudication_source"] = source
        out["adjudication_note"] = decision
        census_rows.append(out)

    for k in sorted(both_app):
        add(cursor[k], "both", "both_coders_application")
    for k in merge_cursor_keys:
        add(cursor[k], "merge", "alias_or_title_normalization")
    for k in cursor_uniques_include:
        add(cursor[k], "cursor_unique", "adjudicated_include")
    for k in bravo_uniques_include:
        add(bravo[k], "bravo_unique", "adjudicated_include")
    for k, source_rows, source_label in freeze3_reversals:
        add(source_rows[k], source_label, "freeze3_register_reversal_submission_artifact")

    out_dir = ROOT / "adjudication"
    with (out_dir / "title_backfill.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["application_id", "company_canonical", "role_as_listed", "role_lane", "source_file"],
        )
        writer.writeheader()
        writer.writerows(sorted(backfilled, key=lambda r: r["application_id"]))

    fields = list(census_rows[0].keys())
    path = out_dir / "applications__adjudicated.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(census_rows)

    # Interviews: union of event types on these application_ids plus bravo ids for bravo-unique rows
    census_ids = {r["application_id"] for r in census_rows}
    interviewed: set[str] = set()
    for coder in ("cursor", "bravo"):
        for event in load_events(ROOT / f"coding/{coder}/events__{coder}.csv"):
            if (event.get("event_type") or "") in INTERVIEW_TYPES:
                if is_excluded_event(event):
                    continue
                if event.get("application_id") in census_ids:
                    interviewed.add(event["application_id"])

    exact = [r for r in census_rows if r.get("date_precision") == "exact"]
    monthly: dict[str, int] = {}
    for row in exact:
        date = row.get("date_applied") or ""
        if len(date) >= 7:
            monthly[date[:7]] = monthly.get(date[:7], 0) + 1

    n = len(census_rows)
    n_int = len(interviewed)
    rate = n_int / n if n else 0
    summary = f"""# Adjudication

Coders compared: bravo and cursor. Alpha CSVs were not present when this pass ran.

## Pre-adjudication (raw match keys)

- bravo rows: {len(bravo)}
- cursor rows: {len(cursor)}
- intersection: {len(both)}
- both `register = application`: {len(both_app)}
- role_lane percent agreement: 0.9621
- role_lane Cohen's kappa: 0.9510
- include percent agreement: 0.9905
- include kappa: 0.7452 (two disagreements on a rare class)

## Register disagreements (intersection)

1. The Hog GTM Engineer. Bravo: opportunity. Cursor: application. Adjudicated **opportunity** at Freeze 1, on the ground that no ATS or sent-mail submission artifact existed. **Reversed at Freeze 3 to application**: the LinkedIn formal export carries a submission dated 2026-06-04, eleven days before the interview invitation.
2. BX Studio unspecified. Bravo: application. Cursor: opportunity. Adjudicated **opportunity** at Freeze 1, on the ground that a video forwarded to a hiring manager is not a submission. **Reversed at Freeze 3 to application**: the export carries a submission dated 2026-04-06, two days before the employer acknowledgment.
3. Weave GTM Engineer, 2026. Adjudicated **opportunity**, and separated from the 2025 Business Development Manager application it had been attached to. Same rule as The Hog: an interview with no submission artifact does not mint an application row. See the corrections below.

## Corrections applied after coding

These are named changes to coder output, applied here rather than by editing the coder CSVs. Both were disclosed in `knowledge/protocol.md` and `paper/DEFECTS.md` on the date they were made.

Events excluded from the interview derivation:

{chr(10).join(f"- `{a}`, `{t}` dated {d}. {reason}" for a, t, d, reason in EVENT_EXCLUSIONS)}

Terminal outcomes corrected:

{chr(10).join(f"- `{a}` set to `{v[0]}` dated {v[1]}. {v[2]}" for a, v in terminal_overrides.items())}

The Weave role title, the counterparty, and the inbound origination are author recall, not artifact. The corpus establishes only that an interview at Weave happened and was declined on 2026-08-18, from `gth_0339a17e3860d167`. Under `prompts/extraction.md` rule 8 recall is not recorded as evidence, so none of those three is written into a structured field.

## Freeze 3 register reversals, 2026-08-30

These two were the only include-or-exclude disagreements between the blind coders, the pair that produced the include kappa of 0.7452. Both went to the opportunity register on one stated ground: no submission artifact existed in the corpus. The LinkedIn formal export supplies one for each.

The rule did not change. Its premise did. An interview with no submission still does not mint an application row; a submission now exists. Each row is taken from the coder who read it as an application, so the surviving row is a real coder's judgement rather than one assembled during adjudication.

Consequence: census 221 becomes 223, interviewed applications 13 becomes 14, and the rate 13/221 becomes 14/223. See `challenge/CHALLENGE.md` section 1.2 and `paper/DEFECTS.md`.

## Alias merges (same process, different keys)

Anduril / Anduril Industries; Attentive unspecified c1 / GTM Engineer c1; HartleyCo / Bluejay Founding GTM; Exa / Exa Labs; IBM title with and without Confluent in the role string; Manifold / Manifold AI; Tekion comma in title; Valsoft GTM Engineer / GTM Engineer DockMaster.

Productboard GTM Engineer vs Associate GTM Engineer stays one row (the Associate title already in the dual-agreement set). Talentpluto GTM Engineer vs Go-to-Market Engineer is one opening, not two. Pindrop unspecified c2 is not a new cycle: no terminal on c1.

## Uniques included

From bravo: Glean GTM Engineer Marketing (Greenhouse 2026-03-23); Jobright.ai Product Manager Early Career (2026-03-31).
From cursor: Agroknow North America Sales; Classet Head of GTM; jobmail.io Growth Lead; Stellar Substitute; Switchyards Digital Product Builder.

## Opportunity, not census

WorkOS (TopHire). Mercor Growth Strategist / GTM Engineer contract path. ThriveLink referral. Dexian. Luzmo. Glytec. SmartMode AI. Crossing Hurdles / Montauk Capital. micro1 client submissions. Pinterest June 2025 referral-accept messages. Weave GTM Engineer 2026, inbound, interview evidenced by the 2026-08-18 decline with no submission artifact.

The Hog and BX Studio were on this list until Freeze 3. They are not any more, and the reason is an artifact rather than a change of mind. WorkOS and the 2026 Weave opening remain here because no submission artifact has been found for either.

## Adjudicated application census

- n = **{n}**
- evidence_class: employer_artifact (platform_log stratum empty; LinkedIn export absent)
- full census equals the employer_artifact stratum in this freeze
- interviewed applications (derived from events, either coder): {n_int}
- application-to-interview rate: {n_int}/{n} = {rate:.4f}
- exact-date n: {len(exact)}; non-exact n: {n - len(exact)}
- exact-date monthly: {dict(sorted(monthly.items()))}

This {n} is not 247. It is not a completeness percentage. Capture recapture remains unmeasured.

## 212 to 163

Still undocumented. Workbooks absent.
"""
    (out_dir / "ADJUDICATION.md").write_text(summary, encoding="utf-8")
    print(f"census={n} interviewed={n_int} exact={len(exact)}")


if __name__ == "__main__":
    main()
