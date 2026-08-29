# Bravo coding notes

## Artefact counts

- Gmail unique thread_ids parsed from logs 001–029 tables: 734
- Calendar confirmed events with event_id: 32
- Applications rows: 231 (register=application 215; register=opportunity 16)
- Events rows: 404
- Exclusions rows: 362 (gmail 331; gcal 31)
- Duplicate application_ids renamed at assemble time: see judgement if any printed

Manifest listed 994 keeganmoody33 threads and 177 lecturesfrom threads with overlap across queries. Unique table-parsed thread_ids are 734. Retriever pages that omitted individual newsletter thread_ids (log 012 remainder; log 014 ZipRecruiter alerts listed by category; log 028 pages 1–2 sender mix) cannot be excluded row-by-row without IDs.

## Judgement calls

1. Retriever parentheticals such as (declined) and (first cycle) were not treated as subject-line facts. Terminal outcomes coded only when the subject clause itself states filled, no longer available, not currently accepting, offer acceptance, or a clearly separate rejection artifact is present. Many processes therefore have empty terminal_outcome.
2. Weave 2025-07-27 Greenhouse receipt merged with 2025-07-31 employer BDM message as one application. 2026-08-18 Ashby interview-decline has no 2026 submission artifact: exclusion unresolvable_identity, not a second cycle.
3. WorkOS/TopHire: recruiter path, no submission, register=opportunity.
4. Mercor coded per application: six marketplace submissions plus two recruiter/instant-offer opportunity rows. Referral from Victor Ekuta attached as event on the Cincinnatus collaborator submission.
5. Talentpluto Workable receipts say submitted (Go-to-Market Engineer and GTM Engineer). One application row; titles not materially different. Later Pluto-call incomplete messages are events, not un-submissions. Employer unnamed: company_canonical=unknown, underlying_employer=unknown.
6. Jobgether unnamed employer: company_canonical=unknown, still an application because next-steps language documents a job application.
7. Unnamed Greenhouse GTM Engineer 19f586b7fbc50265: company_canonical=unknown.
8. DeKalb general AppliTrack start/expiry: exclusion attempted_not_submitted. Ten named school STAR Substitute filled notices: distinct applications, date_precision=evidence_bound. Chapel Hill two notices merged.
9. Atlanta Public Schools AppliTrack confirmation counted; APS not-accepting-substitutes is a later event and terminal role_paused_or_closed. Role remains unspecified (substitute not used as invented title).
10. Gwinnett started plus expiry: exclusion attempted_not_submitted. Douglas County and City Schools of Decatur confirmations counted, roles unspecified.
11. Mixmax product onboarding excluded. PhrasIQ calendar Discovery is an interview event on the Wellfound-accepted parent (role unspecified).
12. The Hog interview and take-home have no submission artifact: register=opportunity so events have a parent.
13. PandaDoc: employer We got it plus later GTM Engineer rejection; Greenhouse security code is an event. Application counted.
14. FOSSA: 2026-04-22 receipt c1; 2026-05-20 interest message treated as terminal; 2026-05-21 receipt is c2.
15. Attentive: unspecified c1 2026-06-22, Thank You from Attentive 2026-07-07 as terminal, GTM Engineer c2 2026-07-15.
16. Pindrop: c1 2026-05-21 / specialist named on 05-27 update; c2 2026-06-22 after that terminal.
17. Unframe 04-06 and 04-17 receipts merged (no terminal between). Hightouch 07-15 and 07-22 merged then 07-24 decline. Together AI 07-13 and 07-15 merged. Pogo Gem/Ashby receipts merged.
18. Owner.com subject GTM Engineer vs body Product Builder, GTM Product: listed from subject, conflict in notes.
19. Cursor listed; company_canonical=Anysphere.
20. Inertia Growth sent as GTME role; employer later named Outbound Campaign Manager. Verbatim sent title kept.
21. Beckhoff: incomplete Paycom message plus later status update. Counted as application because Paycom treated a Sales Engineer application as existing. Paycom not in ats_system vocabulary: none_observed.
22. Galileo Growth Engineer (07-02) and GTM Engineer (07-28) are two applications.
23. Ambrook Partnerships Lead 2025-08-06 and Business Operations Lead 2026-02-11 are two applications.
24. Productboard GTM Engineer 07-13 and Associate GTM Engineer 07-15 are two applications.
25. TRACTIAN Senior GTM Engineer Hubspot and Sales Engineer Automation are two applications.
26. Switchyards Launch Manager 2025 counted (SENT thread). 2026 Digital Product Builder decline without receipt: exclusion.
27. Apply4Me Lattice and Firstup promoted to employer_artifact by matching ATS receipts. AI Digital remains application via agent sent plus employer decline.
28. ZipRecruiter Revic complete message counted (platform_log). Gradient Labs complete-your-application: exclusion attempted_not_submitted; later Ashby update without receipt: exclusion unresolvable_identity.
29. Built Recruiting, OpenObserve, Vonage, Classet, ClassDojo, Hyperbound, Meshy: rejection/update without submission receipt: exclusions.
30. Pinterest June 2025 referrals: opportunity. March 2026 Apprentice Engineer Greenhouse application is a separate row.
31. micro1 matching-platform items: opportunity, not census.
32. One artifact = one event: duplicate extra events sharing an evidence_id were dropped. Multi-message threads (brand.ai, Apollo identical receipts) stay one event with notes.
33. Fullsteam Workday update used as evidence_bound application (role named; no thank-you).
34. saveurdays.com thank-you with no named company/role: application company_canonical=unknown, role unspecified, confidence low.
35. WilsonHCG thank-you for applying counts; client unnamed.
36. HartleyCo first artifact unnamed client; later message names Bluejay Founding GTM. Merged to Bluejay.
37. Calendar meetings without job-process language (demos, office hours, personal, Jorge GTME connect, Stainless intro, Zentrik web form, Erin Xue/Firecrawl, Morph) excluded. PhrasIQ Discovery included as interview.
38. Wellfound successfully submitted: platform_log except Ava Labs which also has employer interest (employer_artifact).
39. Level and salary empty/not_stated unless observed in the listed title. Interviewed is not stored.
40. Lecturesfrom logs 022–029 are almost entirely product mail and Jobright alerts; coded as exclusions. No ATS receipts on that mailbox.

## Conflicts between artifacts

1. Owner.com: subject GTM Engineer vs body Product Builder, GTM Product.
2. Inertia Growth: sent GTME role vs employer Outbound Campaign Manager.
3. Talentpluto: Workable submitted vs Pluto process incomplete.
4. Huzzle: Workable GTM Engineer submitted vs talent-pool language.
5. Mercor: 2026-06-30 mail says signed up but has not applied, contradicting 2026-06-22 submission receipts. Coded the receipts; marketing contradiction noted.
6. APS: AppliTrack submission confirmation vs district not accepting substitutes. Both kept.
7. Sage receipt omits role; later update names Director of Growth, Small role.
8. Weave Greenhouse omits role; employer mail names BDM.
9. SentiLink first receipt omits role; later update names Go-to-Market Strategy Analyst.
10. Trase receipts omit role; later update names GTM Engineer, Healthcare.
11. Hologram activation omits role; interview reminder names GTM Engineer Pre-Sales.
12. Chapel Hill ES two filled notices (07-14 and 08-04): merged as one application.

## Vocabulary wanted and not had

- Paycom, Newton, AppliTrack/Frontline, Hirebridge, Ceipal, Spark Hire, ZipRecruiter as ats_system or submission_channel values.
- event_type for security-code / email-verification (coded employer_ack).
- exclusion_reason for newsletters/product mail (used unresolvable_identity).
