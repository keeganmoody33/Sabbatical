# Adjudication

Run after at least two of `coding/alpha`, `coding/bravo`, and `coding/cursor` exist. Do not edit coder files.

```bash
python3 adjudication/compare_coders.py
python3 adjudication/adjudicate.py
python3 adjudication/derive_metrics.py
```

Writes `adjudication/PRE-ADJUDICATION.md`, `adjudication/disagreements.csv`, and `adjudication/applications__adjudicated.csv`.

## Include/exclude

An application is included when `register = application`. Agreement is on the binary: in the application census vs excluded or opportunity.

Match keys: lowercase `company_canonical` + `|` + lowercase `role_as_listed` + `|c` + `cycle`. If cycle is empty, treat as 1.

## role_lane

Cohen's kappa on the intersection of application_ids both coded, using `role_lane`.

## Capture-recapture

Restricted to the stratum where both LinkedIn and ATS mail could observe the same application: LinkedIn rows submitted through an external ATS, not Easy Apply.

Freeze 2 has LinkedIn pages 1 to 10 without that channel label. Do not run naive Lincoln-Petersen. Report the method and that the overlap stratum is unmeasured.

## Defects

- WorkOS: artifacts in log 020 (TopHire). Register is adjudicated, not assumed.
- 212-to-163: workbooks absent. Still undocumented.
- Dedupe key: `company|role|cycle` as coded in application_id.

## Subject-confirmed overlay (not a fourth independent coder)

Coder `confirmed` records recall and origins after Freeze 1 through Freeze 4. It does not recode Freeze 1 Gmail or Freeze 2 platform files. `adjudication/derive_metrics.py` does not read it, so 14/298 cannot move by accident.

- Paper-facing tally: `adjudication/ORIGINS.md`
- Flags for the paper: `adjudication/origins__subject_confirmed.csv`
- Overlay rows: `coding/confirmed/`
- Retrieval: `logs/retrieval-log-056.md`

Filter the origins CSV. Do not union opportunity, employment, consulting, or communal rows into the application census.
