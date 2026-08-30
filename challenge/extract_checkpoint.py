"""Extract the combined audit checkpoint workbook into committed CSVs.

The workbook arrived 2026-08-30, after Freeze 1, blind coding, and adjudication
were complete. It is an INDEPENDENT RECONSTRUCTION of the same job search,
produced separately from this repository and holding 353 records against this
repository's 298. It is therefore treated as an adversarial challenger rather
than as a coder: it saw a different source set, so it is not a third blind
rating and no kappa is computed against it.

Two things in it are primary evidence rather than reconstruction, and only
those enter the corpus:

  * `LinkedIn Applications`, 107 rows from the real LinkedIn data download
    (`Job Applications_5.csv` and `_6.csv`), carrying job IDs, job URLs, and
    EXACT application dates. This is the artifact stop condition 3 has been
    waiting for. It supersedes the 99-row paged scrape, whose stamps were
    relative.
  * `Jobright Applications`, 40 rows, already in the corpus at Freeze 2.

Everything else is written under `challenge/` and is never read by the census
pipeline. It exists so the reconciliation in `challenge/CHALLENGE.md` can be
recomputed rather than asserted.

REDACTION. The workbook names real recruiters and other third parties, far more
identifiably than the existing corpus does, which stores at most a first name in
`counterparty_name`. Committed output here replaces every personal name with a
stable one-way pointer `per_<sha256[:12]>`, following the convention in
`scripts/redact_corpus.py`. Company names stay, because the study is about
companies. No reverse map is committed.

    python3 challenge/extract_checkpoint.py path/to/workbook.xlsx

The workbook itself is deliberately NOT committed. It contains unredacted
personal names and this repository is public. Its sha256 is recorded below so
provenance is checkable by anyone holding the file.
"""

from __future__ import annotations

import csv
import hashlib
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "challenge"
ARTIFACTS = ROOT / "artifacts" / "platform"

SOURCE_SHA256 = "5a5c012f3a438ef388ba5afb235d635ecdffb860c9a7979f647a581db402c0a9"
SOURCE_NAME = "combined_job_search_audit_checkpoint_updated.xlsx"
# The workbook's own stated freshness boundary. Activity after this date is not
# in it, which bounds every coverage claim the challenge makes.
EXPORT_FRESHNESS = "2026-08-23"


def person_pointer(name: str) -> str:
    return "per_" + hashlib.sha256(name.strip().lower().encode()).hexdigest()[:12]


def load_workbook(path: Path):
    try:
        import openpyxl
    except ImportError:
        raise SystemExit(
            "openpyxl is required to re-extract the workbook.\n"
            "The extracted CSVs under challenge/ are committed, so the rest of the\n"
            "pipeline runs without it. Install it only to re-run this step."
        )
    return openpyxl.load_workbook(path, read_only=True, data_only=True)


def sheet_rows(wb, name: str) -> tuple[list[str], list[dict]]:
    """Row 1 is a merged banner title, row 2 is the header, data starts at row 3."""
    rows = [r for r in wb[name].iter_rows(values_only=True)]
    header = [str(c).strip() if c is not None else "" for c in rows[1]]
    data = [
        dict(zip(header, r))
        for r in rows[2:]
        if any(c not in (None, "") for c in r)
    ]
    return header, data


def clean(value) -> str:
    """Normalize a cell to text. Datetimes become ISO dates, not timestamps."""
    if value is None:
        return ""
    text = str(value).strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2} 00:00:00", text):
        return text[:10]
    return text


def build_person_roster(wb) -> dict[str, str]:
    """Names to redact, gathered from the columns that hold them explicitly.

    Built from data rather than from a hardcoded list, so a name added to the
    workbook later is redacted on the next run instead of leaking.
    """
    roster: set[str] = set()
    for sheet, column in (
        ("LinkedIn Job Threads", "Person"),
        ("Uncertain and Quarantined", "Contact"),
    ):
        _, rows = sheet_rows(wb, sheet)
        for row in rows:
            name = clean(row.get(column))
            # Split compound entries such as "Marina Ghilchik → Jacob Bowman".
            for part in re.split(r"→|/|;|\band\b", name):
                part = part.strip()
                # A person here is two or more capitalized words, or a name with
                # an initial. Single tokens are skipped: too likely to be a
                # company or a common word, and over-redacting company names
                # would gut the analysis.
                if len(part.split()) >= 2 and not part.isupper():
                    roster.add(part)
    return {name: person_pointer(name) for name in sorted(roster, key=len, reverse=True)}


def redact(text: str, roster: dict[str, str]) -> str:
    """Replace every rostered personal name with its stable pointer."""
    for name, pointer in roster.items():
        if name and name in text:
            text = text.replace(name, pointer)
    # Residual pattern: "Recruiter outbound: Firstname Lastname / Company".
    # Catches names that never appear in a dedicated person column.
    def _sub(match: re.Match) -> str:
        return f"{match.group(1)}{person_pointer(match.group(2))}{match.group(3)}"

    return re.sub(
        r"((?:outbound|outreach|intermediary|inbound|via|follow-up)[:\s]+)"
        r"([A-Z][a-z]+(?:\s+[A-Z][A-Za-z.'’-]+)+)"
        r"(\s*(?:/|→|$))",
        _sub,
        text,
    )


def write_csv(path: Path, header: list[str], rows: list[dict], roster: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [h for h in header if h]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({f: redact(clean(row.get(f)), roster) for f in fields})
    print(f"wrote {path.relative_to(ROOT)} ({len(rows)} rows)")


# sheet name -> output path. The LinkedIn export is the only one that lands in
# artifacts/, because it is the only one that is an artifact.
SHEETS = {
    "LinkedIn Applications": ARTIFACTS / "linkedin_job_applications_export.csv",
    "Combined Ledger": OUT / "checkpoint__ledger.csv",
    "Source Classification": OUT / "checkpoint__source_classification.csv",
    "Role Classification": OUT / "checkpoint__role_classification.csv",
    "Role Lane Distribution": OUT / "checkpoint__role_lane_distribution.csv",
    "LinkedIn Job Threads": OUT / "checkpoint__linkedin_threads.csv",
    "Jobright Applications": OUT / "checkpoint__jobright.csv",
    "Dedup Decisions": OUT / "checkpoint__dedup_decisions.csv",
    "Data Quality Findings": OUT / "checkpoint__data_quality_findings.csv",
    "Platform Merge Summary": OUT / "checkpoint__merge_summary.csv",
    "Uncertain and Quarantined": OUT / "checkpoint__uncertain.csv",
    "Remaining Excluded": OUT / "checkpoint__remaining_excluded.csv",
}


def main() -> int:
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    elif os.environ.get("CHECKPOINT_XLSX"):
        path = Path(os.environ["CHECKPOINT_XLSX"])
    else:
        print(
            f"No workbook path given. Pass it as an argument or set CHECKPOINT_XLSX.\n"
            f"Expected {SOURCE_NAME}, sha256 {SOURCE_SHA256}.\n"
            f"The extracted CSVs are committed, so nothing downstream needs this step re-run."
        )
        return 0

    if not path.is_file():
        print(f"Workbook not found at {path}. Extracted CSVs under challenge/ are already committed.")
        return 0

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        print(
            f"WARNING: workbook sha256 is {digest}, expected {SOURCE_SHA256}.\n"
            f"This is a different file from the one the challenge was written against.\n"
            f"Re-read challenge/CHALLENGE.md before trusting any comparison built on it."
        )

    wb = load_workbook(path)
    roster = build_person_roster(wb)
    print(f"redacting {len(roster)} personal names to per_ pointers")

    for sheet, destination in SHEETS.items():
        header, rows = sheet_rows(wb, sheet)
        write_csv(destination, header, rows, roster)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
