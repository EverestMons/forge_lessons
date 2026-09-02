# QA Receipt — gate2-dc-w28-2026-09-01

**Plan slug:** gate2-dc-w28-2026-09-01
**Step:** 2 (QA)
**QA agent worktree:** /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100008
**CAPTURE_COMMIT:** 9976238e7ba12b688afad7e08a030fa6545a2b4b
**Subject:** [100008] gate2-dc(gate2-dc-w28-2026-09-01): 426+427+428+429+432+439+440+441 — consumer dry-run, standing-rules + register diffs, read/ran label, violate-the-rule, split-on-tier, class-sampling, derived enumeration, referential distance, pool-is-population — DC v2.23

**Isolation check:** live sha `3a84137ed3669de1d690c4b22b57b158c3387792b12902de6be0aa34f8c63a77` equals committed blob sha; porcelain empty. All Item 1 probes run against committed extraction `/tmp/g2dcw28-HEAD-DC.md`.

---

## Verification Table

| Deliverable | Expected | Status | Evidence |
|---|---|---|---|
| Item 1 — Task C battery (31 probes) against committed extraction | All 31 counts at declared values (E1–E9 each 1; 8 fold clauses each 1; 9 provenance tags each 1; version 2.23=1, 2.22=0; history rows 2.23=1, 2.22=1; wc-l=369; bullets=172; sha=P7) | ✅ | probes-raw.txt |
| Item 2 — C1 byte-identity | builder_exit=0; cmp_exit=0 (rebuilt byte-identical to committed extraction) | ✅ | probes-raw.txt |
| Item 3 — C4/C5 commit structure | CAPTURE_COMMIT numstat: 1 row DRAFTING_CYCLE.md 12/6; dev-log commit: 1 file; flip commit: 3 files; doctrine-landed count=1; flip-implemented count=1; governance amend count=0 | ✅ | probes-raw.txt |
| Item 4 — gate-neutrality sweep | All 9 new tokens count 0 in plan_lint.py and gates.py; positive controls: Rule 20 in plan_lint=3, cycle_tier in plan_lint=7 | ✅ | probes-raw.txt |
| Item 5 — C7 flip re-verify (POST-COMMIT fresh-connection read) | All 8: `implemented\|codify\|ceo\|2026-09-02T00:23:40Z`; categories all `governance_rule`; ACC=12; IMPL=322; NEWROWS=0; 12 remaining accepted rows all PLANNER_TEMPLATE.md; capture re-run 433 lines; diff vs deposited file empty | ✅ | probes-raw.txt, flip-capture.txt |
| Item 6 — raw output throughout | Raw output in probes-raw.txt; all ❌ markers backtick-quoted inside literals | ✅ | probes-raw.txt |
| Item 7 — corpus preservation | PROPOSALS=441 (441+0); ENTRIES=433 (433+0); no shortfall | ✅ | probes-raw.txt |
| Item 8 — suite (P11) | 80 passed; exit=0 | ✅ | full-suite-gate2-dc-w28.txt |

---

## Rule 20 — QA Self-Check Verification

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/forge_lessons/.bellows-worktrees/100008/knowledge/qa/evidence/gate2-dc-w28-2026-09-01
Files verified: 3
```
