# Retrieval log 041

**Targeted retrieval: Orchestry Software Inc.** Query `orchestry`, full window, `in:anywhere`, trash included. 9 threads, 8 artifacts, 1 newsletter.

**Trigger:** subject states "I interviewed with Orchestry." **Result: the artifacts support him, and logs 006 and 022 under-read the record.** This is a correction in the opposite direction from log 040.

## The complete record, four days, one requisition

| # | timestamp (UTC) | party | artifact |
|---|---|---|---|
| 1 | 2026-03-24 01:39:37 | Breezy, `no-reply@orchestry-software-inc.breezy-mail.com` | "You did it! We have received your application for **GTM Engineer (Sales)**" |
| 2 | 2026-03-24 17:12:46 | **Jay Banga**, `eml_87e77a84a157` | "We'd like to progress you to a **45-minute video interview.** You may select a timeslot here" |
| 3 | 2026-03-24 17:13:40 | Breezy | Meeting scheduled. Video link `...2030985d543c` — **slot 1** |
| 4 | 2026-03-25 20:20:00 | Breezy | "meeting in 10 minutes: **Recruiter Screen** With: Jay Banga" — slot 1 at 20:30 |
| 5 | 2026-03-25 20:44:48 | Jay Banga | **"I wanted to follow up as we missed each other for our scheduled interview.** I completely understand that things come up" |
| 6 | 2026-03-25 21:50:30 | Breezy | Meeting scheduled. **Different** video link `...b4a1b815ab17` — **slot 2** |
| 7 | 2026-03-26 20:20:00 | Breezy | "meeting in 10 minutes: Recruiter Screen With: Jay Banga" — slot 2 at 20:30 |
| 8 | 2026-03-27 23:45:49 | Jay Banga | "Thank you for taking the time to apply for the GTM Engineer (Sales) position at Orchestry Software Inc **and for the effort you have put into the interview process.** After careful consideration..." |
| 9 | 2026-03-27 23:48:14 | Keegan | "Thanks no worries Jay! **Truly appreciated your time.** You are doing a bang up job. Godspeed" |

## What the record actually shows: two slots, not one

**Slot 1, 2026-03-25 20:30, was missed.** Jay says so at 20:44, fourteen minutes after the start time.

**Slot 2, 2026-03-26 20:30, was booked 66 minutes after the miss** — artifact 6 carries a *different* Breezy video-conversation URL from artifact 3, which is what distinguishes a genuine reschedule from a resent link.

**Slot 2 was held.** Three independent supports:

1. **Jay's own words in the decline:** "the effort you have put into **the interview process**." That is not the language of a process that never got past scheduling.
2. **Keegan's reply:** "Truly appreciated **your time**." Time was given.
3. **Jay's demonstrated behavior:** when slot 1 was missed he wrote within fourteen minutes. **No equivalent message exists after slot 2.** Negative evidence on its own is weak — log 039 established that in this project — but here it sits against a measured response pattern from the same counterparty on the same requisition two days earlier.

Plus the subject's direct statement, `evidence_system = memory`, 2026-08-30.

**Ruling: the recruiter screen was held 2026-03-26.** `terminal_outcome = rejected_after_interview`, 2026-03-27, precision exact.

**Orchestry does not depend on recall.** The artifacts carry it. That matters because `00-core.md` requires memory-sourced rows to be excludable from the reproducible subset — Orchestry survives that exclusion, unlike Pin, which exists only on subject recall. The subject's statement here *directed* the retrieval; it is not what the finding rests on.

## What the earlier logs got wrong

Log 006 recorded a "missed-interview update, 2026-03-25." Log 022 listed "recruiter screen scheduled 03-24, reminder 03-25, reschedule 03-25, reminder 03-26, decline 03-27."

Both captured the artifacts correctly. **Neither followed the sequence through to its conclusion.** The 03-25 miss got carried forward as if it were the outcome of the process, when it was the outcome of the *first slot*. The 03-26 reminder is sitting right there in log 022's own list.

**This is a summarization failure, not a retrieval failure.** The sweep found everything. The reading stopped early.

## The meta-finding, and it is the important one

Two consecutive checks on the interview layer, two errors, in **opposite directions**:

| | error | direction |
|---|---|---|
| Dagster Labs, log 040 | a held interview absent from the count of eleven | count too **low** |
| Orchestry, log 041 | a held interview recorded as missed | reading too **pessimistic** |

The interview layer has now been probed twice and failed twice. Neither error was a retrieval gap; both were reconciliation gaps between artifacts already in the corpus and the figures carried forward from [S1].

**This converts the recomputation from a good idea into a requirement.** `interviewed` is a derived metric under design principle 1. Every interview claim must come from Table 2 events built directly off the artifacts, and no interview figure from [S1] may be carried into Results. The stop condition added in log 040 stands and is now evidenced twice.

**A named risk for the recomputation:** any process whose artifacts include a `no_show` must be read to the end of the thread before an outcome is assigned. Orchestry shows a miss is frequently followed by a rebooking within the hour. Inertia Growth (logs 019, 020, 024, 025) shows the same churn shape — three reschedules and a cancellation — and **should be re-read on the same suspicion before its outcome is treated as settled.**

## Coding, ready to write

**Table 1**, `orchestry-software|gtm-engineer-sales|c1`:

- `date_applied` 2026-03-24, `date_precision` exact
- `submission_channel` `ats_direct`, `ats_system` Breezy
- `evidence_tier` A, `evidence_class` `employer_artifact`, `register` `application`
- `terminal_outcome` **`rejected_after_interview`**, 2026-03-27, precision exact

**Table 2**, seven events, `evidence_system = gmail`:

| event_type | date | note |
|---|---|---|
| `submission_receipt` | 2026-03-24 | Breezy |
| `employer_ack` | 2026-03-24 | Jay Banga, invitation to a 45-minute video interview |
| `no_show` | 2026-03-25 | **slot 1.** First evidenced use of this event type in the corpus |
| `reschedule` | 2026-03-25 | **slot 2 booked 66 minutes after the miss.** Distinct Breezy conversation URL |
| `recruiter_screen` | 2026-03-26 | round 1, `medium = video`, counterparty Jay Banga, recruiter |
| `rejection` | 2026-03-27 | Jay Banga |
| — | | subject confirmation 2026-08-30 belongs in `notes`, not as an event |

**`reschedule` here is the real thing**, and it is worth contrasting with log 040. Dagster's 2026-03-30 slot change was a *cancellation backfill* — the counterparty offered an earlier slot freed by someone else, a sign of acceleration. Orchestry's is a genuine reschedule following a `no_show`, a sign of churn. **Coding both as `reschedule` would make the churn measure meaningless.** The distinguishing test, now stated: a reschedule follows a failure to meet; a backfill follows an offer to meet sooner.

## Timings, all exact

- Application to interview invitation: **15h 33m**
- Miss to rebooking: **66 minutes**
- Application to held interview: **2 days 19 hours**
- Full cycle, application to decline: **3 days 22 hours**

Alongside Dagster Labs (5 days, same-day interview) and Bluejay via HartleyCo (11 days), three of the fastest full cycles in the corpus all carry exact dates at both ends and all end in rejection. Whether speed of process correlates with anything is a Results question and is not claimed here.

## Unchanged

Orchestry was already among the eleven in-census interviews in [S1], so **this does not change the interview count.** It corrects the outcome, the event list, and the record of what happened. No LinkedIn row exists for Orchestry — ATS-direct via Breezy — so the dedupe figures in logs 038 and 039 are unaffected.

## Open

1. **Re-read Inertia Growth** on the Orchestry suspicion. Three reschedules and a cancellation; the outcome may have been read from the wrong artifact.
2. Recompute the interview count from Table 2 events. Now evidenced twice as necessary.
3. Sweep the corpus for any other process where a `no_show` or cancellation was treated as terminal.
