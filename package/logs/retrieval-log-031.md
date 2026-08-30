# Retrieval log 031

Not a retrieval. Two facts supplied by the subject, their corroboration against the corpus, and what they change.

**Provenance warning.** Both facts are `evidence_system = memory`. The artifacts are *consistent with* them but do not independently establish them. Per the codebook, memory-sourced rows must stay visible so they can be excluded from the reproducible subset. Neither fact may be reported as artifact-established.

## Fact 1: Pin was applied to through the GTM Cafe community, formerly Clay Cafe

**Pin becomes a census row.** `register = application`, `discovery_source = community`, `submission_channel` to be confirmed. Log 026 reasoned that the absence of an application receipt pointed toward the opportunity register. That reasoning was sound on the artifacts and is now overridden by the subject. Record both: the artifact-only inference and the correction.

Pin is therefore the deepest **application-sourced** process in the 2025 stretch both prior audits recorded as near-empty:

| event | date | counterparty | round |
|---|---|---|---|
| interview | 2025-06-30 | Erica Stacy Tarwater | 1 |
| interview | 2025-07-07 | Conor Kline | 2 |
| assessment_sent, technical_exercise | 2025-07-07 | Erica | |
| rejection, with written feedback | 2025-07-07 | Erica | |

Two rounds and a take-home, applied to and closed inside roughly eleven days.

### Clay Cafe / GTM Cafe is a discovery channel the ledger has no code for

The community now appears three times in the corpus, and it was invisible until this week because it never generates an ATS artifact:

- **Pin**, 2025-06, produced two interviews and a take-home
- **Adam Andrewjeski**, 2025-06-18, booking note "Connected @ Clay Cafe . Spoke via slack" (log 026)
- **George Rekouts / Disco**, 2025-11-06, booking note "CLay Cafe connect" (log 030)

Only the first produced a job process; the other two are networking and stay excluded. But the channel needs a `discovery_source` vocabulary value, and the fact that **the deepest 2025 process came through a community rather than an ATS** is a Results finding, not a footnote. A census built on ATS receipts alone would have scored this channel at zero.

## Fact 2: the Heath Barnett meetings were an interview process

Log 027 recorded seven "No Agenda Meeting with Heath" invitations, 2025-06-30 to 2025-08-14, and characterised them as relationship-building because no role was named in any of them. **That characterisation was wrong.** The subject states these were the interview process, which then converted into the three-month engagement.

Reclassified, the ENG-C timeline reads:

| phase | span | artifacts |
|---|---|---|
| interview process | 2025-06-30 to 2025-08-14 | seven meetings, roughly weekly, no role named in any invitation |
| process formalises | 2025-08-28 to 2025-09-04 | format changes to "GTME Sync"; People Ops sends the welcome and service agreement |
| engagement | 2025-09-04 to approximately 2025-12-22 | daily syncs, provisioned address, invoices #001 to #007 |

### This creates a terminal outcome the codebook cannot express

Table 1's `terminal_outcome` vocabulary has no value for a hiring process that ends in a contract rather than a hire or a rejection. **Add `converted_to_contract`.** Without it, this row has to be coded as either a false negative or a false positive, and both are wrong.

This matters beyond one row. A process that converts to contract work is a real outcome class for an independent GTM engineer, and if the corpus contains one it may contain others. Worth a targeted pass later.

### It also changes what the seven meetings mean methodologically

Seven scheduled conversations over nine weeks, and **not one invitation names a role.** If the subject had not said so, no coder reading this corpus would classify them as an interview process. That is a limitation with teeth and it belongs in Methods: the artifact record systematically under-identifies informal processes, and the direction of the error is toward undercounting.

## On the quiet period

The subject offers the engagement as the explanation for low application volume across the autumn. That is plausible and it is consistent with Q8 block 2 returning zero job-process artifacts across three months (log 030).

**It is an interpretation, not a measurement.** It is the subject's account of his own behaviour, supplied after seeing the pattern. It goes in Discussion, attributed as the author's explanation, and it does not go in Results. Figure C shows the association; it cannot show the reason.

## Open

- **How did the Mixmax process start?** Same question that decided Pin. If the subject applied, ENG-C carries a census row with `terminal_outcome = converted_to_contract`. If Heath initiated, it is an opportunity register row and never enters the application total. Unresolved.
- `discovery_source` needs the community value added before the next harvest.
- `terminal_outcome` needs `converted_to_contract` added. Both are codebook changes and both invalidate prior rows if made mid-harvest, so make them now.
