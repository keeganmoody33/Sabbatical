# Translation layer

An additive companion to this repository. Nothing outside this directory was changed, removed, or softened. The technical corpus, the protocol, the codebook, the coder CSVs, and the paper drafts are all exactly as they were.

This layer exists because the repository is written for itself. It is rigorous, and it is close to unreadable for the audience it needs: people who understand funnels and outcomes but have never written code, including people trying to break into GTM engineering who would read this as a case study of how a practitioner actually works.

## What is here

| File | Audience | Purpose |
|---|---|---|
| `AUDIT-FINDINGS.md` | internal | Sections 1 and 2. A file-by-file adversarial score and the aggregate gaps. This is a QA record, not a publication. |
| `SUBSTACK-DRAFT.md` | public | Sections 3 through 6. Reader leverage map, plain-language rewrite, extracted templates, closing takeaways. Paste-ready in order. |
| `templates/` | public | The five extracted templates as individual files, so each can be forked on its own. |

## Two notes on conventions

**Placeholder syntax.** The templates use `{{VARIABLE}}`. This repository does not use that syntax anywhere. Its own placeholder conventions are `company_slug|role_slug|c{n}`, `{application_id}|e{n}`, and `applications__{coder_id}.csv`. The `{{VARIABLE}}` form was chosen for the extracted templates because they are meant to leave this repository and be adapted elsewhere. Do not mistake it for existing repo syntax.

**House style.** Files in this directory follow the repository's stated conventions: no dashes as punctuation, "percent" spelled out, rates written as unreduced fractions such as `14/221`, dates in ISO form.

## Verification status

Every number quoted in this layer was recomputed from the CSVs rather than copied from the prose. Where a claim could not be verified from the repository alone, it is marked **UNVERIFIED, confirm with the author** rather than guessed.
