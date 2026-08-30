# Retrieval log 035

**Q13, LinkedIn data export.** Source: `Complete_LinkedInDataExport_08-19-2026.zip`, generated 2026-08-19, supplied by the subject. Processed locally. This is the largest single retrieval event in the project and it changes the census, the opportunity register, and the date-precision problem all at once.

Export generated 2026-08-19, ten days before window close. **Anything after 2026-08-19 is not in it.**

## Stratum A: `Jobs/Job Applications*.csv`

Seven files, **1,279 application rows all-time**, all with exact timestamps, company, job title, job URL, and resume filename.

**In window (2025-06-01 to 2026-08-30): 105 applications, 98 distinct companies, 101 unique company-plus-title pairs.** Zero unparseable dates.

First: 2025-06-14, Databar.ai, GTM Engineer (Growth & Sales). Last: 2026-07-26, Doomers AI, Founding GTM.

| month | applications |
|---|---|
| 2025-06 | 5 |
| 2025-07 | 7 |
| 2025-08 | 1 |
| 2025-09 | **0** |
| 2025-10 | **0** |
| 2025-11 | 1 |
| 2025-12 | **0** |
| 2026-01 | 2 |
| 2026-02 | 5 |
| 2026-03 | 7 |
| 2026-04 | 15 |
| 2026-05 | 5 |
| 2026-06 | 32 |
| 2026-07 | 25 |
| 2026-08 | 0 (export cut 08-19) |

### This solves the date-precision problem for a large slice

`00-core.md` and the Methods rules require that any monthly series from the full census be reported with a warning that a large share of dates are `relative_display` approximations. **These 105 rows are `date_precision = exact`**, with minute-level timestamps and a job URL each. They are the cleanest stratum in the entire corpus.

Figure C's "exact-only" variant now has real substance instead of a thin remainder.

### And it gives Figure C an actual result

Cross the series against the engagement register:

- **ENG-C, 2025-09 to 2025-12:** applications 0, 0, 1, 0. Outbound application activity **stops almost completely** during the contract.
- **ENG-D and ENG-E, 2026-04 onward:** applications 15, 5, 32, 25. Outbound activity runs at its **highest volume of the entire window** while two engagements are live.

So the relationship is not monotonic and the simple story is wrong in both directions. Whatever drove the autumn stop, it was not "being engaged," because 2026-06 is the busiest month in the record and he was engaged twice over. This must be reported as-is, without a causal account.

## Stratum B: `messages.csv`

**5,256 messages all-time. 1,664 in window, across 494 distinct conversations.**

Filtering to conversations where a non-Keegan party addresses him as a candidate: **114 conversations.** Of those, 46 drew a reply, 42 run to three or more messages, and 29 are substantive exchanges of four or more messages with Keegan engaged.

| month of first message | inbound candidate conversations |
|---|---|
| 2025-06 | 16 |
| 2025-07 | 13 |
| 2025-08 | 9 |
| 2025-09 | 5 |
| 2025-10 | 7 |
| 2025-11 | 7 |
| 2025-12 | 3 |
| 2026-01 | 8 |
| 2026-02 | 5 |
| 2026-03 | 8 |
| 2026-04 | 4 |
| 2026-05 | 8 |
| 2026-06 | 8 |
| 2026-07 | 12 |
| 2026-08 | 1 |

**114 is an upper bound, not a count.** The filter catches agency solicitations, offshore dev-shop pitches, financial-advisor recruiting, and Keegan's own network chatter. A coder has to triage every one. Do not publish 114 as a number of opportunities.

### The second half of the Figure C result

Compare the two series across the ENG-C autumn:

- Outbound applications, 2025-09 to 2025-12: **0, 0, 1, 0**
- Inbound candidate approaches, same months: **5, 7, 7, 3**

**Applications stopped. Approaches did not.** The inbound channel kept producing at roughly its normal rate through the exact stretch that logs 030 and 033 read as a dead zone. The dead zone was in one channel only, and it was the channel the original census was built on.

## Corroboration and new processes

Confirmed from earlier logs: the Glytec thread with Patrick Cua (8 messages, 2026-01-21 to 01-30, log 034), and the WorkOS approach via TopHire (Siddharth Gopi, 2025-08-25).

New and substantive, not previously in any log:

- **Eoin Clancy, 48 messages, 2025-07-24 to 2026-07-14.** A year-long relationship including "We have some related roles. Nick is the main hiring manager, but happy to connect if something like the above stands out." Invisible to every Gmail and Calendar query in this project.
- **Greg Reardon, 10 messages, 2025-07-26 to 07-31:** "throw an application in, ill let my recruiting team know to keep an eye out." A referral that converts into an ATS application. This is a **channel-crossing event** and the codebook currently cannot represent one: `discovery_source` and `submission_channel` are separate fields, which is correct, but nothing records that a network contact caused the submission.
- McKenzie Skamarycz (15 msgs, 2026-03), Chrissy Repko (2X, GTM Engineer, 2026-04), Aleksandra Belousova (2026-07), Michael Berry (RevOps search, 2026-06), Phillip Sweeney (2026-02, declined on NYC relocation), Mounika Ravi (Flexton, 2025-10), Rachel Downs (2026-03).

## Excluded, recorded without detail

Several flagged threads are personal correspondence with friends and peers about their own job situations, or Keegan helping others prepare. These are **not job processes for the subject** and nothing about their content is recorded in this project.

Also excluded: vendor and agency solicitation (offshore app development, outbound-service packages, financial-advisor recruiting), and LinkedIn SpinMail templates with unreplaced `%FIRSTNAME%` merge fields.

## What this does to the manifest

The stop rule in `QUERY-MANIFEST.md` is wrong and must be rewritten. Every exhaustiveness claim in logs 021 to 033 was exhaustive **with respect to Gmail and Calendar only**. Three strata now exist:

| stratum | status | measures |
|---|---|---|
| Gmail | Q1 to Q7b exhausted; Q3b, Q6, Q9, Q10 pending | applications with receipts, employer correspondence |
| Calendar | blocks 1 to 3 done, 4 to 6 pending | scheduled processes, poorly labelled |
| **LinkedIn** | **export in hand, triage not started** | applications without receipts, and the entire inbound channel |

## Open, in priority order

1. **Deduplicate the 105 LinkedIn applications against the Gmail census.** Some generated receipts and are already counted; some did not. Until this is done the census total cannot be stated at all. This is the blocking task.
2. Triage the 114 inbound conversations to a real opportunity count.
3. `Invitations.csv`, `Saved Jobs` (426 rows all-time), and `Job Applicant Saved Screening Question Responses` are unexamined and may carry more.
4. Codebook: a field or note recording that a network contact caused an ATS submission.
5. Still open: Q8 blocks 4 to 6, Q12 pagination, five engagement descriptions, three codebook changes from logs 031 and 032.
