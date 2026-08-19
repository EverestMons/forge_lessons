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

## Walk 3 — first pass over walk 2's folds. NOT DRY.

**Findings: 3. Instruction-class 3 / record-class 0.** ⚠️ **Both mechanical checks were GREEN before this walk and stayed green after it — every finding came from READING the code the plan depends on.** The tools have drained what they can see; this is the residue they structurally cannot.

| id | lens | finding | resolution |
|---|---|---|---|
| w3-1 | 3 Vulnerabilities (3.2) | ⚠️⚠️ **w1-6's stated reason is FALSE, and it is the exact trap this plan criticises 423 for.** Walk 1 claimed `ingest_lesson_entries` "contains a `conn.commit()`" so a caller's rollback could not be trusted. Traced at walk 3: **all three `conn.commit()` occurrences (`lessons_forge.py:127, :212, :436) are DOCSTRING SENTENCES stating the function does NOT commit.** My walk-1 probe was `'conn.commit()' in source` — **it matched prose.** The function leaves the transaction to the caller; the rollback that worked did so correctly, not by luck. ⚠️ **Inherited-fact 7 of this very plan faults 423 for a claim whose reason was false and whose conclusion survived — and I did the same thing one walk later, in the same document.** | Reason corrected in place, not deleted. **The guard stays** (a fresh `cp` per dry run is cheap and kills a class of resume ambiguity) but is now labelled defence-in-depth rather than a fix for a commit that does not exist. |
| w3-2 | 5 ACID (5.3 Isolation) | **G1 and G2 are not independent of the mutation they verify.** `ingest_lesson_entries` marks proposals `stale` and flags terminal-status proposals **only inside its UPDATE branch** (`:160–194`), and the stale UPDATE excludes terminal statuses — i.e. it targets **exactly the non-terminal set G1 pins**. The gates are safe here *only because* `N3` is 0. Unstated, a G1 failure would read as corpus corruption when it could be correct behaviour. | The coupling is now named at the gate: read a G1 failure alongside `N3` before calling it damage. |
| w3-3 | 4 Integration-vs-record (4.2) | **`N1`, `N4` and `N7` are absolutes, and nothing said they were deliberate.** On plan 451 absolutes over a growing register were a false-halt bug that cost two walks to remove. **An ingest inverts that**: the fingerprint and the whole pre-ingest duplicate audit were computed over one specific set of `N1` headings, so a grown register means the evidence no longer covers what would be ingested. Left unexplained, a later walk would "fix" them into deltas and **delete the guard while believing it was applying a lesson.** | Marked ABSOLUTE ON PURPOSE, with the 451 contrast stated and a mismatch defined as a re-scope signal rather than a defect. |

⛔ **Bar NOT met** — three instruction-class findings. `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both re-run **after** the folds.

⚠️ **The pattern across walks 2 and 3 is worth carrying.** Walk 2: six of seven findings came from tools. Walk 3: **zero** came from tools and all three came from reading source. The two are not substitutes — the tools drain restatement and form, and leave untouched every claim about *what the code actually does*. w3-1 is the sharpest case: a tool could never have caught it, because the defect was a **probe that matched prose**, and the fix was to read the function.

## Walk 4 — confirming pass. NOT DRY.

**Findings: 3. Instruction-class 3 / record-class 0. Pre-existing 3 of 3** — none descend from walk 3's folds. Both mechanical checks green before and after; all three came from reading, as at walk 3.

| id | lens | finding | resolution |
|---|---|---|---|
| w4-1 | 1 Weak spots (1.1) | ⛔ **§Scope said "Write to exactly one artifact" while the plan writes SIX** — the corpus, the `.backup`, and four declared deposits. §HALT ROUTING's own authorized-writes line already said three classes, so the document contradicted itself across two sections. **An agent following §Scope literally would skip its deposits and fail `deposit_exists` and `deposit_uncommitted`** — the pair of gates plan 451 already burned a verdict on. | §Scope restated as *one MUTATED artifact plus backup plus four deposits*, and made to **reference** the authorized-writes list rather than restate it. One declaration. |
| w4-2 | 3 Vulnerabilities (3.1) | **Three look-alike DB paths were described in two places in terms that read as a contradiction.** §Scope called `forge.db` a 0-byte decoy; Step 1 (inherited from 423) called `forge/forge.db` "REAL but DIFFERENT". **Measured: both are true of different files** — `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0 bytes**, while `forge/forge.db` is a real **61.6 MB** database from another project. The two hazards are not the same: a decoy gives a false ABSENCE; the real one gives a **wrong answer from real data**, which no emptiness check would catch. | Both stated together with measured sizes and the distinct failure mode of each. |
| w4-3 | 5 ACID (5.2 Consistency) | **The baseline status distribution was written as eight gated absolutes.** A Gate-1 routing between authoring and dispatch legitimately moves them — and **that is precisely what this arc is waiting on the CEO to do.** ⚠️ Unlike `N1` (w3-3), a moved proposal status does **not** invalidate the batch: the ingest is over `lesson_entries`, so proposal state is orthogonal and gating on it is a pure false halt. | **Record raw, gate only on the SUM equalling `N5`** — which is what actually protects the no-classification boundary. Walk-0 reading kept for comparison, explicitly not for matching. |

⛔ **Bar NOT met** — three instruction-class findings. `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both re-run after the folds.

**Note on w4-3, because it nearly shipped:** this plan spent walk 3 arguing that `N1`'s absolutes are *deliberate* and must not be softened. Walk 4 found a different set of absolutes in the same document that must be softened, for the opposite reason. **The rule is not "absolutes are good" or "absolutes are bad" — it is whether a change in the value invalidates the plan's evidence.** For `N1` it does; for the proposal distribution it does not. Applying w3-3 mechanically across the document would have preserved a false halt sitting directly in the path of the CEO's own next action.

## Walk 5 — confirming pass. NOT DRY.

**Findings: 3. Instruction-class 3 / record-class 0. Pre-existing 3 of 3** — the third consecutive walk whose findings all came from **reading**, with both mechanical checks green before and after.

| id | lens | finding | resolution |
|---|---|---|---|
| w5-1 | 1 Weak spots (1.2) | ⛔ **THE SENTINEL WAS THE WRONG ENTRY — the canary was outside the population it guards.** Walk 0 pinned the **last parsed REGISTER entry** (`2026-08-19: A knowledge destination…`, hash `76b1b344…`). Measured: that heading has **0 corpus rows** — it is a **batch** entry. 423's sentinel was an **already-ingested** row (its entry 344), which is the entire point: the sentinel proves the ingest touched no pre-existing data. Pre-ingest there was nothing for mine to match, so the Step 1a-bis check was incoherent and **G5 would have verified nothing while reporting PASS.** | Corrected to **corpus entry 345** — `2026-08-14: A residual "everything else" bucket…`, hash `8df4331b…`. **Verified earnable:** exactly 1 register match, hash equal to the corpus. *(It is the very entry 423 ingested — the sentinel chain is continuous.)* ⚠️ Its heading carries a **double quote**, 423's own hazard class, so probes over it must be `grep -F` single-quoted. |
| w5-2 | 1 Weak spots (1.2) | **G4 carried a clause with no probe:** *"confirm no pre-existing `content_hash` changed"*. The baseline captures **no hash manifest**, so nothing could satisfy it — an unverifiable gate clause reads as rigour and delivers none. | Removed and replaced by the traced guarantee: the **only** write path to an existing row's `content_hash` is the UPDATE branch (`:160–168`) that increments `updated`, so **`updated == 0` IS the guarantee**, not a proxy for it. |
| w5-3 | 4 Integration-vs-record | G5 read only *"sentinel intact"* — no entry id, no hash, no statement of what it proves. | Names entry 345, its hash, and why the check is meaningful only for an already-ingested entry — so the w5-1 defect cannot be reintroduced by a later reader. |

⛔ **Bar NOT met** — three instruction-class findings. `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both after the folds.

⚠️ **w5-1 is the most serious finding of this cycle and it survived four walks and two green tool runs.** It is a **false-PASS gate**: not a check that fails wrongly, but one that succeeds while measuring nothing. Neither tool can see this class — `plan_lint` reads form, `propagation_check` reads restatement, and both are satisfied by a coherent sentence about the wrong object. **The only detector was asking what the sentinel is FOR and then checking whether the pinned entry could do that job.**

**Cycle yield: 6 → 7 → 3 → 3 → 3.** Pre-existing: 6 → 1 → 3 → 3 → 3. **Unlike plan 451's tail, this cycle's findings are NOT fold damage — they are original defects in the authored steps, surfacing at a steady three per walk.** That is not convergence; it is a plan whose machinery is dense enough that each read reaches a new part of it.

## Walk 6 — confirming pass. NOT DRY.

**Findings: 3. Instruction-class 1 / record-class 2. Fold-introduced 2 of 3** — the first fold damage this cycle has produced, and it is concentrated in one place: **the Cycle Log**.

| id | lens | finding | resolution |
|---|---|---|---|
| w6-1 | 4 Integration-vs-record | ⚠️ **The Cycle Log's ACID bullet still asserted the claim walk 3 DISPROVED** — *"a dry run is not dry; `ingest_lesson_entries` commits (w1-6)"*. w3-1 traced all three `conn.commit()` hits to docstrings saying the function does **not** commit, and corrected the step body — **but not the lens summary.** A false factual claim was left standing in the plan's own account of itself, cited to a superseded finding. | Bullet rewritten to carry the w3-1 correction plus w3-2 and w3-3, so the lens summary states what the cycle now believes rather than what it believed at walk 1. |
| w6-2 | 4 Integration-vs-record | The walk-0 line still read *"Direction verdict pending walk 1"* six walks after walk 1 returned **PROCEED**. | Corrected, with the fold count. |
| w6-3 | 1 Weak spots (1.3) | **Step 2 item 4 asserted `get_unclassified_entries()` returns an `N1`-id list.** That function is **not scoped to this batch** — it returns every corpus entry lacking a non-stale proposal. The assertion is correct **only while the pre-existing unclassified count is zero**, which the plan never stated and never measured. Measured at walk 6: **`UNCLASSIFIED_BASE` = 0**, so it holds today — by luck of the corpus's state, not by construction. | `UNCLASSIFIED_BASE` added to the Step 1a baseline capture; item 4's expectation is now **computed** as `UNCLASSIFIED_BASE + N1`, never hard-coded. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both after the folds.

⚠️ **Two structural notes worth carrying.**

**1. The Cycle Log is invisible to both tools, by design.** `propagation_check.instruction_region()` deliberately excises the `## Drafting Cycle` section as record, and `plan_lint` checks only that lens lines and a Closing line exist — never whether their content is true. **So the one region of a plan that summarises what the cycle believes is the one region no mechanical check reads.** Both of w6-1 and w6-2 lived there, and w6-1 was a false factual claim, not a stale number. That is a real gap in the tooling story and belongs in the honing notes rather than being folded silently.

**2. w6-3 is the third instance this cycle of one specific shape** — after w1-1 (423's criterion-1 reason false on both operands) and w5-1 (the sentinel outside its population): **a correct conclusion resting on an unstated operand that nobody measured.** The conclusion holds each time; the reasoning does not; and the guard degrades silently the moment the unmeasured operand moves. This cycle has now found it in an inherited fact, in a gate's subject, and in a helper's scope.

**Cycle yield: 6 → 7 → 3 → 3 → 3 → 3.** Pre-existing: 6 → 1 → 3 → 3 → 3 → 1.
