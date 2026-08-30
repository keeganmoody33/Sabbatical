# Integrity defects

None of these is closed by inventing a number. Each is closed by an artifact or disclosed as unmet.

## WorkOS register assignment

Closed for this freeze.

Artifact: Gmail log 020, thread with Somya Shruti at TopHire, 2025-08-25 to 2025-08-27. Recruiter approach for a remote GTM Engineer role at WorkOS. Interest confirmed, a slot booked, a resume requested. No submission receipt exists in the frozen corpus.

Adjudication rule applied: `discovery_source = recruiter_inbound`, `register = opportunity`. It stays in the dataset. It does not enter the application census or any application-to-interview rate.

The 212-row prior audit listed WorkOS as Interviewed. The 247-row ledger omitted it. Both can be true under the two-register rule. The 212 row was an opportunity. Dropping it from an application ledger was correct. Treating the drop as a missing application would be wrong.

## 212 to 163

Still undocumented.

The prior Gmail-only floor used as the [S1] base was 163. The relationship from the 212-row audit to that 163 is not reconstructable in this repository. The [S1] and [S2] workbooks are not in the artifact set. See `artifacts/platform/KEEGAN-EXPORTS-ABSENT.md`.

This freeze does not inherit 163, 212, or 247 as counts. Those remain prior-audit floors.

## Dedupe key includes cycle

The unit of analysis is `company_canonical + role_as_listed + cycle`. Application IDs are `company-slug|role-slug|c{n}`.

FOSSA in this corpus: receipt 2026-04-22, decline 2026-05-20, second receipt 2026-05-21. That is `c1` then `c2`.

Attentive: receipt 2026-06-22, decline 2026-07-07, second receipt 2026-07-15. That is `c1` then `c2`.

A key that omitted cycle would collide those pairs.

## Stored outcome versus derived interview (jobmail.io)

Disclosed, not recoded.

`jobmail-io|growth-lead|c1` is in the 14 because cursor events include `recruiter_screen`. Stored `terminal_outcome` is `rejected_no_interview`. Interviewed is derived from Table 2 and is never stored. The disagreement is expected under that rule. Recoding the close would rewrite Freeze 1.

## Capture recapture not computed

The protocol restricts two-source capture recapture to LinkedIn rows submitted through an external ATS, not Easy Apply. Freeze 2 has LinkedIn pages 1 to 10 without that channel label. Naive Lincoln Petersen on Gmail overlap versus Easy Apply is a misuse and was not run.

The overlap stratum is unmeasured. Completeness is therefore not reported as a percentage.
