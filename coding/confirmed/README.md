# Subject-confirmed overlay

Coder `confirmed`. 2026-08-30.

This layer does **not** recode Freeze 1 Gmail, Freeze 2 platform CSVs, or Freeze 3 extracts. It records what the subject confirmed after those freezes: recall tagged `evidence_system = memory`, origins, money, and two opportunity rows that had calendar meetings but no named employer application.

Join to frozen rows on `application_id`. Memory events may attach to an existing freeze3 or cursor parent.

Two overlay application rows are minted here and not copied into `adjudication/applications__full_census.csv`:

- `unknown|informal-adam-andrewjeski|c1`
- `unknown|cro-idea-doug-shankman|c1`

`company_canonical` stays `unknown`. They are opportunity, not applications.

See `adjudication/ORIGINS.md` for the paper-facing tally. Retrieval log 056.
