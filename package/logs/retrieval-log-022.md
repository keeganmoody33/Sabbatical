# Retrieval log 022

Query Q7, interview and scheduling language: `{"schedule a time" "book a time" "calendly" "phone screen" "recruiter screen" "looking forward to speaking" "invitation to interview" "interview invitation" "grab any time" "hiring manager" "next steps in the process" "chat about the role"}` minus substack, ziprecruiter, wellfound. Window 2025-06-01 to 2026-08-30. Page 2 of 4. `nextPageToken` for page 3: `tok_7f498e174f48`. Returned this page: 50 threads. Result count estimate reported by the API: 201.

## Interview and process artifacts

| date | sender | what it shows | thread_id |
|---|---|---|---|
| 2026-04-20 | eml_50d007c54e63 | **Every, GTM Engineer.** "Thanks so much for applying for the GTM Engineer role. I'd love to chat. Grab any time." Keegan books 12:15 next day. 2 msgs incl. SENT | gth_3731d4c2c0e7637c |
| 2026-04-14 | eml_3753b60c2e7b | **Hypergen calendar invite**, Mon Apr 20 09:00 to 09:20 EDT | gth_cc1c2088d64efe52 |
| 2026-03-11 then 2026-04-14 | recruitee.com then people@hypergen.io | Hypergen application receipt 03-11, then "we would love to meet with you, book a time" 04-14, same thread | gth_d34cb1ecb8ba51f6 |
| 2026-04-08 | eml_520bf8c2802d | **Bask Health, Sales Engineer.** "Your background looks solid, let's set up a time to chat", two Calendly links. No application artifact in this thread | gth_f5e980eb01afdda8 |
| 2026-04-08 | eml_dd661064d709 | **BX Studio, GTM Engineer Application.** TA manager outreach, Keegan replies, sends a video, Simon forwards to the hiring manager. 5 msgs incl. 3 SENT | gth_cd9b1dc5bcc04d6c |
| 2026-04-06 | no-reply@ashbyhq.com | **Rula, GTM Engineer (Remote)** application receipt | gth_b6c113b453e1bffe |
| 2026-03-24 | no-reply@orchestry-software-inc.breezy-mail.com | **Orchestry, GTM Engineer (Sales)** application receipt | gth_397ef5934d0939b2 |
| 2026-03-24 | eml_87e77a84a157 | **Invitation to Interview with Orchestry**, 45 minute video interview, same day as the receipt | gth_a97f0370deb0e0f5 |
| 2026-03-24 | orchestry breezy-mail | Recruiter Screen scheduled | gth_75b51a62759f69be |
| 2026-03-25 | orchestry breezy-mail | Recruiter Screen reminder, 10 minutes out, with Jay Banga | gth_2bc5f58bf63d9e09 |
| 2026-03-25 | orchestry breezy-mail | Recruiter Screen rescheduled, new video link | gth_f5dbe645e66b665d |
| 2026-03-26 | orchestry breezy-mail | Recruiter Screen reminder, 10 minutes out | gth_46950509081a40b9 |
| 2026-03-13 | eml_5b07f5a5583b | **Beautiful.ai, GTM Engineer intro request.** Keegan books for Tuesday. 3 msgs incl. SENT | gth_c85343e199b747cd |
| 2026-03-17 to 03-19 | eml_5b07f5a5583b | Post-interview thread: Keegan sends State of GTME and portfolio, Emily says she will chat with Brandon Ness, then 03-19 the hiring manager wants more candidate conversations before deciding. 4 msgs incl. 2 SENT | gth_ec1fac33cf5f23f1 |
| 2026-02-20 | eml_261b430a689a | **TestGorilla, Go-to-Market Engineer.** Senior TA partner opens the process and walks through stages | gth_3e7b5aedf6286ab2 |
| 2026-01-22 | eml_e5c4cc8ec99d | 30 Minute Sync booked via Calendly. Note in the booking form: "Patrick dropped me your link". Purpose not stated in the artifact | gth_3b4b72238f26a336 |

## False positives on this page

Vendor and buyer-side calls left out of the census: Inboxkit demo (2026-04-17, three artifacts including a Calendly reminder), Firecrawl product feedback with Erin Xue (2026-01-23 and 01-28, sender eml_9e53ca73d659), Erlin AI pro-access invitation (2026-02-26, eml_089cd7d5b388), CentralNic four-message sales sequence to Keegan (2026-02-09 to 03-24), Read.ai meeting report for a "Sales sync with Keegan and Lindsay" on his own client work (2026-03-15).

Newsletters and digests: Skool weekly digest, Resume Worded, Wired, Upwork, theaireport, aiforwork, superhuman, demandcurve, rb2b, ghuntley, Glassdoor job alerts, kylepoyar, vcunfiltered, codewords, retrainedsearch, godofprompt, coldiq, shorthand, wispr.

## Retriever notes

- **Every is a new application with a same-day interview booking.** Austin's message names the GTM Engineer role and says "thanks for applying", which is employer-side confirmation that an application exists even though no ATS receipt for Every has surfaced in any log so far. Tier B on the application itself, Tier A on the scheduling.
- **Orchestry is the fullest single process in the corpus so far.** Application receipt, interview invitation, recruiter screen scheduled, reminder, reschedule, second reminder, all inside 72 hours, 2026-03-24 to 03-26. Six artifacts, one req. Any per-application event count that treats this as one row will understate process depth badly.
- **Hypergen's timeline is now complete.** Application 2026-03-11 via Recruitee, interview offer 2026-04-14, calendar invite 2026-04-14 for 2026-04-20. Log 021 and the manifest recorded only the 04-14 invitation. The 03-11 receipt ties it to the census.
- **Beautiful.ai ran at least two stages.** The 03-13 intro request and the 03-17 to 03-19 follow-up are separate threads. The 03-19 message is a soft hold, not a rejection, and no closure artifact appears on this page.
- **Bask Health and Glytec are unresolved.** Bask names a role and a Calendly link but no application receipt appears in this thread. Glytec is a 30 minute sync sourced by a referral ("Patrick dropped me your link") with no role named. Both go to the coder, not to a lane.
- One alternate address appears in the corpus that has not been swept: `eml_909e9737534a`, cc'd on an EmailBison calendar invite (log 024). Flagging it here because it may be a Mixmax integration artifact rather than a mailbox. Do not assume either way.
