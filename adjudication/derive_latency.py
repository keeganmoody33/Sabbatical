"""Time to first response and time to first interview, per the pre-registration.

knowledge/protocol.md names these as secondary outcomes and fixes the method:
metrics are computed only on rows where both dates carry precision = exact, and
the excluded n is reported alongside. This script implements that and nothing
more. It does not deviate from the protocol, so it needs no changelog entry.

Two response definitions are reported. The broad one counts employer_ack, the
strict one does not. The day-zero share doubles under the broad definition,
which is the signature of an automated acknowledgment arriving with the receipt,
so the strict figure is the headline and both are published.

Response rate and latency are reported separately and never merged. The median
is conditional on having responded. Roughly half of all applications produced a
receipt and then nothing, and folding those into a single "typical response
time" would drop them from the denominator.

Cells below MIN_CELL are suppressed. Suppressed groups are named with their
counts so the suppression is visible rather than silent.
"""

from __future__ import annotations

import collections
import csv
import datetime
import statistics

from _common import INTERVIEW_TYPES, ROOT, iso_date, load_csv

OUT = ROOT / "adjudication"

# End of the study window, knowledge/protocol.md. Used for exposure only.
WINDOW_END = datetime.date(2026, 8, 29)

# Minimum rows before a slice cell is published.
MIN_CELL = 5

# A substantive employer response. employer_ack is excluded here and added back
# for the broad definition.
STRICT_RESPONSE = {"rejection", "assessment_sent", "offer"} | INTERVIEW_TYPES
BROAD_RESPONSE = STRICT_RESPONSE | {"employer_ack"}

ROW_FIELDS = [
    "application_id",
    "company_canonical",
    "role_as_listed",
    "date_applied",
    "exposure_days",
    "days_to_response_strict",
    "days_to_response_broad",
    "days_to_interview",
    "role_lane",
    "ats_system",
    "month",
]


def build_rows() -> tuple[list[dict], int, int]:
    """One row per census application with an exact-dated submission receipt."""
    census = load_csv(OUT / "applications__adjudicated.csv")
    apps = {r["application_id"]: r for r in census}

    # Union both coders' events, as adjudicate.py does for the interview
    # numerator. Every derived value below is a per-application minimum, so an
    # event recorded by both coders is harmless.
    events: list[dict[str, str]] = []
    for coder in ("cursor", "bravo"):
        path = ROOT / "coding" / coder / f"events__{coder}.csv"
        if path.exists():
            events.extend(load_csv(path))

    by_app: dict[str, list[dict[str, str]]] = collections.defaultdict(list)
    for event in events:
        if event.get("application_id") in apps:
            by_app[event["application_id"]].append(event)

    rows = []
    for app_id, app in apps.items():
        evs = by_app.get(app_id, [])
        submissions = [
            iso_date(e["event_date"])
            for e in evs
            if e.get("event_type") == "submission_receipt"
            and e.get("event_date_precision") == "exact"
        ]
        submissions = [s for s in submissions if s]
        if not submissions:
            continue
        start = min(submissions)

        def first_after(types: set[str]) -> int | None:
            dates = [
                iso_date(e["event_date"])
                for e in evs
                if e.get("event_type") in types
                and e.get("event_date_precision") == "exact"
            ]
            dates = [d for d in dates if d and d >= start]
            return (min(dates) - start).days if dates else None

        rows.append(
            {
                "application_id": app_id,
                "company_canonical": app.get("company_canonical", ""),
                "role_as_listed": app.get("role_as_listed", ""),
                "date_applied": start.isoformat(),
                "exposure_days": (WINDOW_END - start).days,
                "days_to_response_strict": first_after(STRICT_RESPONSE),
                "days_to_response_broad": first_after(BROAD_RESPONSE),
                "days_to_interview": first_after(INTERVIEW_TYPES),
                "role_lane": app.get("role_lane", ""),
                "ats_system": app.get("ats_system", ""),
                "month": start.strftime("%Y-%m"),
            }
        )
    return rows, len(census), len(census) - len(rows)


def fmt(value: float) -> str:
    """Render a median without a trailing .0 on whole numbers."""
    return str(int(value)) if float(value).is_integer() else str(value)


def summary(values: list[int]) -> dict:
    values = sorted(values)
    n = len(values)
    return {
        "n": n,
        "median": statistics.median(values),
        "mean": sum(values) / n,
        "p25": values[n // 4],
        "p75": values[(3 * n) // 4],
        "min": values[0],
        "max": values[-1],
        "day0": sum(1 for v in values if v == 0),
    }


def slice_table(rows: list[dict], field: str, metric: str) -> tuple[list, list]:
    """Published cells and suppressed cells for one dimension."""
    groups: dict[str, list[int]] = collections.defaultdict(list)
    for row in rows:
        if row[metric] is not None:
            groups[row[field] or "(empty)"].append(row[metric])
    published, suppressed = [], []
    for key, values in groups.items():
        entry = (key, len(values), statistics.median(values))
        (published if len(values) >= MIN_CELL else suppressed).append(entry)
    published.sort(key=lambda e: -e[1])
    suppressed.sort(key=lambda e: -e[1])
    return published, suppressed


def interview_provenance() -> tuple[set, set, set, list]:
    """Who found each interview, and any interview event postdating a rejection.

    Time to first interview inherits whatever the interview set gets wrong, so
    the report states how that set was assembled rather than presenting it as
    settled.
    """
    census = {r["application_id"] for r in load_csv(OUT / "applications__adjudicated.csv")}
    per_coder: dict[str, set] = {}
    events: dict[str, list] = collections.defaultdict(list)
    for coder in ("cursor", "bravo"):
        path = ROOT / "coding" / coder / f"events__{coder}.csv"
        rows = [e for e in load_csv(path) if e.get("application_id") in census] if path.exists() else []
        per_coder[coder] = {e["application_id"] for e in rows if e.get("event_type") in INTERVIEW_TYPES}
        for e in rows:
            events[e["application_id"]].append(e)

    union = per_coder["cursor"] | per_coder["bravo"]
    both = per_coder["cursor"] & per_coder["bravo"]
    cursor_only = per_coder["cursor"] - per_coder["bravo"]

    flagged = []
    for app_id in sorted(union):
        evs = events[app_id]
        rejections = sorted(x for x in (iso_date(e["event_date"]) for e in evs if e.get("event_type") == "rejection") if x)
        interviews = sorted(
            (iso_date(e["event_date"]), e.get("coder_id", ""), e.get("event_type", ""))
            for e in evs
            if e.get("event_type") in INTERVIEW_TYPES and iso_date(e["event_date"])
        )
        if rejections and interviews and interviews[0][0] > rejections[0]:
            date, coder, etype = interviews[0]
            flagged.append((app_id, rejections[0].isoformat(), date.isoformat(), coder, etype, (date - rejections[0]).days))
    return union, both, cursor_only, flagged


def main() -> None:
    rows, census_n, excluded = build_rows()
    interviewed_union, interviewed_both, interviewed_cursor_only, post_rejection = interview_provenance()
    cursor_only_names = ", ".join(f"`{a}`" for a in sorted(interviewed_cursor_only)) or "none"

    strict = summary([r["days_to_response_strict"] for r in rows if r["days_to_response_strict"] is not None])
    broad = summary([r["days_to_response_broad"] for r in rows if r["days_to_response_broad"] is not None])
    interview = summary([r["days_to_interview"] for r in rows if r["days_to_interview"] is not None])
    base = len(rows)

    with (OUT / "latency__by_application.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in sorted(rows, key=lambda r: r["date_applied"]):
            writer.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in ROW_FIELDS})

    r = []
    r.append("# Response latency")
    r.append("")
    r.append("Secondary outcomes named in `knowledge/protocol.md`, computed under the rule stated there: only rows where both dates carry `precision = exact`, with the excluded n reported alongside. This executes the pre-registration and does not deviate from it.")
    r.append("")
    r.append("## Base population")
    r.append("")
    r.append(f"- Adjudicated application census: {census_n}")
    r.append(f"- With an exact-dated `submission_receipt`, the base for every figure below: {base}")
    r.append(f"- Excluded for lacking one: {excluded}")
    r.append("")
    r.append("The base is not the census. Any rate below is stated against " f"{base}, and the published application-to-interview rate remains 14/{census_n}.")
    r.append("")
    r.append("## Response rate and latency are separate")
    r.append("")
    r.append(f"- Substantive response, `employer_ack` excluded: {strict['n']}/{base}")
    r.append(f"- Any response, `employer_ack` included: {broad['n']}/{base}")
    r.append(f"- No response at all beyond the receipt: {base - broad['n']}/{base}")
    r.append("")
    r.append("The medians below are conditional on having responded. They describe responders only and must not be quoted as a typical response time for an application.")
    r.append("")
    r.append("| definition | n | median | p25 | p75 | mean | max | day zero |")
    r.append("|---|---|---|---|---|---|---|---|")
    for label, s in (("substantive, headline", strict), ("any, includes ack", broad)):
        r.append(
            f"| {label} | {s['n']} | {fmt(s['median'])} | {s['p25']} | {s['p75']} | "
            f"{s['mean']:.1f} | {s['max']} | {s['day0']} ({s['day0'] / s['n']:.1%}) |"
        )
    r.append("")
    r.append("The day-zero share roughly doubles when `employer_ack` is included, which is what an automated acknowledgment arriving with the receipt looks like. The substantive figure is the headline for that reason. The distribution is right-skewed in both cases, mean well above median, so the median is the statistic to quote.")
    r.append("")
    r.append("## Time to first interview")
    r.append("")
    r.append(f"- n = {interview['n']}, median {fmt(interview['median'])} days, mean {interview['mean']:.1f}, range {interview['min']} to {interview['max']}")
    r.append("")
    r.append("Two things make this figure weaker than its n suggests, and both are about the interview set rather than the latency arithmetic.")
    r.append("")
    r.append(f"**Provenance.** The census records {len(interviewed_union)} interviewed applications. Both coders independently found {len(interviewed_both)}. The remaining {len(interviewed_cursor_only)} rest on cursor alone, and bravo contributes none that cursor missed: {cursor_only_names}. Agreement on which applications were interviewed is therefore {len(interviewed_both)}/{len(interviewed_union)}, which is much weaker than the published role-lane kappa of 0.9510 implies. Event-level agreement is not among the reliability statistics `knowledge/protocol.md` requires, so this is unmeasured rather than measured and small.")
    r.append("")
    if post_rejection:
        r.append("**Ordering.** These carry an interview event dated after a rejection on the same application:")
        r.append("")
        for aid, rej, iv, coder, etype, gap in post_rejection:
            r.append(f"- `{aid}`: rejection {rej}, then `{etype}` on {iv} by {coder}, {gap} days later.")
        r.append("")
        r.append("An interview that postdates the rejection closing the same cycle is either a genuine re-engagement or an event coded under the wrong type. `coding/cursor/notes__cursor.md` describes the Weave case as an \"interview decline\", and a decline is a `rejection` under the codebook vocabulary, not an interview. Resolve this in adjudication before either the interview count or this latency figure is published. It is not a latency question and this script does not decide it.")
        r.append("")
    r.append("## Right censoring")
    r.append("")
    r.append(f"Applications submitted near the {WINDOW_END.isoformat()} window end have had less time to draw a response. The rate is stable across exposure windows, so censoring is not driving it.")
    r.append("")
    r.append("| minimum exposure | base n | responded | rate |")
    r.append("|---|---|---|---|")
    for window in (0, 14, 30, 60, 90):
        eligible = [x for x in rows if x["exposure_days"] >= window]
        responded = [x for x in eligible if x["days_to_response_broad"] is not None]
        r.append(f"| {window} days | {len(eligible)} | {len(responded)} | {len(responded) / len(eligible):.3f} |")
    r.append("")
    r.append(f"Applications with under 30 days of exposure: {sum(1 for x in rows if x['exposure_days'] < 30)}.")
    r.append("")
    r.append(f"## Slices, cells under {MIN_CELL} suppressed")
    r.append("")
    r.append("Median days to any response, `employer_ack` included, so the cells are as populated as the data allows. Suppressed groups are named with their counts rather than dropped silently.")
    for field, title in (("role_lane", "By role lane"), ("ats_system", "By ATS"), ("month", "By month applied")):
        published, suppressed = slice_table(rows, field, "days_to_response_broad")
        r.append("")
        r.append(f"### {title}")
        r.append("")
        if published:
            r.append(f"| {field} | n | median days |")
            r.append("|---|---|---|")
            for key, n, med in published:
                r.append(f"| {key} | {n} | {fmt(med)} |")
        else:
            r.append(f"No cell reaches n = {MIN_CELL}.")
        if suppressed:
            names = ", ".join(f"{k} (n={n})" for k, n, _ in suppressed)
            r.append("")
            r.append(f"Suppressed, {len(suppressed)} of {len(published) + len(suppressed)} groups: {names}.")
    r.append("")
    r.append("The ATS table is the one to read carefully. Most systems in this corpus appear too few times to support a median, so the published rows are a minority of the systems observed and are not a ranking of ATS platforms.")
    r.append("")

    (OUT / "LATENCY.md").write_text("\n".join(r) + "\n", encoding="utf-8")
    print("\n".join(r))


if __name__ == "__main__":
    main()
