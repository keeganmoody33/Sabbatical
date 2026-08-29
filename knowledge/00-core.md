<!-- kit-meta
file: 00-core.md
tier: 0 (durable)
created: 2026-08-29 13:37 ET
updated: 2026-08-29 13:37 ET
review-by: 2027-08-29
sources: [S1] [S2] [S6]
-->

# Core

How Keegan works, and the standard this paper is held to. Changes rarely and only on purpose.

## Who

Keegan Moody. GTM engineer and product builder, Atlanta, operating independently through lecturesfrom LLC. Background in biochemistry and molecular biology research, including EPA-published work on mercury detection. He applies hypothesis-testing discipline to go-to-market systems, and he is applying it here to his own job search record. [S6]

He is the subject of the dataset and the author of the paper. That dual role is a declared limitation, handled in Methods.

## Voice and writing

- Ship first. A complete rough section beats a polished fragment. [S6]
- No fabricated personal context. If it did not happen, it does not go in. [S6]
- No dashes in published copy. [S6]
- Voice over polish. First person, plain sentences, his cadence. [S6]
- Specificity over adjectives. "247 confirmed applications, 88 to 93 percent census completeness" beats "a lot of applications". [S6]
- Reject: consultant register, LinkedIn-inspirational register, hedging that hides a number.
- Accept: a number with its uncertainty attached, a named company, a verbatim rejection line.

## Publication standard

This is written as a paper, not a blog post wearing a lab coat. That means:

- Every quantity carries an evidence tier and a date-precision label.
- Methods must be reproducible by a stranger holding the same exports.
- Limitations are stated in the paper, not buried in an appendix.
- The count is presented as a measurement with error, not a fact.

## Counting rules

These are the rules of the census. They do not expire. [S2 A_Verdict, rules 1 to 8]

1. Unit of analysis: `normalized_company + normalized_role + application_cycle`.
2. Same company, materially different title, equals two applications. Example: Tractian Sales Engineer and Tractian Senior GTM Engineer are two.
3. Same company, same title, plus reminder and rejection threads, equals one application.
4. A new receipt after a prior rejection for the same company and title is a new cycle and counts again. Example: FOSSA (2026-04-22, 2026-05-21) and Attentive (2026-06-22, 2026-07-15). [S1 Master Ledger]
5. Marketplace: titled role submissions count. Generic profile visibility does not.
6. Aggregator sends (Apply4Me, agent-applied) count only when the receipt says the application was sent, or a matching ATS receipt exists.
7. A recruiter saying "thank you for applying" counts for that client role.
8. Never invent a company or a title. A receipt that omits the role is recorded as Unspecified, not guessed.
9. Window is inclusive and stated in America/New_York.

## Evidence tiers

- **Tier A, definitive**: ATS, employer, or recruiter message using explicit application language. Received, submitted successfully, thank you for applying.
- **Tier B, corroborated**: application language present but employer or title partially missing, resolved by a second artifact.
- **Tier C, self-logged**: a tracker or applied-list row with no employer-side artifact. LinkedIn applied rows sit here unless an ATS receipt corroborates them.
- **Attempted, excluded**: started and never submitted. Kept in a visible log, never in the total.

Confidence in the ledger (High / Medium) is the item-level judgement. Census completeness is the separate, population-level judgement. Report both.

## The two-register rule

The single most important structural decision in this work. [S1 Opportunity Attribution]

- **Application census**: roles Keegan submitted himself. This is the denominator for any funnel rate.
- **Opportunity attribution register**: referrals, recruiter-initiated processes, matching-platform contracts, consulting prospects. These produced real interviews and real money. They never enter the application census, because putting them there inflates the conversion rate with outcomes that did not come from applying.

The reasoning outlives the specific entities: a job search has two independent pipelines, and mixing them makes both unmeasurable.

## Vocabulary

- **Census**: the reconciled set of confirmed applications.
- **Floor**: a count known to be an undercount. Prior floors are superseded, not deleted.
- **Cycle**: one application to one req. A second cycle is a genuine re-application after the first closed.
- **Dedupe key**: the normalized string used to collapse duplicates across sources.
- **Date precision**: exact, relative display, unknown with evidence date, or latest bound.
- **Role lane**: one mutually exclusive category per application. Modifiers describe flavor within the lane.
- **Attempted**: started, never submitted. Not an application.

## Quality bar

Output is good here when a skeptical reader who dislikes Keegan could not find a number to attack. It fails when it states a total without a completeness estimate, when it lets an interview from a referral count against applications, or when it presents a monthly curve without saying which dates were approximated.
