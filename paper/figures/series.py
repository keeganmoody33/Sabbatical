"""Recompute figure series from the freeze census. No invented values."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTERVIEW_TYPES = {
    "recruiter_screen",
    "hiring_manager_interview",
    "panel",
    "technical_exercise",
    "final_round",
}
MONTHS = [
    "2025-06",
    "2025-07",
    "2025-08",
    "2025-09",
    "2025-10",
    "2025-11",
    "2025-12",
    "2026-01",
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06",
    "2026-07",
    "2026-08",
]
LANE_ORDER = [
    "explicit_gtm_engineering",
    "unspecified",
    "sales_bd_partnerships",
    "growth_demand_marketing",
    "sales_solutions_engineering",
    "other",
    "revops_gtm_ops_strategy",
    "product_ai_technical",
]
LANE_LABEL = {
    "explicit_gtm_engineering": "GTM engineering",
    "unspecified": "unspecified",
    "sales_bd_partnerships": "sales/BD",
    "growth_demand_marketing": "growth",
    "sales_solutions_engineering": "solutions",
    "other": "other",
    "revops_gtm_ops_strategy": "RevOps",
    "product_ai_technical": "product/AI",
}
MONTH_LABEL = {
    "2025-06": "Jun 25",
    "2025-07": "Jul 25",
    "2025-08": "Aug 25",
    "2025-09": "Sep 25",
    "2025-10": "Oct 25",
    "2025-11": "Nov 25",
    "2025-12": "Dec 25",
    "2026-01": "Jan 26",
    "2026-02": "Feb 26",
    "2026-03": "Mar 26",
    "2026-04": "Apr 26",
    "2026-05": "May 26",
    "2026-06": "Jun 26",
    "2026-07": "Jul 26",
    "2026-08": "Aug 26",
}


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def monthly_exact(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for row in rows:
        if row.get("date_precision") != "exact":
            continue
        date = row.get("date_applied") or ""
        if len(date) >= 7:
            counts[date[:7]] += 1
    return {month: counts.get(month, 0) for month in MONTHS}


def compute() -> dict[str, object]:
    census = [
        row
        for row in load(ROOT / "adjudication" / "applications__full_census.csv")
        if row.get("register") == "application"
    ]
    freeze1 = [
        row
        for row in load(ROOT / "adjudication" / "applications__adjudicated.csv")
        if row.get("register") == "application"
    ]
    events = load(ROOT / "coding" / "cursor" / "events__cursor.csv")
    freeze1_ids = {row["application_id"] for row in freeze1}
    census_ids = {row["application_id"] for row in census}
    interviewed = {
        event["application_id"]
        for event in events
        if (event.get("event_type") or "") in INTERVIEW_TYPES
    } & census_ids
    freeze2_new = [row for row in census if row["application_id"] not in freeze1_ids]
    freeze2_interviewed = interviewed & {row["application_id"] for row in freeze2_new}
    offers = [
        row
        for row in census
        if row.get("terminal_outcome") in {"offer_accepted", "offer_declined"}
    ]
    employer_artifact = [
        row for row in census if row.get("evidence_class") == "employer_artifact"
    ]
    return {
        "n_applications": len(census),
        "n_companies": len({row.get("company_canonical") for row in census}),
        "n_freeze1": len(freeze1),
        "n_freeze2_new": len(freeze2_new),
        "n_interviewed": len(interviewed),
        "n_interviewed_freeze1": len(interviewed & freeze1_ids),
        "n_employer_artifact": len(employer_artifact),
        "n_interviewed_employer_artifact": len(
            interviewed & {row["application_id"] for row in employer_artifact}
        ),
        "n_freeze2_interviewed": len(freeze2_interviewed),
        "n_offers": len(offers),
        "n_exact_freeze1": sum(1 for row in freeze1 if row.get("date_precision") == "exact"),
        "n_not_exact_freeze1": sum(
            1 for row in freeze1 if row.get("date_precision") != "exact"
        ),
        "n_exact_full": sum(1 for row in census if row.get("date_precision") == "exact"),
        "n_relative_full": sum(
            1 for row in census if row.get("date_precision") == "relative_display"
        ),
        "n_evidence_bound_full": sum(
            1 for row in census if row.get("date_precision") == "evidence_bound"
        ),
        "monthly_freeze1": monthly_exact(freeze1),
        "monthly_full": monthly_exact(census),
        "lane_freeze1": {lane: sum(1 for row in freeze1 if row.get("role_lane") == lane) for lane in LANE_ORDER},
        "lane_full": {lane: sum(1 for row in census if row.get("role_lane") == lane) for lane in LANE_ORDER},
        "outcomes_freeze1": dict(
            Counter((row.get("terminal_outcome") or "") for row in freeze1)
        ),
        "outcomes_freeze2_blank": sum(
            1 for row in freeze2_new if not (row.get("terminal_outcome") or "")
        ),
        "mercor_marketplace": sum(
            1 for row in census if row.get("company_canonical") == "Mercor"
        ),
        "gtm_modifier_freeze1": dict(
            Counter(
                (row.get("gtm_modifier") or "")
                for row in freeze1
                if row.get("role_lane") == "explicit_gtm_engineering"
            )
        ),
        "gtm_modifier_full": dict(
            Counter(
                (row.get("gtm_modifier") or "")
                for row in census
                if row.get("role_lane") == "explicit_gtm_engineering"
            )
        ),
    }


def assert_freeze_headlines(data: dict[str, object]) -> None:
    """Fail if a figure would print a number this freeze cannot defend."""
    assert data["n_applications"] == 298
    assert data["n_companies"] == 273
    assert data["n_freeze1"] == 221
    assert data["n_freeze2_new"] == 77
    assert data["n_interviewed"] == 14
    assert data["n_interviewed_freeze1"] == 14
    assert data["n_freeze2_interviewed"] == 0
    assert data["n_offers"] == 0
    assert data["n_interviewed_employer_artifact"] == 14
    assert data["n_employer_artifact"] == 220
    assert data["n_exact_freeze1"] == 195
    assert data["n_not_exact_freeze1"] == 26
    assert data["n_exact_full"] == 201
    assert data["n_relative_full"] == 71
    assert data["n_evidence_bound_full"] == 26
    assert data["monthly_freeze1"]["2026-07"] == 33
    assert data["monthly_full"]["2026-07"] == 33
    assert data["monthly_freeze1"]["2025-09"] == 0
    assert data["monthly_freeze1"]["2025-10"] == 0
    assert data["lane_freeze1"]["explicit_gtm_engineering"] == 86
    assert data["lane_full"]["explicit_gtm_engineering"] == 113
    assert data["lane_freeze1"]["unspecified"] == 35
    assert data["lane_full"]["unspecified"] == 35
    assert data["outcomes_freeze1"]["rejected_no_interview"] == 73
    assert data["outcomes_freeze1"]["rejected_after_interview"] == 6
    assert data["outcomes_freeze1"]["role_paused_or_closed"] == 18
    assert data["outcomes_freeze1"]["still_open"] == 124
    assert data["outcomes_freeze2_blank"] == 77
    assert data["mercor_marketplace"] == 6
