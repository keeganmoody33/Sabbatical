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
    # Freeze 4, 2026-08-30. An invitation is not a round.
    #
    # These four were coded from an artifact that PROPOSES a conversation, or
    # administers one asynchronously, rather than one that RECORDS a completed
    # round. The codebook gave the coders no rule separating
    # the two, so `recruiter_screen` and `hiring_manager_interview` were assigned
    # to invitations as readily as to completed rounds. That is a missing rule,
    # not a careless coder: two coders independently made the same call on
    # TestGorilla and RevSpring.
    #
    # The corpus itself supplies the test. Every interview that holds carries at
    # least one of: a scheduling confirmation or calendar reminder naming an
    # interviewer, a decline phrased as after a process, a candidate-experience
    # survey, a SENT message referencing the conversation, or a later stage that
    # presupposes the first. These four carry none. Full evidence table in
    # `adjudication/INTERVIEW-EVIDENCE.md`.
    #
    # Three were removed together; jobmail-io followed once the author supplied
    # the underlying decline. None carries a terminal outcome that needs
    # reverting, so unlike the Weave correction nothing else moves.
    (
        "hypergen|gtm-engineer|c1",
        "hiring_manager_interview",
        "2026-04-14",
        "An interview INVITATION from people@hypergen.io replying to the March 11 "
        "confirmation, with nothing after it. Flagged at retrieval time: "
        "retrieval-log-006 records that the prior ledger held Hypergen as a receipt "
        "only and that the Interviews sheet does not list it. Bravo blind-coded the "
        "same artifact `employer_ack`; cursor is the lone outlier and adjudication "
        "took cursor.",
    ),
    (
        "testgorilla|go-to-market-engineer|c1",
        "recruiter_screen",
        "2026-02-20",
        "A recruiter INTRO message, alongside an assessment invitation the same day "
        "and a recruiter update on 2026-04-23. No scheduling artifact, no completion "
        "signal, no SENT reply. Both coders made this call, which is why it is "
        "recorded as a missing codebook rule rather than a coder error.",
    ),
    (
        "jobmail-io|growth-lead|c1",
        "recruiter_screen",
        "2026-07-13",
        "The decline credits 'completing the requested steps through' a named "
        "party that is an AUTOMATED SCREENING PRODUCT, not a person at the "
        "employer: the sending address and the reply-to both belong to that "
        "product rather than to the hiring company. The steps were therefore "
        "asynchronous and machine-administered. Kept at Freeze 4 as ambiguous "
        "on the retrieval note alone; resolved when the author supplied the "
        "decline itself. Also the row carrying the standing contradiction "
        "between a derived interview and a stored `rejected_no_interview`, "
        "from one coder with no blind second reading.",
    ),
    (
        "revspring|lead-agentic-operations-gtm-engineering|c1",
        "recruiter_screen",
        "2026-06-10",
        "A Recruiter Screen REQUEST. The surrounding thread is two submission "
        "receipts and two employer acknowledgments, with no scheduling artifact and "
        "no completion signal. Both coders made this call.",
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
