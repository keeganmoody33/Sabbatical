# Coder cursor notes

Artifacts processed: Gmail logs 001-029 (1171 threads listed), calendar CSV (31 events), platform-absent note. Retriever notes were not treated as facts.

Rows emitted: applications 232 (register=application 222, register=opportunity 10), events 278, exclusions 45.

Skipped extra events whose application_id did not match a minted key: 0.

## Judgement calls

1. Weave: Greenhouse 2025-07-27 is the submission. 2026-08-18 interview decline is the same cycle (no second submission).
2. WorkOS: opportunity. Recruiter-sourced, no submission receipt.
3. Mercor: six Application Submitted rows are applications. Growth Strategist / hourly contract is opportunity.
4. Huzzle: Workable submission language wins over talent-pool marketing copy.
5. Talentpluto: two Workable titles three minutes apart counted as two applications. Underlying employer unknown.
6. DeKalb general expiry is attempted. Eleven position-filled notices are applications because the employer said the position you applied for. Chapel Hill ES two notices = one cycle.
7. Atlanta Public Schools: submitted, then district not accepting substitutes. Both recorded.
8. Gwinnett: started plus expiry = attempted_not_submitted.
9. Pinterest June 2025 referrals: attempted. March 2026 Apprentice Engineer Greenhouse row is the application.
10. The Hog: no ATS receipt. Coded application from a titled GTM interview plus take-home. Medium confidence. Could have been opportunity.
11. Owner.com: used subject GTM Engineer; body Product Builder recorded in notes.
12. Anysphere canonical for Cursor.
13. FOSSA and Attentive use cycle 2 after a terminal outcome.
14. Pogo 2026-07-08 Ashby coded as cycle 2 with medium confidence; may be a channel duplicate of the June Gem receipt.
15. Unframe 04-06 and 04-17 merged as one cycle.
16. Productboard 07-13 GTM Engineer and 07-15 Associate GTM Engineer merged as one cycle using the more specific later title.
17. Meshy 2025-06-01 interview decline: out_of_window (submission likely before window).
18. Dover/beehiiv Leidos and Rippling SEM: unresolvable_identity.
19. Newsletters, Anthropic job alerts, ZipRecruiter alerts, Jobright alerts, study portals, Apple Card, Kimi beta, Alibaba, Wells Fargo banking: not coded as employment candidates except as listed exclusions. Remaining Substack/newsletter threads are classified as non-candidates by sender domain and are not one-row-per-thread.
20. Calendar PhrasIQ Discovery attached to the Wellfound PhrasIQ application. Jorge Macias / Kivira / Rocketeer / Mixmax product / Morphin are not applications.
21. Inertia Growth title taken from the decline (Outbound Campaign Manager), not the sent-mail subject GTME role.
22. IBM Confluent: underlying_employer Confluent on an IBM submission.
23. ThriveLink: opportunity (referral intro, no submission).
24. Classet: evidence_bound decline without a submission receipt.
25. Gradient Labs: ZipRecruiter complete-your-application plus later decline. Medium. Not promoted solely by the ZipRecruiter complete prompt.
26. Built Recruiting: evidence_bound position-filled update.
27. Salary always not_stated; never inferred.

## Conflicts

- Owner.com subject vs body titles. Subject used.
- Mercor 2026-06-30 marketing said not yet applied, contradicting 2026-06-22 Application Submitted receipts. Receipts win.
- Retriever notes that cite prior ledger totals were ignored.
- Weave 2025-07-31 decline vs 2026-08-18 interview: both kept; terminal is the later interview decline.

## Vocabulary wanted and not used

- AppliTrack / Frontline as ats_system. Used none_observed.
- Newton / Paycom / Gem already partly covered; Gem is in the vocab.
- event_type for marketplace contract activation. Used offer for Mercor contract.
