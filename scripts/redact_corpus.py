#!/usr/bin/env python3
"""Hash provider IDs and redact account identifiers in the committed corpus.

Stable, one-way pointers:
  Gmail thread IDs (16 hex)  -> gth_<sha256[:16]>
  Calendar event IDs        -> cal_<sha256[:16]>
  Gmail page tokens          -> tok_<sha256[:12]>
  Third-party emails          -> eml_<sha256[:12]>

Study mailbox labels stay so retrieval scope remains auditable.
Do not commit a reverse map.
"""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STUDY_EMAILS = {
    "33@lecturesfrom.com",
    "keeganmoody33@gmail.com",
    "keegan@lecturesfrom.com",
    "keeganmoody@gmail.com",
}

ATS_LOCAL_PARTS = {
    "noreply",
    "no-reply",
    "no_reply",
    "donotreply",
    "do-not-reply",
    "notifications",
    "notification",
    "notify",
    "mailer",
    "mailer-daemon",
    "talent",
    "jobs",
    "job",
    "recruiting",
    "careers",
    "applications",
    "candidates",
    "candidate",
    "support",
    "info",
    "team",
    "updates",
    "hello",
    "hi",
    "mail",
    "bounce",
    "invites",
    "invite",
    "calendar-notification",
    "partnership",
    "customersuccess",
    "success",
    "hr",
    "people",
    "hiring",
}

CONSUMER_DOMAINS = {
    "gmail.com",
    "googlemail.com",
    "outlook.com",
    "hotmail.com",
    "yahoo.com",
    "icloud.com",
    "me.com",
    "live.com",
    "msn.com",
}

TEXT_SUFFIXES = {".md", ".csv", ".py", ".txt", ".tsv"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}

EMAIL_RE = re.compile(
    r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"
)
THREAD_RE = re.compile(r"\b[0-9a-f]{16}\b")
PAGE_TOKEN_RE = re.compile(r"\b\d{20}\b")
CANDIDATE_ID_RE = re.compile(r"Candidate ID\s+\d+", re.IGNORECASE)
IBM_REF_RE = re.compile(r"\bRef(?:erence)?\s+\d{5,}\b", re.IGNORECASE)
IBM_APP_NUM_RE = re.compile(r"(IBM job application,\s*)\d+", re.IGNORECASE)
IBM_SUBMITTED_RE = re.compile(r"successfully submitted \d{5,}", re.IGNORECASE)


def digest(value: str, length: int) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:length]


def hash_thread(thread_id: str) -> str:
    return "gth_" + digest(thread_id.lower(), 16)


def hash_calendar(event_id: str) -> str:
    return "cal_" + digest(event_id, 16)


def hash_token(token: str) -> str:
    return "tok_" + digest(token, 12)


def hash_email(address: str) -> str:
    return "eml_" + digest(address.lower(), 12)


HASHED_PREFIXES = ("gth_", "cal_", "tok_", "eml_")


def is_hashed_pointer(value: str) -> bool:
    """Committed corpus IDs are already one-way pointers. Do not hash them again."""
    return value.startswith(HASHED_PREFIXES)


def keep_email(address: str) -> bool:
    lowered = address.lower()
    if lowered in STUDY_EMAILS:
        return True
    local, _, domain = lowered.partition("@")
    if domain in CONSUMER_DOMAINS:
        return False
    local_base = local.split("+", 1)[0]
    if local_base in ATS_LOCAL_PARTS:
        return True
    if local_base.startswith("noreply") or local_base.startswith("no-reply"):
        return True
    return False


def collect_calendar_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    if not path.exists():
        return ids
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in ("event_id", "evidence_id"):
                value = (row.get(key) or "").strip()
                if value and not is_hashed_pointer(value):
                    ids.add(value)
    return ids


def iter_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        files.append(path)
    return files


def redact_text(text: str, calendar_ids: set[str]) -> str:
    # Calendar IDs first, longest first, so 32-hex event IDs are not split
    # into two Gmail-thread hashes.
    for event_id in sorted(calendar_ids, key=len, reverse=True):
        if is_hashed_pointer(event_id):
            continue
        hashed = hash_calendar(event_id)
        text = text.replace(event_id, hashed)
        if len(event_id) >= 12:
            text = text.replace("cal-" + event_id[:12], hashed)

    def replace_thread(match: re.Match[str]) -> str:
        raw = match.group(0)
        prefix = text[max(0, match.start() - 4) : match.start()]
        if prefix in {"gth_", "cal_"}:
            return raw
        return hash_thread(raw)

    text = THREAD_RE.sub(replace_thread, text)

    def replace_token(match: re.Match[str]) -> str:
        raw = match.group(0)
        prefix = text[max(0, match.start() - 4) : match.start()]
        if prefix == "tok_":
            return raw
        return hash_token(raw)

    text = PAGE_TOKEN_RE.sub(replace_token, text)

    def replace_email(match: re.Match[str]) -> str:
        raw = match.group(0)
        if keep_email(raw):
            return raw
        return hash_email(raw)

    text = EMAIL_RE.sub(replace_email, text)
    text = CANDIDATE_ID_RE.sub("Candidate ID [redacted]", text)
    text = IBM_REF_RE.sub("Ref [redacted]", text)
    text = IBM_APP_NUM_RE.sub(r"\1[redacted]", text)
    text = IBM_SUBMITTED_RE.sub("successfully submitted [redacted]", text)
    return text


def main() -> None:
    calendar_ids: set[str] = set()
    for name in (
        "q8-lecturesfrom-primary.csv",
        "q8-keeganmoody33-primary.csv",
    ):
        calendar_ids |= collect_calendar_ids(
            ROOT / "artifacts" / "calendar" / name
        )
    changed = 0
    for path in iter_text_files(ROOT):
        original = path.read_text(encoding="utf-8")
        updated = redact_text(original, calendar_ids)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"files_changed={changed} calendar_ids={len(calendar_ids)}")


if __name__ == "__main__":
    main()
