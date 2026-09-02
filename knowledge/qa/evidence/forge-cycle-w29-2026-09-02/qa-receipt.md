# QA Receipt — forge-cycle-w29-2026-09-02

**Plan:** forge-cycle-w29-2026-09-02
**Step:** 3 (QA)
**Date:** 2026-09-02
**QA Agent:** Forge QA agent

---

## Dispatch-State Probe

- `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md` in working tree: ABSENT
- `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md` in HEAD: ABSENT
- `git log --all -- knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md`: no hits
- Positive control: `knowledge/FORWARD.md` — EXISTS
- **Determination: FRESH**

---

## Worktree Toplevel

`/Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100020`

---

## Commit Numstats

**Step 1 — ingest commit (5f058ca):**
```
256	0	knowledge/development/dev-log-ingest-w29-2026-09-02.md
```
1 file committed. ✓

**Step 2 — classify commit (76ad9b8):**
```
238	0	knowledge/development/dev-log-classify-w29-2026-09-02.md
90	0	knowledge/development/evidence-classify-w29-2026-09-02.txt
```
2 files committed. ✓

**Report commit (323e4b4):**
```
190	0	reports/lessons-report-2026-09-02.md
```
1 file committed. ✓

---

## Reflog (no amends)

```
323e4b4 HEAD@{0}: commit: [100020] forge-cycle-w29: cycle report
76ad9b8 HEAD@{1}: reset: moving to HEAD
76ad9b8 HEAD@{2}:
```
0 amends in reflog. ✓

---

## M9 Check (pre-existing 25 report files)

- Before report generation: `shasum -a 256 reports/*.md | shasum -a 256 | cut -c1-16` = `8f61939d22de31e3` (25 files)
- After report generation (same 25 names, excluding 2026-09-02): `8f61939d22de31e3`
- **UNCHANGED — byte-identical**

## M10 Check (today's report)

- `reports/lessons-report-2026-09-02.md` exists (28351 bytes, created 2026-09-02)
- None of the 25 prior reports affected

---

## New 25-Proposal Batch (Gate 1 read)

The report (`reports/lessons-report-2026-09-02.md`) renders the new batch as 25 proposals under `## Governance Rule`. All 25 carry `category=governance_rule`, `confidence=high`, `status=proposed`, `route=NULL`. The twenty 2026-09-02 entries carry `[AUTHOR-CONFLICT]` in their reasoning. The five 2026-09-01 entries carry no marker.

Report summary table:
```
| Category       | Count |
|---|---|
| governance_rule | 25   |
Total proposals: 25
```

First entry (entry 434, proposal 442, 2026-09-01 — no AUTHOR-CONFLICT):
> **2026-09-01: TWO RECORDS OF ONE FACT WILL DIVERGE UNLESS ONE IS A PROJECTION OF THE OTHER**
> Suggested action: Add rule to PLANNER_TEMPLATE.md…
> Reasoning: Entry proposes a process-integrity rule…

First 2026-09-02 entry (entry 439, proposal 447):
> **2026-09-02: A PROBE'S LOCATION IS PART OF ITS ENVIRONMENT**
> Reasoning: [AUTHOR-CONFLICT] Entry proposes a verification rule…

---

## Verification Table

| Deliverable | Expected | Status | Evidence |
|---|---|---|---|
| M2: unclassified entries | [] (count=0) | ✅ | probes-raw.txt |
| M3: status histogram | total=466; accepted=12; K=25 | ✅ | probes-raw.txt |
| M4: new proposals with route!=NULL or status!='proposed' | COUNT=0 | ✅ | probes-raw.txt |
| M5: pre-existing triple-set SET-IDENTICAL | 441 rows, accepted 12 unchanged | ✅ | probes-raw.txt |
| M6: lesson_entries | COUNT=458, MAX=458 | ✅ | probes-raw.txt |
| M7 dir (i): AC markers match 2026-09-02 entries | 20 == 20; SET-IDENTICAL | ✅ | probes-raw.txt |
| M7 dir (ii): AC markers on non-2026-09-02 entries | COUNT=0 | ✅ | probes-raw.txt |
| M11: pre-existing content_hash set | SET-IDENTICAL vs Step 1 (433 entries) | ✅ | probes-raw.txt |
| M12: stale proposals | COUNT=3 (unchanged) | ✅ | probes-raw.txt |
| M15: DISPOSITION lines in classify log | COUNT=25 | ✅ | probes-raw.txt |
| M16: new duplicate proposals | COUNT=0 | ✅ | probes-raw.txt |
| M17: dup proposals per entry / out-of-band | 0 rows / 0 | ✅ | probes-raw.txt |
| M8: LESSONS.md sha | ee0432aeb88a3dfed4e8… (unchanged) | ✅ | probes-raw.txt |
| M9: prior 25 reports unchanged | hash=8f61939d22de31e3 (before and after) | ✅ | probes-raw.txt |
| M10: today's report exists | reports/lessons-report-2026-09-02.md | ✅ | ls -la reports/ |
| M14: test suite | 80 passed; exit=0 | ✅ | full-suite-forge-cycle-w29.txt |
| Step 1 numstat | 1 file (dev-log-ingest) | ✅ | git diff-tree 5f058ca |
| Step 2 numstat | 2 files (dev-log-classify + evidence-classify) | ✅ | git diff-tree 76ad9b8 |
| Report numstat | 1 file (lessons-report-2026-09-02.md) | ✅ | git diff-tree 323e4b4 |
| Reflog amends | 0 amends | ✅ | git reflog -n 5 |

---

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100020/knowledge/qa/evidence/forge-cycle-w29-2026-09-02/
Files verified: 2
```
