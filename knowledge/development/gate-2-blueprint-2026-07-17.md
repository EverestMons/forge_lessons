# Gate 2 Blueprint — 2026-07-17 Cycle (PLANNER_TEMPLATE v4.74 → v4.75)

**Date:** 2026-07-18
**Agent:** Solution Architect
**Plan:** 228
**Source proposals:** 149, 150, 151, 152, 153, 154 (all routed `codify`)
**Target:** `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root, live v4.74)

---

## Dedup Summary

Grepped the live template (v4.74) for all five edit topics — **zero hits** across all searches:

| Search pattern | Hits | Conclusion |
|---|---|---|
| `drafting.cycle` | 0 | No existing section or mention |
| `region.scoped` | 0 | No existing rule on scoped metrics |
| `bare.*(expected\|number)` | 0 | No existing checklist item on bare predictions |
| `schema.*version.*bump` | 0 | No existing checklist item on schema-version pin enumeration |
| `integration.vs.record` | 0 | No existing mention of the fourth lens |
| `four.*lenses\|named.lenses` | 0 | No existing mention of named-lens analysis |
| `diminishing.returns` | 0 | No existing mention of the stop signal |
| `off.queue\|deposit.once` | 0 | No existing mention of off-queue drafting or deposit-once |

**Confirmed:** highest existing Rule = 52 (line 1015), highest existing Checklist = 28 (line 1209). No `## The Drafting Cycle` section exists. New items are 53 / 29 / 30 / 31 — no renumbering required.

---

## Edit 1 — New Section: `## The Drafting Cycle`

**Source:** Proposals 150 + 152 (both implemented — the section IS both; 150 defines the cycle, 152 amends it with the fourth lens)

**Anchor:** Insert AFTER the `---` at line 312 (separator between `## Quick Fix Protocol` and `## Output Format`) and BEFORE `## Output Format` at line 314.

**Exact insertion text:**

```markdown

## The Drafting Cycle

The Drafting Cycle is the adversarial pre-deposit analysis process for orchestration plans. It is **tiered** — a mandatory floor applies universally; escalation to the full cycle is triggered by scope or by the floor pass itself.

### Mandatory Floor — Integration-vs-Record Pass (every diagnostic and executable)

Before depositing any plan, run the **integration-vs-record pass**: scan the drafted plan against LESSONS.md, `knowledge/decisions/Done/`, `knowledge/research/`, and the actual code for precedent conflicts, convention violations, and the "is this actually trivial?" check. Clean pass → deposit. The pass surfaces entanglement or non-trivial blast radius → **ESCALATE** to the full cycle.

### Escalation Triggers

Escalate to the full four-pass cycle when:
- The floor pass surfaces entanglement, convention conflict, or non-trivial blast radius
- The plan is inherently high-stakes: production-data mutation, a CEO-run tool, a money-affecting write path, or a cross-machine / irreversible action

### The Full Cycle

Draft the plan **off-queue** — outside the watched `decisions/` directory, because deposit equals dispatch. Cycle through adversarial analysis under four **named lenses**, each a distinct pass:

1. **Weak spots** — correctness and safety of the plan itself
2. **Destruction / mitigating-rewrites** — harm to existing functionality; agent watering-down of constants, contracts, or invariants
3. **Vulnerabilities** — adversarial and degenerate conditions
4. **Integration-vs-record** — scan the draft against the project's accumulated record (LESSONS.md, `knowledge/decisions/Done/`, `knowledge/research/`, the code) for convention violations, precedent conflicts, and stated-consequence gaps; passes 1–3 require adversarial imagination, pass 4 requires institutional memory

Each pass: severity-rank findings, verify claims against code and data mid-analysis (grep, not assume), report what held up alongside what failed. Fold **all** accepted findings into the next draft. Repeat until a pass honestly reports **diminishing returns** — the signal to stop drafting. Fold-and-deposit **exactly once** (deposit-once discipline).

### Why this process exists

Trivial-looking plans have repeatedly caused retroactive fixes because no analysis preceded them. The mandatory floor pass makes analysis universal without imposing four heavy passes on a one-liner, and preserves the cycle's own diminishing-returns stop signal (which mandatory-max would contradict). The Drafting Cycle hardens the **plan**; Planner verification at the verdict gate hardens the **deliverable** — the 216→217 boundary established this distinction. Plan 224 was the first to run the full four-lens cycle and landed first-dispatch clean.

---
```

**Dedup note:** Grepped `drafting.cycle`, `four.*lenses`, `named.lenses`, `diminishing.returns`, `off.queue`, `deposit.once` — zero hits. No existing coverage.

---

## Edit 2 — New Rule 53: Region-scoped metrics end-to-end

**Source:** Proposal 153

**Anchor:** Insert AFTER `Source: proposal 147, lesson 2026-07-07` at line 1023 (end of Rule 52) and BEFORE the `---` at line 1025.

**Exact insertion text:**

```markdown

### 53. Region-scoped metrics must be computed with scope applied end to end

Any metric that is semantically scoped — by region, carrier, contract, config, or time window — must be computed with that scope applied end to end: every aggregate in the chain, not just the final comparison. A single unscoped aggregate silently converts "this entity's value" into "everyone's value" and the verdict inherits the error. When two tools disagree on a scoped metric, the one that carries the scope through its entire computation is the authority. A characterization line that feeds an escalation deserves the same scoping scrutiny as the decision itself.

Source: proposal 153, lesson 2026-07-17
```

**Dedup note:** Grepped `region.scop` — zero hits. Sibling framing to Rule 52 (re-verify inherited claims); no overlap.

---

## Edit 3 — New Checklist #29: Pair predictions with verify-and-explain

**Source:** Proposal 149

**Anchor:** Insert AFTER `Source: proposal 145, lesson 2026-07-06` at line 1213 (end of Checklist #28) and BEFORE the `---` at line 1215.

**Exact insertion text:**

```markdown

### 29. Pair every predicted number with a verify-and-explain clause

Never state a bare expected number in plan text. Pair every prediction with a verify-and-report clause ("verify and report actual, never force") — the prediction is evidence of Planner intent, not ground truth. Where the number gates a destructive step, name the catastrophic signature too (e.g., "if `implemented` is anywhere near 33, halt loudly"). When a step reports a different number than the plan predicted, the plan is the first suspect, not the step.

Source: proposal 149, lesson 2026-07-16
```

**Dedup note:** Grepped `bare.*(expected|number)` — zero hits. No existing coverage of prediction-pairing discipline.

---

## Edit 4 — New Checklist #30: Schema/migration QA rows

**Source:** Proposal 151

**Anchor:** Insert immediately AFTER Edit 3 (Checklist #29).

**Exact insertion text:**

```markdown

### 30. Schema/migration QA rows name the absolute canonical path and show pre- and post-version

A worktree QA step cannot verify a live-DB migration against an untracked canonical DB — it fresh-builds and reports the new version as a migration. Schema-bump QA rows must name the **absolute** canonical DB path and require the pre-migration version to be shown before the post-version (a fresh build cannot show the pre-version — that asymmetry is the tell). The Planner verifies the canonical DB by absolute path at the verdict gate **before** composing the verdict. Activation is pending per machine until each app restart is confirmed.

Source: proposal 151, lesson 2026-07-17
```

**Dedup note:** Grepped `schema.*version.*bump` — zero hits. Checklist #28 (DB-out-of-git evidence-source contract) is a sibling covering general worktree QA evidence; this item addresses the specific schema-migration pre/post asymmetry. No overlap.

---

## Edit 5 — New Checklist #31: Schema-version bumps enumerate version-pinned assertions

**Source:** Proposal 154

**Anchor:** Insert immediately AFTER Edit 4 (Checklist #30).

**Exact insertion text:**

```markdown

### 31. Schema-version bumps enumerate and classify all version-pinned assertions

Any plan bumping `CURRENT_SCHEMA_VERSION` must, in the same DEV step: (a) grep for every version-pinned assertion and enumerate hits in plan text before dispatch; (b) classify each as tripwire (update to new version) or migration-precondition (preserve — changing it destroys the test's meaning); (c) re-grep after editing to prove none remain. Leaving version pins for QA to discover converts a mechanical authoring task into either a blocked plan or a QA role violation.

Source: proposal 154, lesson 2026-07-17
```

**Dedup note:** Grepped `schema.*version.*bump`, `version.pin` — zero hits. No existing coverage of version-pin enumeration discipline.

---

## Version Bump

**Line 5:** `**Version:** 4.74` → `**Version:** 4.75`
**Line 6:** `**Last Updated:** 2026-07-16 (v4.74)` → `**Last Updated:** 2026-07-18 (v4.75)`

---

## Changelog Row

**Anchor:** Insert at the TOP of the changelog table, AFTER the `|---|---|` header separator at line 1753 and BEFORE the existing v4.74 row at line 1754.

**Exact insertion text:**

```
| 2026-07-18 | v4.75: Gate 2 codification, 2026-07-17 cycle. New section `## The Drafting Cycle` — tiered named process with mandatory integration-vs-record floor, four named lenses, and diminishing-returns stop (from proposals 150 + 152). New Rule 53 (region-scoped metrics end-to-end; from proposal 153). Checklist #29 (pair predictions with verify-and-explain; from proposal 149), #30 (schema/migration QA rows name absolute path and show pre/post version; from proposal 151), #31 (schema-version bumps enumerate version-pinned assertions; from proposal 154). Six proposals (149–154) → implemented. |
```

**Renumbering check:** No renumbering. Existing highest Rule = 52, new Rule = 53. Existing highest Checklist = 28, new Checklist = 29/30/31. All existing items unchanged.

---

## Status Transitions

All six proposals transition to `implemented`:

| Proposal ID | Source Lesson | Current Status | New Status |
|---|---|---|---|
| 149 | 2026-07-16 bare-number discipline | proposed | implemented |
| 150 | 2026-07-16 drafting cycle | proposed | implemented |
| 151 | 2026-07-17 worktree migration QA | proposed | implemented |
| 152 | 2026-07-17 drafting cycle pass 4 amendment | proposed | implemented |
| 153 | 2026-07-17 region-scoped metrics | proposed | implemented |
| 154 | 2026-07-17 schema-version pins | proposed | implemented |

Zero superseded, zero rejected. Proposals 150 and 152 are co-authors of one section (The Drafting Cycle) — both implemented, neither supersedes the other.

---

## Output Receipt

**Step:** 1 (SA)
**Status:** Complete
**Agent:** Solution Architect
**Deposits:**
- `knowledge/development/gate-2-blueprint-2026-07-17.md`

### Ledger Updates

#### Prompt Feedback

| Feedback | Source |
|---|---|
| The plan's CEO Context section embedding the tiered trigger criteria (floor / escalate / full-cycle) with explicit rationale made blueprinting the Drafting Cycle section straightforward — the exact governance shape was decided at plan authoring, not left for SA to infer. | Plan 228, Step 1 |
| Specifying "highest Rule = 52, highest Checklist = 28" in CEO Context eliminated a potential anchoring error — without it SA would have had to scan and count, risking off-by-one on item numbering. | Plan 228, Step 1 |
