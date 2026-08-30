# Retrieval log 046

**Gmail stratum dedupe, half complete.** The roster is built. The join cannot be run.

## Why it stopped

`sources.md` records [S1] as `job_search_reconciled_audit.xlsx`, "Keegan's local copy, **uploaded to chat**." **It is not in this project and not in this session.** The 247-row Master Ledger — the set the Gmail roster must be compared against — is unavailable.

The expensive half was done anyway: extracting every company with a hiring-process artifact from logs 001 to 034. **Once the workbook is uploaded, the comparison is a single join.**

## The roster

`gmail-stratum-roster.csv`. **274 distinct entities**, typed so the comparison is meaningful rather than a raw name match.

| type | n | meaning |
|---|---|---|
| **EMP** | **224** | Employers with a hiring-process artifact. **This is the set to compare** |
| INT | 19 | Intermediaries, agencies, marketplaces. Get a row with `underlying_employer` |
| ATS | 18 | Delivery platforms. **Never an employer row.** Greenhouse, Ashby, Breezy, Workable, Dover, Paycom, AppliTrack and the rest |
| ENG | 5 | ENG-A to ENG-E. Not applications |
| EXC | 8 | Explicitly excluded by a prior log. getcrate/"Umicas ATS" and the Google and OpenAI roles it named, Luzmo, gtm-engineering.io, Nomi.ai, Podium, Common Room |

The typing is the point. A naive name-match against the ledger would have counted eighteen ATS vendors and nineteen agencies as employers and inflated the census by roughly fifteen percent.

**One merge made:** "Exa Labs Inc." (log 002) and "Exa" (logs 020, 024) are one company. Log 020 already flagged that Exa appears twice in the corpus for different reasons — a Growth Lead application and a product conversation after an API signup. **One company, two registers.**

**Two additions from outside the Gmail logs:** Renoir and Hotglue, both surfaced by the calendar re-sweep (logs 043 to 045). Marked as such, since they are not Gmail-stratum finds.

## What the counts already imply, stated carefully

The 247-row ledger contains **229 distinct normalized companies** [S1, via `02-current.md`].

The Gmail and Calendar corpus alone yields **224 distinct employers**.

**These numbers are close, and that closeness is not reassurance. It is the opposite.**

The ledger's 229 was assembled from **five sources**: the prior audit [S2], the LinkedIn applied list [S3, 99 rows], Jobright [S4, 40 rows], Ladders [S5], and Gmail. The Gmail roster is **one source**.

If a single stratum reaches 224 while a five-source reconciliation reached 229, then either the ledger was already almost entirely Gmail-derived, or **the Gmail sweep has surfaced a substantial number of employers the ledger never contained.** The second is far more likely, because the sweep is known to have overturned exclusions the prior audits made — the query manifest lists ten by name, including Weave, WorkOS, Huzzle, Mercor, Talentpluto, Atlanta Public Schools, DeKalb County, PandaDoc, Inertia Growth and Pin.

**No number is claimed here.** Two sets of similar size can differ substantially in membership, and only the join settles it. The point is that the arithmetic gives no reason to expect the Gmail addition to be small, and every reason to expect it to be material.

## Symmetry with the LinkedIn dedupe

Logs 038 and 039 measured the LinkedIn stratum: 105 rows in, 87 net additions out, 17 percent overlap. That was possible because the LinkedIn export was in hand.

The Gmail stratum is larger, longer-swept, and has never received the same treatment. **The census currently rests on one measured stratum and one unmeasured one.** Until the join runs, `247 + 87 = 334` is a floor with a missing term, and the paper cannot state a total at any stratum.

## To finish this

**Upload `job_search_reconciled_audit.xlsx`.** The Master Ledger sheet is the only one needed; its `company_canonical` column against this roster's EMP set produces:

1. Companies in Gmail but not the ledger — **net additions, the missing term.**
2. Companies in the ledger but not Gmail — LinkedIn-, Jobright- and Ladders-sourced rows with no employer artifact. These are the `platform_log` stratum and matter for the sensitivity analysis.
3. The intersection — the overlap figure, directly comparable to LinkedIn's 17 percent.

The CSV carries an empty `in_247_ledger` column for exactly this.

**One caution for when it runs.** Company-name matching across sources fails on normalization: DISQO versus DSQO, Anysphere versus Cursor, "Exa Labs Inc." versus "Exa," "Insignia Assets" versus "Insignia Collab." The codebook's `company_canonical` rule exists for this. **Match on normalized names and review every near-miss by hand** — an automated exact match will overstate the additions.

## Open

1. Upload [S1] and run the join.
2. Carried: classify the 34 meetings; recompute the interview count; correct the PhrasIQ worked example; decide A5 and A6; sweep the two extra mailboxes; Q3b, Q6, Q9, Q10, Q12.
3. **Five engagement descriptions. Still blocking Methods.**
