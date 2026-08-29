"""Derive interview metrics from events. Interviewed is never stored on applications."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

INTERVIEW_TYPES = {
    "recruiter_screen",
    "hiring_manager_interview",
    "panel",
    "technical_exercise",
    "final_round",
}

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize(coder: str) -> dict[str, object]:
    apps = load(ROOT / "coding" / coder / f"applications__{coder}.csv")
    events = load(ROOT / "coding" / coder / f"events__{coder}.csv")
    interviewed = {
        e["application_id"]
        for e in events
        if (e.get("event_type") or "") in INTERVIEW_TYPES
    }
    census = [a for a in apps if a.get("register") == "application"]
    opportunity = [a for a in apps if a.get("register") == "opportunity"]
    census_ids = {a["application_id"] for a in census}
    opp_ids = {a["application_id"] for a in opportunity}
    interviewed_census = interviewed & census_ids
    interviewed_opp = interviewed & opp_ids
    exact = [a for a in census if a.get("date_precision") == "exact"]
    monthly: Counter[str] = Counter()
    for row in exact:
        date = row.get("date_applied") or ""
        if len(date) >= 7:
            monthly[date[:7]] += 1
    employer_artifact = [a for a in census if a.get("evidence_class") == "employer_artifact"]
    platform_log = [a for a in census if a.get("evidence_class") == "platform_log"]
    rate = (len(interviewed_census) / len(census)) if census else None
    return {
        "coder": coder,
        "n_rows": len(apps),
        "n_application": len(census),
        "n_opportunity": len(opportunity),
        "n_employer_artifact": len(employer_artifact),
        "n_platform_log": len(platform_log),
        "n_interviewed_census": len(interviewed_census),
        "n_interviewed_opportunity": len(interviewed_opp),
        "application_to_interview_rate_employer_artifact": (
            (len(interviewed_census) / len(employer_artifact)) if employer_artifact else None
        ),
        "application_to_interview_rate_full_census": rate,
        "n_exact_date": len(exact),
        "n_non_exact_date": len(census) - len(exact),
        "monthly_exact": dict(sorted(monthly.items())),
        "role_lane": dict(Counter(a.get("role_lane") or "" for a in census)),
    }


def main() -> None:
    import json

    for coder in ("cursor", "alpha", "bravo"):
        path = ROOT / "coding" / coder / f"applications__{coder}.csv"
        if not path.exists():
            continue
        print(json.dumps(summarize(coder), indent=2))


if __name__ == "__main__":
    main()
