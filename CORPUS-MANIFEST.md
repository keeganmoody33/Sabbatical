# Corpus manifest

Frozen 2026-08-29 ET for independent coding. Every coder receives this set. A coder holding a different set is running a different study.

| artifact | format | scope | rows or items | frozen on |
|---|---|---|---|---|
| Gmail keeganmoody33 sweep, logs 001–021 | md | 2025-06-01 to 2026-08-29, queries Q1–Q5, Q3, Q4, Q7 page 1 | 994 threads | 2026-08-29 |
| Gmail 33@lecturesfrom sweep, logs 022–029 | md | same window, Q6 Q7 Q3b Q9 Q10 plus identity check | 177 threads + account notes | 2026-08-29 |
| Google Calendar 33@lecturesfrom | csv | same window, 90-day blocks, no keyword filter | 31 events | 2026-08-29 |
| Google Calendar transferred keegan@lecturesfrom | md | same window | 0 events | 2026-08-29 |
| LinkedIn applied list | csv | all pages | **absent** | waived, see artifacts/STOP-CONDITIONS.md |
| Jobright tracker | csv | full export | **absent** | waived |
| Ladders applied list | csv or image | full list | **absent** | waived |
| Wellfound applications | csv or screenshots | full list | Wellfound receipts only, inside Gmail logs | 2026-08-29 |
| YC Work at a Startup | screenshots | applied roles | **absent** | waived |
| Prior workbooks [S1] [S2] | xlsx | 247 and 212 ledgers | **absent** from this workspace | waived as coding input; they are not artifacts for extraction |

## Retrieval is not coding

Logs 001–029 are artifacts. They contain retriever notes. Coders treat subject, sender, date, hashed `thread_id`, and quoted snippets as observations. Retriever notes are not coded as facts. If a note asserts a count, ignore the count.

## Redaction

Committed artifacts store hashed evidence pointers, not raw provider IDs.

- Gmail `thread_id` values are SHA-256 prefixes with a `gth_` prefix.
- Calendar `event_id` values are SHA-256 prefixes with a `cal_` prefix.
- Gmail page tokens are SHA-256 prefixes with a `tok_` prefix.
- Applicant account IDs (IBM Candidate ID and matching req numbers) are replaced with `[redacted]`.
- Third-party addresses are hashed with an `eml_` prefix. Study mailbox labels (`33@lecturesfrom.com`, `keeganmoody33@gmail.com`, `keegan@lecturesfrom.com`) remain so retrieval scope is auditable. Automated ATS senders (`noreply`, `talent@`, `notifications@`) stay as domain identity.
- Coders join events to artifacts on these hashed pointers. Published paper copy never includes raw or hashed provider IDs.

Git history on this branch before the redaction commit still contains raw identifiers. This commit does not rewrite history. A later history rewrite would be required to purge prior commits.

## Freeze rule

No new artifacts after coder 1 begins. If keeganmoody33 Gmail or calendar, LinkedIn export, Ladders, Jobright, YC, or the xlsx workbooks arrive later, every coder re-runs or the addition is excluded from this freeze.
