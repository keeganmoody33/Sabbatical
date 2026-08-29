# Retrieval log 021

Query Q7, interview and scheduling language: `{"schedule a time" "book a time" "calendly" "phone screen" "recruiter screen" "looking forward to speaking" "invitation to interview" "interview invitation" "grab any time" "hiring manager" "next steps in the process" "chat about the role"}` minus substack, ziprecruiter, wellfound. Window 2025-06-01 to 2026-08-30. Page 1 of n. `nextPageToken` for page 2: `tok_f6fa12a39fc7`. Returned this page: 50 threads.

## Interview and process artifacts

| date | sender | what it shows | thread_id |
|---|---|---|---|
| 2026-06-15 | eml_24f646d7eb92 | **Invitation: GTM Interview with Hudson Liao**, Jun 16 | gth_d1989dfb9542a2da |
| 2026-06-16 | eml_8eedb7e060e1 | Welcome to The Hog (product signup, same day as interview) | gth_4f900acf4573a3ad |
| 2026-06-18 to 06-20 | eml_24f646d7eb92 | **GTM Engineer at The Hog: take-home assignment**, ~4 hours, 3 msg thread including SENT and a credits grant | gth_df78e875e89e162f |
| 2026-06-10 | recruiting.echo.newtonsoftware.com | **Recruiter Screen Request: RevSpring, Lead Agentic Operations + GTM Engineering** | gth_d679e7c78f455a3c |
| 2026-05-29 | eml_8ad1c0e92399 | AI role at RevSpring, from Stephanie Cunningham (recruiter approach preceding the screen) | gth_1202203d544f6fc9 |
| 2026-04-30 | eml_50d25fbb9fc0 | **Interview @ Pearl**, Keegan initiates scheduling, Alex confirms for the following week (2 msgs, includes SENT) | gth_fb41d68a16ad8c02 |
| 2026-06-05 | eml_264b9a330770 | **Dexian recruiting, Outbound Sales Consultant III (Remote)** | gth_b2e79fb0aee71c4d |
| 2026-06-30 to 07-08 | eml_e683b1afcb11 | **Luzmo SDR**, three-message recruiter sequence via Jobright, no application evidence | gth_bc1e528deaa64ce8 |
| 2026-05-28 | eml_f29cd323310b, cc eml_c15692699c6a | Meeting reminder, Common Room. Purpose not stated in the artifact | gth_b9d4242b85dd638d |
| 2026-04-29 | eml_486fba8aa61e | Invitation, 30 Minute Meeting [GTME], sent to both personal and lecturesfrom addresses | gth_6836c04b00947b35 |
| 2026-08-20 | team@mercor.com | Instant Work Offer, Growth Strategist | gth_da5b9d0848d88f36 |

Vendor demos surfaced and left in: Orbb (2026-08-17), Roark (2026-08-12). These are product demos to Keegan as a buyer, not job processes.

Roughly thirty newsletter false positives on this page (Resume Worded, Product Hunt, Wired, The Neuron, Demand Curve, Remote Hunter, Elite Recruiter Podcast, Section AI, City Lifestyle, arc.dev job recommendations).

## Retriever notes

- **The Hog ran a take-home assignment.** The prior Interviews sheet records The Hog with a single round on 2026-06-16. The corpus shows an interview invitation on 06-15, the interview on 06-16, a product signup the same day, a roughly four-hour take-home sent 06-18, and a credits grant on 06-20 after Keegan asked to use a business email. `assessment_sent` and `technical_exercise` are both live event types here.
- **Pearl has a fourth scheduling artifact.** Beyond the three Ashby reminders in logs 008 and 009, Alex DeCeglie confirmed another interview on 2026-04-30 for the following week. Pearl's process runs from at least 2026-04-30 to 2026-05-17.
- **RevSpring's process is fuller than a receipt.** A LinkedIn recruiter approach on 2026-05-29, a formal recruiter screen request on 2026-06-10, and receipts on 06-04 and 06-23. The prior ledger merged a recruiter screen into the application row; the events are separable.
- **Two agencies pitched the same role title.** WilsonHCG submitted him for Outbound Sales Consultant III on 2026-02-13, and Dexian approached him about Outbound Sales Consultant III (Remote) on 2026-06-05. Same title, different intermediaries, underlying employer unnamed in both. A coder must decide whether these are one req seen twice or two distinct opportunities.
- **Luzmo is confirmed as outreach only.** Three messages from Jobright's recruiting side across nine days, with no submission artifact anywhere in the corpus. The prior workbook's exclusion holds.
- Common Room and gtm-engineering.io meetings are ambiguous on their face. Neither artifact states whether the meeting was a job process, a vendor call, or a community conversation. Left unresolved for the coder rather than assigned.
