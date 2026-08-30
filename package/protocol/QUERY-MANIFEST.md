# Query manifest

Tracks every retrieval query against the study window 2025-06-01 to 2026-08-29. A query is `done` only when the API returns no `nextPageToken`.

Last updated 2026-08-29 after Q7 reached exhaustion.

| id | source | query | window | status | threads | logs |
|---|---|---|---|---|---|---|
| Q1 | Gmail | receipt phrases OR 12 ATS domains | 2025-06-01 to 2025-11-03 | **done**, 3 pages, no further token | 129 | 001, 002, 003 |
| Q2a | Gmail | Q1 set plus wellfound, greenhouse-mail, dover.io, paycom | 2025-11-02 to 2026-01-15 | **done**, 1 page | 39 | 004 |
| Q2b | Gmail | same | 2026-01-15 to 2026-04-16 | **done**, 3 pages | 124 | 005, 006, 007 |
| Q2c | Gmail | same | 2026-04-15 to 2026-06-16 | **done**, 2 pages | 100 | 008, 009 |
| Q2d | Gmail | same | 2026-06-15 to 2026-08-30 | **done**, 4 pages | 179 | 010, 011, 012, 013 |
| Q3 | Gmail | aggregator and discovered channels: ziprecruiter, talentpluto, jobmail, jobgether, mercor, a4m.theladders, wellfound, huzzle, applitrack, frontlineed, hirebridgemail, certn, micro1, getcrate | full window | **done**, 4 pages | 163 | 014, 015, 016, 017 |
| Q3b | Gmail | remaining discovered employer and ATS domains not yet swept, now including the Q7 batch below | full window | pending | | |
| Q4 | Gmail | rejection and closure language without the word "application" | full window | **done**, 2 pages | 74 | 018, 019 |
| Q5 | Gmail | `in:sent` application, resume, portfolio, careers language | full window | **done**, 1 page | 36 | 020 |
| Q6 | Gmail | `in:sent` job application language, no attachment | full window | pending | | |
| Q7 | Gmail | interview and scheduling language | full window | **done**, 4 pages, no further token | 195 | 021, 022, 023, 024 |
| Q7b | Gmail | targeted origin check: pin.com, cyft.ai, getcrate.app, inertiagrowth.com | full window | **done**, 1 page | 13 | 025 |
| Q8 | Calendar | all events, 90 day blocks, no keyword filter | full window | pending | | |
| Q9 | Gmail | `in:anywhere` repeat of Q1 including spam and trash | full window | pending | | |
| Q10 | Gmail | ZipRecruiter, Talentpluto, Mercor, Wellfound, Ladders Apply4Me aggregator channels, discovered mid-sweep | full window | pending | | |

## Sender domains discovered, to be swept in Q3b

From Q1: hi.wellfound.com, paycomonline.com, comeet-notifications.com, notifications.dover.io, us.greenhouse-mail.io, eu.greenhouse.io, careers.scaleops.com, candidates.workablemail.com, pinteresttalenthub.com, appreview.gem.com, ats.rippling.com, mail.beehiiv.com

From Q2a and Q2b: us.greenhouse-jobs.com, eu.greenhouse-mail.io, ceipalmail.com, companycam.com, cresta.ai, lumenalta.com, virtru.com, saveurdays.com, micro1.ai, agroknow.com, proofpoint.com, remail.wellfound.com, jobright.ai, vercel.com, newrelic.com, breezy-mail.com, recruitee.com subdomains, hypergen.io, beautiful.ai, orchestry.com, testgorilla.com, sailpoint myworkday, thomsonreuters myworkday

**New from Q7 and Q7b:** every.to, bask.health, bx.studio, glytec.com, discolike.com, starbridge.ai, getstarbridge.xyz, inertiagrowth.com, cyft.ai, pin.com, getcrate.app, teamtailor-mail.com, orchestry-software-inc.breezy-mail.com, ajbubb.com, thehog.ai, hellopearl.com, dexian.com, newtonsoftware.com

## Stop rule

Retrieval is exhaustive when Q1 through Q10 all return no further page token, and when a final pass on any new sender domains discovered along the way also returns nothing new. Q7 alone added eighteen domains, so at least one more added round is required.

## Running total

**1152 threads captured across logs 001 to 025.** Q1, Q2a to Q2d, Q3, Q4, Q5, Q7 and Q7b are exhausted. Q3b, Q6, Q8, Q9 and Q10 remain.

## Exclusions overturned by artifact, so far

| entity | prior classification | artifact found |
|---|---|---|
| Weave | recruiter-initiated, no application evidence | Greenhouse receipt 2025-07-27, post-interview decline 2026-08-18 |
| WorkOS | present in 212 ledger, absent from 247 | Tier A, marked Interviewed. Full TopHire sequence to a booked screen, log 023 |
| Huzzle | talent-pool profile, excluded | Workable submission receipt 2026-06-04 plus required AI interview |
| Mercor | matching pathway, no direct application | six "Application Submitted" receipts from team@mercor.com |
| Talentpluto (x2) | attempted, incomplete | two Workable submission receipts 2026-07-12 with data copies |
| Atlanta Public Schools | attempted, candidate says not submitted | AppliTrack submission confirmation 2026-06-19 |
| DeKalb County School District | attempted, incomplete, one row | eleven position-filled notices naming ten distinct schools, 2026-07-08 to 2026-08-11 |
| PandaDoc | (retriever's own error in log 006) | employer rejection 2026-04-27 referencing the application |
| Inertia Growth | not in either workbook | self-initiated email application with resume 2025-07-26, employer rejection naming the role 2025-07-30, log 025 |
| Pin | not in either workbook | interview, assignment, employer feedback and rejection, all 2025-07-07, log 024 |

## Exclusions confirmed or newly created

| entity | ruling | reason |
|---|---|---|
| Luzmo | exclusion holds | outreach only via Jobright, no submission artifact, log 021 |
| gtm-engineering.io (Jorge Macias) | exclude | nine invitations across nine months, a standing meeting series, not an interview, log 023 |
| Google, eml_f8aba22fb35b | exclude | Keegan booked it himself as lecturesfrom for "Intro to Cloud Partnership Program", log 024 |
| getcrate.app / "Umicas ATS" | exclude, new class | four messages matching a GTM candidate to backend SWE roles at Google, OpenAI and Crate in four days, log 025 |
| eml_93bc653507a1 "Rippling" | exclude pending adjudication, same class | newsletter delivery domain, Software Engineering Manager Banking role, sent twice, log 023 |

## Open retrieval items

1. **Pin origin.** The "Next Steps" thread parent predates 2025-07-07 and is not from pin.com. One `get_thread` on `gth_fe49801b0505bbbc` decides census versus opportunity register.
2. **Cyft origin.** Nothing in email. Check Q8 Calendar and Q9.
3. **Exa contradiction.** The manifest lists Exa as a new application in the 2025 window, but the Exa thread found in Q7 is a product conversation triggered by an API signup. Two different artifacts or one error. Do not merge.
4. **eml_909e9737534a.** Appears as a cc on a calendar invite. May be an integration artifact rather than a mailbox. Verify before assuming a third address exists.
5. **Reschedule event type.** Orchestry and Inertia Growth each produced multiple reschedules. `03-codebook.md` has no event type for this. Adding one changes prior rows, so decide before the next harvest.

## Progress

- Q7 is the highest-yield query in the sweep so far on process depth rather than volume. It surfaced six complete or near-complete processes inside the 2025 window that both prior audits treated as empty: Pin, Cyft, Starbridge, Inertia Growth, plus Headway and Circle receipts.
- The contrast established at Q1 versus Q2a holds and strengthens. Queries run over the period the earlier audit searched reproduce the existing ledger. Queries run over the period it did not search multiply it. The empty 2025 is a census boundary artifact, not applicant behaviour.
- Scheduling churn is now a visible and unmeasured feature. Orchestry produced six artifacts in 72 hours for one req. Inertia Growth produced four across five days. Counting one row per application discards this entirely.
