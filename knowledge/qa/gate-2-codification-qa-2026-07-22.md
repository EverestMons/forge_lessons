# Gate 2 Codification — QA Report (cycle 2026-07-22, v4.77 → v4.78)

**Plan:** 259 | **Step:** 3 (QA) | **Date:** 2026-07-23

---

## Rule 20 — QA Self-Check Results

**PASSED — SELF-CHECK PASSED**

---

## Verification Table

### Check 0 — Template Integrity

`shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`:
```
8b6ba2ed282007636435683b29faac1bb33199cd8ac60ee57107a0a090af8970  /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md
```

Step-2 dev-log hash:
```
8b6ba2ed282007636435683b29faac1bb33199cd8ac60ee57107a0a090af8970  /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md
```

**Byte-match: PASS**

---

### Check 1 — Version 4.78

Line 5: `**Version:** 4.78` (no `v` prefix) ✓
Line 6: `**Last Updated:** 2026-07-22 (v4.78)` ✓

**PASS**

---

### Check 2 — E1-E5 present in `## The Drafting Cycle`

**E1 (line 349):** "Any executable check, computed gate, or repeatable procedure embedded in a plan is validated ONLY by running it against real corpus data before deposit — the five adversarial lenses read the description, not the output, and cannot validate an executable check. A text-parsing check prefers extraction-free comparison (canonicalize both sides, then longest-common-substring) over parse-then-match; the parse step is where false FAILs are born. Record the measured range in the plan, not just the threshold. A lens pass that HARDENS such a check rather than rewriting it is a signal to execute it, not evidence it is now sound — a partially-fixed check is the most dangerous state it can occupy, because it buys confidence without buying coverage. For any plan that hands an agent a repeatable procedure over a set of items, run that procedure on the hardest one or two real items before deposit — not to verify the claims, but to confirm the method produces an answer at all; "the instructions are correct" and "the instructions work" are separate questions, and the lenses answer only the first."
- Names execute-against-real-data for both checks AND procedures ✓

**E2 (line 351):** "After folding a fix, re-run the lens that found the ORIGINAL defect on the fix itself — treat the fix as a new draft that no pass has examined, not as a closed finding. Where the fix contains an executable step (a grep, a guard, a command), run it against real data before accepting it (per the execute-against-real-data rule above). The sharpest form: an accommodation written for one edge case often produces the defect ON that exact edge case. This rule is the lens-side companion to Plan Authoring Checklist #26 (the artifact-side sibling sweep); cross-reference, do not duplicate."
- Cross-references Checklist #26 without editing it ✓ (Checklist #26 at line 1302 unchanged)

**E3 (line 353):** "Before splitting or extracting shared content, diff the candidate regions and move only byte-identical clauses; unifying things that differ is the false-sharing bug, duplicating things that are identical is the drift bug. After extraction, walk the seam as its own surface — the ACID and destruction lenses have the most purchase there, because seam defects are drift and watering-down, not correctness of any single part. State the four-part extraction contract: what moves, what stays, how the moved content is retrieved, and what the retrieval promises (over-return, under-return, an absent source); each unstated part is a separate defect."

**E4 (line 355):** "Before deposit, sketch one real block of the finished deliverable — the actual rows, cells, or sections a single item produces — and confirm the mandated format can hold everything the plan requires per item. The five adversarial lenses read the procedure; the shape of the product is orthogonal to all of them and invisible until you draw it. Where per-item output is rich (quotes, paired values, multi-part findings), prefer a block-per-item structure with a compact summary index over a table; a table forces truncation of exactly the evidence that motivated the plan."

**E5 (line 357):** "**Mechanical conformance pass (distinct from the adversarial lenses above).** Once the plan's shape is stable and before the closing walk, run a non-adversarial mechanical conformance pass: execute `plan_lint`, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope (the two sections number independently — never grep `### N.` unscoped). This pass checks the plan against the codified authoring rules, not against reality; the adversarial lenses do the latter. Most items are N/A for a given plan; the value is the few that are not and that no adversarial lens is looking for."
- E5 is explicitly a MECHANICAL pass, "distinct from the adversarial lenses above", "non-adversarial" ✓
- NOT a lens ✓

**Lens list (lines 335-345):** runs 1-5 (Weak spots, Destruction, Vulnerabilities, Integration-vs-record, ACID) — unchanged ✓
**Line 333:** "Cycle through adversarial analysis under five **named lenses**" — FIVE ✓
**Line 361:** "without imposing five heavy passes on a one-liner" — FIVE ✓

**PASS**

---

### Check 3 — E6 — New `## Halted-Plan Triage` section

Section head at line 365: `## Halted-Plan Triage`

**Half 1 — Three-rung successor ladder:**
"When triaging a halted plan to determine whether its work shipped under a different plan, search for a successor via a three-rung ladder, tried in order:
1. **Slug-reference grep** — `grep -rl '<qualified-slug>' <repo>/knowledge/decisions/Done/`...
2. **Term-search** — search `Done/` for the halted plan's technical identifiers...
3. **Date-adjacency** — the halted plan's filename date → same/adjacent-date entries...
Stop at the first rung that answers; state which rung produced the result. Each rung's result is bounded..."

**Half 2 — Artifact-type triage:**
"**Classify the artifact type before choosing the disposition test.** For an executable, ask whether the CODE shipped... For a diagnostic, ask whether the QUESTIONS were answered — look in `Done/diagnostic-*`, in `knowledge/research/` deposits, and for the same questions restated in a successor plan's Context. Source code is not evidence either way for a diagnostic..."

Both halves present ✓

**PASS**

---

### Check 4 — E7, E8, E11

**E7 (line 943):** "A directory-declared deposit is neither present nor missing — it is a THIRD outcome, `unmeasurable`..." — present in Rule 37 region, after the existing Rule 37 content ✓

**E8 (line 937):** "**Completeness sweeps.** For a completeness sweep, use `/usr/bin/grep` explicitly and state which binary — the shell's default `grep` is often a wrapper (e.g., `ugrep --ignore-files`) that honours `.gitignore` and silently under-reports. Bound the sweep with `--exclude-dir=.git,.bellows-worktrees,logs` and `--include` globs..." — present in Rule 36, AFTER existing Rule 36 content ("Common failure mode: grepping for warning text...") ✓

**E11 (line 1513):** `### Dispatch Path Rules` — "Split path instructions in Bellows-dispatched plan steps by operation ROLE, never by a blanket "run from X." READS of shared state... take an ABSOLUTE path... WRITES of the step's own deposits take a path RELATIVE to the agent's working tree... This rule is about operation type, not dispatch topology..." ✓

**PASS**

---

### Check 5 — E9=#57, E10=#58 in Orchestration Plan Rules

**E9 at line 1118:** `### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics` — in `## Orchestration Plan Rules` section (between Rule 56 at line 1112 and `## Lifecycle DB Read Protocol`) ✓
**E10 at line 1124:** `### 58. Pre-stated conclusions require verification anchors and equal evidence burden` — in same section ✓
**Prior highest was #56** (line 1112: "### 56. Resume machinery is justified only when the interrupted work is not reproducible") — nothing renumbered ✓

**PASS**

---

### Check 6 — Historical changelog counts intact

**Line 1893:** "...ACID as fifth named lens..." — INTACT ✓
**Line 1894:** "...four named lenses..." — INTACT ✓

This plan swept no counts.

**PASS**

---

### Check 7 — New changelog row

Line 1891: `| 2026-07-22 | v4.78: Gate 2 codification, 2026-07-22 cycle. Fourteen proposals (172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 184, 185, 186) via eleven edits, two merges (E1 = 172+173+179 execute-before-deposit; E6 = 174+175 halted-plan triage). E1: executable checks/procedures validated by running against real data... E5: mechanical conformance pass distinct from the five adversarial lenses — the lens count deliberately stays five (185). E6: new `## Halted-Plan Triage` section... Fourteen proposals → implemented. |`

Names: v4.78 ✓, fourteen proposals ✓, eleven edits ✓, two merges (E1, E6) ✓, new section ✓, lens count stays five ✓

**PASS**

---

### Check 8 — Fourteen proposals at `implemented`

QA re-run (DB: lessons-forge.db):
```
172|implemented|2026-07-23T16:53:21Z|ceo
173|implemented|2026-07-23T16:53:21Z|ceo
174|implemented|2026-07-23T16:53:21Z|ceo
175|implemented|2026-07-23T16:53:21Z|ceo
176|implemented|2026-07-23T16:53:21Z|ceo
177|implemented|2026-07-23T16:53:21Z|ceo
178|implemented|2026-07-23T16:53:21Z|ceo
179|implemented|2026-07-23T16:53:21Z|ceo
180|implemented|2026-07-23T16:53:21Z|ceo
181|implemented|2026-07-23T16:53:21Z|ceo
182|implemented|2026-07-23T16:53:21Z|ceo
184|implemented|2026-07-23T16:53:21Z|ceo
185|implemented|2026-07-23T16:53:21Z|ceo
186|implemented|2026-07-23T16:53:21Z|ceo
```

Step-2 dev-log block:
```
172|implemented|2026-07-23T16:53:21Z|ceo
173|implemented|2026-07-23T16:53:21Z|ceo
174|implemented|2026-07-23T16:53:21Z|ceo
175|implemented|2026-07-23T16:53:21Z|ceo
176|implemented|2026-07-23T16:53:21Z|ceo
177|implemented|2026-07-23T16:53:21Z|ceo
178|implemented|2026-07-23T16:53:21Z|ceo
179|implemented|2026-07-23T16:53:21Z|ceo
180|implemented|2026-07-23T16:53:21Z|ceo
181|implemented|2026-07-23T16:53:21Z|ceo
182|implemented|2026-07-23T16:53:21Z|ceo
184|implemented|2026-07-23T16:53:21Z|ceo
185|implemented|2026-07-23T16:53:21Z|ceo
186|implemented|2026-07-23T16:53:21Z|ceo
```

Byte-identical (all fourteen = `implemented`, `status_updated_by='ceo'`) ✓

**PASS**

---

### Check 9 — Proposal 183 UNTOUCHED

QA re-run (DB: lessons-forge.db):
```
183|reference|2026-07-23T16:08:21Z|ceo
```

Step-2 dev-log:
```
183|reference|2026-07-23T16:08:21Z|ceo
```

183 is at `status='reference'` — NOT `implemented`. Timestamp `2026-07-23T16:08:21Z` predates this plan's transition (`2026-07-23T16:53:21Z`). UNTOUCHED ✓

**PASS**

---

### Check 10 — Corpus totals

```
sqlite3 lessons-forge.db "SELECT COUNT(*) FROM lesson_entries"
178

sqlite3 lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals"
186

sqlite3 lessons-forge.db "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status"
implemented|133
reference|7
rejected|15
stale|3
superseded|28
```

DB: lessons-forge.db. Entries: 178, Proposals: 186. **`proposed` is 0** (absent from distribution = zero rows). ✓

**PASS**

---

### Check 11 — No `src/` change, no schema drift

`git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/` → **empty** ✓

**PASS**

---

## Verification Summary

| # | Check | Result |
|---|-------|--------|
| 0 | Template integrity (shasum match) | PASS |
| 1 | Version 4.78 on :5/:6 | PASS |
| 2 | E1-E5 in Drafting Cycle; lens count five | PASS |
| 3 | E6 Halted-Plan Triage section (both halves) | PASS |
| 4 | E7 unmeasurable, E8 Rule 36, E11 dispatch paths | PASS |
| 5 | E9=#57, E10=#58 in Orchestration Plan Rules | PASS |
| 6 | Historical changelog counts intact | PASS |
| 7 | New changelog row (v4.78, fourteen, merges, section, lens-five) | PASS |
| 8 | Fourteen proposals implemented | PASS |
| 9 | 183 untouched at reference | PASS |
| 10 | Corpus totals: 178 entries, 186 proposals, proposed=0 | PASS |
| 11 | No src/ change, no schema drift | PASS |

**ALL CHECKS PASS.**

---

## Rule 20 Self-Grep

`grep -c 'PASSED — SELF-CHECK PASSED' knowledge/qa/gate-2-codification-qa-2026-07-22.md` → 2 (banner + this self-grep line)

---

## Output Receipt

**Status:** Complete
**Agent:** QA (Step 3)
**Plan:** 259 — Gate 2 Codification (cycle 2026-07-22)

### Ledger Updates
#### Project Status
Gate 2 complete — PLANNER_TEMPLATE **v4.78**, fourteen proposals (172-186 except 183) implemented, two merges [E1 execute-before-deposit (172+173+179), E6 halted-plan triage (174+175)], a new `## Halted-Plan Triage` section, a mechanical conformance pass (E5) added distinct from the five adversarial lenses, lens count deliberately stays five, `proposed` now 0. The 2026-07-22 lessons arc is COMPLETE.

#### Prompt Feedback
**2026-07-23 — Gate 2 Codification cycle 2026-07-22 (QA Step 3)**

1. The Step-2 dev-log's raw CLI output for the per-id DB read was directly byte-comparable with QA's re-run — the plan's instruction to use identical query format across steps made this check mechanical.
2. Including 183 in both the Step-2 and QA query sets produced an unambiguous proof of non-interference — the timestamp predating the transition is the strongest evidence.
3. The shifted line numbers (plan referenced :1845/:1846 at authoring against v4.77; actual post-edit positions are 1893/1894) were not a problem because QA re-derived by grep rather than trusting offsets — the plan's "re-derive every line number" instruction from Step 1 prevented false failures.
4. E5's explicit wording as "distinct from the adversarial lenses above" and "non-adversarial" made the lens-count check trivially confirmable — no judgment needed about whether E5 was a sixth lens.
5. The status distribution showing `proposed` absent (rather than `proposed|0`) is the correct SQLite behavior for GROUP BY with zero rows — QA correctly interpreted absence as zero.
