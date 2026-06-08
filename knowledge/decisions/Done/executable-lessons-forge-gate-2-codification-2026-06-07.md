# Executable: Lessons Forge 2026-06-07 Gate 2 — Codify 5 governance rules + route 1 structural finding to BACKLOG

**Plan slug:** executable-lessons-forge-gate-2-codification-2026-06-07
**Plan type:** executable
**Project:** governance (root, /Users/marklehn/Developer/GitHub/)
**Specialist:** Forge Developer (SA, DEV, QA roles all use lessons-forge/agents/FORGE_LESSONS_AGENT.md as project context anchor; this plan edits governance-root PLANNER_TEMPLATE.md so SA/DEV/QA also read PLANNER_TEMPLATE.md fully)
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-06-07
**qa_steps:** 3

---

## Context

Gate 2 (codification) of the 2026-06-07 Lessons Forge cycle. Gate 1 completed 2026-06-07: 9 proposals (IDs 122-130, entries 93/116/117-123) dispositioned in `lessons-forge.db` — 6 accepted, 3 rejected. This plan codifies the 5 accepted proposals that target `PLANNER_TEMPLATE.md` and routes the 1 accepted `structural` proposal to Bellows BACKLOG. No narratives this cycle.

Same SA -> DEV -> QA shape as the 2026-06-03 Gate 2 (`Done/executable-lessons-forge-gate-2-codification-2026-06-03.md`). Like that cycle, this one mixes APPEND-NEW with in-place STRENGTHEN edits, so QA verifies modifications (not additive-only). Smaller scope: 3 append-new + 2 narrow strengthen.

**Gate 1 dispositions (locked; statuses already written to `lessons-forge.db`, `status_updated_by='ceo'`):**

REJECTED — already covered by live v4.59, no governance action:
- **122 (entry 93)** schema-migration init_db+PRAGMA discipline — duplicate of Plan Authoring Checklist **#12** (`### 12. Schema migration plans include init_db and PRAGMA verification`, ~L1033), codified 2026-05-27. Content is verbatim equivalent.
- **123 (entry 116)** scope_check blueprint-delegation false-positive *interim* discipline — superseded by Plan Authoring Checklist **#14** (`### 14. Name all target file paths literally in step bodies`, ~L1045), codified at the 06-03 Gate 2. #14 is prop-121's codification; inlining target paths removes the false-positive trigger, so the "expect the FP, don't escalate" workaround is moot and would undercut #14.
- **125 (entry 118)** clean-main-before-redispatch — covered by Bellows Operational Workaround **#13** (keep watched roots clean before deposit, ~L1331) plus the no-edits-while-in-flight rule, both codified at the 06-03 Gate 2. A re-dispatch is a deposit. 118's instruction to commit lifecycle artifacts is also slightly wrong — #13's dirty-tree check exempts them.

ACCEPTED -> codify into PLANNER_TEMPLATE.md (this plan):
- **124 (entry 117)** APPEND-NEW
- **126 (entry 119)** STRENGTHEN Plan Authoring Checklist **#16** (`### 16. Copy strict convention strings from known-good artifacts`, ~L1057) — NARROW
- **127 (entry 120)** APPEND-NEW
- **128 (entry 121)** APPEND-NEW
- **130 (entry 123)** STRENGTHEN Guardrails recurring-bug-class bullet (`Do NOT write quick fixes for recurring bug classes`, ~L1093) — NARROW

ACCEPTED -> route to BACKLOG (NOT a template edit):
- **129 (entry 122)** structural; `target_artifact=None`. `__file__`-relative root constants break under worktree execution. Filed to Bellows BACKLOG at session-wrap (Planner-direct, see Housekeeping #4). SA authors NO template text for this.

**Locked CEO decisions (pre-blueprint, binding — do NOT re-litigate):**

1. **Dedup baseline is the LIVE PLANNER_TEMPLATE.md v4.59.** SA re-verifies each of the 5 codification targets against the live file before authoring. The three REJECTED proposals above are already dispositioned — SA does not author text for them; if SA's dedup disagrees with any rejection, SA flags it for CEO rather than acting.

2. **CRITICAL — proposal 124 codifies the HELPER, not the quoted SQL.** Entry 117's note text quotes `WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)` — the buggy non-stale-aware form that silently drops entries whose only proposal is `stale` (the edit-requeue path). The codified rule MUST reference `get_unclassified_entries(conn)` (the stale-aware helper at `src/lessons_forge.py`), NOT the SQL from the entry text. This is the one place a careless codification re-introduces the exact bug this cycle fixed.

3. **The two STRENGTHEN edits are NARROW additions, not rewrites:**
   - **126 -> Checklist #16:** add ONLY a silent-failure note — an invalid `pause_for_verdict` token (e.g. `after_each_step`) is silently treated as no-pause; the daemon runs the whole plan straight through with no verdict gates, and no gate catches it. This makes `pause_for_verdict` uniquely higher-stakes than other convention strings. Do NOT duplicate #16's existing copy-verbatim instruction — the value added is the silent-failure cost, which #16 does not currently state.
   - **130 -> Guardrails recurring-bug-class bullet:** add ONLY an inherited-frame clause — when handed a proposed fix (baton, prior session, or your own first instinct), verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom. Do NOT restate the existing recurring-bug-class text; this extends it.

4. **No version bump in DEV.** PLANNER_TEMPLATE.md `**Version:**` stays at 4.59 through this plan. Bump to 4.60 happens Planner-direct at session-wrap, after QA verdict.

5. **Proposal 129 is NOT a template edit.** It is filed to Bellows BACKLOG at session-wrap (Housekeeping #4). SA produces no blueprint text for it.

**Source proposals — 5 accepted `governance_rule`, `target_artifact='PLANNER_TEMPLATE.md'` (suggested_action verbatim from `lessons-forge.db`):**

| ID | Entry | Disposition | Suggested home | suggested_action (verbatim) |
|---|---|---|---|---|
| 124 | 117 | APPEND-NEW | Plan Authoring Checklist (new item) or Orchestration Plan Rule | any consumer of run_full_lessons_cycle() must derive the classification work list from get_unclassified_entries(conn) — the stale-aware DB helper — not from the needs_classification field. Never loop needs_classification verbatim. |
| 126 | 119 | STRENGTHEN Checklist #16 | Plan Authoring Checklist #16 (~L1057) | confirm pause_for_verdict is one of the three accepted tokens (always, after_step_1, after_qa_step) by copying from a known-good plan; for per-step gating use always; the parsed value from gates._parse_plan_header is shown but NOT enum-validated; an invalid token is silently treated as no-pause. |
| 127 | 120 | APPEND-NEW | Orchestration Plan Rules (new rule) or Quality Standards | any gate-enforced QA action (e.g. Rule 20 self-check) must have a MANDATORY callout at the TOP of the QA step that (a) names the gate, (b) quotes the byte-exact banner the gate greps for, (c) states the verification table does NOT satisfy it, and (d) ends with a self-grep so the agent cannot finish without it. |
| 128 | 121 | APPEND-NEW | Quality Standards (new bullet) | DEV self-verify and Planner review must each run the full pytest suite to a pass/fail result and read the tail output; never infer green from a collect count or target-file subset; Bellows gates do NOT include suite-green — it must be enforced by plan authoring. |
| 130 | 123 | STRENGTHEN Guardrails | Guardrails recurring-bug-class bullet (~L1093) | when handed a proposed fix (baton, prior session, or own first instinct), verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom. |

**Net: 5 distinct PLANNER_TEMPLATE edits (3 APPEND-NEW + 2 NARROW STRENGTHEN). 1 BACKLOG route (129). 0 narratives.**

---

## Execution Map

Step 1 (SA) -> [verdict pause] -> Step 2 (DEV) -> [verdict pause] -> Step 3 (QA)

Sequential. No parallel lanes. Single project context (governance-root PLANNER_TEMPLATE.md + lessons-forge knowledge deposits). DEV edits after SA blueprint is verdict-approved. QA verifies after DEV is verdict-approved.

---

## How to Run This Plan

Bellows-dispatched. After deposit to `lessons-forge/knowledge/decisions/`, Bellows claims and dispatches Step 1 automatically. `pause_for_verdict: always` produces a verdict request after each step; the Planner verifies per Rule 22 and issues continue/stop verdicts to `bellows/verdicts/resolved/`.

---

## STEP 1 — Forge Developer (SA role)

**Role:** Systems Analyst / Architect

**Reads:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.59 — the dedup baseline)
- `/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-06-07.md` (if present; else `lessons-report-2026-06-06.md` — the cycle's classification report)
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/executable-lessons-forge-gate-2-codification-2026-06-03.md` (prior-cycle precedent: footer convention, entry prose style, heading depth, anchor-map shape)
- This plan file (Context section: the 5-proposal table, the 3 locked-rejection rationales, the 5 locked CEO decisions)
- `lessons-forge.db` — read the `reasoning` column for any of the 5 proposals whose `suggested_action` is insufficient to author the rule body: `SELECT id, suggested_action, reasoning FROM lesson_proposals WHERE id IN (124,126,127,128,130) AND status='accepted';`

**Task:**

Author one SA blueprint that resolves dedup + placement + exact rule text for the 5 accepted codification proposals. Deduplicate each against the live v4.59 file (decision 1) before assigning a disposition.

Produce, in a single blueprint deposit file, for EACH of the 5 rules:

1. **Disposition** — APPEND-NEW or STRENGTHEN-EXISTING. The Context section pre-assigns these (124/127/128 APPEND-NEW; 126/130 STRENGTHEN); CONFIRM each against the live file. For STRENGTHEN, the exact existing target (section + current heading + line range in v4.59) and a unified before/after of the prose.

2. **Section home + heading** — for APPEND-NEW: the section, the next available number, and the sentence-case working title matching existing entry style (Plan Authoring Checklist entries are `### N. Title`; Orchestration Plan Rules are `### N. Title`; Quality Standards are bullets/prose under `## Quality Standards`). For 124 decide Plan Authoring Checklist item vs Orchestration Plan Rule; for 127 decide Orchestration Plan Rule vs Quality Standards; for 128 Quality Standards bullet. State final placement with the exact number.

3. **Rule body** — the exact prose DEV will write (mechanical, actionable, matching the register of existing entries). Include the source-attribution footer `Source: proposal N, lesson 2026-06-07`.

**Binding constraints (decisions 2 + 3 — do NOT re-litigate):**
- **124:** the rule body MUST reference `get_unclassified_entries(conn)`; it MUST NOT reproduce the `NOT EXISTS (SELECT 1 ... WHERE p.entry_id=e.id)` SQL from entry 117's text. Frame: "derive the work list from the helper, never from `needs_classification` and never from a hand-copied query."
- **126:** STRENGTHEN Checklist #16 by ADDING ONLY a silent-failure sentence (invalid `pause_for_verdict` token -> silently treated as no-pause -> daemon runs straight through, no gate catches it -> uniquely high-stakes). Do NOT duplicate #16's existing copy-verbatim instruction. Provide the before/after with the single added sentence visible.
- **130:** STRENGTHEN the Guardrails recurring-bug-class bullet by ADDING ONLY the inherited-frame clause. Do NOT restate the existing recurring-bug-class prose. Provide before/after with the added clause visible.

**Also specify:**
4. **Per-edit anchor map for DEV** — for every APPEND-NEW insertion: the exact v4.59 line-before / line-after anchor lines. For each STRENGTHEN: the verbatim `old_string` (exact whitespace, em-dashes, smart quotes) and the exact `new_string`. Plus expected net line delta per edit.

**Liveness anchors (Rule 41 — this prompt is >400w):** emit a one-line claim-confirmation BEFORE your first read; a one-line acknowledgment after each file read; and a one-line section marker at the start of each blueprint section (dedup pass, per-rule dispositions, anchor map).

**Deposits:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-07.md`

**Output Receipt fields required:**
- What was done (summary)
- Files deposited (the blueprint path)
- Decisions made (final disposition + placement per rule; final APPEND-NEW vs STRENGTHEN count; confirmation that 124 references the helper not the SQL)
- Flags for CEO (any of the 5 found fully subsumed by existing text and recommended for `implemented` with no edit; any dedup judgment that disagrees with a locked rejection)
- Flags for Next Step (DEV anchor map confirmed; the two STRENGTHEN `old_string`s flagged for exact-match care)

---

## STEP 2 — Forge Developer (DEV role)

**Role:** Developer

**Reads:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-07.md` (Step 1 blueprint — source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.59 — verify SA anchors before editing)

**Task:**

Apply the SA blueprint to `PLANNER_TEMPLATE.md`: 3 APPEND-NEW insertions + 2 in-place STRENGTHEN edits, per the blueprint's disposition for each rule.

**Pre-edit verification (per blueprint anchor map):**
1. For every APPEND-NEW insertion: grep the SA-cited line-before / line-after anchors; confirm both exist verbatim at the cited lines.
2. For each STRENGTHEN edit (126, 130): confirm the SA-cited `old_string` exists verbatim and EXACTLY ONCE in the file. These edits modify existing text — exact match is mandatory; em-dashes, smart quotes, and whitespace must match.
3. Confirm `**Version:** 4.59` at line 5 is unchanged (no version bump in this step — decision 4).
4. If ANY anchor or `old_string` fails to match: set Output Receipt status to `Partial`, populate **Flags for CEO** with the mismatch evidence, edit NOTHING in PLANNER_TEMPLATE.md, and end the step. Bellows trips the receipt gate and pauses for Planner verdict.

**Edits:**
- APPEND-NEW (124, 127, 128): insert at the specified section position with the specified heading depth and number.
- STRENGTHEN (126, 130): replace the cited `old_string` with the blueprint's `new_string`. These are NARROW — the new_string is the original text plus one added sentence/clause (decision 3). Do not rewrite surrounding prose.
- Renumber within a section ONLY if the blueprint specifies it (e.g., a new Plan Authoring Checklist item 19, or a new Orchestration Plan Rule number). Do not renumber any rules the blueprint does not touch.
- Every new rule carries its `Source: proposal N, lesson 2026-06-07` footer; each strengthened rule gets its footer updated to append `; proposal N, lesson 2026-06-07` if it already has a Source line, else add one.

**No version bump.** `**Version:**` stays 4.59. Session-wrap handles the bump to 4.60.

**No edits for proposal 129.** It is not a template change (decision 5).

**Deposits:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (modified — 3 insertions + 2 in-place edits)

**Output Receipt fields required:**
- What was done (summary; per-section line ranges touched; insertion vs in-place-edit counts)
- Files deposited (the path above)
- Lines added / lines changed (counts)
- Pre-edit verification results (anchor + old_string match confirmations)
- Flags for CEO (any blueprint-vs-file mismatch caught; any prose adjustment made for line-fit)
- Flags for Next Step (QA evidence — exact inserted/changed byte ranges per rule for verbatim-match verification)

---

## STEP 3 — Forge Developer (QA role)

**Role:** Quality Assurance

**MANDATORY — GATE-ENFORCED SELF-CHECK (read first):** This step is gated by `rule_20_self_check`, which greps this QA report for the byte-exact banner from `RULE_20_SELF_CHECK_BLOCK.md` (`Rule 20 — QA Self-Check Results` and the `PASSED` line). The verification table below does NOT satisfy this gate. You MUST author and run the canonical Rule 20 Python block (check 8) and reproduce its stdout banner byte-identically, then self-grep your own report for the banner before finishing. If the banner is absent the gate FAILS and the plan halts.

**Reads:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-07.md` (blueprint — source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (Step 2 deposit, modified)
- `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (canonical Rule 20 self-check Python block)

**Task:** Verify Step 2 against the Step 1 blueprint. Each check produces a PASS/FAIL row with line citations.

**Verification checks:**
1. **Per-rule verbatim match.** For each of the 5 rules, the modified file contains the blueprint's prescribed text at the blueprint's prescribed location, with correct heading depth/number and the `Source: ... lesson 2026-06-07` footer. One PASS/FAIL row per rule.
2. **STRENGTHEN edits are narrow + correct.** For 126 and 130: the original text is intact and ONLY the prescribed sentence/clause was added (no rewrite, no duplication of existing instruction). Cite before/after line ranges.
3. **124 references the helper, not the SQL.** Confirm the codified 124 rule names `get_unclassified_entries(conn)` and does NOT contain the string `NOT EXISTS (SELECT 1 FROM lesson_proposals`. This is a hard FAIL if the buggy SQL appears.
4. **No collateral disturbance.** `git diff` on PLANNER_TEMPLATE.md shows only the 5 blueprint-specified ranges; no content outside them is altered. Cite the diff hunk summary. Evidence file: `qa/evidence/<plan-slug>/git_diff.txt`.
5. **Version field unchanged.** `**Version:** 4.59` at line 5 is unchanged.
6. **No proposal-129 text.** Confirm no `__file__` / `GOVERNANCE_ROOT` / marker-walk-up rule text was added to the template (129 is BACKLOG-routed, not codified here).
7. **Rule 20 canonical self-check.** Author the canonical QA self-check Python block per Rule 20 from `RULE_20_SELF_CHECK_BLOCK.md` with placeholders filled. Required-evidence-files for this governance-edit plan is just the git_diff evidence from check 4; pass `evidence_dir=lessons-forge/knowledge/qa/evidence/<plan-slug>/` and the corresponding `required_evidence_files`. Run via `python3`; capture stdout under a section titled "Rule 20 Self-Check (canonical Python block, stdout)". The PASSED banner line MUST appear byte-identically — do NOT paraphrase, substitute, or omit. Then self-grep this report for the banner and confirm presence.

**Deposits:**
- `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-06-07.md`

**Output Receipt fields required:**
- What was done (PASS/FAIL counts per check)
- Files deposited (the QA report path)
- Decisions made (any QA judgment calls; should be none for verbatim work)
- Flags for CEO (any FAIL row with evidence; any Rule 20 block discrepancy)
- Flags for Next Step (none — Step 3 is terminal)

---

## End-of-Plan Housekeeping (Planner-side, post-QA-verdict)

After QA continue verdict and Rule 22 (b) substance pass:

1. **Bellows owns the terminal Done/ move** on continue-verdict consumption (recovery path: Planner-direct `Filesystem:move_file` only if the daemon is not running). Do NOT pre-rename.

2. **Split-commit pattern** (this plan edits a file OUTSIDE the lessons-forge submodule):
   - **Governance repo** (`/Users/marklehn/Developer/GitHub/`): `git add PLANNER_TEMPLATE.md` (the codification edit; folds in the version bump from step 6 if done before push).
   - **lessons-forge submodule**: `cd lessons-forge && git add knowledge/research/gate-2-codification-blueprint-2026-06-07.md knowledge/qa/gate-2-codification-qa-2026-06-07.md knowledge/qa/evidence/ knowledge/decisions/Done/` (blueprint, QA report, evidence, consumed plan-lifecycle artifacts).
   - Each repo: `git fetch origin && git pull --rebase origin main && git push origin main`. Agents do NOT push; Planner pushes at wrap.

3. **Submodule pointer bump:** after the lessons-forge push, `cd` to governance root, `git submodule status` (expect `+` prefix on lessons-forge). If dirty: `git add lessons-forge && git commit -m "chore: bump lessons-forge submodule (2026-06-07 Gate 2)" && git push origin main`.

4. **File proposal 129 to Bellows BACKLOG (Planner-direct):** append an entry to `bellows/knowledge/BACKLOG.md` for the `__file__`-relative root-constant fix: replace `GOVERNANCE_ROOT`/`BELLOWS_ROOT` (and anvil `ANVIL_ROOT`) with a shared marker walk-up resolver that finds a stable marker (e.g. `COMPANY.md`) by traversing parents; audit all `__file__`-relative roots across bellows, forge, anvil for worktree-reachability. Note: third instance of the worktree-root-confusion class (anvil F8, bellows GOVERNANCE_ROOT, this). Source: proposal 129, lesson 2026-06-07. Commit in the bellows submodule, then bump the bellows submodule pointer at governance root (same two-commit pattern as #3).

5. **Gate 2d status advancement (DB):** advance the codified + routed proposals to `implemented`:
   `UPDATE lesson_proposals SET status='implemented', status_updated_at='2026-06-07', status_updated_by='planner' WHERE id IN (124,126,127,128,129,130);`
   (6 rows: 5 template codifications + 129 once its BACKLOG entry is filed. The 3 rejected — 122, 123, 125 — stay `rejected`.)

6. **Version bump:** PLANNER_TEMPLATE.md `**Version:**` 4.59 -> 4.60; `**Last Updated:** 2026-06-07 (v4.60)`; Planner-direct write at session-wrap. Add a Lessons row documenting the 2026-06-07 Gate 2 ratification (5 rules from 6 accepted proposals; 3 rejected as already-covered: 93/Rule12, 116/Checklist#14, 118/Workaround#13; 1 structural routed to Bellows BACKLOG; dedup baseline was live v4.59). Commit on the governance repo (folds into step 2's governance commit if done before push).

7. **NEXT_SESSION baton:** update `lessons-forge/NEXT_SESSION.md` — clear the Gate 1/Gate 2 in-flight thread; mark the 2026-06-07 cycle closed through Gate 2d. Update shop-level `shop_next_session.md` only if a shop-meta carry exists.

8. **Horizon (not this plan):** Bellows `_teardown_worktree` (b) silent-loss daemon restart; worktree BACKLOG family re-eval against the merge-ff model; `_LIFECYCLE_IGNORE_RE` latent-instance audit; 16 halted-* plan sweep; Anvil first-cycle setup.
