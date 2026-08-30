# Retrieval log 049

**All 34 meetings classified.** Subject-supplied, with one artifact. The critical path from logs 043 to 047 is cleared.

## Final tally

| code | n |
|---|---|
| `VEND` | 13 |
| `VEND?` — blanket applied, low confidence | 12 |
| `COMM` | 5 |
| `OPP` | 3 |
| `INT` | 1 |
| **total** | **34** |

**Zero unclassified. Twelve carry a confidence flag** and are listed at the end.

## Finding 1: Hotglue is a YC Work at a Startup process, and that opens an unswept channel

Subject supplied a screenshot from **workatastartup.com**. Verbatim, from **Kevin Wright, Head of GTM & Partnerships, hotglue (S21)**:

> "Saw you just started in a new role, but if you're still poking around at other opportunities, **I'm interested in your background for a role we're currently hiring for: Business Development Manager.** ... Would offer to jump on a call sometime to chat."

**Kevin reached out first.** There is no application. `register = **opportunity**`, `discovery_source = **yc_wfs**` — a value the codebook already carries and which has never once been used.

The meeting followed on 2026-04-20 (`Keegan + Kevin: Hotglue BDM Role`, log 043). **The census interview count is unchanged at ≥13** — this raises the opportunity register instead. It was the only candidate in the set that could have moved the census number, and it did not.

### Stop condition 6 is live, and it is a whole instrument

`protocol.md` stop condition 6 reads: *"YC Work at a Startup dashboard inspected."* Never done. Log 002 recorded "YC Work at a Startup applied roles: no Gmail artifacts found" and the thread went cold.

**Now there is proof the channel carries real hiring conversations, and it has its own inbox that neither Gmail nor Calendar can see.**

This is a **fourth blind spot**, alongside phone calls (log 048), DM-arranged meetings (log 043), and calendar deletion (log 045). Every one has produced at least one real process. **The YC WFS inbox must be exported or screenshotted in full before any census total is stated.**

### One detail worth recording, not interpreting

Kevin's opening: *"Saw you just started in a new role."* The message is roughly five months before the screenshot, placing it near late March 2026 — inside the ENG-A window.

**How counterparties perceived the subject's employment status affects who approached him and what they offered.** That is a live variable in a study about a job search. The artifact does not say what they saw, and nothing here should assume. **Flagged for the subject.**

## Finding 2: Common Room was a GTM Cafe intro, not a vendor call

The subject corrects a guess I made in log 045, where Common Room sat in the "likely VEND" block. It was **a GTM Cafe connection and introduction — not an interview, not a job opportunity, and not a sales call.**

`COMM`, `discovery_source = community_gtm_cafe`.

**GTM Cafe now accounts for seven touches**: Every.to, Pearl, Great Question, Pin, Doug Shankman, Adam, and Common Room. The community channel keeps growing every time the corpus is pushed on.

**Note the direction of my error.** I guessed vendor from the domain. A GTM tooling company's employee met him through a community, and domain-based inference got it backwards. **Do not infer register from a counterparty's industry.**

## Finding 3: two Dougs, resolved

- **Doug Bell**, Cannonball GTM, and **Jordan Crawford**, Blueprint GTM — M04, 2025-06-17. *"Helping me with some stuff but not jobs."* `COMM`.
- **Doug Shankman**, Renoir — M18, 2025-10-27. Separate person, separate process.

Log 045 flagged the possible collision. **It is not one.** Both entities enter Table 3 exclusions with a reason, not silently.

## Finding 4: Doug Shankman's origin confirmed, classification still soft

`discovery_source = community_gtm_cafe`, subject-stated.

**The tension log 044 raised is not resolved.** The subject calls it an informal interview about Doug's CRO idea; the artifact reads *"time to workshop, connect, brainstorm,"* runs fifteen minutes, and Doug booked the page. Coded `OPP` on the subject's classification, `evidence_system = memory`. **If Doug was pitching, this is not an interview in any register** — and Results should not lean on it.

## Finding 5: Vee is a peer

M24 to M26, three meetings across five weeks. *"Is a peer of mine and you don't need to worry about."* `COMM`.

Log 045 read three touches with one counterparty as "a process shape, not a one-off." **That inference was wrong.** Recorded because the reasoning was sound and the conclusion was not: meeting frequency does not distinguish a hiring process from a friendship, and the corpus cannot tell them apart without the subject.

## The twelve low-confidence rows

The subject's *"the rest are vendors"* is applied to all remaining rows. Twelve are marked **`VEND?`** because a vendor reading conflicts with his own earlier testimony or with the artifacts:

| ref | counterparty | why it does not read as a vendor |
|---|---|---|
| M03 | Kellen Casebeer, The Deal Lab | You said he founded GTM Cafe and met with you as you geared up for Mobb.ai. Reads `COMM` |
| M08 | Matteo Tittarelli | Logs 035/036: the GTM Engineer School testimonials contact whose testimonial produced The Kiln. Reads `COMM` |
| M21 | George Rekouts, Disco | Log 030 filed it as a Clay Cafe networking connection, and the event is **Canceled**. Reads `COMM` |
| M27, M28 | Josh Peyton; Dom, Lucid Trust | Both inside the ENG-D window with the Josh Pappas network. Read `WORK` |
| M14 | Felipe Aranguiz | EmailBison is a vendor, but a **mixmax.com attendee is on the invite** during ENG-C. Could be `WORK` |
| M02, M07, M19 | Micah; Sarah Aitcheson; Hollie Maddux | gmail.com, no domain, no log. Nothing supports a vendor reading either way |
| M09, M10 | Mathew Joseph ×2 | **He booked your page twice.** Inbound booking is an unusual shape for a vendor |
| M12 | J. Sheen | Title: *"Kings of Collaboration: What if GTME / Growth Hackers solely focused on the flip-side... creators."* Reads like peer collaboration |

**None of these changes an interview count.** They change Table 3's exclusion reasons, which is what makes the census auditable. A row excluded as `VEND` when it was `COMM` is still excluded — but the exclusion reason would be wrong, and the exclusion log is published.

## Where the numbers now stand

- **Census interviews: ≥13.** Unchanged. Nothing in the 34 moved it.
- **Opportunity register: 13 processes reaching a real conversation** — Mixmax, Glytec, Starbridge, WorkOS, The Kiln, Opsin, Weave, Mercor, Adam, TrueBuilt, **Hotglue**, Doug Shankman, plus Pin's counterparty-initiated origin.
- **GTM Cafe: 7 touches.**
- **Excluded with a reason: 25 vendor or community meetings**, previously invisible to the record entirely.

**The two pipelines are now the same size.** Thirteen and thirteen. One is the residue of several hundred applications; the other came from communities, referrals, and inbound.

**Still not publishable.** The census denominator is missing the Gmail dedupe, the interview numerator is a floor with a phone-call gap, and the YC WFS channel is unswept.

## Open

1. **Export the YC Work at a Startup inbox.** Stop condition 6. A live channel with at least one real process.
2. Confirm or correct the twelve `VEND?` rows.
3. Was the subject showing a new role publicly in early 2026? Bears on how counterparties approached him.
4. Carried: Gmail dedupe join (needs [S1]); interview recomputation; PhrasIQ worked example; A5 and A6; the two extra mailboxes; Q3b, Q6, Q9, Q10, Q12.
5. **Five engagement descriptions. Still blocking Methods.**
