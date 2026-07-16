# Gate 2 Codification QA — 2026-07-16
**Plan:** 208 — Gate 2 codification, 2026-07-16 cycle
**Agent:** Lessons Forge QA
**Step:** 3 (QA)
**Date:** 2026-07-16
**Domain context:** `agents/FORGE_LESSONS_AGENT.md` read for domain context.

---

## Rule 20 — QA Self-Check Results

This deposit is verification + reporting only. No product-code or template changes were made.

**PASSED — SELF-CHECK PASSED**

---

## Verification Table

All SQL queries ran against: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro"`.
All file reads against: `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`.

| # | Claim | Source | Result |
|---|---|---|---|
| 1 | Rule 52 is live | PLANNER_TEMPLATE.md:1015–1023 | PASS |
| 2 | Checklist #16 refined, not replaced | PLANNER_TEMPLATE.md:1135–1141 | PASS |
| 3 | No duplicate qa_steps rule | grep count = 1 | PASS |
| 4 | Version + changelog | PLANNER_TEMPLATE.md:5–6, :1754 | PASS |
| 5 | No renumbering | grep for `### N.` headings | PASS |
| 6 | Statuses transitioned | DB read-back | PASS |
| 7 | Routes unchanged + 98/121/130 untouched | DB read-back | PASS |
| 8 | Standing plan-204 regression watch | DB + pytest | PASS |
| 9 | Governance root NOT committed | git status | PASS |

---

### 1. Rule 52 is live

**Query:** `grep -n "### 52\." /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Raw output:**
```
1015:### 52. Re-verify inherited claims before dispositions and routing decisions
```

**Query:** `grep -n "Source: proposal 147, lesson 2026-07-07" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Raw output:**
```
1023:Source: proposal 147, lesson 2026-07-07
```

**Rule 39 citation and edit-time vs decision-time distinction — quoted from lines 1019:**
> Rule 39 protects an EDIT: the acting agent re-runs the SA's declared queries before editing against SA-derived claims. Rule 52 protects a DECISION: the Planner (or any agent shaping a plan, routing a proposal, or issuing a disposition) re-verifies inherited claims before acting on them, even when no edit is involved. The two rules are siblings covering different moments in the pipeline — Rule 39 at edit time, Rule 52 at decision time — and neither subsumes the other.

**Full text of Rule 52 (lines 1015–1023):**
```
### 52. Re-verify inherited claims before dispositions and routing decisions

Any claim about the state of the world that is inherited from a generated artifact — classifier output, a Lessons Forge report, a baton or next-session file, a prior plan's findings, a PROJECT_STATUS entry — must be re-verified against ground truth (the filesystem, the live DB, the code, `git log`) before it informs a disposition, a routing decision, or a plan's shape. Generated artifacts describe the world as of their generation time; they are not live sensors. Ground truth is the filesystem and the code.

Rule 39 protects an EDIT: the acting agent re-runs the SA's declared queries before editing against SA-derived claims. Rule 52 protects a DECISION: the Planner (or any agent shaping a plan, routing a proposal, or issuing a disposition) re-verifies inherited claims before acting on them, even when no edit is involved. The two rules are siblings covering different moments in the pipeline — Rule 39 at edit time, Rule 52 at decision time — and neither subsumes the other.

**Why this rule exists:** Three instances of the same failure class surfaced on 2026-07-16, all involving claims inherited from generated artifacts that had gone stale. (a) A three-week-stale FORGE_QA.md "does not exist" flag — originally accurate, wrong for weeks — nearly shaped a Gate 2 authoring decision; no edit was involved, so Rule 39 would never have fired. (b) The plan-205 classifier cited `_parse_session_limit_reset`, a function that does not exist (the real function is `_parse_session_reset`, `bellows/runner.py:36`) — a fabricated identifier inherited from a generated classification, not a filesystem claim. (c) The Planner's own baton refresh carried two already-dead threads (the session-end evidence-file convention, retired v4.72; the Workaround #3 factual tension, corrected v4.73) plus a two-version-stale template number (v4.71 vs. live v4.73), all inherited from the prior baton without re-reading the template — one hour after authoring the verdict that flagged this same class of error. The rule exists because this failure mode does not spare someone who has just named it; it must be mechanical rather than remembered.

Source: proposal 147, lesson 2026-07-07
```

**Result:** PASS

---

### 2. Checklist #16 refined, not replaced

**Original body preserved (line 1137):** The `### 16. Copy strict convention strings from known-good artifacts` heading and original paragraph about strict Bellows convention strings are intact at lines 1135–1137.

**Degenerate-exemplar refinement added (line 1139):** New paragraph begins "Known-good is necessary but NOT sufficient" — verified present.

**Source line extended (line 1141):**
**Query:** `grep -n "Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07; proposal 148, lesson 2026-07-07" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Raw output:**
```
1141:Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07; proposal 148, lesson 2026-07-07
```

All three proposals (114, 126, 148) named. Original guidance survives. Refinement added, not replaced.

**Result:** PASS

---

### 3. No duplicate qa_steps rule

**Query:** `grep -c "listing the step numbers that are QA-gated" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Raw output:**
```
1
```

Count is 1, not 2. The rejected clause from proposal 148 was NOT added. The existing semantics at `:407` remain the sole instance.

**Result:** PASS

---

### 4. Version + changelog

**Query:** `sed -n '5,6p' /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
**Raw output:**
```
**Version:** 4.74
**Last Updated:** 2026-07-16 (v4.74)
```

**Changelog — new row at TOP (line 1754):**
**Query:** `grep -n "^| 2026-07" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md | head -5`
**Raw output:**
```
1754:| 2026-07-16 | v4.74: Gate 2 ratification, 2026-07-16 cycle. New Rule 52 (re-verify inherited claims before dispositions/routing, sibling to Rule 39's edit-time protection; from proposal 147). Checklist #16 refined with degenerate-exemplar discipline (from proposal 148's residue; its qa_steps semantics clause was rejected as already-covered at `:407`, with only the known-good-but-degenerate gap codified). Proposal 146 routed to `reference` (no edit). |
1755:| 2026-07-09 | v4.73: corrected Workaround #3 factual tension ...
1756:| 2026-07-09 | v4.72: retired the session-end `pytest_session_end.txt` evidence-file convention ...
1757:| 2026-07-07 | Gate 2 ratification, 2026-07-06 cycle (v4.71): ...
```

Exactly ONE new row at the top. Pre-existing v4.73 (line 1755) and v4.72 (line 1756) rows intact below.

**Result:** PASS

---

### 5. No renumbering

**Highest Orchestration rule:**
**Query:** `grep -n "^### [0-9]*\." /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md | grep -E "### (5[0-9]|4[5-9])\."` (tail)
**Raw output:**
```
968:### 45. SA blueprints must verify downstream consumers when adding to recognized-sets
974:### 46. Lessons Forge Gate 1 — reject daemon-bug workaround proposals
980:### 47. Derive Lessons Forge classification work list from the stale-aware DB helper
986:### 48. Gate-enforced QA actions require a mandatory top-of-step callout
992:### 49. Delegated verdict authority on clean Bellows runs (CEO policy 2026-07-02)
998:### 50. Derive step scope from SA enumeration, not hand-typed lists
1009:### 51. Corrections at verdict time go into plan text, not verdict disposition prose
1015:### 52. Re-verify inherited claims before dispositions and routing decisions
```

Rules 45–51 retain their numbers. 52 is the only new addition. Highest rule is now 52.

**Highest checklist item:**
**Query:** `grep -n "^### [0-9]*\." /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` filtered for checklist section (lines 1091+)
**Raw output (checklist tail):**
```
1191:### 25. Regression gates identify time-dependent inputs
1197:### 26. Convention-change plans grep for all occurrences
1203:### 27. Step composition passes the Position A check
1209:### 28. QA steps for DB-out-of-git projects carry an evidence-source contract
```

Highest checklist item is 28 — unchanged.

**Result:** PASS

---

### 6. Statuses transitioned

**Per-proposal read-back:**
**Query:** `SELECT id, status, route FROM lesson_proposals WHERE id IN (146, 147, 148) ORDER BY id;`
**Raw output:**
```
146|reference|reference
147|implemented|codify
148|implemented|codify
```

147=implemented, 148=implemented, 146=reference. All correct.

**Distribution:**
**Query:** `SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY COUNT(*) DESC;`
**Raw output:**
```
implemented|99
superseded|28
rejected|15
reference|3
stale|3
```

`proposed` is absent (= 0). Every proposal from the 2026-07-16 cycle is dispositioned.

**Expected vs actual:** implemented 99 ✓, superseded 28 ✓, rejected 15 ✓, stale 3 ✓, reference 3 ✓, proposed 0 ✓.

**Result:** PASS

---

### 7. Routes unchanged + 98/121/130 untouched

**Routes (from check 6 read-back):** 146=reference, 147=codify, 148=codify — unchanged from Gate 1 settings.

**98/121/130:**
**Query:** `SELECT id, status FROM lesson_proposals WHERE id IN (98, 121, 130) ORDER BY id;`
**Raw output:**
```
98|stale
121|stale
130|stale
```

All three remain `stale`. CEO decision honored.

**Result:** PASS

---

### 8. Standing plan-204 regression watch

**Proposal 145:**
**Query:** `SELECT id, status FROM lesson_proposals WHERE id = 145;`
**Raw output:**
```
145|implemented
```
Still `implemented`. ✓

**get_unclassified_entries():**
**Query:** `python3 -c "import sys; sys.path.insert(0, 'src'); from lessons_forge import get_unclassified_entries; import sqlite3; conn = sqlite3.connect('lessons-forge.db'); print(get_unclassified_entries(conn))"`
**Raw output:**
```
[]
```
Empty list. ✓

**Test suite:**
**Query:** `python3 -m pytest src/ -v`
**Raw output (summary):**
```
55 passed in 0.10s
```
All 55 tests passed. No regressions. ✓

**Result:** PASS

---

### 9. Governance root NOT committed

**Query:** `git status --short PLANNER_TEMPLATE.md` (from `/Users/marklehn/Developer/GitHub`)
**Raw output:**
```
 M PLANNER_TEMPLATE.md
```

Modified but uncommitted. Planner commits cross-repo at session wrap (plan-134 precedent).

**Result:** PASS

---

### Ledger Updates

#### Project Status

Gate 2 of the 2026-07-16 cycle is complete: PLANNER_TEMPLATE v4.73→v4.74. Rule 52 (re-verify inherited claims before dispositions and routing decisions) codified from proposal 147 as a sibling to Rule 39, covering decision-time where Rule 39 covers edit-time. Checklist #16 refined with the degenerate-exemplar discipline from proposal 148's residue — its qa_steps semantics clause was rejected as already-covered (`:407`), with only the known-good-but-degenerate gap codified. Proposal 146 dispositioned to `reference` (no edit; fix already shipped). All three proposals (146/147/148) now carry terminal statuses; `proposed` count is 0 — the 2026-07-16 cycle is fully closed.

#### Prompt Feedback

| File | Agent | Feedback |
|---|---|---|
| executable-208.md | Lessons Forge QA | The plan's QA step is well-structured: 9 verification claims with explicit queries and expected values make the checks mechanical. The Rule 52 self-discipline requirement ("this is the Gate that codified it — do not be its first violation") is a strong forcing function for the QA agent to grep-before-asserting. The evidence-source rule (canonical DB path + read-only mode) prevents accidental writes during QA. |

---

## Output Receipt

**Status:** Complete
**Agent:** Lessons Forge QA
**Plan:** 208 — Gate 2 codification, 2026-07-16 cycle
**Step:** 3

### Files Created or Modified

| File | Action | Notes |
|---|---|---|
| `knowledge/qa/gate-2-codification-qa-2026-07-16.md` | Created | This deposit. |

### Flags

None. All 9 verification checks passed. No blockers found.
