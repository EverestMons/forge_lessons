# Walk Register — cycle-ingest-consolidation-batch-2026-08-19

`schema_version: 0.3`

Plan: `lessons-forge/knowledge/decisions/drafts/WIP-cycle-ingest-consolidation-batch-2026-08-19.md` (project **lessons-forge**). Tier **T1** (T-8 clone of `executable-423`).

## Walk 0 — context pin (five DC §2.0 measurements + the mandated clone-diff)

**(1) Newest same-class.** `Done/` listed by ship date: 428 (Gate-1 routing write) and 427 (QA corrective) are newer but are **not cycle runs**; **423** is both direct clone origin and newest same-class cycle plan.
**(2)–(3) The batch, measured two independent ways.** A real `ingest_lesson_entries` dry run against a `cp`-made scratch DB: **`inserted 25 / updated 0 / unchanged 288`**. Content-hash set difference against the live corpus: the same **25**. Parser total **313**.
**(4) Provenance.** 11 entries pre-date this session (2026-08-16/18, incl. a parallel terminal's), 9 are plan 451's appends, 5 were written today.
**(5) Pins.** `E0` **345** · `P0` **353** · sentinel `76b1b344…` · `DRAFTING_CYCLE.md` v2.11 sha `acce7ebe…`.

### Clone-diff against 423 — seven inherited facts, five FALSE
1. Batch **25**, not 1. 2. Em-dash regime **inverted** (10 of 25 carry ` — ` vs 423's 0 of 1). 3. New hazard: a **backtick inside a heading** plus 4 apostrophes; 423's was a double quote. 4. Baselines moved (344→345, 352→353). 5. Sentinel moved. 6. ✅ **STILL TRUE — the non-terminal set is unchanged at `{340,342,346,350,352}`**, recorded explicitly *because* it survived. 7. Doctrine pin unchanged at v2.11.

## Walk 1 — all five lenses. Direction verdict: **PROCEED**.

**Findings: 6. Instruction-class 6 / record-class 0. Pre-existing 6 of 6** (v0's steps were stubs).

| id | lens | finding | resolution |
|---|---|---|---|
| w1-1 | 4 Integration-vs-record | ⚠️ **423's criterion-1 verdict is false on BOTH stated operands.** It called criterion 1 *"doubly unfalsifiable"* because PT carries 0 `**Tag:**` lines and the entry's tags were NULL. Measured: **PT carries 1** occurrence, and **all 25 entries carry tags.** The conclusion survives only by a **third reason neither plan stated** — `_TAG_LINE_RE.match(line.strip())` anchors at line start and PT's occurrence is mid-line prose at :1967, so `ref_tag_sets` builds empty. **The guard went from two operands to one without anyone noticing.** | G-DUP now **asserts `ref_tag_sets` is empty at run time** instead of inheriting it. One line-initial `**Tag:**` added to PT would mark all 25 duplicate at once. |
| w1-2 | 1 Weak spots | Steps 1 and 2 were stubs. | Authored from 423's machinery: Step 0 dispatch-state, single-writer check, backup + `?immutable=1` verify, before-anchor commit, pre-ingest guard, one mutation, G1–G7, deposit. |
| w1-3 | 3 Vulnerabilities (3.1) | A batch heading contains a **backtick** and four contain apostrophes — a class 423 never faced. A double-quoted shell probe would command-substitute it. | `grep -F` with single-quoted patterns mandated in the step preamble, with the hazard named. |
| w1-4 | 1 Weak spots (1.2) | `detect_duplicates` **cannot answer pre-mutation and answers anyway** — `row is None: continue` returns `[]` for un-ingested ids, a confident false zero on a HALT condition. *(Carried from 423, verified still true against the live code at `:363–369`.)* | Criterion 2 mirrored by hand. ✅ **Improvement over 423: 10 entries take the separator path and 15 the fallback, so each path is an in-batch control for the other.** 423 had only the fallback and no control. |
| w1-5 | 4 Integration-vs-record | Plan 451 failed `qa_test_result` because its Deposits named no `.txt`. | Both steps now name a `.txt` deposit explicitly, citing 451. |
| w1-6 | 5 ACID (5.1 Atomicity) | ⚠️ **A "dry run" here is not dry.** `ingest_lesson_entries` contains a `conn.commit()`, so a caller's `rollback()` cannot be relied on. Measured honestly: in my invocation the rollback **did** hold (scratch returned to `E0` = 345, live corpus untouched at 345) — **but whether that `commit()` fires depends on a branch I did not trace, and a safety property resting on an untraced branch is not a safety property.** | Fresh `cp` per dry run; assert the copy equals `E0` before use; never hand the live DB to a call described as dry. |

**Direction verdict: PROCEED.** The angle is right — a measured clone of a proven cycle plan, ingest-only, with the scope boundary (no classification) guarded by G2 rather than asserted in prose. No finding invalidates the clone origin, the mechanism, or the premise licensing scope.

⛔ **Bar NOT met** — six instruction-class findings. Walk 2 is a first pass over the newly authored steps.

## Walk 2 — first pass over the newly authored steps. NOT DRY.

**Findings: 5. Instruction-class 5 / record-class 0. Fold-introduced 5 of 5** (walk 1 authored the steps this walk reads).

**Both mechanical checks were run first, and between them they found four of the five.**

| id | lens | finding | resolution |
|---|---|---|---|
| w2-1 | 1 Weak spots | ⛔ `plan_lint` **FAIL (b) step 2 deposits** — I wrote Step 2's Deposits inline (`**Deposits:** \`a\` **and** \`b\``), which yields **zero** parsed paths. ⚠️ **This is plan 451's S1-3(b) defect re-introduced in a different shape, one step after I cited it in the same document.** Step 1 used bullets and passed with 2 paths; Step 2 did not. | Bullet-list form, with the parser dependency named so it is not re-broken. |
| w2-2 | 1 Weak spots | `plan_lint` **FAIL (c)** — I paraphrased the Rule 20 close as *"the `PASSED` line"*. The gate matches the literal `PASSED — SELF-CHECK PASSED`. | Both literals written out, with "matched literally" stated. |
| w2-3 | 4 Integration-vs-record | `plan_lint` WARN — the Cycle Log named no lenses, so §3's per-lens record was absent. | Five lens bullets added. |
| w2-4 | 3 Vulnerabilities (3.2) | ⚠️⚠️ **`propagation_check` reported `CLEAN` on a plan it could not read.** `declared symbols: (none found)` — this plan's Numbers table declares `\| N1 \| batch size \| — \| **25** \|`, with no backticked symbol, so `declared_values()` matched nothing and detector (1) ran over an empty declaration set. **A clean report across zero declarations is the exact failure mode the tool exists to prevent** — the same shape as its `instruction_region` bug: silent, total, indistinguishable from success. | **Tool fixed**: zero parsed declarations is now **exit 2 (could not run)**, never CLEAN, with the expected row form printed. Regression-tested — shipped plans 432, 451 and 411 still exit 0. Plan's table amended to declare `**\`N1\`**`. |
| w2-5 | 4 Integration-vs-record | Found by the repaired tool on its first real run: the **title** hard-coded *"the 25-entry consolidation batch"*, and the CEO Context restated **25**. A count in a title is the literal that goes stale — measured on plan 451, whose register moved 298 → 299 between authoring and dispatch. | Both restated against `N1`; the count now lives only in the Numbers table. |

⚠️ **CORRECTION — the line originally committed here said `propagation_check` was "clean and now provably able to read this plan". That was FALSE and is struck.** It was written from a run taken *before* the w2-5 fold, and it asserted a clean result on the strength of a run whose declaration set had just changed. Re-run immediately after: **15 divergences.**

| id | finding | resolution |
|---|---|---|
| w2-6 | ⚠️ **The repaired tool immediately found 15 restatements of the batch count that had been in the plan since walk 1** — the Execution header, the CEO Context, the inherited-facts block, the em-dash note, the criterion-1 and criterion-2 text, the arm-1 foreign-writer check, and both classification assertions. **Every one predates this walk; none were new.** The earlier `CLEAN` was exactly the false negative w2-4 describes — the tool could not see `N1`, so detector (1) compared against nothing. | 14 restatements folded to `N1`. |
| w2-7 | ⚠️ **Tool false positive: `propagation_check` flagged the very Numbers-table row it parsed the declaration FROM.** A correct single-declaration table read as a divergence — the self-referential trap that also bit plan 451's freeze checklist at w7-3, where the placeholder sweep halted on its own wording. | **Tool fixed**: declaring lines are recorded at parse time and skipped by detector (1). Regression-tested — 451 and 411 still exit 0. |

⛔ **Bar NOT met — 7 findings, all instruction-class.** After the folds: `plan_lint` **exit 0** (one deliberate WARN — no Closing line, the cycle is open) and `propagation_check` **CLEAN, verified by a run taken after the final fold, not before it.**

⚠️ **The lesson I will not soften: I committed a clean-gate claim sourced from a stale run.** The plan's own doctrine is *earn the clean gate, do not author it*, and I authored one — in the walk register, about a tool I had just changed. **A verification result is only valid for the artifact state it was taken against**, and a fold invalidates it exactly as it invalidates a probe.

**Worth naming:** four of five findings came from tools, not from reading — and the fifth (w2-5) came from a tool that had to be repaired first. The one class reading caught nothing of. This is the honing-note P-4 thesis holding on a second, unrelated plan.
