<!-- kit-meta
file: 02-current.md
tier: 2 (volatile)
created: 2026-08-29 13:37 ET
updated: 2026-08-30 ET (Freeze 3)
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
| Application census, employer-side proof | 223 | `adjudication/applications__adjudicated.csv` |
| Full census, including platform-only rows | 317 | `adjudication/applications__full_census.csv` |
| Interviewed applications, derived from events | 14 | `views/funnel_by_role_lane.csv` |
| Application to interview rate | 11/223 | same |
| Latency base, exact-dated receipt | 197 | `adjudication/latency__by_application.csv` |
| Any response | 100/197 | `views/latency_by_slice.csv` |
| Substantive response | 79/197 | same |
| No response beyond the receipt | 97/197 | derived |
| Median days to substantive response, responders only | 7 | `adjudication/LATENCY.md` |
| Time to first interview | n = 8, median 5.5 | same |
| Census completeness | not published | no method available, see below |

## Role lanes, 223 applications

| Lane | n | Interviewed |
|---|---|---|
| explicit_gtm_engineering | 92 | 10 |
| sales_bd_partnerships | 31 | 0 |
| unspecified | 25 | 2 |
| growth_demand_marketing | 23 | 2 |
| other | 18 | 0 |
| sales_solutions_engineering | 16 | 0 |
| revops_gtm_ops_strategy | 10 | 0 |
| product_ai_technical | 8 | 0 |

All 11 interviews sit in three lanes. The five lanes covering the other 83 applications produced
none. Wilson intervals in `views/funnel_by_role_lane.csv`. Descriptive only.

## Monthly distribution

One version now, not two. Exact-dated rows only, n = 196, with 27 non-exact rows excluded and
reported alongside. From `views/monthly_trend.csv`:

2025-06 5, 2025-07 19, 2025-08 16, 2025-09 0, 2025-10 0, 2025-11 1, 2025-12 2, 2026-01 7,
2026-02 10, 2026-03 21, 2026-04 27, 2026-05 22, 2026-06 28, 2026-07 33, 2026-08 5.

The two prior curves that disagreed are both superseded. Zero in September and October 2025 is a
count of exact-dated rows, not a claim of zero activity.

## Origin: the finding is an absence

`discovery_source` is `unknown` on 208 of 223 census rows. On the full census, 88 rows know they came
from LinkedIn and none has an observable outcome, because a platform applied-list row carries no
employer-side artifact and therefore no events.

Freeze 3 sharpened this into three tiers, in `views/origin_recoverability.csv`: origin captured at
write time on 15 of 223, recoverable afterwards on 60 more only because a platform logged them, and
unrecoverable on the remaining 148. Recovered values are not written into `discovery_source`.

No origination-channel conversion figure exists anywhere in this repository, and none should be
produced without new data. `company_stage` does not exist in the schema at all.

See `views/origin_coverage.csv` and `paper/PAPER.md` section 3.2.

## Reliability

- bravo 228 rows, cursor 231, intersection 211
- role lane percent agreement 0.9621, Cohen's kappa 0.9510
- include percent agreement 0.9905, kappa 0.7452
- interview set found by both coders: 9 of 11

The last line is the weakest link in the interview-based findings. Event-level agreement is not among
the statistics the protocol requires, so it is unmeasured rather than measured and small.

## Open threads

| Thread | Status | Next action |
|---|---|---|
| Ladders applied list | Unmet stop condition | Export the full applied list |
| LinkedIn Easy Apply channel label | Unmet | The Freeze 3 export has no such flag. Capture recapture stays unmeasured |
| YC Work at a Startup dashboard | Unmet stop condition | Inspect the dashboard directly |
| LinkedIn pages beyond 10 | Met at Freeze 3 | The full data download arrived, 107 rows with exact dates |
| Personal Gmail Q7 page 2 and beyond, Q6, Q3b, Q9 | Partial | Requires a connector on `keeganmoody33@gmail.com` |
| Personal Gmail calendar | Not reachable | Same |
| Talentpluto and Jobgether underlying employers | Partial | Resolve or formally exclude |
| 212 to 163 reconciliation | Open | Workbooks absent, may be unreconstructable |
| `jobmail-io|growth-lead|c1` contradiction | Open, found 2026-08-30 | Interview event against a stored `rejected_no_interview`, one coder. Needs the artifact |
| 20 companies only in the challenger workbook | Open | 15 arrive via the adopted export. The rest need artifacts |
| 53 LinkedIn recruiter threads | Deferred | A channel never harvested here. Mostly opportunity register |
| Pogo cluster, one to three requisitions | Open | Neither dataset has requisition-level evidence |
| Possible 2025-08-08 interview, company unknown | Open | If real, both datasets understate interviews |
| Codebook exists twice and the copies differ | Open | Resolve to one file, point the other at it |
| Three rows carry a city in `work_type` | Open by design | Coder files are frozen. Reported by the validator on every run |
| The Kiln, two interviews | Open, author recall 2026-08-30 | In no census row, no opportunity row and no challenger record. Origin a LinkedIn DM. Needs the thread |
| Pinn, Opsin Security, Hotglue, Mixmax interviews | Open, author recall 2026-08-30 | Four more interviewing processes absent from the corpus. See `knowledge/04-author-recall.md` |
| Hypergen interview disputed | Open, author recall 2026-08-30 | Author says none happened. Bravo coded `employer_ack` on an invitation, cursor coded an interview, adjudication took cursor |
| RevSpring, TestGorilla interviews disputed | Open, author recall 2026-08-30 | Both derive from a screen *request* or an *intro*. Answerable from artifacts already held |
| GTM Cafe Slack `#jobsandopportunities` | Never authorized | Named by the author as the origin of at least four interviewing processes. Not in the protocol source list |
| Mercor register | Open | Author says the rows were self-submissions through an account. Two sit in the opportunity register |

## Paper status

Drafted and split into two pieces.

`paper/PAPER.md` is the paper, Abstract through Appendix, roughly 3,350 words plus tables, inside the
1,800 to 3,000 target's neighbourhood. `paper/COMPANION.md` is the companion, roughly 2,150 words,
carrying the full origin analysis and the Freeze 3 challenge that the paper now summarizes and links
to. The split was made on 2026-08-30 at the author's instruction.

| File | State |
|---|---|
| `paper/PAPER.md` | Draft, awaiting review |
| `paper/NUMBERS.md` | Every numeric claim mapped to its view |
| `paper/FIGURES.md` | Six figures specified, none rendered. No plotting library in the environment |
| `paper/COMPANION.md` | Draft, awaiting review. Names 10 companies the paper does not |
| `paper/NAMED-COMPANIES.md` | Naming pass as a checklist, covering both pieces. **Eight still-open processes need a decision**, plus whether the companion publishes at all |
| `paper/DEFECTS.md` | Updated at Freeze 3 with the two reversals |
| `paper/METHODS.md`, `paper/RESULTS.md` | **Stale.** Still carry Freeze 2 figures. `PAPER.md` supersedes both |
| `challenge/CHALLENGE.md` | The adversarial reconciliation |
| `translation/SUBSTACK-DRAFT.md` | Unchanged, the companion methods-translation piece |

**Nothing has been published.** No Substack post, no LinkedIn post. Both remain downstream of the
author's approval of the draft.

## Superseded, kept so nobody reintroduces them

These are prior-audit figures. They are not the output of this freeze and must not be quoted as
findings. The full blocklist with reasons is in `paper/RESULTS.md`.

- 247 confirmed unique applications
- 221 applications and 13/221, superseded at Freeze 3
- The challenger workbook's 353, which mixes both registers
- 11 applied companies interviewed
- 4.45 percent application to interview rate
- Census completeness of 88 to 93 percent, or 80 to 85 percent
- The two disagreeing monthly curves from the 212-row and 247-row ledgers

## Changelog

- 2026-08-29 13:37 ET: created from [S1] [S2] [S3] [S4] [S5] [S6].
- 2026-08-30 ET, Freeze 3.1: role titles backfilled onto 11 census rows from the Jobright and LinkedIn
  artifacts already committed here, after re-reading the challenger for what it got right. Unspecified
  lanes 36 to 25, unspecified titles 40 to 29, explicit_gtm 87 to 92. Census, interviews and latency
  base unchanged. See `adjudication/title_backfill.csv`.
- 2026-08-30 ET, Freeze 3: LinkedIn formal export ingested, The Hog and BX Studio reversed to the
  application register on new evidence. 221 to 223, 13 to 14, 298 to 317, 196 to 197. Origin restated
  as three recovery tiers. See `challenge/CHALLENGE.md`.
- 2026-08-30 ET: rewritten against this freeze's own output. Prior-audit headline figures moved to
  Superseded. Monthly curve reduced to the one publishable version. Origin section added. Paper
  status updated from "nothing drafted" to drafted and awaiting review.
