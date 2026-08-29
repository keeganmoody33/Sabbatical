# Coder alpha notes

## Artifacts processed

- Gmail retrieval logs 001 through 029 under `/workspace/artifacts/gmail/` (personal ATS harvest 001–021; lecturesfrom.com mailbox 022–028; account-identity check 029).
- Calendar exports: `/workspace/artifacts/calendar/q8-lecturesfrom-primary.csv` and `q8-transferred-empty.md`.
- Codebook sources used: `/workspace/codebook.md`, `/workspace/prompts/extraction.md`, `/workspace/coding/README-coder.md`, counting rules and evidence tiers in `/workspace/knowledge/00-core.md`, `/workspace/knowledge/03-codebook.md`.
- Retriever commentary in the logs was not treated as fact. Coding used subject, sender, date, snippet, and thread_id.

## Rows emitted per table

- applications__alpha.csv: 232
- events__alpha.csv: 397
- exclusions__alpha.csv: 56

Newsletters (Substack, beehiiv product news, Search Engine Land, ByteByteGo, YC editorial, Anthropic “New Jobs” Greenhouse-jobs alerts, ZipRecruiter job alerts, GrantWatch, and similar) were seen across logs 001–028 and omitted as non-candidates. They do not have exclusion rows.

## Judgement calls

- Role omitted from a thank-you or receipt was recorded as `unspecified`; titles were never inferred from the company’s usual openings.
- `gtm_modifier` was filled only when `role_lane = explicit_gtm_engineering`.
- ATS mail with an ISO date and explicit application language got `date_precision = exact`. Updates, declines-only, and “opening filled” messages without a first receipt got `evidence_bound` with `date_evidence_anchor` equal to that artifact date.
- Wellfound “successfully submitted” receipts without a matching employer ATS row were `evidence_class = platform_log`. A later employer message (Ava Labs) promoted that row to `employer_artifact`.
- Apply4Me “Application Sent” plus a same-minute employer ATS receipt (Firstup, Lattice) was coded as one application, `submission_channel = apply4me_agent`, `evidence_class = employer_artifact`.
- Apply4Me-only AI Digital was kept as an application because the Ladders agent stated the application was sent, then the employer declined.
- ZipRecruiter “application is complete” (Revic) is a platform confirmation; `submission_channel = unknown` because ZipRecruiter is not in the channel vocabulary.
- Mercor six titled “Application Submitted” receipts were coded as applications (`register = application`). Claire Gauthier / Daniel Luo / hourly GTM Engineer contract was coded `register = opportunity` because Instant Work Offer states he did not apply directly. Atlanta Furniture Shopper Study pause is a separate opportunity row.
- Huzzle: Workable “submitted successfully” plus application-data copy was treated as a titled submission, not a talent-pool exclusion. Huzzle’s own “talent pool” interview mail was coded as `assessment_sent` on that application.
- Talentpluto: two Workable successful submissions three minutes apart (Go-to-Market Engineer and GTM Engineer) were two applications. Later Pluto chase mail that the AI-agent call was incomplete was not treated as unsubmission.
- PandaDoc Greenhouse security-code plus same-day `no-reply@pandadoc.com` “We got it” plus 2026-04-27 decline: completed application, not attempted.
- Beacon Software, Hologram, Axiad, Hightouch, Together AI, Dagster Labs security-codes followed by completed receipts: routine step, not attempted.
- Beckhoff: Paycom “not fully completed” then 2025-08-08 “thanks for applying” decline: coded as submitted then `rejected_no_interview`, not `attempted_not_submitted`.
- Atlanta Public Schools: AppliTrack submission confirmation stands; APS reply that they were not accepting substitutes is `role_paused_or_closed`. Both facts kept.
- DeKalb general AppliTrack start plus expiry warning: one `attempted_not_submitted` exclusion. Ten distinct STAR Substitute “position you applied for has been filled” notices: ten applications, `role_paused_or_closed`. Chapel Hill ES 2026-07-14 and 2026-08-04 notices merged as one title.
- Gwinnett start plus expiry warning: `attempted_not_submitted`. Douglas County and City Schools of Decatur have submission confirmations: applications.
- FOSSA and Attentive: second Greenhouse thank-you after an explicit prior-cycle decline licensed `c2`.
- Pindrop 2026-06-22 thank-you after 2026-05-27 decline licensed `c2` with `role_as_listed = unspecified` because the second receipt omitted the title.
- Unframe 2026-04-06 and 2026-04-17 receipts with one 2026-05-12 decline: one cycle (no terminal between receipts).
- Pogo Gem 2026-06-04, Gem 2026-06-26, Ashby 2026-07-08, same title, no terminal: one cycle.
- Hightouch two “Application Received” then one Go-to-Market Engineer decline: one cycle.
- Together AI 2026-07-13 and 2026-07-15: one cycle.
- Trase 2026-04-27 and 2026-06-26 thank-yous then 2026-07-10 Healthcare GTM decline: one cycle; role taken from the decline.
- Cursor listed name kept in `company_as_listed`; `company_canonical = Anysphere`.
- DISQO kept as DISQO.
- WorkOS/TopHire: named remote GTM Engineer, recruiter slot booked, no ATS receipt: `register = opportunity`, `discovery_source = recruiter_inbound`. TopHire is recruiter, not `underlying_employer`.
- PhrasIQ Wellfound accepted notice omits role: `role_as_listed = unspecified`. Calendar Discovery 2026-04-02 is round 1. Relay “GTM System Deep Dive” was not confirmed on calendar, so no round-2 event.
- The Hog: `hudson@thehog.ai` GTM Interview plus take-home is `register = opportunity` (no submission receipt). `hudson@notifications.thehog.ai` Welcome to The Hog is a product-welcome exclusion, not the interview.
- Jorge Macias / gtm-engineering.io 30 Minute Meeting [GTME] and calendar row: `consulting_prospect` exclusion (no submission, purpose not stated as a job loop).
- Kivira.health JP/KM connects with joshpap22: `consulting_prospect`.
- Mixmax welcome (including SENT) is product, not employment. Morphin / Morph Data Strategies calendar meetings with Daniel Hill: `consulting_prospect`.
- ThriveLink Healthcare BD Rep via Josh Pappas: `register = opportunity`, `discovery_source = referral`.
- Pinterest June 2025 referral-accept messages: `register = opportunity`. 2026-03-25 Apprentice Engineer Greenhouse receipt is a separate application.
- WilsonHCG “thank you for your application” for Outbound Sales Consultant III: census application, `recruiter_submitted`, client unnamed. Dexian later outreach on the same title: separate `recruiter_initiated` exclusion.
- Crossing Hurdles / Montauk Capital Ceipal mail: recruiter notice, not a submission receipt.
- jobmail.io Growth Lead for a stealth company: `unresolvable_identity` even though there is a receipt, because the employer is unnamed.
- 2026-07-12 Greenhouse thank-you that names GTM Engineer but not the employer: `unresolvable_identity`.
- Meshy 2025-06-01 “will not be proceeding with your interview process”: rejection/interview language only, no receipt: `unresolvable_identity`.
- Weave 2026-08-18 post-interview decline: no 2026 submission artifact; 2025 BDM cycle already terminal: `unresolvable_identity`, not a second cycle.
- Switchyards Digital Product Builder 2026-04-25 decline: no submission artifact: `unresolvable_identity`. Launch Manager 2025 remains an email_direct application.
- GDPR/retention-only (Gong, Spot AI, New Relic, Celonis): `unresolvable_identity`.
- Dover beehiiv Leidos interview series and Rippling “Software Engineering Manager, Banking” invites: unverified sender, no submission: `unresolvable_identity`.
- getcrate.app OpenAI/Google/Crate claims: sender is not the named employer: `unresolvable_identity`.
- SBGA thread starts 2025-04-11: `out_of_window`.
- YC Work at a Startup profile sharing / “still looking”: one `marketplace_profile` exclusion (not every reminder).
- School-district STAR/substitute roles used `role_lane = other`.
- Owner.com subject GTM Engineer vs body Product Builder, GTM Product: body used as `role_as_listed`.
- Inertia Growth sent subject “GTME role” vs employer decline “Outbound Campaign Manager”: decline title used as listed.
- Classet Wellfound update is a decline without a separate successfully-submitted receipt: kept as an application with `evidence_bound` and `platform_log`.
- BrightHire “thank you for your interest”: kept as a low-confidence application, not dropped.
- Hirebridge “Profile submitted to Tripleseat for GTM Engineer #611301”: titled req, kept as application with `platform_log`.
- IBM Ref 119353 Manager, Applied AI & GTM Systems for Confluent: `company_canonical = Confluent`.
- HartleyCo Josh Kelly process later names Bluejay Founding GTM: `company_canonical = Bluejay`; HartleyCo is recruiter.
- Valsoft Workable subject names DockMaster: `underlying_employer = DockMaster`.
- Graph.one founder cannot see an application: `attempted_not_submitted`.
- Calendar haircuts, rap battles, self-run office hours, ApolloNEXT conference, State of GTME Launch, and similar non-employment blocks were not coded as applications or exclusions.
- Lecturesfrom.com mailbox ATS queries returned zero employment receipts; Hog product welcome vs interview distinction is logged as above.
- Transferred keegan@lecturesfrom.com calendar had zero events in the window.
- `still_open` used when no terminal artifact exists. `no_response` was not inferred from silence.
- Duplicate-in-source receipts (Apollo.io 62s, 10x Genomics 14s, Applied Systems three iCIMS messages, RevSpring Newton duplicate, Crossing Hurdles identical pair) were merged at the application level; extra messages became events or notes with both evidence IDs.
- Round numbers assigned only to interview-class event types, in observed order, not from memory of an Interviews sheet.
- Medium left empty when the artifact did not state video/phone/onsite/async/email. Invalid filler values were not written.
- Counterparty names taken only from the artifact (Eddie was not copied from the codebook PhrasIQ worked example).

## Conflicts between artifacts

- Owner.com: subject “GTM Engineer” vs body “Product Builder, GTM Product”. Used body. Evidence `19f8aa5a9dee405a`.
- Inertia Growth: sent “GTME role” (`19844e86afa37157`) vs decline “Outbound Campaign Manager” (`1985d0a9011176a8`). Used decline title.
- Mercor contract: Instant Work Offer “Growth Strategist” (`1a021442493bec48`) vs Offer Acceptance “GTM Engineer” (`1a025862aa01f0dc`). Used offer-acceptance title.
- Mercor timeline: onboarding/phone verification and two evaluator submissions 2026-06-22 vs 2026-06-30 “signed up but haven’t applied” vs 2026-07-20 Victor Ekuta referral. All three dated artifacts kept; referral does not erase the 06-22 submissions.
- Talentpluto: Workable “submitted successfully” (`19f5862ce3bd83b7`) vs Pluto chase “process incomplete” (07-12 through 07-22). Coded as submitted; incomplete refers to a later call.
- Huzzle: Workable GTM Engineer submitted (`19e9214f255608aa`) vs Huzzle “applying to join our talent pool” (`19e92180ca58bd3a`). Coded as application.
- Atlanta Public Schools: AppliTrack “submission confirmed” (`19ee1ef014efde21`) vs APS “not currently accepting substitute applications” (`19edf97699db02b8`). Both kept; terminal `role_paused_or_closed`.
- Beckhoff: Paycom “not fully completed” (`1988608ae766bb44`) vs next-day thanks-for-applying decline (`1988bb3318ed28b3`). Coded as submitted then rejected.
- Crypto.com 2025-08-05 “Product Growth Hacker: Exchange & Main App” (`1987abec68c6f639`) vs 2025-11-02 “Product Growth Hacker, Exchange” declined (`19a45779c86938f1`). Different listed titles and threads; two applications, both cycle 1.
- SentiLink 2026-02-23 unspecified thank-you vs 2026-06-22 thank-you plus 2026-07-13 Go-to-Market Strategy Analyst decline: two applications (titles differ).
- Productboard 2026-07-13 GTM Engineer vs 2026-07-15 Associate GTM Engineer: two applications.
- TRACTIAN Sales Engineer, Automation vs Senior GTM Engineer, Hubspot: two applications.
- Galileo Growth Engineer 2025-07-02 vs GTM Engineer 2025-07-28: two applications.
- Ambrook Partnerships Lead 2025-08-06 vs Business Operations Lead 2026-02-11: two applications.
- Switchyards Launch Manager 2025 vs Digital Product Builder 2026 decline-only: application plus exclusion.
- Weave 2025 BDM rejected vs 2026-08-18 interview decline without a 2026 receipt: application plus exclusion.
- The Hog interview (`hudson@thehog.ai`, `19ecda5fa25e0d35`) vs product welcome (`hudson@notifications.thehog.ai`, `19ed298800137744` / `19edfbeff6d01f38`): opportunity application vs product exclusion.
- Beautiful.ai employment loop on keeganmoody33 vs product billing on 33@lecturesfrom.com: only the employment loop is an application.
- Vercel GTM Engineer application vs Vercel payment/sign-in mail on the business mailbox: only the Greenhouse/Vercel recruiting thank-you is an application.
- Airtable GTM Engineer application vs Airtable workspace/trial mail on the business mailbox: same split.
- Cloudflare GTM Engineer application vs Cloudflare nameserver/product mail on the business mailbox: same split.
- Exa Labs Growth Lead Lever receipt vs June 2025 Exa product/API outreach: application vs consulting_prospect exclusion.
- PandaDoc: early retriever note that no receipt followed the security code is contradicted by `19d3f0236cb930e4` and `19dcf9174d4a446f`. Coded as completed then rejected.
- Jobright on 33@lecturesfrom.com (“Hi Logan” Turbo welcome plus alerts) vs Jobright.ai Product Manager (Early Career) update on the personal harvest: account/marketplace exclusion vs one application to Jobright as employer.

## Vocabulary terms wanted and not available

- `ziprecruiter` as a `submission_channel` (Revic complete-notice; Gradient Labs prompt).
- `hirebridge` / `applitrack` / `paycom` / `newton` / `ceipal` / `spark_hire` as `ats_system` values (mapped to `none_observed` except where a listed ATS domain was also present).
- `background_check` as an `event_type` (Certn on the Mercor contract was stored as `assessment_sent` / `assessment_completed`).
- `vendor_demo` / `product_signup` / `credit_product` as `exclusion_reason` (credit cards, Upstart, Alibaba Pay Later, Kimi beta, Mixmax welcome, The Hog product welcome used `unresolvable_identity` or `consulting_prospect`).
- `ats_security_code` as an `event_type` (noted on the application, not stored as events).
- `contract_paused` as a `terminal_outcome` (Mercor Furniture Shopper pause left as opportunity without overwriting the GTM Engineer `offer_accepted`).
