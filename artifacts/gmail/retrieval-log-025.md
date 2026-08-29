# Retrieval log 025

Role: retriever. No coding.

- Query: Q9 `in:anywhere` receipt phrases including spam and trash
- Query string: `in:anywhere after:2025/06/01 before:2026/08/30 {"thank you for applying" "application received" "we received your application" "successfully submitted" "application has been submitted"}`
- includeTrash: true
- Account: 33@lecturesfrom.com
- Run at: 2026-08-29 ET
- Result count estimate: 2
- Page: 1 of 1. No `nextPageToken`. **Q9 exhausted on this mailbox.**

| date | sender | subject | thread_id |
|---|---|---|---|
| 2026-06-21 | noreply@getbalance.com | Complete your Pay Later for Business application with Alibaba.com | 19ee9f880d3fe262 |
| 2026-06-20 | noreply@moonshot.kimi.ai | Application Submitted (Kimi Code Beta Program) | 19ee44d95cf17f20 |

## Retriever notes

- Neither artifact is employment. Alibaba is a credit product. Kimi is a product beta.
- Spam label holds 16 threads; trash 14. This query searched them. No ATS employment receipts in spam or trash on this account.
