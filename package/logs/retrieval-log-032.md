# Retrieval log 032

Subject-supplied, `evidence_system = memory`. Same provenance warning as log 031: the artifacts are consistent with these facts but do not independently establish them.

## Fact: Heath Barnett initiated, via GTM Engineer School

**ENG-C is an opportunity register row. It does not enter the application census.**

This is the correct outcome under the separation rule set in `00-core.md`, and it is worth stating plainly what that rule just cost: the single largest paid outcome of the study window contributes nothing to the application conversion rate. That is the rule working, not failing. Counting it would have inflated the census conversion with work the census did not produce.

Corrected sequence:

| phase | dates | source |
|---|---|---|
| connection formed | before 2025-06-30 | GTM Engineer School |
| counterparty initiates | 2025-06-30 | artifact |
| informal interview process | 2025-06-30 to 2025-08-14, seven meetings, no role named in any | artifact, reclassified in log 031 |
| paused | during ENG-B | subject |
| resumed, "picked up where we left off" | 2025-08-28, format changes to GTME Sync | artifact plus subject |
| **two week contract trial** | from 2025-09-04 | subject |
| three month engagement | to approximately 2025-12-22 | artifact |

The 2025-09-04 service agreement is most likely the **trial** instrument, not the engagement instrument. The artifacts do not distinguish them. Do not assert which it is.

## The finding this produces

Two things in the window produced real outcomes. Neither came through an application.

| outcome | channel | register | would an ATS-based census see it? |
|---|---|---|---|
| Pin, two rounds plus take-home | GTM Cafe, formerly Clay Cafe | **application census** | No. No receipt exists. Recovered only by subject recall. |
| ENG-C, trial converting to a three month engagement | GTM Engineer School | **opportunity register** | No. Counterparty-initiated, no role ever named. |

**Both ran through GTM communities, and neither generates an ATS artifact.** One is the deepest application-sourced process of 2025; the other is the largest paid outcome of the window. A census built on receipt phrases and ATS domains scores both channels at zero.

That is the paper's strongest structural result so far, and it is not a story about effort or volume. It is a measurement result: **the instrument that captures applications is blind to the channel that produced the outcomes.** Everything in logs 021 to 030 about sweep exhaustiveness supports it, because the sweep was exhaustive and still found neither.

It also sharpens what the paper has to report. The application census conversion rate and the opportunity attribution register have to be reported side by side, and the Discussion has to say directly that the second is where the work came from. Reporting only the first would be accurate and misleading at once.

## ENG-B reclassified

The subject states Mobb.ai was **a job**, not contract work, and that he left. The register note is updated. This strengthens the Methods condition rather than weakening it: the window opens with the subject entering employment.

## Codebook changes now required

Three, all of which invalidate prior rows if made mid-harvest. Make them before the next pass.

1. `discovery_source`: add a value for GTM community channels. Two distinct communities are now evidenced (GTM Cafe, GTM Engineer School) and they behave differently, so consider whether one value or two.
2. `terminal_outcome`: add `converted_to_contract` (log 031).
3. Table 4 `notes`: ENG-C now carries internal structure, trial then engagement, which the schema has no field for. A note is sufficient; do not add a field for one row.

## Open

- **Was the two week trial paid separately from the engagement?** Invoice #001 timing would show it. Q12 is unexhausted and may carry it.
- Whether GTM Cafe and GTM Engineer School are one `discovery_source` value or two.
- The unexplained `eml_b041d204b81d` (log 027) is still unresolved.
- Q8 blocks 3 to 6. Block 3 remains the priority: 2025-11-28 to 2026-02-26, containing two of the three months with no evidenced engagement.
