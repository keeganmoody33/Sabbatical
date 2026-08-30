<!-- kit-meta
file: 05-codebook-amendments-r1.md
tier: 0 (durable)
created: 2026-08-30 ET
status: PENDING APPROVAL. Nothing here is in force until the subject approves and 03-codebook.md is revised.
sources: [logs 031, 032, 035, 036, 037] [03-codebook.md] [protocol.md]
-->

# Codebook amendments, revision 1

Four changes were carried forward as pending in log 037. On inspection against `03-codebook.md`, **one is already in force and two need reshaping**. What follows is the corrected set.

## Why now, and only now

`protocol.md` freezes the codebook before coder 1 runs. Coder 1 has not run: `CORPUS-MANIFEST.md` is unpopulated and no Table 1 rows have been written. **Migration cost today is zero.** After the dedupe writes rows, every one of these changes invalidates prior coding and must be logged and disclosed in the paper as a mid-study protocol deviation.

This is the last cheap moment.

---

## A1 — `terminal_outcome`: add `converted_to_contract`

**Status: needed.** Not present in the current vocabulary. Source: log 031, restated in log 032.

**Value:** `converted_to_contract`

**Definition:** The process terminated because the counterparty engaged the subject on paid or contract work, rather than by hire, rejection, withdrawal, or silence. It is a terminal state for *the process*, not for the relationship.

**Coding rule:** Applies to rows in either register. An `opportunity` row may convert (ENG-C); an `application` row could in principle convert and must be codeable if one does.

**Linkage:** The resulting work is a Table 4 row. Record the `engagement_id` in Table 1 `notes` — e.g. `converted to ENG-C`. Log 032 already ruled that a dedicated field is not warranted for a single row. Revisit only if a second conversion appears.

**Effect on derived metrics:** `converted_to_contract` is **not** an interview-set event and does not enter `interview_rate`. It must appear as its own line in any outcome distribution, never folded into `still_open` or `no_response`.

**Decision needed:** none. Recommend adopt as written.

---

## A2 — `no_response` is already in force. The real gap is the anchor field.

**Status: the amendment as written is a no-op.** `no_response` is already a `terminal_outcome` value in `03-codebook.md`. Logs 036 and 037 flagged it as missing; it is not.

Also already in force: `reschedule` exists in `event_type`, closing open item 5 in `QUERY-MANIFEST 2.md`.

**The gap those logs were actually pointing at is real and is not fixed.** The Kiln (log 037) is coded `terminal_outcome = no_response`, `terminal_outcome_precision = evidence_bound`, bound 2026-07-17. Table 1 requires `date_evidence_anchor` whenever `date_applied` carries `evidence_bound` precision — **but there is no equivalent anchor for `terminal_outcome_precision`.** The bounding date currently has nowhere to live except free text, which design principle 6 forbids.

**Amendment:** add one field to Table 1.

| field | type | definition |
|---|---|---|
| `terminal_outcome_evidence_anchor` | date | Required when `terminal_outcome_precision = evidence_bound`. The artifact date that bounds the outcome. |

**Coding rule for `no_response`:** the anchor is the date of the **last unanswered outbound message from the subject**, not the date of the counterparty's last reply. For The Kiln that is 2026-07-17, not 2026-03-04. This makes the silence measurable — the interval between the last counterparty message and the anchor is the ghosting duration, and it is derivable rather than asserted.

**Decision needed:** none. Recommend adopt. This is a strict addition; it invalidates no vocabulary.

---

## A3 — `discovery_source`: split the community channel

**Status: needed, and it is the highest-stakes of the four.** Source: logs 032 and 036, both arguing for two values.

**Current:** a single value, `newsletter_community`, fusing newsletters and communities.

**The problem:** log 032 identifies the paper's strongest structural result — *the instrument that captures applications is blind to the channel that produced the outcomes*. That result is a claim about the GTM community channel specifically. **It cannot be measured on a field that bundles communities with newsletters,** and it cannot be disaggregated afterward.

**Evidence for splitting the two communities rather than using one community value:** they behave differently and produce different register outcomes.

| community | produced | register | ATS artifact? |
|---|---|---|---|
| GTM Cafe (formerly Clay Cafe) | Pin — two rounds plus take-home, deepest application-sourced process of 2025 | `application` | none. Recovered only by subject recall |
| GTM Engineer School | ENG-C (largest paid outcome of the window), The Kiln (two founder calls in 32 hours), June 2025 events, cohort taster sessions — four appearances | `opportunity` | none |

One produced an application. The other produced counterparty-initiated processes, repeatedly. Collapsing them hides that.

**Amendment:** retire `newsletter_community`. Replace with four values.

- `community_gtm_cafe`
- `community_gtm_engineer_school`
- `community_other` — a third community, so no future row is forced into one of the two named ones
- `newsletter` — genuinely a different channel and should never have shared a value

Full revised vocabulary: `linkedin`, `wellfound`, `jobright`, `ladders`, `yc_wfs`, `referral`, `recruiter_inbound`, `company_site`, `community_gtm_cafe`, `community_gtm_engineer_school`, `community_other`, `newsletter`, `unknown`

**Migration:** no Table 1 rows currently carry `newsletter_community`. Zero recoding.

**Decision needed — one, and it is yours:** whether the two communities are **named in the published paper** or reported as `community_A` / `community_B`. The redaction protocol in `04-engagements.md` covers engagements and counterparties, not channels, so it does not decide this. Arguments both ways: GTM Engineer School is already publicly associated with you through your own published testimonial, so naming costs little and makes the result concrete and checkable; against, naming a specific community alongside a finding about which channels convert invites a reading you have not tested. **The working record keeps names either way** — this only governs the manuscript, and it can be deferred to the redaction step without blocking anything.

---

## A4 — recording that a network contact caused an ATS submission

**Status: needed, and reshaped.** Source: log 035, the Greg Reardon case — 10 messages, 2025-07-26 to 07-31: *"throw an application in, ill let my recruiting team know to keep an eye out."*

**The gap:** `discovery_source` records where the role was *found*; `submission_channel` records how it was *sent*. Separating them is correct (design principle 3). But neither records that a named contact **caused** the submission and offered internal advocacy. Coding this row as `discovery_source = referral` would also be wrong on the facts if the role was found elsewhere.

**Rejected approach:** a `referral_type` field on Table 1. It would be a stored rollup of an event, which design principle 1 forbids, and it would force a single enum choice on a case that is two things at once — Greg Reardon both suggested applying *and* offered internal advocacy.

**Amendment:** store the observation, derive the rollup.

Add to Table 2 `event_type`:

- `referral_offered` — a named contact suggests or encourages a submission, or offers internal advocacy for one. `counterparty_name` and `counterparty_role` carry who. `event_date` carries when, which makes the relationship to `date_applied` visible rather than asserted: an event before the application is causal, an event after it is advocacy on an application already submitted.

Add to derived metrics, never stored:

- `referral_assisted` = any application with at least one `referral_offered` event.

**Two consequences to accept:**

1. **A referral that produced no application cannot be stored.** Table 2 events require a parent Table 1 row. A contact who offered a referral that went nowhere belongs in Table 3 exclusions, with `what_would_promote_it` naming the submission artifact that would move it into the census. Worth checking the 114 inbound LinkedIn conversations for these when they are triaged.
2. **`medium` is ambiguous for a LinkedIn DM.** The current enum is `video`, `phone`, `onsite`, `async`, `email`. `async` most plausibly meant asynchronous assessment. A DM is neither that nor email.

**Decision needed:** add `message` to `medium` for DMs and chat, and reserve `async` for asynchronous assessments — or accept `async` as a catch-all and document it. Recommend adding `message`: it costs nothing now, and the LinkedIn export is 1,664 in-window messages across 494 conversations, so this medium is about to become common in Table 2.

---

## Summary of what changes

| # | change | type | migration cost | decision needed |
|---|---|---|---|---|
| A1 | `terminal_outcome` += `converted_to_contract` | vocabulary addition | none | no |
| A2 | Table 1 += `terminal_outcome_evidence_anchor` | field addition | none | no |
| A3 | `discovery_source`: `newsletter_community` → 4 values | **vocabulary replacement** | none today | yes — naming in the paper (deferrable) |
| A4 | `event_type` += `referral_offered`; `medium` += `message` | vocabulary addition | none | yes — `message` vs `async` |

A3 is the only replacement rather than addition, and it is the only one that becomes expensive the moment coding starts.

## On approval

1. Revise `03-codebook.md` and append to its changelog with date and reason.
2. Log the amendment set in `protocol.md` — it predates coder 1, so it is a pre-registration revision, not a deviation, and should be stated as such.
3. Then, and only then, run the 10-query dedupe against the 105 LinkedIn rows.
