# Results

These are the numbers this freeze can defend. Prior-audit figures 247, 11 interviews, and 4.45 percent are not restated as findings.

No dashes are used as punctuation in this file.

## Evidence class of this section

Until independent coder files are compared and adjudicated, any application total is a single-coder extract, not the census. The first publishable census number is the adjudicated `register = application` count plus the capture recapture interval (here: unmeasured) and the list of unmet or waived stop conditions.

## Search coverage (measured, not a census)

Harvest coverage of the frozen corpus, 2026-08-29:

- Gmail keeganmoody33@gmail.com, logs 001 to 021: 994 threads. Queries Q1 through Q5, Q3, Q4 exhausted. Q7 page 1 captured. Q7 page 2 and later, Q6, Q3b, Q9, Q10 on that mailbox were not run in this environment.
- Gmail 33@lecturesfrom.com, logs 022 to 029: 177 threads. Q6, Q7, Q3b, Q9, Q10 exhausted on this mailbox. Almost none were employment ATS receipts.
- Calendar 33@lecturesfrom.com: 31 events across five 90-day blocks with no keyword filter.
- Calendar transferred keegan@lecturesfrom.com: reachable and empty.
- Calendar keeganmoody33@gmail.com: not listed. Waived in writing.
- LinkedIn Job Applications.csv, Ladders full list, Jobright full export, YC dashboard, [S1] and [S2] workbooks: absent. Waived in writing.

Stop conditions: see `artifacts/STOP-CONDITIONS.md`. Personal Gmail Q7 is incomplete. Personal calendar is unswept.

## Completeness

95 percent completeness is a goal, not a verified claim. The intended estimator is stratified two-source capture recapture on the overlap where LinkedIn and external ATS mail could both have seen the same application.

That overlap stratum is unmeasured because Job Applications.csv is not in the corpus. No completeness percentage is published. No Lincoln Petersen estimate is computed.

Independence assumption, stated for when the export arrives: LinkedIn applied-list rows and employer ATS mail are not independent for Easy Apply, which is why that channel is excluded from the overlap stratum.

Likely bias direction if someone later runs an unstratified estimator anyway: Easy Apply is visible to LinkedIn and invisible to ATS mail, which would inflate apparent uniqueness and understate completeness.

## Single-coder extract (coder cursor, not adjudicated)

Coder `cursor` coded the frozen logs independently. This is not the paper total.

- Rows with `register = application`: 222
- Rows with `register = opportunity`: 10
- Events: 278
- Exclusions (employment-adjacent only; newsletters classified by sender domain are not one row per thread): 45

`evidence_class` on this extract is `employer_artifact` throughout. The platform_log stratum is empty because LinkedIn, Jobright, Ladders, and YC exports were absent.

Among the 222 application rows, 196 have `date_precision = exact` and 26 do not. A monthly series may use only the 196. The non-exact n is 26 and must sit next to any monthly chart.

Interviewed-ness is not stored. It is derived from `event_type` in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}. On this extract that derivation yields 15 interviewed application rows and 3 interviewed opportunity rows. The application-to-interview rate on the employer_artifact stratum would be 15/222. That rate is not adjudicated and is not a headline.

Exact-date monthly counts on `register = application` only: 2025-06 5, 2025-07 19, 2025-08 16, 2025-09 0, 2025-10 0, 2025-11 1, 2025-12 2, 2026-01 7, 2026-02 10, 2026-03 20, 2026-04 26, 2026-05 22, 2026-06 28, 2026-07 35, 2026-08 5. September and October 2025 being zero on exact dates does not mean zero search activity. Fullsteam 2025-09-29 is evidence_bound. Q1 harvest already showed that empty early months in prior audits were a search-boundary artifact.

## Two strata (method)

Report separately, after adjudication:

1. `evidence_class = employer_artifact` and `register = application`
2. Full census: that set plus `platform_log` rows, when those files exist

The application-to-interview rate uses only `register = application` in the denominator. Opportunity interviews (WorkOS, Mercor contract path, recruiter screens with no submission) are listed beside the rate, never inside it.

## Role lane

Do not publish a lane distribution until Cohen's kappa on `role_lane` is reported from at least two independent coders. See `adjudication/PRE-ADJUDICATION.md` once that file exists.

## Defects that condition any interview total

1. WorkOS: closed as opportunity. See `paper/DEFECTS.md`.
2. 212 to 163: still undocumented. Workbooks absent.
3. Cycle is in the key. FOSSA and Attentive second cycles are separate rows in the cursor extract.

## What a skeptic should not be shown as a finding

- 247
- 11 interviews
- 4.45 percent
- Naive capture recapture on 17 overlap versus 163 and 99
- Any Mixmax product onboarding row in the application denominator
- The Mercor Growth Strategist contract mixed into the application denominator
- Weave treated as recruiter-initiated with no application (the Greenhouse receipt is in log 002)

## After adjudication

Replace the single-coder extract above with:

- Adjudicated confirmed applications, employer_artifact stratum
- Adjudicated confirmed applications, full census (same as the first stratum in this freeze)
- Interviewed applications derived from events, in-census versus opportunity
- Application-to-interview rate on each stratum
- Role-lane distribution only with kappa
- Monthly series on `date_precision = exact` only, with approximate-date n annotated
