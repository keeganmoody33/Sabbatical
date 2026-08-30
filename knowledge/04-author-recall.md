# Author recall, 2026-08-30

Statements the author made about interviews and origins after seeing the analysis. Recorded here
because they are decision-relevant. **Nothing in this file is written into a structured census
field**, and nothing here has moved a published figure.

Structured companion: `knowledge/author_recall__2026-08-30.csv`. Personal names are `per_` pointers
on the same one-way convention as everything else in this repository. No reverse map is committed.

No dashes are used as punctuation in this file.

## Why this is quarantined rather than adopted

`prompts/extraction.md` rule 8 forbids writing recall into a structured field, and the
`knowledge/protocol.md` changelog already carries one case where this rule was tested: the Weave
2026 interview, corrected from author recall after the analysis was seen, and disclosed as "the
failure mode blind coding exists to prevent". Recall arriving **after** the author has read the
results is the single most contaminated evidence class this study can receive. It is not worthless.
It is not a census input.

So this file exists to do three things: record the claims verbatim in structure, say exactly what
each one would change, and name the artifact that would settle it.

## Two claims verified against committed files before anything else

The author's recall reproduces redacted values in a file the author has not read.

| Author's statement | Pointer it hashes to | Where that pointer already sits |
|---|---|---|
| One interview at Hotglue with a named person | `per_8c8479ce1bf3` | Challenger register, Hotglue row, verbatim |
| Two interviews at PhrasIQ with a named person | `per_3b9d8298f1b5` | Challenger register, PhrasIQ row, verbatim |

The challenger workbook was produced independently and its extracts here are redacted, so a name
supplied from memory landing on the same hash is not something recall can fake. This does not make
the rest of the file evidence. It does raise the prior on it considerably, and it is the reason the
claims below are treated as a retrieval plan rather than as noise.

## The finding underneath all of it

The census carries `submission_channel` on 213 of 223 rows and `discovery_source = unknown` on 206.
The paper published that as a null result. The author's recall shows **why** the field is empty, and
the reason is worse than "it was not logged".

An ATS confirmation email records that a form was submitted. It records nothing about how the
opportunity was found. The two are different questions and the corpus can only ever see the first.

| Company | `submission_channel` in census | Origin per author recall |
|---|---|---|
| Every | unknown | GTM Cafe Slack `#jobsandopportunities` |
| Great Question | ats_direct | GTM Cafe Slack `#jobsandopportunities` |
| Pearl | ats_direct | GTM Cafe Slack post, then a referral from a contact connected through agency work |
| PhrasIQ | wellfound_apply | Wellfound |

Great Question and Pearl are coded `ats_direct` and that coding is **correct**. The applicant did
submit through the employer's ATS. The origin was a Slack channel, and no artifact in this corpus
could have shown that, because the receipt is byte-identical whether the job was found on a job
board or from a friend.

**Origin is not missing at random. It is unobservable in principle from the artifact class this
study is built on, and it is missing hardest exactly where the outcomes concentrate.** That is a
stronger and more useful claim than the one currently in the paper, and it does not depend on
believing any specific recall claim, only on the structural point about what a receipt contains.

## Interviews the census does not count

Seven processes the author reports reaching interview that sit outside the 223 denominator, either
in the opportunity register or absent from the corpus entirely.

| Company | Rounds claimed | Origin claimed | Status here |
|---|---|---|---|
| Glytec | 1 | Inbound LinkedIn DM from the CEO citing a referral | Opportunity register, interview already coded |
| Mercor | 2 | Self-submitted through Mercor's internal job board | Opportunity register, interviews already coded |
| The Kiln | 2 | Inbound LinkedIn DM, second round with the founder | **Absent entirely** |
| Pinn | 2 | GTM Cafe Slack `#jobsandopportunities` | **Absent entirely**, held by the challenger |
| Opsin Security | 2 | Intermediary recruiter, then the CEO | **Absent entirely** |
| Hotglue | 1 | Inbound on YC Work at a Startup | **Absent entirely**, unmet stop condition 6 |
| Mixmax | 1 | GTM Engineering School relationship | **Absent entirely**, led to a contract |

Not one of these is a cold application through an ATS. Every one arrived through a channel that
generates no employer email receipt: a LinkedIn DM, a Slack channel, a school network, a platform's
internal message system. That is the same structural blindness as above, now visible in the
outcomes rather than in a missing field.

**The Kiln is the sharpest case.** It appears in no census row, no opportunity row, and no
challenger record. Two independent reconstructions of these fifteen months both missed a process
that reached a founder interview, because both were built from email and neither could see a
LinkedIn DM thread.

## Interviews the census counts that the author disputes

These matter more than the additions, because they subtract from a published figure.

| Company | Author | What the coders did | Reading |
|---|---|---|---|
| Hypergen | "I dropped the ball. I never scheduled a date. 0 interviews" | bravo `employer_ack`, cursor `hiring_manager_interview`, on an interview **invitation** | Recall agrees with the blind coder that adjudication did not follow |
| RevSpring | "not sure" | Both coders `recruiter_screen`, from a "Recruiter Screen **Request**" | A request is not a completed round |
| TestGorilla | doubted | Both coders `recruiter_screen`, from a Teamtailor recruiter **intro** | May be an automated introduction |
| jobmail.io | doubted | cursor only `recruiter_screen`, no blind second reading | Already an open defect: the derived interview contradicts a stored `rejected_no_interview` |

There is one pattern across all four: **an invitation, a request, or an intro was coded as an
interview.** The interview derivation counts an event type, and for these four the underlying
artifact is an offer to meet rather than a record of having met.

Hypergen is the strongest of the four and is not recall-only. Bravo, blind, coded it `employer_ack`.
Cursor coded it an interview. Adjudication took cursor. The author's recall now independently agrees
with bravo. That is the same shape as the Weave correction, which was accepted on the same
reasoning: the correction moves the census toward the blind coder's judgement rather than away
from it.

If all four fall, interviewed applications go 14 to 10 and the headline rate goes 14/223 to 10/223.
If only Hypergen falls, 14 to 13.

## What this does not establish

- **No round counts change.** The author reports two rounds at Pearl, PhrasIQ and Hologram where
  the census codes one. The published metric is interviewed applications, not rounds, so this
  changes nothing downstream and is recorded only for completeness.
- **Mercor's register is not resolved.** The author states the Mercor rows were self-submissions
  through an account they created, which would make them application register rather than
  opportunity. Six Mercor rows already sit in the census as applications with submission receipts.
  The two in the opportunity register are the ones the challenger also disputes. A Mercor account
  export would settle it.
- **Nothing here is a completeness estimate.** Two reconstructions missed The Kiln. That is
  evidence that the union of both is still short, not a basis for a percentage.

## The retrieval this makes possible

The origins named above are not lost. They are **unretrieved**, which is a different word, and the
protocol's stop conditions are the place that distinction gets recorded.

| Source | What it would settle | Stop condition |
|---|---|---|
| LinkedIn DM threads | Glytec, The Kiln, and the inbound origin class generally | Currently unmet |
| GTM Cafe Slack `#jobsandopportunities` | Every, Great Question, Pearl, Pinn | Not previously named as a source at all |
| YC Work at a Startup messages | Hotglue | Stop condition 6, unmet |
| Mercor account export | The Mercor register question | Not previously named |
| Wellfound | PhrasIQ | Not previously named |

The GTM Cafe Slack channel is the notable one. It was never in the protocol's source list, and on
this account it is the single origin behind at least four processes that reached interview. A study
that set out to measure which channels convert never authorized retrieval from the channel that
appears to convert best.

## Open decisions for the author

1. **Hypergen.** Correct to 0 interviews on the strength of bravo's blind coding plus recall, taking
   the headline to 13/223? This is the only one of the four disputes with independent blind support.
2. **RevSpring, TestGorilla, jobmail.io.** Re-examine the three underlying artifacts against a
   stricter rule, that an invitation or request is not an interview? This is a coding-rule question,
   not a recall question, and it can be answered from artifacts already in the corpus.
3. **Retrieval.** Authorize any of the five sources above? Each is a protocol amendment and a new
   freeze, not an edit.
4. **The Kiln.** Record as a known-missing process with no artifact, the same treatment AnyInt AI
   already has in `knowledge/02-current.md`?

None of these has been actioned. The census remains 223 with 14 interviews.
