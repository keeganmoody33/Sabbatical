# Retrieval log 050

**Q3b, Q6, Q9, Q10 run.** Two close. Two do not, and the reason matters more than the results.

## Status, honestly stated

| query | result | exhausted? |
|---|---|---|
| **Q3b** — remaining discovered employer and ATS domains | **47 threads, no page token** | **Yes** |
| **Q6** — `in:sent` application language, no attachment | **5 threads, no page token** | **Yes** |
| **Q9** — receipt phrases across spam and trash | **201 ceiling** | **No** |
| **Q10** — aggregator channels | **201 ceiling** | **No** |

**Q9 and Q10 both returned at the API result ceiling**, dominated by material already in the census — ATS receipts already extracted, and in Q10's case hundreds of Ladders and ZipRecruiter job alerts, which are excluded by class.

Per the rule set in log 047: **reaching a page token is not the same as reading the results.** These two are recorded as *run and unclosed*, not as exhausted. Closing them needs narrower slices, not more pages.

## Open item closed: Pin's origin is unrecoverable

`QUERY-MANIFEST 2.md` open item 1: *"The 'Next Steps' thread parent predates 2025-07-07 and is not from pin.com. One `get_thread` on `gth_fe49801b0505bbbc` decides census versus opportunity register."*

**Done. It decides nothing, and that is the finding.**

`get_thread` returns **five messages, all dated 2025-07-07**, every one a `Re: Next Steps`. The thread id encodes a timestamp earlier than its own earliest message, which means Gmail assigned it from a parent that **is no longer in the mailbox** — deleted, or sent to an address not being swept.

The domain sweep `from:pin.com` in Q3b returns this thread and nothing else.

**Naming the queries, per log 039's rule:** `{from:pin.com ...}` full window including spam and trash, and `get_thread` on the parent id. Both reached the artifact class. Neither found a parent.

**Pin's origin therefore stands on subject recall alone** — GTM Cafe `#jobsandopportunities`, log 042. That is now a settled limitation rather than an open thread. Close it.

## Pearl's outcome, recovered

Pearl was carrying `interview_scheduled` with no terminal outcome. Q3b returns the full sequence from `eml_50d25fbb9fc0`:

| date | artifact |
|---|---|
| 2026-04-20, 04-29 | availability requests, Lead GTM Engineer |
| **2026-05-05 13:00** | **Interview 1, by phone** |
| 2026-05-08, 05-12 | next-round availability, then Zoom invite |
| **2026-05-18 10:00** | **Interview 2, Zoom, 45 minutes** |
| **2026-05-20** | *"After careful consideration, the team has decided not..."* |

`terminal_outcome = rejected_after_interview`, **2026-05-20**, exact. Two interviews, confirming the subject and log 043 against the five Gmail scheduling artifacts that were never interviews.

## Starbridge's origin is artifact-backed, and it is a community

Log 042 recorded Starbridge as inbound with no stated origin. Q3b returns Justin Wenig's cold outreach of 2025-07-25, and Keegan's reply names the method verbatim:

> *"Thanks for the Friday outreach — and for the creative sourcing method. **Using an LLM to score Clay Slack users for GTM fit?** Cool take on prospecting."*

**Starbridge sourced him out of the Clay Slack community.** That is a community-origin process with an artifact behind it, not recall — and it is a *seventh* community-attributable process, reached by a route none of the others took: he was scored and targeted rather than posting or being referred.

The sequence completes: outreach 07-25 → intro to Henry Bell, Head of Growth, 07-28 → meeting booked for 08-01 → **cancelled the same morning**, *"we ended up finding a dream candidate through our network."*

## Two smaller corrections

**RevSpring — the silence runs the other way.** Recruiter screen requested 2026-06-10, a *"One last try…"* on 06-15 saying they had attempted contact several times without reply, then the decline on 06-25. **The candidate went quiet, not the company.** Every other `no_response` in this corpus runs the opposite direction. Recorded on the row.

**Glytec's referral is confirmed in writing.** Clayton Maike's 2026-01-22 invite carries the line *"Patrick dropped me your link."* The CEO-referral origin the subject stated is now artifact-backed.

## Census effect

**No change to the count. 321 stands.** Q3b and Q6 returned no application that was not already in the register — which is itself the first evidence in this project of a query closing without adding anything.

What changed is **quality**: one outcome recovered, one origin upgraded from recall to artifact, two rows annotated, one open item closed.

## What Q9 and Q10 would need

Not more pages. Narrower slices:

- **Q9** — split by quarter and add `-from:linkedin.com -from:theladders.com -from:ziprecruiter.com`, or restrict to `in:spam` and `in:trash` explicitly rather than `in:anywhere`, which re-returns the inbox.
- **Q10** — drop the alert traffic. `{from:ziprecruiter.com from:theladders.com} {"application" "applied"} -subject:"is hiring" -subject:"may want to hire" -subject:"opening at"`.

Both are worth running. Neither is likely to be high-yield: the aggregator channels have already been mined through Q3 and Q10's own receipts, and the spam/trash hypothesis has not produced a single unique application so far.

## Open

1. Q9 and Q10, narrowed as above. **Not exhausted; do not mark them closed.**
2. The YC Work at a Startup inbox — still the highest-value unswept channel.
3. `33@lecturesfrom.com` and `keegan@morphdatastrategies.com`. Note Q3b showed Keegan using `33@lecturesfrom.com` for The Hog take-home, so that mailbox demonstrably carries process artifacts.
4. Q12 pagination.
5. **Five engagement descriptions. Still blocking Methods.**
