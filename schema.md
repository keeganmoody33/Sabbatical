# Schema

The relational model behind the census: tables, grain, keys, and the unit of analysis for every
metric the paper reports.

This file does not define fields. `codebook.md` does, and it is the frozen instrument. This file
states what the codebook leaves implicit: what a row of each table *is*, what identifies it, how
the tables join, and which denominator each downstream number is computed against.

No dashes are used as punctuation in this file.

## Why the grain matters more than the fields

Every wrong number in the prior audits of this dataset came from a grain error rather than a field
error. A rejection thread counted as a second application is a grain error. A recruiter-run process
counted in an application denominator is a grain error. A re-application collapsed into its first
attempt is a grain error. The fields were fine in all three cases.

So the rule this schema exists to enforce: **decide what one row means before deciding what columns
it has.**

## Tables

### `applications`

**Grain.** One row per application cycle. Not one row per company, not one per role, not one per
email thread.

**Primary key.** `application_id`, formatted `company_slug|role_slug|c{n}`, for example
`fossa|gtm-engineer|c2`. The three components correspond to `company_canonical`, `role_as_listed`,
and `cycle`.

**Why cycle is in the key.** A second submission to the same company and role is a separate row,
but only when a terminal outcome closed the first. The terminal outcome is what licenses the second
cycle to exist. FOSSA: receipt 2026-04-22, decline 2026-05-20, second receipt 2026-05-21. Attentive:
receipt 2026-06-22, decline 2026-07-07, second receipt 2026-07-15. A key of `company|role` collides
both pairs, and an earlier version of this dataset did exactly that. Three Pogo artifacts across two
systems with no terminal outcome between them stayed one cycle, which is the same rule running the
other direction.

**Register is a field, not a table.** `register` is `application` or `opportunity`. Both live here.
Only `register = application` enters the census. Moving opportunity rows to a separate sheet would
lose the history of why a row is out, so they are filtered rather than relocated.

**Files at this grain.**

| File | Rows | What it is |
|---|---|---|
| `coding/bravo/applications__bravo.csv` | 228 | Blind coder output. Frozen. |
| `coding/cursor/applications__cursor.csv` | 231 | Blind coder output. Frozen. |
| `coding/platform/applications__freeze2.csv` | 134 | Platform exports mapped to the schema. Generated. |
| `adjudication/applications__adjudicated.csv` | 221 | The application census. Generated. |
| `adjudication/applications__full_census.csv` | 298 | Census plus net-new platform rows. Generated. |

The coder files carry 28 columns. The adjudicated files carry those 28 plus `adjudication_source`
and `adjudication_note`, which record where each surviving row came from and under which rule.

### `events`

**Grain.** One row per timestamped interaction on one application. Many per application.

**Primary key.** `event_id`, formatted `{application_id}|e{n}`.

**Foreign key.** `events.application_id` references `applications.application_id`, within the same
coder. An event may never exist without a parent application row. `data_quality_report.md` section
6 checks this on every run and currently reports zero orphans across both coders.

**This table is where outcomes live.** `interviewed`, `n_rounds`, `days_to_first_response`, and
`days_to_interview` are all derived from it and are never stored on an application row. A stored
rollup and a stored event list will eventually disagree, and then neither can be trusted.

The consequence is structural and shows up throughout the results: a row with no employer-side
artifact has no events, so it can be counted in a denominator but can never contribute to a
numerator.

### `exclusions`

**Grain.** One row per candidate that was considered and rejected.

**Primary key.** `candidate_id`, unique within a coder.

Rejected rows are kept visible rather than deleted. The `what_would_promote_it` column names the
specific artifact that would move the row into the census, which turns the exclusion list into a
work queue rather than a graveyard.

### `platform_match`

**Grain.** One row per platform export row, carrying its resolution against Freeze 1.

**File.** `adjudication/platform_match.csv`, 134 rows.

**Key columns.** `match_status` is one of `overlap`, `net_new`, `ambiguous`, or a non-census status.
`parent_id` is populated only on `overlap`. `candidate_parent_ids` is populated only on `ambiguous`
and lists the rows the matcher could not choose between.

`ambiguous` exists because a refusal that produces no distinguishable output is not conservative,
it is an unrecorded merge decision. Ambiguous rows are held out of the full census on the ground
that an omitted row is recoverable and an inflated census is not. Zero rows hit that branch on the
current corpus.

### `latency__by_application`

**Grain.** One row per census application that carries an exact-dated submission receipt. 196 rows.

**Foreign key.** `application_id` references the adjudicated census.

This is a derived table, not a source. It exists because the response-time metrics have a different
denominator from the census and that difference has to be visible in the data rather than in a
footnote.

## How the tables join

```
applications (221 census / 298 full)
    |
    | application_id  1..n
    v
events (414 bravo, 279 cursor)          exclusions (44 bravo, 45 cursor)
    |
    | derives
    v
latency__by_application (196)           views/*.csv
```

Platform rows enter through `platform_match`, which resolves each export row against the census
before anything is added to it. Nothing is appended to a census without a recorded match decision.

## Unit of analysis, per metric

This is the section the codebook does not have, and the one that prevents most published-number
errors. Every metric below names what one observation is and what it is divided by.

| Metric | Unit of analysis | Numerator | Denominator | View |
|---|---|---|---|---|
| Application census | per-opportunity | n/a | n/a, it is a count: 221 | `adjudication/applications__adjudicated.csv` |
| Full census | per-opportunity | n/a | n/a, it is a count: 298 | `adjudication/applications__full_census.csv` |
| Application to interview rate | per-opportunity | applications with at least one interview event | all census applications | `funnel_by_role_lane.csv`, `funnel_by_evidence_class.csv` |
| Interview rate by lane | per-opportunity | interviewed in the lane | applications in the lane | `funnel_by_role_lane.csv` |
| Substantive response rate | per-opportunity | applications with a non-ack response | 196 with an exact-dated receipt | `latency_by_slice.csv` |
| Any response rate | per-opportunity | applications with any response | 196 with an exact-dated receipt | `latency_by_slice.csv` |
| Median days to first response | per-opportunity, conditional on responding | n/a | responders only, count printed per row | `latency_by_slice.csv` |
| Time to first interview | per-opportunity, conditional on interviewing | n/a | 11 with both dates exact | `adjudication/LATENCY.md` |
| Applications per month | per-month | n/a | 195 exact-dated rows, 26 excluded | `monthly_trend.csv` |
| Origin channel share | per-opportunity | n/a | stated per stratum, 221 or 298 | `origin_coverage.csv` |
| Role lane agreement (kappa) | per-opportunity | n/a | 211 rows both coders coded | `adjudication/PRE-ADJUDICATION.md` |

Three denominators are in play and they are not interchangeable: **221** (the census), **196** (the
exact-dated receipt base), and **298** (the full census including platform-only rows). Any figure
quoting one of them must name it. The 298 in particular adds 77 rows that carry no events, so an
interview rate against it is arithmetically smaller for a reason that has nothing to do with the
search.

## Precision is a field, not an assumption

`date_precision` is `exact`, `relative_display`, `evidence_bound`, or `unknown`, and every date has
one. A LinkedIn stamp reading "2mo ago" is `relative_display` and carries `date_capture`, the date
the stamp was read. It is never upgraded to a calendar date, because "2mo ago" read on 2026-08-29 is
a range, and writing 2026-06-29 into a date column would convert a range into a false fact.

Consequence: the monthly series runs on `date_precision = exact` only, n = 195, with the 26
excluded rows printed beside it.

## Two things this schema does not have

**No `company_stage` field.** Startup, growth, and enterprise are not recorded anywhere in this
dataset, so no cut by company size or stage is available. This is a genuine gap rather than a
suppressed cell.

**No usable origin on most rows.** `discovery_source` exists and is populated, but its value is
`unknown` on 206 of 221 census rows. The field is in the schema. The data is not in the field.

## A hazard worth naming

The codebook exists twice: `codebook.md` at the repository root and `knowledge/03-codebook.md`. They
already differ in wording, and the root copy carries the evidence-tier and counting-rule sections
the kit copy delegates elsewhere. `pipeline/data_quality.py` parses the **root** copy, so that is
the copy the validator treats as authoritative. Two copies of a frozen instrument is exactly the
condition the codebook's own first design principle warns about, and it should be resolved to one
file with the other pointing at it.
