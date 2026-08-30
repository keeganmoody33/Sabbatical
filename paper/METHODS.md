# Materials and methods

I am the subject of this dataset and the author of this paper. That dual role is a limitation. It is not a footnote. Independent model coding of the Gmail extracts is not a human gold standard. A stranger with the same exports should be able to rebuild the census. That is the test.

## Window and unit

The window is 2025-06-01 through 2026-08-29, America/New_York, inclusive. Fifteen months. Earlier audits searched from late August 2025, so June 2025 through early November 2025 was unharvested in those ledgers rather than empty.

The unit of analysis is one application cycle: `company_canonical` plus `role_as_listed` plus `cycle`. Same company and a materially different title is two applications. Same company, same title, plus reminder and rejection threads, is one. A new receipt after a terminal outcome on the same company and title is a new cycle. FOSSA (receipt 2026-04-22, decline 2026-05-20, second receipt 2026-05-21) and Attentive (2026-06-22, decline 2026-07-07, second receipt 2026-07-15) are the worked cases. A key that omitted cycle would collide those pairs.

I never invent a company or a title. A receipt that omits the role is `unspecified`.

## Two registers

A job search has two pipelines. Mixing them makes both unmeasurable.

The **application census** is roles I submitted. It is the only denominator for an application-to-interview rate.

The **opportunity register** is recruiter-initiated processes, referrals, matching-platform contracts, and consulting prospects. Those conversations happened. They produced interviews and, in some cases, money. They do not enter the application census, because putting them there would inflate conversion with outcomes that did not come from applying.

WorkOS is the closed example. TopHire approached me for a remote GTM Engineer role in August 2025. A slot was booked. No submission receipt exists in the frozen corpus. `register = opportunity`. It stays in the dataset. It does not enter 14/298.

## Freeze discipline

A freeze is a locked snapshot of evidence. After it, those artifacts are not recoded. Later work may add a source or a sidecar overlay. It may not rewrite the earlier extracts.

**Freeze 1.** Gmail and Calendar extracts. keeganmoody33@gmail.com, logs 001 to 021, 994 threads. 33@lecturesfrom.com, logs 022 to 029, 177 threads. Calendar on 33@lecturesfrom.com: 31 events across five 90-day blocks with no keyword filter. Transferred keegan@lecturesfrom.com calendar: reachable and empty. Two independent extracts, `cursor` and `bravo`, coded without seeing each other's rows. Alpha CSVs were not on disk for this pass. After include/exclude adjudication and alias merge: **221** applications with `register = application`.

**Freeze 2.** LinkedIn applied-list pages 1 to 10 (99 rows, relative stamps, `date_capture` 2026-08-29) and the Jobright tracker (40 rows, exact dates). Freeze 1 Gmail was not recoded. Platform rows were mapped onto Freeze 1 on company, role, and cycle. Titles that expand or abbreviate the same opening do not increment the census. Net-new `platform_log` applications: **77**. Full census: **298**. Platform files carry no interview-set events. LinkedIn `submission_channel` is `unknown`. The applied list does not label Easy Apply versus an external ATS. This codebook does not import the package value `linkedin_easy_apply`. Page 10 of the applied list is full, so a later page is not ruled out.

**Freeze 3.** Remaining personal Gmail on keeganmoody33@gmail.com: Q7 re-run from the start (195 unique threads), Q6, Q9 (178 unique threads, including spam and trash), Q3b. Primary calendar, five 90-day blocks, no keyword filter: 338 events. Hidden calendars MCAT PREP and SI CHM222 were listed and not swept. Net-new applications: **0**. Opportunity rows added in freeze coder files: Pin, Hotglue, Opsin, The Kiln. They stay out of 298. Freeze 3 is a documented addendum, not a second independent coding pair. Role-lane kappa is not recomputed.

**Freeze 4.** A Claude care package dropped 2026-08-30 is a sidecar under `package/`. It is a different assembly. It is not this freeze's census. Treatments that would add, merge, or remove an `application_id` remain held. A subject-confirmed overlay in `coding/confirmed/` records recall tagged `evidence_system = memory`. Overlay rows are not copied into the 298. The 14 cannot move by accident: `adjudication/derive_metrics.py` reads `cursor`, `alpha`, and `bravo` only.

## Harvest

Queries are recorded in `QUERY-MANIFEST.md`. A Gmail query is done only when the API returns no further page token.

I searched receipt language, ATS domains, aggregator channels, rejection language without the word application, sent mail, interview and scheduling language, and (on 33@lecturesfrom.com) offer language including spam and trash. Q1 through Q9 are exhausted on both mailboxes. Q11 offer language is closed on 33@lecturesfrom.com and was not run on keeganmoody33@gmail.com this pass. Personal Q9 is receipt language, not offer language. Unharvested is not empty.

Committed artifacts store hashed evidence pointers: `gth_` for Gmail threads, `cal_` for calendar events, `tok_` for tokens, `eml_` for third-party addresses. Study mailbox labels stay so retrieval scope remains auditable. Published copy does not include raw or hashed provider IDs.

Ladders full list is absent. YC Work at a Startup dashboard is absent. Prior-audit workbooks labeled [S1] and [S2] are absent. Talentpluto and Jobgether receipts exist; underlying employers are still unnamed. Those stops bound the census. They are not silent omissions.

## Coding and adjudication

The codebook (`knowledge/03-codebook.md`, rev 1) is the logging schema. Changes to it would invalidate prior rows. This tree did not apply package codebook rev 2 (`converted_to_contract`, `no_response` anchoring, community source split).

Table 1 is applications. Table 2 is events. `interviewed` is not a field. It is derived: at least one event whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}. A stored rollup and a stored event list will eventually disagree. I compute the rollup.

Every date carries a precision label. Monthly series use only `date_precision = exact`. Relative LinkedIn stamps are not upgraded to calendar dates. Evidence-bound dates are not plotted as if they were exact.

Evidence class is `employer_artifact` or `platform_log`. That split is the sensitivity stratum.

Role lane is one mutually exclusive category. Cohen's kappa on the Freeze 1 intersection (n = 211 matched keys) is 0.9510. Include/exclude percent agreement is 0.9905. Include kappa is 0.7452. The two include disagreements were The Hog and BX Studio. Both stay opportunity.

Freeze 2 and Freeze 3 are documented column mappings of structured files and new artifacts onto the existing census. They are not a second independent LLM pair. Kappa is not recomputed on the 77.

## Completeness

Ninety-five percent completeness is a goal, not a verified claim. The intended estimator is stratified two-source capture recapture, restricted to LinkedIn rows submitted through an external ATS, because only there could both LinkedIn and employer mail have observed the same application.

That overlap stratum is unmeasured. The Freeze 2 LinkedIn file does not label Easy Apply versus external ATS. Naive Lincoln-Petersen on Easy Apply versus ATS mail is invalid: those sources are near-disjoint by construction. Easy Apply is visible to LinkedIn and invisible to ATS mail. An unstratified estimator would inflate uniqueness and understate completeness. I did not run it. I do not print a completeness percentage.

## Offers

A zero is a positive claim. It requires a search for offers, not the absence of offers in a ledger. Freeze 1 and Freeze 2 code no `offer_accepted` or `offer_declined` on census rows. Q11 on 33@lecturesfrom.com, including trash, found no employment offer letter. The personal mailbox offer-language family is still open. The Mercor Instant Work Offer is opportunity. It states I did not apply directly.

## Overlay

If I say a conversation happened, it is logged. Recall is tagged memory so a skeptic can drop it. Happened is not the same as `register = application`. Mixmax, the Mercor contract path, Pin, The Hog, Glytec, Opsin, Hotglue, The Kiln, Adam (Stellar Growth), and Doug (Renoir, meeting 2025-10-27, before AICRO) stay out of 298. Frozen `discovery_source` is not recoded to GTM Cafe. That value is not in this codebook.

## What Results is licensed to use

From this methods section, Results may print: 298 applications; 273 companies on those applications; 14 interviewed applications; 14/298, 14/221, and 14/220; 0 coded offers from the 298; Freeze 1 closes on 221; role-lane counts on 221 with kappa; role-lane counts on 298 as a documented mapping without a second kappa; exact-date monthly series with the not-exact count beside the chart; money listed beside the rate, not inside it. Results may not print a completeness percent, a reply percent over 298, a combined conversation count as a rate, or the retired prior-audit figures as this freeze's finding.

## Limitations, in the body

I coded my own search. Model pairs are independent of each other, not of me. Freeze 2 LinkedIn is pages 1 to 10. Freeze 3 skipped two hidden calendars. Offer-language is unclosed on the personal mailbox. Ladders, YC, and the prior workbooks are missing. Twelve LinkedIn rows and AnyInt AI are held, not minted. `work_type = Atlanta` on three rows is a vocabulary error and is not interpreted.

<!-- claims
| # | quantity as written | value | source | tier |
|---|---|---|---|---|
| 1 | window | 2025-06-01 through 2026-08-29, America/New_York | knowledge/00-core.md, QUERY-MANIFEST.md | measured |
| 2 | Freeze 1 applications | 221 | adjudication/applications__adjudicated.csv | measured |
| 3 | Freeze 2 net-new platform_log | 77 | adjudication/FREEZE-2.md | measured |
| 4 | Full application census | 298 | adjudication/applications__full_census.csv | measured |
| 5 | role_lane kappa | 0.9510 | adjudication/PRE-ADJUDICATION.md | measured |
| 6 | include kappa | 0.7452 | adjudication/PRE-ADJUDICATION.md | measured |
| 7 | personal calendar events swept | 338 | paper/RESULTS.md Freeze 3, logs/retrieval-log-032.md family | measured |
| 8 | completeness percent | not computed | paper/DEFECTS.md | unknown |
| 9 | Q11 mailbox | 33@lecturesfrom.com closed; keeganmoody33 open | logs/retrieval-log-059.md, QUERY-MANIFEST.md | measured |
-->
