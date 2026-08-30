# Named companies in the draft

`knowledge/01-engagement.md` requires a naming pass before anything is published, because the ledger
names companies including active relationships. This file is that pass as a checklist rather than a
re-read: every company named in `paper/PAPER.md` **or** its companion `paper/COMPANION.md`, where it
appears, and the risk of naming it. Both pieces are publication candidates, so both are covered.

**Which names survive is the author's decision alone.** Nothing here recommends removing a name. It
flags what needs a decision.

No dashes are used as punctuation in this file.

## Decide these first: still-open processes

Eight of the fourteen interviewed applications carry `terminal_outcome = still_open`. Naming a
company while a process with it is live is the case `knowledge/instructions.md` says to flag and
hand back, so these are listed first.

| Company | Where it appears | What is disclosed | Risk |
|---|---|---|---|
| Every.to | Section 3.3 interview table | Applied, interviewed, process open | Live process |
| Hologram | Section 3.3 interview table | Applied, interviewed, process open | Live process |
| Hypergen | Section 3.3 interview table | Applied, interviewed, process open | Live process. Also one of the three interviews resting on a single coder |
| Pearl | Section 3.3 interview table | Applied, interviewed, process open | Live process |
| PhrasIQ | Section 3.3 interview table | Applied, interviewed, process open. Title unknown from the receipt | Live process |
| RevSpring | Section 3.3 interview table | Applied, interviewed, process open | Live process |
| TestGorilla | Section 3.3 interview table | Applied, interviewed, process open | Live process |
| The Hog | Paper section 3.3 interview table and section 5; companion part 2 | Applied, interviewed, process open. Also named as a row reversed from opportunity to application at Freeze 3, with its submission date | Live process, and named as a methodology example in both pieces |

Options if any of these should not be named: replace the cell with a stable pseudonym (Company A,
Company B) and keep the row, so the count of 14 still reconciles. Dropping a row silently would
break the arithmetic in section 3.1.

## Closed processes, named

| Company | Where it appears | What is disclosed | Risk |
|---|---|---|---|
| Beautiful.ai | Section 3.3 interview table | Applied, interviewed, rejected after interview. Title unknown from the receipt | Closed. Discloses a rejection |
| Dagster Labs | Section 3.3 interview table | Applied, interviewed, rejected after interview | Closed. Discloses a rejection |
| Great Question | Section 3.3 interview table | Applied, interviewed, rejected after interview | Closed. Discloses a rejection |
| HartleyCo | Section 3.3 interview table | Applied, interviewed, rejected after interview | Closed. HartleyCo is an intermediary, so the underlying employer is not named |
| Orchestry | Section 3.3 interview table | Applied, interviewed, rejected after interview | Closed. Discloses a rejection |
| jobmail.io | Section 3.3 interview table and section 5 | Applied, interviewed, and named as the row carrying a coding contradiction | Closed. The row is named as a data defect, which is a second thing to weigh |
| BX Studio | Paper section 5; companion part 2 | Applied. Named as the second row reversed from opportunity to application at Freeze 3, with its submission date | Closed. No interview |
| PhrasIQ | Companion part 2, twice | Named as one of the eight rows the competing reconstruction dropped, and again as one of the fourteen interviews | Already listed above as a live process. The companion names it more prominently than the paper does |

## Platforms and vendors, not employers

These are named as tools rather than as counterparties, and they are already named throughout the
public repository.

| Name | Where | Note |
|---|---|---|
| LinkedIn | Paper sections 3.2, 5, Appendix B; companion throughout | Named as a source with 88 outcome-blind rows, as the origin of the Freeze 3 export, and in the Easy Apply explanation |
| Wellfound, Jobright, Ladders, Apply4Me | Appendix B only | Channel names in the taxonomy table |
| Greenhouse, Ashby, Lever, Workable | Not in the paper | In `views/latency_by_slice.csv` and `paper/RESULTS.md`. The paper deliberately publishes no per-ATS ranking, so no ATS is named in it |

## Named only in the companion piece

The companion names the eight companies the competing reconstruction dropped and this census keeps
with employer-side proof. Seven are not named in the paper at all, so publishing the companion
discloses more than publishing the paper alone.

| Company | What is disclosed | Risk |
|---|---|---|
| Lattice, Firstup | Applied, Tier A evidence, dropped by the other reconstruction | Closed. Discloses an application only, no outcome |
| Ava Labs, Fibr AI, 12100 Collective, Infisical, Classet | Same | Closed. Discloses an application only, no outcome |
| Fullsteam, Toast | Named as companies the other reconstruction missed entirely | Closed. Discloses an application only |

None of these discloses a rejection or an interview. PhrasIQ is the exception and is listed above,
because the companion names it as an interview.

## Named elsewhere in the repository but not in either piece

Listed so the pass is complete. Publishing the paper does not publish these, but the repository is
public and they are in it.

- **Opportunity register, converted to paid work**: Mixmax, Kivira Health, Mercor. These carry
  commercial relationships and compensation context. They are referenced in the paper only as
  "three engagements that converted to paid work", unnamed.
- **Opportunity register, adjudicated out of the census**: WorkOS via TopHire, Weave, Glytec, and
  others in `adjudication/ADJUDICATION.md`. The Hog and BX Studio were on this list until Freeze 3
  and are now applications, so both are named above instead.
- **Second-cycle pairs**: FOSSA and Attentive, named in `schema.md`, `paper/DEFECTS.md`, and
  `paper/NUMBERS.md`. Unnamed in the paper, which says only that two such pairs exist.
- **Latency outlier**: SentiLink, the single response at 140 days, named in
  `data_quality_report.md`. Unnamed in the paper.

## What the paper does not disclose about any named company

- No compensation, contract value, or offer terms.
- No individual's name. No counterparty is identified anywhere in the paper.
- No raw Gmail thread id or calendar event id. The committed corpus stores hashed pointers only.
- No interview content, question, or take-home material.

## Sign-off

- [ ] Still-open processes reviewed, and each is named, pseudonymized, or removed
- [ ] Closed processes reviewed
- [ ] jobmail.io reviewed specifically, since it is named as a data defect
- [ ] The Hog and BX Studio reviewed, since both are named as methodology examples as well as applications
- [ ] Companion-only names reviewed: the eight dropped-row companies plus Fullsteam and Toast
- [ ] Decided whether the companion publishes at all, and whether it publishes with or after the paper
- [ ] Confirmed no compensation or individual names entered the draft
- [ ] Approved for publication
