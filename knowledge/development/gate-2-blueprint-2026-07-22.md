# Gate 2 Blueprint — Cycle 2026-07-22 (v4.77 → v4.78)

**Plan:** 259 | **Step:** 1 (SA) | **Date:** 2026-07-23

## Pinned Git State

- **Governance-root HEAD:** `9974f1468a8dc6e01bd97750078ba2d763c8e4c7`
- **Template last-touching commit:** `042ae3431752b77d149d196d2c954e4877f9b57a`

## Proposal Read Confirmation

Fourteen rows read from DB via join query (proposals 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 184, 185, 186). Proposal 183 confirmed ABSENT from query and at `status='reference'` (out of scope, terminal).

---

## Dedup Verification (all against live v4.77)

| Edit | Grep pattern | Count |
|------|-------------|-------|
| E1 | `extraction-free comparison\|canonicalize.*longest-common-substring\|execute it against real data before deposit\|execute.*real corpus data before deposit` | 0 |
| E2 | `fix is a new draft\|re-run the lens that found\|treat.*fix as a.*draft no pass has examined` | 0 |
| E3 | `seam.*surface\|extraction contract\|restructuring for DRY\|byte-identical clauses` | 0 |
| E4 | `sketch.*deliverable\|physical shape\|block-per-item\|mandated format can hold` | 0 |
| E5 | `mechanical conformance pass\|mechanical pass.*distinct.*lenses\|conformance pass.*distinct` | 0 |
| E6 | `Halted-Plan Triage\|successor ladder\|three-rung\|artifact type before.*disposition` | 0 |
| E7 | `unmeasurable\|directory.*deposit.*neither present nor missing\|third outcome` | 0 |
| E8 | `/usr/bin/grep\|bounded negative\|ignore-aware.*silently under-report` | 0 |
| E9 | `pin the specifics\|absence of a pin.*hard failure\|generaliz.*guard.*specific` | 0 |
| E10 | `pre-state.*conclusion\|verification anchors.*licence to disagree\|equal evidence burden` | 0 |
| E11 | `reads.*absolute.*writes.*relative\|operation.*ROLE\|write.*relative.*working tree` | 0 |

All eleven edits confirmed absent from live v4.77.

### Known Adjacencies (distinct — word AROUND, not duplicate)

- **E1 vs :598** "Execute every check, depositing output to evidence files" — QA-runtime instruction, not draft-time; distinct.
- **E2 vs Checklist #26** (line 1262) — E2 cross-references #26 as its lens-side companion; no edit to #26.
- **E5 vs :1252** plan_lint mandate (Checklist #24) — E5 is the broader conformance pass; plan_lint is one step within it.
- **E7 vs Rule 37** (line 913) — E7 extends Rule 37 with the third outcome; does not replace existing content.
- **E8 amends Rule 36** (line 909) in place — extends, does not replace.
- **E11 vs Rule 55** (line 1078) absolute-path/vacuous-git — Rule 55 covers the READ-side positive-signal discipline; E11 adds the WRITE-relative half and frames both as operation roles.

### Lens Count Confirmation

- **:333** reads: "Cycle through adversarial analysis under five **named lenses**" — FIVE, unchanged.
- **:351** reads: "without imposing five heavy passes on a one-liner" — FIVE, unchanged.
- **:1845 / :1846** historical changelog counts — untouched (E5 is a mechanical pass, not a lens).

---

## Edit E1 — Execute against real data (merge of proposals 172 + 173 + 179)

**Type:** INSERTION  
**Region:** `## The Drafting Cycle`  
**Anchor:** `### Why this process exists` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + the paragraph BEFORE the anchor line.

**Exact text to insert:**

```
Any executable check, computed gate, or repeatable procedure embedded in a plan is validated ONLY by running it against real corpus data before deposit — the five adversarial lenses read the description, not the output, and cannot validate an executable check. A text-parsing check prefers extraction-free comparison (canonicalize both sides, then longest-common-substring) over parse-then-match; the parse step is where false FAILs are born. Record the measured range in the plan, not just the threshold. A lens pass that HARDENS such a check rather than rewriting it is a signal to execute it, not evidence it is now sound — a partially-fixed check is the most dangerous state it can occupy, because it buys confidence without buying coverage. For any plan that hands an agent a repeatable procedure over a set of items, run that procedure on the hardest one or two real items before deposit — not to verify the claims, but to confirm the method produces an answer at all; "the instructions are correct" and "the instructions work" are separate questions, and the lenses answer only the first.
```

---

## Edit E2 — A fix is a new draft (proposal 178)

**Type:** INSERTION  
**Region:** `## The Drafting Cycle`  
**Anchor:** `### Why this process exists` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + the paragraph BEFORE the anchor line, AFTER E1.

**Exact text to insert:**

```
After folding a fix, re-run the lens that found the ORIGINAL defect on the fix itself — treat the fix as a new draft that no pass has examined, not as a closed finding. Where the fix contains an executable step (a grep, a guard, a command), run it against real data before accepting it (per the execute-against-real-data rule above). The sharpest form: an accommodation written for one edge case often produces the defect ON that exact edge case. This rule is the lens-side companion to Plan Authoring Checklist #26 (the artifact-side sibling sweep); cross-reference, do not duplicate.
```

---

## Edit E3 — Restructuring for DRY trades a seam surface (proposal 180)

**Type:** INSERTION  
**Region:** `## The Drafting Cycle`  
**Anchor:** `### Why this process exists` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + the paragraph BEFORE the anchor line, AFTER E2.

**Exact text to insert:**

```
Before splitting or extracting shared content, diff the candidate regions and move only byte-identical clauses; unifying things that differ is the false-sharing bug, duplicating things that are identical is the drift bug. After extraction, walk the seam as its own surface — the ACID and destruction lenses have the most purchase there, because seam defects are drift and watering-down, not correctness of any single part. State the four-part extraction contract: what moves, what stays, how the moved content is retrieved, and what the retrieval promises (over-return, under-return, an absent source); each unstated part is a separate defect.
```

---

## Edit E4 — Sketch the deliverable's physical shape (proposal 182)

**Type:** INSERTION  
**Region:** `## The Drafting Cycle`  
**Anchor:** `### Why this process exists` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + the paragraph BEFORE the anchor line, AFTER E3.

**Exact text to insert:**

```
Before deposit, sketch one real block of the finished deliverable — the actual rows, cells, or sections a single item produces — and confirm the mandated format can hold everything the plan requires per item. The five adversarial lenses read the procedure; the shape of the product is orthogonal to all of them and invisible until you draw it. Where per-item output is rich (quotes, paired values, multi-part findings), prefer a block-per-item structure with a compact summary index over a table; a table forces truncation of exactly the evidence that motivated the plan.
```

---

## Edit E5 — Mechanical conformance pass (proposal 185) — NOT A LENS

**Type:** INSERTION  
**Region:** `## The Drafting Cycle`  
**Anchor:** `### Why this process exists` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + the paragraph BEFORE the anchor line, AFTER E4. This is the last insertion before the anchor.

**Exact text to insert:**

```
**Mechanical conformance pass (distinct from the adversarial lenses above).** Once the plan's shape is stable and before the closing walk, run a non-adversarial mechanical conformance pass: execute `plan_lint`, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope (the two sections number independently — never grep `### N.` unscoped). This pass checks the plan against the codified authoring rules, not against reality; the adversarial lenses do the latter. Most items are N/A for a given plan; the value is the few that are not and that no adversarial lens is looking for.
```

**⚠️ LENS COUNT GUARD:** E5 is worded as "distinct from the adversarial lenses above" and "non-adversarial." The five-lens list (lines 335-339) is NOT modified. The count phrases at :333 ("five named lenses") and :351 ("five heavy passes") remain UNCHANGED.

---

## DEV NOTE — E1 through E5 combined insertion

All five edits (E1–E5) are inserted as a consecutive block BEFORE the anchor `### Why this process exists`. The combined insertion replaces:

**old_string (the text DEV will find):**
```

### Why this process exists
```

**new_string (what DEV writes):**
```

Any executable check, computed gate, or repeatable procedure embedded in a plan is validated ONLY by running it against real corpus data before deposit — the five adversarial lenses read the description, not the output, and cannot validate an executable check. A text-parsing check prefers extraction-free comparison (canonicalize both sides, then longest-common-substring) over parse-then-match; the parse step is where false FAILs are born. Record the measured range in the plan, not just the threshold. A lens pass that HARDENS such a check rather than rewriting it is a signal to execute it, not evidence it is now sound — a partially-fixed check is the most dangerous state it can occupy, because it buys confidence without buying coverage. For any plan that hands an agent a repeatable procedure over a set of items, run that procedure on the hardest one or two real items before deposit — not to verify the claims, but to confirm the method produces an answer at all; "the instructions are correct" and "the instructions work" are separate questions, and the lenses answer only the first.

After folding a fix, re-run the lens that found the ORIGINAL defect on the fix itself — treat the fix as a new draft that no pass has examined, not as a closed finding. Where the fix contains an executable step (a grep, a guard, a command), run it against real data before accepting it (per the execute-against-real-data rule above). The sharpest form: an accommodation written for one edge case often produces the defect ON that exact edge case. This rule is the lens-side companion to Plan Authoring Checklist #26 (the artifact-side sibling sweep); cross-reference, do not duplicate.

Before splitting or extracting shared content, diff the candidate regions and move only byte-identical clauses; unifying things that differ is the false-sharing bug, duplicating things that are identical is the drift bug. After extraction, walk the seam as its own surface — the ACID and destruction lenses have the most purchase there, because seam defects are drift and watering-down, not correctness of any single part. State the four-part extraction contract: what moves, what stays, how the moved content is retrieved, and what the retrieval promises (over-return, under-return, an absent source); each unstated part is a separate defect.

Before deposit, sketch one real block of the finished deliverable — the actual rows, cells, or sections a single item produces — and confirm the mandated format can hold everything the plan requires per item. The five adversarial lenses read the procedure; the shape of the product is orthogonal to all of them and invisible until you draw it. Where per-item output is rich (quotes, paired values, multi-part findings), prefer a block-per-item structure with a compact summary index over a table; a table forces truncation of exactly the evidence that motivated the plan.

**Mechanical conformance pass (distinct from the adversarial lenses above).** Once the plan's shape is stable and before the closing walk, run a non-adversarial mechanical conformance pass: execute `plan_lint`, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope (the two sections number independently — never grep `### N.` unscoped). This pass checks the plan against the codified authoring rules, not against reality; the adversarial lenses do the latter. Most items are N/A for a given plan; the value is the few that are not and that no adversarial lens is looking for.

### Why this process exists
```

---

## Edit E6 — NEW `## Halted-Plan Triage` section (merge of proposals 174 + 175)

**Type:** INSERTION  
**Region:** New top-level section  
**Anchor:** `## Output Format` (unique, grep count: 1)  
**Placement:** Insert the new section + a `---` separator BEFORE the anchor line.

**old_string:**
```
## Output Format
```

**new_string:**
```
## Halted-Plan Triage

When triaging a halted plan to determine whether its work shipped under a different plan, search for a successor via a three-rung ladder, tried in order:

1. **Slug-reference grep** — `grep -rl '<qualified-slug>' <repo>/knowledge/decisions/Done/`. The slug must be qualified (e.g., `executable-216`, not bare `216` which matches incidental digits). A hit IS the confirmation — successor plans usually name the plan they replace. Silence proves nothing (Rule 36); do not read rung-1 silence as absence.
2. **Term-search** — search `Done/` for the halted plan's technical identifiers (function names, table names, flags). Works only when the title names a technical artifact; roughly half of legacy-named plans have no technical identifier.
3. **Date-adjacency** — the halted plan's filename date → same/adjacent-date entries in `Done/` → `git log --since/--until`. A date-adjacent plan is a CANDIDATE only — confirm by reading its body for a reference to the halted plan. Proximity alone does not license `archive`.

Stop at the first rung that answers; state which rung produced the result. Each rung's result is bounded — expect a real miss rate and report "no successor found" as a result, not a failed search.

**Classify the artifact type before choosing the disposition test.** For an executable, ask whether the CODE shipped — a successor plan that implemented the feature, the deposit's `landed` flag, the feature visible in source. For a diagnostic, ask whether the QUESTIONS were answered — look in `Done/diagnostic-*`, in `knowledge/research/` deposits, and for the same questions restated in a successor plan's Context. Source code is not evidence either way for a diagnostic; a module existing proves the area was built, never that these questions were answered. If you cannot establish that the questions were answered, a halted diagnostic is `ceo-review`, never `archive`.

---

## Output Format
```

---

## Edit E7 — Directory deposit = unmeasurable (proposal 176)

**Type:** INSERTION (append to Rule 37)  
**Region:** `## Orchestration Plan Rules`, Rule 37  
**Anchor:** `For paths unknown at plan-write time, either (a) use the parent directory (gate accepts directory existence as proxy), or (b) introduce a Step 0 diagnostic to discover the path before authoring the dependent step.` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + a new paragraph AFTER the anchor line.

**old_string:**
```
For paths unknown at plan-write time, either (a) use the parent directory (gate accepts directory existence as proxy), or (b) introduce a Step 0 diagnostic to discover the path before authoring the dependent step.

### 38.
```

**new_string:**
```
For paths unknown at plan-write time, either (a) use the parent directory (gate accepts directory existence as proxy), or (b) introduce a Step 0 diagnostic to discover the path before authoring the dependent step.

A directory-declared deposit is neither present nor missing — it is a THIRD outcome, `unmeasurable`, because the directory exists regardless of what the plan produced. When the `deposit_exists` gate passes on a directory path, fall through to discriminating evidence: look INSIDE the directory for a file attributable to that plan, and let the verdict text override the `landed` flag. More generally, when a check's subject can satisfy it without the thing being true, the check needs a third outcome rather than a better threshold.

### 38.
```

---

## Edit E8 — Amend Rule 36: completeness sweeps (proposal 177)

**Type:** INSERTION (append to Rule 36)  
**Region:** `## Orchestration Plan Rules`, Rule 36  
**Anchor:** `Common failure mode: grepping for warning text in reports from a period of clean state, then concluding "the warning logic doesn't work."` (unique, grep count: 1)  
**Placement:** Insert TWO blank lines + a new paragraph AFTER the anchor line.

**old_string:**
```
Common failure mode: grepping for warning text in reports from a period of clean state, then concluding "the warning logic doesn't work."

### 37.
```

**new_string:**
```
Common failure mode: grepping for warning text in reports from a period of clean state, then concluding "the warning logic doesn't work."

**Completeness sweeps.** For a completeness sweep, use `/usr/bin/grep` explicitly and state which binary — the shell's default `grep` is often a wrapper (e.g., `ugrep --ignore-files`) that honours `.gitignore` and silently under-reports. Bound the sweep with `--exclude-dir=.git,.bellows-worktrees,logs` and `--include` globs to stay under step-timeout limits, and report the exclusions as part of the finding. State the result as a bounded negative — *"no references found in `*.md`/`*.py`/`*.json` outside `.git`, `logs`, `.bellows-worktrees`"* — never as exhaustive. A bounded sweep reported as exhaustive is worse than no sweep.

### 37.
```

---

## Edit E9 — New Rule #57 (proposal 181)

**Type:** INSERTION  
**Region:** `## Orchestration Plan Rules`, after Rule 56  
**Anchor:** `## Lifecycle DB Read Protocol (Planner)` (unique, grep count: 1)  
**Placement:** Insert new rule + blank line + `---` BEFORE the anchor line, replacing the existing `---` separator.

**old_string:**
```
---

## Lifecycle DB Read Protocol (Planner)
```

**new_string:**
```
### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics

When moving a guard into a reusable or generic form, keep the mechanism generic but require the CALLER to pin the specifics (an enumerated list, a count, a name), and make the absence of a pin a HARD failure. A concrete enumerated list IS the guard; a generic description is a prompt to re-derive it, and re-derivation can undercount. Ask of any generalisation: did the concrete version carry information that the general version turns into a judgment call? If so, the specifics must be re-supplied at the point of use — the extraction converts a guard into a suggestion unless the reusable contract forces each user to pin.

Source: proposal 181, lesson 2026-07-22

### 58. Pre-stated conclusions require verification anchors and equal evidence burden

Pre-state a conclusion only with (1) named, agent-runnable verification anchors and explicit licence to disagree — the pre-resolution cannot launder an assertion into an audited finding; (2) a statement that the pre-resolutions are a fact about which items were investigated, not a distribution — the Planner holds no opinion on the rest; and (3) equal evidence burden on every disposition, so the cheap/default one is not the low-effort path. Watch specifically for bias toward whichever disposition the plan's method is best at recognising — the sweep exists to resist exactly that pull.

Source: proposal 186, lesson 2026-07-22

---

## Lifecycle DB Read Protocol (Planner)
```

---

## Edit E11 — Bellows dispatch path rules (proposal 184)

**Type:** INSERTION  
**Region:** `## Bellows Execution Model (Layer 1 Autonomous Dispatch)`  
**Anchor:** `### Bellows Operational Workarounds` (unique, grep count: 1)  
**Placement:** Insert new subsection BEFORE the anchor line.

**old_string:**
```
### Bellows Operational Workarounds
```

**new_string:**
```
### Dispatch Path Rules

Split path instructions in Bellows-dispatched plan steps by operation ROLE, never by a blanket "run from X." READS of shared state — a canonical DB, another repo, a config file — take an ABSOLUTE path, so the agent audits real on-disk state regardless of its working directory. WRITES of the step's own deposits take a path RELATIVE to the agent's working tree, so an isolated worktree commits and lands them; an absolute main-tree write path lands the file in the main tree where the worktree's commit cannot see it, producing the R2 teardown failure shape. This rule is about operation type, not dispatch topology — a lessons-forge cycle that ran in-place (2026-07-22) follows the same role split; the two path frames happen to coincide in that case.

Source: proposal 184, lesson 2026-07-22

### Bellows Operational Workarounds
```

---

## Mechanical Edit M1 — Version bump (4.77 → 4.78)

**Type:** REPLACEMENT  
**Anchor (line 5):** `**Version:** 4.77` (unique — bare number, no `v` prefix)  
**Anchor (line 6):** `**Last Updated:** 2026-07-21 (v4.77)` (unique)

**M1a old_string:** `**Version:** 4.77`  
**M1a new_string:** `**Version:** 4.78`

**M1b old_string:** `**Last Updated:** 2026-07-21 (v4.77)`  
**M1b new_string:** `**Last Updated:** 2026-07-22 (v4.78)`

---

## Mechanical Edit M2 — Changelog row

**Type:** INSERTION  
**Region:** `## Lessons Learned`  
**Anchor:** `| 2026-07-21 | v4.77: Gate 2 codification, 2026-07-21 cycle.` (unique, grep count: 1 — first few words suffice for match)  
**Placement:** Insert new row BEFORE the anchor line (append at top of table body, after header).

**old_string:**
```
| 2026-07-21 | v4.77: Gate 2 codification, 2026-07-21 cycle.
```

**new_string:**
```
| 2026-07-22 | v4.78: Gate 2 codification, 2026-07-22 cycle. Fourteen proposals (172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 184, 185, 186) via eleven edits, two merges (E1 = 172+173+179 execute-before-deposit; E6 = 174+175 halted-plan triage). E1: executable checks/procedures validated by running against real data, not lenses (merge of 172+173+179). E2: a fix is a new draft — re-run the original lens on the fix (178). E3: restructuring for DRY trades a seam surface (180). E4: sketch the deliverable's physical shape before deposit (182). E5: mechanical conformance pass distinct from the five adversarial lenses — the lens count deliberately stays five (185). E6: new `## Halted-Plan Triage` section — three-rung successor ladder + artifact-type triage (merge of 174+175). E7: directory-declared deposit is `unmeasurable`, a third outcome (176). E8: Rule 36 amended — `/usr/bin/grep` for completeness sweeps, bounded negatives (177). E9: new Rule #57 — generalizing a guard requires the caller to pin specifics (181). E10: new Rule #58 — pre-stated conclusions need verification anchors + equal evidence burden (186). E11: Bellows dispatch path rules — reads-absolute/writes-relative by operation role (184). Fourteen proposals → implemented. |
| 2026-07-21 | v4.77: Gate 2 codification, 2026-07-21 cycle.
```

**⚠️ Historical changelog counts at :1845/:1846 ("five"/"four") are NOT touched by any edit.**

---

## Summary of Anchor Uniqueness Verification

| Edit | Anchor substring | Grep count |
|------|-----------------|------------|
| E1–E5 | `### Why this process exists` | 1 |
| E6 | `## Output Format` | 1 |
| E7 | `For paths unknown at plan-write time, either (a) use the parent directory` | 1 |
| E8 | `Common failure mode: grepping for warning text in reports from a period of clean state` | 1 |
| E9+E10 | `## Lifecycle DB Read Protocol (Planner)` | 1 |
| E11 | `### Bellows Operational Workarounds` | 1 |
| M1a | `**Version:** 4.77` | 1 |
| M1b | `**Last Updated:** 2026-07-21 (v4.77)` | 1 |
| M2 | `\| 2026-07-21 \| v4.77: Gate 2 codification, 2026-07-21 cycle.` | 1 |

---

## Output Receipt

**Status:** Complete  
**Agent:** SA (Step 1)  
**Plan:** 259 — Gate 2 Codification (cycle 2026-07-22)

### Ledger Updates
#### Prompt Feedback
**2026-07-23 — Gate 2 Codification cycle 2026-07-22 (SA Step 1)**

1. The plan's inline line-number references (:333, :351, :598, :1252, :1845, :1846) were all accurate against live v4.77 — authoring-time pinning worked well for this cycle.
2. The merged-proposals convention (E1 = 172+173+179, E6 = 174+175) with a stated spine and per-proposal specifics produced clean, non-redundant edit text on first draft.
3. The explicit "known adjacencies to word AROUND" list in the plan prevented three potential false-dedup calls (E1 vs :598, E5 vs :1252, E11 vs Rule 55).
4. Fourteen proposals across eleven edits is near the practical maximum for a single Gate 2 plan — the SA step consumed significant context tracking all anchors and dedup patterns simultaneously.
5. The constraint "E5 IS A MECHANICAL PASS, NOT A SIXTH LENS" was the most load-bearing editorial guardrail; bolding and explicit count-guard instructions in the plan made it unmissable.
