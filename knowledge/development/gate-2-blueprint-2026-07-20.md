# Gate 2 Blueprint — 2026-07-20 Cycle

**Plan:** 246 — Gate 2 Codification (cycle 2026-07-20)
**Step:** 1 (SA)
**Target:** `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root, READ-ONLY this step)
**Live version:** 4.75
**Target version:** 4.76

## Git Pin (Cross-Step Drift Guard)

- **HEAD:** `3191a2014dc00f82a70eb48f56a4c390af8478d0`
- **Template last-touching commit:** `d4dca9f0f263b56f6dcad25f3f6581035fa44cd5`

DEV re-checks the latter before applying — if the template changed between this read and DEV's write, the blueprint's anchors are stale.

---

## Edit 1 — Amend `### Escalation Triggers` (proposal 158)

**Source lesson:** entry 150 (DB `entry_id` 150, proposal 158) — "The full Drafting Cycle applies to DIAGNOSTICS, not just executables"

**Anchor — REPLACE the full `### Escalation Triggers` subsection content (lines 324–326):**
```
Escalate to the full four-pass cycle when:
- The floor pass surfaces entanglement, convention conflict, or non-trivial blast radius
- The plan is inherently high-stakes: production-data mutation, a CEO-run tool, a money-affecting write path, or a cross-machine / irreversible action
```

**Replacement text (note: "four-pass cycle" phrase is ALSO changed by edit 2's lens-count sweep — the replacement here uses the count-free form so both edits compose cleanly):**
```
Escalate to the **full cycle** when:
- The floor pass surfaces entanglement, convention conflict, or non-trivial blast radius
- The plan is inherently high-stakes: production-data mutation, a CEO-run tool, a money-affecting write path, or a cross-machine / irreversible action
- The plan is a **diagnostic** whose findings will be authored from without re-verification, whose questions depend on data whose availability is unconfirmed, that scopes a multi-plan arc, or that touches a leak, money, or governance surface

For a diagnostic the highest-value lens is **weak spots aimed at the questions themselves** — is each question answerable, answerable *from here*, and phrased so that "unknown" is an acceptable answer rather than a failure the agent will paper over. Evidence: diag-229 Q6/Q7 (struck for answering data questions from data that did not exist).
```

**Dedup check:**
- `grep -cF 'diagnostic escalat' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'authored from without' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'weak spots aimed at the questions' PLANNER_TEMPLATE.md` → 0 hits
- Known-adjacent: the existing executable-shaped triggers (lines 325–326) are RETAINED and extended, not duplicated.

---

## Edit 2 — ACID as Fifth Named Lens + Lens-Count Sweep (proposal 157)

**Source lesson:** entry 149 (DB `entry_id` 149, proposal 157) — "Add an ACID lens to the Drafting Cycle"

### 2a. Add ACID lens after lens 4

**Anchor — REPLACE lens 4 line and add lens 5 (line 335):**

Live line 335:
```
4. **Integration-vs-record** — scan the draft against the project's accumulated record (LESSONS.md, `knowledge/decisions/Done/`, `knowledge/research/`, the code) for convention violations, precedent conflicts, and stated-consequence gaps; passes 1–3 require adversarial imagination, pass 4 requires institutional memory
```

**Replacement text (lens 4 description byte-identical; ONLY the note tail extended; lens 5 added):**
```
4. **Integration-vs-record** — scan the draft against the project's accumulated record (LESSONS.md, `knowledge/decisions/Done/`, `knowledge/research/`, the code) for convention violations, precedent conflicts, and stated-consequence gaps; passes 1–3 require adversarial imagination, pass 4 requires institutional memory, pass 5 requires systems reasoning over the plan's own requirements
5. **ACID (atomicity, consistency, isolation, durability)** — examine the plan's accepted requirements **as a system**, specifically hunting contradictions between requirements folded by earlier passes and converting accidental properties into stated ones. Atomicity: what is the state set if this half-completes, and is every member acceptable? Consistency: which invariant closes each gap, and is it stated or merely lucky? Isolation: what does a concurrent actor observe mid-operation? Durability: what survives a crash, and is the surviving record sufficient to reconstruct what happened?
```

### 2b. Lens-count sweep — three phrases become false when the fifth lens lands

**Phrase 1 (line 324) — already handled by edit 1's replacement above:** `"Escalate to the full four-pass cycle when:"` → `"Escalate to the **full cycle** when:"` (count-free — durable if the lens list grows again). Edit 1's replacement text already carries this change.

**Phrase 2 (line 330):**

Live:
```
Draft the plan **off-queue** — outside the watched `decisions/` directory, because deposit equals dispatch. Cycle through adversarial analysis under four **named lenses**, each a distinct pass:
```

Replacement (ONLY "four" → "five"; the off-queue intro sentence is element (v) — byte-untouched):
```
Draft the plan **off-queue** — outside the watched `decisions/` directory, because deposit equals dispatch. Cycle through adversarial analysis under five **named lenses**, each a distinct pass:
```

**Phrase 3 (line 341, in `### Why this process exists`):**

Live:
```
Trivial-looking plans have repeatedly caused retroactive fixes because no analysis preceded them. The mandatory floor pass makes analysis universal without imposing four heavy passes on a one-liner, and preserves the cycle's own diminishing-returns stop signal (which mandatory-max would contradict). The Drafting Cycle hardens the **plan**; Planner verification at the verdict gate hardens the **deliverable** — the 216→217 boundary established this distinction. Plan 224 was the first to run the full four-lens cycle and landed first-dispatch clean.
```

Replacement (ONLY "four heavy passes" → "five heavy passes"; "four-lens cycle" EXEMPT — historical record):
```
Trivial-looking plans have repeatedly caused retroactive fixes because no analysis preceded them. The mandatory floor pass makes analysis universal without imposing five heavy passes on a one-liner, and preserves the cycle's own diminishing-returns stop signal (which mandatory-max would contradict). The Drafting Cycle hardens the **plan**; Planner verification at the verdict gate hardens the **deliverable** — the 216→217 boundary established this distinction. Plan 224 was the first to run the full four-lens cycle and landed first-dispatch clean.
```

**Dedup check:**
- `grep -cF 'ACID' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'atomicity, consistency, isolation, durability' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'systems reasoning' PLANNER_TEMPLATE.md` → 0 hits
- Known-adjacent: the four existing lens descriptions are RETAINED byte-identical (only the note tail of lens 4's line is extended).

**Diminishing-returns reconciliation (edit 2 owns this check for `### Why this process exists`):** The clause "preserves the cycle's own diminishing-returns stop signal" remains true under element (f) of the rewritten stop condition — (f) explicitly retains diminishing-returns as the outer framing. No additional phrase change needed.

---

## Edit 3 — Rewrite the Stop Condition (proposal 159, CEO walk-the-list form)

**Source lesson:** entry 151 (DB `entry_id` 151, proposal 159) — "A drafting-cycle lens is not done at one pass"
**Evidence entry:** LESSONS.md "2026-07-20: Walk the lens list, don't re-run one lens to dry" (entry 99, C1 — un-ingested)
**CEO decision:** entry 94's within-lens iterate-to-dry model is REPLACED by the walk-the-list form.

**Anchor — REPLACE exactly ONE paragraph (line 337):**

Live:
```
Each pass: severity-rank findings, verify claims against code and data mid-analysis (grep, not assume), report what held up alongside what failed. Fold **all** accepted findings into the next draft. Repeat until a pass honestly reports **diminishing returns** — the signal to stop drafting. Fold-and-deposit **exactly once** (deposit-once discipline).
```

**Replacement text (walk-the-list form with all seven elements (a)–(g) and all six preserved-doctrine items (i)–(vi)):**
```
Each pass: severity-rank findings, verify claims against code and data mid-analysis (grep, not assume), report what held up alongside what failed. Fold **all** accepted findings into the next draft after each pass. Walk the full lens list in order — one pass per lens per walk. A lens is re-run only on a **subsequent walk** of the entire list, never immediately on its own fold; the structural reason is that a defect introduced by a fold is usually caught by a *different* lens reading different evidence, not by re-running the lens that produced it. The cycle is done when a full walk returns **zero or only-minor findings** — this IS the diminishing-returns signal: a full walk that finds nothing new. A dry pass is an honestly reportable success, not underperformance — manufacturing minor findings to appear diligent is the same Goodhart failure as forcing a predicted number. The last event before deposit must be a **lens pass, never a fold** (a fold produces a draft no pass has examined): if the walk's final lens pass folded anything, a brief confirming pass over the folded draft supplies the closing lens pass (expected dry; any new material finding re-opens the walk; new minor findings at the closing check are recorded in the deposit, not folded — a minor-only closing pass still satisfies the deposit condition; this closing check is exempt from the walk-rotation rule — it is a deposit-condition check, not a lens re-run). Cross-lens contradictions are the closing lens's job (ACID runs last — see lens 5). Fold-and-deposit **exactly once** (deposit-once discipline).
```

**Blast radius verification:** the replacement target is EXACTLY the one paragraph at line 337. The off-queue/lens-list intro above it (line 330) is edit 2's territory. The `### Why this process exists` subsection below (line 339–341) is NOT part of the replacement — its only touches are edit 2's "four heavy passes" → "five heavy passes" and the diminishing-returns reconciliation check (passed — no phrase change needed).

**Dedup check:**
- `grep -cF 'walk the' PLANNER_TEMPLATE.md` → 0 hits (phrase "Walk the full lens list" is new)
- `grep -cF 'walk-the-list' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'subsequent walk' PLANNER_TEMPLATE.md` → 0 hits
- Known-adjacent: diminishing-returns language in `### Why this process exists` is NOT duplicated — the rewrite references it structurally via element (f) but does not restate the `### Why` section's text.

### Per-Element Verification Checklist

#### Seven Added Elements (a)–(g) from CEO Context

| Element | Requirement | Present in replacement text | Quote |
|---|---|---|---|
| (a) | One pass per lens; walk the whole lens list in order, folding after each pass | YES | "Fold **all** accepted findings into the next draft after each pass. Walk the full lens list in order — one pass per lens per walk." |
| (b) | A lens is re-run only on a subsequent walk, never immediately on its own fold | YES | "A lens is re-run only on a **subsequent walk** of the entire list, never immediately on its own fold" |
| (c) | Cycle done when a full walk returns zero or only-minor findings | YES | "The cycle is done when a full walk returns **zero or only-minor findings**" |
| (d) | Last event before deposit must be a lens pass, never a fold; closing mechanism stated | YES | "The last event before deposit must be a **lens pass, never a fold** … if the walk's final lens pass folded anything, a brief confirming pass over the folded draft supplies the closing lens pass (expected dry; any new material finding re-opens the walk; new minor findings at the closing check are recorded in the deposit, not folded — a minor-only closing pass still satisfies the deposit condition; this closing check is exempt from the walk-rotation rule — it is a deposit-condition check, not a lens re-run)" |
| (e) | Honest-zero guard: dry pass is reportable success, not underperformance | YES | "A dry pass is an honestly reportable success, not underperformance — manufacturing minor findings to appear diligent is the same Goodhart failure as forcing a predicted number" |
| (f) | Diminishing-returns retained as outer framing | YES | "this IS the diminishing-returns signal: a full walk that finds nothing new" |
| (g) | Cross-lens contradictions are the closing lens's job (ACID runs last) | YES | "Cross-lens contradictions are the closing lens's job (ACID runs last — see lens 5)" |

#### Six Preserved-Doctrine Items (i)–(vi)

| Item | Requirement | Status | Quote / Evidence |
|---|---|---|---|
| (i) | Severity-rank findings each pass | PRESERVED | "severity-rank findings" |
| (ii) | Verify claims against code and data mid-analysis (grep, not assume) | PRESERVED | "verify claims against code and data mid-analysis (grep, not assume)" |
| (iii) | Report what held up alongside what failed | PRESERVED | "report what held up alongside what failed" |
| (iv) | Fold ALL accepted findings | PRESERVED | "Fold **all** accepted findings into the next draft after each pass" |
| (v) | Off-queue/deposit-equals-dispatch intro sentence ABOVE the paragraph is intact and NOT restated | INTACT / NOT RESTATED | Line 330 "Draft the plan **off-queue** — outside the watched `decisions/` directory, because deposit equals dispatch." is OUTSIDE the replacement paragraph; not duplicated in the rewrite (confirmed: grep "off-queue" and "deposit equals dispatch" in the replacement text → 0 hits) |
| (vi) | Fold-and-deposit exactly once (deposit-once discipline) | PRESERVED | "Fold-and-deposit **exactly once** (deposit-once discipline)" |

---

## Edit 4 — New Rule 54 (proposal 155)

**Source lesson:** entry 147 (DB `entry_id` 147, proposal 155) — "An instruction that is not a numbered row, a named test, or a gate is an instruction that evaporates"

**Anchor — INSERT after Rule 53's source line (after line 1060 "Source: proposal 153, lesson 2026-07-17"), BEFORE the `---` at line 1062:**

**Insertion text:**
```

### 54. Every requirement needs a structural home — a numbered row, a named test, or a gate condition

Requirements living only in prose paragraphs do not survive execution — every instruction bound to a numbered QA row, a named test, or a mechanical gate is honoured; every instruction living only in prose is dropped. When a verdict adds a requirement mid-plan, restate it as a numbered row in the plan file, not only in the verdict. Location (in the plan file the agent works from) precedes numbering: a numbered item in a document the agent never reads is invisible regardless of its number (Rule 51 — corrections go into plan text, not verdict prose; Rule 54 says what form those corrections take). Evidence: the 2026-07-19 arc — three prose-only instructions dropped; every numbered/named/gated instruction honoured.

Source: proposal 155, lesson 2026-07-19
```

**Sibling framing to Rule 51:** Rule 51 (line 1040: "Corrections at verdict time go into plan text, not verdict disposition prose") says WHERE a correction goes. Rule 54 says WHAT FORM any requirement must take. The two are siblings — Rule 54 explicitly references Rule 51 in its text.

**Dedup check:**
- `grep -cF 'structural home' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'prose paragraphs do not survive' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'Location (in the plan file' PLANNER_TEMPLATE.md` → 0 hits
- Known-adjacent: Rule 51 (line 1040) — sibling, not duplicate. Rule 51 says WHERE; Rule 54 says WHAT FORM. Rule 54 explicitly cites Rule 51.

**No renumbering:** Rule 53 remains `### 53.` — Rule 54 is appended after it.

---

## Edit 5 — New Checklist #32 (proposal 156)

**Source lesson:** entry 148 (DB `entry_id` 148, proposal 156) — "Grep presence is not effect — a wired call needs an observed behaviour change, not a source-code match"

**Anchor — INSERT after Checklist #31's source line (after line 1268 "Source: proposal 154, lesson 2026-07-17"), BEFORE the `---` at line 1270:**

**Insertion text:**
```

### 32. Verification of a wired call must observe a behaviour change through the real entry point

Grep proves wiring exists; a green suite proves it does not throw; only an **observed delta** proves it works. Verification of any wired call must observe a behaviour change through the real entry point — a before-value, the action, an after-value. When designing such a check, verify the construction actually produces the expected delta (a test built on the wrong arithmetic reports a false failure and costs more trust than no test). This is the general form of Workaround #15 (post-activation live canary for daemon write paths); Workaround #15 is the specific instance for silent/best-effort daemon channels. Evidence: plan 230 (stopped one row short of closing on a money path because every test called the engine directly, not through the real entry point).

Source: proposal 156, lesson 2026-07-19
```

**Dedup check:**
- `grep -cF 'observed delta' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'observed-delta' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'behaviour change' PLANNER_TEMPLATE.md` → 0 hits
- `grep -cF 'before-value' PLANNER_TEMPLATE.md` → 0 hits
- Known-adjacent: Workaround #15 (line 1537, "Post-activation live canary for silent/best-effort daemon write paths") — Checklist #32 is the GENERAL rule; Workaround #15 is the specific instance. Checklist #32 cites Workaround #15 explicitly. Not a duplicate.

**No renumbering:** Checklist #31 remains `### 31.` — Checklist #32 is appended after it.

---

## Version Bump

**Line 5 — REPLACE:**
```
**Version:** 4.75
```
**With:**
```
**Version:** 4.76
```

**Line 6 — REPLACE:**
```
**Last Updated:** 2026-07-18 (v4.75)
```
**With:**
```
**Last Updated:** <EXECUTION-DATE> (v4.76)
```

(`<EXECUTION-DATE>` is the ONE sanctioned substitution — DEV resolves to the actual apply date.)

---

## Changelog Row

**Anchor — INSERT one new row at the TOP of the `| Date | Lesson |` table under `## Lessons Learned` (after line 1808 `|---|---|`, before the current top data row at line 1809):**

**Insertion text (one row, no unescaped `|` in cell text):**
```
| <EXECUTION-DATE> | v4.76: Gate 2 codification, 2026-07-20 cycle. Amended `## The Drafting Cycle` — (1) diagnostic-shaped escalation triggers alongside executable-shaped (from proposal 158); (2) ACID as fifth named lens, run last, examining the plan's accepted requirements as a system (from proposal 157); (3) stop condition rewritten to walk-the-list form: one pass per lens, walk the full list, re-run only on subsequent walks, done when a full walk returns zero or only-minor findings, last event before deposit must be a lens pass not a fold (from proposal 159; entry 94/DB 151 within-lens iterate-to-dry model REPLACED by walk-the-list form, evidence entry 99/C1). New Rule 54 (every requirement needs a structural home — numbered row, named test, or gate condition; sibling to Rule 51; from proposal 155). New Checklist #32 (verification of a wired call must observe a behaviour change through the real entry point; general form of Workaround #15; from proposal 156). Five proposals (155–159) → implemented. |
```

**Verification:** the v4.75 row (current line 1809) remains intact beneath the new row.

---

## Status-Transition List

All five proposals transition `proposed` → `implemented` via direct SQL on the canonical DB (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`, read-write connection). No helper exists — verified: `set_proposal_status` does not exist in `src/lessons_forge.py`.

```sql
UPDATE lesson_proposals
SET status='implemented',
    status_updated_at=<UTC-ISO-8601-timestamp>,
    status_updated_by='ceo'
WHERE id IN (155,156,157,158,159)
```

Verify `cur.rowcount == 5` before commit. On any other rowcount: `conn.rollback()`, HALT, report.

**Mapping:**
| Proposal ID | Entry ID | Status Before | Status After | Route |
|---|---|---|---|---|
| 155 | 147 | proposed | implemented | codify |
| 156 | 148 | proposed | implemented | codify |
| 157 | 149 | proposed | implemented | codify |
| 158 | 150 | proposed | implemented | codify |
| 159 | 151 | proposed | implemented | codify |

---

## No-Renumbering Confirmation

- Existing Rules: 1–53 unchanged. Rule 54 appended after Rule 53.
- Existing Checklist items: 1–31 unchanged. Checklist #32 appended after Checklist #31.
- `### 31.` appears in BOTH the Rules section (line 867, Rule 31 — submodule pointer bump) and the Checklist section (line 1264, Checklist #31 — schema-version bumps). These are in different sections with independent numbering — no conflict.

---

## Output Receipt

**Plan:** 246 — Gate 2 Codification (cycle 2026-07-20)
**Step:** 1 (SA)
**Agent:** SA
**Status:** Complete
**Scope:** `knowledge/development/gate-2-blueprint-2026-07-20.md`

**Deliverables:**
- Blueprint for 5 edits to PLANNER_TEMPLATE.md (v4.75 → v4.76)
- Exact insertion/replacement text with live anchors for each edit
- Dedup checks (all pass — zero hits for new content)
- Per-element verification checklists: (a)–(g) added elements AND (i)–(vi) preserved-doctrine items
- Git pin for cross-step drift guard
- Version bump and changelog row text
- Status-transition SQL and mapping

### Ledger Updates

#### Prompt Feedback

**2026-07-21 — Gate 2 Codification 2026-07-20 (SA Step 1)**

The plan's specification of edit 3 is exceptionally detailed — the seven (a)–(g) elements, the six (i)–(vi) preserved-doctrine items, and the blast-radius constraint to exactly one paragraph provided clear guardrails for the rewrite. The dual citation clarification (entry 94 / DB entry_id 151) in CEO Context prevented a join-failure that the ordinal-vs-DB-id ambiguity would have caused. The lens-count sweep being owned by edit 2 (with one phrase physically in `### Why this process exists`) is a clean ownership assignment. The ADR-004 Decision 6 constraint (no new cross-references from inside the section into other template sections) was easy to follow — Rule 54 and Checklist #32 are outside the Drafting Cycle section and may cite it, not vice versa.
