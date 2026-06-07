# Gate 2 Codification Blueprint — 2026-06-07

**Author:** Forge Developer (SA role), Step 1
**Dedup baseline:** PLANNER_TEMPLATE.md v4.59 (live file as of 2026-06-07)
**Source proposals:** 5 accepted governance_rule proposals (IDs 124, 126, 127, 128, 130)
**Net distinct edits to PLANNER_TEMPLATE.md:** 5 (3 APPEND-NEW + 2 STRENGTHEN-EXISTING)

---

## Dedup Pass Summary

Every proposal was deduplicated against the live v4.59 PLANNER_TEMPLATE.md. No fully-subsumed proposals were found.

| Proposal | Disposition | Rationale |
|---|---|---|
| 124 | APPEND-NEW | No existing rule covers deriving the classification work list from `get_unclassified_entries(conn)`. No mention of `needs_classification` field handling anywhere in v4.59. |
| 126 | STRENGTHEN-EXISTING Checklist #16 | Checklist #16 (L1057) lists `pause_for_verdict` among convention strings to copy but does NOT state the silent-failure cost of an invalid token. Workaround #6 (L1279) documents the daemon-side behavior separately. The strengthening adds the uniquely-high-stakes silent-failure note to #16 — complementary, not duplicative. |
| 127 | APPEND-NEW | No existing rule prescribes a mandatory top-of-step callout structure for gate-enforced QA actions. Rule 20 (L523) covers the self-check block itself; Checklist #4 (L985) covers including the canonical template. Neither prescribes the four-element callout structure (name gate, quote banner, state table doesn't satisfy, self-grep). |
| 128 | APPEND-NEW | No existing rule requires DEV self-verify and Planner review to run the full pytest suite and read tail output. Rule 21 (L564) covers test-scope declaration. Quality Standards substance-check bullet (L1112) covers individual assertion verification. Wall-clock bullet (L1113) covers execution mechanics. None require "run the full suite, read the tail, never infer from collect count." |
| 130 | STRENGTHEN-EXISTING Guardrails recurring-bug-class bullet | The existing bullet (L1093) covers checking knowledge base and demanding systemic solutions. It does NOT address verifying inherited fixes (from baton, prior session, or first instinct) against root cause before building. The strengthening adds the inherited-frame clause — a different angle (inherited fix verification vs. broader-fix mandate). |

**Final counts:** 3 APPEND-NEW, 2 STRENGTHEN-EXISTING, 0 FULLY SUBSUMED.

---

## Per-Rule Dispositions

### Rule 1 — Proposal 124 (Orchestration Plan Rule #47)

**Disposition:** APPEND-NEW
**Section home:** Orchestration Plan Rules
**Heading:** `### 47. Derive Lessons Forge classification work list from the stale-aware DB helper`

**Placement rationale:** This is a mandatory discipline for any plan step consuming the Lessons Forge classification pipeline — not a mechanical pre-deposit check (Checklist) but a behavioral rule in the same category as Rule 46 (Lessons Forge Gate 1 routing). Orchestration Plan Rule is the correct home.

**Rule body:**

```
### 47. Derive Lessons Forge classification work list from the stale-aware DB helper

Any plan step that consumes `run_full_lessons_cycle()` or independently derives the set of entries needing classification must use `get_unclassified_entries(conn)` — the stale-aware DB helper in `src/lessons_forge.py` — as the authoritative work-list source. Do not loop the `needs_classification` field from `run_full_lessons_cycle()`'s return value verbatim, and do not hand-copy a `NOT EXISTS` query from entry text or session notes. The `needs_classification` field is a convenience summary that may include entries whose only prior proposal has status `stale` (the edit-requeue path); `get_unclassified_entries(conn)` correctly excludes those entries by filtering on `p.status != 'stale'` in its subquery. Deriving the work list from any source other than the helper re-introduces the silent-drop bug class where stale-requeued entries are skipped.

Source: proposal 124, lesson 2026-06-07
```

**Confirmation (locked decision 2):** Rule body references `get_unclassified_entries(conn)` as the authoritative source. Does NOT reproduce the buggy `NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)` SQL from entry 117's text.

---

### Rule 2 — Proposal 126 (Plan Authoring Checklist #16, STRENGTHEN)

**Disposition:** STRENGTHEN-EXISTING
**Target:** Plan Authoring Checklist, `### 16.` (v4.59 lines 1057-1061)
**Current heading:** `### 16. Copy strict convention strings from known-good artifacts` (unchanged)

**old_string (verbatim, for DEV exact-match):**

```
Strict Bellows convention strings — header field names, dispatch mode values, directory names, lifecycle-prefix spellings, `pause_for_verdict` values — must be copied verbatim from a known-good artifact (a recent `Done/` plan, the Bellows README, or the relevant PLANNER_TEMPLATE rule), never authored from memory. Three failures in one session shared this root cause: a header field-line position error, a dispatch-mode typo, and a directory-name misspelling. Each was a machine-checked value that the Planner specified from recall rather than copy-paste.

Source: proposal 114, lesson 2026-06-03
```

**new_string:**

```
Strict Bellows convention strings — header field names, dispatch mode values, directory names, lifecycle-prefix spellings, `pause_for_verdict` values — must be copied verbatim from a known-good artifact (a recent `Done/` plan, the Bellows README, or the relevant PLANNER_TEMPLATE rule), never authored from memory. `pause_for_verdict` is uniquely high-stakes among these strings: an invalid token (e.g., `after_each_step`) is silently treated as no-pause — the daemon runs a multi-step plan straight through to completion with no verdict gates, and no downstream gate catches the misconfiguration. Three failures in one session shared this root cause: a header field-line position error, a dispatch-mode typo, and a directory-name misspelling. Each was a machine-checked value that the Planner specified from recall rather than copy-paste.

Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07
```

**Change summary:** One sentence inserted after the first sentence (after "never authored from memory."). The inserted sentence is: `\`pause_for_verdict\` is uniquely high-stakes among these strings: an invalid token (e.g., \`after_each_step\`) is silently treated as no-pause — the daemon runs a multi-step plan straight through to completion with no verdict gates, and no downstream gate catches the misconfiguration.` Source footer appended with `; proposal 126, lesson 2026-06-07`. No other text changed.

---

### Rule 3 — Proposal 127 (Orchestration Plan Rule #48)

**Disposition:** APPEND-NEW
**Section home:** Orchestration Plan Rules
**Heading:** `### 48. Gate-enforced QA actions require a mandatory top-of-step callout`

**Placement rationale:** This is a mandatory plan-structure rule about how QA steps must be composed when they include gate-enforced actions. It prescribes a four-element structural requirement, not a mechanical pre-deposit grep (Checklist) or a prose quality guideline (Quality Standards). Orchestration Plan Rule is the correct home.

**Rule body:**

```
### 48. Gate-enforced QA actions require a mandatory top-of-step callout

Any gate-enforced QA action (e.g., the Rule 20 self-check Python block) must have a MANDATORY callout at the TOP of the QA step — before the verification checklist, before the evidence collection, before any other QA work. The callout must: (a) name the gate that enforces the action, (b) quote the byte-exact banner string the gate greps for, (c) state explicitly that the verification table does NOT satisfy the gate, and (d) end with a self-grep instruction so the agent cannot finish the step without confirming the banner appears in its own output. Without this callout, agents routinely complete all other QA checks, produce a clean verification table, and skip the gate-enforced action — the gate FAILS, the plan halts, and a full re-dispatch is required. The callout structure makes the gate-enforced action impossible to overlook by placing it first and making it self-verifying.

Source: proposal 127, lesson 2026-06-07
```

---

### Rule 4 — Proposal 128 (Quality Standards, new bullet)

**Disposition:** APPEND-NEW
**Section home:** Quality Standards
**Format:** Unordered list bullet (matching existing Quality Standards format, with inline source citation)

**Rule body:**

```
- DEV self-verify and Planner review must each run the full pytest suite to a pass/fail result and read the tail output. Never infer green from a collect count, a target-file subset, or a prior step's pass headline. Bellows gates do NOT include suite-green — a plan can close with failing tests if no one runs the suite. This must be enforced by plan authoring: DEV steps include an explicit `pytest tests/` (or equivalent full-suite command) with output-tail verification, and the Planner confirms a fresh full-suite result during Rule 22 review. (Source: proposal 128, lesson 2026-06-07)
```

---

### Rule 5 — Proposal 130 (Guardrails recurring-bug-class bullet, STRENGTHEN)

**Disposition:** STRENGTHEN-EXISTING
**Target:** Guardrails, recurring-bug-class bullet (v4.59 line 1093)
**No heading change** (this is a bullet, not a headed rule)

**old_string (verbatim, for DEV exact-match):**

```
- Do NOT write quick fixes or point patches for recurring bug classes. When a bug surfaces that is similar to a prior fix (same code area, same failure mode, same root cause class), the Planner MUST check the knowledge base for prior diagnostics and fixes in that area. If a prior fix exists, the new fix must address the systemic cause — not add another layer of patching. The Planner should ask: "Why didn't the prior fix prevent this?" If the answer is "the prior fix was too narrow," the new plan must be broader. Recurring symptoms demand architectural solutions: centralized sanitization functions, structural refactors, schema-level constraints — not another point fix in another code path. This is the Eluvian process: deep diagnostics, reference to past fixes, structural solutions that compound into reliability.
```

**new_string:**

```
- Do NOT write quick fixes or point patches for recurring bug classes. When a bug surfaces that is similar to a prior fix (same code area, same failure mode, same root cause class), the Planner MUST check the knowledge base for prior diagnostics and fixes in that area. If a prior fix exists, the new fix must address the systemic cause — not add another layer of patching. The Planner should ask: "Why didn't the prior fix prevent this?" If the answer is "the prior fix was too narrow," the new plan must be broader. When handed a proposed fix — from a baton, a prior session, or your own first instinct — verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom. Recurring symptoms demand architectural solutions: centralized sanitization functions, structural refactors, schema-level constraints — not another point fix in another code path. This is the Eluvian process: deep diagnostics, reference to past fixes, structural solutions that compound into reliability.
```

**Change summary:** One sentence inserted after "the new plan must be broader." and before "Recurring symptoms demand architectural solutions". The inserted sentence is: `When handed a proposed fix — from a baton, a prior session, or your own first instinct — verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom.` No other text changed. No Source footer added (the existing bullet has no Source footer; this is original Guardrails text, not a forge-cycle addition, so the footer convention does not apply).

---

## Per-Edit Anchor Map for DEV

DEV must verify each anchor verbatim before editing. If any anchor or old_string fails to match, set Output Receipt status to `Partial` and halt.

**Recommended edit order:** Apply bottom-to-top (Edit 4 → Edit 3 → Edit 2 → Edit 1) so earlier edits do not shift the line numbers of later anchors. Alternatively, apply in any order and re-verify anchors against the file state at each step (the anchor text is unique regardless of ordering).

### Edit 1 — Orchestration Plan Rules: append Rules 47 and 48 (proposals 124, 127)

**Type:** INSERTION
**Anchor line-before (v4.59 line 957):**
```
Source: proposal 118, lesson 2026-06-03
```
**Anchor line-after (v4.59 line 959):**
```
---
```
**Action:** Insert Rules 47 and 48 (with blank-line separators) after line 957 (Source line of Rule #46), before the `---` separator.

**Insert block (exact text):**

```

### 47. Derive Lessons Forge classification work list from the stale-aware DB helper

Any plan step that consumes `run_full_lessons_cycle()` or independently derives the set of entries needing classification must use `get_unclassified_entries(conn)` — the stale-aware DB helper in `src/lessons_forge.py` — as the authoritative work-list source. Do not loop the `needs_classification` field from `run_full_lessons_cycle()`'s return value verbatim, and do not hand-copy a `NOT EXISTS` query from entry text or session notes. The `needs_classification` field is a convenience summary that may include entries whose only prior proposal has status `stale` (the edit-requeue path); `get_unclassified_entries(conn)` correctly excludes those entries by filtering on `p.status != 'stale'` in its subquery. Deriving the work list from any source other than the helper re-introduces the silent-drop bug class where stale-requeued entries are skipped.

Source: proposal 124, lesson 2026-06-07

### 48. Gate-enforced QA actions require a mandatory top-of-step callout

Any gate-enforced QA action (e.g., the Rule 20 self-check Python block) must have a MANDATORY callout at the TOP of the QA step — before the verification checklist, before the evidence collection, before any other QA work. The callout must: (a) name the gate that enforces the action, (b) quote the byte-exact banner string the gate greps for, (c) state explicitly that the verification table does NOT satisfy the gate, and (d) end with a self-grep instruction so the agent cannot finish the step without confirming the banner appears in its own output. Without this callout, agents routinely complete all other QA checks, produce a clean verification table, and skip the gate-enforced action — the gate FAILS, the plan halts, and a full re-dispatch is required. The callout structure makes the gate-enforced action impossible to overlook by placing it first and making it self-verifying.

Source: proposal 127, lesson 2026-06-07
```

**Expected net line delta:** +12 lines

### Edit 2 — Checklist #16: in-place STRENGTHEN (proposal 126)

**Type:** IN-PLACE REPLACE (exact-match mandatory)
**old_string:** The body paragraph at v4.59 L1059 plus the Source footer at L1061. See Rule 2 above — the verbatim old_string from `Strict Bellows convention strings` through `Source: proposal 114, lesson 2026-06-03`.
**new_string:** See Rule 2 above — same text with the silent-failure sentence inserted after "never authored from memory." and Source footer updated.

**⚠ Exact-match care:** The old_string contains em-dashes (`—`), backtick-quoted inline code, and a long single-line paragraph. DEV must match the exact characters including em-dashes (not hyphens) and backtick boundaries.

**Expected net line delta:** 0 (the paragraph is longer but structurally the same number of lines)

### Edit 3 — Guardrails recurring-bug-class bullet: in-place STRENGTHEN (proposal 130)

**Type:** IN-PLACE REPLACE (exact-match mandatory)
**old_string:** The bullet at v4.59 L1093. See Rule 5 above — the verbatim old_string from `- Do NOT write quick fixes` through `structural solutions that compound into reliability.`
**new_string:** See Rule 5 above — same text with the inherited-frame sentence inserted after "the new plan must be broader." and before "Recurring symptoms demand architectural solutions".

**⚠ Exact-match care:** The old_string contains em-dashes (`—`), straight double-quotes around internal strings, and a long single-line paragraph. DEV must match exact characters.

**Expected net line delta:** 0 (the paragraph is longer but structurally the same number of lines)

### Edit 4 — Quality Standards: append one new bullet (proposal 128)

**Type:** INSERTION
**Anchor line-before (v4.59 line 1113):**
```
- When authoring test-execution instructions for QA or diagnostic steps, use a wall-clock bound external to pytest (e.g., `timeout 600 pytest ...` via shell) plus `--collect-only` for collection-time isolation. `pytest --timeout=N` bounds per-test execution only — it cannot catch hangs during collection/import, session/module-scoped fixture setup, or C-level/non-main-thread blocking. The external wall-clock bound catches all of these. `--collect-only` as a preliminary command isolates collection-time hangs from execution-time behavior, allowing targeted diagnosis. This supplements Rule 21's full-suite output mode (which keeps the run visible) with a hard bound that kills genuinely hung runs. (Source: proposal 102, lesson 2026-06-03)
```
**Anchor line-after (v4.59 line 1115):**
```
---
```
**Action:** Insert one new bullet after line 1113, before the blank line + `---` separator.

**Insert text (exact):**
```
- DEV self-verify and Planner review must each run the full pytest suite to a pass/fail result and read the tail output. Never infer green from a collect count, a target-file subset, or a prior step's pass headline. Bellows gates do NOT include suite-green — a plan can close with failing tests if no one runs the suite. This must be enforced by plan authoring: DEV steps include an explicit `pytest tests/` (or equivalent full-suite command) with output-tail verification, and the Planner confirms a fresh full-suite result during Rule 22 review. (Source: proposal 128, lesson 2026-06-07)
```

**Expected net line delta:** +1 line
