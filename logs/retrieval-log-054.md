<!-- kit-meta
file: retrieval-log-054.md
created: 2026-08-30
source: LinkedIn_Job_Threads_Analysis_2025-06_to_2026-08_1653.md (Claude coding of LinkedIn messages.csv, export dated 2026-08-23)
method: parse 54 job-related threads plus 20 uncertain; independent match to applications__full_census.csv, linkedin-applications-in-window.csv, and the opportunity register
-->

# Retrieval log 054

LinkedIn data export, messages and DM unpacking. No census total is changed. No interview is minted from this file.

## What arrived

One markdown analysis, not `messages.csv` and not `Job Applications.csv`.

- Claimed source: LinkedIn data export 2026-08-23, `messages.csv`, 5,262 messages, 497 conversations in the analysis window
- Analysis window: 2025-06-01 to 2026-08-31. Study window ends 2026-08-29. Export date is 2026-08-23, so nothing after that date exists in the export
- 54 job-related threads, 20 uncertain
- Analysis also claims 107 formal LinkedIn applications in the Jobs folder. This tree's dated extract has 105. Raw Jobs CSV is still absent

Committed as `artifacts/linkedin/job-threads-analysis-2025-06-to-2026-08.md` (redacted). Independent match: `adjudication/linkedin_dm_match.csv`. Builder: `adjudication/build_linkedin_dm_match.py`.

## Match of 74 coded rows

| match_status | n |
|---|---|
| exclusion | 31 |
| candidate_opportunity_held | 17 |
| already_application | 9 |
| unidentifiable | 6 |
| already_opportunity | 6 |
| held_role_collision | 3 |
| candidate_application_held | 1 |
| held_implied_interview | 1 |

Already in the 298 (DM is follow-up, not a new row): Virtru, 2X, AICRO, RevSpring, TrueBuilt, Melavex, Gradient Labs, Patch, WilsonHCG.

Already opportunity (stay outside the 14): WorkOS, Glytec, The Kiln, Opsin, The Hog, plus Jan Durbin corroborating Glytec.

The 12 held LinkedIn application candidates from Freeze 4 do not appear in these DMs.

## Gaps in the analysis itself

- Hotglue (Kevin Wright) is not in the 54. Freeze 3 coded that as a LinkedIn inbound. Either the keyword scan missed it, or it was not in `messages.csv`.
- Pin is not in the 54. Freeze 3 Pin is Gmail and Calendar.
- AnyInt AI (Woody Hu, 2026-06-09) is the one named LinkedIn application that is in this analysis and in neither the 105 extract nor the 298. Hold. Do not mint. That is the only named candidate for the 107 versus 105 gap.
- Claudomat, Ambient.ai, Aptean (two recruiters), Parallel, Speakeasy, AutoLeap, Cyft, Starbridge, and several unnamed-client inbounds are not in the 298. Held as opportunities or unidentifiable. Not applications unless a Jobs-folder row is produced.

## The Kiln

This analysis's Giorgio thread (start 2026-03-03): same-day video call, intro to Patrick and Mathias promised, 2026-03-06 follow-up unanswered. Stage Ghosted.

That is a different thread from the GTME Intro screenshots (2026-03-04, Patrick). It does not mint a second interview. Package log 037's two-interview coding is not adopted.

## Pierre Verhoeven, 2025-08-08

Uncertain thread: "Good luck for tomorrow" implies an interview on 2025-08-08. Primary calendar that day: Jorge Macias (standing GTME-titled meeting, already treated as relationship not interview), Exploring Octave + Clay, Michael Slawson vendor. Mixmax Heath is 2025-08-14. Beckhoff rejection mail is 2025-08-08. No company is minted.

## Census

`adjudication/applications__full_census.csv` still 298. Interviewed applications remain 14. Opportunity register unchanged. Raw `messages.csv` and `Job Applications.csv` remain absent.
