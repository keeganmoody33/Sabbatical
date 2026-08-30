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


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def iso_date(value: str) -> datetime.date | None:
    """Parse an ISO date. Returns None rather than raising on anything else."""
    try:
        return datetime.date.fromisoformat((value or "").strip())
    except ValueError:
        return None
