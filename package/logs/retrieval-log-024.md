# Retrieval log 024

Query Q7, same string as logs 021 to 023. Window 2025-06-01 to 2026-08-30. Page 4 of 4. **No `nextPageToken`. Q7 is exhausted.** Returned this page: 45 threads. Q7 total across four pages: 195 threads.

## Interview and process artifacts

| date | sender | what it shows | thread_id |
|---|---|---|---|
| 2025-07-07 | eml_a104534da53d | **Pin, "Next Steps".** Assignment chased before a meeting with Conor, Keegan submits, Keegan flags a sitemap issue on pin.com unprompted, same-day rejection: "we've decided to not move you forward in the interview process. I listened to your interview today" plus written feedback. 5 msgs incl. 3 SENT | gth_fe49801b0505bbbc |
| 2025-07-08 | eml_c3efd3e79830 | **Cyft Growth Team Interview** scheduled via Calendly | gth_232aafe206c8c681 |
| 2025-07-14 | eml_c3efd3e79830 | Cyft interview **canceled** | gth_d06da5b154ea5645 |
| 2025-07-25 to 07-30 | eml_2478127bd08b | **Starbridge, founding GTM engineer.** Founder outreach 07-25, Keegan replies same day, 07-28 intro to Henry Bell (Head of Growth), Keegan proposes Wednesday, 07-30 Henry offers his calendar. 5 msgs incl. 2 SENT | gth_c9afad0ec6efb54a |
| 2025-08-01 | eml_a6156f4c5e37 | Starbridge 30 Minute Meeting invite for Aug 1 14:30 | gth_cb808aa7a44998c9 |
| 2025-08-01 | eml_a6156f4c5e37 | **Starbridge closes the loop:** "we ended up finding a dream candidate through our network" | gth_d1b9551b995c0838 |
| 2025-08-01 | eml_a6156f4c5e37 | Starbridge event canceled | gth_40279d3d04eed6ea |
| 2025-07-26 | eml_63112bdfe422 | **Inertia Growth, Outbound Campaign Manager Intro Call** invite for Jul 28 | gth_3f5088370129f004 |
| 2025-07-28 | eml_63112bdfe422 | Rescheduled to Jul 30 | gth_6983748205fb618f |
| 2025-07-30 | eml_63112bdfe422 | Rescheduled to Jul 31 | gth_48aa2664a461bf01 |
| 2025-07-30 | eml_63112bdfe422 | Canceled | gth_99cbcae1bfa4b884 |
| 2025-07-03 | no-reply@us.greenhouse-mail.io | **Headway, Growth Marketing Specialist** application receipt | gth_24f31ba9b6d07994 |
| 2025-06-20 | no-reply@us.greenhouse-mail.io | **Circle, GTM Engineer, Outbound** application receipt | gth_d2d399fc49799ade |
| 2025-06-23 and 06-24 | eml_d498ccd3103f | "Crate Recruitment", Software Engineering position, two reminders that interview prep and scheduling materials are missing. See log 025 | gth_73b9f98c99a2ac43, gth_3491eb82f8ab15f5 |
| 2025-06-16 to 06-18 | notifications@calendly.com | 30 Minute Meeting with Adam Andrewjeski, confirmed 06-16, two reminders. No company, no role named | gth_d1c3656455b5dd6e, gth_76a710a2db60a950, gth_40cec6bd30a9c6c2 |
| 2025-08-06 | keeganmoody33@gmail.com to eml_fc0d386e78b0 | **SENT.** Self-initiated pitch to MxP.studio as a technical resource for prototyping and context engineering. No reply in this thread | gth_513195aca313fb41 |

## Named false positives worth recording

- **Google is not an interview.** `eml_f8aba22fb35b`, "Meeting with Google (Keegan Moody)", Aug 8 2025. The booking form shows Keegan booked it under the organisation name "lecturesfrom" with the agenda "Intro to Cloud Partnership Program". This is a partner call, not a job process. Worth naming because a reader scanning sender domains would read it as a Google interview.
- **Exa is a product conversation, not an application.** `eml_215e3f8ad944` 2025-06-12: "saw you signed up for the API so thought I'd reach out", then Will Roberts sends a cal.com link. The manifest lists Exa among new applications discovered in the June to October 2025 window. Either that row rests on a different artifact or it is an error. **Do not merge these two Exa threads.** Open question for the coder.
- Clay customer call (2025-06-18), Breakthrough Z "Clarity Call" coaching sales call (2025-07-08), La Growth Machine trial expiry, AppCompass launch mail, Skool digest, coldiq, outskillai, superhuman, Product Hunt, theneuron, open-source-ceo, salescraft, Resume Worded, cultivatedculture.

## Retriever notes

- **Pin is the most complete single process yet found inside the window both prior audits treated as empty.** Interview, assignment, employer-side feedback, and rejection, all on 2025-07-07. The parent message of the thread predates 07-07 and is not from a pin.com address, so the origin artifact, which decides whether Pin enters the application census or the opportunity register, is one `get_thread` call away. Flagged, not assumed.
- **Starbridge and Cyft are both July 2025 processes that ended by counterparty cancellation.** Starbridge states the reason in writing. Cyft does not. Neither has an application receipt in the corpus, so both are opportunity register candidates pending Q9.
- **Inertia Growth rescheduled twice before cancelling.** Four scheduling artifacts for one process. Same pattern as Orchestry in log 022. Scheduling churn is itself a measurable feature of these processes and the current codebook has no event type for a reschedule.
- **The 2025 window keeps producing.** This page alone adds Pin, Cyft, Starbridge, Inertia Growth, Headway and Circle to a period the 212 and 247 ledgers between them recorded as nearly empty. That is now six separate direct processes plus two employer receipts from a single page of a single query.
- Adam Andrewjeski, three Calendly artifacts and no company or role anywhere in them, is unresolvable from email alone. Q8 on Calendar may carry the organiser domain.
