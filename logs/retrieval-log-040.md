# Retrieval log 040

**Targeted retrieval: Dagster Labs.** Query `dagster`, full window, `in:anywhere`, trash included. 17 threads returned, 6 are artifacts, the rest are data-engineering newsletters.

**This log reports a numerator error in the headline interview count.**

## The complete record, one company, five days

| # | timestamp (UTC) | party | artifact |
|---|---|---|---|
| 1 | 2026-03-30 12:30:35 | `no-reply@us.greenhouse-mail.io` | Security code for your application to Dagster Labs. Resubmit required |
| 2 | 2026-03-30 13:39:22 | Greenhouse | **"Thanks for applying to Dagster Labs!"** Application received, **GTM Engineer** |
| 3 | 2026-03-30 15:29:04 | **Delaney Housley**, `eml_d3df7b160e39` | "Thanks for your interest in the GTM Engineer position... **We're excited to move you along to the next step of the interview process.** I'd like to schedule an introductory..." |
| 4 | 2026-03-30 15:47:23 | Delaney | Asks for more availability options, her day is booked |
| 5 | 2026-03-30 15:50:23 | Keegan | Flexible, and asks how to prepare beyond the obvious |
| 6 | 2026-03-30 16:48:07 | Delaney | **"I actually just had a cancelation this afternoon, would 4pm ET work today?"** |
| 7 | 2026-03-30 16:48:52 | Delaney | **"Keegan, you're invited to an interview with Dagster Labs!"** Phone Interview confirmed |
| 8 | 2026-03-30 17:55:21 | Keegan | "Nice I'll be ready!" |
| 9 | 2026-03-30 20:02:16 | Keegan | "Just making sure my spam filter didn't block the call. I'm ready when you are." **20:02 UTC = 16:02 ET, the call slot itself** |
| 10 | 2026-03-31 17:22:54 | Keegan | Follow-up, **"wanted to follow up our convo to ask about next steps"** |
| 11 | 2026-03-31 17:43:41 | Delaney | **"It was great chatting with you yesterday.** I'm planning to circle up with the team a bit later this week" |
| 12 | 2026-04-03 19:00:00 | Delaney | **"Thank you so much for taking the time to chat with me... At this time, we've made the decision to not move"** forward |
| 13 | 2026-04-03 19:13:41 | Keegan | "No worries Delaney. Appreciate your time! Lmk if I could be of service in the future." |

**The interview happened.** Two independent counterparty statements confirm it: "great chatting with you yesterday" (artifact 11) and "taking the time to chat with me" (artifact 12). This is not an invitation that lapsed.

## Finding 1: the headline interview count is wrong

`02-current.md`, sourced from the reconciled audit [S1], lists **eleven** in-census interviews: Fullsteam, Glytec, Beautiful.ai, Orchestry Software, PhrasIQ, Every, Pearl, The Hog, Bluejay via HartleyCo, Hologram, Great Question.

**Dagster Labs is not among them.** The artifacts show a scheduled, held, and concluded phone interview with a named recruiter, ending in a post-interview decline.

The artifacts were already in the corpus. Log 006 captured the receipt and security code; log 018 captured the decline and described it as a "post-chat decline." **The retrieval caught it. The reconciliation against the interview count never happened.**

Do not silently renumber. The correct action is stated in Finding 3.

## Finding 2: application to interview in one hour fifty minutes

Receipt 13:39:22. Interview invitation 15:29:04. **1h 49m 42s.** The interview itself was held the same afternoon.

`days_to_first_response` = 0. `days_to_interview` = 0. **Both dates carry `precision = exact`**, so this row survives the precision constraint and enters the computed subset rather than the excluded n.

Against a corpus where the dominant outcome is no response at all, a same-day application-to-interview is the extreme tail of the response-time distribution and will anchor that figure. Whether it is the fastest in the corpus is a Results question and is not claimed here — it requires the exact-precision subset to be computed.

It also produced a **five-day** full cycle: submission 2026-03-30, decline 2026-04-03. Compare Bluejay via HartleyCo at eleven days (log 039). Both are exact.

## Finding 3: the interview count is unaudited, and that is the real problem

Dagster Labs is a single row. The reason it matters is what it implies about method.

The eleven came from the reconciled audit workbook [S1], which predates the entire retrieval sweep. **Logs 001 to 034 have since surfaced complete or near-complete processes that neither prior audit contained** — Pin, Cyft, Starbridge, Inertia Growth, WorkOS, Orchestry, The Kiln, and now Dagster Labs. The interview count was never recomputed against the swept corpus. It was carried forward.

`interview_rate` is a **primary secondary outcome** in `protocol.md`. Its numerator has never been derived from the corpus, only inherited.

**Required action, added as a stop condition:** derive the interview count from Table 2 events across the full corpus, not from [S1]. Per design principle 1, `interviewed` is a derived metric and was never supposed to be a stored figure in the first place. The eleven is exactly the stored rollup that principle warns about, and it has now been shown to disagree with the event list.

**Do not publish any interview count or interview rate until it is recomputed.** The denominator is already moving by 87 from the LinkedIn dedupe. A numerator inherited from a superseded workbook, sitting over a denominator being rebuilt, is not a rate.

## Coding, ready to write

**Table 1**, one row, `dagster-labs|gtm-engineer|c1`:

- `date_applied` 2026-03-30, `date_precision` exact
- `discovery_source` unknown — no LinkedIn row exists, this was an ATS-direct submission and the origin is not in the artifacts
- `submission_channel` `ats_direct`, `ats_system` Greenhouse
- `evidence_tier` A, `evidence_class` **`employer_artifact`**
- `register` `application`
- `terminal_outcome` **`rejected_after_interview`**, date 2026-04-03, `terminal_outcome_precision` exact

**Table 2**, six events, all `evidence_system = gmail`:

| event_type | date | counterparty |
|---|---|---|
| `submission_receipt` | 2026-03-30 | Greenhouse |
| `employer_ack` | 2026-03-30 | Delaney Housley, recruiter |
| `recruiter_screen` | 2026-03-30, round 1, `medium = phone` | Delaney Housley |
| `followup_sent` | 2026-03-31 | Keegan |
| `employer_ack` | 2026-03-31 | Delaney Housley |
| `rejection` | 2026-04-03 | Delaney Housley |

Artifact 1, the Greenhouse security code forcing a resubmit, is a platform mechanic rather than a process event. **Not coded.** The same pattern appears on PandaDoc, Hightouch, Hologram, Axiad, Beacon Software and Together AI, so if it is ever coded it must be coded consistently across all of them.

Note that no `reschedule` event applies. Artifact 6 is a **cancellation backfill** — the counterparty offered an earlier slot freed by someone else's cancellation, and the offer was accepted. Nothing was rescheduled. The distinction matters because `reschedule` is being used to measure scheduling churn (Orchestry, Inertia Growth), and a backfill is the opposite signal: it is the process accelerating, not thrashing.

## Not affected by the LinkedIn dedupe

Dagster Labs has no row in `linkedin-applications-in-window.csv`. This was an ATS-direct Greenhouse submission, already inside the Gmail census. The dedupe figures in logs 038 and 039 stand unchanged.

## Open

1. **Recompute the interview count from Table 2 events.** New stop condition. Blocks every interview figure in Results.
2. `discovery_source` for this row is genuinely unknown. If it is worth recovering, it would come from `Saved Jobs` or the browser history, neither of which is in scope.
3. Decide once whether Greenhouse security-code artifacts are ever coded, and apply that ruling to all seven companies showing the pattern.
