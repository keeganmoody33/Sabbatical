"""Adjudicate include/exclude and role_lane after at least two coder CSVs exist."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def match_key(row: dict[str, str]) -> str:
    company = (row.get("company_canonical") or "").strip().lower()
    role = (row.get("role_as_listed") or "").strip().lower()
    cycle = (row.get("cycle") or "1").strip() or "1"
    return f"{company}|{role}|c{cycle}"


def load_apps(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {match_key(row): row for row in csv.DictReader(handle)}


def majority(values: list[str]) -> str | None:
    counts = Counter(v for v in values if v)
    if not counts:
        return None
    top = counts.most_common()
    if len(top) > 1 and top[0][1] == top[1][1]:
        return None
    return top[0][0]


def main() -> None:
    coding = ROOT / "coding"
    loaded: dict[str, dict[str, dict[str, str]]] = {}
    for coder in ("alpha", "bravo", "cursor"):
        path = coding / coder / f"applications__{coder}.csv"
        if path.exists():
            loaded[coder] = load_apps(path)
    if len(loaded) < 2:
        raise SystemExit("need at least two coder CSVs")
    keys: set[str] = set()
    for table in loaded.values():
        keys |= set(table)
    out_rows = []
    fields = [
        "application_id",
        "match_key",
        "n_coders",
        "register_majority",
        "register_tie",
        "role_lane_majority",
        "role_lane_tie",
        "included_in_census",
        "coders_present",
        "registers",
        "role_lanes",
    ]
    for key in sorted(keys):
        rows = {coder: table[key] for coder, table in loaded.items() if key in table}
        registers = [r.get("register") or "" for r in rows.values()]
        lanes = [r.get("role_lane") or "" for r in rows.values()]
        reg_maj = majority(registers)
        lane_maj = majority(lanes)
        included = reg_maj == "application"
        sample = next(iter(rows.values()))
        out_rows.append(
            {
                "application_id": sample.get("application_id") or key,
                "match_key": key,
                "n_coders": str(len(rows)),
                "register_majority": reg_maj or "",
                "register_tie": "" if reg_maj else "1",
                "role_lane_majority": lane_maj or "",
                "role_lane_tie": "" if lane_maj else "1",
                "included_in_census": "1" if included else "0",
                "coders_present": "|".join(sorted(rows)),
                "registers": "|".join(f"{c}:{rows[c].get('register')}" for c in sorted(rows)),
                "role_lanes": "|".join(f"{c}:{rows[c].get('role_lane')}" for c in sorted(rows)),
            }
        )
    out_dir = ROOT / "adjudication"
    path = out_dir / "applications__adjudicated.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)
    census = [r for r in out_rows if r["included_in_census"] == "1"]
    ties = [r for r in out_rows if r["register_tie"] == "1"]
    lane_ties = [r for r in out_rows if r["role_lane_tie"] == "1" and r["included_in_census"] == "1"]
    summary = out_dir / "ADJUDICATION.md"
    summary.write_text(
        "\n".join(
            [
                "# Adjudication",
                "",
                f"Coders compared: {', '.join(sorted(loaded))}.",
                f"Distinct match keys: {len(out_rows)}.",
                f"Majority `register = application`: {len(census)}.",
                f"Register ties (unresolved): {len(ties)}.",
                f"role_lane ties among included keys: {len(lane_ties)}.",
                "",
                "A key is in the census only when a majority of coders who coded it assigned `register = application`.",
                "Ties stay out of the census and are listed in disagreements.csv after compare_coders.py.",
                "",
                "Capture recapture was not computed. LinkedIn Job Applications.csv is absent.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {path} n={len(out_rows)} census={len(census)} register_ties={len(ties)}")


if __name__ == "__main__":
    main()
