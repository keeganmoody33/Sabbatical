# Retrieval log 013

Query Q2d, page 4 of 4. No `nextPageToken`. **Q2d exhausted.** Returned this page: 29 threads. Q2d total: 179 threads.

| date | sender | subject | thread_id |
|---|---|---|---|
| 2026-06-24 | no-reply@us.greenhouse-mail.io | Thank you for applying to Tekion (Senior Manager, Inside Sales) | gth_653430f586268a32 |
| 2026-06-24 | eml_7ffabcf390dc | Thank You for Your Application: Sales Engineer at Automation Anywhere | gth_7eb495f5480f0b39 |
| 2026-06-24 | no-reply@ashbyhq.com | Thanks for applying to Canals (Sales Manager) | gth_e4e764ac5937a26a |
| 2026-06-24 | no-reply@ashbyhq.com | Thanks for applying to StackAI (Sales Engineer) | gth_c08064541ef65721 |
| 2026-06-24 | eml_29155538ea21 | RevPartners Application | gth_90376d5350b9a83a |
| 2026-06-24 | no-reply@us.greenhouse-mail.io | Thank you for applying to Enlace Health (Sales Engineer) | gth_af78469adf88e697 |
| 2026-06-24 | no-reply@us.greenhouse-mail.io | Thanks for applying to Toast | gth_8c8f0f471d0e4a6b |
| 2026-06-23 | eml_398de6c56b3b | Follow-up on your application to GTM Engineer (Match Score and Assessment Report) | gth_e14476762165423d |
| 2026-06-23 | no-reply@cloudflare.vssend.com | Cloudflare Application Update, GTM Engineer (declined) | gth_6c9a388506c32c47 |
| 2026-06-23 | eml_129233152bc5 | Thanks for Applying to RevSpring (duplicate of 06-04) | gth_3a754bf7babaa62d |
| 2026-06-22 | talent@ibm.com | You have successfully submitted your IBM job application, [redacted], Candidate ID [redacted] | gth_3f4c8312020cfc53 |
| 2026-06-22 | no-reply@us.greenhouse-mail.io | Thank you for applying to Pindrop | gth_c0cbc29cd628c44d |
| 2026-06-22 | no-reply@ashbyhq.com | Wealth.com Application Update (declined) | gth_6c9eef7e51f73df6 |
| 2026-06-22 | eml_398de6c56b3b | Next Steps for Your Job Application: GTM Engineer at Jobgether | gth_39fd61eed7768f9e |
| 2026-06-22 | no-reply@ashbyhq.com | Thanks for applying to SentiLink | gth_2670a5da7c851b05 |
| 2026-06-22 | no-reply@syncromsp.com | Thank you for applying to Syncro (GTM Operations Manager) | gth_331d3bc7e9183987 |
| 2026-06-22 | team@mercor.com | Application Submitted, Education / school Evaluator on Mercor | gth_0d17ddc7df5b3ff5 |
| 2026-06-22 | team@mercor.com | Application Submitted, General Sales / GTM Evaluator on Mercor | gth_76956966f57e2d8c |
| 2026-06-22 | no-reply@ashbyhq.com | Wealth.com Application Confirmation (GTM Engineer) | gth_31cf19b2d7f93c6d |
| 2026-06-22 | no-reply@us.greenhouse-mail.io | Thank you for applying to Attentive (first cycle) | gth_ed449ca6f36aaabd |
| 2026-06-22 | no-reply@us.greenhouse-mail.io | Thank you for applying to Armada (AI Factory, Value Engineer) | gth_56900e76d4a66f13 |
| 2026-06-21 | no-reply@anduril.com | Your Application to Anduril (Technical Operations Engineer, Launched Effects) | gth_c8b5ddd27cce25d9 |
| 2026-06-19 | eml_eabc1aeed2f7 | **Your online application with Atlanta Public Schools (submission confirmed 6/19/2026 5:09:44 PM)** | gth_69afd05b60e34a48 |
| 2026-06-19 | eml_eabc1aeed2f7 | Atlanta Public Schools Application Started | gth_ca4ec7de603636fa |
| 2026-06-18 | info@eml.upstart.com | Upstart loan offer | gth_741ca63689d90648 |
| 2026-06-16 | no-reply@adaptive6.comeet-notifications.com | Thank you for applying for the Sales Engineer position at Adaptive6 (declined) | gth_ef399881f5a0b233 |
| 2026-06-16 | notifications@us.greenhouse-jobs.com | New Jobs at Anthropic | gth_d2bf1b922efb3359 |
| 2026-06-16 | support@huzzle.app | 48 Hours Left, Final Chance to Complete Your Interview (Huzzle AI interview) | gth_c01326ed91095875 |

## Retriever notes

- **Atlanta Public Schools was submitted.** AppliTrack confirms submission on 2026-06-19 at 5:09:44 PM Central. The prior exclusions log records Atlanta Public Schools on 2026-06-19 as attempted and incomplete, with the note that the candidate explicitly says the application was not submitted. There is a started notice at 02:45 UTC and a submission confirmation nineteen hours later.
- The AppliTrack pattern is now legible across five districts. Started notices exist for Atlanta Public Schools, City Schools of Decatur, DeKalb, Gwinnett, and Douglas County. Submission confirmations exist for Atlanta Public Schools, City Schools of Decatur, and Douglas County. Expiry warnings exist for DeKalb and Gwinnett. Started plus confirmation equals submitted. Started plus expiry warning equals attempted. That is a clean decision rule.
- **Jobgether produced two artifacts**: an application receipt on 2026-06-22 and a Match Score follow-up on 2026-06-23. The prior review queue lists Jobgether as an unresolved intermediary with no employer named. The employer remains unnamed, but the application itself is documented.
- IBM's submission confirmation carries a candidate ID and requisition number, one of the highest-fidelity identifiers in the corpus.
- Huzzle sent AI-interview deadline notices on 2026-06-16 and 2026-06-11, both framing the interview as required to keep the application alive.
- Second RevSpring receipt on 2026-06-23 duplicates the 2026-06-04 receipt, consistent with the prior ledger's merge note.
- New sender domains: `jobgether.com`, `syncromsp.com`, `anduril.com`, `cloudflare.vssend.com`, `eml_7ffabcf390dc`.
