# notes__bravo.md

Coder: bravo

Did not consult another coder. Did not read any file under `/workspace/coding/` except `README-coder.md`. After writing these rows, `git status` listed `coding/alpha/` as untracked; those files were not opened.

## Artifacts processed

- `/workspace/artifacts/gmail/retrieval-log-001.md` through `021.md` (keeganmoody33@gmail.com harvest). Coded every application-relevant thread.
- `/workspace/artifacts/gmail/retrieval-log-022.md` through `029.md` treated as a second mailbox (`33@lecturesfrom.com`). Exhausted queries on that mailbox produced no employer ATS receipts and no additional employment applications. Jobright traffic on that mailbox is account signup plus job alerts. Alibaba Pay Later and Kimi Code Beta are not employment.
- `/workspace/artifacts/calendar/q8-lecturesfrom-primary.csv`
- `/workspace/artifacts/calendar/q8-transferred-empty.md` (zero events)

Newsletters (Substack, Search Engine Land, ByteByteGo, YC essays, GrantWatch, The Pipeline, The Neuron, and similar) were seen and omitted as non-candidates. Credit-card, affiliate, Coursera, Studyportals, Gusto benefits, Apple Card, Upstart, ZapConnect speaker, and product-SaaS lifecycle mail (Vercel, Airtable, Cloudflare product, Beautiful.ai billing on lecturesfrom) were omitted the same way. YC Work at a Startup "still looking / profile no longer shared" repeats were collapsed to one marketplace_profile exclusion rather than one row per reminder.

Retriever notes in the logs were not treated as facts. Coding used subject, sender, date, snippet, thread_id, and the calendar CSV columns.

## Rows emitted

- applications: 228
- events: 414
- exclusions: 44

These are table row counts, not a census headline.

## Judgement calls

- FOSSA receipts omit the role; both cycles are `role_as_listed=unspecified` rather than an inferred GTM title.
- PhrasIQ Wellfound acceptance omits the role; `unspecified`. Calendar `Discovery | Keegan Moody<>PhrasIQ` on 2026-04-02 is parented as `hiring_manager_interview` round 1. Counterparty name is not on that calendar row so `unknown`. Medium is empty; video was not observed.
- Attentive c1 receipt omits the role; c2 names GTM Engineer after a terminal. Treated as cycle 2 of the same company process rather than an unrelated title.
- Pindrop c2 after the 2025-05-27 specialist decline omits the role; new cycle with `unspecified` rather than copying the prior title.
- Auctane 2026-04-10 receipt omits the role; 2026-05-14 decline names Pre-Sales Engineer. Merged as one cycle with the named title.
- Toast, Nebius, Virtru, GTP Software, Sage, Anaconda update, Weave 2025, Anduril decline: later named title applied back to an earlier untitled receipt at the same company when no second titled req was visible.
- Owner.com subject is GTM Engineer; body names Product Builder, GTM Product. Subject used; conflict in notes.
- Inertia Growth send says GTME; employer decline names Outbound Campaign Manager. Employer title used.
- HartleyCo 07-13 says GTM Engineer; 07-23 names Founding GTM at Bluejay. Decline title and Bluejay as company; HartleyCo as `underlying_employer`.
- Talentpluto Workable copies for Go-to-Market Engineer and GTM Engineer three minutes apart treated as one role. Follow-ups say the AI-agent call was incomplete; Workable "submitted successfully" includes the row.
- Huzzle Workable says GTM Engineer submitted successfully; Huzzle emails say talent pool. Included from Workable submission language.
- Unframe receipts 04-06 and 04-17 with no terminal between them: one cycle.
- Pogo Gem 06-04, Gem 06-26, Ashby 07-08: one cycle, no terminal between receipts.
- Hightouch 07-15 and 07-22 receipts then 07-24 decline: one cycle.
- Together AI 07-13 and 07-15: one cycle.
- Trase 04-27 and 06-26 receipts then 07-10 Healthcare decline: one cycle.
- Mento 03-24 and 03-30: one cycle.
- Fixify 04-03 and 04-06: one cycle.
- Tapcheck 03-30 and 04-06: one cycle.
- Crypto.com 2025-08-05 receipt and 2025-11-02 thank-you/declined thread: one cycle.
- Beckhoff "not fully completed" on 08-07 then 08-08 rejection thanking him for applying: completed, not attempted.
- PandaDoc Greenhouse security code plus `no-reply@pandadoc.com` We got it plus 04-27 GTM Engineer decline: completed application, no interview artifact so `rejected_no_interview`.
- DeKalb general AppliTrack started plus expiry warning: attempted. Ten STAR Substitute filled notices: separate position-level applications, dates evidence-bound to the filled notice. Chapel Hill 07-14 and 08-04 merged.
- Frontline "Stellar Substitute position filled" does not name a district; parented to Atlanta Public Schools because the APS sent thread is the Frontline relationship in this corpus.
- APS AppliTrack submission confirmation and APS reply that they are not accepting substitutes both kept; terminal `role_paused_or_closed`.
- WilsonHCG thank-you-for-applying counts; client unnamed so `underlying_employer=unknown`. Dexian later outreach on the same title not merged.
- Crossing Hurdles / Montauk Capital: company Montauk Capital, underlying Crossing Hurdles.
- Jobgether: company Jobgether, underlying unknown.
- Mercor six "Application Submitted" rows are census applications (`register=application`, `platform_log`). Recruiter-sourced GTM Engineer contract (Claire Gauthier, offer accepted) is a separate opportunity row. Instant Work Offer Growth Strategist ("didn't apply directly") kept on that opportunity row.
- The Hog: interview and take-home, no submission_receipt; `register=opportunity`.
- WorkOS via TopHire: recruiter slot booked, no submission; `register=opportunity`.
- Pinterest June 2025 accepted referrals: opportunity, no submission_receipt. March 2026 Apprentice Engineer Greenhouse receipt is a separate application.
- ThriveLink: referral intro, no ATS receipt; opportunity.
- micro1 AI Training Pilot: interview plus profile submitted to unnamed client; opportunity. Finance Expert and community-pool mails excluded.
- Apply4Me Firstup and Lattice have matching employer receipts the same minute: `evidence_class=employer_artifact`. AI Digital Apply4Me has only the agent send plus employer decline: `platform_log`.
- ZipRecruiter Revic "application is complete": included, `submission_channel=unknown` (ZipRecruiter not in the vocabulary).
- Gradient Labs: ZipRecruiter asked to complete; Ashby later "update on your application" declined. Included from the Ashby application-update language, date evidence-bound.
- Built Recruiting, Hyperbound, OpenObserve, Vonage, Jobright PM, Fullsteam, ClassDojo, Drata: no discrete thank-you receipt; included from ATS/employer application-update language with `evidence_bound`.
- Classet Wellfound "update / declined" has no submission_receipt: exclusion `unresolvable_identity`, not an application row.
- Weave 2026-08-18 post-interview decline is a year after the 2025-07-31 BDM terminal and has no 2026 receipt: exclusion, not a new cycle.
- Switchyards Digital Product Builder 2026-04-25 decline has no submission_receipt: exclusion. Launch Manager 2025-08 is a separate application.
- Meshy 2025-06-01 "will not be proceeding with your interview process": no submission_receipt; exclusion.
- jobmail.io Growth Lead: unnamed stealth company; exclusion despite an application-received message.
- 2026-07-12 Greenhouse "Thank you for applying (GTM Engineer)" with employer not named: exclusion.
- Leidos / Dover beehiiv and Dover "Software Engineering Manager, Banking" / Rippling subject: sender unverified, no matching employer receipt; exclusion.
- getcrate.app OpenAI / Google / Crate: sender does not match the claimed employer; exclusion.
- Gong, Spot AI, Celonis, New Relic: GDPR/retention only; exclusion.
- Gwinnett and DeKalb general: started plus expiry, no submission confirmation; attempted.
- Douglas County, Decatur, APS: started plus submission confirmation; included.
- Common Room ChiliPiper and Jorge Macias / gtm-engineering.io 30 Minute Meeting [GTME]: job-like meetings with no parent application; exclusion. Not coded as applications from calendar/interview alone.
- Glytec interview logistics without a receipt: exclusion.
- BX Studio video-to-hiring-manager send: included as `email_direct` with low confidence.
- Foursquare 2026-01-08 "Update on your application" does not say declined; left `still_open`.
- Pearl interview dates taken from reminder subjects (May 5 phone, May 17 Zoom), not from a calendar of the personal mailbox.
- Dagster 2026-04-03 post-chat decline: interview event dated to the follow-up because the chat date is not stated.
- Orchestry: two Breezy video-screen invites, missed-interview note, later decline after process.
- Hologram: Preliminary Screening Call Amy Schwartz 07-20 as round 1; Cross-Functional Interview Derrick Calderon 07-22 as round 2 `panel`.
- RevSpring LinkedIn recruiter 05-29 precedes the 06-04 Newton receipt so `discovery_source=recruiter_inbound` with `register=application`.
- Anysphere canonical for Cursor, alias in notes, per codebook.
- DISQO spelled as listed on the Lever receipt.
- School-district roles coded `role_lane=other`.
- `salary_range_listed=not_stated` on every row; no comp figures appear in the coded subjects/snippets.
- Calendar events that are product demos, office hours, haircuts, rap battles, vendor onboarding, or community connects were not coded as job events.

## Conflicts between artifacts

- Owner.com: subject GTM Engineer vs body Product Builder, GTM Product. Subject used.
- Inertia Growth: candidate send GTME vs employer Outbound Campaign Manager. Employer used.
- HartleyCo GTM Engineer vs Bluejay Founding GTM. Decline used; employer Bluejay.
- Huzzle: Workable GTM Engineer submitted vs Huzzle talent-pool language. Included from Workable.
- Talentpluto: Workable submitted successfully vs Pluto "process incomplete" / "about to be closed". Included from Workable; incomplete-call chase logged as `employer_ack`.
- Mercor: 2026-06-22 Application Submitted receipts vs 2026-06-30 "signed up but haven't applied to a project yet". Receipts coded as applications; the 06-30 mail is a marketplace_profile exclusion with the conflict noted.
- Mercor Instant Work Offer "didn't apply directly" is true of that offer and does not override the six Application Submitted mails.
- APS: AppliTrack submission confirmation vs district reply not accepting substitutes. Both kept.
- Crypto.com 08-05 title "Product Growth Hacker: Exchange & Main App" vs 11-02 "Product Growth Hacker, Exchange". Merged.
- Productboard GTM Engineer 07-13 vs Associate GTM Engineer 07-15 kept as two rows (materially different titles).
- TRACTIAN Senior GTM Engineer Hubspot vs Sales Engineer Automation: two rows.
- Galileo Growth Engineer vs GTM Engineer: two rows.
- Ambrook Partnerships Lead vs Business Operations Lead: two rows.
- SentiLink Feb unspecified vs June Go-to-Market Strategy Analyst: two rows because the Feb receipt omits the title.
- Two Pinterest June referrals vs 2026-03-25 Apprentice Engineer: three rows, two opportunity, one application.

## Missing vocabulary

Wanted more than twice, not invented:

- `ats_system`: AppliTrack/Frontline, Paycom, Newton, Ceipal, HireBridge, Spark Hire, applicant-tracking.com
- `submission_channel`: ZipRecruiter
- `event_type`: interview invitation (scheduled, not yet occurred); ATS security-code / email-verify step
- `medium`: unknown / unstated
- `discovery_source`: ZipRecruiter, Jobgether, Mercor, HireBridge

## Second mailbox (022-029)

No additional application, event, or exclusion rows beyond what 001-021 plus calendar already support, except the Jobright lecturesfrom signup marketplace_profile exclusion (Welcome to Jobright / Turbo on 33@lecturesfrom.com) and the Jorge Macias meeting which also appears on the lecturesfrom calendar and Gmail.
