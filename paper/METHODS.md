# Methods

Window: 2025-06-01 to 2026-08-29, America/New_York, inclusive. Fifteen months. Prior audits searched 2025-08-25 forward, so June 2025 through early November 2025 was unharvested rather than empty.

Unit of analysis: `company_canonical + role_as_listed + cycle`.

Two registers stay separate. Application census is roles submitted by the applicant. Opportunity attribution (referrals, recruiter-initiated processes, matching-platform contracts) stays out of the denominator.

Evidence is harvested as raw artifacts, then coded independently. Retrieval logs are the Gmail and Calendar extracts. Committed logs store hashed evidence pointers rather than raw Gmail thread IDs, calendar event IDs, or applicant account IDs. Coders do not see each other's rows. Interviewed-ness is derived from the events table, never stored on the application row.

Date precision is a field. Monthly series use only `date_precision = exact`. Relative LinkedIn stamps are not upgraded to calendar dates.

## Completeness

95 percent completeness is a goal, not a verified claim. The intended estimator is two-source capture recapture, restricted to LinkedIn rows submitted through an external ATS. Naive Lincoln Petersen on Easy Apply versus ATS mail is invalid because those sources are near-disjoint by construction.

This freeze has no LinkedIn export, so the overlap stratum is unmeasured. The paper reports that gap instead of a completeness percentage.

## Limitations

Subject and author are the same person. Coding is independent across models, not a human gold standard. The personal Gmail calendar was not reachable in the environment that froze this corpus. Platform trackers (LinkedIn full dump, Ladders, Jobright, YC) were not in the artifact set.
