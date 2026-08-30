# Retrieval log 047

Two classifications supplied by the subject. One is confirmed by artifact and **opens a process that appears in no prior log.**

## M05, Adam Andrewjeski — `OPP`

`register = opportunity`, informal interview, 2026-06-18 (log 045 dated it).

**No company is named in any artifact**, and none is supplied. `company_canonical = unknown`, `underlying_employer = unknown`. The row stands as an opportunity-register entry with an unknown employer, which is auditable; a silently dropped row is not.

`discovery_source = community_gtm_cafe`, subject-stated (log 042). Log 026's original exclusion is formally overturned.

## M23, Opsin Security — `INT`, and the artifacts are complete

The subject said: interview with the founder, facilitated by a recruiter. **Both halves confirmed.** Query `{opsin opsinsecurity}` returns five artifacts across two days.

| timestamp (UTC) | party | artifact |
|---|---|---|
| 2026-03-12 14:05:50 | `eml_47730432bde4` | "**Keegan Moody booked a meeting with: James Pham**" — Mar 13, 1:30 PM EDT |
| 2026-03-12 14:06:01 | James Pham | Calendar invite, `Opsin Sync`, Mar 13 13:30–14:00 EDT, MS Teams |
| 2026-03-12 14:06:05 | **`eml_d704380cb842`**, cc `eml_2b8a91327171` | "**Video Interview; Opsin Security with James Pham Friday @ 1:30pm EST**" — prep material, and: "**The 2nd round is a take home activity**" |
| 2026-03-12 21:15:29 | Keegan | Reply to Adrianna acknowledging the prep pack |
| 2026-03-13 16:30:37 | James Pham | Meeting reminder |
| 2026-03-13 17:10:00 | Keegan | "Eager to meet as well" |
| 2026-03-13 17:58:16 | Keegan | "**Thanks / heres video**" — sends *Assetmule.ai Campaign 1.0*, a walkthrough of his process |
| 2026-03-13 18:28:14 | Keegan | "**Question**": "What does success look like to you after 6 months of having a GTME James? ... Why not just continue to do what you are doing?" |

**Interview held 2026-03-13 13:30 EDT** with **James Pham, founder, Opsin Security**, facilitated by **Adrianna at Colossus Technology Group**. A second round take-home was contemplated in writing. **No outcome artifact exists** — no rejection, no round-two confirmation, nothing after 2026-03-13.

### Register: `opportunity`, not census

There is no application receipt anywhere and the recruiter initiated the process. Under the two-register rule this is `register = opportunity` — the same shape as WorkOS via TopHire.

**It therefore does not raise the census interview count.** It raises the opportunity register, which is the point the paper keeps arriving at.

### Colossus Technology Group is an intermediary, and this reclassifies a LinkedIn row

`colossustg.com` is a recruiting firm. **`LI-034` in `linkedin-applications-in-window.csv` is "COLOSSUS TECHNOLOGY GROUP, GTM Engineer," dated 2026-04-06** — and log 038's dedupe marked it `net_new` with **no company match**, because Colossus appears nowhere in logs 001 to 034.

Two corrections follow:

1. **Colossus is `INT`, not an employer.** LI-034 needs `underlying_employer`, currently `unknown`.
2. **The Opsin interview (2026-03-13) precedes the Colossus application (2026-04-06) by three weeks.** They are not the same process in the obvious direction. Either LI-034 is a second, later Colossus-posted role for a different client, or it is a re-approach to the same one. **Ask the subject; do not merge.**

### The retrieval failure

**Five Gmail artifacts, two of them with "Interview" in the subject line, and none of them is in any retrieval log.**

Q7 was the interview-and-scheduling-language sweep, declared exhausted at four pages and 195 threads (logs 021 to 024). The subject line "**Video Interview**; Opsin Security with James Pham" should have been a direct hit.

This is the **fourth** instance of the same failure class: Dagster (log 040), Orchestry (log 041), the blocks 1–3 calendar sweep (log 045), and now Opsin. In each case the artifacts were reachable and the reading did not reach them.

**Consequence for the manifest:** Q7's exhaustion claim should be treated as unverified. "No further page token" proves the query was paginated to the end; it does not prove the results were read. Those are different claims and `QUERY-MANIFEST 2.md` conflates them.

### A behavioural pattern worth recording

Keegan sent James a **work-sample video** hours after the call. The same move appears at **BX Studio** (log 020: video sent, forwarded to the hiring manager) and at **TrueBuilt** (log 042: the CEO saw a video he had sent and asked about contract work).

Three instances, one of which converted an expired requisition into a contract conversation. **This is a candidate finding for Discussion**, not a coded field — and it is the kind of thing a census of receipts is structurally incapable of seeing.

## Where the two registers now stand

Provisional, and both are floors.

- **Census interviews: ≥13** — the eleven, plus Dagster and Hypergen. Unchanged by this log.
- **Opportunity-register processes reaching a real conversation: ~11** — Mixmax, Glytec, Starbridge, WorkOS, The Kiln, Weave, Mercor, Adam, TrueBuilt, **Opsin**, and Doug Shankman pending his classification.

**Two pipelines of comparable size.** One is the residue of several hundred applications; the other came from communities, referrals and inbound. The paper has been circling this since log 032. It is now close to being countable.

**Do not state it yet.** Thirty-two meetings remain unclassified and any of them could move either number.

## Open

1. **32 of 34 meetings still unclassified.** Critical path unchanged.
2. Ask: is LI-034 (Colossus, 2026-04-06) the Opsin role or a different client?
3. Re-type Colossus as `INT` in `gmail-stratum-roster.csv` and set LI-034's `underlying_employer`.
4. **Q7's exhaustion claim is unverified.** Distinguish "paginated to the end" from "read" throughout the manifest.
5. Carried: Gmail dedupe join (needs [S1]); interview recomputation; PhrasIQ worked example; A5 and A6; the two extra mailboxes; Q3b, Q6, Q9, Q10, Q12.
6. **Five engagement descriptions. Still blocking Methods.**
