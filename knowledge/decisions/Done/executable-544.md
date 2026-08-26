# lessons-forge — executable: `knowledge/glossary.md` retired to a pointer (central-glossary follow-up)

**Date:** 2026-08-26 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (doc-only; consumer sweep measured 0 code hits) | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

**auto_close:** false

**Depends on:** plan 542 (Done — the CEO's one-central-glossary ruling, proposals 378 + 389; `GLOSSARY.md` live with BOTH lessons-forge entries); plan 543 (Done TODAY — **CLONE ORIGIN**, its post-fold form carried entire; ⚠️ 543 also already re-pointed `/wrap` 3d shop-wide, so the SC-5 ordering precondition — no scaffold clause may survive the pointer-ization — is ALREADY satisfied globally; this plan is the W2 half only); the CEO's go-ahead this session ("go ahead with the lessons-forge pointer plan").

## Why this exists

`lessons-forge/knowledge/glossary.md` is the last live per-repo glossary scaffold (the three grandfathers are declared deferrals, not scaffolds). Its 2 entries already live in the central file under `[project: lessons-forge]`; the file must retire to a pointer so nothing accretes in a superseded location.

## What this plan does NOT do

- No wrap.md edit (543 shipped it); no write to root `GLOSSARY.md` or any root file — root is READ-ONLY here (the completeness guard reads it); no touch of the grandfathered legacy glossaries.

## Numbers discipline

⚠️ **Measured 2026-08-26 at authoring; Step 1 re-derives — yours supersede.**

| id | pin | value | anchor |
|---|---|---|---|
| S1 | old glossary | 10 lines, exactly 2 `## ` entries (`Gate 1 (routing)`, `DISPOSITION line`) | `knowledge/glossary.md` (repo-relative) |
| S2 | central census | `[project: lessons-forge]` == 2 | `/Users/marklehn/Developer/GitHub/GLOSSARY.md` (root, read-only) |
| S3 | consumer sweep | 0 `.py` hits for "glossary" in this repo | measured at authoring; the file is prose-only surface |

Post-edit counts are NOT predicted here — Step 1 measures and records in the dev note; QA compares the RECORDED values (543's design note (b), clone-carried).

## STEP 1 — DEV (completeness-guard then pointer-ize)

> **Task A — worktree discipline + state branch (clone-carried 543 W1-F2/F3).** ⚠️ **Your cwd IS the claimed tree (bellows dispatches into a WORKTREE) — never cd to `/Users/marklehn/Developer/GitHub/lessons-forge`; an absolute cd would edit the LIVE tree and defeat isolation.** Open with: `cd "$(git rev-parse --show-toplevel)" && test -f knowledge/glossary.md && echo TREE_OK` — HALT unless `TREE_OK`. ALL in-repo paths RELATIVE to this toplevel; the ONLY absolute path in this plan is the read-only root `GLOSSARY.md`. Probe: (i) `/usr/bin/grep -c "^## " knowledge/glossary.md; true` (⚠️ REGEX form deliberately — under `-F` the caret is a LITERAL and the count silently reads 0), (ii) `/usr/bin/grep -cF -- "RETIRED" knowledge/glossary.md; true`, (iii) `/usr/bin/grep -cF -- "Do not add entries here" knowledge/glossary.md; true`.
> - (i)=2 AND (ii)=0 → run Task B.
> - (i)=0 AND (ii)=1 AND (iii)=1 → pointer already landed INTACT (a pre-commit death); go to Task C, and re-derive the MATCH proof by running Task B's compare in CHECK-ONLY mode against `git show HEAD:knowledge/glossary.md` (the pre-retirement bytes are TRACKED and unchanged pre-plan — the overwrite lost only the working copy, never the history).
> - Any other combination (a torn pointer: (ii)>=1 with (i)>0 or (iii)=0) → HALT and report all three values.
>
> **Task B — completeness-guard then pointer-ize (python heredoc, guard IN the control flow).** ONE script, run from the Task-A toplevel, that (1) parses `knowledge/glossary.md` (RELATIVE) into its `## <term>` sections — asserts exactly 2 (design note (d)); (2) parses `/Users/marklehn/Developer/GitHub/GLOSSARY.md` (READ-ONLY) sections `## <term> [project: lessons-forge]` — term matched as a LITERAL string (`Gate 1 (routing)` contains parentheses; never treat it as a pattern); (3) for each of the 2 old terms: the central body must equal the old body after per-line trailing-whitespace strip and outer blank-line strip — ANY mismatch or missing term → SystemExit naming every offending term, NO write; (4) only then overwrites `knowledge/glossary.md` with the pointer:
>
> ```
> # Glossary — lessons-forge (RETIRED → pointer)
>
> **This file is retired.** Both entries migrated VERBATIM to the central
> glossary at `/Users/marklehn/Developer/GitHub/GLOSSARY.md` under
> `[project: lessons-forge]` tags (proposals 378 + 389 — the CEO's
> one-central-glossary ruling; plans 542 + 543, PT v4.93, 2026-08-26).
> Do not add entries here: new lessons-forge domain definitions go to the
> central file, tagged `[project: lessons-forge]`. The migration-completeness
> proof (both bodies matched at retirement) is in this plan's dev note.
> ```
>
> Post-write: `/usr/bin/grep -cF -- "RETIRED" knowledge/glossary.md` == 1 AND `/usr/bin/grep -c "^## " knowledge/glossary.md; true` == 0 (regex form — Task A's caret warning) AND the script's `MATCH <term>` lines (2 of them) pasted into the dev note; MEASURE and RECORD `wc -l knowledge/glossary.md` in the dev note.
>
> **Task C — dev note + commit.** Write `knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md`: the branch taken, the 2 MATCH lines, post-write probes, recorded `wc -l`. Commit (ONE compound, cd-first, no amend — the WORKTREE toplevel, never the live tree): `cd "$(git rev-parse --show-toplevel)" && git add knowledge/glossary.md knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md && git commit -m "[<id from your plan filename>] lf-glossary-pointer(lf-glossary-pointer-2026-08-26): knowledge/glossary.md retired to pointer (completeness-proven, 2 MATCH)" -- knowledge/glossary.md knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md && git rev-parse HEAD`. The hash is **CAPTURE_COMMIT**; separate compound: `git show <CAPTURE_COMMIT> --numstat --format=` — exactly the two files (mismatch → report loudly).
>
> **Deposits:**
> - `knowledge/glossary.md`
> - `knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md`
>
> **Scope:**
> - `knowledge/glossary.md`
> - `knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md`

## STEP 2 — QA (verify against the COMMITTED state)

> **Item 1 — committed extraction.** `cd "$(git rev-parse --show-toplevel)"` (Task A's worktree law applies to QA too); `git show <CAPTURE_COMMIT>:knowledge/glossary.md` to a `/private/tmp/` scratch path; probes against the EXTRACTION (raw → `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/probes-raw.txt`): `"RETIRED"` == 1; `^## ` count == 0 (regex form, never `-F`); `"[project: lessons-forge]"` >= 2; `"plans 542 + 543"` == 1; `wc -l` EQUALS the dev note's recorded value (read the dev note; compare — never a plan-predicted number). Then `cmp` the extraction against the live file (exit 0 — no drift).
> **Item 2 — completeness proof re-run.** Re-run Task B's parse-and-compare in CHECK-ONLY mode against the CENTRAL file and the PRE-RETIREMENT glossary extracted via `git show <CAPTURE_COMMIT>^:knowledge/glossary.md` — both `MATCH` lines again, from the parent commit's bytes.
> **Item 3 — commit hygiene.** `git show <CAPTURE_COMMIT> --numstat --format=` pasted (exactly 2 files); `git rev-parse --show-toplevel` printed; reflog window `-n 4` → 0 amends.
> **Item 4 — write the receipt** `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/qa-receipt.md`: per-item table with expected/measured/✅, then the Rule 20 block.
>
> ⚠️ **Gate note (pre-declared):** probe-battery QA, NO pytest scope (Test Scope: none). `qa_test_result` will report "no parseable pytest summary" — the known-benign class; the Planner overrides with reference to this clause and the evidence files (8th precedent).
>
> **Deposits:**
> - `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/qa-receipt.md`
>
> **Scope:**
> - `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/qa-receipt.md`

Rule 20 banner (byte-exact, inside the QA receipt's verification section):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```

## Drafting Cycle

**Tier:** T1 — one doc retirement; clone of 543's post-fold form (every 543 walk fold carried from birth: worktree law, regex entry-count, torn-pointer predicate, control-flow completeness guard, recorded-not-predicted counts). Two-walk form, no panel; a direction-class finding escalates to Fork C.

**Walk register:** `lessons-forge/knowledge/research/walk-register-lf-glossary-pointer-2026-08-26.md`

**Walk 0 (context pin, measured):** old glossary 10 lines / 2 entries; central `[project: lessons-forge]` == 2; consumer sweep 0 `.py` hits; id prediction 544; the 543 clone-diff stated (NO wrap.md edit — the ordering precondition already satisfied shop-wide by 543; this is the W2 half only). Design notes (a)–(e) clone-carried, incl. the literal-string term match for the parenthesized `Gate 1 (routing)`.

**Walks:**
- Weak spots:          w1 dry — probes re-read; the Task-A triple partitions ((i)=2∧(ii)=1 falls to the HALT arm); the two pointer-text probes measured against the drafted pointer body (2 and 1).
- Destruction:         w1 1 folded — branch-2 re-entry (death between the overwrite and the commit) could not reproduce the MATCH proof against a pointer-ized working copy: the recipe now names `git show HEAD:knowledge/glossary.md` as the pre-retirement source (tracked, unchanged pre-plan — only the working copy was overwritten).
- Vulnerabilities:     w1 dry — guard fail-closed on mismatch/missing; literal-string term match for the parenthesized `Gate 1 (routing)`; root read-only.
- Integration-record:  w1 dry — pointer names 542+543; open_forks carries the siblings; register single-line ref; the halted-425/499 artifacts in this decisions/ prove the daemon watches this lane.
- ACID:                w1 dry — one commit, two files; sentinels 10/2/2/0 consistent.
- **Walk 1 total: one finding, folded.**
- Weak spots:          w2 dry — the folded branch-2 recipe re-read; its `git show HEAD:` source verified reachable (the file is tracked and clean at authoring).
- Destruction:         w2 dry — all death states land in exactly one predicate; the folded recipe closes the pre-commit gap.
- Vulnerabilities:     w2 dry.
- Integration-record:  w2 dry — manifest yields/validation filled from the real runs at conformance time.
- ACID:                w2 dry.
- **Walk 2 total: 0 findings — all five lenses dry.**

**Closing:** ✅ **BAR MET at walk 2 — dry confirming pass, all five lenses.** T1 two-walk form; no direction-class finding; close is MANUAL (CEO-lane verdicts).

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: lessons-forge/knowledge/glossary.md
class: app-feature
reads: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/glossary.md, /Users/marklehn/Developer/GitHub/GLOSSARY.md, /Users/marklehn/Developer/GitHub/bellows/knowledge/decisions/Done/executable-543.md
writes: knowledge/glossary.md, knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md, knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/probes-raw.txt, knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/qa-receipt.md
open_forks: the three grandfathered migrations + their CLAUDE.md re-points (own plans); ELUVIAN_PATH.md L131 (rides the wrap); the project-tag-on-lessons ruling (awaiting the CEO)
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A
