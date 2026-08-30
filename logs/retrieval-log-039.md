# Retrieval log 039

**Adjudication of the four unresolved rows from log 038.** All four resolve on artifact. Zero remain open. Three targeted Gmail queries plus a re-read of log 020.

## Result

| row | prior | ruling | net effect |
|---|---|---|---|
| LI-014 Insignia Assets | unresolved | `net_new` | +1 |
| LI-048 Jobright.ai, PM | unresolved | `distinct_cycle_net_new`, cycle 2 | +1 |
| LI-058 Jobright.ai, AI Engineer | unresolved | `net_new` | +1 |
| LI-097 HartleyCo | unresolved | **`duplicate_of_ledger_row`** | 0 |

**Revised dedupe:** `net_new` 82, `duplicate_gmail_receipt` 17, `net_new_employer_artifact_exists` 3, `distinct_cycle_net_new` 2, `duplicate_of_ledger_row` 1. Total 105.

**Net additions from LinkedIn: 87.** Up from the 84 held in log 038, because three of the four unresolved rows were additions and only one was not.

**Two overlap figures, and they are not the same number.**

- Rows already represented in the census: **18 of 105, 17.1 percent.**
- Rows that produced ATS or receipt mail: **17 of 105, 16.2 percent.**

The second is the capture-recapture stratum, the set where both sources could have observed the same application. LI-097 belongs to the first and not the second: it produced recruiter email, never an ATS receipt. **Use 16.2 percent for the estimator and 17.1 percent for the reconciliation.** Conflating them would inflate the stratum by one and misstate the method.

## LI-097, HartleyCo. The double-count risk was real and is now closed.

Log 038 flagged this as the live risk. It was correctly flagged, and the ruling goes the way that protects the census.

The thread, `gth_59384916f1d2f6ca` and successors:

| when | artifact |
|---|---|
| 2026-07-12 15:19 | LinkedIn submission, HartleyCo, GTM Engineer (this row) |
| 2026-07-13 04:39 | Josh Kelly, eml_0a253147bb65: **"Thanks for applying for the GTM Engineer position I'm working on for a client in SF."** |
| 2026-07-13 12:38 to 13:25 | Reply, availability, Google Meet invite for 09:45 the same morning |
| 2026-07-14 08:44 | Recap: "a YC-backed AI infrastructure startup building the simulation, evaluation, and..." |
| 2026-07-23 09:14 | **"Update on the Founding GTM Role at Bluejay"** — "they've decided to move forward with other candidates" |

The recruiter's own words settle it. **This row is the application that produced the process the ledger already counts.** "Confidential client via HartleyCo" is one of the eleven in-census interviews. Adding LI-097 as a new application row would have counted one process twice.

Instead it does the opposite of adding: it **supplies the missing submission evidence and an exact date** for a ledger row that previously had an interview with no evidenced application behind it.

Three field resolutions fall out, and all three close open threads:

1. **`underlying_employer` = Bluejay.** The "confidential client" is no longer confidential in the working record. Whether it is named in the manuscript is a separate decision; the redaction protocol in `04-engagements.md` governs engagements and counterparties, not employers applied to, so it does not decide this.
2. **`terminal_outcome` = `rejected_after_interview`, 2026-07-23, precision exact.**
3. **`evidence_class` upgrades to `employer_artifact`**, making four such upgrades in total with Bask Health, BX Studio and The Hog.

**One metric observation, flagged not claimed.** Submission 2026-07-12, recruiter contact 2026-07-13, screen held the same day, decline 2026-07-23. `days_to_first_response` = 1, both dates exact. Eleven days end to end. Whether that is the fastest full process in the corpus is a question for Results, not a claim here — it needs the exact-precision subset computed.

## LI-048 and LI-058, Jobright.ai. Not one ambiguity, two different rows.

The artifact, `noreply@jobright.ai`, **2026-03-31 17:05**:

> "Thanks so much for applying to the **Product Manager (Early Career)** role at Jobright.ai. The hiring team has carefully reviewed your application and decided not to move forward on this role."

That is a **rejection**, dated **two months before** LI-048's submission of 2026-05-26. It cannot be the same event, and the direction matters: the terminal outcome precedes the second submission.

**That is exactly the condition the codebook cycle rule requires.** Cycle 1 carried `rejected_no_interview` dated 2026-03-31; cycle 2 was submitted 2026-05-26. LI-048 is `cycle = 2`, a clean net addition, and the same shape as FOSSA in the worked examples.

**Coding note that must be settled before Table 1 is written.** `role_as_listed` differs verbatim between the two cycles: "Product Manager (Early Career)" on the rejection, "Product Manager, Entry Level" on the LinkedIn row. `application_id` is `company_slug|role_slug|c{n}`. If `role_slug` does not normalize these to one value, the two cycles become two separate `c1` rows and the cycle relationship is destroyed. This is the FOSSA and Attentive collision from design principle 2, arriving from the other direction: there, one slug wrongly merged two cycles; here, two slugs would wrongly split one lineage.

LI-058 is AI Engineer, an unrelated role, with no Gmail artifact of any kind. `net_new`, no complication.

## LI-014, Insignia. Resolved as an addition; an entity question remains and does not block.

Log 038 suspected one event recorded twice. It is not.

The only Gmail item is Keegan's **own sent mail**, thread `gth_1aa4bb3bc36115a4`, 2025-11-18 09:53:46 UTC, to `eml_16011a3a61e9`, subject "Operator / architect / Atlanta resident", resume attached, opening "Outdated resume. Currently owning sole GTM Engineering role @ SaaS company amidst brand reconfiguration..." **One message, no reply, no role named.**

That is outbound cold outreach, not an employer artifact and not a receipt. So:

- **`net_new`.** Nothing in Gmail duplicates this submission.
- **`evidence_class` stays `platform_log`.** This is the distinction that separates LI-014 from Bask Health, BX Studio, The Hog and HartleyCo: those four have *employer* correspondence. A row's own outbound mail never upgrades its evidence class. Worth stating plainly, because it is an easy error to make in the other direction.

**Open coding note, non-blocking.** Whether "Insignia Assets" (LinkedIn, Head of Digital, req 4323010631) and insigniacollab.com are the same entity. If yes, the email is a `followup_sent` event on this row. If no, it is a separate opportunity-register row and the same-day timing is coincidence. **Not resolvable from the corpus** — it needs the job posting or a company lookup. Either way the count is unaffected, which is why this does not block.

Note also that log 020's retriever recorded the company as "Insignia Collab," reading it off the email domain. LinkedIn's `company_as_listed` is "Insignia Assets." Neither is wrong; they are two sources naming what may be two things. `company_as_listed` is verbatim per source and is never overwritten.

## Instrument note

A bare full-text search for `insignia` across the window returned four threads, **all newsletters, none the actual artifact.** The artifact surfaced only on a query including `insigniacollab`. The company token lives inside an email address and did not match the shorter term.

This is the same failure mode that killed the batched company-name method in log 038, seen from the other side: there, common words produced false positives; here, a domain-embedded token produced a **false negative**. Both are properties of Gmail full-text search, not of the corpus.

**Consequence for the stop rule.** "A search returned nothing" is not evidence of absence unless the query shape can be shown to reach the artifact class in question. Any future absence claim in this project should name the query that was run.

## Status

**Zero unresolved rows in the LinkedIn applications stratum.** Stop condition 8 is met for the four sources swept to date. The census total still cannot be stated: Q3b, Q6, Q9, Q10 and Q8 blocks 4 to 6 are unexhausted, and each can still flip a `net_new` row to a duplicate.

## Open, carried forward unchanged

- `submission_channel` non-conforming on all 105 rows, falsified for at least 17. Integrity defect 4.
- Attentive second cycle present in Gmail, absent from the LinkedIn export. Bears on stop condition 3.
- Whether "Insignia Assets" and insigniacollab.com are one entity.
- `role_slug` normalization for the Jobright cycles.
- Triage the 114 inbound LinkedIn conversations.
- `Invitations.csv`, Saved Jobs, screening-question responses.
- Q3b, Q6, Q9, Q10; Q8 blocks 4 to 6; Q12 pagination.
- **Five engagement descriptions. Still blocking Methods.**
