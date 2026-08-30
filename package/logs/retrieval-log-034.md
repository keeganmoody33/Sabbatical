# Retrieval log 034

Source: three screenshots of a LinkedIn direct message thread with Patrick F. Cua, supplied by the subject. `evidence_system = linkedin`, `evidence_class = employer_artifact`, Tier A. Not retrievable by any query run in this project so far.

## Glytec, resolved

| date | artifact |
|---|---|
| 2026-01-21 00:39 | **Patrick F. Cua, President and CEO of Glytec**, LinkedIn outreach, subject line "ceo outreach - atl-based (glytec)". Opens: "you were personally recommended by my network, so I wanted to reach out myself." Describes an AI-enabled GTM engine role owning "the systems that turn AI outputs into sales-ready pipeline". Names **Clayton Maike, VP of Sales, as hiring manager**. Invites Keegan to "**bypass our standard recruiting process**" and book directly. Notes the exec team is Atlanta-based and that they are "already actively interviewing". |
| 2026-01-22 | Keegan books the 30 Minute Sync. Calendly note: "Patrick dropped me your link" (log 022) |
| 2026-01-27 | The sync with Clayton Maike takes place (log 033) |
| 2026-01-29 11:51 | Keegan sends Patrick a PPTX, "Glytec GTM Intelligenc...", 305 KB, describing it as "what I send over to Clayton after our convo". Adds: "I think there was too much churn in my background for Clayton's liking." Offers to help "in a 1099 capacity" |
| 2026-01-30 00:47 | Patrick: "Thanks for taking the time to meet with him and we'll let you know if that could be a fit in the future." Soft decline |

**Classification.** `register = opportunity`. CEO-initiated, network-referred, and the counterparty explicitly routes around the ATS. There is no application. It does not enter the census.

Events: one interview round with the hiring manager, one unsolicited deliverable, one terminal decline. The "too much churn in my background" line is the subject's own reading and is `evidence_system = memory`, not the employer's stated reason. **The employer gave no reason.** Do not report the churn explanation as the cause.

## Correction to log 033

Log 033 stated: "six consecutive months with no job-process calendar artifacts", 2025-08-30 to 2026-02-26.

**That is wrong.** The 2026-01-27 Glytec sync was an interview with a hiring manager. It sat in the calendar the whole time, titled "Keegan Moody and Clayton Maike, 30 Minute Sync", with no role, no company context, and a referral note. I read it as unresolvable and counted the month as empty.

Corrected: the span contains **one** job-process artifact, and the claim of a six-month dead zone must be withdrawn from Results.

## This is the third instance of the same failure, and it is now the paper's central methodological finding

| process | what the artifact said | what it was |
|---|---|---|
| ENG-C interview phase, 7 meetings over 9 weeks | "No Agenda Meeting with Heath" | an interview process (log 031) |
| Glytec, 1 meeting | "Keegan Moody and Clayton Maike, 30 Minute Sync" | an interview with the hiring manager |
| Pin, 2 rounds | two neutral cal.com bookings, no receipt anywhere | an applied-to process with a take-home (log 031) |

In all three cases the scheduling artifact names no role, no company intent, and no process stage. In all three cases **the classification was only recoverable because the subject said so.**

Stated plainly for Methods: *the artifact record does not distinguish an interview from a coffee chat. Interview counts derived from artifacts alone are systematically low, and the error is not random. It is concentrated in exactly the processes that came through networks rather than ATSs.*

That is not a caveat. It is the result. And it compounds the log 032 finding: the channels that produced outcomes are the same channels whose artifacts are unclassifiable.

## The counterparty said the thesis out loud

A sitting CEO wrote, unprompted, that the way to reach him was to **bypass the standard recruiting process**. That line is worth quoting in the paper, anonymized as "the CEO of a healthcare software company", because it is the clearest external corroboration in the corpus that the application channel is not where these decisions happen.

Check it against the redaction rules in `04-engagements.md` before use. "Healthcare software company, Atlanta, CEO outreach" is close to identifying. Consider "a healthcare technology company".

## A retrieval stratum that has never been touched

**LinkedIn direct messages have not been swept at all.** Q1 through Q12 covered Gmail and Calendar. This entire process, start to finish, lived on LinkedIn and was invisible to every query in this project.

The four unswept mailboxes in log 028 were flagged as an unbounded hole. **This is larger.** Glytec proves that at least one complete Tier A process with a named hiring manager and a terminal outcome existed entirely outside the swept corpus. There is no basis for assuming it is the only one.

Consequences:

1. Census completeness cannot be stated as a range until the LinkedIn stratum is either swept or explicitly declared out of scope with its size unknown.
2. If LinkedIn messages are exportable (LinkedIn offers a data export that includes `messages.csv`), that export should be requested now. It is the single highest-value outstanding retrieval action in the project.
3. Every prior statement in logs 021 to 033 about sweep exhaustiveness is exhaustive **with respect to Gmail and Calendar only**. That qualifier now has to appear in the Methods stop rule, and the stop rule in `QUERY-MANIFEST.md` needs rewriting.

## Also recorded

Patrick's outreach references prior roles: co-founding SDR at Biofourmis, and pipeline generation in 90 days at TraceAir from a greenfield start. Both predate the study window. Context only.

## Open

- **Request the LinkedIn data export.** Highest priority.
- Glytec role title is not stated in any artifact. `role_as_listed = unspecified`.
- Whether the 1099 offer went anywhere. No further messages in the screenshots.
- Q8 blocks 4 to 6, Q12 pagination, the five engagement descriptions, three codebook changes.
