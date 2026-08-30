<!-- kit-meta
file: 02-current.md
tier: 2 (volatile)
created: 2026-08-29 13:37 ET
updated: 2026-08-30 ET
review-by: 2026-09-30
sources: [S1] [S2] [S3] [S4] [S5] [S6] plus this repository's own generated outputs
-->

# Current state

Everything here is assumed stale until the meta block says otherwise. Delete and regenerate freely.

The numbers below are the output of this freeze, reproducible with `make check`. The prior-audit
figures that used to sit at the top of this file (247 applications, 11 interviews, 4.45 percent) are
**not findings** and have been moved to the superseded section at the bottom.

## Headline numbers

| Metric | Value | Source |
|---|---|---|
| Application census, employer-side proof | 221 | `adjudication/applications__adjudicated.csv` |
| Full census, including platform-only rows | 298 | `adjudication/applications__full_census.csv` |
| Interviewed applications, derived from events | 13 | `views/funnel_by_role_lane.csv` |
| Application to interview rate | 13/221 | same |
| Latency base, exact-dated receipt | 196 | `adjudication/latency__by_application.csv` |
| Any response | 100/196 | `views/latency_by_slice.csv` |
| Substantive response | 79/196 | same |
| No response beyond the receipt | 96/196 | derived |
| Median days to substantive response, responders only | 7 | `adjudication/LATENCY.md` |
| Time to first interview | n = 11, median 6 | same |
| Census completeness | not published | no method available, see below |

## Role lanes, 221 applications

| Lane | n | Interviewed |
|---|---|---|
| explicit_gtm_engineering | 86 | 9 |
| unspecified | 35 | 2 |
| sales_bd_partnerships | 28 | 0 |
| growth_demand_marketing | 22 | 2 |
| other | 18 | 0 |
| sales_solutions_engineering | 15 | 0 |
| revops_gtm_ops_strategy | 9 | 0 |
| product_ai_technical | 8 | 0 |

All 13 interviews sit in three lanes. The five lanes covering the other 78 applications produced
none. Wilson intervals in `views/funnel_by_role_lane.csv`. Descriptive only.

## Monthly distribution

One version now, not two. Exact-dated rows only, n = 195, with 26 non-exact rows excluded and
reported alongside. From `views/monthly_trend.csv`:

2025-06 5, 2025-07 19, 2025-08 16, 2025-09 0, 2025-10 0, 2025-11 1, 2025-12 2, 2026-01 7,
2026-02 10, 2026-03 21, 2026-04 26, 2026-05 22, 2026-06 28, 2026-07 33, 2026-08 5.

The two prior curves that disagreed are both superseded. Zero in September and October 2025 is a
count of exact-dated rows, not a claim of zero activity.

## Origin: the finding is an absence

`discovery_source` is `unknown` on 206 of 221 census rows. On the full census, 71 rows know they came
from LinkedIn and none of them has an observable outcome, because a platform applied-list row carries
no employer-side artifact and therefore no events. The overlap that could support a channel analysis
is 15 rows of 221.

No origination-channel conversion figure exists anywhere in this repository, and none should be
produced without new data. `company_stage` does not exist in the schema at all.

See `views/origin_coverage.csv` and `paper/PAPER.md` section 3.2.

## Reliability

- bravo 228 rows, cursor 231, intersection 211
- role lane percent agreement 0.9621, Cohen's kappa 0.9510
- include percent agreement 0.9905, kappa 0.7452
- interview set found by both coders: 10 of 13

The last line is the weakest link in the interview-based findings. Event-level agreement is not among
the statistics the protocol requires, so it is unmeasured rather than measured and small.

## Open threads

| Thread | Status | Next action |
|---|---|---|
| Ladders applied list | Unmet stop condition | Export the full applied list |
| YC Work at a Startup dashboard | Unmet stop condition | Inspect the dashboard directly |
| LinkedIn pages beyond 10, and an Easy Apply label | Partial | LinkedIn data download, Job Applications.csv. The label is what would make capture recapture possible |
| Personal Gmail Q7 page 2 and beyond, Q6, Q3b, Q9 | Partial | Requires a connector on `keeganmoody33@gmail.com` |
| Personal Gmail calendar | Not reachable | Same |
| Talentpluto and Jobgether underlying employers | Partial | Resolve or formally exclude |
| 212 to 163 reconciliation | Open | Workbooks absent, may be unreconstructable |
| `jobmail-io|growth-lead|c1` contradiction | Open, found 2026-08-30 | Interview event against a stored `rejected_no_interview`, one coder. Needs the artifact |
| Codebook exists twice and the copies differ | Open | Resolve to one file, point the other at it |
| Three rows carry a city in `work_type` | Open by design | Coder files are frozen. Reported by the validator on every run |

## Paper status

Drafted. `paper/PAPER.md`, Abstract through Appendix, roughly 3,100 words plus tables.

| File | State |
|---|---|
| `paper/PAPER.md` | Draft, awaiting review |
| `paper/NUMBERS.md` | Every numeric claim mapped to its view |
| `paper/FIGURES.md` | Six figures specified, none rendered. No plotting library in the environment |
| `paper/NAMED-COMPANIES.md` | Naming pass as a checklist. **Seven still-open processes need a decision** |
| `paper/METHODS.md`, `paper/RESULTS.md`, `paper/DEFECTS.md` | Unchanged, still the internal record |
| `translation/SUBSTACK-DRAFT.md` | Unchanged, the companion methods-translation piece |

**Nothing has been published.** No Substack post, no LinkedIn post. Both remain downstream of the
author's approval of the draft.

## Superseded, kept so nobody reintroduces them

These are prior-audit figures. They are not the output of this freeze and must not be quoted as
findings. The full blocklist with reasons is in `paper/RESULTS.md`.

- 247 confirmed unique applications
- 11 applied companies interviewed
- 4.45 percent application to interview rate
- Census completeness of 88 to 93 percent, or 80 to 85 percent
- The two disagreeing monthly curves from the 212-row and 247-row ledgers

## Changelog

- 2026-08-29 13:37 ET: created from [S1] [S2] [S3] [S4] [S5] [S6].
- 2026-08-30 ET: rewritten against this freeze's own output. Prior-audit headline figures moved to
  Superseded. Monthly curve reduced to the one publishable version. Origin section added. Paper
  status updated from "nothing drafted" to drafted and awaiting review.
