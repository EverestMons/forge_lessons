# Lessons Forge — Cycle Run 2026-08-19, PLAN B: classify the consolidation batch and deposit the report (Gate-1 routing held to Plan C)

**Date:** 2026-08-19 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — classify) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1 — T-8 (clone of `executable-425`).
**Slug:** `cycle-classify-consolidation-batch-2026-08-19`
**Project:** lessons-forge
**Author:** Planner
**dispatch_mode:** bellows
**Priority:** 1

## CEO Context

**Classify only.** This plan classifies the **`W`** unclassified corpus entries that plan **456** ingested, and deposits the cycle report. **It routes nothing.** Every proposal it creates leaves `route` **NULL** and `status` **`proposed`**; Gate-1 routing is **Plan C** and belongs to a NON-AUTHOR.

⚠️⚠️ **THE AUTHOR-CONFLICT IS LARGER HERE THAN AT ANY PRIOR CYCLE, AND IT IS THE REASON THIS PLAN EXISTS SEPARATELY.** 425 classified **one** entry and flagged it `[AUTHOR-CONFLICT]`. This batch contains **five entries the Planner wrote on 2026-08-19**, each arguing for a change to `DRAFTING_CYCLE.md` or `PLANNER_TEMPLATE.md` that the Planner authored, evidenced, proposed the remedy for, and benefits from — including the retirement of PT v4.89's project-bin arm. **The classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner.** Every proposal derived from those five carries the `[AUTHOR-CONFLICT]` disclosure marker, and the plan asserts their presence mechanically rather than trusting the agent to have thought about it.

**Clone lineage — measured, not recalled:** 423 (Plan A) → **425 (Plan B, the direct origin)** → 427 (QA-only corrective) → 428 (Gate-1 write). ⚠️ **425 is HALTED and is still sitting in `decisions/` as `halted-executable-425.md`.** Cloning a halted plan is legitimate here — its steps 1 and 2 completed with every gate passing — but the reason it halted is inherited machinery and is re-stated below rather than left to be rediscovered.

### ⚠️⚠️ WHY THE CLONE ORIGIN HALTED — inherited and re-measured 2026-08-19

1. ⛔ **THE WORKTREE ABSOLUTE-PATH TRAP — this is what killed 425.** Its Step 2 mandated `output_dir` as *"an ABSOLUTE path rooted at `/Users/marklehn/Developer/GitHub/lessons-forge/reports`"*. That is the **MAIN repo's** reports directory. The agent runs in a worktree, so the report was written **outside the sandbox**, leaving an untracked file in main that teardown's merge then refused to overwrite — `worktree_teardown` aborted and the plan halted with Step 3 never running. **The instruction was a fix for a real hazard (`output_dir` defaults to a CWD-relative `reports`) that prescribed a remedy worse than the disease.** ⚠️ **The rule, verbatim from 425's step-2 verdict: in a worktree-isolated dispatch an absolute path must be anchored at `pwd` (the worktree root), NEVER at the main repo root. The fix for CWD-relative is not "absolute" — it is "absolute WITHIN the sandbox".** Re-verified 2026-08-19: `lessons-forge/.git` exists and `.bellows-worktrees/` is present, so worktree isolation **does** apply to this project.
2. **`insert_proposal` DOES NOT COMMIT** — the caller must, exactly as `ingest_lesson_entries` does not (plan 456's w7-1, proven there on a scratch copy: 370 in-connection vs 345 after close-without-commit). ⚠️ **And the same corollary applies: verify post-conditions on a FRESH connection**, because a read on the writing connection returns the expected values from inside an uncommitted transaction whether or not the commit landed.
3. **THE REPORT DIRECTORY IS DESTRUCTIBLE.** `lessons-forge/reports/` holds `lessons-report-2026-08-13.md`, `-08-14.md` and `-08-15.md`. 425 pinned the prior report's sha before and after; that guard is inherited and the pin is re-measured at walk 0.
4. **THE CLASSIFY-PLAN INVERSION — the definitive proof the work happened.** After classification `get_unclassified_entries()` must return `[]`. ⚠️ 425's clone had **dropped** this check and its walk-0 clone-diff restored it; it is the one post-condition that cannot be satisfied by a partial run.
5. **THE BATCH IS `W`, NOT 1.** 425 classified a single entry. `W` is measured at walk 0 below, and the ids are contiguous.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared** (honing-notes P-5). Every other section references a symbol.

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | **`W`** work list | **25** (ids 346–370, contiguous) | **0** | `len(get_unclassified_entries(conn))` — the inversion, on a FRESH connection |
| M2 | **`P0`** proposals | **353** | `P0` + `K` — ⚠️ **`K` is NOT predictable and is NOT pinned**; classification may emit 0..n per entry | `select count(*) from lesson_proposals` |
| M3 | route on every NEW proposal | — | **NULL, every one** | `select count(*) from lesson_proposals where id > P0 and route is not null` → **0** |
| M4 | status on every NEW proposal | — | **`proposed`, every one** | `select count(*) from lesson_proposals where id > P0 and status <> 'proposed'` → **0** |
| M5 | **`E0`** corpus entries | **370** | **370 — UNCHANGED** | this plan classifies; it must not ingest |
| M6 | pre-existing non-terminal set | `{340,342,346,350,352}` | **still present, untouched** | the live Gate-2 queue must not move |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **≥ 5** | one per Planner-authored entry; **presence asserted mechanically, adequacy left to Gate 1** |

⚠️ **`K` is deliberately unpinned and that is not laziness.** A classifier that must hit a predicted proposal count is a classifier under pressure to fabricate or suppress. **What is pinned is the SHAPE of every proposal it emits (M3, M4, M7), never how many.**

## Scope

Mutates one artifact — the corpus at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — plus the declared deposits and one new report. ⚠️ **Look-alikes, measured:** `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0-byte decoys**; `forge/forge.db` is a **real 61.6 MB database from a different project**. Do **not** route any proposal, do **not** re-ingest, do **not** touch `LESSONS.md`, `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`, and do **not** overwrite any existing report.

## HALT ROUTING

*(v0 — to be authored at walk 1.)*

## STEP 1 — Lessons Agent: classify

*(v0 — to be authored at walk 1.)*

## STEP 2 — DEV: the report

*(v0 — to be authored at walk 1. ⚠️ This is the step that killed 425. `pwd` FIRST; output anchored at the worktree root; prior-report shas pinned before and after.)*

## STEP 3 — QA

*(v0 — to be authored at walk 1. ⚠️ Name a `.txt` deposit — and note that `qa_test_result` STILL cannot pass, because it requires a parseable pytest summary and this plan runs no suite. See plan 456's step-2 verdict: the failure is structural, not a defect.)*

## Drafting Cycle

**Walk 0 (context pin):** register `lessons-forge/knowledge/research/walk-register-cycle-classify-consolidation-batch-2026-08-19.md`. Clone-diff against **425 (halted)** run BEFORE lens 1; five inherited facts recorded, the halt cause identified as a plan defect and re-verified live. `W` **25** (ids 346–370) · `P0` **353** · `E0` **370** · worktree isolation **CONFIRMED** (`lessons-forge/.git` present) · reports dir holds three destructible artifacts. **Direction verdict pending walk 1.**
