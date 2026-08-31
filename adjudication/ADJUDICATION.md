# Adjudication

Coders compared: bravo and cursor. Alpha CSVs were not present when this pass ran.

## Pre-adjudication (raw match keys)

- bravo rows: 228
- cursor rows: 231
- intersection: 211
- both `register = application`: 206
- role_lane percent agreement: 0.9621
- role_lane Cohen's kappa: 0.9510
- include percent agreement: 0.9905
- include kappa: 0.7452 (two disagreements on a rare class)

## Register disagreements (intersection)

1. The Hog GTM Engineer. Bravo: opportunity. Cursor: application. Adjudicated **opportunity** at Freeze 1, on the ground that no ATS or sent-mail submission artifact existed. **Reversed at Freeze 3 to application**: the LinkedIn formal export carries a submission dated 2026-06-04, eleven days before the interview invitation.
2. BX Studio unspecified. Bravo: application. Cursor: opportunity. Adjudicated **opportunity** at Freeze 1, on the ground that a video forwarded to a hiring manager is not a submission. **Reversed at Freeze 3 to application**: the export carries a submission dated 2026-04-06, two days before the employer acknowledgment.
3. Weave GTM Engineer, 2026. Adjudicated **opportunity**, and separated from the 2025 Business Development Manager application it had been attached to. Same rule as The Hog: an interview with no submission artifact does not mint an application row. See the corrections below.

## Corrections applied after coding

These are named changes to coder output, applied here rather than by editing the coder CSVs. Both were disclosed in `knowledge/protocol.md` and `paper/DEFECTS.md` on the date they were made.

Events excluded from the interview derivation:

- `weave|business-development-manager|c1`, `hiring_manager_interview` dated 2026-08-18. Belongs to a separate inbound Weave process, not this application. gth_0339a17e3860d167 is a post-interview decline, so an interview did happen, but the BDM application was already rejected 2025-07-31. Bravo excluded this artifact during blind coding as having no parent.
- `hypergen|gtm-engineer|c1`, `hiring_manager_interview` dated 2026-04-14. An interview INVITATION from people@hypergen.io replying to the March 11 confirmation, with nothing after it. Flagged at retrieval time: retrieval-log-006 records that the prior ledger held Hypergen as a receipt only and that the Interviews sheet does not list it. Bravo blind-coded the same artifact `employer_ack`; cursor is the lone outlier and adjudication took cursor.
- `testgorilla|go-to-market-engineer|c1`, `recruiter_screen` dated 2026-02-20. A recruiter INTRO message, alongside an assessment invitation the same day and a recruiter update on 2026-04-23. No scheduling artifact, no completion signal, no SENT reply. Both coders made this call, which is why it is recorded as a missing codebook rule rather than a coder error.
- `revspring|lead-agentic-operations-gtm-engineering|c1`, `recruiter_screen` dated 2026-06-10. A Recruiter Screen REQUEST. The surrounding thread is two submission receipts and two employer acknowledgments, with no scheduling artifact and no completion signal. Both coders made this call.

Terminal outcomes corrected:

- `weave|business-development-manager|c1` set to `rejected_no_interview` dated 2025-07-31. The interview belonged to a separate opening, so this application was declined without one. Reverts to bravo's coding; cursor and bravo disagreed on this field and adjudication did not cover it.

The Weave role title, the counterparty, and the inbound origination are author recall, not artifact. The corpus establishes only that an interview at Weave happened and was declined on 2026-08-18, from `gth_0339a17e3860d167`. Under `prompts/extraction.md` rule 8 recall is not recorded as evidence, so none of those three is written into a structured field.

## Freeze 3 register reversals, 2026-08-30

These two were the only include-or-exclude disagreements between the blind coders, the pair that produced the include kappa of 0.7452. Both went to the opportunity register on one stated ground: no submission artifact existed in the corpus. The LinkedIn formal export supplies one for each.

The rule did not change. Its premise did. An interview with no submission still does not mint an application row; a submission now exists. Each row is taken from the coder who read it as an application, so the surviving row is a real coder's judgement rather than one assembled during adjudication.

Consequence: census 221 becomes 223, interviewed applications 13 becomes 14, and the rate 13/221 becomes 14/223. See `challenge/CHALLENGE.md` section 1.2 and `paper/DEFECTS.md`.

## Alias merges (same process, different keys)

Anduril / Anduril Industries; Attentive unspecified c1 / GTM Engineer c1; HartleyCo / Bluejay Founding GTM; Exa / Exa Labs; IBM title with and without Confluent in the role string; Manifold / Manifold AI; Tekion comma in title; Valsoft GTM Engineer / GTM Engineer DockMaster.

Productboard GTM Engineer vs Associate GTM Engineer stays one row (the Associate title already in the dual-agreement set). Talentpluto GTM Engineer vs Go-to-Market Engineer is one opening, not two. Pindrop unspecified c2 is not a new cycle: no terminal on c1.

## Uniques included

From bravo: Glean GTM Engineer Marketing (Greenhouse 2026-03-23); Jobright.ai Product Manager Early Career (2026-03-31).
From cursor: Agroknow North America Sales; Classet Head of GTM; jobmail.io Growth Lead; Stellar Substitute; Switchyards Digital Product Builder.

## Opportunity, not census

WorkOS (TopHire). Mercor Growth Strategist / GTM Engineer contract path. ThriveLink referral. Dexian. Luzmo. Glytec. SmartMode AI. Crossing Hurdles / Montauk Capital. micro1 client submissions. Pinterest June 2025 referral-accept messages. Weave GTM Engineer 2026, inbound, interview evidenced by the 2026-08-18 decline with no submission artifact.

The Hog and BX Studio were on this list until Freeze 3. They are not any more, and the reason is an artifact rather than a change of mind. WorkOS and the 2026 Weave opening remain here because no submission artifact has been found for either.

## Adjudicated application census

- n = **223**
- evidence_class: employer_artifact (platform_log stratum empty; LinkedIn export absent)
- full census equals the employer_artifact stratum in this freeze
- interviewed applications (derived from events, either coder): 11
- application-to-interview rate: 11/223 = 0.0493
- exact-date n: 196; non-exact n: 27
- exact-date monthly: {'2025-06': 5, '2025-07': 19, '2025-08': 16, '2025-11': 1, '2025-12': 2, '2026-01': 7, '2026-02': 10, '2026-03': 21, '2026-04': 27, '2026-05': 22, '2026-06': 28, '2026-07': 33, '2026-08': 5}

This 223 is not 247. It is not a completeness percentage. Capture recapture remains unmeasured.

## 212 to 163

Still undocumented. Workbooks absent.
