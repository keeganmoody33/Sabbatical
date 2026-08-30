<!-- kit-meta
file: 02-current.md
tier: 2 (volatile)
created: 2026-08-29 13:37 ET
updated: 2026-08-30 (rev 15, Jobright audited and sized; 33@lecturesfrom.com dropped)
review-by: 2026-09-29
sources: [S1] [S2] [S3] [S4] [S5] [S6] [logs 035, 037-048]
-->

# Current state

Everything here is assumed stale until the meta block says otherwise. Delete and regenerate freely.

## Where the project is

**Retrieval, late stage. Nothing of the paper is drafted.** The codebook is frozen at rev 2 and coder 1 has not run.

## Census status: no total may be stated

Three strata, tracked separately since log 035 established that every exhaustiveness claim in logs 021 to 033 was exhaustive with respect to Gmail and Calendar only.

| stratum | status |
|---|---|
| Gmail | Q1, Q2a-d, Q3, Q4, Q5, Q7, Q7b exhausted, 1,152 threads. Q3b, Q6, Q9, Q10 pending |
| Calendar | **Q8 exhausted [log 045].** Stop condition 2 met, genuinely this time |
| LinkedIn | export in hand, **applications stratum dedupe-resolved (log 038)**; 114 inbound conversations untriaged |

**LinkedIn dedupe, resolved 2026-08-30 [logs 038, 039]. Zero rows unresolved.**

| dedupe_status | rows |
|---|---|
| `net_new` | 82 |
| `duplicate_gmail_receipt` | 17 |
| `net_new_employer_artifact_exists` | 3 |
| `distinct_cycle_net_new` | 2 |
| `duplicate_of_ledger_row` | 1 |

**Net additions from LinkedIn: 87.**

Two overlap figures, which are not interchangeable:

- Rows already represented in the census: **18 of 105, 17.1 percent.** Use for reconciliation.
- Rows that produced ATS or receipt mail: **17 of 105, 16.2 percent.** Use for the capture-recapture stratum.

LI-097 belongs to the first and not the second: it produced recruiter email, never an ATS receipt.

Both figures are an upper bound on additions and a lower bound on overlap, because Q3b, Q6, Q9, Q10 and Q8 blocks 4 to 6 can still flip a `net_new` row to duplicate.

## Corpus retrieved, as measured

These are counts of what has been pulled, not of what it means. All artifact-derived.

| | |
|---|---|
| Study window | 15 months, 2025-06-01 to 2026-08-29 |
| Retrieval logs | 45 |
| Gmail threads captured, logs 001-025 | 1,152 |
| Calendar events enumerated, all 6 blocks | **277** |
| LinkedIn applications, all-time / in-window | 1,279 / **105** |
| LinkedIn messages, all-time / in-window | 5,256 / 1,664 across 494 conversations |
| Inbound candidate conversations (upper bound, untriaged) | 114 |
| Counterparty meetings awaiting classification | **34** |
| Engagements evidenced | 5 (ENG-A to ENG-E) |
| Months with no evidenced engagement activity | 3 of 15 |

## THE CENSUS IS NOW GROUND-UP. The 247 is retired.

**Census: 321 applications, 298 distinct companies.** Stated only in `08-census-ledger.md`, which is the running count.

The 247-row pre-sweep workbook is **no longer an anchor or an input to any total.** It was built before the sweep existed, from a smaller corpus, by a method this project cannot reproduce; every use of it as a base imported an unauditable figure and later required a correction. It stays in `sources.md` as [S1], a historical source.

Construction: 238 Gmail/ATS rows extracted row-level from logs 001-034, plus 105 LinkedIn rows less 18 already represented, less 4 adjudicated removals. Every row traces to a named artifact in a numbered log.

**First outcome distribution the project has been able to compute:** 121 no determinate outcome, **101 no reply at all**, 71 rejected without interview, 9 role closed, 8 interview scheduled or held, 7 rejected after interview, 3 assessment sent, 1 converted to contract. Of the 200 rows with a determinate outcome, **half got no reply.**

## Superseded: the old Gmail-dedupe gap

The LinkedIn stratum was deduped against the census in logs 038 and 039, producing a measured 87 net additions.

**The Gmail stratum has never had the same treatment.**

The 247 came from the reconciled audit workbook [S1], which **predates the entire sweep**. Logs 001 to 034 then swept Gmail exhaustively across eight query families and surfaced applications the prior audits did not contain — the query manifest alone lists ten entities under "exclusions overturned by artifact," and the per-log company rosters run to roughly two hundred names.

**Nobody has ever compared that roster against the 247.** So:

- The LinkedIn addition (87) is **measured**.
- The Gmail addition is **unknown and uncounted**.
- 247 + 87 = 334 is therefore a **provisional floor**, not a total, and it is missing an entire stratum's additions.

This is the same failure class as the interview count: a figure inherited from a pre-sweep workbook, never recomputed against the corpus that superseded it. **It is now the largest single unknown in the census.**

**Required:** run the log 038 set-comparison method in the opposite direction — extract every company from logs 001 to 034 and compare against the 247-row ledger. The roster already exists; three subagents built it during the LinkedIn dedupe.

## Headline numbers, as of the reconciled audit [S1] — now superseded in part

| Metric | Value | Note |
|---|---|---|
| ~~Confirmed unique applications, 247~~ | retired | Pre-sweep, unreproducible. Not an input to any total |
| **Census (ground-up)** | **321** | See `08-census-ledger.md`. A floor with six named gaps, not an estimate |
| Known-held in-census interviews | **≥13** | the eleven, plus Dagster [log 040] and Hypergen [log 043]. **Floor, not a count.** 34 meetings unclassified |
| Application-to-interview rate | **not computable** | numerator is a floor, denominator is provisional and moving. Any figure stated now would be wrong in both terms |
| Applied companies interviewed | 11 | **WRONG. Do not use.** Inherited from [S1], never derived from the corpus. Dagster Labs is a twelfth, evidenced [log 040] |
| Application to interview rate | 4.45 percent | **Do not use.** Numerator wrong AND denominator superseded |
| Census completeness | 88 to 93 percent | asserted, not estimated. Method pre-registered but see the threat below |
| Distinct normalized companies | 229 | pre-LinkedIn |

**Threat to the completeness estimator [protocol.md].** The pre-registered capture-recapture restricts the estimate to LinkedIn rows submitted through an external ATS rather than Easy Apply. The extract codes all 105 rows Easy Apply, which would empty that stratum. Log 038 identifies the stratum empirically instead: **the 17 duplicates are exactly the rows that produced ATS mail.** The estimator has a measured stratum for the first time, and the blanket Easy Apply assignment is falsified for at least those 17.

## Role lanes, 247 applications [S1 Role Analytics]

Explicit GTM engineering 108, Sales/solutions engineering 30, RevOps/GTM ops/strategy 30, Growth/demand/marketing 23, Sales/BD/partnerships 22, Unspecified 15, Product/AI/technical adjacent 15, Other 4. **Not yet recomputed against the LinkedIn additions.**

## Monthly distribution

Two disagreeing versions remain in play [S1] [S2], and the paper must show one and explain the other. **The LinkedIn 105 are the fix for the date-precision problem**: all carry minute-level exact timestamps with a job URL, so Figure C's exact-only variant now has real substance rather than a thin remainder [log 035].

LinkedIn monthly, in window: 2025-06 5, 07 7, 08 1, 09 **0**, 10 **0**, 11 1, 12 **0**, 2026-01 2, 02 5, 03 7, 04 15, 05 5, 06 32, 07 25, 08 0 (export cut 2026-08-19).

**A third instrument agrees on the winter trough [log 045].** Block 3 (2025-11-28 to 2026-02-26) holds 34 calendar events, of which **only four are counterparty meetings**. Block 1 holds 58 events with roughly twenty. The 2025-12 to 2026-02 stretch is sparse in the **meeting layer**, independent of the LinkedIn application series and of the engagement register, and it covers two of the three months with no evidenced engagement activity. Report the agreement; make no causal claim.

**Figure C has a result and it is not the simple one.** Outbound applications during ENG-C (2025-09 to 12) run 0, 0, 1, 0 — they stop almost completely. During ENG-D and ENG-E (2026-04 onward) they run 15, 5, 32, 25, the highest volume of the window, while two engagements are live. Inbound candidate approaches over the same autumn run 5, 7, 7, 3 — **they do not stop.** The dead zone was in one channel only, and it was the channel the original census was built on. Report as-is, with no causal account.

## Opportunity register [S1, logs 031, 032, 036, 037]

**The community channel now has a numerator [log 042].** Subject-supplied origins, `evidence_system = memory`:

- **GTM Cafe** (formerly Clay Cafe): Every.to, Pearl (via a Garrett Wolfe referral), Great Question, Pin, Doug Shankman, Adam — **six** processes reaching a real conversation, four of them traced to one Slack channel, `#jobsandopportunities`.
- **GTM Engineer School**: Mixmax/ENG-C, The Kiln — **two**, both counterparty-initiated, plus the Jorge Macias and Kellen Casebeer relationships.
- **Platform-sourced processes reaching an interview**: The Hog (LinkedIn), PhrasIQ (Wellfound), Beautiful.ai (Jobright), Dagster Labs (ATS-direct) — **four.**

Roughly eight of fifteen named processes that reached a conversation came through two GTM communities; four came through the platforms the census is built on. **This is what amendment A3 exists to make measurable, and the two communities behave differently** — the Cafe sources applications and conversations through a jobs channel, the School sources relationships and inbound approaches.

**Caveat that must travel with the figure.** The *attributions* are recall and carry `evidence_system = memory`. **But the channel itself is no longer recall-only [log 043]:** `🔧 GTM Engine Room — GTMCafe Session` appears on the calendar five times (2026-04-01, 04-08, 04-15, 04-29, 05-06), Tier A evidence of active recurring participation. The "artifact-confirmed only" variant of the community figure is no longer empty. Still **report twice: all sources, and artifact-confirmed only.**

**The two pipelines fail at opposite ends [log 048].** Five counterparty-initiated processes reached a real human conversation — The Kiln (two founder calls in 32 hours), Glytec (CEO to VP Sales), Starbridge (founder to Head of Growth), Opsin (recruiter screen to founder interview, 2nd round specified in writing), WorkOS (recruiter to booked screen). **None produced an offer. Two produced no communication of any kind afterwards.** The application census mostly fails *before* reaching a conversation; this channel fails *after* it. Stated for the corpus only — n is five, the processes are not independent, and one subject supports a description, not an inference.

**The two pipelines are now the same size: 13 and 13 [log 049].**

Counterparty-initiated processes reaching a real conversation (13): Mixmax, Glytec, Starbridge, WorkOS, The Kiln, Opsin, Weave, Adam, TrueBuilt, Mercor, **Hotglue**, Doug Shankman, Pin.

Against census interviews at ≥13. One pipeline is the residue of several hundred applications; the other came from communities, referrals and inbound.

**GTM Cafe now accounts for seven touches**: Every.to, Pearl, Great Question, Pin, Doug Shankman, Adam, **Common Room**. The last was a guess I made from the domain and got backwards — a GTM tooling company's employee met him through the community, not through sales. **Do not infer register from a counterparty's industry.** Against a 105-row LinkedIn application census and several hundred Gmail-sourced applications that produced almost nothing.

**Named counterparties, subject-supplied [log 042]:** Glytec — Clayton Maike, origin LinkedIn DMs with CEO Patrick Cua. The Hog — Hudson. Mixmax — Heath Barnett. Every.to — Austin. PhrasIQ — Eddie. Beautiful.ai — Emily. Pearl — Chris on the second interview, first counterparty not recalled. Great Question — Harry. Pin — Erica Stacy Tarwater, then Conor Kline. Mercor — Claire twice, then David Lou. Doug Shankman plus his CRO.

**TrueBuilt is reclassified [log 042].** It was recorded as producing no engagement. It did. He applied via LinkedIn (LI-067, 2026-06-21), the company **withdrew the requisition**, the CEO saw a video he had sent, asked whether he was open to **contract work**, and **a project proposal was submitted.** The application row takes `terminal_outcome = role_paused_or_closed`; the contract conversation needs its own opportunity row. The codebook cannot currently express that an application row spawned an opportunity row — proposed amendment **A5**, `event_type += converted_to_opportunity`.

**Adam Andrewjeski's exclusion is overturned [log 042].** Log 026 filed him as a Clay Cafe Slack connection with no company named. The subject states Adam interviewed him informally. `register = opportunity`, `discovery_source = community_gtm_cafe`, `company_canonical` stays `unknown`. Overturned by recall rather than artifact, and marked as such.

**Mercor converted to contract [log 042].** Two interviews with Claire, then David Lou, then a secured contract — matching the Instant Work Offer of 2026-08-20 and activation 08-21 in logs 014 and 015. `terminal_outcome = converted_to_contract`, the second row to carry the value introduced in A1.

**BCOFA / ENG-A.** The subject states it "fizzled out because they did not have money" and that he worked on it for a period. **He does not state whether he was paid**, so `compensation_evidenced = no_artifact_retrieved` stands and must not be read as unpaid.

**Jorge Macias: exclusion holds, now with a reason.** Mentorship and community, no concrete job opportunity. Met as a TA in GTM Engineer School, later a friendship. He runs gtm-engineering.io. Confirms log 023.

**Clay Cafe and GTM Cafe are one entity, renamed to gtmcafe.com.** `community_gtm_cafe` carries **`Clay Cafe`** as its only alias. **`Clay Club` is a separate entity and must not be aliased to it** — the "Clay Club Atlanta" event in log 030 is not a GTM Cafe artifact. Corrected 2026-08-30 after the retriever conflated them.

The 11 in-census interviews recorded in [S1]: Fullsteam, Glytec, Beautiful.ai, Orchestry Software, PhrasIQ, Every, Pearl, The Hog, **Bluejay via HartleyCo**, Hologram, Great Question.

**That list is incomplete, at least one entry is mis-coded, and the count must not be published.** Log 040 evidences a twelfth: **Dagster Labs**, GTM Engineer, phone interview held 2026-03-30, confirmed by two counterparty statements, post-interview decline 2026-04-03. The artifacts were captured in logs 006 and 018 but were never reconciled against the interview count.

**Orchestry is mis-coded, not missing [log 041].** The subject states he interviewed, and the artifacts support him: the 2026-03-25 slot was missed, a second slot was booked 66 minutes later, and it was held on 03-26. Jay Banga's decline thanks him "for the effort you have put into the interview process." Logs 006 and 022 captured every artifact and stopped reading at the miss. `terminal_outcome` is `rejected_after_interview`, not a missed process.

**The interview layer has now been probed twice and failed twice, in opposite directions:** Dagster Labs was a held interview absent from the count; Orchestry was a held interview recorded as missed. Neither was a retrieval gap. Both were reconciliation gaps between artifacts already in the corpus and figures carried forward from [S1].

The eleven was inherited from the reconciled audit workbook, which predates the entire retrieval sweep. Since then the sweep has surfaced Pin, Cyft, Starbridge, Inertia Growth, WorkOS, Orchestry, The Kiln and Dagster Labs, none of which the prior audits contained. **`interviewed` is a derived metric under design principle 1 and was never supposed to be a stored figure.** It must be recomputed from Table 2 events across the full corpus.

Four of these rows now carry `evidence_class = employer_artifact` supplied by the LinkedIn dedupe rather than by a receipt: Bask Health, BX Studio, The Hog, and HartleyCo/Bluejay. In each case the submission existed only in the LinkedIn export while the employer correspondence sat in Gmail, attached to nothing.

## Table 4, engagements

ENG-A through ENG-E, rev 2. Three of fifteen months carry no evidenced engagement activity: 2025-08, 2026-01, 2026-02. **Five descriptions still unwritten. This blocks Methods.**

## Open threads

| Thread | Status | Next action |
|---|---|---|
| ~~Dedupe the Gmail stratum against the 247~~ | **Moot [ledger]** | Superseded by the ground-up rebuild. The Gmail stratum is now 234 extracted rows, not a name list |
| Tapcheck 2026-03-30 / 04-06 | Flagged | Role is `unspecified` on both. Counted as one; becomes two if they were different roles |
| **Recompute the interview count from Table 2 events** | Evidenced twice [logs 040, 041] | Blocks every interview figure in Results. Numerator is inherited, not derived |
| **Mercor's register vs the Discussion's sharpest claim** | New [log 042] | Mercor has "Application Submitted" receipts and converted to contract. If it is an application-register row, log 032's "neither came through an application" is falsified as written |
| ~~PhrasIQ: two or three?~~ | **Closed [log 043]** | **Two.** Calendar shows exactly two events with Eddie. Subject was right; the codebook is wrong |
| ~~Pearl: rebuild the event list~~ | **Closed [log 043]** | **Two interviews** (05-05, 05-18). The five Gmail artifacts were reminders |
| A5 proposed, `event_type += converted_to_opportunity` | New [log 042] | For the TrueBuilt shape: an application that spawned an opportunity |
| A1 linkage ruling triggered | New [log 042] | Mercor is a second `converted_to_contract`. Log 032 said revisit if a second appears |
| Create the Doug Shankman opportunity row | New [log 042] | Memory-only, no artifacts anywhere |
| Re-read Inertia Growth for a mis-read outcome | New [log 041] | Three reschedules and a cancellation. Same churn shape as Orchestry, whose outcome was read from the wrong artifact |
| Sweep for `no_show` or cancellation treated as terminal | New [log 041] | Orchestry shows a miss is often followed by a rebooking within the hour |
| Five engagement descriptions | Not started | **Subject to write.** Blocks Methods |
| ENG-B real end date | Evidence-bound to 2025-07 | Subject to state. Decides whether 2025-08 is in the comparison group |
| `submission_channel` on 105 LinkedIn rows | Non-conforming and falsified for 17 | Integrity defect 4. Recode and establish what the export actually distinguishes |
| Attentive second cycle missing from export | New, log 038 | Does the LinkedIn export miss applications? Bears on stop condition 3 |
| ~~LI-014, LI-048, LI-058, LI-097~~ | **Closed [log 039]** | All four adjudicated on artifact. HartleyCo double-count averted |
| Insignia Assets vs insigniacollab.com | Open, non-blocking | Are they one entity? Decides whether the sent mail is a `followup_sent` event or a separate row. Not resolvable from the corpus |
| `role_slug` normalization, Jobright.ai as an employer | Open, blocks Table 1 | "Product Manager (Early Career)" vs "Product Manager, Entry Level". If not normalized, one cycle lineage splits into two c1 rows |
| 114 inbound LinkedIn conversations | Untriaged | Upper bound, not a count. Every one needs a coder |
| `Invitations.csv`, Saved Jobs, screening responses | Unexamined | |
| Q3b, Q6, Q9, Q10 | Pending | |
| ~~Classify the counterparty meetings~~ | **DONE [log 049]** | All 34 classified. 13 VEND, 12 VEND? (low confidence), 5 COMM, 3 OPP, 1 INT. **Nothing moved the census interview count** |
| **Export the YC Work at a Startup inbox** | **NEW, stop condition 6 [log 049]** | Hotglue came through it. A live channel carrying real hiring conversations that neither Gmail nor Calendar can see |
| Confirm the 12 `VEND?` rows | New [log 049] | Blanket "the rest are vendors" applied, but each conflicts with the subject's own earlier testimony or with artifacts. Changes exclusion reasons, not counts |
| Was the subject publicly showing a new role in early 2026? | New [log 049] | Kevin Wright opened with "Saw you just started in a new role." Bears on how counterparties approached him |
| Decide amendment A6 | New [log 045] | `discovery_source` for a counterparty booking the subject's scheduling page. **Five rows qualify**, clearing the bar log 032 set |
| ~~Re-sweep calendar blocks 1 to 3~~ | **Done [log 045]** | 177 events. 20+ counterparty meetings found that appear in no log. Blocks 1-3 had been read for known names, not enumerated |
| Ask the subject about Doug Shankman | New [log 044] | Was Doug pitching his CRO idea or discussing a role? Decides whether this is an interview at all. Also: what happened after |
| Classify Hollie Maddux, 2025-11-04 | New [log 044] | Counterparty meeting in no log |
| Verify the booking-page title hypothesis | New [log 044] | `connect \| KM (Doug Shankman)` = Doug booked Keegan's page. If the pattern holds it makes `register` artifact-derived across a dozen events |
| ~~Q8 calendar blocks 4 to 6~~ | **Closed [log 043]** | Blocks 4-6 exhausted. The Kiln has zero calendar presence — nothing followed off-platform |
| Classify six unknown counterparty meetings | New [log 043] | Hotglue (role named in title), Opsin, Vee/oaktheory ×3, Morpheus Interactive, Bottle Rocket Growth, Common Room |
| Correct the PhrasIQ worked example in `03-codebook.md` | New [log 043] | It specifies three rounds; the calendar shows two. The codebook is teaching the wrong shape |
| Sweep `keegan@morphdatastrategies.com` | New [log 043] | One unswept mailbox. `33@lecturesfrom.com` dropped by the subject 2026-08-30 |
| Q12 pagination | Page token `tok_2e25d4a276d2` | May flip `compensation_evidenced` on ENG-A and ENG-D |
| ~~`33@lecturesfrom.com`~~ | **Dropped by the subject, 2026-08-30** | Not to be swept. Removed from the census gap list |
| **Jobright export** | **Sized gap, audited 2026-08-30** | Census holds **zero** Jobright-channel rows. [S1] recorded 5 Jobright-only additions to the retired 247; by construction they are absent from the 321 and their identities are held nowhere in this project. **Subject to export `jobright_applications_log.csv`** (stop condition 5), then dedupe by the log 038 method |
| Ladders, YC WFS, Wellfound full exports | Not exported | Stop conditions 4, 6 |
| Talentpluto, Jobgether **and Colossus (LI-034)** underlying employers | Unresolved | Stop condition 7. Colossus added [log 048] — LI-034 is a different client from the Opsin process |
| ~~HartleyCo underlying employer~~ | **Closed [log 039]** | = **Bluejay**, a YC-backed AI infrastructure startup. Manuscript naming is a separate decision |
| WorkOS 212-vs-247 discrepancy | Unresolved | Integrity defect 1 |
| 212 to 163 reconciliation | Undocumented | Integrity defect 2 |
| Window disagreement, 08-25 vs 08-27 | Unresolved | Pick one, restate in Methods |

## Paper status

Nothing drafted. Structure agreed: Abstract, Introduction, Methods, Results, Discussion, Conclusion, with figures [S6].

Figures specified, none built:
- Applications per month, exact-date subset (now substantial), with the approximate-date count annotated
- Source reconciliation waterfall, raw rows to net unique
- Role lane distribution
- Evidence tier and evidence class composition
- Funnel, with the opportunity register as a parallel track
- Figure C, dual-axis applications against engagement concurrency, produced twice

## Derivatives planned

Substack post and LinkedIn post, downstream of the paper. Not started [S6].

## Changelog

- 2026-08-30: rev 15. **Jobright audited [ledger].** The census contains zero Jobright-sourced applications — Jobright.ai appears three times as an *employer* only. The 5 Jobright-only rows that fed the retired 247 left the count with it and cannot be recovered from this corpus. Recorded as a **sized gap**, not applied as a correction. Register row counts re-verified with a CSV parser: 321 rows / 234 gmail-ATS / 87 LinkedIn / 298 companies / 35 undated — agrees with the ledger. `33@lecturesfrom.com` dropped at the subject's instruction.
- 2026-08-29 13:37 ET: created from [S1] to [S6].
- 2026-08-30: rev 2. Census section restructured around the three strata. LinkedIn dedupe result added [log 038]. Completeness-estimator threat and its empirical fix recorded. Figure C result added [log 035]. Open threads rebuilt.
- 2026-08-30: rev 14. **Ground-up census adopted at 321; the 247 retired as an anchor.** Gmail/ATS stratum extracted row-level (238 rows) and merged with the LinkedIn stratum at row level, catching one duplicate the company-level dedupe missed. Four adjudicated removals. First outcome distribution computed. `08-census-ledger.md` created as the single running count.
- 2026-08-30: rev 13. All 34 meetings classified [log 049]. Hotglue resolved to YC Work at a Startup, counterparty-initiated — census interview count unchanged at >=13. **YC WFS identified as a live unswept channel (stop condition 6) and a fourth blind spot** after phone, DM and calendar deletion. Two Dougs resolved. 25 meetings excluded with a reason that were previously invisible.
- 2026-08-30: rev 12. LI-034 confirmed a different Colossus client [log 048 addendum 2]. No double count; 87 net additions unaffected. Second instance of one counterparty in two registers (after Exa) — a checkable defence of design principle 5.
- 2026-08-30: rev 11. Opsin closed [log 048]: `no_response`, anchor 2026-03-13, take-home never sent. Second `no_response` in the corpus. Phone-screen blind spot recorded — neither Gmail nor Calendar sees a phone-arranged, phone-held conversation. `evidenced_silence_days` needs a companion flag for zero post-interview contact.
- 2026-08-30: rev 10. Numbers audit. Corpus-retrieved counts tabulated. **Discovered that the Gmail stratum has never been deduped against the 247** — the LinkedIn addition is measured, the Gmail addition is not. 334 recorded as a provisional floor. Interview floor set at 13.
- 2026-08-30: rev 9. Blocks 1-3 re-swept [log 045]. Q8 genuinely exhausted. 20+ counterparty meetings recovered. Pin and the GTM Engineer School tasters are no longer memory-only. Booking-page hypothesis verified on five instances; A6 proposed. Calendar loss quantified at 6 of 7 on the Mixmax series. Critical path is now classifying ~26 meetings.
- 2026-08-30: rev 8. Doug Shankman resolved from artifact [log 044]: Renoir, eml_2db2f7ec072b, 2025-10-27, counterparty-booked, 15 minutes, no outcome artifact. **Q8's exhaustion claim withdrawn** — blocks 1-3 missed at least two counterparty meetings that were on the calendar all along. Third instance of retrieval reaching artifacts the reading did not.
- 2026-08-30: rev 7. Q8 calendar blocks 4-6 swept, Q8 exhausted [log 043]. PhrasIQ and Pearl conflicts closed in the subject's favour. Three held interviews found outside the eleven. Six unknown counterparty meetings opened. Calendar's blind spot documented.
- 2026-08-30: rev 6. Subject-supplied interview and origin register [log 042]. Community channel given a numerator. TrueBuilt reclassified, Adam's exclusion overturned, Mercor's conversion recorded, six new threads opened.
- 2026-08-30: rev 5. Orchestry retrieved [log 041]. Outcome corrected to `rejected_after_interview`; count unchanged. Second consecutive error found in the interview layer. Inertia Growth flagged for re-read.
- 2026-08-30: rev 4. Dagster Labs retrieved [log 040]. Interview count flagged as wrong and unauditable in its current form; recomputation from Table 2 added as a blocking thread.
- 2026-08-30: rev 3. Four unresolved rows adjudicated [log 039]. Net additions 84 to 87. The two overlap figures separated. HartleyCo underlying employer resolved to Bluejay and the double-count averted. Two new non-blocking coding notes opened.
