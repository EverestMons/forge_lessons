# Gate 2 Blueprint — 2026-07-21 Cycle

**Date:** 2026-07-21
**Plan:** 249
**Template baseline:** PLANNER_TEMPLATE.md v4.76

## Pinned State

- **Governance-root HEAD:** `8c9e8b50b64bebd821cb7f9bcdf19bb594d6d496`
- **Template last-touching commit:** `0a6932d34167f441ff2c4dce909d79e13a7fdf1a`
- **Live version:** 4.76 (line 5: `**Version:** 4.76`; line 6: `**Last Updated:** 2026-07-21 (v4.76)`)

## Proposals Read

Nine proposals retrieved from canonical DB (IDs: 160, 162, 163, 165, 166, 167, 168, 170, 171). IDs 161, 164, 169 confirmed absent from the query — they are terminal (`status='reference'`) and out of scope.

## Lens Count Verification

- Line 333: "five **named lenses**" — reads "five". Correct unchanged under the merge. **DO NOT ALTER.**
- Line 345: "five heavy passes" — reads "five". Correct unchanged under the merge. **DO NOT ALTER.**
- Line 1826 changelog row: "four named lenses" — historical reference to v4.75. **PRESERVE. DO NOT SWEEP.**

## Dedup Greps (all against live v4.76)

| Edit | Grep terms | Count | Result |
|------|-----------|-------|--------|
| E1 | `multi-step schedule`, `between-step window`, `conflict.serial` | 0 | ABSENT |
| E2 | `lens set.*open`, `novel lens`, `provisional` | 0 | ABSENT |
| E3 | `panel pass`, `cross-lens.*parallel`, `parallelism.*within`, `parallelism.*across` | 0 | ABSENT |
| E4 | `rotate.*reviewer`, `cold.*reader`, `fresh-context`, `saturat` | 0 | ABSENT |
| E5 | `sibling.*sweep`, `anti-pattern.*instance` | 0 | ABSENT |
| E6 | `git -C`, `positive signal`, `main-tree`, `main tree` | 0 | ABSENT |
| E7 | `restore-and-redo`, `resume machinery`, `reproducible` | 0 | ABSENT |

All seven edits verified absent from the live template. No competing statements exist.

---

## Edit E1 — WIDEN the ACID Isolation clause (proposal 160)

**Type:** REPLACEMENT
**Anchor:** `Isolation: what does a concurrent actor observe mid-operation?`
**Anchor uniqueness:** grep count = 1 (line 339)
**Location:** Line 339, within lens 5's sentence structure

**Replace:**
```
Isolation: what does a concurrent actor observe mid-operation?
```

**With:**
```
Isolation: what does a concurrent actor observe mid-operation? For a multi-step schedule — steps separated by verdict gates of arbitrary wall-clock time, reading and writing shared stores — enumerate each step's reads and writes as a transaction schedule, identify the between-step windows where an unguarded concurrent actor can interleave a conflicting operation (R-W / W-R / W-W), and for each window require an explicit isolation guard (a pin, a byte-match, a locked transaction) rather than assuming quiescence; the between-step windows, not the within-step logic, are where unguarded conflicts live.
```

**Self-test:** Would this clause have prompted a reader to ask about the DEV→QA template window? Yes — it explicitly requires enumerating reads/writes as a schedule, identifying between-step windows on shared stores (the template file is a shared store between DEV and QA/wrap), and requiring an explicit guard for each window. The original clause ("what does a concurrent actor observe mid-operation?") is single-operation scoped and does not prompt this question — as demonstrated by ACID finding zero between-step windows across three runs while conflict-serializability found one on each of its three applications.

**What is NOT changed:** The lens remains lens 5. No sixth lens is introduced. The lens count stays five. The clause stays inside the existing sentence structure (`Atomicity: … Consistency: … Isolation: … Durability: …`).

---

## Edit E2 — The lens set is OPEN; a novel lens's fold is provisional (proposals 163 + 170)

**Type:** INSERTION
**Anchor:** `Fold-and-deposit **exactly once** (deposit-once discipline).`
**Anchor uniqueness:** grep count = 1 (line 341)
**Location:** Insert as a new paragraph AFTER this anchor (after the blank line on line 342, before `### Why this process exists` on line 343)

**Insert (new paragraph):**
```
The lens set is open: add a lens when a plan class raises a question the standing lenses do not ask. A novel lens's first fold is **provisional** — a novel lens reliably finds the right window and reliably ships a broken mechanism. Sequence a standing lens (weak spots or vulnerabilities) immediately behind a novel lens's fold, aimed specifically at whether the new guard is **executable**, not at whether the window is real. Never deposit straight from a novel lens's fold.
```

---

## Edit E3 — Parallelism belongs WITHIN a pass, never ACROSS lenses (proposal 166)

**Type:** INSERTION
**Anchor:** Same as E2 — insert as a new paragraph AFTER E2's inserted text (i.e., E2 and E3 form consecutive paragraphs in the same insertion block after the `deposit-once discipline` anchor)

**Insert (new paragraph, immediately after E2):**
```
Parallelism belongs within a single lens pass (e.g. multiple tracers reading different steps, feeding one fold), never across lenses. Running lenses concurrently severs the cumulative property — each lens must read the draft as the prior lens left it. A concurrent multi-lens run is a **panel pass** (a multi-finder sweep on a frozen draft, folding once as a composite), not a walk; label it as such and follow it with a real sequential walk.
```

---

## Edit E4 — Rotate the reviewer when late walks go quiet (proposal 171)

**Type:** INSERTION
**Anchor:** Same insertion block as E2/E3 — insert as a new paragraph AFTER E3's inserted text

**Insert (new paragraph, immediately after E3):**
```
When late walks stop finding things, rotate the **reviewer**, not the lens — a "dry" verdict from a saturated reviewer is weak evidence. Run the standing lenses **cold** (fresh-context readers given only the artifact plus repo read access), **sequentially** (not concurrently — sequential-cold preserves cumulation; a concurrent cold run is a panel pass, not a walk). Author verification of cold findings remains required: cold readers can misread deliberate design as defect.
```

**E3/E4 reconciliation:** E3 prohibits running lenses concurrently and defines the "panel pass" label. E4 prescribes cold reviewers and explicitly states they run **sequentially**, with the parenthetical "(not concurrently — sequential-cold preserves cumulation; a concurrent cold run is a panel pass, not a walk)" referencing E3's terminology. No licence for a parallel panel from E4's "cold" instruction.

**Combined insertion block (E2 + E3 + E4).** DEV applies this as a single insertion after the `deposit-once discipline` anchor. The full insertion text, in order:

```

The lens set is open: add a lens when a plan class raises a question the standing lenses do not ask. A novel lens's first fold is **provisional** — a novel lens reliably finds the right window and reliably ships a broken mechanism. Sequence a standing lens (weak spots or vulnerabilities) immediately behind a novel lens's fold, aimed specifically at whether the new guard is **executable**, not at whether the window is real. Never deposit straight from a novel lens's fold.

Parallelism belongs within a single lens pass (e.g. multiple tracers reading different steps, feeding one fold), never across lenses. Running lenses concurrently severs the cumulative property — each lens must read the draft as the prior lens left it. A concurrent multi-lens run is a **panel pass** (a multi-finder sweep on a frozen draft, folding once as a composite), not a walk; label it as such and follow it with a real sequential walk.

When late walks stop finding things, rotate the **reviewer**, not the lens — a "dry" verdict from a saturated reviewer is weak evidence. Run the standing lenses **cold** (fresh-context readers given only the artifact plus repo read access), **sequentially** (not concurrently — sequential-cold preserves cumulation; a concurrent cold run is a panel pass, not a walk). Author verification of cold findings remains required: cold readers can misread deliberate design as defect.
```

(Leading blank line included — it separates from the preceding paragraph ending with `deposit-once discipline`. Each paragraph separated by a blank line.)

---

## Edit E5 — Generalize Plan Authoring Checklist #26 (proposal 162)

**Type:** REPLACEMENT
**Anchor:** `### 26. Convention-change plans grep for all occurrences`
**Anchor uniqueness:** grep count = 1 (line 1244 — Plan Authoring Checklist section)
**Verified NOT editing:** Orchestration Plan Rules #26 ("Deposits field convention") at line 795 — UNCHANGED.

**Replace (lines 1244–1248):**
```
### 26. Convention-change plans grep for all occurrences

When a plan redefines a convention — renaming a field, reformatting a header, changing a string pattern — the DEV step must grep for all occurrences of the old convention string rather than relying on a Planner-enumerated site list. The QA step must re-run the same grep and classify every hit as edited or deliberate-survivor (a site that intentionally retains the old form, e.g., a historical reference or backward-compatibility alias). Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

Source: proposal 136, lesson 2026-07-06
```

**With:**
```
### 26. After fixing an anti-pattern instance, sweep the whole artifact for siblings

After fixing any instance of an anti-pattern — a convention violation, a bare hardcoded number, a vacuous check, a wrong-signal guard, an un-isolated read — sweep the whole artifact for the same pattern and confirm zero siblings remain. The sweep must explicitly include places that merely QUOTE the pattern: negative examples, rationale text, documentation, and the fix's own illustration, where the pattern most often survives. A fix reported without a sibling-sweep is unverified.

**Worked example — convention changes.** When a plan redefines a convention — renaming a field, reformatting a header, changing a string pattern — the DEV step must grep for all occurrences of the old convention string rather than relying on a Planner-enumerated site list. The QA step must re-run the same grep and classify every hit as edited or deliberate-survivor (a site that intentionally retains the old form, e.g., a historical reference or backward-compatibility alias). Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

Source: proposals 136 + 162, lessons 2026-07-06 / 2026-07-20
```

---

## Edit E6 — New Orchestration Plan Rule #55 (proposals 165 + 167)

**Type:** INSERTION
**Anchor:** `Source: proposal 155, lesson 2026-07-19`
**Anchor uniqueness:** grep count = 1 (line 1070 — end of Rule 54)
**Location:** Insert AFTER this anchor (after line 1070, before the `---` on line 1072)
**Confirmed:** Rule 54 is the current highest in Orchestration Plan Rules. #55 is the correct next number.

**Insert:**
```

### 55. Assert a positive signal from the repo or tree that holds the state — empty output is not verification

(a) A `git status`/`git diff -- <file>` run from a submodule or worktree that does not track the file passes **vacuously** — the file is absent, not clean. Use `git -C <absolute path to the tracking repo>` to reach the repo that actually tracks the file, and assert on a positive signal (a known HEAD, a specific `--exit-code` diff), never merely empty output, which absence also produces. (b) Bellows lifecycle and dispatch state (`executable-` → `in-progress-` → `verdict-pending-` → `Done/` renames) is **main-tree uncommitted** and therefore structurally invisible to any worktree. A guard reading this state must use an absolute main-tree path and assert a positive signal proving it is reading the live tree. Canonical positive-signal example: a plan's own isolation pre-flight should confirm its own `in-progress-` file is visible, because that proves the read reached the right tree — its absence means a stale or wrong view. Evidence: plan 244's pre-flight ran `ls knowledge/decisions/` relative to its worktree and reported "no `in-progress-*` found" while its own in-progress file sat in the main tree.

Source: proposals 165 + 167, lessons 2026-07-20 / 2026-07-21

### 56. Resume machinery is justified only when the interrupted work is not reproducible

Before building resume machinery for a step that dies mid-write, ask whether the interrupted work can be regenerated from a recipe the plan already carries. If yes, prefer **restore-and-redo** over surgical resume: restore the pre-write state and reapply from the recipe. Surgical resume (determine what landed, apply the remainder) adds state, branches, and its own failure modes to buy back work a deterministic re-run would reproduce for free. Resume machinery is justified only when the interrupted work is NOT reproducible (e.g. committed classifications that cannot be blindly re-run without manufacturing duplicates). Either way, a restore that could discard foreign work needs a snapshot-aside plus per-hunk attribution first — restore is only safe on your own dirt.

Source: proposal 168, lesson 2026-07-21
```

(Leading blank line separates from Rule 54's source line. E7 follows E6 contiguously — both are inserted in a single block.)

---

## Edit E7 — New Orchestration Plan Rule #56 (proposal 168)

Included in E6's insertion block above. Separate documentation here for traceability.

**Type:** INSERTION (contiguous with E6)
**Text:** See E6 insertion block, second rule (`### 56.`).

---

## Mechanical Edit M1 — Version Bump (4.76 → 4.77)

**Type:** REPLACEMENT (two lines, applied as ONE atomic edit)
**Anchor 1:** `**Version:** 4.76` — grep count = 1 (line 5; note: NO `v` prefix)
**Anchor 2:** `**Last Updated:** 2026-07-21 (v4.76)` — grep count = 1 (line 6)

**Replace:**
```
**Version:** 4.76
**Last Updated:** 2026-07-21 (v4.76)
```

**With:**
```
**Version:** 4.77
**Last Updated:** 2026-07-21 (v4.77)
```

The changelog row at line 1825 (`v4.76:`) is a HISTORICAL record of the prior version's changes and is NOT bumped.

---

## Mechanical Edit M2 — Changelog Row

**Type:** INSERTION
**Anchor:** `| 2026-07-21 | v4.76: Gate 2 codification, 2026-07-20 cycle.`
**Anchor uniqueness:** grep count = 1 (line 1825)
**Location:** Insert a new row BEFORE this anchor (the changelog is newest-first)

**Insert:**
```
| 2026-07-21 | v4.77: Gate 2 codification, 2026-07-21 cycle. Seven edits from nine proposals (160, 162, 163, 165, 166, 167, 168, 170, 171). E1: widened the ACID lens's Isolation clause (proposal 160) to cover multi-step schedules — conflict-serializability merged as a facet of Isolation per CEO decision, NOT a sixth lens; the lens count deliberately remains five. E2: the lens set is open; a novel lens's fold is provisional (proposals 163 + 170). E3: parallelism belongs within a pass, never across lenses (proposal 166). E4: rotate the reviewer when late walks go quiet (proposal 171). E5: generalized Plan Authoring Checklist #26 to cover any anti-pattern sibling sweep, not only convention changes (proposal 162). E6: new Rule #55 — assert a positive signal from the repo or tree that holds the state (proposals 165 + 167). E7: new Rule #56 — resume machinery only when the work is not reproducible (proposal 168). Nine proposals (160, 162, 163, 165, 166, 167, 168, 170, 171) → implemented. |
```

---

## ADR-004 Compliance Note

E1–E4 are consequence-lens material and are worded to stay cleanly within the lens-set neighbourhood of `### The Full Cycle`. They do not interleave with the general adversarial doctrine (walk the list, fold, verify-mid-analysis) — E1 is an in-place widening of an existing lens's clause; E2/E3/E4 are appended as new paragraphs after the cycle's procedural content and before `### Why this process exists`. ADR-004's Decision 6 leaves the sixth-lens-vs-ACID-facet question open; E1's merge is within its bounds.

---

## Output Receipt

### Deposit
- **File:** `knowledge/development/gate-2-blueprint-2026-07-21.md`
- **Status:** Complete
- **Agent:** SA (Solution Architect)
- **Plan:** 249

### Ledger Updates

#### Prompt Feedback

| Feedback | Detail |
|----------|--------|
| The plan's explicit instruction to verify E1's self-test ("Would this clause have prompted a reader to ask about the DEV→QA window?") was valuable — it forced the SA to reason about the wording's adequacy rather than stopping at syntactic correctness. | Recommendation: retain self-test instructions for any edit whose purpose is to widen a question's scope — the test makes the success criterion concrete and falsifiable. |
