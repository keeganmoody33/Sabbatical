# Query manifest

Tracks every retrieval query against the study window 2025-06-01 to 2026-08-29. A query is `done` only when the API returns no `nextPageToken`.

| id | source | query | window | status | threads | logs |
|---|---|---|---|---|---|---|
| Q1 | Gmail | receipt phrases OR 12 ATS domains | 2025-06-01 to 2025-11-03 | **done**, 3 pages, no further token | 129 | 001, 002, 003 |
| Q2a | Gmail | Q1 set plus wellfound, greenhouse-mail, dover.io, paycom | 2025-11-02 to 2026-01-15 | **done**, 1 page | 39 | 004 |
| Q2b | Gmail | same | 2026-01-15 to 2026-04-16 | **done**, 3 pages | 124 | 005, 006, 007 |
| Q2c | Gmail | same | 2026-04-15 to 2026-06-16 | **done**, 2 pages | 100 | 008, 009 |
| Q2d | Gmail | same | 2026-06-15 to 2026-08-30 | **done**, 4 pages | 179 | 010, 011, 012, 013 |
| Q3 | Gmail | aggregator and discovered channels: ziprecruiter, talentpluto, jobmail, jobgether, mercor, a4m.theladders, wellfound, huzzle, applitrack, frontlineed, hirebridgemail, certn, micro1, getcrate | full window | **done**, 4 pages | 163 | 014, 015, 016, 017 |
| Q3b | Gmail | remaining discovered employer and ATS domains not yet swept | full window | pending | | |
| Q4 | Gmail | rejection and closure language without the word "application" | full window | **done**, 2 pages | 74 | 018, 019 |
| Q5 | Gmail | `in:sent` application, resume, portfolio, careers language | full window | **done**, 1 page | 36 | 020 |
| Q6 | Gmail | `in:sent` job application language, no attachment | full window | pending | | |
| Q7 | Gmail | interview and scheduling language | full window | in progress, page 1 of n, token `tok_f6fa12a39fc7` | 50 so far | 021 |
| Q8 | Calendar | all events, 90 day blocks, no keyword filter | full window | pending | | |
| Q9 | Gmail | `in:anywhere` repeat of Q1 including spam and trash | full window | pending | | |
| Q10 | Gmail | ZipRecruiter, Talentpluto, Mercor, Wellfound, Ladders Apply4Me aggregator channels, discovered mid-sweep | full window | pending | | |

## Sender domains discovered, to be swept in Q3

From Q1: hi.wellfound.com, paycomonline.com, comeet-notifications.com, notifications.dover.io, us.greenhouse-mail.io, eu.greenhouse.io, careers.scaleops.com, candidates.workablemail.com, pinteresttalenthub.com, appreview.gem.com, ats.rippling.com, mail.beehiiv.com

From Q2a and Q2b: us.greenhouse-jobs.com, eu.greenhouse-mail.io, ceipalmail.com, companycam.com, cresta.ai, lumenalta.com, virtru.com, saveurdays.com, micro1.ai, agroknow.com, proofpoint.com, remail.wellfound.com, jobright.ai, vercel.com, newrelic.com, breezy-mail.com, recruitee.com subdomains, hypergen.io, beautiful.ai, orchestry.com, testgorilla.com, sailpoint myworkday, thomsonreuters myworkday

## Stop rule

Retrieval is exhaustive when Q1 through Q9 all return no further page token, and when a final pass on any new sender domains discovered in Q2 through Q9 also returns nothing new. New domains keep appearing, so expect at least one added round.

## Running total

994 threads captured across logs 001 to 021. All five window slices of the phrase-and-ATS-domain sweep (Q1, Q2a, Q2b, Q2c, Q2d) are exhausted. Queries Q3 through Q10 remain.

## Exclusions overturned by artifact, so far

| entity | prior classification | artifact found |
|---|---|---|
| Weave | recruiter-initiated, no application evidence | Greenhouse receipt 2025-07-27, post-interview decline 2026-08-18 |
| WorkOS | present in 212 ledger, absent from 247 | Tier A, marked Interviewed |
| Huzzle | talent-pool profile, excluded | Workable submission receipt 2026-06-04 plus required AI interview |
| Mercor | matching pathway, no direct application | six "Application Submitted" receipts from team@mercor.com |
| Talentpluto (x2) | attempted, incomplete | two Workable submission receipts 2026-07-12 with data copies |
| Atlanta Public Schools | attempted, candidate says not submitted | AppliTrack submission confirmation 2026-06-19 |
| DeKalb County School District | attempted, incomplete, one row | eleven position-filled notices naming ten distinct schools, 2026-07-08 to 2026-08-11 |
| PandaDoc | (retriever's own error in log 006) | employer rejection 2026-04-27 referencing the application |

## Progress

- Q1 complete. 129 threads captured across logs 001 to 003.
- Q1 alone surfaced roughly 55 to 60 candidate applications in a window both prior audits treated as containing one row.
- Q2a complete. 39 threads, log 004. Only about 4 candidates are new here, because this period was inside the earlier audit's search window.
- The contrast between Q1 and Q2a is itself a result. The same query, run over a period the prior audit searched, reproduces the existing ledger. Run over the period it did not search, it multiplies it. That is evidence the sweep is sound and the earlier census boundary, not the applicant's behavior, produced the empty 2025.
- Q2b complete. 124 threads across logs 005 to 007. Overwhelmingly confirmatory of the prior ledger, with a handful of genuine additions: Virtru, Lumenalta, Celonis, New Relic, Crossing Hurdles for Montauk Capital, PandaDoc (likely attempted), saveurdays.com, micro1 (opportunity register), and Ambrook Partnerships Lead as a second Ambrook application.
- One interview surfaced that the Interviews sheet does not contain: Hypergen, invitation dated 2026-04-14.
- Windows were split into quarters after Q1 hit three pages. Splitting keeps each query under the pagination ceiling and makes exhaustion verifiable per slice.
