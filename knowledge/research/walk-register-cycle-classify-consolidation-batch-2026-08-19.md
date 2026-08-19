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

## Walk 2 — first pass over the authored steps. NOT DRY.

**Findings: 3. Instruction-class 3.** Two pre-existing, one introduced by this walk's own fold and caught by the tool immediately.

| id | lens | finding | resolution |
|---|---|---|---|
| w2-1 | ⛔ 2 Destruction (2.3) | ⛔ **THE DESTRUCTION GUARD POINTED AT A PIN THAT DID NOT EXIST.** Three sections cited *"the three report shas from §Numbers"* — pre-flight, Step 2's before/after guard, and QA item 3. **Measured: those shas appear ZERO times in the plan.** They existed only in the walk register. The guard protecting three shipped artifacts — on the step whose mishandling **halted the clone origin** — had nothing to compare against, and its before/after check would have compared nothing to nothing and passed. | **M8** added with all three sizes and hashes, and **M9** for today's report (ABSENT → exists, and none of M8). |
| w2-2 | 1 Weak spots (1.2) | **M7 said `[AUTHOR-CONFLICT]` markers `≥ 5` with NO probe and no statement of WHICH entries** — an unverifiable pin sitting on this plan's most conflicted surface, the one place the author's interest and the artifact's integrity diverge. | A real probe, and the five identified by measurement: every entry dated 2026-08-19. |
| w2-3 | 3 Vulnerabilities (3.2) | **My own w2-2 fold hard-coded `id > 353` and an id range `366–370`.** `353` is `P0` — it silently becomes wrong the moment a proposal is added — and `370` collides by value with `E0`. ⚠️ **And selecting the five by ID RANGE is wrong in principle**: contiguity is a coincidence of ingest order, while `entry_date = '2026-08-19'` is the property that actually defines them. | `P0` bound from pre-flight; selection by date, with the reasoning stated so a later walk does not "simplify" it back to an id range. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds.

⚠️ **w2-1 is the sharpest kind of defect this cycle produces: a guard that would have PASSED while measuring nothing.** It is the same class as plan 456's w5-1 (a sentinel outside the population it guarded) and w8-2 (a post-condition only its author could verify). **Three instances now, across two plans, all of them checks that fail open rather than closed** — and none visible to `plan_lint` or `propagation_check`, both of which read a coherent sentence citing a section that exists and are satisfied.

⚠️ **w2-3 is the second time in two walks that MY OWN FOLD introduced the defect class the fold was fixing** (w1-3/w1-4 the same). The tool caught it within seconds both times. That is the argument for running the checks after every fold rather than at the end of a walk — which is now this cycle's actual practice.

## Walk 3 — confirming pass. NOT DRY.

**Findings: 2. Instruction-class 2. Both fold-introduced by walk 2, and both are the class that killed the clone origin.**

Run by enumerating **every path in every probe** and asking which resolve against CWD — the question 425 lost on.

| id | lens | finding | resolution |
|---|---|---|---|
| w3-1 | ⛔ 3 Vulnerabilities (3.1) | **M9's probe was `ls reports/lessons-report-2026-08-19.md` — a bare RELATIVE path**, added by walk 2's own fix for the missing sha pins. ⚠️ **In the one plan whose clone origin HALTED on worktree path resolution.** In the worktree it measures the sandbox copy; from main it measures a different file; **either way it returns a plausible answer and looks like it worked.** | Worktree-anchored `"$(pwd)/reports/…"`, matching M8, with the irony recorded so it is not undone. |
| w3-2 | 1 Weak spots (1.3) | The pre-flight asserted `entry_id > 345`. That boundary is correct **only because it happens to equal the pre-456 corpus size** — an artefact of ingest history, not a property of the batch. | Bind the `W` work-list ids: the defining property. *(Third instance of this shape in two walks — w2-3 was the id range, this is the id boundary.)* |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds.

⚠️ **Both findings were introduced by walk 2's folds, and walk 2's folds were themselves fixing a fails-open guard.** Three walks in, the pattern in THIS plan is unambiguous: **every fold so far has introduced its own successor.** w1-3/w1-4 → w2-3 → w3-1. The tools catch the restatement class immediately; the path-resolution and defining-property classes need a targeted read, and I only found these two by deliberately enumerating paths rather than reading prose.

⚠️ **Worth carrying to the honing notes:** the mechanical checks are now demonstrably good at *"is this number stated twice"* and blind to *"does this path resolve where you think"* and *"is this boundary the real property or a coincidence"*. Those two classes have produced **five** findings across plans 456 and this one, every one of them a guard that would have passed while measuring the wrong thing.

## Walk 4 — confirming pass. NOT DRY. ⚠️ Includes a TOOLING near-miss of my own.

**Findings: 2 in the plan, plus 1 process failure by the Planner.**

| id | lens | finding | resolution |
|---|---|---|---|
| w4-1 | 1 Weak spots (1.2) | **M2 is unpinnable — `K`, the proposal count, cannot be predicted — yet QA item 1 said "re-run every pin in table order".** An unpinnable row read as a check, so a correct run would have produced an unresolvable QA line. **Identical to plan 456's w4-3**, where a gated status distribution would have false-halted on the CEO's own next action. | M2 marked **RECORD-ONLY**; QA item 1 scoped to **gated** pins. |
| w4-2 | 5 ACID (5.2 Consistency) | ✅ **The plan had a guarantee available from its own machinery and was not using it.** `get_unclassified_entries()` returns entries with no non-stale proposal, so **M1 == 0 entails that each of the `W` entries acquired at least one** — i.e. **`K` ≥ `W` is DERIVABLE**. The plan declared `K` simply "not predictable" and asserted nothing. **An unpinnable quantity is not an unconstrained one.** | `K` ≥ `W` derived from the inversion and asserted in QA — a real bound that costs no prediction. |

### ⚠️ Planner process failure, recorded because it nearly shipped a half-state

The fold script for w4-1/w4-2 **died at parse time** (a `SyntaxError` from an awkward triple-quoted literal) — so **neither fold applied.** But a *second* script in the same invocation ran successfully and rewrote **QA item 1** to say *"M2 is RECORD-ONLY"*.

**The plan was therefore left asserting, in QA, a property its Numbers table did not state** — a half-state produced by my own tooling, in which the two halves of one fold disagreed. It was caught only because I read the error output instead of the exit line.

**The lesson, and it is not about Python:** *a multi-part fold must apply atomically or not at all.* Both plan 451 and 456 relied on that property — every batch there asserted before writing, so a bad anchor discarded the whole batch. **Here I split one fold across two invocations and lost the atomicity without noticing.** The half-state is closed; the guard is to keep each fold's edits in a single asserted batch.

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds — both re-run **after** the half-state was closed, not before.

## Walk 5 — confirming pass. NOT DRY. A DROPPED CLONE HUNK, found five walks late.

**Findings: 2. Instruction-class 2. Both pre-existing since v0.** Applied as **one atomic batch**, per walk 4's lesson.

| id | lens | finding | resolution |
|---|---|---|---|
| w5-1 | ⛔ 4 Integration-vs-record (4.1) | ⛔ **THE CLONE DROPPED 425's `DISPOSITION` LINE ENTIRELY — measured, zero occurrences.** 425 wrote one per entry (`DISPOSITION \| entry=… \| proposal=… \| remedy: … \| markers: …`) and its QA grepped for it. ⚠️ **It is the only artefact that makes an ABSENT marker auditable**: without it, a missing `[DEDUP]` is indistinguishable from a `[DEDUP]` the classifier never considered — silence reads identically to judgement. **My walk-0 clone-diff did not catch this**, and it is exactly what a clone-diff exists for. | Restored and scaled to `W`: one line per entry, `markers: NONE` an expected value, post-condition `grep -cF 'DISPOSITION \| entry=' == W`, plus a QA re-check. |
| w5-2 | 1 Weak spots (1.3) | **The three disclosure markers were treated asymmetrically with no statement of why.** 425 asserted all three present because its single entry warranted all three; this plan pins only `[AUTHOR-CONFLICT]`. A reader comparing the two would read the difference as an omission. ⚠️ **And it must NOT be "fixed" by pinning all three** — `[DEDUP]` and `[REMEDY-GATED]` are conditional, so a count pin would force the classifier to fabricate markers to hit a number, exactly the failure `K` is unpinned to avoid. | The asymmetry stated in the plan: `[AUTHOR-CONFLICT]` is **deterministic** (the 2026-08-19 entries, pinned as M7); the other two are **conditional**, recorded raw and gated on nothing. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN**, both after the fold.

⚠️ **w5-1 is a walk-0 failure surfacing at walk 5.** The clone-diff at walk 0 compared inherited FACTS — batch size, hazard classes, baselines — and recorded five as false. **It did not enumerate 425's ARTEFACTS and ask which the clone had failed to carry.** A dropped hunk is invisible to a fact-by-fact diff, because an absent thing states nothing to be wrong about. That is the same asymmetry w5-1 itself is about: **absence does not announce itself, in a clone-diff any more than in a marker set.**

**Carried for the honing notes:** a clone-diff needs two passes, not one — *are the inherited claims still true* (done at walk 0) **and** *which of the parent's artefacts are simply not here* (not done, and it took five walks to notice). Plan 456's clone-diff had the same shape and may carry the same gap.

## Walk 6 — the ARTEFACT pass w5-1 said walk 0 never did. NOT DRY.

**Findings: 4 in the plan + 1 process failure by the Planner.** All four plan findings are **artefacts 425 carries that this clone dropped** — none visible to the fact-by-fact diff run at walk 0, and none findable by either tool.

**Method:** enumerated 23 distinctive artefacts/mechanisms named in 425 and counted each in the clone. Seven scored zero in BOTH (they were 423's, not 425's — correctly absent). Four scored high in 425 and **zero here**.

| id | lens | finding | resolution |
|---|---|---|---|
| w6-1 | 4 Integration-vs-record | **No sentinel.** 425 names one 8 times; this clone had none. It converts *"classification writes only `lesson_proposals`"* from an assertion into a measurement, for one query. | **M10** — corpus entry 345, `8df4331b…`, unchanged. *(Continuous with plan 456's sentinel, so the chain holds across the arc.)* |
| w6-2 | 2 Destruction (2.1) | **`STALE_COUNT` not captured.** 3 rows (ids 98/121/130) — a population **distinct from M6** that a stray UPDATE would move invisibly. | **M11**, gated unchanged. |
| w6-3 | 5 ACID (5.2) | **`SURFACEABLE_BASE` not captured** — and 425 insisted it be *"labelled distinctly from NT"*. Here it is **0** and **expected to become `K`**, since every proposal this plan writes is `proposed`. ⚠️ Gating it would false-halt a correct run; omitting it loses the baseline. | **M12**, RECORD-ONLY, with the distinction from M6 stated. |
| w6-4 | 4 Integration-vs-record (4.2) | ⚠️ **AN INHERITED DECISION WHOSE REASON NO LONGER HOLDS.** 414 clustered six entries via Flag (G); **425 collapsed that apparatus explicitly *because its batch was one*.** This clone inherited the collapsed form **without re-deciding it, on a batch of `W`** — so the classifier gets no instruction about relatedness across 25 entries that include four on drafting-cycle mechanics and two on cold-seat conduct. | **Not folded into a cluster mechanism** — inventing one at walk 6 would be novel machinery in a T1 clone. **Recorded as a deliberate, explicit omission** for Gate 1 and the next clone, rather than left as an unexamined default. |

### ⚠️ Planner process failure — the same trap, one plan later

Checking whether a sentinel was warranted, I ran `'lesson_entries' in inspect.getsource(insert_proposal)` and got **True**, and briefly treated classification as writing to `lesson_entries`. **It does not** — the matches are **docstring lines** documenting the FK. The only SQL is `INSERT INTO lesson_proposals`.

**This is precisely plan 456's w3-1**, where `'conn.commit()' in source` matched three docstrings saying the function does *not* commit. I recorded that finding, wrote a lesson about it, ingested that lesson into the corpus **today** — and committed the identical error one plan later. **A substring test over source is a probe against prose, not behaviour**, and knowing that has now demonstrably failed to prevent it twice. The check that works is reading the SQL.

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds.

**The method itself is the carry-forward:** the artefact pass took one command and found four real gaps at walk 6 that five prior walks and two tools missed entirely. **It belongs at walk 0 of every clone**, alongside the fact-diff — which is exactly what w5-1 concluded, now with a measured yield behind it.

## Walk 7 — confirming pass. NOT DRY. FIVE PINS THAT COULD NOT FAIL.

**Findings: 1, instruction-class, spanning five pins.** Found by a mechanical question neither tool asks: **is every declared pin actually exercised by a step?**

| id | lens | finding | resolution |
|---|---|---|---|
| w7-1 | ⛔ 1 Weak spots (1.2) | ⛔ **M8, M9, M10, M11 and M12 were declared in `## Numbers discipline` and referenced by NO step.** M8/M9 were reachable only through the prose *"the three report shas from §Numbers"*; **M10, M11 and M12 were reachable through nothing at all** — declared at walk 6 and wired to no check anywhere. **Five pins that could not fail.** | All five wired: M10/M11/M12 into the pre-flight, Step 1's post-conditions and QA 3b; M8/M9 named **by symbol** in Step 2's destruction guard and QA item 3 rather than by prose. Orphan check now returns **none**. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds.

⚠️ **This is the exact MIRROR of w2-1, and I created it while fixing w2-1.**
- **w2-1:** three checks cited pins that did not exist → the guard compared nothing to nothing and passed.
- **w7-1:** five pins existed and no check cited them → the pins could never fail.

Both are the same defect in a declaration/consumer pair, and **each of my folds fixed one half while creating the other.** Walk 2 added M8/M9 to satisfy the checks and left them prose-linked; walk 6 added M10–M12 and wired them to nothing.

⚠️ **The general form, and it is a real gap in this shop's tooling:** `plan_lint` verifies plan STRUCTURE and `propagation_check` verifies that quantities are not RESTATED — **neither asks whether a declared pin has a consumer, or whether a cited pin has a declaration.** That is a bidirectional reachability check over one table, it is ~15 lines, and across two plans it would have caught w2-1 and w7-1 — both of them guards that pass while measuring nothing.

**Recorded for the honing notes as a concrete tool proposal**, not just an observation: extend `propagation_check` with a **pin-reachability detector** — every `| Mn |` row must be referenced by at least one step, and every `§Numbers`-citing sentence must name a symbol that exists.

## Walk 8 — the STRUCTURAL pass. NOT DRY. A third dropped hunk.

**Findings: 1, instruction-class, pre-existing since v0.**

| id | lens | finding | resolution |
|---|---|---|---|
| w8-1 | ⛔ 1 Weak spots (1.1) | ⛔ **Step 3 had NO dispatch-state probe and NO PROCEED gate. 425 carries BOTH** — it added them specifically to fix its own scout finding S1-6 (*"steps 2 and 3 had no dispatch-state probe and no PROCEED gate, so a bellows re-dispatch would re-run the generator with no idempotency branch"*). **The clone carried the parent's fix into Step 2 and dropped it from Step 3.** Consequences: a re-dispatch re-runs QA with no idempotency branch, and Step 3 begins **regardless of whether Step 2 succeeded**. | Both restored, with the omission and its cause recorded in place. Per-step audit now: Step 1 probe ✓, Step 2 probe ✓ + gate ✓, Step 3 probe ✓ + gate ✓. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN**.

⚠️ **THIS IS THE THIRD DROPPED HUNK, AND IT ESCAPED THE PASS BUILT TO CATCH DROPPED HUNKS.**
- **w5-1** found the `DISPOSITION` line missing — and concluded walk 0's fact-diff cannot see absences.
- **w6** ran an **artefact pass** over 23 named mechanisms and found four more.
- **w8-1** was invisible to that artefact pass too, because **"has a dispatch-state probe" is not a keyword — it is a STRUCTURAL PROPERTY OF A STEP.** Enumerating vocabulary finds missing *nouns*; it cannot find a missing *guarantee*.

**So a clone-diff needs three passes, not two:**
1. **Facts** — are the inherited claims still true? *(walk 0; found 5 false)*
2. **Artefacts** — which of the parent's named mechanisms are absent? *(walk 6; found 4)*
3. **Structure** — does each step still have the properties the parent gave every step? *(walk 8; found 1 — and it was the parent's own scout fix)*

Each pass found what the previous one structurally could not. **Recorded for the honing notes**: the third pass is a per-step matrix — dispatch probe, PROCEED gate, scope block, deposits block, post-conditions — cheap to run and mechanically checkable, which makes it a better candidate for tooling than for discipline.

## Walk 9 — the full structural matrix. NOT DRY.

**Findings: 2, instruction-class, both pre-existing, both in Step 3.**

Walk 8 found one structural gap by checking one property. This walk ran the **full matrix** — eight per-step properties across all three steps of both plans — which is what walk 8's conclusion actually implied.

| property | 425 s1/s2/s3 | mine (before) | |
|---|---|---|---|
| dispatch probe | Y/Y/Y | Y/Y/Y | ✓ *(fixed at w8-1)* |
| PROCEED gate | -/Y/Y | -/Y/Y | ✓ |
| single-writer | Y/-/- | Y/-/- | ✓ |
| Scope / write list | Y/Y/Y | Y/Y/Y | ✓ |
| **visible chat message** | Y/Y/Y | **Y/Y/-** | ⛔ **w9-1** |
| post-conditions | Y/Y/Y | Y/Y/Y | ✓ |
| absolute DB path | Y/-/- | Y/-/- | ✓ |
| **explicit pathspec** | -/-/Y | **Y/Y/-** | ⛔ **w9-2** |

| id | finding | resolution |
|---|---|---|
| w9-1 | Step 3 carried no visible-chat instruction; Steps 1 and 2 do, and 425 has it in all three. | Restored. |
| w9-2 | ⛔ **Step 3 declared two deposits and never said how to commit them.** Steps 1 and 2 both mandate `git add` **by explicit pathspec** and forbid `git add -A`; 425 carries the rule in its Step 3. **A `git add -A` in a worktree QA step would sweep whatever else the tree holds** — and this plan's Step 2 writes a report into that same tree. | Restored as QA item 5, with the renumber of the `git show --stat` check. |

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN** after the folds. Matrix now uniform on both properties.

⚠️ **Both gaps are in Step 3, and so was w8-1 — three of the last four findings.** The pattern is not random: **Step 3 was cloned last and least carefully**, and every pass so far has been aimed at the steps that DO something. A QA step that verifies is easy to treat as inert, but it commits files and runs in the same worktree as the step it verifies.

⚠️ **One honest note on the matrix itself:** it also shows where the clone is BETTER than the parent — my Steps 1 and 2 carry the pathspec rule and 425's do not. **A structural diff is not a checklist of the parent's virtues; it is a comparison, and the divergences point both ways.** Recording that so the third pass is not mis-applied as "make it identical to the parent".

## Walk 10 — the SEMANTIC pass. NOT DRY.

**Findings: 2 folded, 1 suspected defect KILLED BY MEASUREMENT.** Both folds are pre-existing since v0 and neither is visible to any of the three structural passes — they are about what the instructions MEAN, not what they contain.

| id | lens | finding | resolution |
|---|---|---|---|
| w10-1 | 2 Destruction (2.3) | **The destruction guard detects an overwrite and names no recovery.** Step 2 can overwrite a shipped report; the guard takes shasums before and after — and if the post-check fires, the plan tells the agent nothing about undoing it. ⚠️ **Detection without recovery is half a guard**, and HALT ROUTING's "never repair forward" would leave an overwritten artifact in place. | ✅ **Measured: all three reports are TRACKED in git**, so the restore point already existed — `git checkout -- reports/<file>`. **Named in one line; no backup copy added, and the plan now says none should be.** |
| w10-2 | 4 Integration-vs-record (4.4) | ⚠️⚠️ **A SHOP LESSON THAT GIVES THE WRONG ANSWER IF APPLIED MECHANICALLY HERE.** `cycle_date` was justified only as *"can only be wrong by inheritance"*. But this shop carries a lesson — and `accepted\|codify` proposal **352** — instructing an author to **measure the date at authoring and never inherit it**. An agent applying that rule would recompute `cycle_date` from `date -u` and be **wrong**: 352 governs a date describing *when the work happens*, while `cycle_date` names *which cycle the report belongs to*, fixed when the batch was assembled. **The two rules point in opposite directions and the plan did not disambiguate them.** | Stated explicitly: the plan's cycle date is correct even on a later dispatch; do not recompute. The original inheritance hazard retained. |

**Killed by measurement, not folded:** I suspected the plan had **no restore point at all** — `grep -i restore` returned three hits, all of them incidental prose (*"restored from 425"*, *"walk 6 restored"*). That part was right. **But the conclusion "therefore add a backup copy" was wrong**, because `git ls-files` shows all three at-risk reports are tracked. **The gap was documentation, not machinery** — and folding a scratch-copy backup would have added a second restore point where one already existed.

⛔ **Bar NOT met.** `plan_lint` **exit 0**, `propagation_check` **CLEAN**.

⚠️ **w10-2 is the most transferable finding of this cycle.** Every other defect has been something missing or mis-stated. This one is a **correct, shipped, CEO-routed shop rule that produces a wrong action in a specific context** — and nothing in the drafting cycle asks *"which of our own rules would mislead an agent reading this instruction?"*. The three structural passes check the plan against its parent; the tools check it against itself. **Neither checks it against the shop's standing doctrine, which is precisely what an executing agent brings to it.**
