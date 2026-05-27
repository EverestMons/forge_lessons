# Executable: PLANNER_TEMPLATE — Bellows Operational Workarounds subsection

**Plan slug:** executable-planner-template-bellows-operational-workarounds-2026-05-27
**Plan type:** executable
**Project:** governance (root, /Users/marklehn/Developer/GitHub/)
**Specialist:** Forge Developer (SA, DEV, QA roles all use FORGE_LESSONS_AGENT.md as project context anchor; this plan edits governance-root PLANNER_TEMPLATE.md so SA/DEV/QA also read PLANNER_TEMPLATE.md fully)
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-27
**qa_steps:** 3

---

## Context

Plan A is the second half of the 2026-05-27 Gate 1 Phase 2B work. Plan B (Plan Authoring Checklist + residual scatter) shipped earlier this session — `Done/halted-but-shipped-executable-planner-template-plan-authoring-checklist-2026-05-27.md`. Plan A ships the **Bellows Operational Workarounds** subsection — a new `### ` subsection under `## Bellows Execution Model` (line 1035) collecting workaround rules cross-referenced to Bellows BACKLOG entries where applicable. Framed as deprecatable wholesale when daemon fixes ship.

The two plans complete the Phase 2B structural cluster work for the 2026-05-27 cycle (Plan A = 14 rules in scope target; Plan B already shipped). Residual status advancement of all 33 accepted proposals to `status='implemented'` deferred to a Gate 2d-style housekeeping session after both ship.

**Locked CEO decisions (pre-blueprint, this session):**
1. Subsection placement: new `### Bellows Operational Workarounds` subsection under `## Bellows Execution Model` (line 1035), placed as the final subsection of that section — after `### Restart Discipline` (line 1151) and before the `---` separator preceding `## Manual Execution Model` (line 1161). Peer to existing Bellows subsections; daemon-specific scope.
2. Cross-reference format (each workaround rule footer, when a corresponding BACKLOG entry exists): `Workaround for: bellows/knowledge/BACKLOG.md "<entry title>" (added YYYY-MM-DD)`. When no BACKLOG entry exists for the workaround's underlying daemon behavior, the rule omits the cross-reference footer entirely — do not author placeholder backlog entries. Each rule also keeps its lessons-forge source attribution footer (`Source: proposal N, lesson 2026-05-27`) matching the existing Plan Authoring Checklist precedent.
3. Subsection numbering: independent scope (Workaround 1–N), matching Plan B's Plan Authoring Checklist precedent of independent 1-12 numbering. NOT continuous with Orchestration Plan Rules (which run 1–44). Independent numbering signals deprecate-wholesale semantics — when daemon fixes ship for the underlying bugs, individual workarounds retire and renumbering within the subsection has no spillover to Orchestration Plan Rules.

**Source proposals (all currently `status='accepted'`, `status_updated_at='2026-05-27'` in `lessons-forge.db`):**

13 candidates for the new `### Bellows Operational Workarounds` subsection:

| Proposal ID | Suggested action (verbatim from lessons-forge.db `suggested_action`) |
|---|---|
| 65 | Add PLANNER_TEMPLATE.md methodology rule: when analyzing bellows/logs/*.json, use parsed.permission_denials (structured JSON), not grep/substring-match against raw_output. raw_output contains tool-registry echoes producing false positives. |
| 68 | Add PLANNER_TEMPLATE.md dispatch rule: serialize same-project plans by default. Parallel dispatch is only safe when plans target different git roots or one plan does not write to PROJECT_STATUS/feedback log. |
| 70 | Add PLANNER_TEMPLATE.md filesystem-ownership rule: Planner's safe rename destinations are Done/<canonical>, halted-<canonical>, obsolete-<canonical>, and _staging_*. Never rename through verdict-pending-* or other daemon-watched prefixes. |
| 71 | Add PLANNER_TEMPLATE.md daemon-fix checklist: when a fix plan changes daemon code running every rescan cycle, in-plan filesystem migrations against files the old code touches are ineffective until restart. Choose: post-restart manual action, daemon-pause, or self-healing convergence. |
| 73 | Add PLANNER_TEMPLATE.md worktree-safety rule: before any file edit under a project path, check .bellows-worktrees/ for active worktrees on the in-flight plan. If active, use verdict-channel addendum instead of direct file edit. |
| 74 | Add PLANNER_TEMPLATE.md mid-plan communication rule: CEO addenda during plan execution flow downstream via verdict reasoning text, not upstream via blueprint file edits. Blueprints are fixed after dispatch. |
| 77 | Add PLANNER_TEMPLATE.md worktree-recovery rule: before authoring recovery commits for teardown gate_failure, run git fetch origin and check if the agent's work already landed on origin via worktree push. |
| 78 | Add PLANNER_TEMPLATE.md session-start rule: run git fetch origin && git status. If local/origin have diverged with empty diffs on all parallel pairs, resolve via git reset --hard origin/main. |
| 81 | Add verdict-response filename discipline rule to PLANNER_TEMPLATE.md: copy request filename replacing `verdict-request-` with `verdict-`, no suffixes; pre-check resolved/ for colliding processed-verdict files. |
| 82 | Add three worktree lifecycle rules to PLANNER_TEMPLATE.md: (A) operator pre-flight stale worktree prune, (B) halt on second consecutive teardown-empty for same step, (C) recognize daemon-restart fresh-claim state and stop rather than continue. |
| 85 | Add rule to PLANNER_TEMPLATE.md: verdict-time overrides must target documents the next agent reads fresh (UXD design, DEV log, research file), not the cached plan file; Bellows caches plan content at claim-time. |
| 89 | Add final-step gate_failure recovery checklist to PLANNER_TEMPLATE.md: (1) verify substance shipped, (2) issue `verdict: stop`, (3) move in-progress to Done/halted-but-shipped, (4) archive verdict files, (5) note in PROJECT_STATUS. |
| 94 | Add rule to PLANNER_TEMPLATE.md: `pause_for_verdict` must be exactly one of `always`, `after_step_1`, or `after_qa_step`; any other value silently becomes no-pause. |

**Fold-in context for SA:** proposal 74 was demoted from Plan B scope per Plan B's Step 1 SA decision because its concern ("mid-plan communication via verdict reasoning text, not blueprint file edits") overlaps proposal 85's claim-time caching workaround scope ("verdict-time overrides must target documents the next agent reads fresh, not the cached plan file"). Both proposals address how information flows during Bellows-dispatched execution given the claim-time cache constraint. The two are joint-authoring candidates: SA decides during blueprint whether they ship as one combined workaround (with both shapes — what to communicate AND where it lands) or as two adjacent workarounds. No CEO decision required on the join shape; SA picks the cleaner authoring path.

**Rule-count breakdown for SA:** baseline is 13 proposals. Proposal 82 explicitly contains three sub-rules (A/B/C worktree lifecycle); SA decides whether it ships as 1 numbered workaround with three sub-points OR as 3 separate adjacent numbered workarounds. Proposal 74+85 join shape (see above) is a separate independent decision. Final subsection count emerges from those two SA decisions and lands somewhere in the range 13–16 workarounds. Headline target articulated in NEXT_SESSION.md ("14 rules") is informational, not binding — SA's blueprint sets the actual count.

**BACKLOG cross-reference mapping (informational for SA — confirm during blueprint):**

| Proposal | Maps to BACKLOG entry? |
|---|---|
| 65 | No — defensive analysis technique, not a daemon bug |
| 68 | Yes — "Parallel-diagnostic cherry-pick conflicts on shared bookkeeping files at teardown" (added 2026-05-22) |
| 70 | No — daemon-watched filename-prefix semantics, no daemon-side fix candidate |
| 71 | No — restart-discipline cost documented in PLANNER_TEMPLATE Bellows Execution Model `### Restart Discipline` |
| 73 | No — worktree-active-during-edit; no daemon-side fix filed |
| 74 | No — claim-time cache is a daemon design choice, joint with 85 |
| 77 | Loosely related — "Worktree teardown cherry-pick conflict on dirty PROJECT_STATUS.md" (added 2026-05-22). SA decides if cross-ref is accurate enough to cite, or omit footer |
| 78 | No — origin/local divergence symptom on local recovery, not a daemon bug |
| 81 | No — verdict filename discipline, daemon-side parser is correct as-built |
| 82 | No — worktree lifecycle awareness, no daemon-side prune scheduled |
| 85 | No — claim-time cache is the daemon's design contract (Bellows DOES NOT re-read plan content mid-execution) |
| 89 | No — final-step gate_failure recovery flow; the gate-failure pause itself is correct behavior |
| 94 | No — silent-no-pause-on-invalid-value is daemon parser permissiveness, no fix filed |

Only proposals 68 and (loosely) 77 map cleanly to existing BACKLOG entries. SA verifies mapping during blueprint authoring (Step 1) — direct read of `/Users/marklehn/Developer/GitHub/bellows/knowledge/BACKLOG.md` Open section is mandatory. If SA identifies additional matches not listed above, those are valid cross-references; if SA disagrees with a mapping listed here, SA's mapping is authoritative. Do not invent BACKLOG entries — omit the footer when no entry exists.

---

## Execution Map

Step 1 (SA) → [verdict pause] → Step 2 (DEV) → [verdict pause] → Step 3 (QA)

Sequential. No parallel lanes. Single project (governance root PLANNER_TEMPLATE.md). DEV writes after SA blueprint is verdict-approved. QA verifies after DEV is verdict-approved.

---

## How to Run This Plan

Bellows-dispatched. After deposit to `lessons-forge/knowledge/decisions/`, Bellows claims and dispatches Step 1 automatically. `pause_for_verdict: always` produces verdict requests after each step; Planner verifies per Rule 22 and issues continue/stop verdicts.

---

## STEP 1 — Forge Developer (SA role)

**Role:** Systems Analyst / Architect
**Reads:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.54)
- `/Users/marklehn/Developer/GitHub/bellows/knowledge/BACKLOG.md` (Open section)
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/halted-but-shipped-executable-planner-template-plan-authoring-checklist-2026-05-27.md` (Plan B — same-day precedent for subsection authoring shape and footer convention)
- This plan file (context section above + the 13 proposals table + the locked CEO decisions)

**Task:**

Author a SA blueprint for the new `### Bellows Operational Workarounds` subsection under `## Bellows Execution Model` (line 1035 of PLANNER_TEMPLATE.md).

Produce, in a single blueprint deposit file:

1. **Subsection header text.** Exact `### `-level heading and the introductory paragraph(s) explaining what the subsection contains, the deprecate-wholesale framing, and the independent-numbering convention. Match the tone and length of the existing Plan Authoring Checklist intro at PLANNER_TEMPLATE.md line 917–921.

2. **Final rule-count breakdown.** Resolve the two SA decisions:
   - Proposal 82 split: 1 numbered workaround with three labelled sub-points, OR 3 separate numbered workarounds. State the decision and the reasoning.
   - Proposal 74+85 join: single combined workaround covering both shapes, OR two adjacent workarounds. State the decision and the reasoning.
   - Final subsection numbering count (13, 14, 15, or 16 depending on the two decisions above).

3. **Per-workaround blueprint.** For each numbered workaround, produce:
   - Working title (sentence-case, descriptive — match the title style of existing Plan Authoring Checklist entries at PLANNER_TEMPLATE.md lines 923, 929, 935, 941 etc.)
   - The proposal-text shape that becomes the rule body (single paragraph; mechanical and actionable; matches the prose style of the existing Plan Authoring Checklist entries)
   - The cross-reference footer line if a BACKLOG entry maps (format: `Workaround for: bellows/knowledge/BACKLOG.md "<exact entry title>" (added YYYY-MM-DD)`). Omit if no map.
   - The source attribution footer (format: `Source: proposal N, lesson 2026-05-27`). For combined workarounds covering multiple proposals (e.g., 74+85 joint), list both: `Source: proposals 74 and 85, lesson 2026-05-27`.

4. **Insertion-point specification.** Exact line number in PLANNER_TEMPLATE.md v4.54 where the new subsection starts (final subsection of `## Bellows Execution Model`, immediately after `### Restart Discipline` ends). State the surrounding-context lines (line before and line after) DEV will anchor on.

5. **BACKLOG verification.** Read `bellows/knowledge/BACKLOG.md` Open section directly. Confirm or correct the mapping table in the Context section of this plan. Cite exact entry titles and `added YYYY-MM-DD` dates from the BACKLOG file. If a proposal not flagged in the mapping table turns out to have a BACKLOG match, add it. If a flagged mapping turns out to be wrong, remove it.

**Anchor reference:** Plan B's blueprint at `lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` is the structural precedent for this blueprint's shape. Match its level of detail and section structure.

**Deposits:**
- `lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md`

**Output Receipt fields required:**
- What was done (summary)
- Files deposited (the blueprint file path)
- Decisions made (proposal 82 split decision + proposal 74+85 join decision + final rule count)
- Flags for CEO (any BACKLOG mapping corrections, any SA-discovered concerns)
- Flags for Next Step (DEV anchor lines confirmed; any prose-style adjustments DEV should adopt)

---

## STEP 2 — Forge Developer (DEV role)

**Role:** Developer
**Reads:**
- `lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md` (Step 1 blueprint, source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (full file, current v4.54 — to verify the SA-cited insertion-point lines match before editing)

**Task:**

Apply the SA blueprint to `PLANNER_TEMPLATE.md`. Insert the new `### Bellows Operational Workarounds` subsection at the SA-specified location (final subsection of `## Bellows Execution Model`, after `### Restart Discipline`).

**Pre-edit verification:**
1. Open PLANNER_TEMPLATE.md and grep for the SA-cited anchor lines (the line before insertion point and the line after). Confirm both exist verbatim in the current file at the SA-cited line numbers.
2. Confirm the version field at the top of PLANNER_TEMPLATE.md still reads `**Version:** 4.54` (no version bump in this plan — version bump happens at session-wrap, not in DEV step).
3. If anchors don't match, set the Output Receipt status to `Partial`, populate the **Flags for CEO** field with the mismatched-anchor evidence, and end the step without editing PLANNER_TEMPLATE.md. Bellows will trip the receipt_status gate and pause for Planner verdict.

**Edit:**
Insert the new subsection at the verified location. Format:

```
### Bellows Operational Workarounds

[Intro paragraph(s) from SA blueprint — explains subsection purpose, deprecate-wholesale framing, independent-numbering convention]

#### 1. [Working title from SA blueprint]

[Rule body paragraph from SA blueprint]

[Cross-reference footer if applicable, blank line, then source attribution footer]

#### 2. [Working title from SA blueprint]

[...]
```

If SA chose `### `-level (not `#### `-level) for individual workarounds to match the Plan Authoring Checklist precedent, use SA's choice. Mirror Plan B's heading-level choice precisely — read `PLANNER_TEMPLATE.md` lines 923, 929, 935 to confirm the precedent's heading depth and replicate it.

**No version bump in this step.** PLANNER_TEMPLATE.md `**Version:**` line stays at 4.54. Session-wrap is the appropriate version-bump moment.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (modified — net-additive subsection insertion)

**Output Receipt fields required:**
- What was done (summary including insertion line range)
- Files deposited (the modified PLANNER_TEMPLATE.md path)
- Lines added (count)
- Pre-edit verification results (anchor match confirmation)
- Flags for CEO (any blueprint-vs-file mismatches caught during pre-edit; any prose adjustments made for line-fit)
- Flags for Next Step (QA evidence — full inserted-text byte range for verbatim-match verification)

---

## STEP 3 — Forge Developer (QA role)

**Role:** Quality Assurance
**Reads:**
- `lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md` (Step 1 blueprint, source of truth)
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (Step 2 deposit, modified file)
- `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (canonical Rule 20 self-check Python block)

**Task:**

Verify Step 2's insertion against the Step 1 blueprint. Each verification check produces a PASS/FAIL row.

**Verification checks:**

1. **Subsection placement.** The new `### Bellows Operational Workarounds` subsection appears as the final subsection of `## Bellows Execution Model`, immediately after `### Restart Discipline` ends and before the `---` separator preceding `## Manual Execution Model`. Cite exact line numbers in the modified file.

2. **Subsection-header verbatim match.** The `### Bellows Operational Workarounds` heading text and the introductory paragraph(s) match the SA blueprint's prescribed text byte-for-byte. Cite blueprint section reference + modified-file line range.

3. **Per-workaround verbatim match.** For each numbered workaround the SA blueprint specifies, the modified PLANNER_TEMPLATE.md contains: (a) the working title at the correct heading level, (b) the rule body paragraph, (c) the cross-reference footer (if SA specified one), (d) the source attribution footer. Produce one PASS/FAIL row PER workaround with line citations.

4. **Workaround count.** The number of numbered workarounds in the inserted subsection matches SA's specified count (the resolved 13/14/15/16 from SA's proposal 82 split + proposal 74+85 join decisions).

5. **Cross-reference footer accuracy.** For each workaround that has a cross-reference footer, the cited BACKLOG entry title and `(added YYYY-MM-DD)` date match `bellows/knowledge/BACKLOG.md` Open section verbatim. Cite the BACKLOG line numbers.

6. **No source-attribution footer missing.** Every workaround has a `Source: proposal N, lesson 2026-05-27` (or multi-proposal variant) footer.

7. **No surrounding content disturbed.** Lines BEFORE the insertion point are byte-identical to PLANNER_TEMPLATE.md v4.54 pre-edit state. Lines AFTER the insertion point are byte-identical to PLANNER_TEMPLATE.md v4.54 pre-edit state (offset by the inserted-line count, but identical content otherwise). Verify via `git diff` showing only additions, zero deletions, zero modifications outside the insertion range.

8. **Version field unchanged.** `**Version:** 4.54` at PLANNER_TEMPLATE.md line 5 is unchanged. No version bump occurred in this plan.

9. **Heading-level consistency with Plan Authoring Checklist precedent.** Individual workaround headings use the SAME heading depth as the Plan Authoring Checklist entries (PLANNER_TEMPLATE.md lines 923, 929, 935). If Checklist entries are `### `, workarounds are `### `. If Checklist entries are `#### `, workarounds are `#### `. Cite both heading depths.

10. **Rule 20 canonical self-check.** Author the canonical QA self-check Python block per Rule 20 using `RULE_20_SELF_CHECK_BLOCK.md` with placeholders filled. Run the block via `python3` and capture stdout in the QA report under a section titled "Rule 20 Self-Check (canonical Python block, stdout)". Required-evidence-files for this governance-edit plan is an empty list (the only deposit is the QA report itself — no separate evidence directory required); pass `evidence_dir=/tmp/empty-evidence-dir/` (create empty directory if needed) and `required_evidence_files=[]`. The block's PASSED banner line MUST appear byte-identically in the QA report — do NOT paraphrase, do NOT substitute, do NOT omit.

**Deposits:**
- `lessons-forge/knowledge/qa/bellows-operational-workarounds-qa-2026-05-27.md`

**Output Receipt fields required:**
- What was done (summary including count of PASS/FAIL per check)
- Files deposited (the QA report path)
- Decisions made (any QA-side judgment calls; should be none for verbatim-match work)
- Flags for CEO (any FAIL row with evidence; any Rule 20 block discrepancy)
- Flags for Next Step (none — Step 3 is terminal)

---

## End-of-Plan Housekeeping (Planner-side, post-QA-verdict)

After QA continue verdict and Rule 22 pass:
1. Move this plan from `lessons-forge/knowledge/decisions/in-progress-*` to `lessons-forge/knowledge/decisions/Done/` via `Filesystem:move_file`. (Or via Bellows's terminal-step auto-move if `_consume_verdicts` reaches the final-step branch.)
2. Update `lessons-forge/PROJECT_STATUS.md` with a session entry summarizing what shipped (delegated to Forge Documentation agent via separate executable if a sync is needed; inline update via direct Planner write is also acceptable since `PROJECT_STATUS.md` is allowed-write under Rule 23 for plan-close housekeeping).
3. Update `lessons-forge/NEXT_SESSION.md`: clear the Plan A in-flight thread; surface the residual housekeeping (33 accepted proposals pending `status='implemented'` advancement — Gate 2d-style session).
4. Commit governance-root PLANNER_TEMPLATE.md change with submodule pointer bump for lessons-forge (covers SA blueprint + DEV edit + QA report).
5. Push all touched repos.
6. Bump PLANNER_TEMPLATE.md `**Version:**` to next minor (4.55) at session-wrap, as a separate Planner-direct write.
