# Stop conditions

Written 2026-08-29 ET after the harvest that this environment can run. Waivers are explicit. They are not silent omissions.

| # | Condition | Status | Waiver |
|---|---|---|---|
| 1 | Gmail swept 2025-06-01 to 2026-08-29 for ATS domains, receipt phrases, and Sent mail with attachments | Partial | keeganmoody33@gmail.com: Q1–Q5, Q3, Q4 exhausted in logs 001–021. Q7 page 1 captured. Q6, Q7 page 2+, Q3b, Q9, Q10 on that account cannot run because this Gmail connector is 33@lecturesfrom.com. Those five queries were exhausted on the business mailbox instead. |
| 2 | Google Calendar swept in 90-day blocks, no keyword filter | Partial | 33@lecturesfrom.com primary: five blocks, no keyword filter, exhausted. Transferred keegan@lecturesfrom.com calendar: reachable, empty. keeganmoody33@gmail.com calendar: not in list_calendars. |
| 3 | LinkedIn applied list complete, including pages beyond 10 | Partial, materially improved at Freeze 3 | The full LinkedIn data download arrived 2026-08-30 and is in `artifacts/platform/linkedin_job_applications_export.csv`, 107 rows with job IDs, job URLs and exact application dates, superseding the 99-row paged scrape. **Met for the applied list.** Still **Unmet for the channel label**: the export does not mark Easy Apply against external ATS, so the capture-recapture stratum remains unmeasured. The export was generated 2026-08-23, so 2026-08-24 to 2026-08-29 is not in it. The paged scrape is kept, because 13 of its companies are absent from the export. |
| 4 | Ladders applied list exported in full | Unmet | Only the three Apply4Me Gmail receipts in Freeze 1. No full list uploaded. |
| 5 | Jobright tracker exported in full | Met | `artifacts/platform/jobright_applications_log.csv`, 40 rows, received 2026-08-29. |
| 6 | YC Work at a Startup dashboard inspected | Unmet | No dashboard artifact. YC profile-sharing mail sits in logs 001–003. |
| 7 | Talentpluto and Jobgether underlying employers resolved or formally excluded | Partial | Workable receipts exist in the keeganmoody33 harvest. Employers still unnamed in those artifacts. |

## Platform files searched and not found

Drive search for job_search, reconciled_audit, linkedin_applied, jobright, LADDERS, and all xlsx files owned by this account. Hits were unrelated (BFS grant trackers, Clay lead lists, BCOFA). [S1] and [S2] workbooks are not in Drive under the connected user.

## 212-to-163

Cannot reconstruct without the workbooks. Defect remains open.
