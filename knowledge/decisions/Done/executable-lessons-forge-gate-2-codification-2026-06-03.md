# Executable: Lessons Forge 2026-06-03 Gate 2 — Codify 19 accepted governance rules + archive 2 narratives

**Plan slug:** executable-lessons-forge-gate-2-codification-2026-06-03
**Plan type:** executable
**Project:** governance (root, /Users/marklehn/Developer/GitHub/)
**Specialist:** Forge Developer (SA, DEV, QA roles all use lessons-forge/agents/FORGE_LESSONS_AGENT.md as project context anchor; this plan edits governance-root PLANNER_TEMPLATE.md so SA/DEV/QA also read PLANNER_TEMPLATE.md fully)
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-06-03
**qa_steps:** 3

---

## Context

Gate 2 (codification) of the 2026-06-03 Lessons Forge cycle. Gate 1 completed: 23 new proposals (IDs 99-121) dispositioned — 21 accepted, 2 rejected (106, 112 — daemon-bug workarounds; underlying bugs already in Bellows BACKLOG, no governance action). This plan codifies the 19 accepted `governance_rule` proposals into `PLANNER_TEMPLATE.md` and archives the 2 accepted `narrative` proposals (109, 117).

Same SA -> DEV -> QA shape as the 2026-05-27 Plan A/B (`Done/executable-planner-template-bellows-operational-workarounds-2026-05-27.md`). Key difference from 05-27: that cycle *created* two new subsections (pure-additive). This cycle *adds into and strengthens* existing sections — several proposals supersede or strengthen existing rules in place, so DEV performs a mix of insertions AND in-place edits, and QA verifies modifications (not zero-deletion additive-only).

**Locked CEO decisions (pre-blueprint, this session):**

1. **Dedup baseline is live PLANNER_TEMPLATE.md v4.58 — NOT v4.55.** Three increments shipped since the cycle's notional v4.55 baseline: v4.56 (Rule 21 test-count right-sizing), v4.57 (dropped vestigial claim-rename from canonical step + SA-blueprint templates; added "Gate-failure evidence-string discrimination — worktree teardown variants" to Rule 25 routing, currently ~L709-711), v4.58 (Rule 21 full-suite output-mode). SA dedups every proposal against the live v4.58 file. Three proposals have confirmed v4.57 overlap and are RECONCILE-not-append (see disposition table): 104, 113, 115.

2. **Three consolidation pairs (proposal-ID space) merge to single rules.** The classifications-summary states these in *entry* IDs (94-116); they map +5 to *proposal* IDs (99-121). Confirmed merges:
   - **100 + 108** -> one rule (no-writes-during-dispatch / clean-tree). 108 explicitly "strengthens existing" -> this STRENGTHENS existing Bellows Operational Workaround #8 ("Check for active worktrees before editing project files"), generalizing it to "defer ALL working-tree edits until no plan in-flight" and adding the ~5-10 min per-dirty-tree-cycle recovery-cost quantification.
   - **113 + 115** -> one rule (R2 recovery). Both are R2 teardown-cherry-pick recovery variants. RECONCILE against existing Workaround #12 ("Final-step gate_failure recovery checklist") AND Rule 25's v4.57 teardown-variant discrimination (~L709-711). 115 ("agent's own in-progress- rename" variant) further interacts with v4.57's claim-rename drop. Net effect should STRENGTHEN existing R2 text, not add a parallel rule.
   - **103 + 121** -> one rule (literal file paths for scope_check). Two angles: deposit paths in `**Deposits:**` blocks (103) and target paths inlined in DEV step bodies rather than delegated to a referenced blueprint (121). SA decides single-rule-two-clauses vs. one rule that subsumes both.

3. **Single plan, both sections + archival** (not A/B split). 16 distinct rules (19 - 3 merges) across both target sections plus the narrative archive ship in one SA->DEV->QA pass.

4. **Narrative archival:** the existing `lessons-forge/knowledge/archived-narratives-2026-05-27.md` is a per-cycle file. DEV creates a NEW `lessons-forge/knowledge/archived-narratives-2026-06-03.md` mirroring its structure (title, intro, per-proposal `## Proposal N — <heading>` blocks with Source lesson / Why archived / Suggested action verbatim). Do NOT append to the 05-27 file (filename-truthfulness, Procedure 6).

5. **No version bump in DEV.** PLANNER_TEMPLATE.md `**Version:**` stays at 4.58 through this plan. Version bump to 4.59 happens Planner-direct at session-wrap, after QA verdict.

**Source proposals — 19 accepted `governance_rule` (all `status='accepted'`, `target_artifact='PLANNER_TEMPLATE.md'` in `lessons-forge.db`).** `suggested_action` text below is verbatim from the DB. Cluster + disposition + suggested section home are SA-confirmable guidance; the locked merges (decision 2) and dedup baseline (decision 1) are binding.

| ID | Cluster | Disposition | Suggested home | suggested_action (verbatim) |
|---|---|---|---|---|
| 99 | plan-authoring | append-new | Plan Authoring Checklist | verify every new plan header with gates._parse_plan_header against the current parser before deposit; never certify a header by pattern-matching old Done/ artifacts. |
| 103 | plan-authoring | MERGE w/121 | Plan Authoring Checklist | name all deposit file paths literally in plan step bodies — scope_check authorizes from named paths, not inferred ones. |
| 107 | plan-authoring | append-new | Plan Authoring Checklist | never name specific tests, files, or values from session memory in plan body assertions — soften to count-or-shape predicates or copy verbatim from a fresh artifact read. |
| 114 | plan-authoring | append-new | Plan Authoring Checklist | strict Bellows convention strings (header fields, dispatch modes, directory names) must be copied verbatim from a known-good artifact, never authored from memory. |
| 116 | plan-authoring | append-new | Plan Authoring Checklist | mechanize dispatch-mode validation by copying the field from a known-good Done/ artifact or running the validator, rather than relying on memory recall of allowed values. |
| 119 | plan-authoring | append-new | Plan Authoring Checklist | use strictly monotonic integer STEP header labels (1, 2, 3...) — Bellows step parser is positional; non-monotonic labels (2A, 2B) cause dispatch/prompt misalignment. |
| 121 | plan-authoring | MERGE w/103 | Plan Authoring Checklist | inline target file paths in DEV step bodies rather than delegating to a referenced blueprint — scope_check cannot follow cross-step blueprint references. |
| 100 | bellows-workaround | MERGE w/108 -> strengthen WA#8 | Bellows Operational Workarounds | defer ALL working-tree edits (source, blueprints, knowledge deposits) until no plan is in-flight for that project. |
| 108 | bellows-workaround | MERGE w/100 -> strengthen WA#8 | Bellows Operational Workarounds | Strengthen existing PLANNER_TEMPLATE.md rule on no-writes-during-dispatch: quantify recovery cost (~5-10 min per dirty-tree cycle) and extend to all project directory writes, not just source edits. |
| 104 | bellows-workaround | RECONCILE vs v4.57 Rule 25 | Bellows Operational Workarounds / Rule 25 | read the verdict-request Gate Result JSON and Pause Reason Code before issuing any verdict — the terminal log line predates teardown and misses post-log failures. |
| 105 | bellows-workaround | append-new (relates to dirty-tree LESSONS 2026-05-29) | Bellows Operational Workarounds | keep watched repo roots clean of uncommitted non-lifecycle files between plans; commit or remove stray files before depositing new plans. |
| 110 | bellows-workaround | RECONCILE vs WA#5 + verdict-cycle text | Bellows Operational Workarounds | always write verdict response files to verdicts/resolved/ — no other directory is consumed by Bellows. |
| 113 | recovery | MERGE w/115 -> strengthen WA#12 + Rule 25 | Bellows Operational Workarounds / Rule 25 | document R2 Planner-direct close as the standard recovery shape for 'substance shipped, teardown cherry-pick conflicts on lifecycle artifacts' — two sessions confirm the pattern is mechanical and reliable. |
| 115 | recovery | MERGE w/113 -> strengthen WA#12 + Rule 25 | Bellows Operational Workarounds / Rule 25 | document the agent claim-rename variant where the cherry-pick conflict is on the agent's own in-progress- rename rather than a Planner edit. |
| 101 | qa/testing | append-new | Quality Standards / QA discipline | substance-check feature assertions individually via Rule 22; never accept a full-suite pass-count headline as independent verification. |
| 102 | qa/testing | append-new (reconcile vs v4.56 Rule 21) | Quality Standards / QA discipline | use a wall-clock bound external to pytest (shell timeout) plus --collect-only for collection-time isolation; pytest --timeout=N only bounds per-test execution. |
| 111 | qa/testing | append-new (Rule 22(d) override) | near Rule 22 / Bellows Operational Workarounds | scope_check false-positives on collectively-referenced evidence files in plan Deposits blocks warrant Planner override per Rule 22(d). |
| 120 | SA | append-new | Orchestration Plan Rules (new rule) or SA-discipline | blueprints that add a value to a recognized-set must verify all downstream consumers (branches, validators, lookup functions) handle the new value. |
| 118 | gate-1 routing meta | append-new | Lessons Forge / Gate 1 routing section | reject medium-confidence proposals flagged as 'Planner-side workaround for daemon bug' and route the underlying bug to Bellows BACKLOG rather than codifying workarounds as governance. |

**Net distinct rules after the 3 locked merges: 16.**

**Two narratives to archive (verbatim from `lessons-forge.db`):**

| ID | Heading | suggested_action (verbatim) | Why archived (from reasoning) |
|---|---|---|---|
| 109 | Wall-clock calibration — small-tier approximates medium-tier | Archive as context — wall-clock calibration data showing small-tier executables with comprehensive test coverage run closer to medium-tier (~72 min agent runtime). | Observational timing data (Diag S1 11m51s; Exec S1 40m28s; Exec S2 20m06s; ~72 min total). Implies re-tiering but prescribes no concrete governance change. |
| 117 | Verdict filename prefix tolerance | Archive as context — Bellows tolerates verdict-response filenames with unstripped diagnostic-/executable- prefixes despite README specifying prefix strip; documentation drift between spec and implementation. | Both prefixed verdict files consumed correctly; plans auto-moved to Done/. Documentation drift (README vs implementation), no PLANNER_TEMPLATE action proposed. |

---

## Execution Map

Step 1 (SA) -> [verdict pause] -> Step 2 (DEV) -> [verdict pause] -> Step 3 (QA)

Sequential. No parallel lanes. Single project (governance root PLANNER_TEMPLATE.md + lessons-forge knowledge deposits). DEV edits after SA blueprint is verdict-approved. QA verifies after DEV is verdict-approved.

---

## How to Run This Plan

Bellows-dispatched. After deposit to `lessons-forge/knowledge/decisions/`, Bellows claims and dispatches Step 1 automatically. `pause_for_verdict: always` produces a verdict request after each step; Planner verifies per Rule 22 and issues continue/stop verdicts to `bellows/verdicts/resolved/`.

---

## STEP 1 — Forge Developer (SA role)

**Role:** Systems Analyst / Architect

**Reads:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.58 — the dedup baseline)
- `/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-06-03.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/classifications-summary-2026-06-03.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/executable-planner-template-bellows-operational-workarounds-2026-05-27.md` AND `Done/halted-but-shipped-executable-planner-template-plan-authoring-checklist-2026-05-27.md` (prior-cycle precedent for footer convention, entry prose style, heading depth)
- This plan file (Context section: the 19-proposal table, locked CEO decisions, 2 narratives)
- `lessons-forge.db` — read the `reasoning` column for any proposal whose `suggested_action` (in the table above) is insufficient to author the rule body. `SELECT id, suggested_action, reasoning FROM lesson_proposals WHERE id BETWEEN 99 AND 121 AND status='accepted';`

**Task:**

Author one SA blueprint that resolves dedup + consolidation + placement for all 16 distinct rules and specifies the narrative archive. Deduplicate every proposal against the live v4.58 file (decision 1) before assigning a disposition.

Produce, in a single blueprint deposit file, for EACH of the 16 distinct rules:

1. **Disposition** — one of: APPEND-NEW (no existing equivalent), STRENGTHEN-EXISTING (edit an existing rule/checklist-item/workaround in place), or SUPERSEDE (replace existing text). State the disposition and, for STRENGTHEN/SUPERSEDE, the exact existing target (section + current heading + line range in v4.58) and a unified before/after of the prose.

2. **Section home + heading** — for APPEND-NEW: the section, the next available number, and the sentence-case working title matching existing entry style (Plan Authoring Checklist entries are `### N. Title`; Bellows Operational Workarounds entries are `#### N. Title`).

3. **Rule body** — the exact prose DEV will write (single paragraph or short structured block; mechanical and actionable; match the prose register of existing entries). Include the source-attribution footer `Source: proposal N, lesson 2026-06-03` (for merged rules: `Source: proposals N and M, lesson 2026-06-03`).

**Binding constraints (do NOT re-litigate):**
- The three merges (100+108, 113+115, 103+121) are locked. Each ships as ONE rule.
- 100+108 STRENGTHENS Bellows Operational Workaround #8. 108's ~5-10 min recovery-cost figure must appear.
- 113+115 must RECONCILE against BOTH Workaround #12 and Rule 25's v4.57 teardown-variant discrimination block (~L709-711). Resolve the relationship explicitly — do not author text that duplicates or contradicts the existing v4.57 discrimination. If the existing text already covers a variant, cross-reference rather than restate.
- 104 must RECONCILE against the same v4.57 Rule 25 block: distinguish what 104 adds (read Gate Result JSON + Pause Reason Code before any verdict; the terminal log line predates teardown) from what v4.57 already says (evidence-string leading-token discrimination). If 104 is fully subsumed, say so and flag for CEO rather than adding a redundant rule.
- 110 must be checked against Workaround #5 (verdict-response filename matching) and the verdict-cycle resolved/ text (~L1120). Fold in or cross-reference; do not add a free-floating duplicate.
- 102 must be checked against v4.56 Rule 21 (test-count right-sizing) and v4.58 Rule 21 (output-mode) — 102 is about wall-clock bounding + --collect-only, adjacent but distinct; confirm no contradiction.

**Also specify:**
4. **Narrative archive blueprint** — the full text of the new `lessons-forge/knowledge/archived-narratives-2026-06-03.md` (title, intro paragraph mirroring the 05-27 file, and the two `## Proposal N — <heading>` blocks for 109 and 117 with Source lesson / Why archived / Suggested action verbatim).

5. **Per-edit anchor map for DEV** — for every insertion and in-place edit, the exact v4.58 anchor lines (line-before / line-after, or the verbatim old_string for in-place edits) DEV will match against, plus expected net line delta.

**Liveness anchors (Rule 41 — this prompt is >400w):** emit a one-line claim-confirmation BEFORE your first read; a one-line acknowledgment after each file read; and a one-line section marker at the start of each blueprint section (dedup pass, per-rule dispositions, narrative archive, anchor map).

**Deposits:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-03.md`

**Output Receipt fields required:**
- What was done (summary)
- Files deposited (the blueprint file path)
- Decisions made (final disposition per rule; final count of APPEND-NEW vs STRENGTHEN vs SUPERSEDE; how 104/113/115/110 reconciled against v4.57/existing text)
- Flags for CEO (any proposal found fully subsumed by existing text and recommended for status='implemented' with no edit; any dedup judgment that changes the 16-rule count)
- Flags for Next Step (DEV anchor map confirmed; any in-place edits needing exact-string care)

---

## STEP 2 — Forge Developer (DEV role)

**Role:** Developer

**Reads:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-03.md` (Step 1 blueprint — source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.58 — verify SA anchors before editing)

**Task:**

Apply the SA blueprint to `PLANNER_TEMPLATE.md` (insertions + in-place strengthen/supersede edits per the blueprint's disposition for each rule), and create the narrative archive file.

**Pre-edit verification (per blueprint anchor map):**
1. For every APPEND-NEW insertion: grep the SA-cited line-before / line-after anchors; confirm both exist verbatim at the cited lines.
2. For every STRENGTHEN/SUPERSEDE in-place edit: confirm the SA-cited `old_string` exists verbatim and EXACTLY ONCE in the file (these edits modify existing text — exact-match is mandatory; em-dashes, smart quotes, whitespace must match).
3. Confirm `**Version:** 4.58` at line 5 is unchanged (no version bump in this step — decision 5).
4. If ANY anchor or old_string fails to match: set Output Receipt status to `Partial`, populate **Flags for CEO** with the mismatch evidence, edit NOTHING in PLANNER_TEMPLATE.md, and end the step. Bellows trips the receipt gate and pauses for Planner verdict.

**Edits:**
- Apply each rule per its blueprint disposition. APPEND-NEW items insert at the specified section position with the specified heading depth (Plan Authoring Checklist = `### N.`; Bellows Operational Workarounds = `#### N.`). STRENGTHEN/SUPERSEDE items replace the cited old_string with the blueprint's new text.
- Renumber within a section ONLY if the blueprint specifies it (e.g., new Authoring Checklist items 13+). Do not renumber Orchestration Plan Rules (1-44) unless the blueprint adds a numbered rule there and specifies the number.
- Every new/strengthened rule carries its `Source: proposal(s) N, lesson 2026-06-03` footer.

**Narrative archive:**
- Create `lessons-forge/knowledge/archived-narratives-2026-06-03.md` with the exact content from the blueprint's narrative-archive section. New file (do NOT append to the 05-27 file).

**No version bump.** `**Version:**` stays 4.58. Session-wrap handles the bump to 4.59.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (modified — insertions + in-place edits)
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-06-03.md` (new)

**Output Receipt fields required:**
- What was done (summary; per-section line ranges touched; insertion vs in-place-edit counts)
- Files deposited (both paths above)
- Lines added / lines changed (counts)
- Pre-edit verification results (anchor + old_string match confirmations)
- Flags for CEO (any blueprint-vs-file mismatch caught; any prose adjustment made for line-fit)
- Flags for Next Step (QA evidence — exact inserted/changed byte ranges per rule for verbatim-match verification)

---

## STEP 3 — Forge Developer (QA role)

**Role:** Quality Assurance

**Reads:**
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-03.md` (blueprint — source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (Step 2 deposit, modified)
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-06-03.md` (Step 2 deposit, new)
- `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (canonical Rule 20 self-check Python block)

**Task:** Verify Step 2 against the Step 1 blueprint. Each check produces a PASS/FAIL row with line citations.

**Verification checks:**
1. **Per-rule verbatim match.** For each of the 16 distinct rules, the modified file contains the blueprint's prescribed text at the blueprint's prescribed location, with the correct heading depth and the `Source: ... lesson 2026-06-03` footer. One PASS/FAIL row per rule.
2. **In-place edits correct.** For each STRENGTHEN/SUPERSEDE rule, the OLD text is gone and the NEW text is present (cite before/after line ranges). For 100+108: the ~5-10 min recovery-cost figure is present in the strengthened Workaround #8.
3. **No-duplication on reconciled rules.** 104, 113, 115, 110 did NOT introduce text that duplicates the existing v4.57 Rule 25 teardown-variant block (~L709-711) or Workarounds #5/#12. Confirm the reconciliation matches the blueprint (cross-reference vs restate).
4. **Merge count.** Exactly 16 distinct rules present (the three merged pairs each appear once). No proposal appears as two separate rules.
5. **Narrative archive.** `archived-narratives-2026-06-03.md` exists, mirrors the 05-27 file structure, and contains both proposal 109 and 117 blocks with verbatim suggested_action text. The 05-27 file is unmodified.
6. **No collateral disturbance.** `git diff` on PLANNER_TEMPLATE.md shows only the blueprint-specified insertion/edit ranges; no content outside those ranges is altered. Cite the diff hunk summary.
7. **Version field unchanged.** `**Version:** 4.58` at line 5 is unchanged.
8. **Rule 20 canonical self-check.** Author the canonical QA self-check Python block per Rule 20 from `RULE_20_SELF_CHECK_BLOCK.md` with placeholders filled. Required-evidence-files for this governance-edit plan is empty (only deposit is this QA report); pass `evidence_dir=/tmp/empty-evidence-dir/` (create if needed) and `required_evidence_files=[]`. Run via `python3`; capture stdout under a section titled "Rule 20 Self-Check (canonical Python block, stdout)". The PASSED banner line MUST appear byte-identically — do NOT paraphrase, substitute, or omit.

**Deposits:**
- `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-06-03.md`

**Output Receipt fields required:**
- What was done (PASS/FAIL counts per check)
- Files deposited (the QA report path)
- Decisions made (any QA judgment calls; should be none for verbatim work)
- Flags for CEO (any FAIL row with evidence; any Rule 20 block discrepancy)
- Flags for Next Step (none — Step 3 is terminal)

---

## End-of-Plan Housekeeping (Planner-side, post-QA-verdict)

After QA continue verdict and Rule 22 pass:

1. **Bellows owns the terminal Done/ move** on continue-verdict consumption (recovery path: Planner-direct `Filesystem:move_file` only if daemon is not running). Do NOT pre-rename.

2. **Split-commit pattern** (caution #1 — this plan edits a file OUTSIDE the lessons-forge submodule):
   - **Governance repo** (`/Users/marklehn/Developer/GitHub/`): commit the PLANNER_TEMPLATE.md edit. `git add PLANNER_TEMPLATE.md`.
   - **lessons-forge submodule**: commit the plan housekeeping — SA blueprint, QA report, new `archived-narratives-2026-06-03.md`, and the consumed plan-lifecycle artifacts (Done/ move, verdict files). `cd lessons-forge && git add knowledge/research/gate-2-codification-blueprint-2026-06-03.md knowledge/qa/gate-2-codification-qa-2026-06-03.md knowledge/archived-narratives-2026-06-03.md knowledge/decisions/Done/`.
   - Each repo: `git fetch origin && git pull --rebase origin main && git push origin main`. Agents do NOT push; Planner pushes at wrap.

3. **Submodule pointer bump:** after the lessons-forge push, `cd` to governance root, `git submodule status` (expect `+` prefix on lessons-forge). If dirty: `git add lessons-forge && git commit -m "chore: bump lessons-forge submodule" && git push origin main`.

4. **Gate 2d status advancement (DB):** advance the 19 codified `governance_rule` proposals AND the 2 archived `narrative` proposals to `status='implemented'`:
   `UPDATE lesson_proposals SET status='implemented', status_updated_at='2026-06-03', status_updated_by='planner' WHERE id IN (99,100,101,102,103,104,105,107,108,109,110,111,113,114,115,116,117,118,119,120,121);`
   (21 rows: 19 governance_rule + 2 narrative. The 2 rejected — 106, 112 — stay `rejected`.) NOTE: if SA's Step 1 dedup flags any proposal as fully subsumed (implemented with no edit), it is still advanced to `implemented` here.

5. **Version bump:** PLANNER_TEMPLATE.md `**Version:**` 4.58 -> 4.59, `**Last Updated:** 2026-06-03 (v4.59)`, Planner-direct write at session-wrap. Add a Lessons row documenting the 2026-06-03 Gate 2 ratification. Commit on the governance repo (folds into step 2's governance commit if done before push).

6. **NEXT_SESSION baton:** update `lessons-forge/NEXT_SESSION.md` — clear the Gate 2 in-flight thread; mark the 2026-06-03 cycle closed through Gate 2d. Update shop-level `shop_next_session.md` if any shop-meta carries.

7. **Horizon (not this plan):** Bellows teardown Gap 3 (dirty-tree auto-stash); invoice-pulse T0.5.1 reconciliation; email-PRO->assigned-user (gated on the two Windows prod-DB queries in `email-pro-user-lookup-prod-queries-2026-06-03.sql`).
