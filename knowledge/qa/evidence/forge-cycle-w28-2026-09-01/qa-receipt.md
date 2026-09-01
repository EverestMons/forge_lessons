# QA Receipt — forge-cycle-w28-2026-09-01

**Plan:** forge-cycle-w28 (W=28, 2026-09-01)
**QA Agent:** Bellows-dispatched, worktree 100007
**Date:** 2026-09-01
**Worktree:** /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100007

---

## Dispatch State

Three-place probe:
- `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md` in HEAD: ABSENT (fresh)
- Working tree: clean
- Positive control `knowledge/FORWARD.md`: PRESENT

Determination: **FRESH** — no prior Step 3 run.

---

## Numstats

Step 1 commit (e2318bc):
```
209	0	knowledge/development/dev-log-ingest-w28-2026-09-01.md
```
1 file ✓

Step 2 commit (5f21613):
```
170	0	knowledge/development/dev-log-classify-w28-2026-09-01.md
68	0	knowledge/development/evidence-classify-w28-2026-09-01.txt
```
2 files ✓

Report commit (ed59a68):
```
219	0	reports/lessons-report-2026-09-01.md
```
1 file ✓

---

## Toplevel

```
/Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100007
```

---

## Git Reflog (last 5 — 0 amends)

```
ed59a68 HEAD@{0}: commit: [100007] forge-cycle-w28: cycle report
5f21613 HEAD@{1}: reset: moving to HEAD
5f21613 HEAD@{2}: (classify commit)
```
No `amend` entries present. ✓

---

## M9 Verification (six prior reports byte-identical)

Pre-report shasums:
```
7cfd7904c849197645300ea8b0c83078b4d3ebc997a5e85be70eaa2f29e7d7a5  reports/lessons-report-2026-08-13.md
f1807cf266b369541ce5ae56f17e83966e354dd36d0ac8daa7ec73d4ec454c85  reports/lessons-report-2026-08-14.md
b21281169ac1a138ade427d338c90823382d03cb69800234533d5e86a87d991d  reports/lessons-report-2026-08-15.md
7f9b283bf42a31eb9fca9fb97121cad1a5dfc654a9fc5a8aa06e5b3dcafa363e  reports/lessons-report-2026-08-19.md
0984fdd3521e682c3c0a4cba0c604122a58ee872232640dd4e5b370879a688c7  reports/lessons-report-2026-08-25.md
3c8362d2191da39ec3887ea1557aec4578fcc0db4dc23ac923b265bc5fdbad37  reports/lessons-report-2026-08-26.md
```

Post-report shasums: IDENTICAL (generate_lessons_report only writes `lessons-report-2026-09-01.md`, does not touch prior files).

All six byte-identical before and after report generation. ✓

---

## M10 Verification

```
-rw-r--r--@ 1 marklehn  staff  29393 Sep  1 16:36 reports/lessons-report-2026-09-01.md
sha256: f47220f98d2709c873befc179e4b2188012c782a0a5d38778e23ebf9c93ba0a1
```
File exists at worktree-anchored path. None of M9 files. ✓

---

## Report Rendering — New 28-Proposal Batch (for Gate 1)

The report at `reports/lessons-report-2026-09-01.md` renders the batch as follows:

**Summary table:**

| Category | Count |
|---|---|
| governance_rule | 23 |
| instrumentation | 2 |
| structural | 3 |

**Total proposals: 28**

All 28 proposals have `route = NULL` and `status = proposed`. The four proposals for entries 430–433 (dated 2026-09-01) carry the `[AUTHOR-CONFLICT]` disclosure marker in their reasoning.

**Proposal headings in the report (28 entries, dates 2026-08-26 through 2026-09-01):**

governance_rule (23):
- 2026-09-01: EXECUTING A PLAN'S COMMANDS IS NOT EXECUTING THE GATES THAT JUDGE ITS STEPS
- 2026-09-01: A POST-CONDITION BUILT ON A HAND-ENUMERATED LIST IS ONLY AS COMPLETE AS ITS AUTHOR
- 2026-09-01: A LOSSLESS REORDER PRESERVES TRUTH AND DESTROYS PROXIMITY
- 2026-09-01: A WORK POOL DEFINED BY A TAGGING CONVENTION MEASURES THE CONVENTION, NOT THE SUBJECT
- 2026-08-31: A VARIABLE YOUR HARNESS INJECTS IS NOT PRESENT FOR THE DAEMON THE HARNESS SPAWNS
- 2026-08-31: ENABLING A WATCHER OVER A DIRECTORY RETROACTIVELY PROMOTES EVERYTHING ALREADY IN IT TO AN INPUT
- 2026-08-31: ⛔ CORRECTS THE ENTRY ABOVE — `is_runnable_plan` IS AN ALLOWLIST
- 2026-08-31: A NORMATIVE DOCUMENT'S WORKED EXAMPLE IS NOT A KNOWN-GOOD ARTIFACT WHEN A MACHINE COMPARATOR IS THE AUTHORITY
- 2026-08-30: WHEN ONE DEFECT CLASS FIRES ON CONSECUTIVE REVIEW PASSES, THE REVIEW HAS BECOME SAMPLING
- 2026-08-27: A test written by the author of the code inherits the author's model
- 2026-08-27: A DORMANT CLASSIFICATION BECOMES POLICY the moment a new mechanism starts reading it
- 2026-08-27: A STOP ARM must key on the claim that would make the work worthless
- 2026-08-27: BEFORE OPTIMIZING A SYSTEM'S LIFECYCLE, CONFIRM WHAT THE SYSTEM IS FOR
- 2026-08-27: ROUTE A QUESTION BY WHETHER A COMMAND CAN ANSWER IT
- 2026-08-27: A SHIPPED ARTIFACT IS A POOR TEACHER ABOUT ITS OWN MISTAKES
- 2026-08-27: PROVING A GUARD COVERS A RULE REQUIRES VIOLATING THE RULE
- 2026-08-27: A DOCTRINE EDIT RIDING A CODE PLAN IMPOSES THE DOCTRINE'S TIER ON THE CODE
- 2026-08-27: A DETECTOR'S FIRE COUNT IS A RATIO
- 2026-08-27: WHEN A DATUM IS OPTIONAL, ITS CONSUMERS WILL SILENTLY DISAGREE ABOUT ABSENCE
- 2026-08-26: A verification instrument's DEFAULTS are part of the pin
- 2026-08-26: A plan authored on one machine carries its layout's absolute paths into another machine's gates
- 2026-08-26: A live canary must be fired in the STATE the tool exists to discriminate
- 2026-08-26: A ruling amended MID-CYCLE moves the artifact its in-flight plans pin

instrumentation (2):
- 2026-08-27: EARNABILITY IS NOT DISCRIMINATION
- 2026-08-27: Jointly-sufficient guards are individually UN-mutation-testable

structural (3):
- 2026-08-31: AN EMPTY DIRECTORY SATISFIES A PATH CHECK, AND `git -C` INSIDE AN UNINITIALIZED SUBMODULE RESOLVES TO THE PARENT REPO
- 2026-08-27: VALIDATE-THEN-WRITE IS NOT ALL-OR-NOTHING
- 2026-08-27: A CHECK WHOSE TWO OPERANDS COME FROM THE SAME SOURCE CAN NEVER FIRE

---

## Verification Table

| Deliverable | Expected | Status | Evidence |
|---|---|---|---|
| M2 — unclassified after classify | 0 (full inversion) | ✅ | probes-raw.txt § M2 |
| M3 — proposal histogram K | K=28; total=441 | ✅ | probes-raw.txt § M3 |
| M4 — new band route/status | 0 rows with route or non-proposed | ✅ | probes-raw.txt § M4 |
| M5 — triple-set SET-IDENTITY | 413 rows unchanged | ✅ | probes-raw.txt § M5 |
| M6 — entry count and band | 433 total; ids 406–433 contiguous; dates 2026-08-26 to 2026-09-01 | ✅ | probes-raw.txt § M6 |
| M7(i) — AUTHOR-CONFLICT markers (forward) | 4 proposals = 4 entries dated 2026-09-01 | ✅ | probes-raw.txt § M7 |
| M7(ii) — AUTHOR-CONFLICT markers (reverse) | 0 non-09-01 entries with marker | ✅ | probes-raw.txt § M7 |
| M8 — LESSONS.md sha and parse count | sha prefix f4b732f1c6bb2fa113bc; 376 entries | ✅ | probes-raw.txt § M8 |
| M9 — six prior reports byte-identical | all six sha-identical before and after | ✅ | this receipt § M9 |
| M10 — today's report exists | reports/lessons-report-2026-09-01.md | ✅ | this receipt § M10 |
| M11 — content_hash set (with 347/398 exceptions) | 405 rows; 347→8074f58c; 398→3ccad66a; rest unchanged | ✅ | probes-raw.txt § M11 |
| M12 — stale proposals | 3 unchanged | ✅ | probes-raw.txt § M12 |
| M14 — test suite | 80 passed; exit=0 | ✅ | full-suite-forge-cycle-w28.txt |
| M15 — DISPOSITION lines | 28 in classify dev log | ✅ | probes-raw.txt § M15 |
| M16 — no new duplicate proposals | 0 | ✅ | probes-raw.txt § M16 |
| M17a — no entry with >1 new proposal | 0 rows | ✅ | probes-raw.txt § M17 |
| M17b — all new proposals within entry band | 0 outside band | ✅ | probes-raw.txt § M17 |
| Step 1 commit numstat | 1 file | ✅ | this receipt § Numstats |
| Step 2 commit numstat | 2 files | ✅ | this receipt § Numstats |
| Report commit numstat | 1 file | ✅ | this receipt § Numstats |
| Reflog — 0 amends | no amend entries | ✅ | this receipt § Reflog |

---

## Rule 20 Self-Check Output

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100007/knowledge/qa/evidence/forge-cycle-w28-2026-09-01/
Files verified: 2
```

