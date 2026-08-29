# Extraction prompt

Use this when converting raw artifacts (ATS receipts, applied-list rows, tracker exports, calendar events) into rows under `knowledge/03-codebook.md`. Paste the artifact batch after the rules.

---

You are extracting structured records from job search artifacts into a research dataset. Accuracy beats coverage. An omitted row can be recovered later. A fabricated row poisons the census.

**Your output is rows, not prose.** Emit `applications`, `events`, and `exclusions` rows as tables using the exact field names and controlled vocabularies in the codebook, including `coder_id` as the first field of every row. Do not invent fields. Do not invent enum values. If a value does not fit an existing vocabulary term, emit the fallback listed for that field: `unknown` where the vocabulary includes it, and `none_observed` for `ats_system`. Describe the unmatched value in `notes`.

**Hard rules:**

1. Never infer a company or a role. If the receipt omits the role, `role_as_listed = unspecified`. If the employer is an intermediary and the client is unnamed, `underlying_employer = unknown`.
2. Never emit an application row from an interview or rejection artifact alone. An employer saying "thanks for interviewing" proves a process existed, not that a submission happened. Emit the event, flag the missing parent, and add an `exclusions` row with `exclusion_reason = unresolvable_identity` until a submission artifact appears.
3. Never merge two artifacts into one row silently. One artifact produces one event. Merging happens at the application level and must be stated in `notes` with both evidence IDs.
4. Every date gets a precision label. A relative stamp requires `date_capture`. An artifact-bounded date requires `date_evidence_anchor`. Never upgrade a relative date to exact.
5. A second receipt for the same company and role after a terminal outcome is a new cycle. Increment `cycle`, mint a new `application_id`, do not overwrite the first.
6. Assign `evidence_class = employer_artifact` only when the artifact came from the employer, their ATS, their recruiter, or the candidate's own sent mail. Applied-list rows and tracker rows are `platform_log`.
7. Assign `register = opportunity` when the process began with a referral, recruiter outreach, or a matching platform and no submission exists. These rows stay in the dataset and out of the census.
8. Anything sourced from recall rather than an artifact gets `evidence_system = memory`. Never disguise recall as evidence.
9. When two artifacts conflict on a date, company name, or title, emit the row with the better-evidenced value and record the conflict in `notes`. Do not average, do not pick silently.

**Before the tables, output a three-line header:**
- Artifacts processed: n
- Rows emitted: applications n, events n, exclusions n
- Conflicts and unresolved identities: a numbered list, or "none"

**After the tables, list every judgement call you made in one line each.** If you made none, say so. If you were tempted to fill a gap and did not, say what the gap was.
