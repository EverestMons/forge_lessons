# Walk Register — cycle-classify-consolidation-batch-2026-08-19

`schema_version: 0.3`

Plan: `lessons-forge/knowledge/decisions/drafts/WIP-cycle-classify-consolidation-batch-2026-08-19.md`. Tier **T1** (T-8, clone of **`halted-executable-425`**).

## Walk 0 — context pin

**Lineage, measured:** 423 (Plan A, ingest) → **425 (Plan B, classify — HALTED, the direct origin)** → 427 (QA-only corrective) → 428 (Gate-1 write for proposal 353). Plan **456** is this arc's Plan A and closed clean.

**Why the origin halted — read from its own step-2 verdict, not inferred:** 425's Step 2 mandated `output_dir` as an absolute path **rooted at the MAIN repo**. The agent runs in a worktree, so the report was written outside the sandbox; teardown's merge refused to overwrite the untracked result, the plan halted, and **Step 3 never ran**. The instruction was a fix for a real hazard (`output_dir` defaults CWD-relative) that prescribed a **remedy worse than the disease**. Re-verified 2026-08-19: `lessons-forge/.git` exists and `.bellows-worktrees/` is present — **worktree isolation does apply.**

**Pins:** `W` **25** (ids 346–370, contiguous) · `P0` **353** · `E0` **370** · NT `{340,342,346,350,352}` · reports dir holds **three** shipped artifacts (`08-13` 12,212 B `7cfd7904…`, `08-14` 7,256 B `f1807cf2…`, `08-15` 2,593 B `b2128116…`) and **no** `lessons-report-2026-08-19.md` · `generate_lessons_report(conn, cycle_date, output_dir='reports')`.

## Walk 1 — all five lenses. Direction verdict: **PROCEED**.

**Findings: 6. Instruction-class 6.** ⚠️ **Four of six were caught by the two mechanical checks within seconds of the steps being authored.**

| id | lens | finding | resolution |
|---|---|---|---|
| w1-1 | 1 Weak spots | Steps 1–3 were stubs. | Authored from 425's machinery, with its halt cause designed around rather than inherited. |
| w1-2 | 4 Integration-vs-record | ⛔ `plan_lint` FAIL — Step 2's Deposits written inline, yielding **zero** parsed paths. ⚠️ **My THIRD instance of this exact defect: plan 451 (S1-3(b)), plan 456 (w2-1), and here — each time within a document that CITES the previous one.** Reading the lesson has now failed three times where a lint run succeeded three times. | Bullet form, with the parser dependency and the repetition recorded in the plan. |
| w1-3 | 3 Vulnerabilities (3.2) | `propagation_check` flagged three restatements of `E0` = 370. **All three are FALSE POSITIVES** — two cite plan 456's measurement (a different plan's numbers) and one is the entry-**id** endpoint 370. ⚠️ **But the collision is real in the document too**: `E0` (a COUNT) and the top entry **id** are the same number by coincidence, and a reader can conflate them exactly as the tool did. | Prose disambiguated at all three sites; the id/count collision named explicitly. **The tool's limit recorded: it matches numerals by VALUE and cannot distinguish a count from an id or from another plan's citation.** |
| w1-4 | 3 Vulnerabilities | `propagation_check` parsed **`proposed` as a numeric symbol with value 0**, polluting the symbol table — M4's cell used the ``**`x`**`` + `**N**` shape the declaration regex keys on, for a row declaring a status string rather than a quantity. | M4 reworded. **Fixed in the plan, not the tool** — the tool's pattern is correct for real declarations; the plan was mimicking a declaration it did not mean. |
| w1-5 | 4 Integration-vs-record | `plan_lint` WARN — the Cycle Log named no lenses. | Five lens bullets added. |
| w1-6 | 5 ACID (5.1) | **The single-commit design creates a resume guarantee 425 could not express.** Committing once after all `W` inserts means the work list is only ever `W` or 0 — so **a strict subset is positive evidence of a foreign writer and a HALT**, not an ambiguity. With a batch of one, 425 had no intermediate value and no such check. | RESUME defined by three explicit arms keyed to the work list. |

**Direction verdict: PROCEED.** Nothing invalidates the clone origin (halted, but for a cause now understood and designed around), the mechanism, or the premise licensing scope.

⛔ **Bar NOT met** — six instruction-class findings. `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both after the folds.
