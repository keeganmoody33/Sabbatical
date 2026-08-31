# Did the interview happen? Re-reading all fourteen against the artifacts

Prompted by the author disputing four of the fourteen. The dispute is resolved here **from the
frozen corpus**, not from recall, because the author's own argument is the reason to do it that way:
five hundred applications cannot be recalled individually, so recall is the wrong instrument for
this flag in either direction.

Nothing here has been applied. The census still reports 14. No dashes are used as punctuation.

## The rule the corpus already contains

The interview derivation counts an `event_type`. That was the defect. `recruiter_screen` and
`hiring_manager_interview` are assigned to the artifact that **proposes** a conversation just as
readily as to one that **records** one, and an invitation and a completed round are different facts.

Reading all fourteen threads, a completed interview leaves at least one of five marks. None is
subtle and all five are machine-detectable:

1. A scheduling confirmation or a calendar reminder naming an interviewer or a meeting tool
2. A post-interview decline, phrased as declined **after** a process
3. A candidate-experience survey, which employers send only after a round
4. A `SENT` message from the applicant referencing the conversation
5. A subsequent stage that presupposes the first, such as a take-home or a named second round

An interview **invitation**, a screen **request**, a recruiter **intro**, or an assessment
invitation is none of these. It is an offer to meet.

## The fourteen

| Company | Coders | Evidence found | Verdict |
|---|---|---|---|
| Beautiful.ai | both | Two message thread on the application update, includes `SENT` | **holds** |
| Dagster Labs | both | `SENT`: "thank you for taking the time to chat with me" | **holds** |
| Every.to | both | "I'd love to chat", **call booked** | **holds** |
| Great Question | both | Two interview reminders, Google Meet, **post-interview decline**, candidate survey | **holds** |
| HartleyCo | cursor | Recruiter call arranged within hours; the Bluejay role **declined after process** | **holds** |
| Hologram | both | Reminders for **two named rounds**, a preliminary screening call and a cross-functional interview, plus a candidate survey and `SENT` | **holds, and two rounds** |
| Orchestry | both | **Declined after interview process**, includes `SENT` | **holds** |
| Pearl | both | "Interview @ Pearl", scheduling initiated and confirmed | **holds** |
| PhrasIQ | both | A **completed Discovery Session** referenced on 2026-04-06, with a GTM System Deep Dive proposed as the next stage. The calendar independently carries `Discovery \| Keegan Moody<>PhrasIQ` on 2026-04-02 | **holds, and two rounds** |
| The Hog | both | Invitation 06-15, **interview 06-16**, product signup the same day, a roughly four hour take-home 06-18, credits grant 06-20 | **holds** |
| **Hypergen** | cursor only | An interview **invitation** dated 2026-04-14 and nothing after it | **does not hold** |
| **TestGorilla** | both | An assessment invitation, a recruiter **intro**, and a recruiter **update**. No scheduling, no completion | **does not hold** |
| **RevSpring** | both | A screen **request** dated 2026-06-10, two receipts, and a role message. No scheduling, no completion | **does not hold** |
| **jobmail.io** | cursor only | A decline saying the requested steps "were completed through" a named person | **ambiguous** |

## Hypergen is the clearest, and it was flagged at retrieval time

`artifacts/gmail/retrieval-log-006.md` says it outright:

> Hypergen thread carries an interview invitation dated 2026-04-14 from `people@hypergen.io`,
> replying to the March 11 application confirmation. The prior ledger records Hypergen as a receipt
> only, **and the Interviews sheet does not list Hypergen.**

Four independent sources agree there was no interview: the artifact is an invitation, the retriever
said so at capture, bravo blind-coded it `employer_ack`, and the prior 247 row ledger's Interviews
sheet omits it. Cursor's `hiring_manager_interview` is the lone outlier and adjudication took it.
The author's recall is the fifth source and the least important of the five.

## jobmail.io stays ambiguous, and should

The decline says the requested steps were completed. That is more than a receipt and less than a
recorded conversation, and an asynchronous screening stage would produce the same sentence. It is
also the row already carrying an open defect: a derived interview contradicting a stored
`rejected_no_interview`, from one coder with no blind second reading. It is left unresolved rather
than pushed either way.

## What adopting this would do

| | Now | Three fall | Four fall |
|---|---|---|---|
| Interviewed applications | 14 | 11 | 10 |
| Rate | 14/223 | 11/223 | 10/223 |

The three that clearly do not hold are Hypergen, TestGorilla and RevSpring. The fourth is
jobmail.io, and on the evidence it should stay in unless a reader of the underlying thread decides
otherwise.

Round counts also move on two rows that hold: Hologram and PhrasIQ each show two named stages where
the census codes one. The published metric is interviewed applications rather than rounds, so this
changes no headline figure, but it does mean the corpus supports the author's round counts on both.

## Why this is a coding defect and not a recall correction

Every fact above is in the frozen corpus and was there before the author said anything. It was
missed because the derivation asks what `event_type` a coder assigned, and the coders had no rule
telling them an invitation is not a round. Two coders independently made the same call on
TestGorilla and RevSpring, so this is not one coder being careless. It is a **missing rule**, which
is the kind of defect a codebook is supposed to prevent and this one did not.

That is the honest framing for the paper. The author's recall pointed at the four rows. The
artifacts decided them, and they would have decided them the same way with no author involved.

## Two observations recorded in passing

- The author names the HartleyCo recruiter as one person; the retrieval log names another. HartleyCo
  is the firm and the log names the individual, so this is most likely firm and person conflated. It
  changes nothing and is a fair reminder that recall is unreliable on names even when reliable on
  events.
- `artifacts/gmail/*.md` carries **personal names in cleartext** in its retriever notes, while the
  same corpus redacts sender addresses to `eml_` pointers. That is an inconsistency in the existing
  redaction, not something introduced here. The corpus is frozen so it is reported rather than
  edited, and it is a live disclosure question before anything is published.
