# QA Report — s2-rewrite-2026-08-11 (Plan 348, Step 2)

## Deliverable Verification

| # | Check | Status |
|---|-------|--------|
| 1 | DOC INTEGRITY — commit by slug `6f7dd2d`, three-way SHA match (`c678f288…`), porcelain clean (DRAFTING_CYCLE.md), name-only exact | ✅ |
| 2 | THE REWRITE LANDED WHOLE — all 13 post-condition probes match, paragraph count 9 (from 3), `^Walk the lenses` = 1 | ✅ |
| 3 | COHERENCE SWEEP — `predominantly fold-introduced` = 2 (described-retirement + v2.0 row), `stops trending toward dry` = 0, `instruction 0 / record` = 4, cross-refs intact | ✅ |
| 4 | NUMSTAT — `21 7` | ✅ |
| 5 | VERSION + CHANGELOG — v2.4 line present, `2.3 (2026-08-11)` = 1, tail probe = 1, PARTIAL-clause = 1, History awk = 14 | ✅ |
| 6 | FLIP + BLAST RADIUS — 12/12 `implemented|codify|ceo`, Z-GLOB, not-in both priors, category `governance_rule` all 12, RB = 6 survivors exact, G2 capture 302 lines byte-identical | ✅ |
| 7 | TARGETED TESTS — 55 passed, none excluded (baseline 55/0, delta 0) | ✅ |
| 8 | GATE-NEUTRALITY — `fold-introduced`/`instruction-class`/`instruction 0` = 0 in both plan_lint.py and gates.py; positive control `Drafting Cycle` = 11; closing-fold WARN fires correctly; deferred half declared | ✅ |
| 9 | CONSUMER SEMANTICS — `reference` terminal (line 31), all 12 source entries absent from unclassified before and after; route = `codify` on all 12 | ✅ |
| 10 | DOCTRINE PARSES — `## ` count = 9, `### ` count = 11, both unchanged | ✅ |

## Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: knowledge/qa/evidence/s2-rewrite-2026-08-11/
Files verified: 4
```

## Evidence and Narrative

### Row 1 — DOC INTEGRITY

Commit discovered independently: `git log --all --oneline --grep='s2-rewrite-2026-08-11'` → `6f7dd2d`. Three-way SHA: DOC_SHA from dev-log, live `shasum -a 256`, and `git show 6f7dd2d:DRAFTING_CYCLE.md | shasum -a 256` all return `c678f288deba2725fa878969e10362f618de532786a2f75f1a1c4c391d52e54e`. Porcelain shows submodule pointers (`M bellows`, `M lessons-forge`) and `?? scratchpad/` — DRAFTING_CYCLE.md is clean. Name-only: exactly `DRAFTING_CYCLE.md`, one file in the commit. Evidence: `doc-integrity.txt`.

### Row 2 — THE REWRITE LANDED WHOLE

All 13 Step-1 post-condition probes re-run independently on the live file. Every value matches: `zero instruction-class findings` = 2, `DEMOTED to a diagnostic` = 2, `convergence clock RESETS` = 1, `converged before its account of itself` = 1, `sweeps the record lines that track it` = 1, `stops trending toward dry` = 0, `instruction 0 / record` = 4 occurrences (via `grep -Fo | wc -l`), version 2.4 line = 1, `2.3 (2026-08-11)` = 1, `predominantly fold-introduced` = 2, `14 of 19 confirming-pass findings at exec-330` = 1, `N of M fold-introduced` = 1, History awk = 14. Bar structure: `grep -cE '^Walk the lenses'` = 1, paragraph count via the shipped python3 extraction command = 9 (from 3 pre-edit — both sides measured on the executed dry-run). Evidence: `doc-integrity.txt`.

### Row 3 — COHERENCE SWEEP

`predominantly fold-introduced` = 2 with locations classified: (1) line 42, §2 bar — the described-retirement parenthetical ("the prior bar's 'predominantly fold-introduced' condition and the section's own noise-floor warning were the same number read in opposite directions"); (2) line 268, the immutable v2.0 History row. No third location. `stops trending toward dry` = 0. `instruction 0 / record` = 4 occurrences. Cross-references: `### 2.0 Walk 0` = 1, `A walk covers, it does not target.` = 1, `alongside the per-class split (and the origin split as its diagnostic)` = 1 — all intact. Evidence: `doc-integrity.txt`.

### Row 4 — NUMSTAT

`git diff 6f7dd2d^..6f7dd2d --numstat` → `21	7	DRAFTING_CYCLE.md`. Exact match. Evidence: `doc-integrity.txt`.

### Row 5 — VERSION + CHANGELOG

v2.4 line present (1). `2.3 (2026-08-11)` = 1 (the prior History row). Tail probe `stated for the audit trail` = 1 (earnable — 0 pre-edit). PARTIAL-clause probe `259's cross-plan-measurement middle ask` = 1 (earnable — 0 pre-edit). History awk = 14. New v2.4 row is FIRST at line 264, names slug `s2-rewrite-2026-08-11`, prior 2.3 row intact below at line 268. Evidence: `doc-integrity.txt`.

### Row 6 — FLIP + BLAST RADIUS

**(a)** All 12 rows show `governance_rule|implemented|codify|ceo|2026-08-11T22:44:51Z`. Category = `governance_rule` on every row (asserted against the authoring pin — all 12 measured `governance_rule` 2026-08-11). Route flipped `backlog → codify` on all 12 (pre-flip-state.txt confirms prior route was `backlog`). Z-GLOB: 12 of 12. Not equal to prior old value (`2026-08-09T01:20:01Z`): 0 matches. Not equal to prior new value (`2026-08-11T13:42:09+00:00`): 0 matches.

**(b)** `reference|backlog` corpus-wide = 6. Survivor ids: `161, 169, 291, 294, 299, 301` — exact match to the authoring-time list (queried 2026-08-11). No MISSING ids. No ADDED ids.

**(c)** Re-ran the EXACT G2 capture SELECT (copied verbatim, projection order `id|category|status|route|status_updated_at|status_updated_by`). QA capture: 302 lines. Deposited: 302 lines. First-line shape: `1|governance_rule|implemented||2026-05-13 16:07:24|ceo` (six pipe-delimited fields). Diff: empty (byte-identical). Evidence: `db-invariants.txt`.

### Row 7 — TARGETED TESTS + PREMISE

Single-module premise: DRAFTING_CYCLE.md changed (no source code); the builder script has no runtime consumers; the DB flip touches `lesson_proposals` rows, exercised by `src/test_lessons_forge.py`. `python3 -m pytest src/test_lessons_forge.py -v --tb=short` → 55 passed in 0.10s. Baseline: 55/0. Delta: 0. Evidence: `pytest_targeted.txt`.

### Row 8 — GATE-NEUTRALITY + THE DEFERRED HALF

**(a)** `fold-introduced`, `instruction-class`, `instruction 0` → 0 in both `/Users/marklehn/Developer/GitHub/bellows/scripts/plan_lint.py` and `/Users/marklehn/Developer/GitHub/bellows/gates.py`. Gates.py is at the bellows ROOT, not beside plan_lint.

**(b)** Positive control: `Drafting Cycle` in `plan_lint.py` = 11.

**(c)** The closing-fold WARN (check-(f), plan_lint.py ~lines 220–240) keys on per-lens lines' `fold` and `dry` tokens. The mechanism: `lens_line_re` matches per-lens lines (weak spots, destruction, etc.), scans the last lens line before `**Closing:**` for `'fold' in ll_lower` and `re.search(r'\bdry\b', cleaned)`. The WARN fires when `has_fold=True AND has_dry=False`. The v2.4 rewrite changes §2's bar prose paragraphs — the per-lens line format (`w<N> <count> folded`, `dry`) is unchanged. The worked form (E5) modifies the parenthetical content but retains `folded` and `dry` tokens. The check fires correctly on v2.4-form plans.

The check-(f) prose refresh is the DEFERRED gate half: the WARN text now UNDERSTATES the closing condition (the 332-precedent class — an understatement, not a false check). Owed: check-(f) prose refresh + optional per-class line-form check. Owner: bellows plan_lint. Delivery: wrap-emitted FORWARD row (Planner-direct). Evidence: `gate-neutrality.txt`.

### Row 9 — CONSUMER SEMANTICS

**(a)** Preservation check (not a flip observer — seat 3): `lessons_forge.py` line 31: `_TERMINAL_STATUSES = frozenset(('implemented', 'rejected', 'superseded', 'reference'))`. Both `reference` (pre-flip) and `implemented` (post-flip) are terminal. `get_unclassified_entries` excludes entries with terminal-status proposals. All 12 source entries (225, 230, 238, 239, 250, 251, 263, 267, 270, 284, 294, 300) verified ABSENT from the unclassified set before AND after — guards linkage deletion only.

**(b)** Route consumer: `lessons_forge.py` reads `route` in `generate_lessons_report()` (line 538+ SELECT, line 583–584 rendering as `- **Route:** {route}`). Route-reading query confirms all 12 read `codify` where backlog-readers no longer see them. Evidence: `db-invariants.txt`.

### Row 10 — DOCTRINE PARSES

`grep -cE '^## '` = 9 (unchanged; one is the fenced `## Drafting Cycle` decoy inside §3's example, noted per the 253 strip-fences rule). `grep -cE '^### '` = 11 (unchanged; the rewrite adds paragraphs and bullets, zero headings). Evidence: `doc-integrity.txt`.

## Output Receipt

- **DOC_SHA:** `c678f288deba2725fa878969e10362f618de532786a2f75f1a1c4c391d52e54e`
- **Commit (doctrine):** `6f7dd2d44c6639eb1ce8ab2b5b5c15807bd908b7`
- **Numstat:** `21 7`
- **All 10 QA rows:** ✅

### Ledger Updates

#### Prompt Feedback

#### Forward Register
NONE
