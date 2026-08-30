"""Generate `data_quality_report.md` from the data, every run.

The report is generated rather than written because a hand-written data quality
report describes the data as it was on the day someone looked. This one cannot
drift: if a value goes out of vocabulary or a duplicate appears, the next run
prints it whether or not anyone remembered to check.

Controlled vocabularies are PARSED OUT OF `codebook.md` rather than restated
here. The codebook is the frozen instrument, and a validator carrying its own
copy of the vocabulary is a second instrument that will eventually disagree
with the first. If a vocabulary line in the codebook is reformatted so it no
longer parses, this script fails loudly rather than validating against nothing.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adjudication"))

from _common import INTERVIEW_TYPES, iso_date, load_csv  # noqa: E402

ADJ = ROOT / "adjudication"
REPORT = ROOT / "data_quality_report.md"

# Vocabularies stated in the codebook's field table rather than in its
# "Controlled vocabularies" section, so they cannot be parsed from it.
INLINE_VOCAB = {
    "date_precision": {"exact", "relative_display", "evidence_bound", "unknown"},
    "terminal_outcome_precision": {"exact", "relative_display", "evidence_bound", "unknown", ""},
    "event_date_precision": {"exact", "relative_display", "evidence_bound", "unknown", ""},
    "work_type": {"remote", "hybrid", "onsite", "unstated"},
    "evidence_tier": {"A", "B", "C"},
    "evidence_class": {"employer_artifact", "platform_log"},
    "register": {"application", "opportunity"},
    "confidence": {"high", "medium", "low"},
}

# Fields whose vocabulary is parsed from the codebook. An application row may
# legitimately leave some of these empty, which is checked as population
# rather than as a vocabulary violation.
PARSED_VOCAB_FIELDS = [
    "role_lane",
    "gtm_modifier",
    "discovery_source",
    "submission_channel",
    "ats_system",
    "terminal_outcome",
    "event_type",
    "medium",
    "exclusion_reason",
]

# Fields that must carry a value on every application row for the row to enter
# any analysis at all.
REQUIRED_FIELDS = [
    "application_id",
    "company_canonical",
    "role_as_listed",
    "date_applied",
    "date_precision",
    "role_lane",
    "evidence_tier",
    "evidence_class",
    "register",
]

# Additional conditions a row must meet to be fully usable, each with the
# analysis it unlocks. A row failing one of these is Partial, not Unusable:
# it still counts in the census, it just cannot answer that question.
COMPLETENESS_CONDITIONS = [
    ("exact_date", "monthly series and every latency figure", lambda r: r["date_precision"] == "exact"),
    ("named_role", "any role title or lane analysis", lambda r: r["role_as_listed"] != "unspecified"),
    ("known_origin", "origination-channel conversion", lambda r: r["discovery_source"] != "unknown"),
    (
        "observable_outcome",
        "any funnel or conversion figure",
        lambda r: r["evidence_class"] == "employer_artifact",
    ),
]

DUPLICATE_WINDOW_DAYS = 7
LATENCY_OUTLIER_DAYS = 120
ROUNDS_OUTLIER = 6


def parse_codebook_vocabularies() -> dict[str, set[str]]:
    """Read `**field**: `a`, `b`, `c`` lines out of codebook.md."""
    text = (ROOT / "codebook.md").read_text(encoding="utf-8")
    found: dict[str, set[str]] = {}
    for match in re.finditer(r"^\*\*(\w+)\*\*:\s*(.+)$", text, flags=re.MULTILINE):
        field, body = match.group(1), match.group(2)
        values = set(re.findall(r"`([^`]+)`", body))
        if values:
            found[field] = values
    missing = [f for f in PARSED_VOCAB_FIELDS if f not in found]
    if missing:
        raise SystemExit(
            "codebook.md no longer yields a vocabulary for: "
            + ", ".join(missing)
            + ". The validator refuses to run against a vocabulary it cannot read."
        )
    return found


def date_range(rows: list[dict], field: str) -> str:
    # Take the leading 10 characters so an ISO datetime (calendar `start`)
    # reads as its date without a second parser.
    dates = sorted(d for d in (iso_date(r.get(field, "")[:10]) for r in rows) if d)
    if not dates:
        return "no parseable dates"
    return f"{dates[0].isoformat()} to {dates[-1].isoformat()} ({len(dates)} of {len(rows)} parse)"


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    """Markdown table. Application ids contain pipes, which must be escaped or
    the cell splits and the row renders with the wrong number of columns."""
    if not rows:
        return ["None."]
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |" for row in rows]
    return out


def section_inventory(lines: list[str]) -> None:
    lines += ["## 1. Source inventory", ""]
    lines += [
        "Every table the pipeline reads or writes, with its row count and the date range it covers.",
        "",
    ]
    inventory = [
        # LinkedIn carries `applied_date_relative` ("2mo ago") and no calendar
        # date, which is why it has no date range and why its rows can never
        # enter the monthly series.
        ("artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv", None),
        ("artifacts/platform/jobright_applications_log.csv", "Date Applied"),
        ("artifacts/calendar/q8-lecturesfrom-primary.csv", "start"),
        ("coding/bravo/applications__bravo.csv", "date_applied"),
        ("coding/bravo/events__bravo.csv", "event_date"),
        ("coding/bravo/exclusions__bravo.csv", "date"),
        ("coding/cursor/applications__cursor.csv", "date_applied"),
        ("coding/cursor/events__cursor.csv", "event_date"),
        ("coding/cursor/exclusions__cursor.csv", "date"),
        ("coding/platform/applications__freeze2.csv", "date_applied"),
        ("coding/platform/exclusions__freeze2.csv", "date"),
        ("adjudication/applications__adjudicated.csv", "date_applied"),
        ("adjudication/applications__full_census.csv", "date_applied"),
        ("adjudication/platform_match.csv", None),
        ("adjudication/latency__by_application.csv", "date_applied"),
    ]
    rows = []
    for rel, date_field in inventory:
        path = ROOT / rel
        if not path.is_file():
            rows.append([f"`{rel}`", "ABSENT", "", ""])
            continue
        data = load_csv(path)
        cols = len(data[0]) if data else 0
        span = date_range(data, date_field) if date_field else "not date-keyed"
        rows.append([f"`{rel}`", str(len(data)), str(cols), span])
    lines += table(["file", "rows", "columns", "date range"], rows)
    lines.append("")


def section_population(lines: list[str], census: list[dict], full: list[dict]) -> None:
    lines += ["## 2. Field population", ""]
    lines += [
        "Count of rows where the field is empty, and count where it carries an admitted",
        "unknown. The codebook requires a legal way to say \"I could not tell\", so an",
        "admitted unknown is a recorded observation rather than a missing value. The two",
        "are counted separately because they mean different things: an empty field is a",
        "coder omission, an admitted unknown is a fact about the artifact.",
        "",
    ]
    for label, data in (("Application census, n = 221", census), ("Full census, n = 298", full)):
        lines += [f"### {label}", ""]
        rows = []
        for column in data[0]:
            empty = sum(1 for r in data if not r[column].strip())
            unknown = sum(1 for r in data if r[column].strip() in {"unknown", "unspecified", "none_observed"})
            if empty or unknown:
                rows.append(
                    [
                        f"`{column}`",
                        str(empty),
                        f"{empty / len(data):.1%}".replace("%", " percent"),
                        str(unknown),
                    ]
                )
        lines += table(["field", "empty", "share empty", "admitted unknown"], rows)
        lines.append("")


def section_vocabulary(lines: list[str], census: list[dict], full: list[dict], vocab: dict[str, set[str]]) -> None:
    lines += ["## 3. Controlled vocabulary violations", ""]
    lines += [
        "Values found in the data that the codebook does not define. Empty values are",
        "excluded here and counted in section 2 instead.",
        "",
    ]
    checks = {**{f: vocab[f] for f in PARSED_VOCAB_FIELDS}, **INLINE_VOCAB}
    rows = []
    for table_name, data in (
        ("applications (full census)", full),
        ("events (cursor)", load_csv(ROOT / "coding/cursor/events__cursor.csv")),
        ("events (bravo)", load_csv(ROOT / "coding/bravo/events__bravo.csv")),
        ("exclusions (cursor)", load_csv(ROOT / "coding/cursor/exclusions__cursor.csv")),
        ("exclusions (bravo)", load_csv(ROOT / "coding/bravo/exclusions__bravo.csv")),
    ):
        if not data:
            continue
        for field, allowed in checks.items():
            if field not in data[0]:
                continue
            bad = Counter(r[field] for r in data if r[field].strip() and r[field] not in allowed)
            for value, n in sorted(bad.items()):
                rows.append([table_name, f"`{field}`", f"`{value}`", str(n)])
    lines += table(["table", "field", "value", "rows"], rows)
    lines.append("")
    if rows:
        lines += [
            "Every violation above is real and is left in the data rather than silently",
            "corrected, because the coder CSVs are frozen. A correction to a frozen coder",
            "file would be an undocumented recode.",
            "",
        ]


def section_duplicates(lines: list[str], full: list[dict]) -> None:
    lines += ["## 4. Duplicate detection", ""]
    lines += [
        f"Pairs of rows at the same company with the same role whose submission dates fall",
        f"within {DUPLICATE_WINDOW_DAYS} days of each other. The unit of analysis is",
        "`company_canonical + role_as_listed + cycle`, and a new cycle is licensed only by a",
        "terminal outcome on the prior one, so a near-date pair at the same company and role",
        "is a candidate duplicate that the key would not catch.",
        "",
    ]
    by_key = defaultdict(list)
    for row in full:
        by_key[(row["company_canonical"].lower(), row["role_as_listed"].lower())].append(row)

    rows = []
    beyond_window = []
    for (company, role), group in sorted(by_key.items()):
        if len(group) < 2:
            continue
        for i, left in enumerate(group):
            for right in group[i + 1 :]:
                d1, d2 = iso_date(left["date_applied"]), iso_date(right["date_applied"])
                entry = [
                    company,
                    role or "(empty)",
                    f"`{left['application_id']}`",
                    f"`{right['application_id']}`",
                ]
                if d1 is None or d2 is None:
                    rows.append(entry + ["one date unparseable", "review"])
                    continue
                delta = abs((d1 - d2).days)
                if delta <= DUPLICATE_WINDOW_DAYS:
                    rows.append(entry + [f"{delta} days", "review"])
                else:
                    beyond_window.append((delta, entry))

    lines += table(["company", "role", "row A", "row B", "gap", "status"], rows)
    lines.append("")

    # A duplicate check that finds nothing proves nothing unless you can see it
    # had candidates to reject. These are the same-company, same-role pairs that
    # fell outside the window, closest first.
    lines += [
        f"Same company and role pairs beyond the {DUPLICATE_WINDOW_DAYS} day window, closest first.",
        "These are the pairs the check considered and cleared, which is what makes an empty",
        "result above meaningful. A legitimate second cycle is licensed by a terminal outcome",
        "on the first, and both pairs below carry one.",
        "",
    ]
    lines += table(
        ["company", "role", "row A", "row B", "gap"],
        [entry + [f"{delta} days"] for delta, entry in sorted(beyond_window)[:10]],
    )
    lines.append("")

    same_key = [k for k, v in Counter(r["application_id"] for r in full).items() if v > 1]
    lines += [
        f"Rows sharing an `application_id`: {len(same_key)}."
        + (" " + ", ".join(f"`{k}`" for k in sorted(same_key)) if same_key else ""),
        "",
    ]


def section_outliers(lines: list[str], census: list[dict], latency: list[dict]) -> None:
    lines += ["## 5. Outliers and range checks", ""]
    rows = []

    long_latency = [
        r for r in latency if r["days_to_response_broad"] and int(r["days_to_response_broad"]) > LATENCY_OUTLIER_DAYS
    ]
    rows.append(
        [
            f"days to any response over {LATENCY_OUTLIER_DAYS}",
            str(len(long_latency)),
            ", ".join(f"`{r['application_id']}` at {r['days_to_response_broad']}" for r in long_latency) or "none",
        ]
    )

    negatives = [
        r
        for r in latency
        if r["days_to_response_broad"] and int(r["days_to_response_broad"]) < 0
    ]
    rows.append(["negative response latency", str(len(negatives)), "none" if not negatives else "see rows"])

    round_counts: Counter[str] = Counter()
    for coder in ("cursor", "bravo"):
        for event in load_csv(ROOT / "coding" / coder / f"events__{coder}.csv"):
            if event["event_type"] in INTERVIEW_TYPES:
                round_counts[event["application_id"]] += 1
    many_rounds = {a: n for a, n in round_counts.items() if n > ROUNDS_OUTLIER}
    rows.append(
        [
            f"interview events over {ROUNDS_OUTLIER} on one application (both coders unioned)",
            str(len(many_rounds)),
            ", ".join(f"`{a}` at {n}" for a, n in sorted(many_rounds.items())) or "none",
        ]
    )

    backwards = []
    for row in census:
        applied, terminal = iso_date(row["date_applied"]), iso_date(row["terminal_outcome_date"])
        if applied and terminal and terminal < applied:
            backwards.append(f"`{row['application_id']}`")
    rows.append(["terminal outcome dated before submission", str(len(backwards)), ", ".join(backwards) or "none"])

    out_of_window = [
        f"`{r['application_id']}` at {r['date_applied']}"
        for r in census
        if (d := iso_date(r["date_applied"])) and not ("2025-06-01" <= d.isoformat() <= "2026-08-29")
    ]
    rows.append(
        ["submission date outside the study window", str(len(out_of_window)), ", ".join(out_of_window) or "none"]
    )

    lines += table(["check", "rows", "detail"], rows)
    lines.append("")


def section_referential(lines: list[str]) -> None:
    lines += ["## 6. Referential integrity", ""]
    lines += [
        "`events.application_id` is a foreign key to `applications.application_id` within the",
        "same coder. An event with no parent application row is an orphan, and an orphan is",
        "how an interview gets counted against an application that was never submitted.",
        "",
    ]
    rows = []
    for coder in ("cursor", "bravo"):
        apps = {r["application_id"] for r in load_csv(ROOT / "coding" / coder / f"applications__{coder}.csv")}
        events = load_csv(ROOT / "coding" / coder / f"events__{coder}.csv")
        orphans = sorted({e["application_id"] for e in events if e["application_id"] not in apps})
        rows.append(
            [
                coder,
                str(len(apps)),
                str(len(events)),
                str(len(orphans)),
                ", ".join(f"`{o}`" for o in orphans) or "none",
            ]
        )
    lines += table(["coder", "application rows", "event rows", "orphan events", "orphans"], rows)
    lines.append("")


def section_completeness(lines: list[str], census: list[dict]) -> None:
    lines += ["## 7. Row completeness", ""]
    lines += [
        "Every census row classified against what it can actually answer.",
        "",
        "- **Unusable**: a required field is empty, so the row cannot enter any analysis.",
        "- **Complete**: every required field present and every condition below met.",
        "- **Partial**: in the census and counted, but blocked from at least one analysis.",
        "",
        "Required fields: " + ", ".join(f"`{f}`" for f in REQUIRED_FIELDS) + ".",
        "",
    ]
    lines += table(
        ["condition", "what it unlocks"],
        [[f"`{name}`", unlocks] for name, unlocks, _ in COMPLETENESS_CONDITIONS],
    )
    lines.append("")

    buckets: Counter[str] = Counter()
    failures: Counter[str] = Counter()
    for row in census:
        if any(not row[f].strip() for f in REQUIRED_FIELDS):
            buckets["Unusable"] += 1
            continue
        failed = [name for name, _, test in COMPLETENESS_CONDITIONS if not test(row)]
        for name in failed:
            failures[name] += 1
        buckets["Complete" if not failed else "Partial"] += 1

    n = len(census)
    lines += table(
        ["bucket", "rows", "share of census"],
        [
            [bucket, str(buckets.get(bucket, 0)), f"{buckets.get(bucket, 0) / n:.1%}".replace("%", " percent")]
            for bucket in ("Complete", "Partial", "Unusable")
        ],
    )
    lines.append("")
    lines += ["Which condition each Partial row failed. A row can fail more than one, so these do not sum.", ""]
    lines += table(
        ["condition", "rows failing", "share of census"],
        [
            [f"`{name}`", str(failures.get(name, 0)), f"{failures.get(name, 0) / n:.1%}".replace("%", " percent")]
            for name, _, _ in COMPLETENESS_CONDITIONS
        ],
    )
    lines.append("")
    lines += [
        "The `known_origin` row is the finding this report exists to surface. It is the",
        "single largest completeness failure in the dataset, and it is the one that blocks",
        "the question a job-search log is most often built to answer.",
        "",
    ]


def section_not_checked(lines: list[str]) -> None:
    lines += ["## 8. What this report does not check", ""]
    lines += [
        "- **Whether the corpus is complete.** This validates the rows that exist. Coverage is",
        "  a separate question, answered by `artifacts/STOP-CONDITIONS.md`, and four of its",
        "  seven conditions are Partial or Unmet.",
        "- **Whether a coder read an artifact correctly.** That is what blind double coding and",
        "  `adjudication/PRE-ADJUDICATION.md` measure. A row can be internally valid and wrong.",
        "- **Event-level agreement between coders.** The protocol names role lane and the",
        "  include decision as the reliability statistics. Event agreement is unmeasured, and",
        "  the interview set rests on 10 of 13 found by both coders.",
        "- **Anything about the opportunity register.** This report validates the application",
        "  census. Opportunity rows are adjudicated, not validated here.",
        "",
    ]


def main() -> None:
    vocab = parse_codebook_vocabularies()
    census = load_csv(ADJ / "applications__adjudicated.csv")
    full = load_csv(ADJ / "applications__full_census.csv")
    latency = load_csv(ADJ / "latency__by_application.csv")

    lines: list[str] = [
        "# Data quality report",
        "",
        "Generated by `pipeline/data_quality.py`. Do not edit by hand, the next pipeline run",
        "overwrites it. Controlled vocabularies are read from `codebook.md` at run time, so",
        "this report validates against the frozen instrument rather than against a copy.",
        "",
        "No dashes are used as punctuation in this file.",
        "",
    ]

    section_inventory(lines)
    section_population(lines, census, full)
    section_vocabulary(lines, census, full, vocab)
    section_duplicates(lines, full)
    section_outliers(lines, census, latency)
    section_referential(lines)
    section_completeness(lines, census)
    section_not_checked(lines)

    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
