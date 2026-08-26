# lessons-forge — executable: `[project:]` heading markers stripped from ingest identity keys (the CEO's additive project tag, forge side)

**Date:** 2026-08-26 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** lessons-forge suite (`PYTHONPATH=. python3 -m pytest src/test_lessons_forge.py`) | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

**auto_close:** false

**Depends on:** the CEO's ruling this session (an ADDITIVE `[project: <name>]` tag on LESSONS.md entries, enabling "mechanize lessons for <project>" sweeps) + this session's code diagnostic: `_key_heading` strips only `[status:]`/`[target:]`, so an unstripped `[project:]` bracket would join the entry identity key and make retro-tagging orphan ingest rows. This plan makes the bracket PURE METADATA. The PT v4.94 codification (the house-format line) is the SERIAL follow-up plan; it deposits only after this closes.

## Why this exists

The project tag must be invisible to ingest identity or it cannot be safely added to existing entries. One alternation arm + two tests make it so.

## What this plan does NOT do

- No PT edit (the sibling plan), no LESSONS.md content change, no `**Tag:**`-line semantics change (project names never enter the tags column — tag-overlap dedup would cross-match unrelated same-project lessons).

## Numbers discipline

⚠️ **Measured 2026-08-26 at authoring; Step 1 re-derives — yours supersede.**

| id | pin | value | anchor |
|---|---|---|---|
| S1 | the regex line | count-1, EXACT: `_STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target):[^\]]*\]', re.IGNORECASE)` | `src/lessons_forge.py` (repo-relative — worktree law) |
| S2 | suite baseline | **63 passed** (green, measured) | `src/test_lessons_forge.py` |
| S3 | existing `_key_heading` tests | preserve-tag + strip-status/target — neither involves `project`; both must STILL pass unchanged | ibid. L1590+ |

## STEP 1 — DEV (the arm + the tests, targeted run)

> **Task A — worktree discipline.** ⚠️ Your cwd IS the claimed tree — never cd to `/Users/marklehn/Developer/GitHub/lessons-forge`. Open: `cd "$(git rev-parse --show-toplevel)" && test -f src/lessons_forge.py && echo TREE_OK` — HALT unless TREE_OK. All paths RELATIVE. State probes: (i) `/usr/bin/grep -cF -- "status|target|project" src/lessons_forge.py; true` (the arm), (ii) `/usr/bin/grep -cF -- "test_key_heading_strips_project_marker" src/test_lessons_forge.py; true` (the tests). (0,0) → full run; (1,0) → the arm landed but not the tests: resume at Task C; (1,1) → both landed: skip to Task D's commit-check; (0,1) → impossible state, HALT with both values.
>
> **Task B — the arm (anchored, count-1, write-after-assert).** In `src/lessons_forge.py` replace (python heredoc; anchor count-1 else SystemExit, no write):
>
> ```
> _STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target):[^\]]*\]', re.IGNORECASE)
> ```
>
> with:
>
> ```
> _STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target|project):[^\]]*\]', re.IGNORECASE)
> ```
>
> (The name keeps its historical form — renaming it would touch every call site for zero behavior; the docstring comment gains nothing the tests don't state.)
>
> **Task C — two tests appended to `src/test_lessons_forge.py`** (after `test_key_heading_preserves_tag_markers`, anchor on that function's final assert line count-1):
>
> ```
> def test_key_heading_strips_project_marker():
>     """[project: ...] is identity-invisible: new-entry keys are stable and
>     retro-tagging an existing entry does not change its ingest key."""
>     tagged = "2026-08-26 — Lesson [tag: x] [project: invoice-pulse]"
>     assert _key_heading(tagged) == "2026-08-26 — Lesson [tag: x]"
>     multi = "2026-08-26 — Lesson [tag: x] [project: invoice-pulse, anvil]"
>     assert _key_heading(multi) == "2026-08-26 — Lesson [tag: x]"
>
>
> def test_key_heading_strips_project_with_status_and_target():
>     """project composes with the existing stripped markers in any order."""
>     mixed = "2026-08-26 — L [project: anvil] [status: pending] [target: X]"
>     assert _key_heading(mixed) == "2026-08-26 — L"
> ```
>
> Targeted run (DEV law — never the full suite here): `PYTHONPATH=. python3 -m pytest src/test_lessons_forge.py -k "key_heading" --tb=short -q 2>&1 | cat` → **4 passed** (the 2 existing + the 2 new), 0 failed; paste raw.
>
> **Task D — dev note + commit.** Write `knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md` (anchor probe, targeted-run raw output). Commit (WORKTREE toplevel): `cd "$(git rev-parse --show-toplevel)" && git add src/lessons_forge.py src/test_lessons_forge.py knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md && git commit -m "[<id from your plan filename>] forge-project-marker-strip(forge-project-marker-strip-2026-08-26): [project:] joins the identity-strip alternation + 2 tests" -- src/lessons_forge.py src/test_lessons_forge.py knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md && git rev-parse HEAD` — **CAPTURE_COMMIT**; separate: `git show <CAPTURE_COMMIT> --numstat --format=` — exactly the three files.
>
> **Deposits:**
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
> - `knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md`
>
> **Scope:**
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
> - `knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md`

## STEP 2 — QA (FULL suite — the safety net)

> **Item 1 — full suite.** `cd "$(git rev-parse --show-toplevel)"`; `PYTHONPATH=. python3 -m pytest src/test_lessons_forge.py --tb=short -q 2>&1 | cat | tee knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/pytest_full.txt` → **65 passed** expected (63 baseline + 2 new), 0 failed — the summary line is the gate's food; HALT on ANY failure with the raw output.
> **Item 2 — committed-extraction probes.** `git show <CAPTURE_COMMIT>:src/lessons_forge.py` to scratch: `"status|target|project"` == 1 AND `"status|target):"` == 0; `git show <CAPTURE_COMMIT>:src/test_lessons_forge.py`: `"test_key_heading_strips_project_marker"` == 1 AND `"test_key_heading_strips_project_with_status_and_target"` == 1; `cmp` both vs live → 0. Raw → `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/probes-raw.txt`.
> **Item 3 — commit hygiene.** numstat exactly 3 files; toplevel printed; reflog `-n 4` → 0 amends.
> **Item 4 — receipt** `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/qa-receipt.md`: per-item table, then the Rule 20 block.
>
> ⚠️ **Gate note:** this QA HAS a pytest summary (`pytest_full.txt` named above) — the `qa_test_result` gate should PARSE it; no benign override is pre-declared. A gate failure here is REAL and pauses for genuine adjudication.
>
> **Deposits:**
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/pytest_full.txt`
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/qa-receipt.md`
>
> **Scope:**
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/pytest_full.txt`
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/qa-receipt.md`

Rule 20 banner (byte-exact, inside the QA receipt's verification section):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```

## Drafting Cycle

**Tier:** T1 — one alternation arm + two tests; the worktree law carried; REAL pytest QA (the first in this arc — the gate parses, no benign override declared).

**Walk register:** `lessons-forge/knowledge/research/walk-register-forge-project-marker-strip-2026-08-26.md`

**Walk 0 (context pin, measured):** the regex line count-1 verbatim; suite baseline 63 green; the two existing `_key_heading` tests project-free (they must pass unchanged); the code diagnostic recorded (identity-key trap, tags-column exclusion); id prediction 549.

**Walks:**
- Weak spots:          w1 dry — every probe pair earnable (`status|target):` == 0 flips only on the arm; the 65-passed expectation is measured-63 + deterministic-2, not a bare prediction); the -F literals contain no regex metacharacter traps.
- Destruction:         w1 1 folded — the single resume probe conflated arm-landed with tests-landed (a death between Tasks B and C would skip the tests and commit without them, caught only at QA): split into the two-probe branch table incl. the impossible-state HALT.
- Vulnerabilities:     w1 dry — MEASURED: `[project:` count in the live LESSONS.md corpus is 0, so the widened strip changes NO existing entry's identity key at next ingest (the retro-orphan risk the diagnostic named is vacuous today and becomes safe-by-design after this ships).
- Integration-record:  w1 dry — the tags-column exclusion stated with its dedup rationale; PT v4.94 named as the serial sibling; Test Scope declared so the real pytest gate engages, no benign override pre-declared.
- ACID:                w1 dry — one commit, three files, pathspec-limited, worktree-pinned.
- **Walk 1 total: one finding, folded.**
- Weak spots:          w2 dry — the branch table's four arms re-read; each probe re-verified count-1/0 against the live tree.
- Destruction:         w2 dry — arms partition pre-B / B-to-C / C-to-D / post-D.
- Vulnerabilities:     w2 dry.
- Integration-record:  w2 dry.
- ACID:                w2 dry.
- **Walk 2 total: 0 findings — all five lenses dry.**

**Closing:** ✅ **BAR MET at walk 2 — dry confirming pass, all five lenses.** T1 two-walk form; no direction-class finding; close is MANUAL (CEO-lane verdicts).

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: lessons-forge/src/lessons_forge.py
class: shop-infra
reads: /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py, /Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py
writes: src/lessons_forge.py, src/test_lessons_forge.py, knowledge/dev-logs/forge-project-marker-strip-dev-2026-08-26.md, knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/pytest_full.txt, knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/probes-raw.txt, knowledge/qa/evidence/forge-project-marker-strip-2026-08-26/qa-receipt.md
open_forks: PT v4.94 house-format codification (SERIAL sibling, deposits after this closes); the invoice-pulse legacy LESSONS.md bin retirement; the record errors + 346-residue entry + /wrap (in order)
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A
