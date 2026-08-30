# Retrieval log 026

Query Q8, Calendar, all events, no keyword filter. **Block 1 of 6: 2025-06-01 to 2025-08-30.** Source: Google Calendar API, primary calendar `keeganmoody33@gmail.com`, `orderBy=startTime`, `pageSize=250`. Single page, no `nextPageToken`. Returned: 52 events.

A prior pass through the device calendar aggregator returned only 7 events for the same block across all eight local calendars, none of them job processes. The Google Calendar API is the authoritative source for Q8. **The device mirror is not usable for this study and should not be cited.**

## Job-process artifacts

| date | event | counterparty | what it shows |
|---|---|---|---|
| 2025-06-30 13:00 | 1 Hour Meeting between Erica Stacy Tarwater and Keegan Moody | eml_a104534da53d | Booked via cal.com, created 2025-06-26. Description: "One hour meeting to cover all things BD." |
| 2025-07-07 11:00 | 30 Min Meeting between Conor Kline and Keegan Moody | eml_0c4c75def0f9 | Booked via cal.com, created 2025-06-30. Zoom |
| 2025-06-18 14:00 | 30 Minute Meeting with Adam Andrewjeski | Calendly | Booking form field reads "Connected @ Clay Cafe . Spoke via slack" |

## Pin is now fully mapped

Combining this block with logs 024 and 025, the Pin process runs:

- 2025-06-26, Erica books a one hour BD conversation for 06-30
- 2025-06-30, the call happens; Conor Kline books a second 30 minute call for 07-07 the same day
- 2025-07-07 11:00, the Conor call happens
- 2025-07-07 13:59, Erica chases the assignment
- 2025-07-07 16:50, Keegan submits it
- 2025-07-07 19:25, Erica declines him with written interview feedback

**Two interviews, one assignment, and a rejection inside eleven days, in July 2025.** Still no application receipt anywhere in the corpus. The earliest artifact is Erica's cal.com booking, which means Pin most likely belongs in the opportunity attribution register rather than the application census. That call is the coder's, not the retriever's.

## Adam Andrewjeski resolved

The Calendly booking form carries the context the email artifacts did not: "Connected @ Clay Cafe . Spoke via slack." A community connection, not a job process. Three artifacts in log 024 were unresolvable from email alone and are resolved by one calendar field. Exclude.

## Two work email addresses appear in the window

This is the most consequential finding in the block.

- **`eml_b0aac6b6d044`** is an attendee on a recurring **"Weekly BD Huddle"**, organiser `eml_e12cda6832c0`, other attendees `eml_adda1fb50b1c` and `eml_7798af81d583`. Created 2025-04-07, recurring weekly, instances running from 2025-06-09 and last updated 2025-07-28. The agenda is internal revenue management: "What companies did we book meetings with last week", "How are we moving along existing Qualified pipeline", "What Enablement can I provide", "DNC List Update". `keeganmoody33@gmail.com` is a separate attendee on the same event.
- **`eml_909e9737534a`** is cc'd on an EmailBison calendar invite (log 024) and Keegan holds a "No Agenda Meeting with Heath", `eml_5938273c650a`, on 2025-08-14 hosted on `mixmax.zoom.us`.

**What this does not establish:** the nature, status, or dates of either arrangement. An address on a calendar invite is not a contract. Do not write either of these into the paper as employment without a document that says so.

**What it does establish:** at least two mailboxes attached to the subject inside the study window have never been swept. Every completeness figure computed so far assumes a single-mailbox corpus. That assumption is now known to be false.

## Cancellation bias in the calendar stratum

Four processes that logs 021 to 025 document as ending in cancellation are **absent from this block entirely**: Cyft (interview 2025-07-08, canceled 07-14), Starbridge (Aug 1, canceled same day), Inertia Growth (three reschedules, canceled 2025-07-30), and Disco (canceled 2025-11-05, outside this block but same pattern).

Calendar deletes what email preserves. A calendar-only census would systematically drop exactly the processes that failed late, which is the subset most relevant to a study about conversion. **This belongs in Methods as a named limitation of the calendar stratum, and it is an argument for keeping email as the primary source.**

## Context artifacts, not census

GTM community and vendor events dominate the block and are excluded, but they are worth recording as background for the Discussion: GTM Engineer School, Cargo Hackatool, AirOps, #GirlsWhoClay, The AI Collective Atlanta chapter (three events), Startup Oasis at ATDC (three events), ZoomInfo, Clari, Pragmatic Institute, Airtable, HeySummit, La Growth Machine, Aimfox.

Inbound bookings on Keegan's own Calendly link, all networking: Kellen Casebeer (thedeallab.com), Mathew Joseph (twice), Michael Slawson (aperoadvisors.com), Jorge Macias, Jam Sheen. Vendor and peer calls: Ocean.io, Bitscale, Cannonball GTM, Matteo Tittarelli, Micah Givens, Mixmax.

Camp Horizon and CHAMPS mentor meetings are volunteer commitments, recurring throughout.

## Retriever notes

- The `eml_486fba8aa61e` series is now confirmed from a second source. This block adds five more instances including a three-way "Jorge + Robert/Keegan [GTM Engineering]" with `eml_0ed0fae9c43a`. Fourteen artifacts total across email and calendar. The exclusion recorded in log 023 stands and is now well supported.
- Q8 blocks 2 through 6 remain: 2025-08-30 to 2025-11-28, 2025-11-28 to 2026-02-26, 2026-02-26 to 2026-05-27, 2026-05-27 to 2026-08-25, 2026-08-25 to 2026-08-30.
