# Retrieval log 003

Same query as logs 001 and 002. Page 3 of 3. No `nextPageToken` returned, so **query Q1 is exhausted**. Returned on this page: 35 threads. Total across Q1: 129 threads.

| date | sender | subject | thread_id |
|---|---|---|---|
| 2025-07-17 | notifications@careers.scaleops.com | Thank you for applying for the Sales Engineer, USA position at ScaleOps (Spark Hire Recruit) | 19816fa4ed2957bf |
| 2025-07-15 | productforengineers@substack.com | Finding a job as a product engineer | 1980f1873f5059e8 |
| 2025-07-15 | Coursera@m.learn.coursera.org | Earn your master's of accounting | 1980e145b3a008c3 |
| 2025-07-12 | bytebytego@substack.com | EP171: The Generative AI Tech Stack | 197ff4c0fd18f34d |
| 2025-07-11 | workatastartup@ycombinator.com | Still looking for a job? (action required) | 197f9d5969e8db3c |
| 2025-07-09 | team@hi.wellfound.com | An update from Classet (Head of GTM, declined) | 197efe9bab3feb22 |
| 2025-07-08 | no-reply@gong.io | GDPR Notification from Gong.io | 197eb3b08adb3220 |
| 2025-07-08 | sarah@breakthroughz.com | Canceled invitation, Breakthrough Z Clarity Call | 197ea96a83814609 |
| 2025-07-08 | no-reply@designit.com | Thank you for applying to Designit | 197ea85c50a5e246 |
| 2025-07-08 to 07-09 | noreply@candidates.workablemail.com | Enterprise SDR, Applause (2 msg thread: receipt then rejection) | 197e8563609b2b60 |
| 2025-07-08 | noreply@candidates.workablemail.com | Thanks for applying to Applause (full application data copy) | 197e8533c3fb823c |
| 2025-07-08 | sarah@breakthroughz.com | Invitation, Breakthrough Z Clarity Call | 197e7fc9a0915aea |
| 2025-07-05 | nlpnews@substack.com | Context Engineering Guide | 197dc101c3524d89 |
| 2025-07-03 | no-reply@us.greenhouse-mail.io | Thank you for applying to Headway (Growth Marketing Specialist) | 197d047a6d227e74 |
| 2025-07-02 | no-reply@ats.rippling.com | Thank you for applying to Galileo (Growth Engineer) | 197cbf50d42e42d4 |
| 2025-07-01 | dailydozen@email.forbes.com | Quietly Building Ammunition | 197c5e530ed81b5e |
| 2025-06-30 | no-reply@eu.greenhouse.io | Thank you for applying to Gigs | 197c324e2c6972a8 |
| 2025-06-30 | noreply@pinteresttalenthub.com | You've Accepted Your Referral at Pinterest (Product Manager II, Search) | 197c192980869142 |
| 2025-06-30 | noreply@pinteresttalenthub.com | Myriah Towner has referred you for a position at Pinterest (PM II, Search) | 197c1531c3b0cd45 |
| 2025-06-28 | noreply@pinteresttalenthub.com | You've Accepted Your Referral at Pinterest (Apprentice Product Researcher) | 197b4e0054e600c8 |
| 2025-06-26 | noreply@pinteresttalenthub.com | Myriah Towner has referred you for a position at Pinterest (Apprentice Product Researcher) | 197ad3ae5480d64b |
| 2025-06-26 | no-reply@ashbyhq.com | Thanks for applying to Runway (Go-To-Market AI Engineer) | 197a9b7e36f15a96 |
| 2025-06-25 | no-reply@us.greenhouse-mail.io | Your application to Trace3 (SDR, opening filled) | 197a864d4c88286e |
| 2025-06-24 | speedrun@substack.com | SR005 Apps Reviewed | 197a23e786e215bb |
| 2025-06-22 | info@ycombinator.com | Andrej Karpathy: Software Is Changing (Again) | 197994b4d3da6db5 |
| 2025-06-21 | Jacob@getcrate.app | Umicas ATS, OpenAI Backend Software Engineer, complete your application | 19794f4f00396b15 |
| 2025-06-21 | Jacob@getcrate.app | Umicas ATS, Google Senior Software Engineer Gemini, missing materials | 197934f165cb9c11 |
| 2025-06-20 | no-reply@us.greenhouse-mail.io | Thanks for applying to Circle (GTM Engineer, Outbound) | 1978fae6c43de77c |
| 2025-06-19 | benefits@gusto.com | Update on your Gusto benefits | 19786fce29233298 |
| 2025-06-17 | benefits@gusto.com | Update on your Gusto benefits (3 msg thread) | 1977cb04971d2c89 |
| 2025-06-16 | no-reply@us.greenhouse-mail.io | An update on your application to Drata (SDR Remote) | 197794fc216fb2ec |
| 2025-06-11 | Michel@coldiqb2b.com | $2M under a year with AI (ColdIQ Accelerator Program, incomplete) | 1975ccc76268e020 |
| 2025-06-10 | myriah@townerproductions.co | W9 Form | 1975b81655c41d7e |
| 2025-06-06 | aakashgupta@substack.com | The One Skill Every AI PM Needs | 197478bec51df70e |
| 2025-06-01 | xiaosuishang@meshy.ai | Important information about your application to Meshy | 197294f8d50e00cf |

## Retriever notes

- Pinterest appears here as a **referral pathway** from a named referrer, twice, for two different roles, in June 2025. The existing ledger carries a Pinterest Apprentice Engineer application dated 2026-03-25. These are separate events and the June pair may or may not have resulted in submissions. The referral acceptance message states the application may still be unsubmitted.
- `Jacob@getcrate.app` ("Umicas ATS") claims matches to OpenAI and Google roles. Sender domain does not match either employer. Flagged for the coder as identity-unverified, not excluded by the retriever.
- Galileo appears twice with different roles and dates: Growth Engineer 2025-07-02 and GTM Engineer 2025-07-28. Two applications under the counting rules, not a duplicate.
- Applause thread contains a full copy of submitted application data, which is the highest-fidelity artifact seen so far.
- Gong.io and Spot AI appear only as GDPR retention notices. Those imply a prior application but do not date it.
- Non-employment applications present in these results: Gusto benefits, ColdIQ accelerator, Breakthrough Z coaching call. Retriever leaves them in.
