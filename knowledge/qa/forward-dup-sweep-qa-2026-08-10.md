# QA Report — forward-dup-sweep-2026-08-10

**Plan:** executable-341
**Step:** 2 (QA)
**Date:** 2026-08-11

## Deliverable Verification

**$ROOT:** `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/341`
**Plan path:** `/Users/marklehn/Developer/GitHub/bellows/.bellows-cache/executable-341.md.pristine`

Step-1 dev log reviewed at `knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md`. Output Receipt is complete — all tasks (A1–A7, C1–C4, D, E, F) recorded with raw output. Both Scope files claimed by Step 1 exist and carry the described changes.

| Deliverable | Expected | Status (✅/❌) | Evidence |
|---|---|---|---|
| `knowledge/FORWARD.md` | Rows 2, 10, 11 → `withdrawn`; row 6 → `closed-by-plan-341`; all other rows and non-data content unchanged | ✅ | Blob hash `66b318c2d274338419a8d6008e9cd81e1e7c75a2` matches dev log POST_EDIT_BLOB; all 8 verification rows PASS |
| `knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md` | Dev log with $ROOT, plan path, classification, blob hashes, derived N, baselines, 12-row receipt, Task-E control output | ✅ | File exists; all required fields present: CLEAN classification, PRE_EDIT_BLOB `0958b166...`, POST_EDIT_BLOB `66b318c2...`, N=341, row count 12, status dist `{'open': 12}`, dash-marker set `[3,4,5,6,7,8,11,12]`, non-data sha1 `e8743f9f...`, both comparator halves |

### Task Q0 — Re-pin

- `git log --oneline -- knowledge/FORWARD.md knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md | head -5`:
  ```
  ee7cd27 [341] Step 1 complete — FORWARD register void-row status sweep (rows 2, 6, 10, 11)
  d59a11e docs(forward): FORWARD row 12-12 for plan 340 (daemon-post-merge)
  d636e32 docs(forward): FORWARD row 11-11 for plan 339 (daemon-post-merge)
  9e42f3e docs(forward): FORWARD row 10-10 for plan 311 (daemon-post-merge)
  b00acf5 docs(forward): FORWARD row 9-9 for plan 311 (daemon-post-merge)
  ```
  $ROOT = `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/341`
- Latest commit touching scope files: `ee7cd27` (Step 1's commit). No newer commit.
- `git hash-object knowledge/FORWARD.md` = `66b318c2d274338419a8d6008e9cd81e1e7c75a2` — matches Step 1's POST_EDIT_BLOB.
- `git status --porcelain --` on both scope paths: empty. No uncommitted edits.

### Verification Table

| # | Claim | Status (✅/❌) | Evidence |
|---|---|---|---|
| 1 | Row count unchanged | ✅ | Live: 12, Step 1 baseline: 12. Equal. |
| 2 | Status distribution delta correct | ✅ | open: 12→8 (−4), withdrawn: 0→3 (+3), closed-by-plan-341: 0→1 (+1). N re-derived independently from plan path `executable-341.md.pristine` = 341; matches file value. No other status values changed. |
| 3 | Four cells by row number correct; untouched rows unchanged | ✅ | Row 2=`withdrawn`, 6=`closed-by-plan-341`, 10=`withdrawn`, 11=`withdrawn` — all byte-exact case-sensitive. Untouched rows (derived: {1,3,4,5,7,8,9,12}) all carry before-state status (`open`). |
| 4 | Column invariance — (a) data cells, (b) non-data block, (c) row-number join | ✅ | (a) Added/Item/Type/Plan-id byte-identical all 12 rows; Status differs for exactly {2,6,10,11}. (b) Non-data block sha1 before=after=`e8743f9fa83132bc51a69f3b3451489b21ba6d1e`. (c) Row-number sets identical: {1..12} both sides, 0 asymmetries. Before-state materialized via `git cat-file -p 0958b1660084343de0350ddb280f99ad207d84b8`. |
| 5 | Comparator control (both halves) | ✅ | Positive: mutated row 4 Item (`- ` → `X `), comparator reported row 4 and only row 4 as Item change + 4 expected Status changes. Negative: unmutated file, comparator reported 0 Item changes + 4 expected Status changes. |
| 6 | Dash markers survived | ✅ | Live set: [3,4,5,6,7,8,11,12] (8 rows). Step 1 baseline: [3,4,5,6,7,8,11,12]. Identical. |
| 7 | Rows 9 and 12 intact and open | ✅ | Row 9: status=`open`, sha1=`7ace3a3fc14f` (matches before). Row 12: status=`open`, sha1=`265c9f0a9ab4` (matches before). Row 12 item length (252) > row 11 item length (237). |
| 8 | Nothing else moved | ✅ | `git status --porcelain`: empty. Named paths absent: `lessons-forge.db`, `FORWARD.md.new`, `PROJECT_STATUS.md`, `agent-prompt-feedback.md`. No commit in this plan touched `PLANNER_TEMPLATE.md` or `RULE_20_SELF_CHECK_BLOCK.md`. |

## Evidence and Narrative

### Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/341/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/
Files verified: 3
```

### Raw Verification Output

All verification was performed using line-anchored Python with the parse contract: data row = `^\|\s*\d+\s*\|`; first cell via `strip().strip('|').split('|', 1)[0].strip()`; status via `rsplit`; all reads/writes with `encoding="utf-8"`. Before-state materialized via `git cat-file -p 0958b1660084343de0350ddb280f99ad207d84b8`.

Evidence files deposited:
- `forward-before.txt` — materialized before-state content with blob hash
- `forward-after.txt` — verification rows 1, 2, 3, 7 raw output
- `column-invariance.txt` — verification rows 4, 5, 6 raw output

## Output Receipt

### Deposits
- `lessons-forge/knowledge/qa/forward-dup-sweep-qa-2026-08-10.md`
- `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-before.txt`
- `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-after.txt`
- `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/column-invariance.txt`

## Ledger Updates

