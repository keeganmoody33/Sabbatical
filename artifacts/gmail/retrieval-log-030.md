# Retrieval log 030

Role: retriever. No coding.

- Query: Q7 interview and scheduling language, re-run **from the start** on the issuing mailbox
- Query string: `after:2025/06/01 before:2026/08/30 {"schedule a time" "book a time" calendly "phone screen" "recruiter screen" "looking forward to speaking" "invitation to interview" "interview invitation" "grab any time" "hiring manager" "next steps in the process" "chat about the role"} -from:substack.com -from:ziprecruiter.com -from:wellfound.com`
- Account: **keeganmoody33@gmail.com**
- Run at: 2026-08-29 ET
- Method: `GMAIL_FETCH_EMAILS` metadata pages until no `nextPageToken`. The hashed token `tok_f6fa12a39fc7` from log 021 was not replayed.
- Result: 215 messages, **195 unique threads**. Last page 15 messages and **no nextPageToken**. **Q7 exhausted on this mailbox.**

Log 021 was page 1 of `GMAIL_LIST_THREADS` (50 threads). This pass covers that page and the remainder.

## Process artifacts that were incomplete or absent from Freeze 1 coding

| date | sender | what it shows | thread_id |
|---|---|---|---|
| 2025-07-07 | eml_a104534da53d | Pin, Re: Next Steps, not moving forward after Conor interview | gth_fe49801b0505bbbc |
| 2026-03-24 to 03-26 | Orchestry / Breezy | Recruiter Screen reminders. Already in Freeze 1 as Orchestry GTM Engineer (Sales) | gth_75b51a62759f69be, gth_f5dbe645e66b665d |
| 2026-03-19 | eml_5b07f5a5583b | State of GTME follow-up, already in Freeze 1 | gth_ec1fac33cf5f23f1 |
| 2026-06-15 | eml_24f646d7eb92 | Invitation Keegan Moody and Hudson Liao | gth_d1989dfb9542a2da |

Most remaining hits are newsletters, Product Hunt, Skool digests, and process mail already listed in logs 001 to 021.

## Retriever notes

- Q7 on this mailbox is closed.
- Pin's rejection lived on page 2+ of Q7 and was not in log 021.
- Dover ATS beehiiv "Rippling interview invitation" rows are newsletter marketing, not an employer ATS receipt.
