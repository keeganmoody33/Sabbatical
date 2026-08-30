<!-- kit-meta
file: retrieval-log-051.md
created: 2026-08-30
source: [S4] jobright_applications_log.csv, 40 rows, re-uploaded 2026-08-30
joined against: claude_full-application-register.csv (321 rows), claude_gmail-stratum-roster.csv (274 entities), linkedin-applications-in-window.csv
method: normalized name join, then manual grep for the three misses
-->

# Retrieval log 051

**[S4] re-joined against the ground-up census.** Its previous reconciliation ("40 raw rows, 5 net-new, 30 dupes, 5 out of window") was computed against the retired 247 workbook and against the old 2025-08-27 window. Both are gone. This is the join redone against the 321.

## Join result

| state | rows |
|---|---|
| Company and date both match a register row | 21 |
| Company matches, date does not | 15 |
| Company absent from the register entirely | 4 |

Of the 4 absent by name-match, 2 turned out to be present with a **blank** `applied_date` and were missed by the join, not by the corpus. See below.

## 1. Two blank dates recovered, precision upgraded

Both register rows carry `applied_date = ""` and `date_precision = unknown`. [S4] carries an exact date for each.

| register row | current | [S4] | effect |
|---|---|---|---|
| `Jobright.ai, Product Manager (Early Career)` (row 305, logs 006, tier B) | blank, `unknown` | **2026-03-27** | `unknown` to `exact` |
| `OpenObserve, Growth Marketer` (row 310, logs 010, tier A, ashby) | blank, `unknown` | **2026-06-24** | `unknown` to `exact` |

Both had a rejection date already (2026-03-31 and 2026-08-24). With the submission date filled, both rows become eligible for `days_to_first_response`, which the protocol computes only where both precisions are `exact`.

**Caveat on the precision label.** The tracker date is the platform's record of when it sent, not an employer artifact. Whether a tracker timestamp earns `exact` or a new precision value is a coder decision, not a retrieval finding.

## 2. One candidate net-new application: Axon

The register holds exactly one Axon row: `Manager, Go-to-Market Readiness`, 2025-08-04, tier A, email_direct, logs 002.

[S4] shows a second: **`Key Account Executive`, 2026-01-02, Atlanta GA, $82K to $138K, Applied by Agent.**

Counting rule 2 (same company, materially different title, is two applications) makes this a separate application cycle. Five months apart, so no cycle collision.

**Evidence state:** tier C, `platform_log` only. No Gmail artifact was found for it in logs 001 to 034, and Axon is in the Gmail roster on the strength of the August row. Counting rule 6 requires that an agent send count only when the receipt states the application was sent or a matching ATS receipt exists. The Jobright row does state "Applied by Agent." **Whether that string satisfies rule 6 is the decision this log cannot make.**

## 3. Three companies visible only in this file

Absent from the register, absent from the 274-entity Gmail roster, absent from the LinkedIn in-window set.

| company | role | date | method | band |
|---|---|---|---|---|
| Autodesk | Sr. Sales Specialist, Fusion Enterprise | 2026-01-02 | Applied by Agent | $155K to $278K |
| MavenAI | GTM Engineer | 2026-05-20 | Applied by Agent | not stated |
| Vanco | GTM Enablement Manager | 2026-06-24 | Applied by Agent | $90K to $110K |

Same rule 6 question as Axon, with less to lean on: for these three there is no other artifact for the company at all.

**If all four enter, the census moves 321 to 325.** **They do. See section 7.** The subject confirmed all four on 2026-08-30.

## 4. A systematic one-day offset in the 2026-05-20 batch

Ten rows carry a [S4] date exactly one day before the ATS receipt date in the register.

Nebius, DBeaver, FOSSA, TRACTIAN, Applied Systems, Pindrop, CoLab, VitalSource, Telnyx, Deepgram, NiCE: [S4] says **2026-05-20**, register says **2026-05-21**. WireScreen shows the same shape on a different date, [S4] 06-24 against register 06-25.

It is not universal. Onit and ServiceTrade appear as 05-21 in [S4] and 05-21 in the register. Nine of the 2026-06-24 rows match exactly.

**Read:** the agent queued a batch late on 05-20 and the ATS receipts landed 05-21. The two dates measure different events, submission versus acknowledgement, and neither is wrong.

**Action under extraction rule 9:** record the conflict in `notes` with both values. Do not average, do not pick silently. The register's receipt-derived date is the better-evidenced value and stays as `date_applied`.

## 5. Unframe, second artifact for a merged submission

[S4] shows Unframe 2026-04-17. The register carries 2026-04-06 only, because log 009 found receipts on both dates and the prior ledger merged 04-17 into 04-06 as the same opening. The rejection landed 2026-05-12, after both, so counting rule 4 does not license a second cycle and **the merge holds.**

What changes is corroboration: 04-17 now has an independent artifact outside Gmail.

## 6. What only this file carries

Neither of these exists anywhere else in the corpus.

**`submission_channel`.** The codebook vocabulary already contains `jobright_agent`. [S4] is the only artifact that can populate it.

| Application Method | rows |
|---|---|
| Applied by Agent | **31** |
| Manual/Unspecified | 6 |
| Not stated | 2 |
| Direct Apply | 1 |

Thirty-one of forty submissions in this stratum were sent by an automated agent rather than by the subject. **This populates `submission_channel` only. It does not populate `discovery_source`, and section 8 explains why the two cannot be inferred from each other.** Every one of those rows currently sits in the register with a channel inferred from the ATS that acknowledged it (greenhouse, ashby, rippling and so on), which records the delivery system and says nothing about who pressed send.

**Compensation bands.** 21 of 40 rows carry a stated range. The register has no compensation field at all.

## 7. Subject confirmation, 2026-08-30. `evidence_system = memory`

**"Yes I applied to these."** Axon (Key Account Executive), Autodesk, MavenAI and Vanco are admitted.

**State the basis precisely.** The artifact still says only "Applied by Agent." Counting rule 6 was not satisfied by the artifact and is not retroactively satisfied now. What admits these four is subject recall. They enter as `evidence_tier = C`, `evidence_class = platform_log`, with `evidence_system = memory` recorded alongside, the same provenance treatment applied in logs 031, 032 and 042.

**Census 321 to 325.** Log the move in `08-census-ledger.md` with this reason.

Rule 6 itself is **still unresolved as a rule.** This log did not answer it, it routed around it. The next agent-only row with no subject recall behind it will hit the same wall.

## 8. Discovery and submission are decoupled. This is the finding

Beautiful.ai does not appear anywhere in [S4]. Zero matches across 40 rows.

Log 042 records the origin from the subject: `Beautiful.ai, counterparty Emily, origin Jobright.ai`. The register carries the application as row 81, `GTM Engineer`, 2026-03-08, **greenhouse**, tier A, `rejected_after_interview` 2026-03-26.

**Subject's account, 2026-08-30:** the export is the complete Jobright record, and the role was found on Jobright but submitted on the employer's own site.

That reconciles every artifact. Greenhouse receipt, no Jobright row, real interview. **A tracker records what it sent. It does not record what you found.**

### Two consequences

**1. This explains, mechanically, why `discovery_source` is unrecoverable from artifacts.** `06-method-retrospective.md` already grades it "near zero from artifacts, ~100 percent recall-dependent, not fixable by more retrieval." That was an observed fact without a cause. The cause is now stated: **no platform in the corpus logs discovery. Every one of them logs submission.** The field is not under-retrieved, it is structurally unrecorded. That belongs in Discussion, not in the limitations list.

**2. A correction to this log's own section 6, and to what was said in chat before the subject's reply.**

Across the 43 register rows tied to these 40 companies: **18 `rejected_no_interview`, 16 `no_response`, 9 `unknown`. Zero interviews.**

The wrong reading is "Jobright produced zero interviews." The right one is:

> **Jobright agent-submitted applications produced zero interviews (0 of 43 rows).** Applications *discovered* on Jobright and submitted elsewhere are not enumerable from any artifact, and Beautiful.ai is a subject-reported instance of exactly that, with an interview.

No per-channel interview rate can be computed for Jobright, or for any discovery source. The denominator does not exist.

### The confidence on Beautiful.ai just dropped

Log 042 recorded the origin as stated. The subject's wording today is **"maybe I sourced from Jobright."** That is a hedge on a claim previously asserted, and the record takes the weaker of the two.

`discovery_source` for `beautiful.ai|gtm-engineer|c1` should carry the hedge explicitly rather than `jobright`. Recommend `unknown` with the candidate origin in `notes`, since an enum value cannot express "probably."

**Consequence for the paper:** Beautiful.ai is the only interview attributed to Jobright in the entire corpus, and that attribution is now a maybe. Jobright's contribution to the interview layer is **zero confirmed, one possible.**

## Open

1. **Rule 6 remains unanswered as a rule.** Section 7 admitted four rows on recall rather than deciding it. Does "Applied by Agent" in a tracker export satisfy "the receipt states the application was sent"? The next agent-only row without recall behind it is blocked.
2. **Precision label for a tracker-supplied date.** `exact`, or a new value.
3. **Compensation.** Adding a field to Table 1 after rev 2 is frozen is a codebook change. It is still pre-coder-1, so it would be a pre-registration revision rather than a deviation, but it has to be logged in `protocol.md` either way.
4. Backfill `submission_channel = jobright_agent` and `discovery_source = jobright` across the 36 matched rows during coding.

## 9. This log closes gap 6 in the census ledger. Added 2026-08-30

`08-census-ledger.md` names **"Gap 6: Jobright is a hole with a known size"** and sets **stop condition 5**: *"the full `jobright_applications_log.csv` export, deduped against the 321 by the same set-comparison method used on LinkedIn in logs 038 and 039."*

That is what sections 1 to 8 did. The subject confirmed on 2026-08-30 that the 40 row export is the complete Jobright record. **Stop condition 5 is met.** The gap 6 section should be struck and replaced with a pointer here.

The ledger made four testable statements. Three are now measured and one is refuted.

| # | ledger statement | measured |
|---|---|---|
| 1 | "The 321 contains zero Jobright-sourced applications. `jobright_agent` and `jobright` are used zero times." | **Confirmed.** Still zero until backfill. 36 matched rows can now carry `submission_channel = jobright_agent`, 31 of them evidenced by the method column |
| 2 | "The 30 dupes were measured against the 163-row Gmail floor... the true overlap against the current census is unmeasured and may be smaller or larger." | **Measured: 36 of 40, larger.** 21 exact company-and-date, 15 company-only. Overlap rose from 30 to 36 against the bigger census, the predicted direction |
| 3 | "The split of the 40 rows by method is unknown." | **Known.** 31 agent, 6 manual, 2 not stated, 1 direct apply |
| 4 | "If Jobright's agent submitted without generating mail to his inbox, agent-applied rows are invisible to Gmail, Calendar *and* LinkedIn simultaneously — a submission channel no instrument in this study can see." | **Bounded, and much smaller than feared. 3 of 31.** Only Autodesk, MavenAI and Vanco were invisible to all three instruments. The other 28 agent-submitted rows produced ATS mail and were already in the census |

**Finding 4 is the one worth carrying into Discussion.** The feared blind channel is real and it is 3 rows, not 31. An automated agent submitting on the subject's behalf did **not** generally suppress employer-side mail. That is a bounded answer to a stated fear, which is more useful than the fear.

### One prediction the ledger made that this log cannot settle

> "Those 5 Jobright-only additions were an input to the retired 247... **The 321 is short by at least those 5, by construction, and their identities are not held anywhere in this project.**"

**This log recovered 4, not 5:** Axon (Key Account Executive), Autodesk, MavenAI, Vanco.

Two candidates that would have looked like a fifth turned out to be **already present with a blank `applied_date`**, not absent: `Jobright.ai, Product Manager (Early Career)` and `OpenObserve, Growth Marketer`. Both were recovered as dates rather than as rows. See section 1.

Three explanations, none decidable from this repo:

1. [S1] counted one of its 5 against the **163-row Gmail floor**. The 321's 234-row Gmail stratum is larger and may have independently recovered that row, leaving 4 genuinely Jobright-only.
2. [S1] counted `Jobright.ai, Product Manager (Early Career)` as a net-new application, which the 321 already holds.
3. [S1]'s figure was wrong.

**Resolving this requires [S1] `job_search_reconciled_audit.xlsx`, which is not in this repo.** Until it is, record the census as **325** and note that a prior source claims a fifth Jobright-only row whose identity is unrecovered. Do not round up to 326 to match [S1]. That is the exact move retiring the 247 was meant to stop.
