# Origins and how the tally combines

Subject confirmation 2026-08-30: if the subject says a conversation happened, it is logged. Recall is tagged `evidence_system = memory`. It is visible so a skeptic can drop it. It is not silently mixed into the artifact census.

Machine-readable rows: `adjudication/origins__subject_confirmed.csv`. Overlay rows: `coding/confirmed/`. Retrieval log 056.

This file is the paper appendix for origins of interviews and origins of money. Frozen numbers stay in `paper/RESULTS.md`. Keegan writes paper sections. This file is the trace, not the manuscript.

## How to combine (do not add into one rate)

Filter `origins__subject_confirmed.csv`. Do not union registers into 298.

| paper question | filter | number this freeze can defend |
|---|---|---|
| How many search applications? | `in_298 = yes` | **298** |
| How many of those reached interview? | `in_298 = yes` and `in_14 = yes` | **14**. Rate **14/298** |
| Which conversations happened outside that rate? | `in_298 = no` | opportunity, employment, consulting, communal |
| What made money? | `made_money = yes` | Mixmax, Mercor contract, Mobb, Kivira.health |
| Where did a named interview come from? | `origin_as_stated` and `origin_evidence` | tables below |

A skeptic who drops memory keeps A plus the artifact columns of B. A narrative that names every conversation the subject confirmed uses A plus B plus Mixmax as employment, and still prints 14/298 as the application rate.

Do not print a combined interview count as if it replaced 14/298. Do not print package 321 or 325 as this freeze's census.

## Why some rows were not added to 298

Two different questions were being mixed.

1. **Did this conversation happen?** Yes, if the subject says so. That is now in the overlay.
2. **Does this row enter the application census and the 14?** Only if it is a role the subject submitted, with `register = application`. Opportunity, employment, consulting, and communal meetings stay out of 298 and out of 14/298.

That is why Mixmax, Mercor contract, Pin, The Hog, Glytec, Opsin, Hotglue, The Kiln, Adam, Doug, Kivira, BCOFA, Jorge, and Kellen were not poured into 298. Adding them there would make the application-to-interview rate uninterpretable.

We also did not invent employer names (Adam and Doug have no company string in the artifacts). We did not overwrite frozen `discovery_source` values. GTM Cafe is not in this tree's codebook vocabulary (`newsletter_community` is the closest slot). Origins live in this overlay so Freeze 1 and Freeze 2 stay reproducible.

Names the subject supplied that are absent from mail and calendar titles (Eddie, Chris, Harry, Giorgio as interviewer, Colossus phone round, Dagster phone) are logged as memory. They do not mint extra artifact rounds.

The twelve held LinkedIn application candidates (Datricks, Bitovi, ScoutLab.io, JetBridge AI, Abacus.AI, Brainfish, ClosedWon Talent, SWARM, Insignia Assets, Stealth Startup, Kana) and AnyInt AI are still not in 298. The subject has not confirmed those as applications. Saying an interview happened is not the same as saying a LinkedIn Easy Apply row is a new application.

## The combined scoreboard (keep these separate in the paper)

### A. Artifact application census

**298** applications. **14** of those have at least one interview event in the frozen events tables. Rate **14/298**.

The 14: Beautiful.ai, Dagster Labs, Every.to, Great Question, HartleyCo, Hologram, Hypergen, jobmail.io, Orchestry, Pearl, PhrasIQ, RevSpring, TestGorilla, Weave.

Source: `adjudication/applications__full_census.csv` filtered `register = application`. Interviews derived from freeze events whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round} intersected with those 298 ids.

### B. Opportunity conversations (not in the 14)

Already in Freeze 3 or cursor as `register = opportunity`, interviews evidenced:

- Glytec (Clayton; origin Patrick F. Cua DMs)
- The Hog (Hudson, one live plus take-home)
- Pin (Erica then Conor)
- Hotglue (Kevin Wright; YC Work at a Startup)
- Opsin (James Pham interview happened, freeze3 calendar; Colossus phone round is memory)
- The Kiln (Patrick interview happened, freeze3; Giorgio interview is memory)
- Mercor contract (two interviews: Claire then Daniel Luo; made money)
- WorkOS (TopHire slot booked; live call not separately dated)

Overlay, subject-confirmed:

- Adam Andrewjeski, founder of Stellar Growth (informal, Clay Cafe / GTM Cafe)
- Doug Shankman, founder and CEO of AICRO (informal plus CRO idea, GTM Cafe). Distinct from the two AICRO application rows in the 298.

### C. Employment and consulting (made money or tried to; not search applications)

- Mixmax / Heath: interview happened. Calendar 2025-08-14 (`cal_3e5387362a5b33e3`). Follow-up SENT in Welcome to Mixmax (`gth_beb7124e93244a82`). Two-week trial then three-month contract. Freeze 3 exclusion from 298 stands.
- Mobb: employment. Gusto first-day (`gth_96b8c659b5fa2546`). Not a search application.
- Kivira.health: three month GTM contract via Josh Pappas. Calendar GTM Overview (`cal_cc9f94b847eb65aa`) and weekly outbound. Consulting.
- BCOFA / Dr. Blaney: consulting that fizzled. Calendar 2026-03-06. No money.

### D. Communal (not jobs)

- Jorge Macias / GTM-engineering.io: TA, mentorship, recurring calendar.
- Kellen Casebeer: Clay Cafe / gtmcafe.com founder, GTM Engineering School TA, Mobb prep. Calendar 2025-06-16.

## Origins of interviews that entered the 14

Only four of the 14 have an origin the subject stated in this pass. PhrasIQ is the one whose frozen `discovery_source` already matches. The rest stay `unknown` on the frozen row. Overlay records cafe origins as memory.

| process | origin as stated | evidence | frozen discovery_source | artifact pointer | memory token |
|---|---|---|---|---|---|
| Every.to | GTM Cafe channel jobsandopportunities | memory | unknown | cal_eb10d6eb86410a16 (Austin 2026-04-21) | origin is the CSV row |
| PhrasIQ | Wellfound | artifact | wellfound | gth_e9be0ace83621c85 (accepted); cal_aa344a710f544818 (Discovery); cal_4906d7d8bd299c13 (Deep Dive) | tok_f70bd14e358a (Eddie) |
| Pearl | Garrett Wolfe referral, GTM Cafe | memory | unknown | gth_6d883e4b5af47f48 (Ashby); two calendar interviews | tok_fd8fde3f5245 (Chris) |
| Great Question | GTM Cafe channel jobsandopportunities | memory | unknown | gth_cf236998e25c2988 (Ashby); Harri gth_8dc62a9ea6433a08 | tok_01583f192d92 (Harry) |
| Beautiful.ai | not restated | artifact | unknown | gth_93b7915bd98264ce; cal_68d3d2165c13499a; HM Brandon Ness gth_ec1fac33cf5f23f1; Emily decline gth_1186b66d0556feda | none |
| Dagster Labs | not restated | artifact | unknown | gth_89b52fe76388035e; chat gth_1c8ae3fa0432b375 | tok_6ad68eb83f3c (phone) |
| HartleyCo | recruiter (Josh Kelly; client Bluejay) | artifact | recruiter_inbound | gth_59384916f1d2f6ca | none |
| Hologram | not restated beyond count | artifact | unknown | Amy gth_fc3a24d02960b24e cal_1e35ab92e7cb411b; Derrick gth_966e3da56037f91c cal_7f6169cd30cea34e | tok_3c7dc3e90dd6 (subject: two interviews) |
| Hypergen | not restated | artifact | unknown | gth_d34cb1ecb8ba51f6 | none |
| jobmail.io | not restated | artifact | unknown | gth_531b132d1253925a; Jack gth_a1cbc75584147ef9 | none |
| Orchestry | not restated | artifact | unknown | gth_397ef5934d0939b2 | none |
| RevSpring | LinkedIn inbound then Newton receipt | artifact | unknown | gth_1202203d544f6fc9; gth_c6362282bdac9373; screen gth_d679e7c78f455a3c | none |
| TestGorilla | not restated | artifact | unknown | gth_f99a415b023fc244 | none |
| Weave | Greenhouse receipt | artifact | unknown | gth_4871569df9c50a18; post-interview decline gth_0339a17e3860d167 | none |

TrueBuilt is in the 298 and not in the 14. LinkedIn applied-list GTM Engineer stays. Later contract quote is consulting, not an interview.

## Origins of opportunity interviews

| process | origin as stated | evidence | artifact pointer | memory token |
|---|---|---|---|---|
| Glytec | LinkedIn DMs with CEO Patrick F. Cua | artifact (messages analysis) | cal_335a1749b1f26d6d (Clayton); gth_7ff12c525a38011d | none |
| The Hog | not restated | artifact | gth_d1989dfb9542a2da; cal_629a071abb61bce9; take-home gth_df78e875e89e162f | none |
| Pin | GTM Cafe channel jobsandopportunities | memory | cal_ad843b81c501a0fe (Erica); cal_1d949b06d7b86c9a (Conor) | origin is the CSV row |
| Hotglue | YC Work at a Startup | artifact plus subject | cal_ccc88f3db9f64129; gth_e5448b420f510900 | none |
| Opsin | Colossus Technology Group | artifact (Adrianna mail) | gth_e756940c516829cf; James cal_d8dafd5d42786dbb | tok_b1f3dc9b0958 (Colossus phone); tok_8d0c98c0fb17 (subject: James happened) |
| The Kiln | GTM Engineer School testimonial | artifact | tok_ad8a6c7aa631 (GTME Intro); Patrick freeze3 e2 | tok_8c8acbc92d3c (Giorgio interview); tok_1bdfc7313b38 (subject: Patrick happened) |
| Mercor contract | Claire Gauthier inbound | artifact | gth_da5b9d0848d88f36 (Instant Work Offer); gth_04388c5d54511960 (contract); two interviews Claire then Daniel Luo | tok_10c69501feb3 (count is two) |
| WorkOS | TopHire recruiter | artifact | gth_7c798c988d52c12f | none |
| Adam / Stellar Growth | Clay Cafe now GTM Cafe | memory (Calendly note names Clay Cafe); company from LinkedIn screenshot | cal_f3694776d5518b14 | tok_4c79cbbc329f; tok_155d133e690a |
| Doug / AICRO | GTM Cafe | memory; company from LinkedIn screenshot | cal_c20ca257f9bdfd6c | tok_654cb884181e; tok_53b6c592660c |

Memory `tok_` values on overlay events are stable recall pointers. They are not Gmail page tokens. Frozen `gth_` and `cal_` pointers stay the reproducible subset.

## What made money

| process | kind | origin | in 298 | in 14 | artifact pointer |
|---|---|---|---|---|---|
| Mixmax | two-week trial then three-month contractor GTM | GTM Engineer School, then Heath interview | no | no | cal_3e5387362a5b33e3; welcome/SENT gth_beb7124e93244a82 |
| Mercor contract | hourly contract | Claire Gauthier inbound | no | no | gth_04388c5d54511960 |
| Mobb | employment | employment onboarding (Kellen meeting was prep) | no | no | gth_96b8c659b5fa2546 |
| Kivira.health | three month GTM consulting | Josh Pappas | no | no | cal_cc9f94b847eb65aa |
| BCOFA | unpaid, fizzled | Josh Pappas; prior engagements before window | no | no | calendar 2026-03-06 in freeze3 exclusions |

Search applications in the 298 did not produce these paid engagements. The paper can say that without mixing Mixmax or Mercor contract into 14/298.

Mercor marketplace evaluator and expert receipts remain in the 298 without interviews. They are a different process from the Growth Strategist / GTM Engineer hourly contract.

## Same company, different process (do not merge)

AICRO appears three times. They are not one row.

| application_id | register | in_298 | in_14 | what |
|---|---|---|---|---|
| aicro\|gtm-engineering-team-lead\|c1 | application | yes | no | Email 2026-02-06 |
| aicro\|gtm-engineer\|c1 | application | yes | no | LinkedIn applied list |
| aicro\|informal-cro-idea\|c1 | overlay opportunity | no | no | Doug Shankman 2025-10-27. Founder identity from LinkedIn screenshot tok_53b6c592660c |

Stellar Growth vs Stellar Substitute are different employers. Overlay `stellar-growth|informal|c1` is Adam. `stellar-substitute|unspecified|c1` is a Frontline substitute notice in the 298.

## Files a later coder or the paper should open

| claim | file |
|---|---|
| 298 applications | `adjudication/applications__full_census.csv` |
| 14 interviewed applications | derived; freeze events in `coding/cursor/events__cursor.csv` plus Freeze 3 corroboration in `coding/freeze3/events__freeze3.csv` |
| Combined process list with flags | `adjudication/origins__subject_confirmed.csv` |
| Memory overlay applications | `coding/confirmed/applications__confirmed.csv` |
| Memory overlay events | `coding/confirmed/events__confirmed.csv` |
| This writeup | `adjudication/ORIGINS.md` |
| Retrieval | `logs/retrieval-log-057.md` (this confirmation), `056.md` (first overlay), `055.md` (pressure-test) |
| Freeze 4 census lock | `adjudication/FREEZE-4.md` |
| Adam company screenshot | `artifacts/linkedin/profile-adam-andrewjeski-stellar-growth.md` |
| Doug company screenshot | `artifacts/linkedin/profile-doug-shankman-aicro.md` |

`adjudication/derive_metrics.py` reads `cursor`, `alpha`, and `bravo` only. Coder `confirmed` is excluded so 14/298 cannot move by accident.

## What a coder still must not do

- Recode Freeze 1 or Freeze 2 CSVs to plant GTM Cafe on `discovery_source`
- Put overlay opportunity or employment interviews into the 14
- Invent a company for Adam or Doug when a screenshot is absent. Screenshots now name Stellar Growth and AICRO.
- Merge Doug's AICRO overlay into `aicro|gtm-engineer|c1` or `aicro|gtm-engineering-team-lead|c1`. That would move 14.
- Merge Adam's Stellar Growth overlay into `stellar-substitute|unspecified|c1`
- Adopt package 321 or 325 as this freeze's census
- Mint the twelve held LinkedIn rows without a per-row application confirmation
- Print a combined conversation count as if it were the application-to-interview rate
