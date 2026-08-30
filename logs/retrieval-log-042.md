# Retrieval log 042

**Subject-supplied. `evidence_system = memory`, 2026-08-30.** Same provenance warning as logs 031 and 032: the artifacts are consistent with these facts but do not independently establish most of them. Named counterparties and origins are recall unless a prior log carries the artifact, and that is marked per row below.

This is the largest single addition to `discovery_source` in the project. **It also converts the paper's central structural result from a two-instance pattern into a counted one.**

## The register, as supplied

| process | counterparty | origin, as stated | artifact support |
|---|---|---|---|
| Glytec | **Clayton** (Clayton Maike, VP Sales) | LinkedIn DMs with CEO **Patrick** (Patrick F. Cua) | **confirmed**, logs 033, 034 |
| The Hog | **Hudson** | LinkedIn application | submission LI-054; process logs 021, 038 |
| Mixmax | **Heath** (Heath Barnett) | GTM Engineer School | **confirmed**, logs 031, 032 |
| Every.to | **Austin** | **GTM Cafe, `#jobsandopportunities`** — someone posted every.to job applications | counterparty confirmed log 020; **origin new** |
| PhrasIQ | **Eddie** | Wellfound, subject hedges "pretty sure" | Wellfound confirmed logs 006, 016 |
| Beautiful.ai | **Emily** | **Jobright.ai** | counterparty confirmed log 020; **origin new** |
| Pearl | **Chris** (2nd interview; 1st counterparty not recalled) | **Garrett Wolfe referral, GTM Cafe** | process confirmed logs 005, 009, 021; **origin new** |
| Great Question | **Harry** | **GTM Cafe `#jobsandopportunities`** | process confirmed logs 010, 011; **origin new** |
| Pin | **Erica Stacy Tarwater**, then **Conor Kline** | **GTM Cafe `#jobsandopportunities`** | **confirmed**, logs 024, 026, 030, 031, 032 |
| Mercor | **Claire** ×2, then **David Lou** | not stated | process confirmed logs 014, 015, 016, 021 |
| Dagster Labs | one interview | not stated | **confirmed**, log 040 |
| TrueBuilt | CEO | LinkedIn application, then req withdrawn | submission LI-067; **rest new** |
| **Doug Shankman** | Doug Shankman, plus his CRO | **GTM Cafe** | **entirely new. Absent from every log** |
| **Adam** (Andrewjeski) | Adam | **Clay Cafe, now GTM Cafe** | Calendly artifacts logs 024, 026 — **but excluded there** |
| Jorge Macias | — | GTM Engineer School, he was a TA | **confirmed**, log 023 |
| BCOFA | Mike Blaney | — | **confirmed**, log 028, ENG-A |
| Kellen Casebeer | — | founder of Clay Cafe → gtmcafe.com; also a GTM Engineer School TA | new |

## Finding 1: the community channel now has a numerator

`00-core.md` and log 032 established the structural claim — *the instrument that captures applications is blind to the channel that produced the outcomes* — on two instances, Pin and ENG-C. **It now rests on a counted set.**

**GTM Cafe** (formerly Clay Cafe), attributed by the subject: **Every.to, Pearl, Great Question, Pin, Doug Shankman, Adam** — six processes that reached a real conversation. Four of the six are traced to one Slack channel, `#jobsandopportunities`.

**GTM Engineer School**: Mixmax/ENG-C, The Kiln (log 036), plus the Jorge Macias and Kellen Casebeer relationships. Two processes, both counterparty-initiated, plus the community's TAs.

**Platform-sourced processes reaching an interview**: The Hog (LinkedIn), PhrasIQ (Wellfound), Beautiful.ai (Jobright), Dagster Labs (ATS-direct). **Four.**

Against a census heading toward 330-plus applications, roughly eight of the fifteen named processes that reached a real conversation came through two GTM communities, and only four came through the platforms the census is built on.

**This is the result the A3 codebook split exists to make measurable, and A3 is now vindicated on the data rather than on argument.** GTM Cafe and GTM Engineer School behave differently: the Cafe sources *applications and conversations* through a jobs channel; the School sources *relationships and counterparty-initiated approaches*. One value would have hidden that.

**Caveat, and it is not small.** These attributions are recall, not artifacts. `discovery_source` is unrecoverable from email for most rows — that is precisely why it was `unknown` — so recall is the only available source and the paper must say so. **Every community attribution in this log carries `evidence_system = memory` and must be excludable from the reproducible subset.** If the result survives only on memory-sourced attribution, Results must state that plainly. Report the figure twice: all sources, and artifact-confirmed only.

## Finding 2: TrueBuilt is reclassified. "No engagement" was wrong.

`02-current.md` recorded: *"Weave, TrueBuilt, and Luzmo produced no engagement."*

**What actually happened:** applied via LinkedIn (LI-067, 2026-06-21) → **the company took the requisition down** → the CEO saw a video the subject had sent → asked whether he would be open to **contract work** → **a project proposal was submitted.**

Not an interview. A proposal. Three consequences:

1. **The application row stands** with `terminal_outcome = role_paused_or_closed` — the req was withdrawn, which is what that value is for.
2. **A separate opportunity-register row is required** for the contract conversation, since it is a different process with a different counterparty relationship.
3. **This is a channel-crossing event in the opposite direction from Greg Reardon** (log 035, amendment A4). There, a network contact caused an ATS submission. Here, **an application that failed as an application converted into a contract prospect.** The codebook has no way to represent that an application row *spawned* an opportunity row.

The Greg Reardon fix was `referral_offered` in Table 2. This needs its own answer, and per design principle 1 it should be an event, not a field. **Proposed: `converted_to_opportunity` as an `event_type`**, with the resulting opportunity row's id in `notes`. Do not add this unilaterally — it is a fifth codebook amendment and the codebook is frozen at rev 2.

## Finding 3: Adam's exclusion is overturned

Log 026 filed Adam Andrewjeski as a "Clay Cafe/Slack connection" and log 024 recorded Calendly artifacts with **no company named**, so he was excluded. The subject now states: **"Adam interviewed me informally."**

The exclusion was correct on the artifacts and is wrong on the facts. This is the eleventh entry in the "exclusions overturned by artifact" pattern, except here it is overturned by **recall**, which is weaker and must be marked as such.

`register = opportunity`. `discovery_source = community_gtm_cafe`. No company is named in the artifacts and none is supplied, so `company_canonical` stays `unknown` and `underlying_employer` stays `unknown`. **A named row with an unknown employer is still auditable; a silently dropped row is not.**

## Finding 4: Mercor converted to contract, and that complicates the Discussion

The subject states: two interviews with Claire, then David Lou, **then secured contract.** That matches logs 014 and 015 — Instant Work Offer 2026-08-20, acceptance and contract activation 08-21, contract paused 08-29.

`terminal_outcome = converted_to_contract`. **This is the second row to carry the value introduced in amendment A1.**

Log 032 ruled: record the linkage in `notes`, "do not add a field for one row," and **"revisit if a second conversion appears."** It has appeared. The linkage decision is now formally triggered and must be re-taken — a `notes` string is no longer obviously sufficient once the value is plural and Results needs to count conversions.

**The harder problem.** Log 032's headline finding reads: *"Two things in the window produced real outcomes. Neither came through an application."* Mercor's own artifacts are **"Application Submitted" receipts**, and the query manifest lists Mercor under *exclusions overturned by artifact* — meaning it was moved **into** the application census.

If Mercor is an application-register row that converted to a contract, **that sentence is falsified as written.** The Discussion's sharpest claim would need to become "two of three," or Mercor's register assignment would need re-examination against `marketplace_profile_submission`, which the codebook provides precisely for platforms of this shape.

**Do not resolve this here.** It is a register question with a direct effect on the paper's strongest claim, and it deserves its own adjudication with the artifacts open.

## Finding 5: confirmations, which are worth as much as the corrections

- **Dagster Labs, one interview.** The subject independently confirms log 040 without having been shown it. The interview-count error stands confirmed from two directions.
- **Pin's GTM Cafe origin** is confirmed, upgrading log 032's attribution from inference to stated.
- **Jorge Macias.** Log 023 excluded the nine gtm-engineering.io invitations as "a standing meeting series, not an interview." The subject confirms: mentorship, no concrete job opportunity, met as a TA in GTM Engineer School, later a friendship. **The exclusion holds and now has a reason on the record rather than only an inference.**
- **BCOFA.** Log 028 and `04-engagements.md` rev 2 recorded ENG-A as ending on a stall, not a completion. The subject supplies the reason: **"fizzled out because they did not have money."** He states he worked on it for a period of time. **He does not state whether he was paid**, so `compensation_evidenced = no_artifact_retrieved` stands unchanged and must not be read as unpaid.
- **Clay Cafe and GTM Cafe are one entity, renamed to gtmcafe.com.** Confirms log 032. `community_gtm_cafe` carries **`Clay Cafe` as its only alias.** **`Clay Club` is a separate entity** and must not be matched to it; the retriever conflated the two on first pass and the subject corrected it. The "Clay Club Atlanta" event in log 030 stands as its own community-context row.

## Conflicts to adjudicate, not resolved here

1. **PhrasIQ: two interviews or three?** The subject states **two**, the final one an hour long. `03-codebook.md`'s worked example specifies **three event rows, "rounds 1 through 3,"** with Eddie as counterparty and calendar IDs as evidence. The codebook's own example is now contradicted by the subject. One of them is wrong, and the calendar IDs can settle it.
2. **Pearl: how many interviews?** The subject states two and recalls only the second counterparty, Chris. Logs 005, 009 and 021 carry scheduling artifacts on 2026-04-30, 05-04, 05-11 (twice) and 05-17. **Reminders are not interviews** — that is the Orchestry lesson from log 041 — so the event count must be built from what was held, not from what was scheduled.
3. **Mercor's register.** See Finding 4.

## Codebook consequences

Rev 2 is frozen and coder 1 has not run, so these are cheap now and expensive later — the same argument as `claude/05-codebook-amendments-r1.md`.

1. **`community_gtm_cafe` alias: `Clay Cafe` only.** Not a vocabulary change, a matching rule. **`Clay Club` is explicitly NOT an alias** — different entity, corrected by the subject.
2. **A5, proposed: `event_type += converted_to_opportunity`** for the TrueBuilt shape.
3. **A1's linkage ruling is triggered** by Mercor as a second conversion. Re-take the decision.
4. **Channel-level attribution.** Four processes trace to one Slack channel, `#jobsandopportunities`. There is no field for a sub-channel and there should not be one for a single community. Put it in `notes`, consistently phrased, so it stays greppable.

## Open

1. Adjudicate PhrasIQ's round count against the calendar IDs.
2. Rebuild Pearl's event list from held interviews, not reminders.
3. Adjudicate Mercor's register, then re-word or defend the Discussion's "neither came through an application."
4. Decide A5 and re-take A1's linkage.
5. Create the Doug Shankman opportunity row. No artifacts exist anywhere; it is memory-only, like Pin's origin.
6. Recompute the interview count from Table 2 events — now with named counterparties for eleven processes, which makes the recomputation materially easier.
7. **Five engagement descriptions. Still blocking Methods.**
