# Gate 2 Codification — QA Report (2026-07-20 Cycle)

**Plan:** 246 — Gate 2 Codification (cycle 2026-07-20)
**Step:** 3 (QA)
**Agent:** QA
**Date:** 2026-07-21

---

## Verification Table

### Row 0 — Template hash match (Step 2 → Step 3 integrity)

- Step 2 deposited hash: `a1c3b12e35ba8993fb536ebef3b374766a16133de5031b0bd6247ffed1955697`
- QA recomputed: `a1c3b12e35ba8993fb536ebef3b374766a16133de5031b0bd6247ffed1955697`
- **PASS** — byte-identical.

### Row 1 — Version is 4.76 on both header lines; no unresolved tokens

- Line 5: `**Version:** 4.76`
- Line 6: `**Last Updated:** 2026-07-21 (v4.76)`
- `grep -c '<EXECUTION-DATE>' PLANNER_TEMPLATE.md` → `0` (exit code 1 = no matches — EXPECTED/PASSING)
- **PASS**

### Row 2 — Walk-the-list stop condition

**Quoted paragraph (line 341):**

> Each pass: severity-rank findings, verify claims against code and data mid-analysis (grep, not assume), report what held up alongside what failed. Fold **all** accepted findings into the next draft after each pass. Walk the full lens list in order — one pass per lens per walk. A lens is re-run only on a **subsequent walk** of the entire list, never immediately on its own fold; the structural reason is that a defect introduced by a fold is usually caught by a *different* lens reading different evidence, not by re-running the lens that produced it. The cycle is done when a full walk returns **zero or only-minor findings** — this IS the diminishing-returns signal: a full walk that finds nothing new. A dry pass is an honestly reportable success, not underperformance — manufacturing minor findings to appear diligent is the same Goodhart failure as forcing a predicted number. The last event before deposit must be a **lens pass, never a fold** (a fold produces a draft no pass has examined): if the walk's final lens pass folded anything, a brief confirming pass over the folded draft supplies the closing lens pass (expected dry; any new material finding re-opens the walk; new minor findings at the closing check are recorded in the deposit, not folded — a minor-only closing pass still satisfies the deposit condition; this closing check is exempt from the walk-rotation rule — it is a deposit-condition check, not a lens re-run). Cross-lens contradictions are the closing lens's job (ACID runs last — see lens 5). Fold-and-deposit **exactly once** (deposit-once discipline).

#### Added elements (a)–(g)

| Element | Requirement | Present text | Verdict |
|---|---|---|---|
| (a) | One pass per lens; walk the whole lens list in order, folding after each pass | "Walk the full lens list in order — one pass per lens per walk" + "Fold **all** accepted findings into the next draft after each pass" | PASS |
| (b) | Re-run only on a subsequent walk, never immediately on own fold | "A lens is re-run only on a **subsequent walk** of the entire list, never immediately on its own fold" | PASS |
| (c) | Done when a full walk returns zero or only-minor findings | "The cycle is done when a full walk returns **zero or only-minor findings**" | PASS |
| (d) | Last event = lens pass not fold; closing mechanism stated | "The last event before deposit must be a **lens pass, never a fold**" + closing mechanism paragraph (confirming pass, expected dry, material re-opens, minor recorded not folded, exempt from rotation) | PASS |
| (e) | Honest-zero guard | "A dry pass is an honestly reportable success, not underperformance — manufacturing minor findings to appear diligent is the same Goodhart failure as forcing a predicted number" | PASS |
| (f) | Diminishing-returns retained as outer framing | "this IS the diminishing-returns signal: a full walk that finds nothing new" | PASS |
| (g) | Cross-lens contradictions = closing lens's job | "Cross-lens contradictions are the closing lens's job (ACID runs last — see lens 5)" | PASS |

#### Preserved-doctrine items (i)–(vi)

| Item | Requirement | Present text | Verdict |
|---|---|---|---|
| (i) | Severity-rank findings each pass | "severity-rank findings" | PASS |
| (ii) | Verify claims against code and data mid-analysis | "verify claims against code and data mid-analysis (grep, not assume)" | PASS |
| (iii) | Report what held up alongside what failed | "report what held up alongside what failed" | PASS |
| (iv) | Fold all accepted findings | "Fold **all** accepted findings into the next draft after each pass" | PASS |
| (v) | Off-queue intro intact and NOT duplicated in rewrite | Line 333: "Draft the plan **off-queue** — outside the watched `decisions/` directory, because deposit equals dispatch." — present ABOVE the paragraph; `grep -nF 'off-queue'` returns ONLY line 333, NOT duplicated inside the rewritten paragraph | PASS |
| (vi) | Fold-and-deposit exactly once | "Fold-and-deposit **exactly once** (deposit-once discipline)" | PASS |

**Superseded-model absence check:** The rewritten paragraph contains "never immediately on its own fold" — the walk-the-list form. No instruction to re-run the SAME lens immediately on its own fold before advancing. **PASS.**

**Row 2 overall: PASS**

### Row 3 — ACID is the fifth named lens, listed last; lens-count sweep

- Line 339: `5. **ACID (atomicity, consistency, isolation, durability)** — examine the plan's accepted requirements **as a system**...`
- ACID is lens 5, listed last. **PASS.**
- Systems-reasoning note extended at end of line 338: "pass 5 requires systems reasoning over the plan's own requirements" — **PASS.**
- Four existing lens descriptions (lines 335–338) — descriptions of lenses 1–4 unchanged apart from the note extension at the tail of lens 4's line.

**Lens-count sweep (all `grep -cF`, scoped to `## The Drafting Cycle` section):**

| Phrase | Count | Expected | Verdict |
|---|---|---|---|
| `four-pass cycle` | 0 | 0 | PASS |
| `four **named lenses**` | 0 | 0 | PASS |
| `four heavy passes` | 0 | 0 | PASS |
| `four-lens cycle` | 1 | 1 (historical: "Plan 224 was the first to run the full four-lens cycle") | PASS (preserved) |

**Row 3 overall: PASS**

### Row 4 — Diagnostic-shaped escalation triggers

Line 327: "The plan is a **diagnostic** whose findings will be authored from without re-verification, whose questions depend on data whose availability is unconfirmed, that scopes a multi-plan arc, or that touches a leak, money, or governance surface"

| Trigger | Present | Verdict |
|---|---|---|
| Authored-from without re-verification | ✓ | PASS |
| Data whose availability is unconfirmed | ✓ | PASS |
| Multi-plan arc | ✓ | PASS |
| Leak, money, or governance surface | ✓ | PASS |

Lines 329: Weak-spots-at-the-questions guidance present ("weak spots aimed at the questions themselves" + diag-229 evidence cite). **PASS.**

Lines 325–326: Executable-shaped triggers unchanged (floor pass surfaces entanglement; inherently high-stakes). **PASS.**

**Row 4 overall: PASS**

### Row 5 — Rule 54 and Checklist #32

**Section-scoped counts:**

| Section | Item | Count | Expected | Verdict |
|---|---|---|---|---|
| Orchestration Plan Rules | `### 54.` | 1 | 1 | PASS |
| Orchestration Plan Rules | `### 55.` | 0 | 0 | PASS |
| Plan Authoring Checklist | `### 32.` | 1 | 1 | PASS |
| Plan Authoring Checklist | `### 33.` | 0 | 0 | PASS |

**Rule 54 content:** Structural-home rule — "Every requirement needs a structural home — a numbered row, a named test, or a gate condition." References Rule 51: "Rule 51 — corrections go into plan text, not verdict prose; Rule 54 says what form those corrections take." **PASS.**

**Checklist #32 content:** Observed-delta rule — "Verification of any wired call must observe a behaviour change through the real entry point." Cites Workaround #15: "This is the general form of Workaround #15 (post-activation live canary for daemon write paths); Workaround #15 is the specific instance for silent/best-effort daemon channels." **PASS.**

**Predecessor headings unchanged:**
- Rule 53: `### 53. Region-scoped metrics must be computed with scope applied end to end` (line 1060) — unchanged. **PASS.**
- Checklist #31: `### 31. Schema-version bumps enumerate and classify all version-pinned assertions` (line 1274) — unchanged. **PASS.**

**Row 5 overall: PASS**

### Row 6 — Exactly one new changelog row

- Line 1825: New row at top of changelog table, naming all five edits (diagnostic escalation triggers, ACID fifth lens, walk-the-list stop condition, Rule 54, Checklist #32), five proposals (155–159) → implemented, and entry-94 supersession ("entry 94/DB 151 within-lens iterate-to-dry model REPLACED by walk-the-list form, evidence entry 99/C1"). **PASS.**
- Line 1826: v4.75 row intact beneath. **PASS.**
- Exactly one new row (no other additions between the header and the v4.75 row). **PASS.**

**Row 6 overall: PASS**

### Row 7 — Canonical statuses

**Per-id facts:**

```
155|implemented|codify
156|implemented|codify
157|implemented|codify
158|implemented|codify
159|implemented|codify
```

All five `implemented`, routes still `codify`. **PASS.**

**Path determination from c-evidence (Step 2 deposit lines 70–74):**

```
155|proposed|codify
156|proposed|codify
157|proposed|codify
158|proposed|codify
159|proposed|codify
```

Pre-write shows `proposed|codify` → **normal-write path** confirmed.

**Distribution delta:**

| Status | Pre-write | Post-write | Delta |
|---|---|---|---|
| implemented | 105 | 110 | +5 |
| proposed | 5 | 0 | −5 |
| reference | 3 | 3 | 0 |
| rejected | 15 | 15 | 0 |
| stale | 3 | 3 | 0 |
| superseded | 28 | 28 | 0 |

Delta: proposed −5, implemented +5. All others unchanged. **PASS.**

**Hardening clause (α) — byte-compare raw CLI output:**

Step 2 deposited:
```
155|implemented|2026-07-21T21:12:52.935910+00:00|ceo
156|implemented|2026-07-21T21:12:52.935910+00:00|ceo
157|implemented|2026-07-21T21:12:52.935910+00:00|ceo
158|implemented|2026-07-21T21:12:52.935910+00:00|ceo
159|implemented|2026-07-21T21:12:52.935910+00:00|ceo
```

QA re-run (identical query):
```
155|implemented|2026-07-21T21:12:52.935910+00:00|ceo
156|implemented|2026-07-21T21:12:52.935910+00:00|ceo
157|implemented|2026-07-21T21:12:52.935910+00:00|ceo
158|implemented|2026-07-21T21:12:52.935910+00:00|ceo
159|implemented|2026-07-21T21:12:52.935910+00:00|ceo
```

**Byte-identical. PASS.**

**Timestamp validation:** `2026-07-21T21:12:52.935910+00:00` — real ISO-8601 UTC timestamp, not placeholder/empty. **PASS.**

**Hardening clause (β):** Current distribution matches Step 2 post-write distribution exactly (no extraneous rows changed between Step 2 and Step 3). No reconciliation needed. **PASS.**

**Row 7 overall: PASS**

### Row 8 — Template modified but uncommitted

- `git -C /Users/marklehn/Developer/GitHub status --short -- PLANNER_TEMPLATE.md` → ` M PLANNER_TEMPLATE.md`
- Modified but uncommitted — positive signal. **PASS.**

**Row 8 overall: PASS**

---

## Rule 20 — QA Self-Check Results

All nine verification rows (0–8) passed. No failures detected.

**PASSED — SELF-CHECK PASSED**

---

## Output Receipt

**Plan:** 246 — Gate 2 Codification (cycle 2026-07-20)
**Step:** 3 (QA)
**Agent:** QA
**Status:** Complete
**Scope:** `knowledge/qa/gate-2-codification-qa-2026-07-20.md`

**Deliverables:**
- All 9 verification rows (0–8) passed
- Template hash match confirmed (Step 2 → Step 3 integrity chain intact)
- Version 4.76 on both header lines; no unresolved `<EXECUTION-DATE>` tokens
- Walk-the-list stop condition verified: all 7 added elements (a)–(g) present, all 6 preserved-doctrine items (i)–(vi) verified, superseded within-lens model absent
- ACID fifth lens present and listed last; lens-count sweep clean (three phrases updated, historical reference preserved)
- Diagnostic escalation triggers present (all four + guidance); executable-shaped unchanged
- Rule 54 (structural-home, sibling to Rule 51) and Checklist #32 (observed-delta, cites Workaround #15) present; no renumbering
- Changelog row names all five edits, five→implemented, entry-94 supersession
- Proposals 155–159 all `implemented` with route `codify`; distribution delta proposed −5, implemented +5; byte-identical raw CLI output vs Step 2 deposit
- Template modified but uncommitted (` M`)

### Ledger Updates

#### Project Status

Gate 2 2026-07-20 complete: PLANNER_TEMPLATE v4.76 — walk-the-list stop condition (entry-94 within-lens iterate-to-dry model superseded, evidence entry 99/C1), ACID fifth lens, diagnostic escalation triggers, Rule 54 structural-home, Checklist #32 observed-delta; proposals 155–159 implemented; `proposed` at 0. WRAP REMINDER: before committing the template cross-repo, the Planner re-matches its shasum against the Step-2 dev-log hash — see the plan's wrap-commit protocol. Entry 99's future classification routes `reference` — its substance shipped here.

#### Prompt Feedback

**2026-07-21 — Gate 2 Codification 2026-07-20 (QA Step 3)**

The Step 2 deposit was comprehensive and well-structured — the raw CLI output, post-edit hash, and c-evidence query were all present and correctly formatted for byte-comparison. The section-scoped grep guidance for `### N.` numbering (which repeats across Rules and Checklist sections) was essential — an unscoped grep for `### 32.` would have returned 2 hits and false-failed a correct apply. The fixed-string (`grep -cF`) requirement for the lens-count sweep was equally critical — the bold markers `**` are regex quantifiers that would produce vacuous matches on the exact phrases the check exists to catch.
