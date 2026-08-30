<!-- kit-meta
file: 01-engagement.md
tier: 1 (engagement)
created: 2026-08-29 13:37 ET
updated: 2026-08-29 13:37 ET
review-by: 2026-11-29
sources: [S1] [S2] [S3] [S4] [S5] [S6]
-->

# Engagement

## What this is

A paper titled Sabbatical. It reconstructs Keegan's job search from 2025-08 to 2026-08 as a forensic census, then reports what the record actually shows. The scientific framing is not decoration. The core intellectual problem is that nobody knows how many jobs they applied to, because the evidence is scattered across ATS receipts, applied-lists, aggregator agents, and screenshots, and every source double-counts the others. [S6]

Deliverables: the paper itself, a Substack post, a LinkedIn post, and figures. [S6]

## The dataset

Two workbooks exist, and the second supersedes the first.

**Prior audit** [S2], dated 2026-08-26, window 2025-08-25 to 2026-08-25:
- 212 confirmed unique applications, of which Tier A 208 and Tier B 4
- 11 interviewed unique companies
- 5 attempted and excluded
- Census completeness estimated at 80 to 85 percent
- Best estimate of true total 200 to 230
- Includes By_Month, Channels, and Open_Questions sheets

**Reconciled audit** [S1], window 2025-08-27 to 2026-08-27:
- 247 confirmed unique applications, all status Confirmed
- 244 High confidence, 3 Medium
- 11 applied companies interviewed, a 4.45 percent application-to-interview rate
- Census completeness estimated at 88 to 93 percent
- Eight sheets: Executive Summary, Master Ledger (247 rows, 22 columns), Source Reconciliation, Role Analytics, Interviews, Opportunity Attribution, External Dedupe Log, Review and Exclusions

Build path to 247, per Source Reconciliation [S1]:

| Layer | Applications |
|---|---|
| Prior Gmail-ledger floor | 163 |
| LinkedIn-only additions | 78 |
| Jobright-only additions | 5 |
| Every.to direct recovery | 1 |
| Reconciled total | 247 |

## Source reconciliation, raw to net

From [S1] Source Reconciliation:

| Channel | Raw rows | New unique | Dupes | Pending | Out of window |
|---|---|---|---|---|---|
| Prior Gmail-ledger audit | 163 | 163 | 0 | 0 | 0 |
| LinkedIn Applied pages 1 to 10 | 99 | 78 | 17 | 4 | 0 |
| Jobright tracker | 40 | 5 | 30 | 0 | 5 |
| Ladders screenshot | 3 | 0 | 3 | 0 | 0 |
| Every.to reply plus Calendar | 3 | 1 | 2 | 0 | 0 |
| Primary Google Calendar | 248 | 0 | 13 | 0 | 0 |
| Recent Gmail gap check | 2 | 0 | 2 | 0 | 0 |

The Jobright row is the strongest single argument in the paper: 40 raw rows produced 5 net-new applications. A naive sum across four trackers would have reported roughly 315 instead of 247.

## Decisions made

| Decision | What it rules out | Source |
|---|---|---|
| Unit is company + role + cycle | Counting a rejection thread as a second application | [S2] rules 1 to 3 |
| Application census separated from opportunity attribution | Counting Mixmax, Kivira Health, Mercor, Weave interviews toward application conversion | [S1] Opportunity Attribution |
| Attempted-but-not-submitted excluded, logged visibly | Silently inflating the total with started drafts | [S1] Review and Exclusions |
| Marketplace profiles excluded (YC Work at a Startup, Huzzle talent pool) | Counting profile creation as applying | [S1] Review and Exclusions |
| Roles omitted from receipts recorded as Unspecified, 15 of them | Guessing a title to make the table look complete | [S1] Role Analytics |
| Completeness reported as a range, not a point | Presenting 247 as a ceiling | [S1] Executive Summary |

## Known data problems, to be handled in Methods

These are real and already visible in the ledger. They are the paper's Limitations section.

1. **Date precision is uneven.** Of 247 rows: 154 exact, 78 relative display, 14 unknown with an evidence date, 1 latest-bound. [S1 Master Ledger] Any monthly time series built on the full census inherits roughly 93 approximate dates, nearly all of them LinkedIn rows carrying "1mo ago" style stamps captured on 2026-08-27.
2. **The dedupe key omits cycle.** The key is `company|role`, so the two legitimate second cycles (FOSSA, Attentive) appear as duplicate keys. The stated counting rule includes cycle; the implemented key does not. Either fix the key to `company|role|cycle` or document the exception. [S1 Master Ledger rows 60, 67, 91, 124]
3. **Window disagreement between workbooks.** [S2] uses 2025-08-25 to 2026-08-25. [S1] uses 2025-08-27 to 2026-08-27. The paper must declare one window.
4. **Prior-total reconciliation is not shown.** [S2] reported 212 confirmed. [S1] uses 163 as the Gmail-ledger floor and reaches 247. The 212-to-163 relationship is not documented anywhere in either workbook and needs an explicit note before publication.
5. **Tier C dominates the increment.** 78 of the 84 net-new rows are LinkedIn applied-list rows with no employer-side artifact. The paper should report the census with and without Tier C so a skeptic can see both.
6. **Self-authorship.** Subject and author are the same person, with no blind coding of role lanes.

## Constraints

- Companies are named throughout the ledger, including active relationships. Anything published needs a naming pass. [S6]
- Interview and rejection evidence lives in Gmail message IDs and Calendar event IDs. These are pointers, not publishable artifacts. Never paste raw IDs or mail links into published copy.
- Compensation, contract values, and client names appear in the Opportunity Attribution sheet. Publication decisions on those are Keegan's alone.
- Several stop conditions were never met, so the census is explicitly incomplete. That must survive into the abstract.

## Already tried

- A Gmail-only forensic audit. Produced the 163 floor. Missed LinkedIn Easy Apply entirely.
- The 212-row audit [S2], which added LinkedIn pages 1 to 10, Jobright, and Ladders, and still called itself 80 to 85 percent complete.
- Calendar keyword search for "interview" on the primary calendar. Returned 0 events. Interview loops lived inside Ashby and Meet invites with generic titles. This is why the Every.to interview on 2026-04-21 was initially invisible. [S2 Channels]
