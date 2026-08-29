# Query manifest

Tracks every retrieval query against the study window 2025-06-01 to 2026-08-29. A query is `done` only when the API returns no `nextPageToken`.

Account for logs 001–021: keeganmoody33@gmail.com (prior run).
Account for logs 022–029: 33@lecturesfrom.com (this run).

| id | source | query | window | status | threads | logs |
|---|---|---|---|---|---|---|
| Q1 | Gmail keeganmoody33 | receipt phrases OR 12 ATS domains | 2025-06-01 to 2025-11-03 | **done**, 3 pages, no further token | 129 | 001, 002, 003 |
| Q2a | Gmail keeganmoody33 | Q1 set plus wellfound, greenhouse-mail, dover.io, paycom | 2025-11-02 to 2026-01-15 | **done**, 1 page | 39 | 004 |
| Q2b | Gmail keeganmoody33 | same | 2026-01-15 to 2026-04-16 | **done**, 3 pages | 124 | 005, 006, 007 |
| Q2c | Gmail keeganmoody33 | same | 2026-04-15 to 2026-06-16 | **done**, 2 pages | 100 | 008, 009 |
| Q2d | Gmail keeganmoody33 | same | 2026-06-15 to 2026-08-30 | **done**, 4 pages | 179 | 010, 011, 012, 013 |
| Q3 | Gmail keeganmoody33 | aggregator and discovered channels | full window | **done**, 4 pages | 163 | 014, 015, 016, 017 |
| Q3b | Gmail 33@lecturesfrom | remaining discovered employer and ATS domains | full window | **done** on this mailbox, 3 pages | 145 | 028 |
| Q3b | Gmail keeganmoody33 | remaining discovered employer and ATS domains | full window | **blocked**, mailbox not connected | | 029 |
| Q4 | Gmail keeganmoody33 | rejection and closure language without the word application | full window | **done**, 2 pages | 74 | 018, 019 |
| Q5 | Gmail keeganmoody33 | `in:sent` application, resume, portfolio, careers language | full window | **done**, 1 page | 36 | 020 |
| Q5b | Gmail 33@lecturesfrom | same sent-mail language | full window | **done**, 1 page | 3 | 027 |
| Q6 | Gmail 33@lecturesfrom | `in:sent` application language, no attachment | full window | **done**, zero threads | 0 | 023 |
| Q6 | Gmail keeganmoody33 | same | full window | **blocked**, mailbox not connected | | 029 |
| Q7 | Gmail keeganmoody33 | interview and scheduling language | full window | **incomplete**, page 1 of n, token `08010679308384994040` unused on the issuing account | 50 | 021 |
| Q7b | Gmail 33@lecturesfrom | same interview language, from the start | full window | **done**, 1 page | 27 | 022 |
| Q8 | Calendar 33@lecturesfrom | all events, 90 day blocks, no keyword filter | full window | **done**, 5 blocks | 31 events | calendar/q8-lecturesfrom-primary.csv |
| Q8b | Calendar transferred keegan@lecturesfrom | same | full window | **done**, empty | 0 | calendar/q8-transferred-empty.md |
| Q8c | Calendar keeganmoody33 | same | full window | **blocked**, calendar not listed | | calendar/q8-transferred-empty.md |
| Q9 | Gmail 33@lecturesfrom | `in:anywhere` receipt phrases including spam and trash | full window | **done**, 1 page | 2 | 025 |
| Q9 | Gmail keeganmoody33 | same | full window | **blocked** | | 029 |
| Q10 | Gmail 33@lecturesfrom | aggregator channels | full window | **done**, zero threads | 0 | 026 |
| Q10 | Gmail keeganmoody33 | same | full window | **blocked**, Q3 already covered most of this set on that account | 163 | 014–017 |

## Stop rule

Retrieval is exhaustive when Q1 through Q9 all return no further page token on **both** mailboxes, and when a final pass on any new sender domains also returns nothing new.

That stop rule is **not met**. Personal Gmail Q6, Q7 page 2+, Q3b, Q9 remain open. Personal calendar remains unswept.

## Running total

994 threads in logs 001 to 021 (keeganmoody33).
177 additional threads in logs 022 to 028 on 33@lecturesfrom.com, overwhelmingly non-employment.
31 calendar events on 33@lecturesfrom.com.
