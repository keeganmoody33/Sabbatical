"""Shared definitions for the adjudication scripts.

INTERVIEW_TYPES is currently also defined verbatim in compare_coders.py,
derive_metrics.py, adjudicate.py, and ingest_platform.py. This module is the
intended single home for it. Migrating those four is a separate,
behaviour-preserving change: their outputs are published, so that refactor
should be verifiable as byte-identical output on its own commit.
"""

from __future__ import annotations

import csv
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# An application counts as interviewed when any of these events exists on it.
# Interviewed-ness is derived from the events table, never stored on the
# application row.
INTERVIEW_TYPES = {
    "recruiter_screen",
    "hiring_manager_interview",
    "panel",
    "technical_exercise",
    "final_round",
}


# Events excluded from every derived metric by named adjudication decision.
# This lives here rather than in adjudicate.py because more than one script
# derives figures from the coder event tables, and a decision applied in only
# one of them produces two published numbers that disagree.
# (application_id, event_type, event_date, reason)
EVENT_EXCLUSIONS = [
    (
        "weave|business-development-manager|c1",
        "hiring_manager_interview",
        "2026-08-18",
        "Belongs to a separate inbound Weave process, not this application. "
        "gth_0339a17e3860d167 is a post-interview decline, so an interview did happen, "
        "but the BDM application was already rejected 2025-07-31. Bravo excluded this "
        "artifact during blind coding as having no parent.",
    ),
]

_EXCLUDED_SIGNATURES = {(a, t, d) for a, t, d, _ in EVENT_EXCLUSIONS}


def is_excluded_event(event: dict[str, str]) -> bool:
    """True when a named adjudication decision removes this event from metrics."""
    return (
        event.get("application_id"),
        event.get("event_type"),
        event.get("event_date"),
    ) in _EXCLUDED_SIGNATURES


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def iso_date(value: str) -> datetime.date | None:
    """Parse an ISO date. Returns None rather than raising on anything else."""
    try:
        return datetime.date.fromisoformat((value or "").strip())
    except ValueError:
        return None
