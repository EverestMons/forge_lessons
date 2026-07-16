# Gate 2 Codification — Dev Log (2026-07-16)
**Plan:** 208 — Gate 2 codification, 2026-07-16 cycle
**Agent:** Forge Developer
**Step:** 1 (DEV)
**Date:** 2026-07-16

---

## Pre-Edit Verification Results

All 4 claims verified against live PLANNER_TEMPLATE.md before any edits.

### 1. Live version is 4.73
**Query:** `sed -n '5p' /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Expected:** `**Version:** 4.73`
**Actual:** `**Version:** 4.73`
**Result:** PASS

### 2. Rule 51 source footer exists exactly once
**Query:** `grep -n "^Source: proposal 138, lesson 2026-07-06" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Expected:** exactly ONE hit (~line 1013)
**Actual:** `1013:Source: proposal 138, lesson 2026-07-06`
**Result:** PASS

### 3. Checklist #16 Source line exists verbatim and exactly once
**Query:** `grep -c "^Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Expected:** `1`
**Actual:** `1`
**Result:** PASS

### 4. qa_steps step-number semantics already covered (dedup basis for rejecting 148's first clause)
**Query:** `grep -c "listing the step numbers that are QA-gated" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Expected:** `1`
**Actual:** `1`
**Result:** PASS — the semantics are already covered at `:407`. No duplicate added.

---

## Edit A — New Rule 52 (proposal 147)

**Inserted after:** Rule 51's `Source: proposal 138, lesson 2026-07-06` footer (line 1013)
**Inserted before:** the `---` / `## Lifecycle DB Read Protocol` section heading
**Lines in edited file:** 1015–1023

### Full text of Rule 52 as written:

```
### 52. Re-verify inherited claims before dispositions and routing decisions

Any claim about the state of the world that is inherited from a generated artifact — classifier output, a Lessons Forge report, a baton or next-session file, a prior plan's findings, a PROJECT_STATUS entry — must be re-verified against ground truth (the filesystem, the live DB, the code, `git log`) before it informs a disposition, a routing decision, or a plan's shape. Generated artifacts describe the world as of their generation time; they are not live sensors. Ground truth is the filesystem and the code.

Rule 39 protects an EDIT: the acting agent re-runs the SA's declared queries before editing against SA-derived claims. Rule 52 protects a DECISION: the Planner (or any agent shaping a plan, routing a proposal, or issuing a disposition) re-verifies inherited claims before acting on them, even when no edit is involved. The two rules are siblings covering different moments in the pipeline — Rule 39 at edit time, Rule 52 at decision time — and neither subsumes the other.

**Why this rule exists:** Three instances of the same failure class surfaced on 2026-07-16, all involving claims inherited from generated artifacts that had gone stale. (a) A three-week-stale FORGE_QA.md "does not exist" flag — originally accurate, wrong for weeks — nearly shaped a Gate 2 authoring decision; no edit was involved, so Rule 39 would never have fired. (b) The plan-205 classifier cited `_parse_session_limit_reset`, a function that does not exist (the real function is `_parse_session_reset`, `bellows/runner.py:36`) — a fabricated identifier inherited from a generated classification, not a filesystem claim. (c) The Planner's own baton refresh carried two already-dead threads (the session-end evidence-file convention, retired v4.72; the Workaround #3 factual tension, corrected v4.73) plus a two-version-stale template number (v4.71 vs. live v4.73), all inherited from the prior baton without re-reading the template — one hour after authoring the verdict that flagged this same class of error. The rule exists because this failure mode does not spare someone who has just named it; it must be mechanical rather than remembered.

Source: proposal 147, lesson 2026-07-07
```

---

## Edit B — Checklist #16 Refinement (proposal 148, residue only)

**Location:** `### 16. Copy strict convention strings from known-good artifacts` (line 1135 in edited file)
**Change type:** in-place append — original body preserved, new paragraph added after it

**Added paragraph (the degenerate-exemplar discipline):**

> Known-good is necessary but NOT sufficient: the exemplar must also be one where the convention's semantics are distinguishable. A degenerate exemplar — one where two different readings of a convention produce the same surface value — cannot teach which reading is correct. `qa_steps: 1` was copied from plan 130, a genuinely known-good plan whose only step was its QA step, so the "count of QA steps" and "step numbers that are QA steps" readings coincide and the example cannot teach which one is meant. Copied into plan 133, it gated the DEV step as QA (Rule 20 banner demanded from a DEV deposit) and let the real QA step run with Rule 20/22 gates skipped. When an exemplar is degenerate for the convention being copied, find a non-degenerate one (where the two readings would produce different values) or read the rule itself.

**Source line extended to:** `Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07; proposal 148, lesson 2026-07-07`

**Not added:** No duplicate qa_steps semantics rule. The semantics are already covered at `:407` ("listing the step numbers that are QA-gated, as a comma-separated list of integers"). Post-edit grep confirms the count remains 1.

---

## Edit C — Version + Changelog

**Version:** `**Version:** 4.74` (line 5)
**Last Updated:** `**Last Updated:** 2026-07-16 (v4.74)` (line 6)
**Changelog:** One new row added at the TOP of the Lessons Learned table (newest-first). Pre-existing v4.73 and v4.72 rows intact below it.

---

## Occurrence-Grep Discipline

These edits introduce no new convention string and rename nothing. Rule 52 is a new rule (no prior string to grep). Checklist #16's refinement adds body prose only — no heading change, no convention-string change. Confirmed.

---

### Ledger Updates

#### Prompt Feedback

| File | Agent | Feedback |
|---|---|---|
| PLANNER_TEMPLATE.md | Forge Developer | The plan's pre-edit verification section is exemplary — having 4 explicit claim/query/expected triples made the verify-before-edit discipline trivially mechanical. The plan also dogfoods its own Rule 52 by requiring re-verification of all Planner-claimed line numbers. |

---

## Output Receipt

**Status:** Complete
**Agent:** Forge Developer
**Plan:** 208 — Gate 2 codification, 2026-07-16 cycle
**Step:** 1

### Files Created or Modified

| File | Action | Notes |
|---|---|---|
| `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` | Modified | Edit A: new Rule 52 (lines 1015–1023). Edit B: Checklist #16 degenerate-exemplar refinement (lines 1135–1141). Edit C: version 4.73→4.74, changelog row added. **NOT COMMITTED** — Planner commits cross-repo at session wrap (plan-134 precedent). |
| `knowledge/development/gate-2-codification-2026-07-16.md` | Created | This deposit. |

### Flags

None. All 4 pre-edit verifications passed. No mismatches detected.
