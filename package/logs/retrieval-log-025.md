# Retrieval log 025

Query Q7b, targeted follow-up on four entities surfaced by Q7 that had scheduling artifacts but no visible origin: `{from:pin.com to:pin.com from:cyft.ai from:getcrate.app from:inertiagrowth.com}`, window 2025-06-01 to 2026-08-30. **Done, 1 page, no page token.** Returned: 13 threads.

## What it resolved

| entity | resolution | evidence |
|---|---|---|
| Inertia Growth | **Resolved. Self-initiated email application.** 2025-07-26 04:17 SENT: "wanted to reach out and see if things were still open with the team @ Inertiagrowth.com. I will attach my rough resume". Hannah replies same day inviting him to book. Rejection 2025-07-30: "Thank you so much for reaching out about the Outbound Campaign Manager role. We've decided to move forward with candidates who more closely align with the level of experience we..." | gth_fa180bfd756b2a92, gth_b32d6c2b2bfb5f2b |
| Pin | **Not resolved.** No pin.com message earlier than 2025-07-07 13:59, which is itself a `Re:`. The thread parent is from a non-pin.com sender. Origin still unknown | gth_fe49801b0505bbbc |
| Cyft | **Not resolved.** Only the two scheduling artifacts already in log 024. No application receipt, no outreach, no rejection from cyft.ai anywhere in the window | gth_232aafe206c8c681, gth_d06da5b154ea5645 |
| Crate / getcrate.app | **Resolved as a false-positive class.** See below | gth_dabc46cd132a51bf, gth_3770b36755228c64, gth_73b9f98c99a2ac43, gth_3491eb82f8ab15f5 |

## The getcrate.app pattern

Four messages, 2025-06-21 to 2025-06-24, all from `eml_d498ccd3103f`, all branded "Umicas ATS" or "Crate Recruitment":

- 2025-06-21 16:25, "Reminder: We're Still Missing Your Interview Prep and Scheduling Materials", body matches Keegan to **Google, Senior Software Engineer, Infrastructure, Gemini**.
- 2025-06-21 22:07, matches him to **OpenAI, Backend Software Engineer, Leverage Engineering**, onsite San Francisco, and asks him to "complete your application, submit your interview answers and cover letter".
- 2025-06-23 01:06 and 2025-06-24 17:43, two identical reminders for a "Software Engineering position at Crate".

Three different employers in four days, all backend software engineering roles, for a candidate whose entire record is GTM and revenue. The subject line of the second message is reused as the subject of the two reminders, which is a template artifact, not a process artifact. All four are unread.

**Ruling for the coder: exclude, and record the exclusion reason.** These are solicitations written in ATS process language. They are not applications, not interview invitations, and not opportunities.

## Retriever notes

- This is now a named class with two independent members: `getcrate.app` here and `eml_93bc653507a1` in log 023. Both invoke interview and application vocabulary, both name roles far outside the candidate's lane, both were sent twice. **Methods needs a paragraph on it.** A phrase-based census that trusts language alone absorbs these; the only reliable filter found so far is a human checking whether the named role is plausible for the candidate.
- Inertia Growth is a clean example of a lane the codebook currently handles poorly: an application made by direct email with a resume attached, no ATS, no receipt, employer confirms by rejecting the specific role. It is Tier A on outcome and Tier A on submission, but it will never appear in any ATS-domain sweep. It surfaced only because a scheduling artifact pointed at it.
- The role title in Keegan's outreach was "GTME role". The rejection names "Outbound Campaign Manager". Same process, two titles. The unit of analysis is company plus role plus cycle, so the coder must pick one, and the employer's title is the defensible choice.
- **Two open retrieval items created by this log:** the Pin thread parent (one `get_thread` call on gth_fe49801b0505bbbc) and the Cyft origin (nothing in email; check Q8 Calendar and Q9 `in:anywhere`).
