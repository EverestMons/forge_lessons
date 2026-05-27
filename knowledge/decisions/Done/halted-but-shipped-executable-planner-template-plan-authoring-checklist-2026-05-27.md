# Executable: PLANNER_TEMPLATE — Plan Authoring Checklist + Residual Scatter

**Plan slug:** executable-planner-template-plan-authoring-checklist-2026-05-27
**Plan type:** executable
**Project:** governance (root, /Users/marklehn/Developer/GitHub/)
**Specialist:** Forge Developer (SA, DEV, QA roles all use FORGE_LESSONS_AGENT.md as project context anchor; this plan edits governance-root PLANNER_TEMPLATE.md so SA/DEV/QA also read PLANNER_TEMPLATE.md fully)
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-27

---

## Context

Lessons Forge cycle 2026-05-27 Gate 1 accepted 33 proposals from 36 (IDs 63–98). The accepted set splits into two structural clusters plus residual scatter. This plan ships **Plan B**: the new `## Plan Authoring Checklist` section (12 mechanical pre-deposit checks) plus 4 actionable residual rules scattered into existing PLANNER_TEMPLATE sections plus 3 narratives archived to a dated file in `lessons-forge/knowledge/`.

Plan A (Bellows Operational Workarounds subsection — 14 rules) ships as a separate plan in a subsequent session.

**Locked CEO decisions (pre-blueprint, this session):**
1. Checklist section placement: new top-level `## Plan Authoring Checklist` section between `## Orchestration Plan Rules` (ends ~line 901) and `## Guardrails` (line 903). Peer to Orchestration Plan Rules, not buried under Procedures.
2. 6-vs-4 actionable residual reconciliation: SA decides during blueprint authoring with a verdict pause before DEV writes. Targets: 4 actionable + 3 archived. Demotion candidates the SA must evaluate are proposals 72 (Phase 1.5 reinforcement; overlaps Rule 33) and 74 (mid-plan communication via verdict text; overlaps Plan A proposal 85). At least one must be demoted to archived or folded into Plan A's scope (deferred to Plan A's session, not shipped here).
3. Archived narratives destination: new dated file `lessons-forge/knowledge/archived-narratives-2026-05-27.md`. PLANNER_TEMPLATE carries no archive metadata.

**Source proposals (all currently `status='accepted'`, `status_updated_at='2026-05-27'` in `lessons-forge.db`):**

12 candidates for the new `## Plan Authoring Checklist` section (mechanical pre-deposit checks, gated by the moment between `Filesystem:write_file` to `_staging_*` and `Filesystem:move_file` to the watched directory):

| ID | One-line summary |
|---|---|
| 66 | All `**Deposits:**` blocks must use canonical multi-line bullet form (one path per `- ` line). Inline comma-separated form forbidden. |
| 67 | Before authoring a follow-up plan from a gate failure, read literal Files Changed list and match each entry against full path to disambiguate slug-sharing artifacts. |
| 69 | When a Bellows fix operates on files by filename pattern, enumerate all lifecycle stages producing that pattern and include a disambiguator if two or more stages match. |
| 75 | Every QA step prompt must include the exact canonical RULE_20_SELF_CHECK_BLOCK paragraph with four placeholders filled. No paraphrasing or "review the file" pointers. |
| 79 | Before depositing any `dispatch_mode: bellows` plan, scan for STOP-prose patterns (`**STOP.**`, "do not proceed", "halt and report") and strip them. `pause_for_verdict` does that work. |
| 80 | When a DEV step connects frontend to backend, specify exact field names and value enums from the backend handler, or instruct the agent to read the handler first. |
| 84 | Multi-step diagnostics needing per-step CEO review must use `pause_for_verdict: always` or split into separate single-step diagnostics. `after_step_1` is only for two-step plans. |
| 90 | QA-step Deposits blocks must declare exactly one `.md` file (the QA report). PROJECT_STATUS and other `.md` writes are side effects, not deposits. |
| 91 | Plans mechanizing a new authoritative data source must ship the governance edit obligating its population in the same session. Defer-to-follow-up is never acceptable. |
| 92 | When a plan changes a function's contract (return type, params, semantics), grep all test files for function references before declaring targeted scope. Bump to full-suite if multi-file coverage. |
| 95 | All agent deposits must use Rule 26 `**Deposits:**` block format with backtick-quoted paths. Inline prose alternatives silently fail parser registration. |
| 98 | Plans shipping schema migrations must include explicit `init_db` run against production DB with PRAGMA verification and commit of modified DB file. |

7 residual proposals (4 actionable, 3 archived narratives — final allocation is SA's call per Decision 2):

| ID | Type | Target | One-line summary |
|---|---|---|---|
| 72 | actionable OR archived | Phase 1.5 / archive (SA decides) | When CEO opening message is substantive, acknowledge briefly and complete Phase 1.5 reads before any investigation. |
| 74 | actionable OR Plan-A-fold | new "Mid-Plan Communication" rule under Orchestration Plan Rules (SA decides) | CEO addenda during plan execution flow downstream via verdict reasoning text, not upstream via blueprint file edits. Blueprints are fixed after dispatch. |
| 76 | actionable | Diagnostic Prompt Engineering subsection | Before asserting timing/ordering claims about Bellows code paths, grep `knowledge/research/` for the most recent ordering audit and verify against it. |
| 83 | actionable | new BACKLOG-authoring rule under Orchestration Plan Rules | When mechanizing a previously-manual check via Rule 25-style routing, scan open BACKLOG entries for defers whose rationale depends on the manual fallback. Re-evaluate each affected defer. |
| 96 | actionable | new baton-authoring rule under Orchestration Plan Rules | Every "On the horizon" item carried from a prior baton must be cross-checked against PROJECT_STATUS Completed entries. Stale claims must be struck and originating docs archived. |
| 97 | actionable | new BACKLOG-authoring rule under Orchestration Plan Rules | Before filing BACKLOG entries framed as "X was never done" or "X is missing", scan BACKLOG Closed section for prior history. Reconcile or reframe if prior entries exist. |
| 64 | archived | `lessons-forge/knowledge/archived-narratives-2026-05-27.md` | Leftover-after-ship tooling. Existing Phase 1.5 discipline catches the pattern at 100% rate; tooling path retired. |
| 87 | archived | `lessons-forge/knowledge/archived-narratives-2026-05-27.md` | Runner log `(step N)` labels unreliable for dispatch-state tracking; use file-state as ground truth. Already noted in user memories; archival captures the narrative. |
| 93 | archived | `lessons-forge/knowledge/archived-narratives-2026-05-27.md` | `git diff --stat` gate blind spot — structural fix shipped 2026-05-25; entry documents the gate-failure framing lesson. |

**Out of scope:**
- Plan A (Bellows Operational Workarounds subsection — 14 rules covering proposals 65, 68, 70, 71, 73, 77, 78, 81, 82, 85, 89, 94, plus 1-2 from residual reconciliation). Separate plan, future session.
- PLANNER_TEMPLATE version bump: this plan does NOT bump v4.53 → v4.54. The version line is bumped in session-wrap, not within plans.
- `lesson_proposals.status` advancement from `accepted` to `implemented` for the 33 proposals. Housekeeping; deferred to a later session (parallels Gate 2d pattern from 2026-05-19).

---

## STEP 1 — Forge Systems Analyst: blueprint the edit set

> **FIRST — before doing anything else, claim this plan:** `Filesystem:move_file` from `verdict-pending-executable-planner-template-plan-authoring-checklist-2026-05-27.md` to `in-progress-executable-planner-template-plan-authoring-checklist-2026-05-27.md` in `lessons-forge/knowledge/decisions/`. **THEN, immediately and BEFORE any other reads or work: post a short visible message to chat (1-2 sentences) confirming you have claimed the plan and stating your immediate next action.** This is a Rule 41 liveness anchor — SA blueprint-authoring steps have hit 600-730s inactivity timeouts in prior sessions when dense content was loaded silently. **AFTER posting confirmation:** read the four files below. **As you finish reading each file, post a 1-line acknowledgment** (e.g., "Read PLANNER_TEMPLATE.md — confirmed line counts and section anchors.") to keep the inactivity timer warm. **As you START each section of the blueprint, post a 1-line marker** ("Drafting Section N.").

You are the Forge Systems Analyst for this step. Read in order:

1. `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — the target artifact, full read. Confirm: `## Orchestration Plan Rules` heading exists; the last numbered rule is `### 41. SA dispatch shape for Bellows-watched directories — distributed early-output anchors mandatory for content load >400w` ending before `## Guardrails`; `## Procedures` exists at the bottom with 6 numbered procedures. Note the current version line (expected `**Version:** 4.53`).
2. `/Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md` — project context anchor.
3. `/Users/marklehn/Developer/GitHub/LESSONS.md` head 100 lines — the 2026-05-27 gate-1-routing rule and the 2026-05-27 Bellows STEP header monotonic lesson set the framing for several proposals in this plan.
4. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/` — locate any prior PLANNER_TEMPLATE edit-blueprint references if useful for shape (the 2026-05-19 gate-2b blueprint is the closest precedent).

**Blueprint scope.** Produce a blueprint deposit specifying the exact edits DEV will apply. Cover four edit clusters:

**Cluster 1 — New `## Plan Authoring Checklist` section.** Author the full Markdown for a new top-level section inserted between the end of `## Orchestration Plan Rules` (after Rule 41's body) and `## Guardrails`. The section opens with a 2-4 sentence preamble explaining the lifecycle moment the checklist runs at (after `_staging_*` write, before atomic `Filesystem:move_file` to watched directory), and that each check is a mechanical pre-deposit verification — not a prose rule to remember at authoring time. Following the preamble, enumerate 12 checks numbered 1-12, in an order you decide based on dependency flow (suggest: format checks first, then content checks, then scope checks). Each check is a `### N. <Title>` subsection of 2-5 sentences: state the check, the grep/diff command or read pattern that mechanizes it, and the action to take if it fails. Map each check to its source proposal ID in a one-line "Source:" footer (e.g., `Source: proposal 66, lesson 2026-05-XX`). The 12 checks correspond to proposals 66, 67, 69, 75, 79, 80, 84, 90, 91, 92, 95, 98 (see Context table for one-liners).

**Cluster 2 — 4 actionable residual rules into existing sections.** Author the full Markdown for the 4 (or 5 — see Decision 2) actionable residual rules placed into the named target sections. Each rule is a new `### N. <Title>` subsection with 2-4 sentences. Use the next monotonic rule number (PLANNER_TEMPLATE currently has Rules 1-41; new rules become 42, 43, 44, 45 unless placed into a subsection like Diagnostic Prompt Engineering where they take a different anchor). Specifically:

- Proposal 76 → new rule under existing `### Diagnostic Prompt Engineering` subsection (line ~760).
- Proposal 83 → new rule appended after Rule 41 under `## Orchestration Plan Rules`. Title naming convention: "BACKLOG defer re-evaluation when manual fallback gets mechanized" or similar.
- Proposal 96 → new rule appended after Rule 41 under `## Orchestration Plan Rules`. Title: "Baton 'On the horizon' cross-check against PROJECT_STATUS Completed" or similar.
- Proposal 97 → new rule appended after Rule 41 under `## Orchestration Plan Rules`. Title: "BACKLOG entry framing — scan Closed section before filing 'never done'" or similar.

**The two SA-decision candidates** (proposals 72 and 74) must be evaluated and resolved in the blueprint. For each, decide: actionable rule (specify section + title + rule text), archived narrative (move to Cluster 4), or Plan-A-fold (note explicitly and exclude from this plan). State your decision and reasoning in the blueprint. Target final count: 4 actionable residual rules in this plan + appropriate disposition for the 2 candidates.

**Cluster 3 — Numbering reconciliation.** PLANNER_TEMPLATE currently has Rules 1-41 under `## Orchestration Plan Rules`. New top-level rules from Cluster 2 (83, 96, 97, and possibly 74) take Rules 42-45 (or 42-44 if 74 is folded/archived). The new `## Plan Authoring Checklist` section uses its own 1-12 numbering scope, NOT continuous with the Orchestration Plan Rules. Confirm this is the intent.

**Cluster 4 — Archived narratives file content.** Author the full Markdown for `lessons-forge/knowledge/archived-narratives-2026-05-27.md`. Header section explains the file's purpose (record of Gate 1 archive-as-context dispositions for the 2026-05-27 cycle). One subsection per archived proposal: title, source lesson reference if any, the one-line "why archived" rationale, and the proposal's `suggested_action` text verbatim. Cover proposals 64, 87, 93, plus any candidates demoted from Cluster 2 (potentially 72).

**Blueprint deposit.** Write the blueprint to `lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md`. The blueprint must contain:
1. A "Pre-edit verification" subsection enumerating the exact line-number expectations DEV must confirm before any `edit_block` call (PLANNER_TEMPLATE version line, `## Orchestration Plan Rules` line, Rule 41 line range, `## Guardrails` line, total line count). Build these from the actual file you read — do not estimate.
2. A "Cluster 1 — Plan Authoring Checklist section" subsection with the full Markdown to insert, including the section heading, preamble, and all 12 numbered checks. Each check has its Source footer.
3. A "Cluster 2 — Residual actionable rules" subsection listing each new rule by target section, insertion anchor (the existing rule it appends after), and full Markdown body.
4. A "Cluster 2 decisions — proposals 72 and 74" subsection: your disposition for each with one-paragraph reasoning.
5. A "Cluster 3 — Numbering" subsection: a 1-2 paragraph confirmation of the rule-numbering plan with the explicit new rule numbers assigned.
6. A "Cluster 4 — Archived narratives file" subsection with the full Markdown content for `archived-narratives-2026-05-27.md`.
7. A "DEV apply order" subsection: ordered list of the `edit_block` operations DEV will run, in dependency order (file changes before any commit).

Verdict pause after this step is `always` — CEO reviews the blueprint and the two SA-decision dispositions before DEV writes.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md`

---

## STEP 2 — Forge Developer: apply edits per blueprint

> **FIRST — before doing anything else, claim this plan:** verify the plan filename is `in-progress-executable-planner-template-plan-authoring-checklist-2026-05-27.md` (Bellows renames on dispatch). Post a 1-2 sentence visible chat confirmation. **As you finish reading each file, post a 1-line acknowledgment.** **As you start each edit cluster, post a 1-line marker** ("Applying Cluster N.").

You are the Forge Developer. Read in order:

1. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` — Step 1's blueprint. This is your authoritative spec.
2. `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — the target artifact. Confirm pre-edit verification from blueprint Section 1 passes (version line, anchor lines, total line count). If any check fails, HALT and report.

**Apply the edits in dependency order specified in blueprint Section 7 ("DEV apply order").** Use `Desktop Commander:edit_block` for each edit against `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`. Anchor each `old_string` with 3-5 surrounding lines (heading + adjacent content) so the match is unambiguous. Do not paraphrase blueprint Markdown — copy verbatim.

**Then create the archived-narratives file.** Use `Filesystem:write_file` to create `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` with the Markdown content from blueprint Cluster 4.

**Strict scope: this step modifies ONLY PLANNER_TEMPLATE.md and creates ONLY archived-narratives-2026-05-27.md.** Do not touch any other file. Do not commit. Do not bump PLANNER_TEMPLATE version line.

**Output receipt** lists each `edit_block` call by anchor + line range, plus the file creation. Note any anchor mismatches encountered and how resolved.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (modified)
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` (new)

---

## STEP 3 — Forge QA: verification

> **FIRST — before doing anything else:** post a 1-2 sentence visible chat message confirming you are starting Step 3 verification. **As you finish reading each file, post a 1-line acknowledgment.** **As you start each verification check, post a 1-line marker** ("Check N.").

You are the Forge QA. Read in order:

1. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` — the spec.
2. `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — the modified file.
3. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` — the new file.

**Verification checks (run all):**

1. **Section exists:** `grep -n '^## Plan Authoring Checklist' /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` returns exactly 1 match, between `## Orchestration Plan Rules` end and `## Guardrails`.
2. **Checklist count:** `grep -nE '^### [0-9]+\.' PLANNER_TEMPLATE.md` within the new section returns exactly 12 entries, numbered 1 through 12, monotonic, no skips, no duplicates.
3. **Checklist Source footers:** each of the 12 checks has a `Source: proposal NN` footer line. Enumerate the proposal IDs in checklist order and confirm the set equals `{66, 67, 69, 75, 79, 80, 84, 90, 91, 92, 95, 98}` (12 IDs, no duplicates, no extras).
4. **New Orchestration Plan Rules:** confirm Rules 42-44 (or 42-45 if SA promoted 74) exist immediately after Rule 41, monotonic numbering, no gap to existing Rule 41. Confirm at least 3 of the new rule titles match the proposals 83, 96, 97 (and 74 if applicable).
5. **Diagnostic Prompt Engineering insertion:** confirm one new rule was inserted under `### Diagnostic Prompt Engineering` subsection sourced from proposal 76.
6. **Archived-narratives file:** confirm `lessons-forge/knowledge/archived-narratives-2026-05-27.md` exists, contains a section per archived proposal, and the set of archived proposal IDs equals what blueprint Cluster 4 specified.
7. **Untouched scope:** `git diff --stat /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` shows additions only (no deletions of existing rules). `git status` shows only PLANNER_TEMPLATE.md and the new archived-narratives file as changes. No other files modified.
8. **Version line untouched:** `grep -n '^\*\*Version:\*\*' PLANNER_TEMPLATE.md` returns `**Version:** 4.53` (or whatever value was present before Step 2). Plan does not bump version.
9. **No STOP-prose in new content:** grep new Plan Authoring Checklist section and new rules for `**STOP.**`, `do not proceed`, `halt and report` — should return zero matches in new content (these are markers of dispatch_mode: bellows STOP-prose hazard).
10. **Rule 20 self-check block** — author the canonical QA self-check Python block per Rule 20 with placeholders filled for this plan. Include the block in the QA report. Run the block manually (read PLANNER_TEMPLATE.md section by section against blueprint Markdown) and report PASS/FAIL per check.

**QA report deposit:** write the full report (each numbered check with PASS/FAIL and supporting evidence — grep output, line counts, file existence confirmations) to `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/plan-authoring-checklist-qa-2026-05-27.md`.

**Output receipt** summarizes: total checks run, PASS count, FAIL count, any FAILs with one-line explanation each.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/plan-authoring-checklist-qa-2026-05-27.md`

---

## Execution Map

Step 1 (SA) → [verdict pause: CEO reviews blueprint + dispositions for proposals 72, 74] → Step 2 (DEV) → [verdict pause] → Step 3 (QA) → [verdict pause: terminal]

All three steps run sequentially. No parallel lanes.

---

## How to Run This Plan

This is a Bellows-dispatched plan (`Dispatch Mode: bellows`). After atomic deposit to `lessons-forge/knowledge/decisions/`, Bellows claims it and dispatches Step 1 to a Forge SA agent in a worktree. CEO reviews each step's deposits at verdict pauses and writes `verdict-<slug>-step-<N>.md` files to `bellows/verdicts/resolved/` to continue or stop.

Terminal close: Bellows moves the plan to `Done/` on consumption of Step 3's continue verdict (per the 2026-05-26 v4.52 terminal-close behavior).
