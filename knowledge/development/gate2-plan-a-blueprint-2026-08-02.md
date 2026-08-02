# Gate 2 Plan A — SA Blueprint (Plan 291)

**Date:** 2026-08-02
**Step:** 1 (SA)
**Plan:** 291

---

## Task A — Pre-edit state

### Full SHA-256 hashes

| File | SHA-256 |
|---|---|
| `DRAFTING_CYCLE.md` | `3951bcf8bc2d9e5f85cf39241ec215e1831cdf07f3cb258bb455b09fab0baaf0` |
| `PLANNER_TEMPLATE.md` | `0c53222fbacdc89cb44899d2df400093a41bed52bdab12d41879ea6fee383e04` |
| `RULE_20_SELF_CHECK_BLOCK.md` | `3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644` |

### CEO Context pin comparison (by 12-hex PREFIX)

| File | Pin prefix | Measured prefix | Match |
|---|---|---|---|
| `DRAFTING_CYCLE.md` | `3951bcf8bc2d` | `3951bcf8bc2d` | ✅ |
| `PLANNER_TEMPLATE.md` | `0c53222fbacd` | `0c53222fbacd` | ✅ |

`RULE_20_SELF_CHECK_BLOCK.md` matches the full 64-hex authoring pin `3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644`. No doctrine drift.

### Version-collision counts (measured)

| Pattern | File | Count | Sites |
|---|---|---|---|
| `1.2 (2026-07-30)` | `DRAFTING_CYCLE.md` | **2** | `:5` version line + `:166` History row |
| `4.81` | `PLANNER_TEMPLATE.md` | **3** | `:5` version + `:6` Last Updated + `:1882` Lessons Learned row |

A replace-all on either pattern destroys a governance changelog entry.

### Pre-edit baseline counts (for QA dev-log contract)

| Measurement | Command | Result |
|---|---|---|
| History row count | `grep -Fc -- '**1.' DRAFTING_CYCLE.md` | **3** (rows 1.2, 1.1, 1.0) |
| Lessons Learned sectional count | `awk '/^## Lessons Learned/{f=1;next} /^## /{f=0} f' PLANNER_TEMPLATE.md \| grep -Fc -- '\| 2026-'` | **104** |

---

## Task B — `DRAFTING_CYCLE.md` proposal edits (three of eleven)

### B1 — 204 → §2.7 (R1)

**Edit type:** APPEND into existing bullet (same physical line)

**Anchor:** The closing sentence of §2.7's first bullet:
```
A lens pass that *hardens* such a check is a signal to run it, not evidence it is now sound.
```
`grep -Fc 'A lens pass that *hardens* such a check is a signal to run it, not evidence it is now sound.' DRAFTING_CYCLE.md` = **1** ✓ unique

**Insertion anchor (insert strictly AFTER this sentence, on the same line):** `not evidence it is now sound.`

**BEFORE (line 80, showing the full first bullet):**
```
- **Execute against real data.** Any executable check, computed gate, or repeatable procedure is validated ONLY by running it on the hardest one or two real items before deposit — the lenses read the description, not the output. Prefer extraction-free comparison for text checks; record the measured range, not just the threshold. A lens pass that *hardens* such a check is a signal to run it, not evidence it is now sound.
```

**AFTER (the same bullet with 204's text appended):**
```
- **Execute against real data.** Any executable check, computed gate, or repeatable procedure is validated ONLY by running it on the hardest one or two real items before deposit — the lenses read the description, not the output. Prefer extraction-free comparison for text checks; record the measured range, not just the threshold. A lens pass that *hardens* such a check is a signal to run it, not evidence it is now sound. For every command the plan MANDATES, state what it prints on success, what it prints on failure, and confirm those two differ. If they do not differ, the check cannot be read from its output and needs a positive control that produces visible output. **Name the channel explicitly when it is not stdout** — a command that fatals to stderr and prints nothing to stdout is byte-identical, on stdout, to the clean result. A command that can produce empty output on BOTH paths needs a liveness proof before it can be trusted as a gate: pair it with its exit code, or with an input known to make it speak.
```

**Post-edit verification:**
- `grep -Fc 'For every command the plan MANDATES' DRAFTING_CYCLE.md` should return 1 (new text present)
- `grep -Fc 'now sound. For every command the plan MANDATES' DRAFTING_CYCLE.md` should return 1 (boundary confirms correct placement)
- Must-survive greps — see Task D

---

### B2 — 202 → §2.8 (R2)

**Edit type:** INSERT new bullet (not an append into an existing bullet). CEO decision 2026-08-02, declared deviation from §Q4.

**Anchor:** The closing sentence of §2.8's oscillation bullet:
```
not a threshold asserted up front.
```
`grep -Fc 'not a threshold asserted up front.' DRAFTING_CYCLE.md` = **1** ✓ unique

**Insert strictly AFTER the line ending with this anchor.** The oscillation bullet is NOT modified — every one of its clauses survives verbatim.

**BEFORE (line 97 — the oscillation bullet's closing text; the NEW bullet goes after this entire line):**
```
- **Persistent oscillation is a signal, not a quota.** If the same region keeps being re-folded across walks, or the per-lens finding count stops trending toward dry, take that as the prompt to step back and joint-resolve or escalate — a design tension the sequential walk will not settle. **This is a judgment signal, deliberately NOT a fixed draft-count limit.** The base sets no hard "escalate after N walks / N drafts" rule; how many walks is too many is something we learn and tune from real runs, not a threshold asserted up front.
```

**AFTER (the oscillation bullet unchanged, followed by the new bullet):**
```
- **Persistent oscillation is a signal, not a quota.** If the same region keeps being re-folded across walks, or the per-lens finding count stops trending toward dry, take that as the prompt to step back and joint-resolve or escalate — a design tension the sequential walk will not settle. **This is a judgment signal, deliberately NOT a fixed draft-count limit.** The base sets no hard "escalate after N walks / N drafts" rule; how many walks is too many is something we learn and tune from real runs, not a threshold asserted up front.
- **Deletion is the third resolution, alongside joint-resolve and escalate.** When the same region has been re-folded repeatedly — **three or more times across walks is the point at which to ask** — stop patching and ask whether the record or the runtime already supplies a simpler method; repeated folding is evidence the region is carrying more than it should. **Treat every-patch-correct as evidence FOR deletion, not against it:** a region where each successive fold was individually right, and which still needed the next one, is precisely the region whose design is wrong. **This is a prompt to ASK, not a quota** — consistent with the judgment signal above, it sets no hard "delete after N folds" rule and reaching the count is never by itself a reason to cut. A trim taken on this signal still needs §2.7's subtractive-trim verification — establish the subsumption against live data — and the same whole-artifact sweep an addition would need.
```

**Post-edit verification:**
- `grep -Fc 'Deletion is the third resolution' DRAFTING_CYCLE.md` should return 1 (new text present)
- Must-survive greps — see Task D

---

### B3 — 206 → §3 (R3)

**Edit type:** INSERT new paragraph

**Anchor:** The closing text of §3's gate-span sentence:
```
evaluated as if the QA step had said it.
```
`grep -Fc 'evaluated as if the QA step had said it.' DRAFTING_CYCLE.md` = **1** ✓ unique

**Insert strictly AFTER the line containing this anchor.** The sentence containing `is a **record, not instructions**` is a must-survive item but is NOT the anchor (B3's anchor is that sentence's closing text).

**BEFORE (line 107 — the end of the paragraph before the fenced example):**
```
The compact form is **load-bearing** — the plan body carries structure, not narrative. Full walk-by-walk analysis lives in a scratchpad file (`scratchpad/`, session-local and ephemeral); only the per-lens summary lines appear in the plan's `## Drafting Cycle` block. Do not keep a running fold-count in the Cycle Log — fold counts belong in the compact per-lens lines (e.g., `w1 2 folded; w2 dry`), not as a separate running tally. The `## Drafting Cycle` section in a deposited plan is a **record, not instructions** — nothing in it is addressed to any executing agent, and the final QA step's gate span absorbs it, so a gate-matching string quoted in the log is evaluated as if the QA step had said it.
```

**AFTER (the original paragraph unchanged, followed by the new paragraphs, then the fenced example continues):**
```
The compact form is **load-bearing** — the plan body carries structure, not narrative. Full walk-by-walk analysis lives in a scratchpad file (`scratchpad/`, session-local and ephemeral); only the per-lens summary lines appear in the plan's `## Drafting Cycle` block. Do not keep a running fold-count in the Cycle Log — fold counts belong in the compact per-lens lines (e.g., `w1 2 folded; w2 dry`), not as a separate running tally. The `## Drafting Cycle` section in a deposited plan is a **record, not instructions** — nothing in it is addressed to any executing agent, and the final QA step's gate span absorbs it, so a gate-matching string quoted in the log is evaluated as if the QA step had said it.

**The Cycle Log must therefore contain no string a gate matches — describe such strings, never quote them.** This covers Rule 20 banner text, deposit and scope markers, path tokens, and test-name patterns. **The prohibition is scoped to the `## Drafting Cycle` block:** a plan's QA step MUST carry the banner strings, because they are what the gate requires; it is the RECORD that must not repeat them.

**After compacting or editing the log, re-run the gate and confirm the WARN/PASS set is unchanged.** A WARN that DISAPPEARS when the only edit was to the log is the signature of this defect — the log has satisfied a check on the step's behalf.
```

**Post-edit verification:**
- `grep -Fc 'The Cycle Log must therefore contain no string a gate matches' DRAFTING_CYCLE.md` should return 1
- `grep -Fc 'scoped to the' DRAFTING_CYCLE.md` — confirm the scope word "Cycle Log" is present (not "plan")
- Must-survive greps — see Task D

---

## Task C — `PLANNER_TEMPLATE.md` proposal edits (three of eleven)

### Rule numbering

Highest existing rule: **60** (`### 60. Rule 20 self-check form selected by plan class` at `:1105`, verified unique via `grep -Fn '### 60.' PLANNER_TEMPLATE.md` = 1 hit). Next free: **61**.

**Assignment: 201 → Rule 61; 203 → Rule 62.** Both APPEND at the END of the Orchestration Plan Rules section, in ASCENDING order, after Rule 60's closing `Source:` line.

**Required final order:** Rule 60, then Rule 61, then Rule 62. Each anchors on the preceding rule's `Source:` line.

### C1 — 201 → new Rule 61 (R6)

**Edit type:** INSERT new rule block

**Anchor:** Rule 60's closing `Source:` line:
```
Source: proposal 192, lesson 2026-07-30
```
`grep -Fc 'Source: proposal 192, lesson 2026-07-30' PLANNER_TEMPLATE.md` = **1** ✓ unique

**Insert strictly AFTER this line.** This anchor is at `:1113` — inserting at Rule 60's heading (`:1105`) would orphan Rule 60's body under Rule 61.

**BEFORE (lines 1113–1116):**
```
Source: proposal 192, lesson 2026-07-30

---

## Lifecycle DB Read Protocol (Planner)
```

**AFTER:**
```
Source: proposal 192, lesson 2026-07-30

### 61. Pin run-time-copied artifacts by content hash, and name which job the pin does

For any artifact a step COPIES at run time — the canonical Rule 20 block, a shared prompt fragment, a template a step reproduces verbatim — the plan records the artifact's content hash at AUTHORING and re-verifies it at QA. **Prefer a hash over a version string for anything a machine must trust:** a version changes only when someone remembers to bump it and a stale one asserts something false, while a hash changes on any edit.

**Two different jobs a pin can do, and one pin cannot serve both.** *Unchanged by THIS plan* is a fail-closed guard: the artifact must be byte-identical before and after, and any difference is a defect. *Unchanged since AUTHORING* is drift detection: the artifact may legitimately have moved, and the pin exists so the run notices rather than proceeding on stale assumptions. State which job each pin does at the point it is taken — a pin whose job is unstated is read as whichever the reader assumes, and the two demand opposite responses to the same observation.

**Before recommending a change to a run-time-copied artifact, enumerate the in-flight plans it would land on.** Deposited-but-unrun plans were authored against the current bytes and inherit the edit at their next dispatch.

Source: proposal 201, lesson 2026-07-29

---

## Lifecycle DB Read Protocol (Planner)
```

**Post-edit verification:**
- `grep -Fc '### 61.' PLANNER_TEMPLATE.md` should return 1
- `grep -Fc 'Source: proposal 201, lesson 2026-07-29' PLANNER_TEMPLATE.md` should return 1
- Confirm Rule 60's body and `Source:` line still sit under Rule 60's heading (not orphaned)

---

### C2 — 203 → new Rule 62 (R7)

**Edit type:** INSERT new rule block

**Anchor (SEQUENCED — re-derive from post-Rule-61 text):** Rule 61's closing `Source:` line:
```
Source: proposal 201, lesson 2026-07-29
```
This anchor does NOT exist in the pre-edit file — it is created by C1. ⚠️ **Exempt from pre-edit uniqueness grep.** Verify its uniqueness AFTER Rule 61 is applied: `grep -Fc 'Source: proposal 201, lesson 2026-07-29' PLANNER_TEMPLATE.md` must return **1**.

**Insert strictly AFTER Rule 61's `Source:` line, BEFORE the `---` separator and `## Lifecycle DB Read Protocol`.**

**AFTER (showing the end of Rule 61 through the section break):**
```
Source: proposal 201, lesson 2026-07-29

### 62. Establish that a recovered-from state is reachable before authoring recovery machinery

Before building resume, restore or repair machinery, establish that the state it recovers FROM is reachable under the ACTUAL dispatch path — **read the runtime that would produce it; do not reason from the general shape of the problem.** This is the necessity-side complement to Rule 56: Rule 56 asks whether the interrupted work is reproducible and therefore what SHAPE the recovery should take; this rule asks the prior question of whether the interruption can occur at all.

**A doctrine rule with a stated precondition is not owed when the precondition is false.** Citing such a rule to justify machinery whose precondition does not hold satisfies the citation, not the rule.

**Unreachable-state machinery is not merely inert.** It branches, it greps, it restores — and a branch that can never legitimately fire can still fire on a state it MISCLASSIFIES, manufacturing a failure the system would not otherwise have had. Establish the state and keep the machinery, or delete it; do not carry it as harmless.

Source: proposal 203, lesson 2026-07-30

---

## Lifecycle DB Read Protocol (Planner)
```

**Post-edit verification:**
- `grep -Fc '### 62.' PLANNER_TEMPLATE.md` should return 1
- `grep -Fc 'Source: proposal 203, lesson 2026-07-30' PLANNER_TEMPLATE.md` should return 1
- Confirm Rule 61 heading line number is strictly LESS than Rule 62 heading line number
- Confirm both are in the Rules section (line numbers strictly greater than Rule 60's heading `:1105` and strictly less than `## Lifecycle DB Read Protocol`'s new line number)

---

### C3 — 205 → Checklist #26 (R8)

**Edit type:** INSERT paragraph above `Source:` line + EXTEND (not replace) the `Source:` line

**Anchor for paragraph insertion:** Checklist #26's `Source:` line:
```
Source: proposals 136 + 162 + 193, lessons 2026-07-06 / 2026-07-20 / 2026-07-30
```
`grep -Fc 'Source: proposals 136 + 162 + 193, lessons 2026-07-06 / 2026-07-20 / 2026-07-30' PLANNER_TEMPLATE.md` = **1** ✓ unique

**Insert the new paragraph DIRECTLY ABOVE this `Source:` line (not after the Worked example block — anchoring on the Source line eliminates the judgment call of where the example ends).**

**Then EXTEND (not replace) the `Source:` line itself.**

**BEFORE (lines 1291–1293):**
```
Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

Source: proposals 136 + 162 + 193, lessons 2026-07-06 / 2026-07-20 / 2026-07-30
```

**AFTER:**
```
Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

**Sweep forward, not only sideways.** The sibling sweep above looks at sites that ALREADY EXIST. Ask of every fold whether the defect is a property of THIS SITE or of this CLASS of site — **only the first is safely fixed in place.** When it is a property of the class, write the general form into the plan's Conflict Ledger as a named constraint, so later folds in the same cycle are checked against it rather than rediscovering it. A fold that changes a convention must be swept FORWARD as well as sideways: the sites that will be written after the fold are as much in scope as the ones written before it.

Source: proposals 136 + 162 + 193 + 205, lessons 2026-07-06 / 2026-07-20 / 2026-07-30 / 2026-07-30
```

**Post-edit verification:**
- `grep -Fc 'Sweep forward, not only sideways.' PLANNER_TEMPLATE.md` should return 1 (new text present)
- `grep -Fc '136' PLANNER_TEMPLATE.md` — confirm prior attribution `136` survives
- `grep -Fc '162' PLANNER_TEMPLATE.md` — confirm prior attribution `162` survives (check it appears on the Source line)
- `grep -Fc '193' PLANNER_TEMPLATE.md` — confirm prior attribution `193` survives
- `grep -Fc '+ 205' PLANNER_TEMPLATE.md` — confirm new attribution added
- Must-survive greps — see Task D

---

## Task D — Must-survive enumeration

### §2.7 (`DRAFTING_CYCLE.md`) — B1 modifies this region

The following clauses must still grep present AFTER B1's edit:

| # | Clause | `grep -Fc` pattern |
|---|---|---|
| D1 | Core mandate | `Any executable check, computed gate, or repeatable procedure is validated ONLY by running it on the hardest one or two real items before deposit` |
| D2 | Extraction-free preference | `Prefer extraction-free comparison for text checks` |
| D3 | Measured range | `record the measured range, not just the threshold` |
| D4 | Closing sentence (also B1 anchor) | `A lens pass that *hardens* such a check is a signal to run it, not evidence it is now sound.` |

All four verified present in pre-edit file (count 1 each).

### §2.8 (`DRAFTING_CYCLE.md`) — B2 inserts after this region

The oscillation bullet is UNMODIFIED. Must-survive:

| # | Clause | `grep -Fc` pattern |
|---|---|---|
| D5 | Opening | `If the same region keeps being re-folded across walks, or the per-lens finding count stops trending toward dry` |
| D6 | Judgment signal | `**This is a judgment signal, deliberately NOT a fixed draft-count limit.**` |
| D7 | Closing (also B2 anchor) | `not a threshold asserted up front.` |

All three verified present in pre-edit file (count 1 each).

### §3 (`DRAFTING_CYCLE.md`) — B3 inserts into this region

| # | Clause | `grep -Fc` pattern |
|---|---|---|
| D8 | Record-not-instructions | `is a **record, not instructions**` |
| D9 | Fenced Cycle Log example opening | ` ## Drafting Cycle` (the backtick-fenced line inside the code block) |

D8 verified present (count 1). D9 is inside a fenced code block starting at `:109`.

### Checklist #26 (`PLANNER_TEMPLATE.md`) — C3 modifies this region

| # | Clause | `grep -Fc` pattern |
|---|---|---|
| D10 | Quote-the-pattern | `must explicitly include places that merely QUOTE the pattern` |
| D11 | Weight toward mutator | `Weight the sweep toward the step that MUTATES` |
| D12 | Consistency after fold | `After any fold, every other site stating the same rule, number, path, or count must be checked for consistency before the fold is closed.` |
| D13 | Fold completeness | `The fold is not done until all sites agree.` |
| D14 | Worked example heading | `**Worked example — convention changes.**` |
| D15 | Worked example closing sentence | `An occurrence-grep catches both.` |
| D16 | Source line — `136` | `136` (on the Source line) |
| D17 | Source line — `162` | `162` (on the Source line) |
| D18 | Source line — `193` | `193` (on the Source line) |

All verified present in pre-edit file (count 1 each for D10–D15; D16–D18 verified present on the Source line).

---

## Task E — Version + changelog edits (five of eleven)

### E1 — `DRAFTING_CYCLE.md:5` version bump (R4)

**Edit type:** SURGICAL substring swap against lengthened unique anchor

**Lengthened anchor (verified unique):**
```
**Version:** 1.2 (2026-07-30). Amended only through the Iteration Protocol (§6).
```
`grep -Fc '**Version:** 1.2 (2026-07-30). Amended only through the Iteration Protocol (§6).' DRAFTING_CYCLE.md` = **1** ✓ unique

**Substring swap:** `1.2 (2026-07-30)` → `1.3 (2026-08-02)` within this anchor only.

**BEFORE (line 5):**
```
**Version:** 1.2 (2026-07-30). Amended only through the Iteration Protocol (§6).
```

**AFTER:**
```
**Version:** 1.3 (2026-08-02). Amended only through the Iteration Protocol (§6).
```

⚠️ `Amended only through the Iteration Protocol (§6).` MUST survive — the swap targets the version substring only.

---

### E2 — `DRAFTING_CYCLE.md` `## History` PREPEND (R5)

**Edit type:** INSERT (PREPEND) — not a swap. The 1.2 row must remain verbatim.

**⚠️ DECLARED DEVIATION:** the map's edit-map row 8 says "APPEND row after last `## History` row" at `:168`, but `:168` is the 1.0 row (the OLDEST). The table is NEWEST-FIRST (`:166`=1.2, `:167`=1.1, `:168`=1.0), and the map's own §Q7 says PREPEND. §6 line 157 says "appends a dated row" — that wording is STALE against the file's newest-first table. **PREPEND, not append.**

**Anchor:** The 1.2 History row:
```
- **1.2 (2026-07-30):** Codified proposals 191, 194, 195 (+parent), 197, 198, 200.
```
(Using a prefix of the line as the anchor; the full line is ~500 characters. The prefix `- **1.2 (2026-07-30):**` is verified unique at `:166`.)

**Insert the new 1.3 row DIRECTLY ABOVE this line.**

**BEFORE (lines 165–166):**
```
## History
- **1.2 (2026-07-30):** Codified proposals 191, 194, 195 (+parent), 197, 198, 200. §2.6: clone-against-newest cold-panel discipline (191), review-target rotation (194). §2.7: subtractive-trim verification with enumerated premises (195+parent), lens attestation integrity (200). §3: compact Cycle Log form load-bearing (197). §4: four shipped plan_lint defect fixes documented — negation-aware dry check, Closing-presence check unconditional, cold-panel check line-anchored, Vulnerabilities regex fixed (198). **The lens count deliberately stays five** — all additions are sub-rules of existing lenses or cross-cutting rules, not new lenses. Paired with Plan B (286, bellows).
```

**AFTER:**
```
## History
- **1.3 (2026-08-02):** Codified proposals 202, 204, 206. §2.7: for every mandated command, state what it prints on success and on failure and confirm those differ, with a positive control when they do not and an explicit channel when it is not stdout (204). §2.8: deletion as a third resolution alongside joint-resolve and escalate, with every-patch-correct read as evidence FOR deletion (202). §3: the Cycle Log must contain no string a gate matches, and the WARN/PASS set is re-checked after any edit to the log (206). **The lens count deliberately stays five** — all three are sub-rules of existing sections, not new lenses. **No paired Plan B (CEO decision, 2026-08-01).** 206 amends §3, so `## When this file changes` requires the §4 self-check be kept in lockstep; the pre-existing `gates.py:449` span-regex defect that makes this rule necessary is **recorded in the Forward Register** and is NOT fixed here — this plan is governance-only by CEO decision. §4's self-check is unchanged by this amendment and remains in lockstep.
- **1.2 (2026-07-30):** Codified proposals 191, 194, 195 (+parent), 197, 198, 200. §2.6: clone-against-newest cold-panel discipline (191), review-target rotation (194). §2.7: subtractive-trim verification with enumerated premises (195+parent), lens attestation integrity (200). §3: compact Cycle Log form load-bearing (197). §4: four shipped plan_lint defect fixes documented — negation-aware dry check, Closing-presence check unconditional, cold-panel check line-anchored, Vulnerabilities regex fixed (198). **The lens count deliberately stays five** — all additions are sub-rules of existing lenses or cross-cutting rules, not new lenses. Paired with Plan B (286, bellows).
```

**Post-edit verification:**
- `grep -Fc -- '**1.' DRAFTING_CYCLE.md` should return **4** (gained exactly one row)
- The 1.2 row is present and VERBATIM
- The 1.3 row sits ABOVE the 1.2 row (newest-first): `grep -Fn '**1.3 (' DRAFTING_CYCLE.md` line number < `grep -Fn '**1.2 (' DRAFTING_CYCLE.md` line number
- The 1.3 row does NOT claim a §6 deferral — it says `§4's self-check is unchanged by this amendment and remains in lockstep`

---

### E3 — `PLANNER_TEMPLATE.md:5` version bump (R9)

**Edit type:** SURGICAL substring swap against verified-unique anchor

**Anchor:**
```
**Version:** 4.81
```
`grep -Fc '**Version:** 4.81' PLANNER_TEMPLATE.md` = **1** ✓ unique (bare `4.81` hits 3)

**BEFORE (line 5):**
```
**Version:** 4.81
```

**AFTER:**
```
**Version:** 4.82
```

---

### E4 — `PLANNER_TEMPLATE.md:6` Last Updated bump (R10)

**Edit type:** SURGICAL substring swap against verified-unique anchor. This is the eleventh edit the map's count omits.

**Anchor:**
```
**Last Updated:** 2026-07-30 (v4.81)
```
`grep -Fc '**Last Updated:** 2026-07-30 (v4.81)' PLANNER_TEMPLATE.md` = **1** ✓ unique

**BEFORE (line 6):**
```
**Last Updated:** 2026-07-30 (v4.81)
```

**AFTER:**
```
**Last Updated:** 2026-08-02 (v4.82)
```

---

### E5 — `PLANNER_TEMPLATE.md` `## Lessons Learned` PREPEND (R11)

**Edit type:** INSERT (PREPEND) — not a swap. The 2026-07-30 row must remain verbatim.

**Anchor:** The existing 2026-07-30 Lessons Learned row (at `:1882`):
```
| 2026-07-30 | v4.81: Gate 2 codification, 2026-07-30 cycle.
```
(Using a prefix. The full row is ~500 characters.)

**Insert the new row DIRECTLY ABOVE this line.**

**BEFORE (lines 1880–1882):**
```
| Date | Lesson |
|---|---|
| 2026-07-30 | v4.81: Gate 2 codification, 2026-07-30 cycle. Four edits from three proposals (192, 193, 196) plus one coupled edit. New Rule 60 for Rule 20 form-by-class selection (192). New Rule 59 — read the cited rule before citing it (196). Checklist #26 strengthened with fold-sweep sibling consistency (193). Checklist #4 amended to conditional form cross-referencing Rule 60 (192-coupled). Three proposals (192, 193, 196) → implemented. |
```

**AFTER:**
```
| Date | Lesson |
|---|---|
| 2026-08-02 | v4.82: Gate 2 codification, 2026-08-02 cycle. Three edits from three proposals (201, 203, 205). New Rule 61 — pin run-time-copied artifacts by content hash, and name whether a pin is a fail-closed guard or drift detection (201). New Rule 62 — establish that a recovered-from state is reachable before authoring recovery machinery; the necessity-side complement to Rule 56 (203). Checklist #26 extended with the forward sweep — a fold that is a property of the CLASS becomes a named Conflict Ledger constraint (205). ⚠️ 205 ships as PROSE ONLY: diagnostic 290 established by execution that no useful subset of its remedy is statically checkable, so the checklist text is its sole enforcement. Three proposals (201, 203, 205) → implemented. |
| 2026-07-30 | v4.81: Gate 2 codification, 2026-07-30 cycle. Four edits from three proposals (192, 193, 196) plus one coupled edit. New Rule 60 for Rule 20 form-by-class selection (192). New Rule 59 — read the cited rule before citing it (196). Checklist #26 strengthened with fold-sweep sibling consistency (193). Checklist #4 amended to conditional form cross-referencing Rule 60 (192-coupled). Three proposals (192, 193, 196) → implemented. |
```

**Post-edit verification:**
- Sectional row count: `awk '/^## Lessons Learned/{f=1;next} /^## /{f=0} f' PLANNER_TEMPLATE.md | grep -Fc -- '| 2026-'` should return **105** (gained exactly one row over pre-edit 104)
- The 2026-07-30 row is present and VERBATIM
- The new 2026-08-02 row sits ABOVE the 2026-07-30 row (newest-first)

---

## Task F — Lens-count guard

### Three count phrases located with live line numbers (as found by me)

| # | Phrase | Line | Full context |
|---|---|---|---|
| 1 | `full five-lens walk` | **:29** | `run the **full five-lens walk** (§2.1–§2.5).` |
| 2 | `run the five lenses` | **:73** | `run the five lenses **cold**` |
| 3 | `all five` | **:132** | `one result line per **required** lens (all five for T1/T2, ACID included)` |

**No blueprinted edit modifies any of these three lines.** The edits touch:
- B1: line 80 (§2.7 first bullet)
- B2: inserts after line 97 (§2.8 fourth bullet)
- B3: inserts after line 107 (§3)
- E1: line 5 (version)
- E2: inserts at line 165/166 (History)

Lines 29, 73, and 132 are untouched. No proposal in this batch adds a lens.

---

## Task G — Status flip blueprint

### Parameterised UPDATE

**Load-bearing ordering:** Every doc edit lands, and is COMMITTED (Task F2), BEFORE the flip.

**Step 1: Compute timestamp into a shell variable:**
```bash
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

**Step 2: Take a `.backup` restore point FIRST (before any UPDATE):**
```bash
BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate2-291-$(date -u +%Y%m%dT%H%M%SZ).db" && \
  sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
```

**Step 3: Prove backup exists:**
```bash
ls -la "$BK"
sqlite3 "file:$BK?immutable=1" "SELECT count(*) FROM lesson_proposals WHERE id BETWEEN 201 AND 206 AND status='proposed';"
```
Expected: **6**. Use `?immutable=1`, NOT `?mode=ro` (which cannot read a fresh WAL backup without sidecars).

**Step 4: The UPDATE statement (with row-count check in the SAME invocation):**
```bash
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)" && sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db \
  "UPDATE lesson_proposals SET status='implemented', status_updated_at='$TS', status_updated_by='ceo' \
   WHERE id IN (201,202,203,204,205,206) AND status='proposed'; SELECT changes();"
```
**Expected `changes()`: exactly 6.** Anything else is a catastrophic signature — 0 = nothing matched; 1–5 = partial; >6 = the predicate reached rows this plan does not own. Any value but 6: HALT.

**⚠️ $TS and the UPDATE MUST be in the SAME invocation** (joined with `&&`). An empty `$TS` writes `status_updated_at=''` and exits 0; only the GLOB assertion catches it.

**Step 5: Read back each of the six by id:**
```sql
SELECT id, status, route, status_updated_at, status_updated_by
FROM lesson_proposals WHERE id BETWEEN 201 AND 206 ORDER BY id;
```
Confirm each reads `implemented`, `codify`, and both audit columns populated.

**Step 6: Timestamp FORMAT assertion:**
```sql
SELECT count(*) FROM lesson_proposals WHERE id BETWEEN 201 AND 206
  AND status_updated_at GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
```
Must return **6**.

**Step 7: Hard assertion + reconcile:**
```sql
SELECT count(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 201 AND 206;
```
Must return **0** (hard).
```sql
SELECT count(*) FROM lesson_proposals WHERE status='proposed' AND id NOT BETWEEN 201 AND 206;
```
Expected **0** at authoring; a non-zero value from a proposal created during a verdict gate is legitimate and is a reconcile-note, not a FAIL.

### Three columns pinned

| Column | Value | Reason |
|---|---|---|
| `status` | `'implemented'` | The flip |
| `status_updated_at` | `$TS` (format `YYYY-MM-DDTHH:MM:SSZ`) | Audit: WHEN |
| `status_updated_by` | `'ceo'` | Audit: BY WHOSE AUTHORITY. ⚠️ Declared deviation from map's §Q8 `'gate2'` — the map's value is REJECTED BY THE LIVE SCHEMA: `CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner','ceo','auto'))` |

### Schema verification (read from `sqlite_master`)

- `status` column: `CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented', 'reference'))` — `'implemented'` is schema-valid ✓
- `status_updated_by` column: `CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))` — `'ceo'` is schema-valid ✓; `'gate2'` is NOT schema-valid ✗

### DB precondition (verified by the SA, 2026-08-02)

```sql
SELECT count(*) FROM lesson_proposals WHERE id BETWEEN 201 AND 206 AND status='proposed' AND route='codify';
```
Expected: **6** before the flip, **0** after.

---

## §6 append-vs-prepend discrepancy

§6 (line 157) reads: `Each Gate-2 codification bumps the version and appends a dated row naming the units it changed.`

The History table is NEWEST-FIRST (`:166`=1.2, `:167`=1.1, `:168`=1.0). The §6 wording "appends" is stale against the live table's newest-first convention. All prior codifications (1.1, 1.2) PREPENDED (newest above oldest). This plan PREPENDs, consistent with the live convention and the map's §Q7. Recorded for a future batch to correct.

---

## Confirmed rule numbers

- **201 → Rule 61** (new, appended after Rule 60)
- **203 → Rule 62** (new, appended after Rule 61)

Both are in the Orchestration Plan Rules section, NOT the Plan Authoring Checklist (the two sections number independently).

---

## Output Receipt

### Status
**Complete**

### Deposits
- `knowledge/development/gate2-plan-a-blueprint-2026-08-02.md`

### Ledger Updates

#### Prompt Feedback

**Agent:** SA (Step 1, Plan 291)
**Plan:** 291 — Gate 2 Plan A: codify proposals 201–206

No prompt feedback to report. All anchors resolved on first attempt. The plan's anchor-discipline instructions and version-collision warnings were accurate and actionable — every predicted count matched the measured value, every anchor was verified unique, and no judgment calls were needed on placement. The plan's exhaustive enumeration of must-survive clauses eliminated the class of failure where a correct-looking edit drops a clause from an adjacent region.
