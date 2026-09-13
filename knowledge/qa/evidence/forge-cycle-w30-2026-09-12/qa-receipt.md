# QA Receipt — forge-cycle-w30-2026-09-12

**Plan:** executable-100096.md  
**Step:** 5 (QA — report + probes + suite)  
**QA Agent dispatch:** FRESH (no prior evidence dir, git log clean on path)  
**Worktree toplevel:** /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100096  
**Date:** 2026-09-13  

---

## Numstats

| Commit | SHA | Files | Description |
|---|---|---|---|
| Step 1 (ingest) | f1e9184 | 1 | knowledge/development/dev-log-ingest-w30-2026-09-12.md (+1212) |
| Step 2 (classify A) | 1873d06 | 2 | dev-log-classify-w30a-2026-09-12.md (+155), evidence-classify-w30a-2026-09-12.txt (+54) |
| Step 3 (classify B) | 5456ed1 | 2 | dev-log-classify-w30b-2026-09-12.md (+153), evidence-classify-w30b-2026-09-12.txt (+48) |
| Step 4 (classify C) | 513fb51 | 2 | dev-log-classify-w30c-2026-09-12.md (+116), evidence-classify-w30c-2026-09-12.txt (+34) |
| Step 5 report | 8eedf38 | 1 | reports/lessons-report-2026-09-12.md (+881) |

---

## Reflog — 0 amends

```
8eedf38 HEAD@{0}: commit: [100096] forge-cycle-w30: cycle report
513fb51 HEAD@{1}: reset: moving to HEAD
513fb51 HEAD@{2}: (truncated — no amend entries)
```

(Full `git reflog -n 8` shows no `amend` in any entry.)

---

## Report Summary (Item 1)

`generate_lessons_report` wrote `reports/lessons-report-2026-09-12.md` (881 lines, 116,322 bytes).

The new 122-proposal batch rendered as:

```
## Summary

| Category | Count |
|---|---|
| governance_rule | 95 |
| instrumentation | 4 |
| narrative | 1 |
| structural | 22 |

**Total proposals:** 122
```

All 122 new proposals have `status=proposed` and `route=NULL` (M4=0, per probes-raw.txt).

**Three flagged entries (Gate 1 read):**
- Entry 98 → proposal 103 (`status: implemented`) — inline rider added 2026-09-08 (governance `1f242128`); flagged as `terminal_proposals_flagged` at ingest; not re-classified
- Entry 106 → proposal 111 (`status: implemented`) — inline rider added 2026-09-08 (governance `1f242128`); flagged as `terminal_proposals_flagged` at ingest; not re-classified
- Entry 368 → proposal 376 (`status: rejected`) — rider added 2026-09-07 (`5e0088ac`); flagged as `terminal_proposals_flagged` at ingest; 368's rider sits under a rejected proposal; not re-classified

M9 listing hash BEFORE report generation: `1fb34ee52650fd5c`  
M9 listing hash AFTER report generation: `1fb34ee52650fd5c` (26 prior reports byte-identical — unchanged)  
M10: `reports/lessons-report-2026-09-12.md` exists, none of M9's 26 files.

---

## Verification Table

| Deliverable | Expected | Status | Evidence |
|---|---|---|---|
| M2 unclassified | 0 after all classify steps | ✅ | probes-raw.txt: `unclassified count: 0` |
| M3 histogram | accepted=23, proposed=122, total=588 | ✅ | probes-raw.txt: M3 section |
| M4 band purity | 0 bad new proposals | ✅ | probes-raw.txt: `bad new proposals: 0` |
| M5 triple-set | SET-IDENTICAL (466 rows, accepted=23) | ✅ | probes-raw.txt: `SET-IDENTICAL check: True` |
| M6 entry count | count=580, max=580 | ✅ | probes-raw.txt: `count: 580   max_id: 580` |
| M7 AUTHOR-CONFLICT | 108=108 (i); 0 early-date (ii) | ✅ | probes-raw.txt: `sets equal: True`, `early-date: 0` |
| M8 register | sha prefix `0c99d2073e5072f83058`, 523 parsed | ✅ | probes-raw.txt: M8 section |
| M9 prior reports | listing hash `1fb34ee52650fd5c` before and after | ✅ | computed both before and after report generation |
| M10 today's report | exists at `reports/lessons-report-2026-09-12.md` | ✅ | `ls -la reports/lessons-report-2026-09-12.md` |
| M11 content hashes | entries 98, 106, 368 match parser; rest unchanged | ✅ | probes-raw.txt: M11 section, all 3 MATCH=True |
| M12 stale proposals | 3, unchanged | ✅ | probes-raw.txt: `stale count: 3` |
| M14 suite | `80 passed`, exit=0 | ✅ | full-suite-forge-cycle-w30.txt |
| M15 DISPOSITION lines | 41 / 41 / 40 = 122 | ✅ | probes-raw.txt: M15 section |
| M16 duplicates | 0 new `category=duplicate` | ✅ | probes-raw.txt: `duplicate proposals in band: 0` |
| M17 pairing | 0 multi, 0 out-of-band, K=122 | ✅ | probes-raw.txt: M17 section |
| Report committed | 1 file, 881 lines | ✅ | git show --numstat 8eedf38 |
| Step 1 committed | 1 file (ingest dev log) | ✅ | git show --numstat f1e9184 |
| Steps 2-4 committed | 2 files each (dev log + evidence) | ✅ | numstats: 1873d06, 5456ed1, 513fb51 |
| No amends | 0 amend entries in reflog | ✅ | git reflog -n 8 |
| Evidence dir populated | probes-raw.txt, full-suite-forge-cycle-w30.txt | ✅ | ls knowledge/qa/evidence/forge-cycle-w30-2026-09-12/ |

### Rule 20 Self-Check Block — stdout

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100096/knowledge/qa/evidence/forge-cycle-w30-2026-09-12/
Files verified: 2
```
