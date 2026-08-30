# Freeze 2 platform files

Received 2026-08-29 ET. These files were not in Freeze 1.

| file | rows | date stamps | notes |
|---|---|---|---|
| `linkedin_applied_jobs_pages_1_to_10.csv` | 99 | relative (`3d ago` … `7mo ago`) | Pages 1 through 10 of the LinkedIn applied list. Page 10 has 10 rows, so a page 11 is not ruled out. The tracker does not label Easy Apply versus external ATS. Relative stamps were read on 2026-08-29. `date_capture = 2026-08-29`. Relative stamps are not upgraded to exact calendar dates. |
| `jobright_applications_log.csv` | 40 | exact ISO dates | Full tracker export matching the previously waived [S4] shape. Application Method is `Applied by Agent`, `Direct Apply`, `Manual/Unspecified`, or `Not stated`. |
| Ladders applied list | absent | | Still unmet. |

No Gmail thread IDs, calendar IDs, or third-party emails are in these files. They are committed as received.

## Freeze 4 copies (not Freeze 2 recodes)

| file | rows | notes |
|---|---|---|
| `linkedin-applications-in-window.csv` | 105 | Claude coding table from the 2026-08-30 care package. Minute timestamps. `dedupe_status=UNCHECKED` on arrival. Not the LinkedIn data download. Not independently minted into the census. |
| `linkedin-dedupe-resolution.csv` | 105 | Package adjudication of those 105 rows. Hint list. Independent match lives in `adjudication/package_linkedin_match.csv`. Third-party addresses redacted on commit. |

The care-package Jobright CSV is byte-identical to the Freeze 2 file above. The package LinkedIn pages 1 to 10 file is the same 99 rows with CRLF line endings. Neither replaces the Freeze 2 originals.

## What this freeze is not

This is not a LinkedIn data-download of every non-Easy Apply ATS submission. Capture recapture remains unmeasured. Ladders is still absent. Personal Gmail remainder and personal calendar are still absent.
