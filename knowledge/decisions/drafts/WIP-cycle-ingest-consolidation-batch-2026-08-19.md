# Lessons Forge — Cycle Run 2026-08-19, PLAN A: ingest the 25-entry consolidation batch (classification held to Plan B)

**Date:** 2026-08-19 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest the 25) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1 — T-8 (clone of `executable-423`). No T-4: read-mostly, single INSERT-only ingest, dry-run rehearsable against a scratch DB copy.
**Slug:** `cycle-ingest-consolidation-batch-2026-08-19`
**Project:** lessons-forge
**Author:** Planner
**dispatch_mode:** bellows
**Priority:** 1

## CEO Context

**Ingest only.** This plan takes the **25** un-ingested `LESSONS.md` entries into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**; Gate-1 routing is a third plan after that.

⚠️ **Why the split matters more here than it did at 423.** Five of the 25 entries were written by the Planner **today**, and they are the evidence base for changes to `DRAFTING_CYCLE.md` and `PLANNER_TEMPLATE.md` that the Planner authored, evidenced, and benefits from — including the retirement of PT v4.89's project-bin arm. **The corpus path exists so a NON-AUTHOR routes them at Gate 1.** That is the entire reason this plan exists instead of a direct doctrine edit, and a 25-entry batch containing the author's own proposals is the strongest case yet for keeping ingest, classification and routing in three separate plans.

**Clone lineage — measured, not recalled:** … → 411 → **423** (direct origin AND newest same-class cycle plan; `Done/executable-423.md`, closed 2026-08-14). Verified by listing `lessons-forge/knowledge/decisions/Done/` by ship date: 427 and 428 are newer but are a QA-corrective and a Gate-1 routing write, not cycle runs.

### ⚠️⚠️ INHERITED FACTS FROM 423 THAT ARE FALSE HERE — every one re-measured 2026-08-19

1. **THE BATCH IS 25, NOT 1.** Verified two independent ways: a real `ingest_lesson_entries` dry run against a `cp`-made scratch DB returned **`inserted 25 / updated 0 / unchanged 288`**, and a content-hash set difference against the live corpus returned the same 25. Parser total **313**.
2. ⚠️ **THE EM-DASH REGIME IS INVERTED.** 423 recorded *0 of 1* headings carrying ` — `, so duplicate detection rested **entirely** on the fallback path. Here **10 of 25** carry it — the primary path runs for 10 and the fallback for 15. **423's "rests entirely on the fallback" note is FALSE here and must not be carried.**
3. ⚠️ **A NEW HOSTILE CHARACTER CLASS 423 NEVER FACED: a BACKTICK inside a heading.** Measured: 1 double quote (423's hazard), **4 apostrophes**, and **1 backtick** — and the backtick entry carries both: `` 2026-08-18: `plan_lint`'s dryness check disagrees with §2's bar… ``. Any shell-interpolated probe over that heading must use `grep -F` with single-quoted patterns; a double-quoted shell string would command-substitute the backticks.
4. **BASELINES MOVED:** `E0 = 345` (423: 344), `P0 = 353` (423: 352).
5. **THE SENTINEL MOVES** to `2026-08-19: A knowledge destination that is not ingested cannot improve the system…`, content-hash `76b1b344208b36f99b80ecda8a878aab8825c0a5901650b38c572b574bce0125`.
6. **STILL TRUE, verified not assumed — the non-terminal proposal set is UNCHANGED at exactly `{340, 342, 346, 350, 352}`.** 423's G1 value guard carries as written. ⚠️ Recorded explicitly *because* it is the one inherited fact that survived; an unverified carry-forward is what the clone-diff exists to catch.
7. **DOCTRINE PIN UNCHANGED:** `DRAFTING_CYCLE.md` is still **v2.11**, sha `acce7ebe6fa4f145bd7440485e45a0e66b650a1e`.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared** (honing-notes P-5). Every other section references a symbol.

| id | pin | before | after | probe |
|---|---|---|---|---|
| N1 | batch size | — | **25** | dry run `inserted`, cross-checked by content-hash set difference |
| N2 | corpus entries `E0` | **345** | `E0` + 25 = **370** | `select count(*) from lesson_entries` |
| N3 | `would_update` | — | **0** | ⚠️ **the invariant. Non-zero → HALT**: an ingested row's body changed |
| N4 | unchanged | — | **288** | dry run `unchanged` |
| N5 | proposals `P0` | **353** | **353 — UNCHANGED** | this plan classifies nothing; any growth is a scope breach |
| N6 | non-terminal set | `{340,342,346,350,352}` | identical | G1 value guard, keyed by id |
| N7 | parser total | **313** | 313 | `parse_lessons_md` on the register |

## Scope

Write to exactly one artifact: `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. ⚠️ **The corpus is `lessons-forge/lessons-forge.db`** — sibling `forge.db` and `lessons.db` are 0-byte decoys that return false absences. Do **not** classify, do **not** create proposals, do **not** write a cycle report, do **not** touch `LESSONS.md`, `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`.

## HALT ROUTING

*(v0 — to be authored at walk 1: the A0 measured-precondition gate in 423's form, its arms, and the dry-run-before-live rehearsal.)*

## STEP 1 — DEV: ingest the batch

*(v0 — to be authored at walk 1.)*

## STEP 2 — QA

*(v0 — to be authored at walk 1. Evidence must be raw command output; name a `.txt` in Deposits or the `qa_test_result` gate cannot pass — the defect plan 451 hit.)*

## Drafting Cycle

**Walk 0 (context pin):** register `lessons-forge/knowledge/research/walk-register-cycle-ingest-consolidation-batch-2026-08-19.md`. Clone-diff against 423 run BEFORE lens 1; seven inherited facts re-measured, **five false, one still true, one unchanged doctrine pin**. Batch **25** verified two ways · dry run `25/0/288` · `E0` 345 · `P0` 353 · non-terminal set unchanged · em-dash regime inverted · new backtick hazard. **Direction verdict pending walk 1.**
