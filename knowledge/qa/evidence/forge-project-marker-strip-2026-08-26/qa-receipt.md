# QA Receipt — forge-project-marker-strip-2026-08-26

**Plan:** `[project:]` heading markers stripped from ingest identity keys
**CAPTURE_COMMIT:** `4317abb`
**Date:** 2026-08-26
**Step:** 2 (QA)

## Verification

| Item | Check | Result | Status |
|------|-------|--------|--------|
| 1 | Full pytest suite — 65 passed, 0 failed | 65 passed in 0.15s | ✅ |
| 2a | `status\|target\|project` count in committed lessons_forge.py == 1 | 1 | ✅ |
| 2b | `status\|target):` count in committed lessons_forge.py == 0 | 0 | ✅ |
| 2c | `test_key_heading_strips_project_marker` count in committed test file == 1 | 1 | ✅ |
| 2d | `test_key_heading_strips_project_with_status_and_target` count in committed test file == 1 | 1 | ✅ |
| 2e | cmp committed vs live src/lessons_forge.py == 0 | exit 0 | ✅ |
| 2f | cmp committed vs live src/test_lessons_forge.py == 0 | exit 0 | ✅ |
| 3a | numstat exactly 3 files | 3 files (knowledge/dev-logs/..., src/lessons_forge.py, src/test_lessons_forge.py) | ✅ |
| 3b | toplevel printed | /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/549 | ✅ |
| 3c | reflog -n 4 — 0 amends | 0 amends | ✅ |

## Evidence Files

- `pytest_full.txt` — full pytest suite output
- `probes-raw.txt` — committed-extraction probe results
- `qa-receipt.md` — this file

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/
Files verified: 3
