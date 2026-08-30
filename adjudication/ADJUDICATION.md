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

1. The Hog GTM Engineer. Bravo: opportunity. Cursor: application. Adjudicated **opportunity**. No ATS or sent-mail submission artifact. Interview plus take-home do not mint an application row.
2. BX Studio unspecified. Bravo: application. Cursor: opportunity. Adjudicated **opportunity**. Video forwarded to a hiring manager is not a submission.
3. Weave GTM Engineer, 2026. Adjudicated **opportunity**, and separated from the 2025 Business Development Manager application it had been attached to. Same rule as The Hog: an interview with no submission artifact does not mint an application row. See the corrections below.

## Corrections applied after coding

These are named changes to coder output, applied here rather than by editing the coder CSVs. Both were disclosed in `knowledge/protocol.md` and `paper/DEFECTS.md` on the date they were made.

Events excluded from the interview derivation:

- `weave|business-development-manager|c1`, `hiring_manager_interview` dated 2026-08-18. Belongs to a separate inbound Weave process, not this application. gth_0339a17e3860d167 is a post-interview decline, so an interview did happen, but the BDM application was already rejected 2025-07-31. Bravo excluded this artifact during blind coding as having no parent.

Terminal outcomes corrected:

- `weave|business-development-manager|c1` set to `rejected_no_interview` dated 2025-07-31. The interview belonged to a separate opening, so this application was declined without one. Reverts to bravo's coding; cursor and bravo disagreed on this field and adjudication did not cover it.

The Weave role title, the counterparty, and the inbound origination are author recall, not artifact. The corpus establishes only that an interview at Weave happened and was declined on 2026-08-18, from `gth_0339a17e3860d167`. Under `prompts/extraction.md` rule 8 recall is not recorded as evidence, so none of those three is written into a structured field.

## Alias merges (same process, different keys)

Anduril / Anduril Industries; Attentive unspecified c1 / GTM Engineer c1; HartleyCo / Bluejay Founding GTM; Exa / Exa Labs; IBM title with and without Confluent in the role string; Manifold / Manifold AI; Tekion comma in title; Valsoft GTM Engineer / GTM Engineer DockMaster.

Productboard GTM Engineer vs Associate GTM Engineer stays one row (the Associate title already in the dual-agreement set). Talentpluto GTM Engineer vs Go-to-Market Engineer is one opening, not two. Pindrop unspecified c2 is not a new cycle: no terminal on c1.

## Uniques included

From bravo: Glean GTM Engineer Marketing (Greenhouse 2026-03-23); Jobright.ai Product Manager Early Career (2026-03-31).
From cursor: Agroknow North America Sales; Classet Head of GTM; jobmail.io Growth Lead; Stellar Substitute; Switchyards Digital Product Builder.

## Opportunity, not census

WorkOS (TopHire). Mercor Growth Strategist / GTM Engineer contract path. ThriveLink referral. Dexian. Luzmo. Glytec. SmartMode AI. Crossing Hurdles / Montauk Capital. micro1 client submissions. Pinterest June 2025 referral-accept messages. Weave GTM Engineer 2026, inbound, interview evidenced by the 2026-08-18 decline with no submission artifact.

## Adjudicated application census

- n = **221**
- evidence_class: employer_artifact (platform_log stratum empty; LinkedIn export absent)
- full census equals the employer_artifact stratum in this freeze
- interviewed applications (derived from events, either coder): 13
- application-to-interview rate: 13/221 = 0.0588
- exact-date n: 195; non-exact n: 26
- exact-date monthly: {'2025-06': 5, '2025-07': 19, '2025-08': 16, '2025-11': 1, '2025-12': 2, '2026-01': 7, '2026-02': 10, '2026-03': 21, '2026-04': 26, '2026-05': 22, '2026-06': 28, '2026-07': 33, '2026-08': 5}

This 221 is not 247. It is not a completeness percentage. Capture recapture remains unmeasured.

## 212 to 163

Still undocumented. Workbooks absent.
