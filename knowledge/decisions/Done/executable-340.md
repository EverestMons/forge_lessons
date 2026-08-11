# Lessons Forge — Cycle Run 2026-08-10, PLAN B: classify the 41 ingested entries, deposit the report

**Date:** 2026-08-10 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (classify tranche A) → Step 2 (tranche B) → Step 3 (tranche C) → Step 4 (DEV — report) → Step 5 (QA) | **qa_steps:** 5 | **pause_for_verdict:** always
**cycle_tier:** T2

## CEO Context

**Classification and report only.** Plan A (id 339, closed 2026-08-10) ingested the 41 un-ingested `LESSONS.md` entries; this plan turns them into proposals and deposits the report. Gate 1 (route disposition) and Gate 2 (codification) remain separate plans with CEO decisions between.

### What Plan A established, and what this plan may therefore assume — each item RE-VERIFIED at authoring, not inherited

| fact | measured now, read-only |
|---|---|
| the 41 entries exist | ids **266–306**, `MAX(id)` 306, `sqlite_sequence` agrees |
| **no proposals exist for them** | `entry_id > 265` → **0 rows**; `MAX(lesson_proposals.id)` still **273** |
| the work list | `get_unclassified_entries()` = **exactly 266…306, ascending** |
| the Gate-2 queue | **42** `accepted\|codify`, 21 `DRAFTING_CYCLE.md` / 21 `PLANNER_TEMPLATE.md` |
| `STALE_COUNT` | **3** (proposals 98/121/130 — the settled plan-204 artifacts) |
| `SURFACEABLE_BASE` | **0** — no `proposed` or `ambiguous` row exists yet |
| batch `raw_content` range | **766–2695** chars |

⚠️ **`P0` = 273 and it did NOT move, which is the whole point of the split.** Plan A's QA verified this by id; this plan re-measured it rather than reading that verification.

### ⚠️⚠️ WHY THIS IS A SEPARATE PLAN

The six-step plan these steps came from ran **eight walks**; walk 8 alone returned **55 findings** on an artifact seven prior walks had worked over, and its per-lens yield ROSE (10 → 9 → 7 → 14 → 15). The ACID lens's isolation map named the cause: six steps behind five verdict gates over one shared store produce a **seven-window guard matrix**, and nearly every HIGH finding lived there. **Plan A took the one destructive step and its window; this plan holds the rest.**

⚠️ **This plan contains NO destructive write.** `insert_proposal` only adds rows. There is no ingest, no `UPDATE`, no delete, and no path by which it can stale the 42. Its risk is **false halts costing dispatches**, not damage — and that is the risk profile the split was chosen to separate.

⚠️⚠️ **THREE FINDINGS DEFERRED AT PLAN A'S DEPOSIT LAND HERE, AND ARE FOLDED.** At that deposit the Planner stated each carried walk-8 finding was "either resolved by the split — it lived in Steps 2–6 — or record-class." Three lived in Steps 2–6 and are therefore this plan's, folded at authoring rather than left as inherited residue: **the QA step had no dispatch-state determination** (a bare daemon retry re-emits the register block and duplicates the row); **the deposit-completion resume could not regenerate flag (G)'s token**, which is not stored in any DB column, so a transient death guaranteed a QA ❌ three gates later; and **two self-reports halted on exactly what their own pre-flights continue.**

⚠️ **`Test Scope: targeted` — re-verified, not inherited.** `find . -name "test_*.py"` returns exactly ONE file, `src/test_lessons_forge.py`, so `python3 -m pytest src/` is simultaneously the targeted and the full run. **`--collect-only` measured 55 at authoring** — report the actual.

**Tier: T2, inherited and NOT down-tiered.** T-2 fires (production-data mutation) and computes T1. The plan is a direct derivation of a T2 artifact, and §2.6 is explicit that a "bounded" or "proven-clone" framing is not licence to down-tier. It is also derived from a cycle that **did not converge** — ten findings from walk 8 remain unfolded in the parent and are enumerated in the committed walk register.

---

### ⚠️⚠️ NUMBERING — the collision band survives the split

- **`lesson_entries.id` 266–306** — the 41 entries, ALREADY CREATED by Plan A. This plan never writes them.
- **`lesson_proposals.id` 274–314** — the 41 proposals this plan creates.
- ⚠️⚠️ **Every numeral in 274–306 names BOTH an existing entry and a proposal this plan creates, and they are NOT paired.** The pairing is `entry 266+k → proposal 274+k` (offset **+8**), so entry 274 pairs with proposal 282, not proposal 274. **Never write a bare number in 223–314 without its namespace.**
- **`lesson_proposals.id` 223–273** — PRE-EXISTING. **223–273 includes the 42 `accepted\|codify` rows of the queued Gate-2 batch (non-contiguously — nine ids inside that span are NOT members). Do not touch any of them.** ⚠️ The lower bound is **223, not 232**: a 232 bound leaves proposals 223–231 — nine members of the protected 42 — outside the rule.

**Tranche map — DERIVED FROM THE LIVE WORK LIST at authoring, not predicted:**
- **Tranche A (Step 1):** entries **266–279** (14) → proposals 274–287.
- **Tranche B (Step 2):** entries **280–293** (14) → proposals 288–301.
- **Tranche C (Step 3):** entries **294–306** (13) → proposals 302–314.

⚠️ These matched the parent's authoring-time prediction exactly, **but the prediction is not the operand: `get_unclassified_entries()` is authoritative at each step**, and each tranche pins its own committed manifest before its first insert.

---

### ⚠️ Planner obligations at this plan's gates

- **At every gate, compare the `steps` table against the commit and deposit counts** before writing a verdict — `pause_for_verdict` is a header contract the runtime does not police (FORWARD 46; plan 336 executed three steps in one dispatch while the daemon recorded one).
- **The Gate-2 id list lives in Plan A's Receipt item 5** (`knowledge/development/dev-log-cycle-step-1-2026-08-10.md`, committed). Every step of this plan reads it; **nothing in this plan can reconstruct it**, and a live predicate re-read cannot detect a row that has already left the set.

**Deposit-once discipline:** to be deposited exactly once (`knowledge/decisions/` enumerated at authoring; holds `Done/` and `halted-executable-334.md` only). ⚠️ **`340` was read from `id_sequence` at deposit, not predicted at authoring** — `id_sequence` = 340 with `MAX(plans.id)` = 339, immediately after Plan A closed and consumed 339. **No filename or in-body token in this plan carries the id**, because this plan creates no backup and no id-stamped artifact; the deposit filename is the only site, so there is nothing to re-token.

**Authoring self-check:** `plan_lint.py` run **at the deposit-path resolution** (`lessons-forge/knowledge/…`, so `project_root` resolves as it will at deposit — a lint from a scratchpad path declares a different state). **Exit 0; last run at deposit.** **The measured set is SIXTEEN, in four classes, re-measured for THIS plan and not inherited from the parent's twenty-one or Plan A's twelve:**
1. **(3) the known-benign steps-mention-tests class** (Steps 1, 2 and 5) — do NOT add test files to any step's scope to silence them.
2. **(1) `T2 plan missing cold-panel line`** — **EARNED**, and phrased so it cannot be cleared by wording.
3. **(1) `closing indicates fold as last event`** — **EARNED and correct**; the Closing declares plainly that this is neither a dry close nor a bar-meeting judged stop.
4. **(11) check (p), constraints carrying no backtick-quoted check token** — the prose invariants of the trimmed ledger; C10, C12, C18 and C19 carry `Check:` tokens and do not warn.

⚠️ **A clean exit is NOT evidence the §4 block ran** — check (f) prints only on WARN, so silence on a conformant plan is correct and the discharge is a constructed positive control. ⚠️ **After any edit touching the ledger, the Cycle Log or the Closing line, re-run the linter and DIFF the WARN set against these sixteen — never re-read the count.** A WARN can DISAPPEAR when a stale record silences a live gate.

- **After Step 5, re-read `knowledge/FORWARD.md` in the MAIN tree and confirm it gained EXACTLY ONE row** matching the item the QA agent recorded emitting. Two rows, or zero, is the finding. **Do not hand-add the item** — Rule 42 authorizes status updates only, never a new row, and the daemon appends from the transcript.

---

### The 41 entries — placement scout

**Governing rule: Rule 58 — pre-stated conclusions require verification anchors and equal evidence burden.** Rule 58(2): **this table records where the Planner looked, not a distribution** — a placement absent from it is not rejected; a fourth artifact is a legitimate outcome. Rule 58(3): every disposition carries the same evidence burden; agreeing with the scout is not the low-effort path. No Rule 27 citation — no diagnostic precedes this plan.

⚠️ **Scout depth is declared, not implied (entry 291 — batch position 26 — whose whole subject is that an ordinal citation is unverifiable).** Each row was derived from the entry's **heading plus its `How to apply:` clause**, read in full; bodies were not read end-to-end. That is a heading-and-remedy scout, and it is weaker than 311's body-level read. Gate 1 owes each entry a body read before routing.

| # | entry | substance (one line) | scouted `target_artifact` |
|---|---|---|---|
| 1 | 266 | a continue verdict is one bit; a plan reading approval from advancement converts every continue into that approval | `PLANNER_TEMPLATE.md` (halt-with-options authoring) — ⚠️ **Rule 46 split; verdict-channel half is bellows-owned** |
| 2 | 267 | the confirming pass measured composition-clean and literal-dirty in the same pass | `DRAFTING_CYCLE.md` §2/§3 (yield by class) — ⚠️ **cluster (A)**, sibling of entries 306 and 294 |
| 3 | 268 | three constraints opened from the batch's own entries were breached by the folds that followed | `DRAFTING_CYCLE.md` §2.8 — sibling of entry 288 |
| 4 | 269 | `id_sequence` at authoring is a prediction; the verify-at-deposit clause must enumerate every site | `PLANNER_TEMPLATE.md` (deposit discipline) — ⚠️ this plan's own deposit step practices it |
| 5 | 270 | the untargeted confirming pass caught the record's own three-line decay | `DRAFTING_CYCLE.md` §2.7/§3 — ⚠️ **flag (D): v2.0 codified the closing-record re-read and the Cycle-Log-as-covered-region; residue is the sweep-the-tracking-lines clause** |
| 6 | 271 | the three-tranche split held classification quality — no inter-tranche cliff at 3.2× the record batch | ⚠️ likely ROUTED `reference` (calibration datum) — ⚠️ **`reference` is a ROUTE value, never a `target_artifact`: set a FILE here or leave the proposal `ambiguous`** — **this plan is its first consumer**; Gate 1 decides |
| 7 | 272 | a recognized-value enum lives in every tool that reads it — census every copy before adding one | `PLANNER_TEMPLATE.md` (multi-copy census rule) |
| 8 | 273 | argue a trade from the population the change actually touches | `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md` §2.7 — Gate 1 splits |
| 9 | 274 | a truth-restoration edit is held to its own standard in both directions | `PLANNER_TEMPLATE.md` (doc-correction rule) |
| 10 | 275 | a filter can silence its own evidence base — re-check coherence after every narrowing fold | `DRAFTING_CYCLE.md` §2.6 — ⚠️ **flag (D): the evidence-attack brief exists at v1.7; residue is the after-every-fold cadence** |
| 11 | 276 | a specified test fixture can FORCE a guard-weakening | `DRAFTING_CYCLE.md` §2.2 (destruction) or `PLANNER_TEMPLATE.md` (test authoring) |
| 12 | 277 | a checker's mechanics approximate its condition; the gap fires in both directions | `DRAFTING_CYCLE.md` §3 (earned-phrasing clause) — sibling of entry 301 |
| 13 | 278 | panel economics, first metered run — HIGHs come from aimed briefs | `DRAFTING_CYCLE.md` §2.6 — ⚠️ **flag (D): the seat-brief registry landed at v1.7; residue is the residue-battery cadence and the metering convention** |
| 14 | 279 | close-commit counts wrong or absent 4-for-4 — enumerate populations by PATH | `DRAFTING_CYCLE.md` §2.7 |
| 15 | 280 | the shell's cwd resets between calls; cd-first plus a toplevel assert is the whole fix | `PLANNER_TEMPLATE.md` (git-commit mechanics) |
| 16 | 281 | the Bellows verdict grammar is continue/stop only; a redo is a stop plus a corrected re-deposit | `PLANNER_TEMPLATE.md` (verdict-gate authoring) — ⚠️ **Rule 46 split** |
| 17 | 282 | a dash-leading constructed grep pattern parses as an OPTION — exit 2, empty stdout | `DRAFTING_CYCLE.md` §2.7 (beside the `grep -F` clause) |
| 18 | 283 | a nine-element compound instruction dropped exactly one element | `PLANNER_TEMPLATE.md` (per-element QA asserts) — cluster with entries 302 and 306 |
| 19 | 284 | a walk examines the WHOLE artifact, so "no walk has examined this region" is never true | ⚠️ **flag (D), strongest case: v2.0's §2 and §2.7 appear to codify this in full.** Candidate `reference`; measure clause-by-clause at Gate 1 |
| 20 | 285 | an inherited SEVERITY label survives every check that catches an inherited factual claim | `DRAFTING_CYCLE.md` §2.7 or `PLANNER_TEMPLATE.md` — **v2.0 did NOT codify it** |
| 21 | 286 | `plan_lint`'s expected-WARN set is LOCATION-dependent | `DRAFTING_CYCLE.md` §5 (record the exit code *and* the resolution it was taken at) |
| 22 | 287 | a sweep whose fixes quote what they fixed can never be verified by a count reaching zero | `DRAFTING_CYCLE.md` §2.7 (verify by classification, not count) |
| 23 | 288 | a constraint opened mid-cycle is never swept backwards over what already existed | `DRAFTING_CYCLE.md` §2.8 — sibling of entry 268 |
| 24 | 289 | a check that fails a correct run is a check an agent will loosen | `PLANNER_TEMPLATE.md` (derived expectations over constants) — sibling of entry 303 |
| 25 | 290 | a guard's stated REASON is part of the guard — correct the premise and the guard is weakened | `DRAFTING_CYCLE.md` §2.7 |
| 26 | 291 | `LESSONS.md` entries carry no numbers, so an ordinal citation is unverifiable | `PLANNER_TEMPLATE.md` (citation convention) — ⚠️ this plan's scout declares its depth because of this entry |
| 27 | 292 | a changelog says what changed, not which direction — read the diff | `DRAFTING_CYCLE.md` §2.6 (clone-diff) / §2.7 |
| 28 | 293 | folding a defect class in one plan does not immunise the next | ⚠️ **routing principle, not a doctrine clause** — ⚠️ **that is a route/disposition note, NOT a `target_artifact`: set a file or leave it `ambiguous`** — recurrence across artifacts ⇒ mechanization queue. Gate 1 decides |
| 29 | 294 | a restructuring pass resets the convergence curve | `DRAFTING_CYCLE.md` §2/§3 — ⚠️ **cluster (A)** |
| 30 | 295 | a corrected corpus measures the FALSE-positive surface and cannot measure true positives | `PLANNER_TEMPLATE.md` (census authoring) / `DRAFTING_CYCLE.md` §2.7 — sibling of entry 305 |
| 31 | 296 | measure how many DIALECTS a record has before computing anything from it | `DRAFTING_CYCLE.md` §2.7 or `PLANNER_TEMPLATE.md` |
| 32 | 297 | `pause_for_verdict: always` is a header contract nothing enforces | `PLANNER_TEMPLATE.md` (verdict-gate check: steps vs commits vs deposits) — ⚠️ **Rule 46 split; FORWARD 46** |
| 33 | 298 | when a self-marking agent returns a NEGATIVE result, the missing independence matters far less | `PLANNER_TEMPLATE.md` (verdict adjudication) |
| 34 | 299 | a census measuring PRECISION over survivors has not measured the class — RECALL decides a check | `PLANNER_TEMPLATE.md` (diagnostic authoring) / `DRAFTING_CYCLE.md` §2.1 sub-question 1.4 |
| 35 | 300 | a walk's convergence is told by what its findings TOUCH, not where they came from | ⚠️⚠️ **`DRAFTING_CYCLE.md` §2 doneness criterion — cluster (A) CENTERPIECE. FORWARD 53** |
| 36 | 301 | a gate that reads a token can be silenced by the record RETRACTING that token | `DRAFTING_CYCLE.md` §3 — ⚠️ **Rule 46 split; FORWARD 50** |
| 37 | 302 | mandates and their observers drift because they are written in different places | `PLANNER_TEMPLATE.md` (mandate names its QA item inline) — **FORWARD 52** |
| 38 | 303 | a mismatched literal probe returns a confident FALSE ABSENCE, on the verification step | `DRAFTING_CYCLE.md` §2.7 (derive the probe from the target) |
| 39 | 304 | the walk register is doctrine-ephemeral and practice-permanent | ⚠️ **`DRAFTING_CYCLE.md` §3. FORWARD 51** — the baton's NEXT #1 |
| 40 | 305 | a per-string prohibition did not hold a structural hazard; the record must leave the gate span | `DRAFTING_CYCLE.md` §3 (placement convention) — ⚠️ **Rule 46 split; FORWARD 45** |
| 41 | 306 | a task paragraph accretes correct folds until an agent acts on a subset | `PLANNER_TEMPLATE.md` (task authoring as ordered sub-items) — **FORWARD 54** |

**⚠️⚠️ STANDING FLAGS FOR GATE 1 — named so they are decided deliberately, not discovered mid-disposition:**

**(A) THE §2 DONENESS CLUSTER — entries 267, 270, 284, 294, 300 (+ 268/288 adjacent).** All bear on §2's convergence criterion, and FORWARD 53 records that criterion as **self-contradictory**: the same origin-split number is both the bar's convergence condition and the section's own noise-floor signature. Entry 300 is the centerpiece and carries the measured replacement (classify findings by the surface they touch). ⚠️ **Routing these independently would produce several surgical edits to a clause that needs one coherent rewrite.** Recommendation: Gate 1 routes the cluster as one unit.

**(B) THE FORWARD-ROW CLUSTER — entries 300, 301, 302, 304, 305, 306 map one-to-one onto FORWARD rows 53, 50, 52, 51, 45, 54.** These six are the reason this plan exists. ⚠️ **Gate 1 must reconcile each proposal against its FORWARD row rather than routing it fresh**, or the register and the corpus double-count the same owed work and each closes independently of the other.

**(C) RULE 46 CANDIDATES — entries 266, 281, 297, 301, 305.** Each pairs an authoring rule (codify) with a bellows-owned tooling defect (route to the owning register, never codify a workaround). 297 and 301 already have FORWARD rows on the bellows side (46 and 50); 305's bellows half is FORWARD 45.

**(D) PARTIALLY OR FULLY CODIFIED BY v2.0 — entries 270, 275, 278, 284.** Entry 284 is the strongest `reference` candidate; v2.0's §2 and §2.7 read as covering it in full. ⚠️ **The failure mode in both directions: a `reference` routing that discards uncodified residue, and a `codify` routing that re-lands what v1.7/v2.0 already shipped.** Each of the four is measured clause-by-clause at Gate 1, against the live file, by diff — not against the History rows (entry 292 of this batch is exactly that error).

**(E) THE PRECEDENT-POOR TAGS — `instruction-design` (3), `bellows-mechanics` (1), `probe-integrity` (1), `measurement` (1), `mechanization` (1): SEVEN entries whose tag has no corpus precedent at all.** Plus `process-discipline` (5 in batch), whose only two priors were classified `instrumentation`. These twelve classifications set precedent for every future batch and carry the higher reason-sourcing burden.

**(F) THE BATCH DESCRIBES THIS PLAN — entries 269, 271, 291, 306.** Four entries prescribe practices this plan itself executes (deposit-time id re-tokening, the tranche split, citation-by-date-and-fragment, tasks as ordered sub-items). ⚠️ **A classifier that notices this must not soften the classification to match the plan**, and the Planner must not read the plan's conformance as evidence for the proposal.

**(G) ⚠️⚠️ MECHANISM-SHAPED ENTRIES — the flag that decides whether this batch changes anything.**

**The governing argument is the batch's own: entry 293 — *a class folded twice across different artifacts is a mechanization candidate, not a lesson candidate.*** Gate 1's default disposition is `codify`, and codification produces PROSE in a doctrine file. **This plan's own drafting cycle is the evidence that prose is not enough:** §2.7's sequential-fold rule has been codified since v1.1, states its own failure mode, and explicitly names the rationalization ("this pass is just confirmation, so cumulation doesn't matter here") as a self-check target — **and this cycle violated it at walks 2 and 3 anyway, having cited it, and it was caught by the CEO rather than by the cycle.** A rule that names its own excuse and still does not bind is not a coverage problem, and routing more of the same to `codify` will reproduce it.

⚠️ **NO COUNT IS ASSERTED HERE, DELIBERATELY.** The Planner derived this set three times by three instruments and got **12, then 16, then 22** — keyword matching over the remedy text is not a classifier, and a stated figure would hand Gate 1 a precision that does not exist (batch entry 279: never trust a narrated count; entry 303: a composed probe is a hypothesis). **The TEST is the deliverable, not the tally.**

**The test, applied per entry on a body read:** *does the entry's own `How to apply:` name a concrete observable — a specific check, a named file or parser, a QA assert, or a structural convention a tool can evaluate — or does it name a discipline a human must remember?* The second is `codify`. **The first is a build candidate and routing it to `codify` converts a mechanism into a sentence.**

**The defensible core — entries whose remedy names a specific mechanism AND an owner. Gate 1 draws the real boundary; these are the ones it should not have to discover:**

| entry | the mechanism its own remedy names | owner | existing row |
|---|---|---|---|
| 283 | one mechanical QA assert per element of a compound output | authoring + QA | — |
| 286 | lint at the deposit-path resolution, not the drafting path | bellows | — |
| 291 | cite by date + title fragment so the citation is `grep -F`-able | authoring + lint | — |
| 293 | **the meta-rule: route a twice-folded class to the build queue** | Gate 1 itself | — |

**Decide entry 293 first — it is circular, and the circularity is load-bearing.** 293 is the entry that tells Gate 1 how to route the others. **If 293 itself is routed to `codify`, it becomes a doctrine sentence about routing, and the sentence has no authority over the routing decision that produced it.** Its disposition determines whether flag (G) is a live instrument or a paragraph.
| 297 | compare the `steps` table against commits and deposits at every gate | bellows | **FORWARD 46** |
| 301 | re-run the gate and diff the WARN set after any record edit | bellows `plan_lint` | **FORWARD 50** |
| 302 | each mandate names its QA item inline; construct the violation and confirm it fails | authoring + lint | **FORWARD 52** |
| 305 | bound the last step's gate span at a trailing record section | bellows `_extract_step_text` | **FORWARD 45** |
| 306 | a check counting instruction-bearing sentences per task block | `plan_lint` | **FORWARD 54** |

⚠️⚠️ **FIVE of these already have FORWARD rows, which means they have been NOTICED and not BUILT.** That is the recurrence loop stated as a measurement rather than a worry: the shop records the class, codifies a rule about it, and the class returns. **If Gate 1 routes these five to `codify`, they will have been recorded twice and built zero times.**

⚠️ **What flag (G) does NOT claim:** that `codify` is the wrong disposition for the rest. Most of the 41 are genuinely rules. It claims only that the mechanism-shaped ones need the routing decision made *deliberately*, with the owner named, rather than absorbed into a doctrine amendment because that is the default path.

**Cluster synthesis for Gate 1:** *"41 entries from sessions 24–33 — 10 `drafting-cycle`, 10 `verification`, 5 `process-discipline`, 3 each `bellows-integration` / `instrumentation` / `instruction-design`, 2 `planner-discipline`, and one each of five further tags; a FIVE-entry cluster bearing on a §2 clause its own FORWARD row calls self-contradictory; SIX entries mapping one-to-one onto open FORWARD rows; FIVE Rule 46 splits; FOUR partial-codification measurements; TWELVE classifications on precedent-poor tags; **and a mechanism-versus-discipline reading on every one of the 41, with owners named where the entry names one.**"* Do NOT skip or downgrade any.

**Do NOT dedup against `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, or `RULE_20_SELF_CHECK_BLOCK.md` during classification.** Gate 1 dedups against live doctrine; the flag-(D) measurements are handed to it, not enforced here.

---


---

## How to Run This Plan

Bellows dispatches this plan automatically when deposited; no manual bootstrap required (Rule 35).

---
---

## STEP 1 — Classification tranche A (the FIRST 14 ids `get_unclassified_entries` returns)

---

> **Before starting, read Plan A's deposit; its Receipt status must be a PROCEED-value** (`Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`) — an ALLOWLIST, not a prefix match; the in-flight stub value stops this step. **ONE additional acceptable state, and it is PLAN A's Receipt that carries it:** a status line of the halt form with **G6 as the gate token** (`Status: Partial — HALTED at G6, <reason>` — matched on the `HALTED at G6` token: an EXPLICIT, declared exemption from the no-prefix rule) WHEN the Receipt carries a `### Deferred entries (G6 candidate)` section — under bellows a halted step advances only on a CEO verdict, so THIS STEP RUNNING is itself the approval of that candidate; state that reasoning in your dev log.
>
> ⚠️⚠️ **THE APPROVAL CHANNEL IS ONE BIT: a continue issued for ANY reason — including "investigate meanwhile" — is structurally converted into deferral approval, and no step can distinguish the intents. So EVERY step running under this state opens BOTH its visible chat message AND its Receipt with: `OPERATING UNDER G6 DEFERRAL: ids <list> — if the continue verdict did not intend deferral (option ii), issue a stop now.`** The mis-conversion exposure is thereby ONE verdict gate, not the rest of the run. **Any other HALTED value stops this step.**
>
> Post a short visible chat message. You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`, ADR-002 six-value taxonomy). Same working-location + absolute-DB rules as Plan A. **Do NOT re-run the ingest. Do NOT touch proposals with id ≤ 273.**
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-10-part1.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-08-10.md`
>
> ### ⚠️ STEP 0 — DISPATCH-STATE DETERMINATION FIRST (the pre-flight branches on it; C8 applies)
>
> Probe THREE places for THIS step's own dev log `knowledge/development/dev-log-cycle-step-2-2026-08-10.md`:
> 1. `git -C <your worktree> show HEAD:<path>`
> 2. the working tree
> 3. `git log --all -- <path>` **and** `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'` — ⚠️ probe 3's exit code carries no signal; pair it with the positive control Plan A's step 0 mandates.
>
> A hit on ANY → **RESUME of this step** — recover the committed `#### Tranche manifest`; its ids are authoritative. Two sub-branches:
> - **Idempotent re-dispatch:** recovered dev log opens with a PROCEED-value AND manifest ∩ unclassified is empty AND its anchor-line count equals the manifest count → APPEND a `### Re-dispatch note`, leave the Complete receipt untouched, and STOP.
> - **Deposit-completion resume:** anchor count BELOW the manifest count with zero remaining work → reconstruct the FULL anchor list from the DB scoped to the manifest ids, AND verify/complete the tranche's OTHER deposits against their consumers' checks: the disposition lines — one per manifest proposal, missing ones regenerated from the DB rows with `reason: not recorded (regenerated on deposit-completion resume)` — ⚠️⚠️ **EXCEPT the flag-(G) `| remedy: … | owner: …` field, which is NOT stored in any DB column and therefore CANNOT be regenerated.** Re-derive it by applying flag (G)'s test to the entry's own `How to apply:` clause, exactly as the original classification would have, and mark the line `remedy: re-derived on resume`. **Do not emit a line without the field** — Step 5 row 3 fails a missing one by id, so a legitimate transient death would otherwise guarantee a ❌ three gates later — and the classifications part-file per its content spec; checked against row 3's counts and the on-disk deposit gate, then re-deposit and stop.
>
> Absent from all three → FRESH. State the determination and its evidence as the first line of your dev log.
>
> ### ⚠️ PRE-FLIGHT (all read-only, all with printed tokens — C8)
>
> 1. `get_unclassified_entries(conn)` length as a printed `UNCLASSIFIED=<n>` token — expected **41** on FRESH. **Any id outside 266–306 that is NOT named in Plan A's `### Deferred entries (G6 candidate)` section → HALT (foreign writer).** On a RESUME a smaller count is expected — the manifest, not this list, bounds the work. ⚠️⚠️ **FRESH + `UNCLASSIFIED` ≠ 41 → CONTRADICTION → HALT** (C7). List the proposals with `entry_id > 265` (report-only complement, C9's carve-out) and do NOT classify. **ONE carve-out (a CEO-approved state must not halt — C5): deferral produces a SURPLUS, not a shortfall** — FRESH + `UNCLASSIFIED` = 41 + |deferred| with EVERY extra id named in the G6-candidate section → proceed; **the tranche and its manifest are built from the NON-deferred work list only, and deferred ids are never classified.**
> 2. **Staleability guard — BRANCHED on step 0:**
>    - FRESH → **nothing of this cycle's is staleable yet; state that, run nothing, and do not report a vacuous green.**
>    - RESUME → the operand is derived from the committed MANIFEST, because the created-proposal anchor lines land in the Receipt at step END and do not exist on a mid-tranche resume: `SELECT 'STALE_IN_MINE=' || COUNT(*) FROM lesson_proposals WHERE entry_id IN (<the manifest's entry ids>) AND status='stale';` — non-zero → HALT.
> 3. **⚠️⚠️ THE GATE-2 QUEUE CHECK — new in this plan, at EVERY classification step.** **read Plan A Receipt item 5's recorded id list and compare ID-FOR-ID**, never a count:
>    ```
>    SELECT group_concat(id,',') FROM (SELECT id FROM lesson_proposals
>      WHERE status='accepted' AND route='codify' ORDER BY id);
>    ```
>    Print **`Q2_INTACT=<count>`** (a `COUNT(*)` over the same predicate — the `group_concat` query above yields the id list, not the count, and the token is consumed by Steps 2, 3, 5 and QA row 10, which must all print the same shape) **and** the symmetric difference against the recorded list, **in both directions with a verdict on each**: a recorded id absent from the live set → the arms below; **a live `accepted|codify` id absent from the RECORDED list → HALT, foreign writer — WITH ONE CARVE-OUT (C5): if that id is one of THIS cycle's own 41, it is a legitimate in-window Gate-1 codify disposition, not a foreign writer.** Record + CONTINUE, naming the ids, and carry the adjusted expectation forward. ⚠️ **Measured: plan 311's own 51 were dispositioned by Gate 1 about 23 hours after they were proposed — well inside this plan's five-gate window — so this is a live state, not a hypothetical.** The same carve-out is owed at Step 4's surfaced-count expectation and at QA rows 3 and 4, which otherwise fail a permitted outcome at four separate sites. — that is the other half of the C10 example this check cites (three staled and three gained still counts 42). ⚠️⚠️ **A COUNT OF 42 IS NOT INTACTNESS AND THIS PLAN SAYS SO IN TWO OTHER PLACES** — QA row 10 states it (a corpus that staled three of the 42 and gained three foreign `accepted|codify` rows counts 42 and is not intact, C10), and this step's own fail-closed clause states that a live predicate re-read cannot detect a row that has already left the set. **A bare `COUNT(*)` IS that live predicate re-read**, so the earlier form committed the exact fallacy the surrounding paragraphs name. **Any id in the recorded list that is absent from the live set → treat as "below 42" and adjudicate causally below, regardless of what the count says.** Expected: the 42 recorded ids, exactly. ⚠️ **This runs at every tranche because the window is five verdict gates wide and the rows are unprotected by `_TERMINAL_STATUSES`; a single whole-corpus `STALE_COUNT` check cannot distinguish which rows moved.**
>
>    ⚠️⚠️ **BELOW 42 IS NOT AUTOMATICALLY A HALT — a legitimate in-window Gate-2 codification is a PERMITTED outcome and C5 forbids failing it.** ⚠️ **Plan A Receipt item 5 missing, truncated or unparseable → HALT (`unverifiable`), with NO predicate fallback** — a live `WHERE status='accepted' AND route='codify'` re-read cannot detect a row that has already left the set, which is the entire failure this check exists to catch (C9's no-fallback rule, and the reason item 5 is recorded pre-ingest). Otherwise adjudicate causally, exactly as Step 5 row 10 does, against that id list:
>    - Every missing id now `implemented`, with its `route` still `codify`, **its `status_updated_at` LATER than the `cycle_timestamp` Plan A recorded — ⚠️⚠️ **compare LEXICOGRAPHICALLY IN SQL, never via `datetime.fromisoformat`.** The column carries two dialects (CEO flips are `...Z`; code-written rows are `...+00:00`), `cycle_timestamp` is the second, and **`fromisoformat` on this machine is Python 3.9.6, which raises `ValueError` on the `Z` form** — the throw would land on the arm whose whole job is to prevent a false HALT. A string comparison orders both dialects correctly for this purpose; if you need instant semantics, normalize `Z` to `+00:00` first and say you did, and `status_updated_by='ceo'`** → **record + CONTINUE**, naming the ids and the plan; carry the adjusted expectation forward to the later steps so they do not re-halt on the same movement.
>
>      ⚠️ **The three extra conjuncts are load-bearing and were added when this branch was re-read by the Destruction lens that follows the lens which wrote it.** The first draft of this carve-out asked only for "a Gate-2 plan visible in `knowledge/decisions/` or `Done/`" — **`Done/` holds several historical Gate-2 codifications (298, 330 among them), so that condition is satisfiable by HISTORY and would wave through exactly the corruption this check exists to catch.** The timestamp comparison is what makes the movement in-window; the actor field is what makes it deliberate.
>    - Any missing id in `stale` → **HALT** — that is the staling signature and has no legitimate in-window producer.
>    - Any missing id in any other status, or missing with no plan to attribute it to → **HALT**, naming the ids, their current status, and the pristine `.backup` (absolute path in Plan A's Receipt item 7 — this plan creates none).
> 4. `STALE_COUNT` (whole corpus) still equals Plan A's recorded baseline (3) → else HALT.
> 5. Confirm no OTHER in-progress lessons/cycle plan (main-tree glob, as Plan A).
>
> ### THE TRANCHE — PINNED BY A COMMITTED MANIFEST, NEVER RE-DERIVED (local C17)
>
> On FRESH: take the work list ASCENDING, select **the FIRST 14 NON-DEFERRED ids** (expected 266–279 — an expectation, never an operand: the LIST is authoritative), and **write + `git commit` them into the dev log as a `#### Tranche manifest` — one line per id, fixed format `- tranche entry=<id>` — BEFORE the first insert.** On RESUME: **the recovered manifest IS the tranche** — classify exactly the manifest ids still unclassified (work list ∩ manifest), and NEVER "the first 14 of the current list": a mid-tranche death shrinks the list, and re-deriving the bound from it would overshoot into the next step's ids. Fewer than 14 on the FRESH list → manifest all that remain and say so.
>
> ### The classification contract
>
> For each: read `id, source_heading, raw_content, tags, entry_date` **from the DB row in front of you**; apply ADR-002; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positional args by NAME in this order; a sixth positional binds to CHECK-constrained `status` and fails.** `status`/`target_layer`/`target_artifact`/`route` are keywords. **`conn.commit()` after EACH insert** — a mid-list death costs the remainder, not the tranche.
>
> 1. `category` ∈ `structural`/`instrumentation`/`governance_rule`/`language`/`narrative` (never hand-assign `duplicate`).
> 2. ⚠️⚠️ **The tag is EVIDENCE, not a synonym — and FIVE of this batch's twelve tags have NO corpus precedent whatsoever** (`instruction-design`, `bellows-mechanics`, `probe-integrity`, `measurement`, `mechanization` — 7 proposals), **while `process-discipline` (5 proposals) has exactly two priors and BOTH were classified `instrumentation`, not `governance_rule`.** These classifications SET the precedent; argue each from the entry's substance, and never anchor a category to a predicted id (Rule 58(3)).
> 3. `suggested_action` — concrete; name any code coupling as a QUESTION for Gate 1 where Rule 46 might fire.
> 4. `reasoning` — **quoted evidence from THAT entry's `raw_content`, bounded at BOTH ends** (Step 5 row 9 measures): longest contiguous quotation **≥ 40 chars** (floor) and **< 80%** of the field's own length (ceiling — a paste is not an argument). ⚠️ **Calibration re-measured at authoring against plan 311's own 51 proposals by row 9's exact algorithm — NOT inherited from 296: match 59–266, ratio 0.102–0.439, zero breaches of either bound.** The floor margin is 59 against 40 — healthier than the 48 that 311 called thin. Cannot cite specific `raw_content` → STOP and report; never write generic justification.
> 5. `confidence` ∈ `low`/`medium`/`high`. `ambiguous` is a valid `status` for a genuine no-fit — say so by id.
> 6. ⚠️ **CATEGORY DIVERGENCE HAS A PRODUCER RULE (C14 — a rule living only in the verifier cannot be complied with). Row 3's arms, derived from measured precedent:**
>    - `verification` (10), `drafting-cycle` (10), `planner-discipline` (2), `drafting` (1) → `governance_rule`
>    - `bellows-integration` (3), `instrumentation` (3), **`process-discipline` (5 — arm WIDENED on its inverted precedent)** → ∈ {`governance_rule`, `instrumentation`}
>    - the five zero-precedent tags (7 proposals) → ∈ {`governance_rule`, `instrumentation`, `structural`, `narrative`}
>
>    **Assigning a category OUTSIDE the arm for the entry's tag is PERMITTED on the entry's substance — and REQUIRES the diverged disposition form:** `field: category | scouted: <the arm's set> | set: <your value> | reason: <raw_content quote justifying the category>`. **An arm-external category recorded with an `agreed` line is exactly the ❌ row 3 fires on.**
> 7. ⚠️⚠️ **FLAG (G)'s PRODUCER — every proposal's disposition line states whether the entry's remedy names a MECHANISM or a DISCIPLINE, and this is the classifier's job, not Gate 1's.** Apply flag (G)'s test to the entry's own `How to apply:` clause: does it name a concrete observable — a specific check, a named file or parser, a QA assert, a structural convention a tool can evaluate — or a discipline a human must remember? Append to the disposition line **`| remedy: mechanism | owner: <named owner or "unnamed">`** or **`| remedy: discipline`** *(observed by Step 5 row 3)*. ⚠️ **Where the entry names a mechanism, `suggested_action` states the mechanism and its owner in its own words** — Gate 1 routes from `suggested_action`, and an entry whose mechanism lives only in this plan's flag table is one Gate 1 must re-derive. **This clause exists because flag (G) was added at walk 6 with no producer anywhere in Steps 1–3** — the mandate-without-an-observer class of batch entry 302, committed against this plan's own newest flag.
> 8. **Set BOTH target fields on every non-`ambiguous` proposal** (`target_layer='governance'` expected; `target_artifact` per your OWN reading — the scout table is guidance with explicit LICENCE TO DISAGREE, Rule 58). Only `route`/`subcategory`/`duplicate_of` stay `None`.
>
> ⚠️ **The scout is NOT a mandate, and it is shallower than 311's** (heading + `How to apply:`, declared in the front matter). Derive each target independently from `raw_content`. ⚠️⚠️ **NO entry in this batch carries a `**Family:**` line — 0 of 41, measured. Every placement derivation comes from the body alone; SAY SO in the disposition line. A disposition line reporting a Family line is reporting something that does not exist.** Divergence from the scout: set what the entry supports and RECORD it — silently conforming and silently overriding are both defects.
>
> ⚠️ **Cluster-(A) entries in THIS tranche — 267 and 270** — follow the flag-(A) convention: `target_artifact` = `DRAFTING_CYCLE.md`, the route-into-the-§2-rewrite flag in `suggested_action` and the disposition line; never a non-file target value. ⚠️ **Rule 46 candidate in THIS tranche — entry 266.** ⚠️ **Shell-hostile headings in THIS tranche — entries 268, 270, 277** (apostrophes / backticks): bind as query parameters, never into a shell string. **On any HALT, commit whatever deposit files exist by EXPLICIT PATHSPEC before stopping, recording the halt point and its measured value.**
>
> **Deposit `#### Scout dispositions` in the DEV LOG (never the QA report — the lines carry `|`):** ONE line per proposal classified in this tranche, fixed formats:
> - `- proposal <id> | entry <id> | agreed | reason: <text>`
> - `- proposal <id> | entry <id> | diverged | field: <category|target_artifact> | scouted: <v> | set: <v> | reason: <text>`
>
> Values bare. **Every `reason:` is drawn from the entry's own `raw_content`** — never the tag, never this plan's scout prose. ⚠️ **The stricter form binds every proposal whose entry carries one of the five zero-precedent tags or `process-discipline`: the `reason:` must quote or name specific text justifying the CATEGORY** — these rows establish precedent for every future batch.
>
> **Also deposit the CREATED-PROPOSAL anchor for this tranche** in the Receipt, fixed format, no `|`: **`- created proposal=<id> entry=<id>`** — expected 14 lines. ⚠️⚠️ **The list covers EVERY proposal of this tranche's MANIFEST, never only this dispatch's inserts: on a RESUME, RECONSTRUCT the dead dispatch's lines from the DB scoped to the manifest ids.** A partial anchor under-scopes every downstream staleability guard and makes Step 4 mislabel this plan's own rows as foreign.
>
> **What `classifications-cycle-2026-08-10-part1.md` carries:** this tranche's per-entry classification reasoning in argued form (beyond the DB `reasoning` column), the narrative explanation for every scout divergence (the machine-checkable line stays in the dev log), and any `ambiguous` rationale by id.
>
> **Self-report:** `SELECT id, entry_id, status, category, target_artifact FROM lesson_proposals WHERE entry_id > 265 ORDER BY id` — expect exactly this tranche's rows (14 on a fresh run). Re-run the `NT` query, label `NT-post-tranche-A` (expected: the 42 `accepted|codify` PLUS exactly this tranche's proposals). ⚠️⚠️ **A change to the 42 is adjudicated HERE by the SAME arms this step's own pre-flight uses — it does NOT halt unconditionally.** An unqualified HALT would contradict the pre-flight in the same step: a legitimate in-window Gate-2 codification continues there and would halt here. Apply the four conjuncts; `stale` → HALT; anything unexplained → HALT. Report `get_unclassified_entries()` — expected: the remaining 27 ids.
>
> **Receipt:** `Status:` line, the tranche's created-proposal list, per-tranche reasoning-depth self-measurement **by Step 5 row 9's stated algorithm — canon() + `SequenceMatcher` longest match; the method IS part of the measurement** — longest-match length + ratio per proposal, id order, `#### Files Created or Modified` (split lists), `#### Prompt Feedback`. Commit by explicit pathspec (pathspec on the COMMIT), asserting the toplevel post-commit.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-10-part1.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-08-10.md`

---
---

## STEP 2 — Classification tranche B (the NEXT 14)

---

> **Preconditions:** Plan A AND Step 1 Receipts carry PROCEED-values (allowlist; the Step-1 G6-deferral state acceptable exactly as Step 1's precondition defines it).
>
> **STEP 0 — dispatch-state determination for THIS step first**, exactly Step 1's three-probe form aimed at `knowledge/development/dev-log-cycle-step-3-2026-08-10.md` (+ the `bellows-preserved/*` branch list; exit codes captured; positive control paired): a hit → RESUME, recover THIS step's `#### Tranche manifest` — **with Step 1's idempotent-re-dispatch AND deposit-completion branches, verbatim in effect**; absent from all three → FRESH.
>
> **Pre-flight (printed tokens — C8):**
> 1. `UNCLASSIFIED=<n>` — expected **27** on FRESH; any id outside 266–306 not named in Plan A's deferred list → HALT; ⚠️ **FRESH + count ≠ 27 → CONTRADICTION → HALT (C7)** — list the `entry_id > 265` proposals (report-only) and do not classify (same surplus carve-out as Step 1).
> 2. **Prior-tranche staleability:** read tranche A's recorded created-proposal ids from Step 1's Receipt (**absent/unparseable → HALT; never reconstruct by predicate — C9**) and check `SELECT 'STALE_IN_A=' || COUNT(*) FROM lesson_proposals WHERE id IN (<tranche A's recorded ids>) AND status='stale';` — non-zero → HALT; on a RESUME additionally `STALE_IN_MINE` derived from THIS step's committed manifest.
> 3. **The Gate-2 queue check, exactly as Step 1 states it — ID-FOR-ID against Plan A Receipt item 5's recorded list, never a count.** Any recorded id absent from the live set → the causal adjudication, whatever the count reads.
> 4. Whole-corpus `STALE_COUNT` == Plan A's recorded baseline (3).
> 5. No other in-progress lessons/cycle plan (main-tree glob).
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-10-part2.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-08-10.md`
>
> **Tranche — manifest-pinned (C17):** FRESH → the first 14 **NON-DEFERRED** ids of the CURRENT work list ascending. ⚠️⚠️ **The qualifier is load-bearing here specifically: G6-deferred ids are entries whose proposals were all staled, so their ids are BELOW 266 and sort FIRST in an ascending list** — an unqualified "first 14" builds this tranche's manifest out of deferred ids. **Select the first 14 non-deferred ids (expected 280–293 — an expectation, never an operand: the LIST is authoritative), and write + `git commit` them into the dev log as a `#### Tranche manifest`, one line per id, BEFORE the first insert (C17).** RESUME → the recovered manifest ∩ unclassified, never re-derived from the shrunken list.
>
> **The classification CONTRACT is Step 1's, and its violable core is RESTATED INLINE (C14) — read Step 1's full rule text as well:**
> 1. `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — five required positionals in exactly that order; a sixth positional binds to CHECK-constrained `status` and fails.
> 2. `status`/`target_layer`/`target_artifact`/`route` are keywords; **`conn.commit()` after EACH insert.**
> 3. **BOTH target fields set on every non-`ambiguous` proposal.**
> 4. `reasoning` quotes THAT entry's own `raw_content` with longest quotation **≥ 40 chars AND < 80%** of the field's own length (calibration: 311's 51 measured 59–266 / 0.102–0.439).
> 5. **Every proposal of the five zero-precedent tags or `process-discipline` carries the category-justifying `reason:` burden.**
> 6. **Category-arm divergence uses the DIVERGED disposition form with `scouted: <the arm's set>`** (arms exactly as Step 1 lists them) — an arm-external category under an `agreed` line is a row-3 ❌.
> 7. Disposition lines in the two fixed `|`-bearing formats, one per proposal, in the DEV LOG only.
> 8. Anchor lines `- created proposal=<id> entry=<id>` (expected 14, no `|`), covering the full manifest.
> 9. Self-report `NT-post-tranche-B` (the 42 intact + tranches A and B) + remaining work list (expected 13).
> 10. Per-tranche reasoning-depth self-measurement in the Receipt by Step 5 row 9's stated algorithm, all inserts in id order.
> 11. `part2` carries `part1`'s content spec.
> 12. Explicit-pathspec commits — **the pathspec on the COMMIT**, toplevel asserted post-commit.
> 13. ⚠️⚠️ **FLAG (G)'s PRODUCER binds here too (C14 — a rule stated in one producer and not its siblings is a defect in the direction that is missing):** every disposition line carries **`| remedy: mechanism | owner: <named owner or "unnamed">`** or **`| remedy: discipline`** *(observed by Step 5 row 3)*, applying flag (G)'s test to the entry's own `How to apply:` clause, and where the remedy is a mechanism `suggested_action` states that mechanism and its owner in its own words. ⚠️ **This matters MORE here than in tranche A: not one of flag (G)'s nine core entries is in tranche A — four are in tranche B and five in tranche C.** A producer that binds Step 1 alone produces the signal for none of the entries the flag exists for.
>
> ⚠️ **Cluster-(A) entry in THIS tranche — 284**, and it is the batch's strongest `reference` candidate (flag D): follow the flag-(A) convention (`target_artifact` = `DRAFTING_CYCLE.md`; route flag in `suggested_action` + disposition line), **and state in its disposition line whether the entry's substance is already fully carried by v2.0 — that reading is Gate 1's to make, but the classifier's read of it is evidence.** ⚠️ **Rule 46 candidate in THIS tranche — entry 281.** ⚠️ **Shell-hostile headings in THIS tranche — entries 280, 281, 284, 286, 290, 291** (apostrophes / backticks): parameters, never shell strings. ⚠️ **No entry here carries a `**Family:**` line** (none in the batch does). **On any HALT, commit whatever deposit files exist by explicit pathspec before stopping.**
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-10-part2.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-08-10.md`

---
---

## STEP 3 — Classification tranche C (the REMAINDER)

---

> **Preconditions:** Plan A and Steps 1–2 Receipts all PROCEED-values (allowlist; the Step-1 G6-deferral state acceptable exactly as Step 1's precondition defines it).
>
> **STEP 0 — dispatch-state determination for THIS step first**, Step 1's three-probe form aimed at `knowledge/development/dev-log-cycle-step-4-2026-08-10.md` (+ `bellows-preserved/*`; exit codes captured) — **with the idempotent-re-dispatch AND deposit-completion branches, uniform with Steps 1–2.**
>
> **Pre-flight (printed tokens — C8):**
> 1. `UNCLASSIFIED=<n>` — expected **13** on FRESH; any id outside 266–306 not named in Plan A's deferred list → HALT; ⚠️ **FRESH + count ≠ 13 → CONTRADICTION → HALT (C7)** (same surplus carve-out).
> 2. **Prior-tranche staleability:** tranches A+B's recorded created-proposal ids from Steps 1–2's Receipts (**either list missing/unparseable → HALT; no predicate fallback — C9**): `STALE_IN_AB` printed token, non-zero → HALT; on a RESUME additionally `STALE_IN_MINE` from THIS step's committed manifest.
> 3. **The Gate-2 queue check — ID-FOR-ID against Plan A Receipt item 5's recorded list, never a count, with Step 1's arms and defaults in full** (item 5 missing/unparseable → HALT `unverifiable`, no predicate fallback; any of the 42 in `stale` → HALT; any other unattributable departure → HALT; only the four-conjunct in-window Gate-2 codification continues). Print the token and the symmetric difference. ⚠️ **Stated in full here rather than by reference: a walk-8 sweep left this step pointing at "the causal adjudication" with no arms inside its own text (C14).**
> 4. Whole-corpus `STALE_COUNT` == 3.
> 5. No other in-progress lessons/cycle plan.
>
> **Tranche — the REMAINDER, manifest-pinned like Steps 1–2:** on FRESH, the manifest = every **NON-DEFERRED** id the work list returns (expected 294–306) — ⚠️⚠️ **the non-deferred qualifier is load-bearing: without it G6 deferral commits deferred ids into a manifest this step then refuses to classify, leaving `13 + |deferred|` manifest lines against an expectation of 13 anchor lines and a resume rule that returns the deferred ids forever** —, written + committed as `#### Tranche manifest` BEFORE the first insert; on RESUME, manifest ∩ unclassified. The remainder property still holds — every remaining id belongs here by construction — it just does not substitute for the committed trace, which is what makes a transient mid-step death resume-determinable.
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-10-part3.md`
> - `knowledge/development/dev-log-cycle-step-4-2026-08-10.md`
>
> **The classification CONTRACT is Step 1's, restated inline exactly as Step 2 restates it (C14) — **all THIRTEEN numbered items bind here** (the count is stated because a stale one silently narrows what binds), with these deltas:**
> - Anchor lines expected **13**.
> - Self-report `NT-post-tranche-C`: the 42 `accepted|codify` intact **plus all 41 of this cycle's proposals.** ⚠️ **Not "and nothing else":** a foreign in-window proposal is a reconcile-note elsewhere in this plan, and an absolute clause here would fail it. Report any extra by id and continue; adjudicate a change to the 42 by the pre-flight's arms, not by an unconditional halt.
> - ⚠️⚠️ **FLAG (G)'s PRODUCER binds here too (C14), and this tranche carries FIVE of its nine core entries — 297, 301, 302, 305, 306, every one of them already holding an open FORWARD row.** Every disposition line carries `| remedy: mechanism | owner: <named owner or "unnamed">` or `| remedy: discipline` *(observed by Step 5 row 3)*; where the remedy is a mechanism, `suggested_action` states it and its owner. **These five are the batch's whole recurrence argument: noticed, recorded, never built.**
> - **`part3` carries `part1`'s content spec PLUS the whole-batch cluster-synthesis UPDATE for Gate 1** — actual tag counts against the expected 10/10/5/3/3/3/2/1/1/1/1/1, the divergence tally across all three tranches (read Steps 1–2's dev logs), all `ambiguous` ids, and any change to the flag-(A)–(F) picture that classification surfaced. **Under the split no other step owns that synthesis.**
>
> ⚠️⚠️ **THIS TRANCHE CARRIES THE WHOLE FORWARD-ROW CLUSTER.** Entries 300, 301, 302, 304, 305 and 306 map one-to-one onto FORWARD rows 53, 50, 52, 51, 45 and 54 — **all six land here, and they are the six items this cycle exists to unblock.** Each disposition line names its FORWARD row explicitly so Gate 1 can reconcile rather than route fresh (flag B). ⚠️ **Cluster-(A) entries in THIS tranche — 294 and 300** (300 is the cluster centerpiece): flag-(A) convention. ⚠️ **Rule 46 candidates in THIS tranche — 297, 301, 305.** ⚠️ **Shell-hostile headings — entries 297 and 300.** **On any HALT, commit whatever deposit files exist by explicit pathspec before stopping.**
>
> Classify EVERY remaining NON-deferred id on the work list. After the last insert: `get_unclassified_entries()` MUST return `[]` — **or EXACTLY the ids of Plan A's `### Deferred entries (G6 candidate)` section in the approved state** — record the printed count token (`REMAINING=0`, or `REMAINING=<n>` with the ids matching the deferred list id-for-id), not silence.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-10-part3.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-4-2026-08-10.md`

---
---

## STEP 4 — DEV (generate the report)

---

> **Before starting: Plan A and Steps 1–3 Receipts ALL carry PROCEED-values** (allowlist — a stub or HALTED value stops this step, EXCEPT the Step-1 G6-deferral state; deliberate narrowing of the template's Partial-acceptable clause: every other halt upstream concerns the integrity of the corpus this report derives from). Post a short visible chat message. You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Same working-location + absolute-DB rules. **Open read-only** (`?mode=ro`).
>
> **Scope:**
> - `reports/lessons-report-2026-08-10.md`
> - `knowledge/development/dev-log-cycle-step-5-2026-08-10.md`
>
> **Pre-check — branch, do NOT halt unconditionally.** If the report exists AND this step's dev log is committed **AND that dev log opens with a PROCEED-value** → **idempotent re-dispatch: APPEND a `### Re-dispatch note`, leave the Complete receipt untouched, and STOP.** ⚠️ **The third conjunct is required and matches Steps 1–3's form:** every HALT arm in this step fires AFTER the report has been written, so "report exists + a committed HALTED dev log" is reachable, and two conjuncts alone would convert it into an append-and-stop that skips the re-check. A committed non-PROCEED dev log → re-run the checks, do not append. ⚠️⚠️ **An unconditional HALT here bricks the run:** Plan A and Steps 1–3 all carry this branch, Step 5's precondition is an allowlist whose only halt exception is the Step-1 G6 state, and a bare daemon retry of an already-complete Step 4 is a normal bellows state — so a Step-5 halt record has no path forward except a stop plus a re-deposit under a fresh id. **Never overwrite a Complete receipt with a halt record.** (`generate_lessons_report` overwrites unconditionally, which is why the report is not regenerated on this branch.) Report exists but deposit absent → deposit-completion resume: **copy the existing report aside FIRST** to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-339-<UTC-stamp>.md` (**339 = the plan id verified at deposit — if it differs at claim, use the ACTUAL id and record it, exactly as Plan A's Step 1a's backup mandates**) (main tree, outside Scope — a worktree copy trips scope_check, an uncommitted one dies with teardown), recorded in `##### Untracked artifacts` on its own labelled line, exact form: `copy-aside (pre-regen): <absolute path>` (Step 5 row 0 cross-checks that token). Verified at authoring: no 2026-08-10 report exists.
>
> Run `generate_lessons_report(conn, "2026-08-10")` — whole-corpus; the date is only the filename/title. **`output_dir` defaults to `"reports"` RELATIVE TO CWD** — `pwd` before the call; state the returned absolute path; confirm the filename matches Scope. ⚠️ The known `encoding=` gap (`src/lessons_forge.py:593`, no explicit encoding) is a FORWARD item already filed by 296 — note, don't re-file.
>
> **Two DERIVED expectations** (read Plan A's `NT` label — `NT-original` when present, NEVER `NT-now` — and Steps 1–3's created-proposal lists; any operand missing/unparseable → STOP and report, no literal fallback):
>
> 1. ⚠️⚠️ **Surfaced proposals = 41, and the derivation is NOT 311's.** 311 derived it as `<pre-ingest NT_COUNT> + <classified>`. **That formula is WRONG here and would predict 83 on a correct run.** `generate_lessons_report` selects `WHERE p.status IN ('proposed','ambiguous')` — verified by source read at authoring (`src/lessons_forge.py:536-543`) — and **none of the 42 `accepted` rows or the 3 `stale` rows are in that predicate.** Planner measured the baseline directly: `SURFACEABLE_BASE = 0`. **The derivation is therefore `SURFACEABLE_BASE + <total classified>` = 0 + 41 = 41**, and the operand to re-read at run time is `SELECT COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','ambiguous')` at Plan A's baseline, not `NT_COUNT`.
>    - A surfaced proposal OUTSIDE the recorded 41 is a RECONCILE-NOTE (id + heading recorded, CONTINUE — the gate windows are hours-to-days and a foreign in-window proposal is legitimate); one you cannot attribute at all → HALT.
>    - ⚠️⚠️ **Surfaced BELOW the derived expectation → the STALING SIGNATURE** (a staled proposal silently vanishes from the report's selection — nothing else makes ours disappear): query the recorded 41 proposal ids for `status='stale'` with a printed count token; **any → HALT naming the pristine `.backup`.** Zero stale with a below-expectation count → ⚠️⚠️ **FIRST check for an in-window Gate-1 disposition of our own 41 before halting.** Gate 1 writes `status='accepted', route='codify', status_updated_by='ceo'`, and `accepted` is not in the report's `('proposed','ambiguous')` predicate — so a legitimate Gate-1 pass drops the surfaced count below 41 with zero stale. **Any of the recorded 41 now `accepted|codify` with a ceo actor and an in-window timestamp → record + CONTINUE, naming the ids and the adjusted expectation.** Only a below-expectation count this does NOT explain is the HALT. **This discharges the carve-out debt Step 1 names as owed here.**
>    - ⚠️ **Also re-run the Gate-2 id-for-id check here** (against the recorded list, not a count — see Step 1). A surfaced count of 41 is fully consistent with the Gate-2 queue having been destroyed, because those rows never surface either way. **The report cannot see the damage Plan A's G1 and pre-ingest guard existed to prevent — and this plan has no equivalent, because it never touches those rows.** That is why the Gate-2 id-for-id check runs at every step here rather than being left to the report.
> 2. **Zero `- **Route:**` lines expected** (`src/lessons_forge.py:584` emits under the `if route is not None` guard at `:583`; every insert left route NULL). ⚠️⚠️ Count with **`grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"`** — BOTH `-F` AND `--` (the pattern starts with `-`; without `--` it parses as an option: empty stdout, exit 2); NEVER pipe to `head` (masks the exit code). Exit 0 = matches (attribute, then decide); exit 1 = zero (the expected result); exit ≥2 = the check did not run → HALT, do not record zero. A route line attributable to one of the recorded 41 with `status` still `proposed` → Gate 1 walked in-window → record + CONTINUE. A route on any `entry_id ≤ 265` proposal, or unattributable → HALT.
>    - ⚠️ The report prints NEITHER proposal id nor entry_id — attribute by `source_heading` via the DB join, **in SQL/Python with bound parameters, never shell interpolation** (eleven of the 41 headings are shell-hostile; some contain backticks that EXECUTE in a double-quoted shell string).
> - Any `Recently-implemented overlap:` line → HALT (`grep -Fc --` + exit code; the detector was retired by plan 207; reappearance is a regression).
>
> **Deposit:** report + dev log with `Status:` line (Step 5 reads it), `#### Files Created or Modified`, report length, proposals surfaced, route-line count + exit codes, overlap-line count (expected zero, with exit code), and the `Q2_INTACT` token. Canonical Python file-write. Explicit-pathspec commit, toplevel asserted.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-10.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-5-2026-08-10.md`

---
---

## STEP 5 — QA

---

> ⚠️⚠️ **STEP 0 — DISPATCH-STATE DETERMINATION FIRST, and this step is the one that lacked it.** Probe three places for THIS step's own report `knowledge/qa/cycle-qa-2026-08-10.md`: (i) `git -C <your worktree> show HEAD:<path>`; (ii) the working tree; (iii) `git log --all -- <path>` **and** `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'` — probe (iii)'s exit code carries no signal, so pair it with a positive control against a known-committed path. **A hit on ANY → idempotent re-dispatch: APPEND a `### Re-dispatch note`, leave the committed report untouched, and STOP.** ⚠️ **A bare daemon retry of an already-complete QA step is a normal bellows state, and without this branch the retry re-emits the Forward Register block and the daemon appends a SECOND row for the same item** — the dup-append defect this plan records as live register debt. Absent from all three → FRESH; state the determination as the first line of your report's narrative.
>
> **Before starting: Plan A and Steps 1–4 Receipt statuses ALL PROCEED-values** (allowlist, named values — an instruction that merely says "confirm the status lines" is satisfied by observing a halted one; this one is not; the Step-1 G6-deferral state is the ONE exception). Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Same working-location + absolute-DB rules. **Verification + reporting only — a failing test is reported, never fixed. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly.**
>
> **MANDATORY — Rule 20 self-check (canonical block, exact template, four placeholders):** run from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path — governance root, not your worktree):
> - `plan_slug`: `cycle-session-24-33-captures-2026-08-10`
> - `qa_report_path`: `<your-own-tree-abs>/knowledge/qa/cycle-qa-2026-08-10.md`
> - `evidence_dir`: `<your-own-tree-abs>/knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/` (derive from `pwd` — the plan-225 trap)
> - `required_evidence_files`: `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]` — quoted Python string literals.
>
> Deposit all four evidence files BEFORE the block (it `sys.exit(1)`s on missing/empty) — **and write the QA REPORT (with its verification table) BEFORE the block too: it `sys.exit(1)`s with a not-found CRITICAL if `qa_report_path` does not exist. The order is: write report → run block → APPEND the stdout to the report.** Include the block's literal stdout in the QA report; the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must appear verbatim in the deposited report (⚠️ stated WITHOUT a `##` prefix — **re-verify against the delivering code before relying on it; do not inherit this claim**). End with a self-grep confirming the banner reached the deposited report.
>
> ⚠️ **What the block verifies: evidence-file presence + hedging keywords ONLY — it cannot see verdicts; expect PASSED even on an honest halt; never flip/soften/drop a row to keep it green; a genuine `❌` fails at the rule_22 gate, and that is correct.** If any row is `❌`, add the standard one-line note under the stdout naming EVERY failing row.
>
> **⚠️ Rule 19 — VERBATIM:** *"If you cannot complete a check, mark it ❌ with a reason. Do NOT mark it ✅ and explain why you couldn't verify. Any ✅ row containing hedging keywords will auto-fail during the self-check in Rule 20."*
>
> ⚠️⚠️ Hedging keywords are fatal even as measured values — write row 1's value as `<N> passed` and NOTHING else. ⚠️⚠️ No command containing `|` in a table cell (fenced block above the table; the row cites the result; escaping `\|` silently breaks the command). ⚠️⚠️ The status column holds EXACTLY one glyph, `✅` or `❌` — no third value, no annotated glyph; a reconcile outcome is a `✅` with a note in the measured-value column. ⚠️ Close the `## Verification Table` section with `## Evidence and Narrative` immediately after the table — the gate's section flag never clears on `###`.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-08-10.md`
> - `knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/invariants.txt`
> - `knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/schema.txt`
>
> Table under exactly `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`. **A failing row does not license skipping the rest — run all eleven (0–10), then halt if owed; a HALT still leaves a committed record.**
>
> ⚠️⚠️ **THE IN-WINDOW RECONCILIATION RULE (rows 3, 5, 8, 9 inherit; FIVE gate windows exist):** every whole-corpus row adjudicates in two parts.
> - **(a) HARD — the delta this plan owns, BY ID:** the **41 proposal ids and 41 entry ids from the recorded anchors** — Plan A's ingested-entry list + the UNION of Steps 1–3's created-proposal lists. Validate each list before querying: **41 integer values, none blank/NULL** (`NOT IN` is NULL-poisoned and fails silently toward "nothing found" — print `FOREIGN=` tokens); missing/truncated/unparseable list → every dependent row `❌ (unverifiable)`, NO predicate fallback (`entry_id > 265` means "after authoring", not "ours").
> - **(b) RECONCILE — everything outside the id set:** report ids, note in the measured-value column, still `✅`.
> - **Gate-1 in-window on our own 41 → ✅ + note, in BOTH shapes: `route` set with status still `proposed`, AND `status='accepted'` with `route='codify'` and a ceo actor — Gate 1's actual write signature, measured.** ⚠️ `accepted` is neither `stale` nor a member of `_TERMINAL_STATUSES`, so without this arm a legitimate Gate-1 pass falls through every branch and returns ❌. A move to `stale` → ❌ always. A terminal flip is adjudicated CAUSALLY:** legitimate Gate-2 activity on THIS cycle's proposals requires Gate 1 to have ROUTED them first — so terminal + `route` set (with `status_updated_by='ceo'` where populated) → ✅ + note naming ids; terminal + `route IS NULL` on one of the 41 → ❌, with ONE narrow exception: `status='rejected'` + `status_updated_by='ceo'` + route NULL is a legitimate in-window Gate-1 REJECTION → ✅ + note naming ids; any OTHER terminal + route NULL → ❌.
>
> Row 7 is the declared C5 exception and fails closed on ANY doctrine change.
>
> 0. **Deliverable verification (Rule 17) — scoped to `##### Committed deposits` sub-lists of ALL FIVE prior Receipts** (the untracked backups/DB live in `##### Untracked artifacts`: cross-check against each Receipt's labelled paths — Plan A item 7, Step 4's `copy-aside (pre-regen):` token via `grep -Fc --` + exit code — but never apply commit tests or fail the row on them). Per committed deposit, BOTH: `git log --oneline -1 -- <path>` (empty = FAILURE here — quote the printed commit line) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"` (empty + exit 0 = clean; non-zero exit = `❌`, never clean). Any ❌ → Critical, blocks Done.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail to `pytest_targeted.txt`. The whole of `src/` IS the complete run under `targeted` (one test file — measured); do not add a second run. Baseline from `--collect-only` reconciled against the most recent prior QA (Planner measured 55). Value cell: `<N> passed` only.
> 2. `get_unclassified_entries(conn)` == `[]` — **or EXACTLY the ids of Plan A's `### Deferred entries (G6 candidate)` section.** Quote the printed result WITH a count token. ⚠️ Non-empty has ONE diagnosis on a completed run: **the staling signature** — report ids, `❌`, cross-reference rows 3/4, name the `.backup`.
> 3. **Invariants over exactly the 41 recorded proposal ids** (expect 41 rows): zero dangling `entry_id`; `route IS NULL` directional per the in-window rule; `status IN ('proposed','ambiguous')` directional (stale→❌ always; terminal→the causal test). Targets for each non-`ambiguous` proposal: `target_layer='governance'`; **`target_artifact` ∈ {`PLANNER_TEMPLATE.md`, `DRAFTING_CYCLE.md`, `RULE_20_SELF_CHECK_BLOCK.md`} as a MEMBERSHIP bound** (bare TEXT, no CHECK), **adjudicated on RECORDED DIVERGENCE, not membership alone:** outside the set + a Scout-dispositions line naming that exact proposal and target + the target RESOLVES (root file via `git -C <root> cat-file -e HEAD:<path>`; submodule-resident via `-C` against that submodule) → ✅; outside with no recorded divergence → ❌. ⚠️ **Cluster-(A) proposals set `target_artifact` to the doctrine file their substance would amend (`DRAFTING_CYCLE.md`), with the route flag in `suggested_action` and the disposition line; a non-file value is ❌ — it can never resolve through this row's existence check.**
>
>    **Category bound, three parts (per-tag, matched by BACKTICK-EXACT EQUALITY — `WHERE tags = '<backtick>tag<backtick>'` with the literal backticks INCLUDED: the stored values carry them, and equality without them returns zero rows, voiding the bound. ⚠️ `LIKE '%tag%'` is FORBIDDEN here — `drafting` is a SUBSTRING of `drafting-cycle`, and `instrumentation`/`instruction-design` share a prefix; PRINT matched row counts):**
>    - `verification` (expect 10), `drafting-cycle` (10), `planner-discipline` (2), `drafting` (1) → `governance_rule`
>    - `bellows-integration` (3), `instrumentation` (3), `process-discipline` (5) → ∈ {`governance_rule`, `instrumentation`}
>    - `instruction-design` (3), `bellows-mechanics` (1), `probe-integrity` (1), `measurement` (1), `mechanization` (1) → ∈ {`governance_rule`, `instrumentation`, `structural`, `narrative`}
>    - `language` (zero corpus uses) and `duplicate` are ❌ regardless — no divergence licenses them.
>
>    ⚠️ The bound is failable BECAUSE it is narrower than the schema CHECK (a bound must be able to fail — the CHECK permits 6 values; these assert 1, 2 and 4). ⚠️⚠️ **Every category arm is adjudicated on RECORDED DIVERGENCE, exactly like the target bound: a category outside its arm's set WITH a diverged disposition line whose `reason:` quotes `raw_content` justifying the CATEGORY → ✅ + note naming the id; without the recorded line → ❌.** **The value-level half a membership bound cannot supply: for every proposal of the five zero-precedent tags or `process-discipline` (12 proposals — the largest zero-precedent set any batch has carried), the disposition `reason:` quotes specific `raw_content` justifying the CATEGORY; empty/generic/tag-only → ❌ by id.** Partition BY THE TAG READ FROM THE ROW, never predicted ids; report measured tag counts (a departure from 10/10/5/3/3/3/2/1/1/1/1/1 is itself the finding). `ambiguous` proposals exempt from target+category bounds; report by id. Scoped count ≠ 41 → FAIL.
>
>    ⚠️ **Declared blind spot: this row enforces membership + recorded divergence; it cannot see an in-set SWAP — a foreign overwrite between two permitted artifacts passes by design.** That mapping is Gate 1's read, informed by the dispositions and row 9.
>
>    **FIRST count the disposition lines across the THREE dev logs: exactly one per created proposal (41 total). ⚠️ Count LINE-ANCHORED, in Python — `sum(1 for l in lines if l.startswith('- proposal '))` per dev log — never a substring-anywhere grep: prose QUOTING the format inflates a substring count, and an over-count can MASK a missing line. Report the three per-tranche numbers. FEWER than the created count → ❌ naming the ids with no line; MORE → ❌ too.**

>    ⚠️⚠️ **FLAG (G)'s OBSERVER — the third time in this cycle a mandate was written without one, and the second time on a fold that was itself repairing an instance of it.** Steps 1–3 require every disposition line to carry `| remedy: mechanism | owner: <…>` or `| remedy: discipline`. **Check it: exactly one of the two values on every one of the 41 lines, parsed line-anchored in Python, per-tranche counts reported.** Missing on any line → ❌ naming the ids. **A `mechanism` value with `owner: unnamed` is legitimate and not a failure** — an entry can name a mechanism without naming who builds it, and forcing an owner would manufacture one. **`mechanism` + a named owner whose `suggested_action` does not state that mechanism → ❌** — that is the flag routed nowhere, which is the outcome flag (G) exists to prevent. ⚠️ **This bound can fail and the failing input is stated rather than argued (C12): a line carrying both values, a line carrying neither, or a `mechanism` line whose `suggested_action` is silent about the mechanism.**
> 4. **The plan-204 fix held.** Baseline from Plan A's Receipt (missing → `❌ (unverifiable)`). `stale` not grown (before=3, after printed); no terminal-status departures; **entry 265's `content_hash` unchanged** (`c30fdaff…`); `updated_count` + `terminal_proposals_flagged` from `#### First-dispatch ingest dict` when a resume is in evidence, else item 1. ⚠️⚠️ **A COUNT IS NOT A VALUE GUARD:** state (i) `stale` before, (ii) after, (iii) **the FULL zero-emitting status distribution before and after with this cycle's own delta subtracted** — expectation exact and failable: `implemented` 171, `superseded` 28, `rejected` 15, **`accepted` 42**, `reference` 14, `stale` 3 all UNCHANGED (confirm against Plan A's Receipt item 3, not these literals); `proposed` ABSENT before, present after
>
>    ⚠️⚠️ **CONFLICT RESOLVED JOINTLY (C20) — this row and row 10 disagreed, and the disagreement was between two folds made by different lenses in the same walk.** The Q2 carve-out permits a legitimate in-window Gate-2 codification, which moves rows from `accepted` to `implemented` — and this row's "`accepted` 42 UNCHANGED … any OTHER bucket moving → ❌" would fail exactly that permitted outcome (C5). **Single resolution, not a patch to either side: `accepted` and `implemented` are adjudicated ONLY by row 10's causal test, and this row reads row 10's verdict rather than asserting its own expectation for those two buckets.** Concretely: `accepted + implemented` is invariant at 213 across the pair; a shift *within* that sum with row 10 returning ✅ is ✅ here too, with the ids named; a change to the SUM, or any movement row 10 did not adjudicate, is ❌. The other four buckets keep their exact expectations. — ⚠️ **with the `ambiguous` carve-out: the classified count SPLITS across `proposed` and `ambiguous`, so the failable expectation is `proposed + ambiguous + <in-window Gate-1 dispositions of our own 41, accepted or rejected> == 41`, and the `accepted + implemented` invariant rises by the number of in-window acceptances rather than holding at 213, each bucket printed, ambiguous ids named and cross-checked against the disposition lines.** ⚠️⚠️ **C20's resolution reached `accepted`/`implemented` and not `rejected`, and the gap was live:** the in-window rule above admits a legitimate ceo Gate-1 rejection of one of our 41 as ✅, which this row's earlier `proposed + ambiguous == 41` form then failed as ❌. **Row 3 owns that adjudication; this row reads its verdict and subtracts the ids it named.** Any OTHER bucket moving → ❌. State the count of proposals examined. Raw to `hash-trap.txt`.
> 5. **Report exists; in-window rule applies.** HARD: all 41 recorded proposals surfaced (attribute headings→ids via the DB join, bound parameters; the report prints neither id). Use the report's own `**Total proposals:** N` line. RECONCILE: foreign surfaced proposals listed by id, ✅+note. **State the heading→id mapping IN the evidence file: a bare "41 surfaced" cannot distinguish the right 41 from a wrong 41.** ⚠️ **The surfaced expectation derives from `SURFACEABLE_BASE` (Planner measured 0), NOT from `NT_COUNT` — see Step 4's expectation 1.** Route lines: directional, `grep -Fc --` + exit code. Zero overlap lines; `detect_recently_implemented_overlaps` still absent from `src/`.
> 6. **No schema drift** — semantic comparison (PRAGMA table_info + constraint set) vs `src/db.py` DDL; cosmetic RENAME artifacts are NOT drift. Raw `.schema` both tables → `schema.txt`.
> 7. **Doctrine unchanged — TWO NAMED SUB-CHECKS, both fail-closed, neither adjudicated by you.**
>    - **7a (this-window guard):**
>      ```
>      git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md PLANNER_TEMPLATE.md RULE_20_SELF_CHECK_BLOCK.md; echo "PORCELAIN-EXIT=$?"
>      ```
>      BOTH pass conditions required: empty output AND exit 0 (`-C` is REQUIRED — from your worktree these files do not exist and a bare invocation passes silently/vacuously). Non-zero exit → `❌ (check did not run)`, distinct from `❌ (doctrine changed)`. **Non-empty porcelain → ❌, full stop — attribution is the CEO's at the verdict gate, never yours:** capture `git log --oneline ad3c2d7..HEAD -- <files>` + `git diff` into `invariants.txt` before halting.
>    - **7b (drift since authoring):** `shasum -a 256` the three files vs **Plan A Receipt item 10**; item 10 absent/short → `❌ (unverifiable)`. Print all three live + all three recorded + three pairwise verdicts. Working-tree content pins, never `rev-parse HEAD:<path>` (blind to uncommitted edits). `plan_lint.py`/`gates.py` deliberately unchecked (no write path from this cycle).
> 8. **Post-cycle DB counts, in-window rule.** HARD by recorded id lists: entries `IN (<the 41>)` = 41; proposals `IN (<the 41>)` = 41 (validated lists; no `> 265` predicates — one foreign in-window row makes 42 and a false ❌). RECONCILE totals: derivation `265 + 41 = 306` entries, `273 + 41 = 314` proposals — Planner measurements to verify and explain, not force (Checklist #29). Above-derivation with owned delta correct → foreign ids named, reconcile-note, no ❌. Status+category actuals. Raw to `invariants.txt`.
> 9. **Classification depth — THE scale instrument, per-proposal over all 41 recorded ids.** Extraction-free: canon() (curly→straight, strip `*_` and backticks, collapse whitespace, lowercase), `difflib.SequenceMatcher(None, a, b, autojunk=False)` longest match; **PASS per proposal iff match ≥ 40 chars AND match < 80% of `canon(reasoning)`'s length.** Report all 41 (length, ratio) in id order — a monotone decline IS the finding independent of the floor; **also report the three per-tranche distributions side by side** — an inter-tranche cliff is the shape-(b) signal. ⚠️ **Calibration MEASURED AT AUTHORING BY THIS ROW'S OWN ALGORITHM AGAINST PLAN 311's OWN 51 (proposals 223–273) — the newest same-class set, not 296's sixteen: match 59–266, ratio 0.102–0.439, zero breaches of either bound.** The floor margin (59 against 40) is healthier than 311 inherited; a sub-40 match remains a live outcome and is reported as the finding it is. Batch `raw_content` 766–2695 chars, so the floor cannot false-FAIL on length. Any proposal failing either bound → ❌ naming id + bound + measured pair. Batch clustering near 0.80 → a finding about the classification work even if all pass.
> 10. **⚠️⚠️ THE GATE-2 QUEUE SURVIVED — this plan's own headline risk, and no other row can see it.** `SELECT id, entry_id, status, route, target_artifact FROM lesson_proposals WHERE status='accepted' AND route='codify' ORDER BY id;` — expect **42 rows, 21 `DRAFTING_CYCLE.md` and 21 `PLANNER_TEMPLATE.md`**, matching Plan A's Receipt item 5 id-for-id. Print `Q2_INTACT=<n>` and the per-artifact split. ⚠️ **The comparison is ID-FOR-ID against the recorded list, never count-against-42** — a corpus that staled three of the 42 and gained three new `accepted|codify` rows from a foreign writer counts 42 and is not intact (C10: a count is not a value guard). **Plan A Receipt item 5 missing, truncated, or unparseable → `❌ (unverifiable)`, no predicate fallback** — the same fail-closed rule the in-window reconciliation applies to the 41. ⚠️ **An id of THIS cycle's own 41 appearing here is a legitimate in-window Gate-1 codify disposition → ✅ + note, not a foreign row.** **Fewer than 42 of the RECORDED 42, or any recorded id absent → ❌ Critical**, naming the missing ids, their current status, and the pristine `.backup` — **its absolute path is recorded in Plan A's Receipt item 7, labelled `pristine (pre-cycle)`; this plan creates no backup of its own and must not improvise one.** ⚠️ **A legitimate in-window Gate-2 codification would move these to `implemented` — that is adjudicated by the SAME conjuncts Step 1's pre-flight uses, **and not by the weaker "a Gate-2 plan is visible in `Done/`" form, which is satisfiable by history**: `implemented` AND `route` still `codify` AND `status_updated_at` later than the recorded `cycle_timestamp` AND `status_updated_by='ceo'` → ✅ + note naming ids. ⚠️⚠️ **The old form asked only whether a Gate-2 plan was visible in `Done/` — and `Done/` holds several historical ones (298, 330 among them), so it was satisfiable by HISTORY and would have waved through the corruption this Critical row exists to catch.** **Any of the 42 in `stale` → ❌ always, no adjudication.** Silence about a departure is the failure this row exists to prevent: rows 3–5 and 8 are all scoped to THIS cycle's 41 and would every one pass while these 42 were destroyed.** Raw to `invariants.txt`.
>
> **Evidence routing:** rows 0/2/3/5/7/8/9/10 → `invariants.txt`; row 4 → `hash-trap.txt`; row 6 → `schema.txt`; row 1 tail → `pytest_targeted.txt`. Before the Rule 20 block runs, self-grep each file for a content marker (`PORCELAIN-EXIT=` in invariants; the `c30fdaff` prefix in hash-trap; `CREATE TABLE` in schema; the pytest summary line in pytest_targeted) with `grep -F`, **printing what matched, not PRESENT/ABSENT** — the block only checks non-empty and a one-byte file passes it.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-08-10.md` + the four evidence files. Canonical Python file-write. `git add <paths>` then `git commit -m "…" -- <paths>` (add first — new files; on a pathspec error, `git add` and retry, never `-a`), toplevel asserted post-commit.
>
> In `### Ledger Updates`:
>
> `#### Project Status` — milestone SCOPED to this cycle's 41: cycle 2026-08-10 complete — the 41-entry session-24→33 batch ingested (Plan A) + classified across three tranches (Steps 1–3), report deposited, corpus integrity held, **the 42-row Gate-2 queue verified intact at close (row 10)**, row 9's per-tranche depth distributions recorded, Gate 1 pending for the 41.
>
> ⚠️⚠️ **`#### Forward Register` — THE WALK-5 DELETION IS REVERSED, AND THE REVERSAL IS THE FINDING.** §2.8's deletion resolution cut this block, on the stated subsumption that its one item would instead be recorded by the Planner at wrap via Rule 42's direct edit. **That subsumption is FALSE, and it was checked against the Planner's recollection of Rule 42 rather than its text.** Rule 42 (`PLANNER_TEMPLATE.md:983-996`) is a *status-update* reconciliation — open → `closed-by-plan-N` — with no new-row branch; Ledger Updates rule (5) states the daemon appends new rows and *agents emit only the Item text*; Rule 44 bounds Rule 42 to status updates in terms. **Measured: every row-adding commit in this register is `(daemon-post-merge)` — there is no Planner-direct precedent to fall back on.** The trim's "one real cost" was therefore not a contingency but the certain outcome, and §2.7's subtractive-trim rule was satisfied in form and not in substance.
>
> Write this block INSIDE `### Ledger Updates` **IN YOUR FINAL MESSAGE OUTPUT — the daemon's parser reads the TRANSCRIPT, never a deposited file, and within the transcript it reads the Ledger Updates body ONLY** (a block one heading too high is silently discarded). Described not quoted. **ONE item, and it must be the FIRST line of the block body with all prose AFTER it**, because the splitter falls back to first-line-only on a block with fewer than two bullets. ⚠️⚠️ **Nothing else in this block may begin with a dash or a digit-and-period: `sanitize_items` matches `^(?:-\s|\d+\.\s)` (`bellows.py:1419`), so a numbered item IS a bullet to it, and two or more bullet-shaped lines emit one register row PER LINE.**
>
> 1. `_TERMINAL_STATUSES` omits `accepted`, so an ingest can silently stale a routed-but-not-yet-codified proposal; this cycle carried 42 such rows and guarded them procedurally at five sites — worth deciding whether the guard belongs in the code instead.
>
> After the bullet and its terminating blank line, in PROSE: state the register's before-count read from your worktree snapshot and record that you read it there (the Planner measured 10 rows at authoring; a difference is a reconcile-note, not a halt). Do NOT re-raise the `get_unclassified_entries` ordering item — it is already open as rows 9 and 10, and this plan depends on that contract rather than duplicating it. Note for the Planner that those two rows are byte-identical duplicates, both written by plan 311's own step 6 through this same channel: live register debt, and the dup-append failure mode observed rather than theorised. ⚠️ **The observer for this mandate is the PLANNER's, at this step's verdict gate, not yours** — the daemon appends to the main tree after the step ends, so no post-append state is reachable from your worktree.
>
> `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-08-10.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-session-24-33-captures-2026-08-10/` (evidence directory as a single bullet — Rule 26; individual evidence filenames stay in Scope and `required_evidence_files` only)
>
> **Do NOT move this plan to `Done/`** — the close path is Bellows-owned on continue-verdict consumption (Rule 8); unconditional, no post-verdict branch.

---


---

## Drafting Cycle
**Tier:** T2 — T-2 fires (production-data mutation) computing T1; **NOT down-tiered** on the derivation, per §2.6. Steps 1–5 are carried from the eight-walk parent draft with their references re-pointed and three deferred findings folded.
**Walks:** 8, inherited. The parent (`knowledge/research/draft-cycle-run-339-2026-08-10.md`) ran eight walks — walks 2 and 3 folded in batch and struck; walk 8's five lenses run by fresh-context readers, sequentially, with the author folding between. **All 90 fold rows are in the committed walk register** at `governance/knowledge/research/walk-register-cycle-run-339-2026-08-10.md`.
- Weak spots:          w8 10 folded — 6 pre-existing after seven prior walks.
- Destruction:         w8 9 folded — 6 of them damage from walk 8's own lens-1 folds.
- Vulnerabilities:     w8 7 folded (the lowercase-sentinel fold and the unpinned reference length both PROVEN on Plan A's live run — each would have halted a correct ingest).
- Integration-record:  w8 14 raised, 7 folded — including the reversal of walk 5's §2.8 deletion.
- ACID:                w8 15 raised, 12 folded — the isolation map that produced the split.
- Derivation pass:     **3 findings folded at this plan's authoring** — the ones deferred at Plan A's deposit that live in these steps (QA dispatch-state; flag-(G) token unregenerable on resume; self-reports contradicting their own pre-flights).
**Panel status (T2):** not convened. ⚠️ Phrased so §4's cold-panel check cannot match it — the canonical form satisfies the check by wording while the panel has not run. The WARN is earned and clears only by convening the panel.
**Conflicts:** C1–C20 inherited from the parent; the ledger below is trimmed per-item to what this plan carries.
**Closing:** ⚠️ **Declared plainly: this is neither a dry close nor a bar-meeting judged stop.** The parent cycle did not converge, and **seven of walk 8's findings remain unfolded in it** — every one re-checked against THIS plan's surface at authoring and found either resolved by the split or record-class in text this plan does not carry, with the three that DID land folded above. **The deposit rests on that re-check plus the risk profile: this plan holds no destructive write, so its failure mode is a halt, not damage.** A walk over this artifact as re-pointed is owed and has not been run.

---

### Conflict Ledger (§2.8) — inherited, TRIMMED per item to what this plan carries

⚠️ **Subsumption stated per item, not asserted in aggregate:** each constraint below is cited in this plan's own text. Dropped: **C1** (the non-terminal baseline premise — this plan does not ingest, so nothing rests on it), **C3** (removal of inherited machinery — none removed here), **C16** (intra-line duplicate counting — no such check survives). The full twenty live in the parent and bound Plan A.

- **C2** — no step hardcodes a count it can read from a recorded capture; literals are declared Planner measurements.
- **C4** — a resume anchors on the ORIGINAL committed capture, never a live re-read.
- **C5** — a permitted outcome is never a FAIL; the one exception is the QA doctrine row, which fails closed.
- **C6** — a fold that changes a convention lands here as a CONSTRAINT, not only at its site.
- **C7** — no step's pre-flight states an unqualified fresh-run claim about a resume-variant value; each carries a CONTRADICTION→HALT arm.
- **C8** — every mandated check reports a positive token or exit code; nothing is discharged by absent output.
- **C9** — assertions about owned rows name the RECORDED id lists; `entry_id > 265` is forbidden as an ownership operand. **The anchor is a THREE-PART union across the tranches — a missing tranche list fails dependents closed, never falls back to a predicate.**
- **C10** — a check replacing a value-level assertion with a count must construct the change the survivor should catch and confirm it FAILS. **Check: the Gate-2 id-for-id comparison.**
- **C11** — no third status glyph; no `|`-bearing command in a table cell.
- **C12** — a bound must be able to fail: name the input that fails it. **Check: the category arms are narrower than the schema CHECK, which permits six values.**
- **C13** — a capture a later step or resume branch must read is deposited in a committed artifact.
- **C14** — every mandated requirement is stated IN the step that must comply with it; a rule living only in a verifier or only in a producer is a defect in whichever direction is missing.
- **C15** — a check on a delivery channel names the ARTIFACT the consumer reads; no bullet wraps; the block terminates with a blank line.
- **C17** — a bounded work-tranche is pinned by a COMMITTED MANIFEST before its first mutation; a resume consumes the manifest and never re-derives the bound from live state.
- **C18** — an unprotected non-terminal row set this plan does not own is named by id and checked at every step boundary. **Check: Plan A's Receipt item 5, read at all five steps.**
- **C19** — a derived expectation names the PREDICATE its operand is drawn from. **Check: the report's surfaced count derives from `SURFACEABLE_BASE`, measured 0, not from `NT_COUNT`.**
- **C20** — where two rows adjudicate the same DB fact, exactly one owns the verdict and the other reads it.

**Ledger status:** C2, C4–C15, C17–C20 OPEN and carried. C1, C3, C16 not carried, per the per-item subsumption above.
