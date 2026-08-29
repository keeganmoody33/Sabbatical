# Alpha coding notes

## Artefact counts

- Gmail logs processed: 001–029 (994 threads claimed on keeganmoody33 in 001–021; 177 additional on 33@lecturesfrom in 022–028; identity check 029).
- Calendar: q8-lecturesfrom-primary.csv (31 events across five 90-day blocks) and q8-transferred-empty.md (0 events).
- Platform: KEEGAN-EXPORTS-ABSENT.md and STOP-CONDITIONS.md (LinkedIn/Jobright/Ladders/YC/xlsx waived).
- Rows emitted: applications 230 (register=application 216, register=opportunity 14), events 409, exclusions 358.
- Unique evidence_ids consumed on application/event rows: 409.

Retriever notes in the logs were not coded as facts. Only subject, sender, date, thread_id, and quoted parenthetical snippets in the tables were used.

## Judgement calls

- Fullsteam, Drata, Vonage, Built Recruiting, Hyperbound, OpenObserve, Gradient Labs, Meshy, Lumenalta, Jobright.ai PM, and DeKalb position-filled notices: coded as applications with date_precision=evidence_bound because the artifact uses application language or a filled-notice that names a position applied for, without a first receipt. Not upgraded to exact.
- Weave 2025 Greenhouse receipt merged with weave.bio BDM decline. 2026-08-18 Ashby post-interview decline has no 2026 submission; excluded as unresolvable_identity rather than cycle 2.
- PandaDoc: Greenhouse security code plus no-reply@pandadoc.com We got it plus later GTM Engineer decline. Treated as a completed application.
- Huzzle: Workable submitted-successfully receipt wins over talent-pool phrasing on huzzle.app. register=application.
- Talentpluto: one Workable thread with two submitted-successfully titles (Go-to-Market Engineer and GTM Engineer). One artifact so one application; underlying_employer=unknown. Chase mails about an incomplete AI-agent call do not override Workable submitted.
- Jobgether: application with underlying_employer=unknown.
- WorkOS/TopHire: opportunity (recruiter path, no submission).
- Mercor: Application Submitted receipts are application register per role; Claire Gauthier GTM Engineer contract is opportunity; Growth Strategist instant offer is opportunity; Furniture Shopper pause is opportunity.
- PhrasIQ: Wellfound acceptance is the submission parent (role unspecified, not inferred as GTME). Calendar Discovery is hiring_manager_interview round 1.
- Anysphere canonical for Cursor Ashby mail.
- DISQO spelling from the Lever subject.
- Owner.com: subject GTM Engineer kept; body Product Builder, GTM Product recorded as conflict.
- Productboard: Associate GTM Engineer (07-15) kept over GTM Engineer (07-13); conflict noted.
- Trase Healthcare in the decline used for role_as_listed and gtm_modifier=ai_product_vertical (vertical in title). Debatable; recorded.
- Anduril 07-15 untitled decline merged into 06-21 Technical Operations Engineer rather than inventing a second Anduril title.
- Nebius untitled 05-21 receipt merged into later Director GTM Physical AI decline.
- FOSSA, Attentive, Pindrop: second receipt after a dated terminal is a new cycle.
- Pogo Gem/Ashby receipts without a terminal merged as one cycle.
- Unframe 04-06 and 04-17 merged (no terminal between).
- Apply4Me Lattice and Firstup paired with same-minute employer ATS receipts; evidence_class=employer_artifact. AI Digital Apply4Me-only is platform_log.
- Atlanta Public Schools: AppliTrack confirmation and APS not-accepting-substitutes both stored; terminal role_paused_or_closed on 2026-06-22.
- DeKalb general expiry/start = attempted_not_submitted. Ten distinct school/role filled notices = ten applications. Chapel Hill 07-14 and 08-04 merged as one school+title.
- Mixmax product onboarding excluded (consulting_prospect / not employment).
- Jorge Macias / gtm-engineering.io calendar and mail excluded as consulting_prospect (no submission).
- Inertia Growth: sent subject GTME role kept; decline names Outbound Campaign Manager; conflict not overwritten.
- brand.ai: role_as_listed=GTME from sent subject, not expanded to GTM Engineer.
- TestGorilla: no classic thank-you; assessment invitation plus recruiter intro coded as application with medium confidence.
- BrightHire: thank you for your interest coded as weak submission (tier B).
- Graph.one founder cannot see an application: attempted_not_submitted.
- SBGA thread starts 2025-04-11: out_of_window.
- Gwinnett: started + expiry only: attempted_not_submitted.
- getcrate.app OpenAI/Google: unresolvable_identity (sender is not the employer).
- Dover beehiiv Leidos and Software Engineering Manager Banking: recruiter_initiated newsletter, not applications.
- Logs 012 remainder, 014 ZipRecruiter alerts without thread IDs, 028 pages 1–2 without enumerated IDs: cannot be coded as rows; noted as coverage holes rather than invented IDs.
- One-artifact-one-event: after emit, events were deduplicated on evidence_id (Bluejay call was the known collision). Combined receipt-then-rejection threads stored as rejection or as the listed type with notes.
- salary_range_listed=not_stated everywhere (never observed). work_type=unstated unless Remote/Atlanta-style tokens appeared in the listed title.
- Calendar PhrasIQ is the only calendar event attached to an application. Other calendar rows are exclusions.
- 33@lecturesfrom.com ATS harvest is empty of employment receipts (logs 023–026). Product mail on that account is exclusions.

## Conflicts between artifacts

1. Owner.com subject GTM Engineer vs body Product Builder, GTM Product (gth_42e02c48ed5bf0d4). Used subject.
2. Productboard GTM Engineer (gth_fa753c8961d636b5) vs Associate GTM Engineer (gth_36e64a008a81fd84). Used Associate.
3. Inertia Growth sent GTME role vs decline Outbound Campaign Manager Role. Used sent title.
4. Talentpluto Workable submitted vs Pluto incomplete-process chases. Used Workable submitted.
5. Huzzle Workable submitted vs huzzle.app talent-pool language. Used Workable submitted.
6. Mercor 2026-06-30 You signed up but haven't applied vs 2026-06-22 Application Submitted receipts. Receipts win; 06-30 mail is exclusion.
7. Atlanta Public Schools AppliTrack confirmation vs APS not accepting substitutes. Both stored.
8. Beckhoff not fully completed (08-07) vs declined thank-you-for-applying (08-08). Treated as completed then rejected.
9. Weave 2025 BDM decline vs 2026 interview decline. Cycle 1 terminal in 2025; 2026 has no submission.
10. Anduril titled 06-21 vs untitled 07-15 decline. Merged as one cycle.
11. Manifold vs Manifold AI on same-day receipt and decline. Company kept as Manifold from the receipt.

## Vocabulary wanted and not used

- AppliTrack / Frontline / Paycom / Newton / Hirebridge / Ceipal / Spark Hire as ats_system values. Coded none_observed.
- consulting or vendor_demo as exclusion_reason for product demos; used consulting_prospect.
- newsletters as exclusion_reason; used unresolvable_identity.
