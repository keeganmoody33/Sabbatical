"""Apply named adjudication decisions. Do not edit coder CSVs."""

from __future__ import annotations

import csv
from pathlib import Path

from _common import EVENT_EXCLUSIONS, is_excluded_event

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

    out_dir = ROOT / "adjudication"
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

1. The Hog GTM Engineer. Bravo: opportunity. Cursor: application. Adjudicated **opportunity**. No ATS or sent-mail submission artifact. Interview plus take-home do not mint an application row.
2. BX Studio unspecified. Bravo: application. Cursor: opportunity. Adjudicated **opportunity**. Video forwarded to a hiring manager is not a submission.
3. Weave GTM Engineer, 2026. Adjudicated **opportunity**, and separated from the 2025 Business Development Manager application it had been attached to. Same rule as The Hog: an interview with no submission artifact does not mint an application row. See the corrections below.

## Corrections applied after coding

These are named changes to coder output, applied here rather than by editing the coder CSVs. Both were disclosed in `knowledge/protocol.md` and `paper/DEFECTS.md` on the date they were made.

Events excluded from the interview derivation:

{chr(10).join(f"- `{a}`, `{t}` dated {d}. {reason}" for a, t, d, reason in EVENT_EXCLUSIONS)}

Terminal outcomes corrected:

{chr(10).join(f"- `{a}` set to `{v[0]}` dated {v[1]}. {v[2]}" for a, v in terminal_overrides.items())}

The Weave role title, the counterparty, and the inbound origination are author recall, not artifact. The corpus establishes only that an interview at Weave happened and was declined on 2026-08-18, from `gth_0339a17e3860d167`. Under `prompts/extraction.md` rule 8 recall is not recorded as evidence, so none of those three is written into a structured field.

## Alias merges (same process, different keys)

Anduril / Anduril Industries; Attentive unspecified c1 / GTM Engineer c1; HartleyCo / Bluejay Founding GTM; Exa / Exa Labs; IBM title with and without Confluent in the role string; Manifold / Manifold AI; Tekion comma in title; Valsoft GTM Engineer / GTM Engineer DockMaster.

Productboard GTM Engineer vs Associate GTM Engineer stays one row (the Associate title already in the dual-agreement set). Talentpluto GTM Engineer vs Go-to-Market Engineer is one opening, not two. Pindrop unspecified c2 is not a new cycle: no terminal on c1.

## Uniques included

From bravo: Glean GTM Engineer Marketing (Greenhouse 2026-03-23); Jobright.ai Product Manager Early Career (2026-03-31).
From cursor: Agroknow North America Sales; Classet Head of GTM; jobmail.io Growth Lead; Stellar Substitute; Switchyards Digital Product Builder.

## Opportunity, not census

WorkOS (TopHire). Mercor Growth Strategist / GTM Engineer contract path. ThriveLink referral. Dexian. Luzmo. Glytec. SmartMode AI. Crossing Hurdles / Montauk Capital. micro1 client submissions. Pinterest June 2025 referral-accept messages. Weave GTM Engineer 2026, inbound, interview evidenced by the 2026-08-18 decline with no submission artifact.

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
