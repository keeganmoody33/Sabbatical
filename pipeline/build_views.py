"""Materialize the analysis views the paper quotes from.

Every number in `paper/PAPER.md` is quoted from a file this script writes, so
that a reader can check a claim by opening a CSV rather than by trusting a
sentence. `paper/NUMBERS.md` maps each claim to its view.

Three rules hold across every view here.

1. INTERVIEWED IS DERIVED, NEVER STORED. The numerator is rebuilt from the
   union of both coders' event tables on each run, using the same
   `INTERVIEW_TYPES` and the same named `EVENT_EXCLUSIONS` that
   `adjudication/adjudicate.py` uses, imported from `adjudication/_common.py`
   rather than restated. A second definition of the interview set is a second
   published number that will eventually disagree with the first.

2. SMALL CELLS ARE SUPPRESSED, NOT DROPPED. Any group under `MIN_CELL` keeps
   its row and its n, and its rate columns are blanked with
   `suppressed = yes`. A silently dropped group is indistinguishable from a
   group that does not exist.

3. RATES CARRY AN INTERVAL. With 14 interviews across 223 applications, every
   per-group rate is a small-sample estimate. Each rate ships with a Wilson 95
   percent interval so the width is visible next to the point. No p-values.
"""

from __future__ import annotations

import csv
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adjudication"))

from _common import (  # noqa: E402
    INTERVIEW_TYPES,
    is_excluded_event,
    iso_date,
    load_csv,
)

ADJ = ROOT / "adjudication"
VIEWS = ROOT / "views"

# Groups smaller than this publish an n and nothing else. The threshold matches
# the one derive_latency.py already applies to its slices.
MIN_CELL = 5

# The pre-registered study window. Months outside it are not rows in the
# monthly view, so a gap inside the window reads as a gap rather than as the
# end of the data.
WINDOW_START = "2025-06"
WINDOW_END = "2026-08"


def wilson(successes: int, total: int) -> tuple[float, float]:
    """Wilson score interval at 95 percent.

    Chosen over the normal approximation because several cells here have zero
    successes, where the normal interval collapses to zero width and asserts a
    certainty the data does not have.
    """
    if total == 0:
        return (0.0, 0.0)
    z = 1.959963984540054
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominator
    return (max(0.0, center - margin), min(1.0, center + margin))


def months_in_window() -> list[str]:
    out = []
    year, month = (int(x) for x in WINDOW_START.split("-"))
    end_year, end_month = (int(x) for x in WINDOW_END.split("-"))
    while (year, month) <= (end_year, end_month):
        out.append(f"{year:04d}-{month:02d}")
        month += 1
        if month == 13:
            year, month = year + 1, 1
    return out


def write_view(name: str, fields: list[str], rows: list[dict]) -> None:
    VIEWS.mkdir(exist_ok=True)
    path = VIEWS / name
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})
    print(f"wrote {path.relative_to(ROOT)} ({len(rows)} rows)")


def interviewed_ids(census_ids: set[str]) -> set[str]:
    """The interview numerator, rebuilt the way adjudicate.py builds it.

    Union of both coders' events. An event recorded by both is harmless because
    membership is a set. Events removed by named adjudication decision are
    excluded here through the same shared predicate.
    """
    found: set[str] = set()
    for coder in ("cursor", "bravo"):
        for event in load_csv(ROOT / "coding" / coder / f"events__{coder}.csv"):
            if (event.get("event_type") or "") not in INTERVIEW_TYPES:
                continue
            if is_excluded_event(event):
                continue
            if event.get("application_id") in census_ids:
                found.add(event["application_id"])
    return found


def funnel_rows(
    rows: list[dict],
    interviewed: set[str],
    latency: dict[str, dict],
    key: str,
    key_label: str,
) -> list[dict]:
    """One row per distinct value of `key`, with the funnel counts under it.

    Response counts come from the latency table, whose base is the subset of
    the census carrying an exact-dated submission receipt. That base is smaller
    than the census, so it is reported as its own column rather than folded
    into the denominator. A response rate computed against the census would
    silently count "no exact date" as "no response".
    """
    out = []
    for value, n in sorted(Counter(r[key] for r in rows).items(), key=lambda kv: (-kv[1], kv[0])):
        group = [r for r in rows if r[key] == value]
        ids = {r["application_id"] for r in group}
        n_interviewed = len(ids & interviewed)
        base = [latency[i] for i in ids if i in latency]
        n_responded_any = sum(1 for r in base if r["days_to_response_broad"] != "")
        n_responded_substantive = sum(1 for r in base if r["days_to_response_strict"] != "")
        suppressed = n < MIN_CELL
        lo, hi = wilson(n_interviewed, n)
        out.append(
            {
                key_label: value,
                "n_applications": n,
                "n_latency_base": len(base),
                "n_responded_any": n_responded_any,
                "n_responded_substantive": n_responded_substantive,
                "n_interviewed": n_interviewed,
                "interview_rate": "" if suppressed else f"{n_interviewed}/{n}",
                "interview_rate_wilson_lo": "" if suppressed else f"{lo:.4f}",
                "interview_rate_wilson_hi": "" if suppressed else f"{hi:.4f}",
                "suppressed": "yes" if suppressed else "no",
            }
        )
    return out


FUNNEL_FIELDS_TAIL = [
    "n_applications",
    "n_latency_base",
    "n_responded_any",
    "n_responded_substantive",
    "n_interviewed",
    "interview_rate",
    "interview_rate_wilson_lo",
    "interview_rate_wilson_hi",
    "suppressed",
]


def build_origin_coverage(census: list[dict], full: list[dict], interviewed: set[str]) -> None:
    """The null result, as a file.

    The brief this study answers asks which origination channels convert. This
    view is the reason no such number is published. It reports, for each of the
    three origin fields the codebook keeps separate, how many rows carry a
    usable value and how many outcomes sit under it.

    The shape to read here: on the full census the rows that DO know their
    origin are almost entirely platform_log rows, and platform_log rows carry
    no events, so origin is known exactly where outcome is not.
    """
    taxonomy = {
        (r["field"], r["raw_value"]): r
        for r in load_csv(ROOT / "pipeline" / "origin_taxonomy.csv")
    }
    census_ids = {r["application_id"] for r in census}
    rows = []
    for stratum, data in ((f"application_census_{len(census)}", census), (f"full_census_{len(full)}", full)):
        for field in ("discovery_source", "submission_channel", "evidence_class"):
            for value, n in sorted(
                Counter(r[field] for r in data).items(), key=lambda kv: (-kv[1], kv[0])
            ):
                mapped = taxonomy.get((field, value))
                group_ids = {r["application_id"] for r in data if r[field] == value}
                # Outcomes are only observable on rows in the adjudicated
                # census, because that is where the event tables attach.
                observable = group_ids & census_ids
                rows.append(
                    {
                        "stratum": stratum,
                        "field": field,
                        "raw_value": value,
                        "normalized_channel": mapped["normalized_channel"] if mapped else "UNMAPPED",
                        "channel_family": mapped["channel_family"] if mapped else "UNMAPPED",
                        "origin_is_known": mapped["origin_is_known"] if mapped else "UNMAPPED",
                        "n": n,
                        "share_of_stratum": f"{n / len(data):.4f}",
                        "n_outcome_observable": len(observable),
                        "n_interviewed": len(group_ids & interviewed),
                    }
                )
    write_view(
        "origin_coverage.csv",
        [
            "stratum",
            "field",
            "raw_value",
            "normalized_channel",
            "channel_family",
            "origin_is_known",
            "n",
            "share_of_stratum",
            "n_outcome_observable",
            "n_interviewed",
        ],
        rows,
    )
    unmapped = [r for r in rows if r["normalized_channel"] == "UNMAPPED"]
    if unmapped:
        raise SystemExit(
            "origin_taxonomy.csv does not cover every observed value: "
            + ", ".join(sorted({f"{r['field']}={r['raw_value']}" for r in unmapped}))
        )


def build_monthly_trend(census: list[dict], interviewed: set[str]) -> None:
    """Applications per month on exact dates only.

    `n_not_exact_total` is repeated on every row on purpose. It is the count of
    census rows this series cannot place, and a chart built from this file
    without printing it would misrepresent the shape of the search.
    """
    exact = [r for r in census if r["date_precision"] == "exact"]
    n_not_exact = len(census) - len(exact)
    by_month = Counter(r["date_applied"][:7] for r in exact)
    interviewed_by_month = Counter(
        r["date_applied"][:7] for r in exact if r["application_id"] in interviewed
    )
    rows = [
        {
            "month": month,
            "n_applications_exact_date": by_month.get(month, 0),
            "n_interviewed_exact_date": interviewed_by_month.get(month, 0),
            "n_exact_date_total": len(exact),
            "n_not_exact_total": n_not_exact,
        }
        for month in months_in_window()
    ]
    write_view(
        "monthly_trend.csv",
        [
            "month",
            "n_applications_exact_date",
            "n_interviewed_exact_date",
            "n_exact_date_total",
            "n_not_exact_total",
        ],
        rows,
    )


# Title tokens tested for association with progression. Each is a regex over
# the lowercased `role_as_listed`. These groups OVERLAP by construction: one
# title can match several, so the rows do not sum to the census.
TITLE_TOKENS: list[tuple[str, str]] = [
    ("gtm_or_go_to_market", r"\bgtm\b|go[- ]to[- ]market"),
    ("engineer", r"\bengineer\b|\bengineering\b"),
    ("growth", r"\bgrowth\b"),
    ("solutions", r"\bsolutions?\b"),
    ("sales", r"\bsales\b"),
    ("operations_or_revops", r"\boperations\b|\brevops\b|\bops\b"),
    ("founding", r"\bfounding\b"),
    ("senior_or_lead_or_head", r"\bsenior\b|\bsr\.?\b|\blead\b|\bhead\b|\bdirector\b"),
    ("ai_or_technical", r"\bai\b|\btechnical\b|\bml\b"),
    ("unspecified_title", r"^unspecified$"),
]


def build_title_language(census: list[dict], interviewed: set[str], latency: dict[str, dict]) -> None:
    """Which title language sat on the applications that progressed.

    Read this as description, not as cause. The applicant chose which roles to
    apply to, so title language is confounded with self-selection: a title that
    progressed may reflect where he was a strong fit rather than any property
    of the words. Nothing here randomizes anything.
    """
    rows: list[dict] = []

    for lane, n in sorted(
        Counter(r["role_lane"] for r in census).items(), key=lambda kv: (-kv[1], kv[0])
    ):
        group = [r for r in census if r["role_lane"] == lane]
        rows.append(_language_row("role_lane", lane, group, interviewed, latency))

    modifiers = [r for r in census if r["gtm_modifier"]]
    for modifier, n in sorted(
        Counter(r["gtm_modifier"] for r in modifiers).items(), key=lambda kv: (-kv[1], kv[0])
    ):
        group = [r for r in modifiers if r["gtm_modifier"] == modifier]
        rows.append(_language_row("gtm_modifier", modifier, group, interviewed, latency))

    for label, pattern in TITLE_TOKENS:
        regex = re.compile(pattern)
        group = [r for r in census if regex.search(r["role_as_listed"].lower())]
        if group:
            rows.append(_language_row("title_token", label, group, interviewed, latency))

    write_view(
        "title_language.csv",
        ["dimension", "value", "n_distinct_titles"] + FUNNEL_FIELDS_TAIL,
        rows,
    )


def _language_row(
    dimension: str,
    value: str,
    group: list[dict],
    interviewed: set[str],
    latency: dict[str, dict],
) -> dict:
    ids = {r["application_id"] for r in group}
    n = len(group)
    n_interviewed = len(ids & interviewed)
    base = [latency[i] for i in ids if i in latency]
    suppressed = n < MIN_CELL
    lo, hi = wilson(n_interviewed, n)
    return {
        "dimension": dimension,
        "value": value,
        "n_distinct_titles": len({r["role_as_listed"].lower() for r in group}),
        "n_applications": n,
        "n_latency_base": len(base),
        "n_responded_any": sum(1 for r in base if r["days_to_response_broad"] != ""),
        "n_responded_substantive": sum(1 for r in base if r["days_to_response_strict"] != ""),
        "n_interviewed": n_interviewed,
        "interview_rate": "" if suppressed else f"{n_interviewed}/{n}",
        "interview_rate_wilson_lo": "" if suppressed else f"{lo:.4f}",
        "interview_rate_wilson_hi": "" if suppressed else f"{hi:.4f}",
        "suppressed": "yes" if suppressed else "no",
    }


def median(values: list[int]) -> str:
    if not values:
        return ""
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return f"{ordered[mid]}"
    return f"{(ordered[mid - 1] + ordered[mid]) / 2:g}"


def build_latency_by_slice(census: list[dict], latency: dict[str, dict]) -> None:
    """Days to first response, cut by every dimension the base supports.

    The base is the 196 census rows with an exact-dated submission receipt, not
    the 221. Medians are conditional on having responded at all, so the row
    also carries the response count that produced them. A single median folding
    in the silent applications would drop them from the denominator, which is
    the same error the two-register split exists to prevent on the interview
    rate.

    `submission_channel` and `discovery_source` are cut here even though most
    of their mass is one value, because a slice that cannot separate anything
    is itself the finding.
    """
    by_id = {r["application_id"]: r for r in census}
    rows = []
    dimensions = [
        ("role_lane", lambda r: r["role_lane"]),
        ("month", lambda r: r["month"]),
        ("ats_system", lambda r: r["ats_system"]),
        ("submission_channel", lambda r: by_id[r["application_id"]]["submission_channel"]),
        ("discovery_source", lambda r: by_id[r["application_id"]]["discovery_source"]),
        ("evidence_class", lambda r: by_id[r["application_id"]]["evidence_class"]),
    ]
    base = list(latency.values())
    for dimension, getter in dimensions:
        for value, n in sorted(Counter(getter(r) for r in base).items(), key=lambda kv: (-kv[1], kv[0])):
            group = [r for r in base if getter(r) == value]
            strict = [int(r["days_to_response_strict"]) for r in group if r["days_to_response_strict"] != ""]
            broad = [int(r["days_to_response_broad"]) for r in group if r["days_to_response_broad"] != ""]

            # A median is suppressed on the count it was computed from, not on
            # the size of the group. These medians are conditional on having
            # responded, so a group of 8 with 3 responders gives a 3-point
            # median, and publishing that beside a 43-point median because both
            # groups cleared a base threshold would present them as comparable.
            suppress_base = n < MIN_CELL
            suppress_strict = suppress_base or len(strict) < MIN_CELL
            suppress_broad = suppress_base or len(broad) < MIN_CELL
            reasons = []
            if suppress_base:
                reasons.append(f"base n={n}")
            else:
                if suppress_strict:
                    reasons.append(f"substantive responders n={len(strict)}")
                if suppress_broad:
                    reasons.append(f"any responders n={len(broad)}")

            rows.append(
                {
                    "dimension": dimension,
                    "value": value,
                    "n_base": n,
                    "n_responded_substantive": len(strict),
                    "n_responded_any": len(broad),
                    "median_days_substantive": "" if suppress_strict else median(strict),
                    "median_days_any": "" if suppress_broad else median(broad),
                    "suppressed_because": "; ".join(reasons),
                }
            )
    write_view(
        "latency_by_slice.csv",
        [
            "dimension",
            "value",
            "n_base",
            "n_responded_substantive",
            "n_responded_any",
            "median_days_substantive",
            "median_days_any",
            "suppressed_because",
        ],
        rows,
    )


def build_origin_recoverability(census: list[dict]) -> None:
    """How much origin is recoverable after the fact, and how much never is.

    This view exists because of the Freeze 3 challenge. Before it, the origin
    finding was stated as a flat 93 percent unknown, which is true of the coded
    field and implies the information is simply gone. It is not quite gone. A
    platform export that recorded an application lets its origin be recovered
    later by matching, and Freeze 3 added a LinkedIn export that does exactly
    that for a further 29 rows.

    So the honest shape is three tiers, not two. Origin captured at write time
    is small. Origin recoverable later by matching a platform export is a third
    of the census. Origin that no route recovers is the remaining two thirds,
    and those are the rows whose only record is employer-side mail, which never
    says where the applicant found the posting.

    The recovered value is NOT written into `discovery_source`. The coded field
    stays as the blind coders left it, and this view sits beside it. A derived
    value overwriting a coded one would make the census unauditable against the
    coder tables.
    """
    matches = load_csv(ADJ / "platform_match.csv")
    census_ids = {r["application_id"] for r in census}
    corroborated: dict[str, set[str]] = {}
    for row in matches:
        if not row["match_status"].startswith("overlap"):
            continue
        parents = row["parent_id"] or row["candidate_parent_ids"] or ""
        for parent in (p.strip() for p in parents.split(";") if p.strip()):
            if parent in census_ids:
                corroborated.setdefault(parent, set()).add(row["discovery_source"])

    rows = []
    for row in census:
        aid = row["application_id"]
        coded = row["discovery_source"]
        sources = corroborated.get(aid, set())
        if coded != "unknown":
            tier, recovered = "captured_at_write_time", coded
        elif sources:
            tier, recovered = "recoverable_from_platform_export", ";".join(sorted(sources))
        else:
            tier, recovered = "unrecoverable", ""
        rows.append(
            {
                "application_id": aid,
                "company_canonical": row["company_canonical"],
                "coded_discovery_source": coded,
                "recovery_tier": tier,
                "recovered_source": recovered,
                "evidence_class": row["evidence_class"],
            }
        )
    write_view(
        "origin_recoverability.csv",
        [
            "application_id",
            "company_canonical",
            "coded_discovery_source",
            "recovery_tier",
            "recovered_source",
            "evidence_class",
        ],
        rows,
    )
    counts = Counter(r["recovery_tier"] for r in rows)
    total = len(rows)
    for tier in ("captured_at_write_time", "recoverable_from_platform_export", "unrecoverable"):
        n = counts.get(tier, 0)
        print(f"    {tier}: {n} of {total} ({n / total:.1%})")


KNOWLEDGE = ROOT / "knowledge"

# Author-supplied discovery sources live OUTSIDE the census on purpose. The
# census is artifact-derived and its reproducibility is the whole claim, so a
# layer the author can revise at any time must not sit inside it, or every
# recall edit becomes a census change. Keeping it a side table also means the
# author can revise freely without touching a frozen file.
#
# `discovery_source` (coded, blind, frozen) and `discovery_source_recalled`
# (author, revisable) are never merged into one stored value. The view carries
# both plus a `basis` naming which one the resolved value came from.
# The extension terms. Everything else in the vocabulary is read from
# `codebook.md` at run time, the same way data_quality.py reads it, so the
# recalled field cannot drift from the frozen instrument.
#
# Only four terms are added, and only where the frozen vocabulary genuinely
# cannot express the value. `newsletter_community` exists but collapses a
# specific Slack channel into the same bucket as a newsletter, and the whole
# point of this layer is that the specific channel is the finding.
DISCOVERY_VOCAB_EXTENSION = {
    "gtm_cafe_slack",
    "gtm_engineering_school",
    "linkedin_inbound_dm",
    "platform_internal_board",
}


def discovery_vocab() -> set[str]:
    """Frozen codebook terms plus the four extensions."""
    text = (ROOT / "codebook.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("**discovery_source**:"):
            terms = {
                t.strip().strip("`")
                for t in line.split(":", 1)[1].split(",")
            }
            return {t for t in terms if t} | DISCOVERY_VOCAB_EXTENSION
    raise SystemExit(
        "codebook.md has no `**discovery_source**:` vocabulary line. The view "
        "layer reads it at run time rather than holding a copy, so a rename "
        "there must not silently pass here."
    )


def venue_edges() -> dict[str, str]:
    """venue -> the venue it was discovered through, or `root`."""
    edges = {}
    for row in load_csv(KNOWLEDGE / "discovery_venues.csv"):
        venue = row["venue"].strip()
        if venue:
            edges[venue] = row["discovered_via"].strip() or "root"
    return edges


def root_venue(venue: str, edges: dict[str, str]) -> str:
    """Walk the discovery chain to its root.

    The author's point: a job found in a Slack channel was not really found in
    a Slack channel, it was found through whatever led to that channel. Here
    `gtm_cafe_slack` resolves to `gtm_engineering_school`, so a rollup can ask
    how many processes trace back to one root rather than counting the
    proximate venue.

    Cycle-guarded. A chain that loops returns the venue it started from rather
    than hanging, and the loop is a data error the vocabulary check will not
    catch on its own.
    """
    seen = set()
    current = venue
    while True:
        nxt = edges.get(current, "root")
        if nxt == "root" or nxt == "" or nxt in seen:
            return current
        seen.add(current)
        current = nxt


def build_discovery_source(census: list[dict], interviewed: set[str]) -> None:
    """Per-application discovery, coded beside recalled, with the basis named.

    Every census row appears. A row with neither a coded nor a recalled value
    resolves to `unknown`, which keeps the residual visible instead of letting
    the populated rows look like the whole picture.
    """
    vocab = discovery_vocab()
    edges = venue_edges()
    recalled = {}
    for row in load_csv(KNOWLEDGE / "discovery_source_recalled.csv"):
        value = row["discovery_source_recalled"].strip()
        if value and value not in vocab:
            raise SystemExit(
                f"discovery_source_recalled.csv: {row['application_id']!r} carries "
                f"{value!r}, which is not in the controlled vocabulary. Add it to "
                f"DISCOVERY_VOCAB_EXTENSION and to knowledge/discovery_venues.csv, or fix the value."
            )
        recalled[row["application_id"]] = row

    rows = []
    for r in census:
        aid = r["application_id"]
        coded = (r.get("discovery_source") or "").strip() or "unknown"
        rec = recalled.get(aid, {})
        rec_value = (rec.get("discovery_source_recalled") or "").strip()

        # Coded wins when it is informative, because it came from an artifact
        # read blind. Recall fills the residual only.
        if coded != "unknown":
            resolved, basis = coded, "coded_artifact"
        elif rec_value:
            resolved, basis = rec_value, "author_recall"
        else:
            resolved, basis = "unknown", "none"

        conflict = "yes" if (coded != "unknown" and rec_value and rec_value != coded) else "no"
        rows.append({
            "application_id": aid,
            "company_canonical": r["company_canonical"],
            "discovery_source_coded": coded,
            "discovery_source_recalled": rec_value,
            "discovery_source_resolved": resolved,
            "basis": basis,
            "conflict": conflict,
            "root_venue": root_venue(resolved, edges),
            "interviewed": "yes" if aid in interviewed else "no",
        })

    rows.sort(key=lambda r: (r["discovery_source_resolved"], r["application_id"]))
    write_view(
        "discovery_source.csv",
        ["application_id", "company_canonical", "discovery_source_coded",
         "discovery_source_recalled", "discovery_source_resolved", "basis",
         "conflict", "root_venue", "interviewed"],
        rows,
    )

    # Funnel on the resolved value. This is the `funnel_by_origin` the brief
    # asked for, finally buildable, and still mostly one enormous unknown cell.
    by_source = {}
    for row in rows:
        bucket = by_source.setdefault(row["discovery_source_resolved"], {"n": 0, "iv": 0, "recall": 0})
        bucket["n"] += 1
        bucket["iv"] += row["interviewed"] == "yes"
        bucket["recall"] += row["basis"] == "author_recall"

    funnel = []
    for source, b in sorted(by_source.items(), key=lambda kv: -kv[1]["n"]):
        suppressed = b["n"] < MIN_CELL
        lo, hi = wilson(b["iv"], b["n"])
        funnel.append({
            "discovery_source_resolved": source,
            "root_venue": root_venue(source, edges),
            "n_applications": b["n"],
            "n_from_author_recall": b["recall"],
            "n_interviewed": b["iv"],
            "interview_rate": "" if suppressed else f"{b['iv']}/{b['n']}",
            "interview_rate_wilson_lo": "" if suppressed else f"{lo:.4f}",
            "interview_rate_wilson_hi": "" if suppressed else f"{hi:.4f}",
            "suppressed": "yes" if suppressed else "no",
        })
    write_view(
        "funnel_by_discovery_source.csv",
        ["discovery_source_resolved", "root_venue", "n_applications",
         "n_from_author_recall", "n_interviewed", "interview_rate",
         "interview_rate_wilson_lo", "interview_rate_wilson_hi", "suppressed"],
        funnel,
    )


def main() -> None:
    census = load_csv(ADJ / "applications__adjudicated.csv")
    full = load_csv(ADJ / "applications__full_census.csv")
    latency = {r["application_id"]: r for r in load_csv(ADJ / "latency__by_application.csv")}

    census_ids = {r["application_id"] for r in census}
    interviewed = interviewed_ids(census_ids)

    # Guards. These are the published figures. If a view is built on a census
    # that no longer matches them, the failure should be loud and immediate
    # rather than discovered later in a table.
    # Freeze 3 figures. Freeze 2 was 221 / 298 / 13 / 196; the LinkedIn formal
    # export and the two register reversals moved all four.
    # Freeze 4 moved interviewed 14 to 11: three rows were coded from an
    # invitation rather than a completed round. See adjudication/INTERVIEW-EVIDENCE.md.
    assert len(census) == 223, f"application census is {len(census)}, expected 223"
    assert len(full) == 317, f"full census is {len(full)}, expected 317"
    assert len(interviewed) == 11, f"interviewed is {len(interviewed)}, expected 11"
    assert len(latency) == 197, f"latency base is {len(latency)}, expected 197"

    # Sanity on the dates the monthly view depends on.
    for row in census:
        if row["date_precision"] == "exact":
            assert iso_date(row["date_applied"]) is not None, row["application_id"]

    build_origin_coverage(census, full, interviewed)

    write_view(
        "funnel_by_role_lane.csv",
        ["role_lane"] + FUNNEL_FIELDS_TAIL,
        funnel_rows(census, interviewed, latency, "role_lane", "role_lane"),
    )
    write_view(
        "funnel_by_submission_channel.csv",
        ["submission_channel"] + FUNNEL_FIELDS_TAIL,
        funnel_rows(census, interviewed, latency, "submission_channel", "submission_channel"),
    )
    write_view(
        "funnel_by_evidence_class.csv",
        ["evidence_class"] + FUNNEL_FIELDS_TAIL,
        funnel_rows(census, interviewed, latency, "evidence_class", "evidence_class"),
    )

    build_origin_recoverability(census)
    build_monthly_trend(census, interviewed)
    build_title_language(census, interviewed, latency)
    build_latency_by_slice(census, latency)
    build_discovery_source(census, interviewed)


if __name__ == "__main__":
    main()
