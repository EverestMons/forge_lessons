# QA Report — ingest-heading-key-corrective-2026-08-21

**Plan:** 500 (corrective to halted-499)
**Date:** 2026-08-21
**Role:** QA
**Step:** 2

## 1. Full Test Suite

```
63 passed in 0.15s
```

All 63 tests passed, including the 8 plan-499/500 heading-key tests (`test_annotated_heading_matches_existing_row`, `test_key_heading_preserves_tag_markers`, `test_heading_with_markers_correct_heading_title`, `test_key_heading_preserves_internal_double_spacing`, `test_key_heading_identity_fixture`, `test_key_heading_annotated_matches_unannotated`, `test_key_heading_tag_survives_status_target_removed`, `test_key_heading_marker_start_or_middle_no_doubled_space`). Zero failures, zero errors.

Raw output: `evidence/ingest-heading-key-corrective-2026-08-21/pytest_full.txt`

## 2. Controlled A/B Ingest Canary

Both arms ran against fresh `cp` copies of the live corpus DB in a TMP directory outside the repo. `source_file="LESSONS.md"` passed as the key, not as a filesystem path.

**ARM A (control):** unannotated LESSONS.md, 324 parsed entries, inserted=11, unchanged=313, updated=0.
**ARM B (treatment):** 3 headings annotated with `[status: learned] [target: PLANNER_TEMPLATE.md]`, 324 parsed entries, inserted=11, unchanged=313, updated=0.

Annotated headings:
1. `2026-06-02: "Known-good" plan headers have a freshness axis...`
2. `2026-06-02: Never edit a project's working tree while a Bellows plan is in-flight...`
3. `2026-06-02: A QA "full suite passes / N passing" headline is the least independently-verifiable...`

Raw output: `evidence/ingest-heading-key-corrective-2026-08-21/canary.txt`

## 3. Live Corpus DB Integrity

SHA256 before: `8317f05483a2be2cbfbaeedbe0786ede7e28f33488e0824a16dd2319d09cc777`
SHA256 after:  `8317f05483a2be2cbfbaeedbe0786ede7e28f33488e0824a16dd2319d09cc777`

Byte-identical. No writes to the live corpus.

## Verification Table

| # | Assertion | Expected | Observed | Status |
|---|-----------|----------|----------|--------|
| i | `arm_B.inserted == arm_A.inserted` | delta = 0 | arm_A=11, arm_B=11, delta=0 | ✅ |
| ii | `arm_A.inserted == (parsed - exact_matches)` | 324 - 313 = 11 | inserted=11 | ✅ |
| ii-signal | Authoring-time sanity (expected ~11) | 11 | 11 | ✅ |
| iii | `stale_proposals_marked == 0` both arms | 0, 0 | arm_A=0, arm_B=0 | ✅ |
| iv | Annotated entries resolve to original row ids | 3/3 match | id 94, 95, 96 all match | ✅ |
| v | Identity: `_key_heading(h) == h` all stored headings | 381/381 | 381/381 | ✅ |
| suite | Full pytest suite | 63 passed | 63 passed in 0.15s | ✅ |
| db | Live corpus DB byte-identical | sha256 match | sha256 match | ✅ |

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/500/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/
Files verified: 2
```

**PASSED — SELF-CHECK PASSED**
