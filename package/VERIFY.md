# VERIFY.md

**An adversarial audit of everything an assistant wrote into this repo on 2026-08-30.** Run this before trusting any of it.

You are not helping. You are checking. **Your job is to find where this is wrong.** A pass with no findings is a suspicious result on a corpus this messy, so if you find nothing, say what you were unable to check rather than reporting all clear.

The person running this has the raw artifacts on his machine. This repo has summaries of them. **The whole point of this pass is that those are different things.**

## The one reason to distrust this repo already

While assembling it, the assistant wrote into `MANIFEST.md` that `retrieval-log-029.md` "is referenced by no file." **That was false.** `knowledge/04-engagements.md` cites log 029 four times, including as a source for ENG-B.

The cause was a brittle query: the grep searched `log 029`, `log-029` and `logs 029`, and the file actually says `logs 026, 027, 028, 029` and `logs 026 to 029`. It was caught on a second pass and corrected in place.

**Assume more of this kind of error is present.** When you check a claim, do not re-run the query that produced it. Design a different one.

## Rules for this pass

1. **Do not edit `logs/`.** They are append only. Every finding you produce goes into a new `logs/retrieval-log-052.md`.
2. **Do not change a census total.** Only `knowledge/08-census-ledger.md` may state one, and only with a reason recorded in it.
3. **Report a discrepancy as a discrepancy.** Do not reconcile it silently, do not average, do not pick the more flattering figure.
4. **Distinguish "I checked and it is wrong" from "I could not check."** The second is a finding too, and on this repo it will be the more common one.
5. Cite a file and a line for every claim you make about a claim.

---

## Part A — checks you can run inside this repo, no raw files needed

Run all of these. They are cheap and two of them have already caught errors.

### A1. Register integrity

`data/full-application-register.csv` against `knowledge/08-census-ledger.md`.

Expected: **321 data rows, 298 distinct companies, 234 `gmail/ATS`, 87 `LinkedIn`, 35 rows with a blank `applied_date`.** Tier split A 291, B 23, C 7. Zero exact duplicate keys on normalized company plus normalized role plus date.

This was verified once and passed. Verify it again with your own parser. If it disagrees, the ledger's own self-audit at line 15 is wrong and everything downstream moves.

### A2. The Jobright join, re-derived from scratch

`logs/retrieval-log-051.md` reports **21 exact company-and-date matches, 15 company-only matches, 4 absent** when `raw/jobright_applications_log.csv` is joined to the register.

**Do not reuse the assistant's normalization.** It used a hardcoded alias map containing only `tekioncorp→tekion` and `colab→colabsoftware`, and it initially produced a false miss on `Jobright.ai` that had to be caught by grep. Build your own matcher, ideally fuzzy, and report any pair the original map would have missed.

Then check specifically:

- **Axon.** Log 051 claims the register holds exactly one Axon row (`Manager, Go-to-Market Readiness`, 2025-08-04) and that Jobright's `Key Account Executive` 2026-01-02 is therefore a second application under counting rule 2. Confirm the register holds exactly one.
- **Autodesk, MavenAI, Vanco.** Log 051 claims all three are absent from the register, absent from `data/gmail-stratum-roster.csv`, and absent from `data/linkedin-applications-in-window.csv`. Check all three files, and check spelling variants: `Maven AI`, `Maven`, `Vanco Payment Solutions`, `Autodesk Inc`.
- **The two blank-date recoveries.** `Jobright.ai, Product Manager (Early Career)` and `OpenObserve, Growth Marketer` are claimed to have blank `applied_date` in the register. Confirm, and confirm nothing else in the corpus already dates them.

### A3. The zero-interview claim

Log 051 claims **0 interviews across 43 register rows tied to the 40 Jobright companies**, with 18 `rejected_no_interview`, 16 `no_response`, 9 `unknown`.

This rests entirely on the register's `outcome` column being correct. **Spot check at least six of those rows against the retrieval log named in their `source` column.** Trase, Clay, Pindrop, FOSSA and Nebius are the highest-value checks because a missed interview there changes a headline rate.

### A4. The one-day offset, interpretation vs evidence

Log 051 section 4 reads a cluster of eleven rows dated 2026-05-20 in Jobright against 2026-05-21 in the register as *"the agent queued a batch late on 05-20 and the ATS receipts landed 05-21."*

**That is an interpretation, not evidence.** Nothing in the corpus establishes it. Competing explanations: a timezone difference in Jobright's export, or the tracker recording when the user queued the role rather than when the agent sent it.

Verify the eleven, then either find an artifact that discriminates between the explanations or **downgrade the sentence to a hypothesis in the log.**

### A5. The collision resolutions

`MANIFEST.md` claims four collisions were resolved when this repo was built from a 75 file Claude Project.

- `extraction.md` ×3 byte identical, md5 `dc6a5f19e963b824927ef39467a233fb`. **Re-derive the md5 from the originals.**
- `codebook.md` dropped as stale because it carried `newsletter_community`, retired by amendment A3, and had no A1 to A4 content. **This is the highest-stakes deletion in the assembly. Verify against `knowledge/05-codebook-amendments-r1.md` that A3 really retired that value, and confirm no other file still depends on `codebook.md`.**
- `QUERY-MANIFEST_2.md` kept over `QUERY-MANIFEST.md` as strictly newer. **Diff both originals line by line.** Confirm no row exists in the discarded file that is absent from the kept one.
- `claude_` prefixes stripped. Confirm no two files collapsed onto the same name.

### A6. Every dangling reference

Grep the whole repo for references to files and logs, and list every one that does not resolve. Log 029 is known. **Find the others.** Include `sources.md` ids S1 to S6, every `logs NNN` citation, every `ENG-x`, every `LI-NNN`, and every `Q` id in the query manifest.

---

## Part B — checks that need the raw files

These cannot be done inside the repo. `raw/README.md` lists what is missing. **For each check below, if the file is absent, say so and stop. Do not substitute a summary for an artifact.**

**Part B is a queue, not a blocker.** Keegan is drafting in parallel. Run each item the day its file lands and append the result to the audit log. Do not wait for the full set.

### B1. The fifth Jobright row

`08-census-ledger.md` states the retired [S1] workbook recorded **5** Jobright-only additions. Log 051 recovered **4**.

Open `raw/job_search_reconciled_audit.xlsx`, Source Reconciliation and Master Ledger, and **name [S1]'s five.** Then say which of the three explanations in log 051 section 9 is right. This is the single highest-value item in Part B.

### B2. Do the logs match the mailbox

**This is the structural check and it is the reason this pass exists.**

Every row in the Gmail stratum of `data/full-application-register.csv` traces to a numbered retrieval log. Those logs are *summaries written by a reader of the mailbox*, not the mailbox. `08-census-ledger.md` gap 5 already admits the misses are "known to be non-zero" and names Opsin, which had five artifacts including two with "Interview" in the subject and appeared in no log.

With the Gmail export in hand, sample **at least 30 threads at random** from the swept windows and check whether each produced the register row it should have. Report the miss rate. **That number is the honest completeness estimate for the Gmail stratum and this project does not currently have it.**

### B3. LinkedIn export against the dedupe resolution

`data/linkedin-dedupe-resolution.csv` resolves 105 in-window rows to 87 net additions. Re-derive from the raw LinkedIn `Job Applications.csv`. Confirm the 105 in-window filter and the 18 overlaps.

Known wrinkle to test: `06-method-retrospective.md` says **Attentive's second cycle is in Gmail and absent from the LinkedIn export**, so the export is not proven complete. Look for other cases of the same shape.

### B4. Calendar against the event layer

`07-meetings-to-classify.md` holds 34 counterparty meetings awaiting classification, and `02-current.md` reports 277 events across 6 blocks. Re-derive both from the calendar export.

Log 043 established that calendar enumerates *invited* meetings and is blind to meetings arranged by phone or DM, with Dagster Labs and The Kiln as proof. **Do not treat the calendar as a bound on the event layer.**

### B5. Log 029

Search the original chat history or any local export for the missing log. If it is unrecoverable, `04-engagements.md` needs a stated gap on ENG-B rather than a silent citation.

---

## Output

Write `logs/retrieval-log-052.md` with this shape:

1. **What I checked and how**, method per check, and the query you used where you deliberately used a different one than the original.
2. **Confirmed**, a table of claims that held, with the check that held them.
3. **Refuted**, every claim that did not survive, with the evidence. Be specific about which file and line carries the wrong claim.
4. **Could not check**, every item blocked by a missing raw file, naming the file.
5. **New findings.** Anything the audit surfaced that nobody was looking for.
6. **Open**, what the next pass has to do.

Then, and only then, propose edits to `MANIFEST.md` and `knowledge/08-census-ledger.md`. **Propose them. Do not apply them.** A census total changes by human decision with a reason recorded, never as a side effect of an audit.

## Things you should refuse to do

- Fill a gap with a plausible value.
- Promote a subject-recall row to artifact evidence because the artifact "probably exists."
- Renumber the retrieval logs to close the 029 hole.
- Reconcile 4 against 5 by choosing one.
- State a census total anywhere except the ledger.
