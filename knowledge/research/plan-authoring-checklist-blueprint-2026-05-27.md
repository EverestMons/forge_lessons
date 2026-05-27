# Blueprint: Plan Authoring Checklist + Residual Scatter — 2026-05-27

**Plan:** `executable-planner-template-plan-authoring-checklist-2026-05-27`
**Step:** 1 (SA blueprint)
**Date:** 2026-05-27

---

## 1. Pre-edit verification

DEV must confirm these anchors before any `edit_block` call. All values were read from the live file on 2026-05-27.

| Anchor | Expected Line | Expected Value |
|---|---|---|
| Version line | 5 | `**Version:** 4.54` |
| `## Orchestration Plan Rules` heading | 439 | `## Orchestration Plan Rules` |
| Rule 41 title | 872 | `### 41. SA dispatch shape for Bellows-watched directories — distributed early-output anchors mandatory for content load >400w` |
| Rule 41 last content paragraph | 899 | Starts with `**Related session-10 patterns (not yet promoted to LESSONS):**` |
| Section separator after Orchestration Plan Rules | 901 | `---` |
| `## Guardrails` heading | 903 | `## Guardrails` |
| `### Diagnostic Prompt Engineering` subsection | 760 | `### Diagnostic Prompt Engineering` |
| Last DPE paragraph ("Parallel implementation check") | 772 | Starts with `**Parallel implementation check.**` |
| `### 28. Pre-cutover unknowns...` (next rule after DPE) | 774 | `### 28. Pre-cutover unknowns diagnostic before destructive cross-cutting work` |
| Total line count | — | 1504 |

**Note:** The plan's Context section expected version 4.53, but the file currently reads 4.54. This is informational only — the plan does NOT bump the version line. DEV confirms 4.54 and does not modify it.

---

## 2. Cluster 1 — Plan Authoring Checklist section

Insert as a new `## Plan Authoring Checklist` top-level section between the `---` separator after `## Orchestration Plan Rules` (line 901) and `## Guardrails` (line 903). The full Markdown to insert (including the section heading) is:

```markdown
## Plan Authoring Checklist

This checklist runs at plan deposit time — after the plan is fully composed in `_staging_*` (or a temp path) and before the atomic `Filesystem:move_file` to the Bellows-watched `knowledge/decisions/` directory. Each check is a mechanical pre-deposit verification: a grep, diff, or structural scan that catches plan-authoring errors before they reach Bellows. These are not prose rules to remember during composition — they are a final-gate scan applied to the finished artifact.

The Planner runs these checks in order before every plan deposit. A failing check blocks the deposit until resolved.

### 1. Deposits blocks use canonical multi-line bullet form

Grep the plan file for `**Deposits:**`. Every match must be followed by one or more `- ` bullet lines, each containing exactly one backtick-quoted path. Inline comma-separated form (e.g., `` `path/a.md`, `path/b.md` `` on a single line) is forbidden — the deposit parser reads line-by-line and treats commas as part of the path string. If inline form is found, rewrite to multi-line bullets before deposit.

Source: proposal 66, lesson 2026-05-27

### 2. Agent deposits use Rule 26 Deposits block format

Grep the plan file for deposit path references that appear in step prose but NOT inside a `**Deposits:**` block. Every path the agent writes to must appear in the step's `**Deposits:**` block with backtick quoting. Inline prose alternatives ("deposit findings to `path/to/file.md`") silently fail parser registration — the `deposit_exists` gate reads only the declared block. If prose-embedded deposit references are found without a corresponding `**Deposits:**` entry, add them to the block.

Source: proposal 95, lesson 2026-05-27

### 3. No STOP-prose in Bellows-dispatched plans

For plans with `dispatch_mode: bellows`, grep for STOP-prose patterns: `**STOP.**`, `do not proceed`, `halt and report`, `wait for CEO confirmation`, `wait for my confirmation`. These patterns are ignored by Bellows — the daemon dispatches steps end-to-end unless `pause_for_verdict` is set in the header. Strip all matches. The `pause_for_verdict` header field is the only mechanism for inter-step pauses in Bellows-dispatched plans.

Source: proposal 79, lesson 2026-05-27

### 4. QA step includes exact canonical Rule 20 self-check reference

Grep the plan file for every step identified as QA (per the `qa_steps` header field). Each QA step must contain the exact canonical template paragraph from `RULE_20_SELF_CHECK_BLOCK.md` with four placeholders filled (`plan_slug`, `qa_report_path`, `evidence_dir`, `required_evidence_files`). No paraphrasing, no "review the file" pointers, no agent-discretion language. If the template paragraph is missing or paraphrased, copy it verbatim from `RULE_20_SELF_CHECK_BLOCK.md` and fill the placeholders.

Source: proposal 75, lesson 2026-05-27

### 5. Frontend-to-backend DEV steps specify exact field names

For any DEV step that connects a frontend component to a backend handler, grep the step text for field-name and value-enum references. The step must either (a) list exact field names and value enums from the backend handler inline, or (b) include an explicit instruction for the agent to read the backend handler first and extract the field contract before wiring. Vague instructions like "connect the form to the API" without field-level specificity cause agents to guess field names, producing silent data-binding failures.

Source: proposal 80, lesson 2026-05-27

### 6. QA-step Deposits blocks declare only the QA report

Grep each QA step's `**Deposits:**` block. It must declare exactly one `.md` file — the QA report. PROJECT_STATUS.md updates, feedback log appends, and other `.md` writes performed during the QA step are side effects, not deposits. Listing them in the `**Deposits:**` block causes the `deposit_exists` gate to verify paths the step writes only conditionally (e.g., PROJECT_STATUS is updated only if deliverable verification passes), producing false gate failures. Evidence directories are listed separately per Rule 26's existing convention.

Source: proposal 90, lesson 2026-05-27

### 7. Follow-up plans from gate failures match files against full paths

When authoring a follow-up plan from a gate failure, read the literal Files Changed list from the verdict request's `file_change_audit` section. Match each entry against its full path — do not match by slug or basename alone. Gate failures on plans with slug-sharing artifacts (e.g., two plans whose filenames share a common substring) can produce Files Changed lists that reference the wrong plan's artifacts. The full-path match disambiguates. If the follow-up plan references files from the gate failure, confirm each path is from the failed plan's scope, not a slug-collision artifact.

Source: proposal 67, lesson 2026-05-27

### 8. Filename-pattern fixes enumerate all lifecycle stages

When a plan's fix operates on files by filename pattern (e.g., `executable-*.md`, `verdict-request-*.md`), enumerate all lifecycle stages that produce files matching that pattern. If two or more stages match, include a disambiguator in the fix (e.g., directory path, lifecycle prefix, or creation timestamp). Bellows plan files pass through multiple lifecycle stages (`executable-*` → `in-progress-*` → `verdict-pending-*` → `Done/`), and verdict files pass through `verdict-*` → `processed-verdict-*`. A pattern-based fix that doesn't account for lifecycle stages can match files in the wrong state.

Source: proposal 69, lesson 2026-05-27

### 9. Multi-step diagnostics use pause_for_verdict: always

Grep the plan file for the `pause_for_verdict` header field. If the plan is a multi-step diagnostic requiring per-step CEO review, the value must be `always`. The value `after_step_1` is reserved for standard two-step DEV → QA plans. Multi-step diagnostics with `after_step_1` will auto-advance from Step 2 onward without pausing for review, which defeats the per-step review intent. Alternative: split into separate single-step diagnostics, each with its own verdict cycle.

Source: proposal 84, lesson 2026-05-27

### 10. Data-source mechanization plans include governance edit

If the plan mechanizes a new authoritative data source (introduces a new field, table, or config that downstream agents or rules will depend on), grep the plan for a governance edit step that obligates population of that data source. The governance edit and the mechanization must ship in the same session. "Defer governance edit to follow-up" creates a window where the data source exists but no rule requires anyone to populate it — the data source ships empty and stays empty until someone notices, which may be never.

Source: proposal 91, lesson 2026-05-27

### 11. Contract-changing plans grep test files before declaring targeted scope

If the plan changes a function's contract (return type, parameter types, or semantic contract), grep `tests/` for references to the changed function: `grep -rn "<function_name>" tests/`. Count the test files where the function appears. If the function appears in more than one test file, test scope must be `full-suite` regardless of how mechanical the production-code change looks. If exactly one test file, `targeted` is acceptable but the QA prompt must explicitly name that file. This supplements Rule 21's contract-change carve-out with a mechanical pre-deposit check.

Source: proposal 92, lesson 2026-05-27

### 12. Schema migration plans include init_db and PRAGMA verification

If the plan ships a schema migration, grep the plan for explicit `init_db` (or equivalent schema-application) instructions against the production database. The plan must include: (a) running the migration/init against the production DB file, (b) a `PRAGMA table_info(<table>)` verification step confirming the migration applied, and (c) a `git add` + commit of the modified DB file. Plans that ship schema migrations via code changes alone leave the production DB in the pre-migration state — code schema changes do not retroactively apply to existing live databases.

Source: proposal 98, lesson 2026-05-27
```

---

## 3. Cluster 2 — Residual actionable rules

### 3a. Proposal 76 → Diagnostic Prompt Engineering technique

**Target section:** `### Diagnostic Prompt Engineering` (line 760)
**Insertion anchor:** After the "Parallel implementation check" paragraph (line 772), before `### 28.` (line 774)
**Anchor text (old_string):** The last DPE paragraph ending with `Without this, agents may trace only one path and miss divergence.` followed by a blank line and `### 28.`

**Full Markdown to insert** (new bold-paragraph technique, matching the existing DPE convention):

```markdown
**Timing and ordering claim verification.** Before asserting timing, ordering, or dispatch-sequence claims about Bellows code paths in a diagnostic prompt, grep `knowledge/research/` for the most recent ordering audit or dispatch-trace deposit and verify the claim against it. Bellows's dispatch ordering has been revised across multiple fix cycles; stale mental models of the ordering produce diagnostic prompts that investigate non-existent code paths or assert sequencing that was true two versions ago. The grep cost is ~5 seconds; the cost of a diagnostic built on a stale ordering assumption is a full re-investigation cycle.
```

Source: proposal 76, lesson 2026-05-27

### 3b. Proposal 83 → Rule 42

**Target section:** `## Orchestration Plan Rules`
**Insertion anchor:** After Rule 41's last content (the `**Related session-10 patterns**` paragraph at line 899), before the `---` separator at line 901

**Full Markdown to insert:**

```markdown
### 42. BACKLOG defer re-evaluation when manual fallback gets mechanized

When a plan mechanizes a previously-manual check via Rule 25-style routing, automated gating, or any new structural enforcement, scan open BACKLOG entries for defers whose rationale depends on the manual fallback. A BACKLOG entry that was deferred because "the Planner checks this manually at verdict time" becomes actionable when the manual check is replaced by a gate. Re-evaluate each affected defer: if the mechanization closes the gap the defer relied on, promote the BACKLOG item to executable scope or close it. If the mechanization doesn't fully close the gap, update the defer rationale to reflect the new state. Stale defer rationales accumulate into a BACKLOG that misrepresents the system's actual automation level.
```

Source: proposal 83, lesson 2026-05-27

### 3c. Proposal 96 → Rule 43

**Target section:** `## Orchestration Plan Rules`
**Insertion anchor:** Immediately after Rule 42 (inserted in 3b above)

**Full Markdown to insert:**

```markdown
### 43. Baton "On the horizon" cross-check against PROJECT_STATUS Completed

Every "On the horizon" item carried from a prior session-handoff baton (`NEXT_SESSION.md` or `shop_next_session.md`) must be cross-checked against the relevant project's `PROJECT_STATUS.md` Completed entries before being carried forward to a new baton. If an "On the horizon" item matches a Completed entry, it is stale — strike it from the baton and archive the originating doc if it has no remaining live items. Stale horizon claims that survive across batons create false urgency and waste diagnostic cycles investigating work that was already shipped.
```

Source: proposal 96, lesson 2026-05-27

### 3d. Proposal 97 → Rule 44

**Target section:** `## Orchestration Plan Rules`
**Insertion anchor:** Immediately after Rule 43 (inserted in 3c above)

**Full Markdown to insert:**

```markdown
### 44. BACKLOG entry framing — scan Closed section before filing "never done"

Before filing a BACKLOG entry framed as "X was never done," "X is missing," or "X was not implemented," scan the BACKLOG's Closed section for prior entries addressing the same area. If a prior entry exists, reconcile: either (a) the prior entry's fix was incomplete and the new entry should reference it ("reopening BACKLOG #N — prior fix was scoped to Y, but Z remains"), or (b) the prior entry fully addressed the concern and the new filing is a misdiagnosis. Filing "never done" entries without checking Closed creates duplicate work items and erodes confidence in the BACKLOG as a reliable record of what has been addressed.
```

Source: proposal 97, lesson 2026-05-27

---

## 4. Cluster 2 decisions — proposals 72 and 74

### Proposal 72 → ARCHIVED

Proposal 72 reinforces Phase 1.5 discipline for the case where "CEO opening message is substantive." Rule 33 (line 800) already mandates: "Phase 1.5 Recent Knowledge Scan happens at session start BEFORE any investigation, regardless of how narrow the opening question seems." The "regardless of how narrow the opening question seems" language directly covers the case proposal 72 targets — a substantive CEO opening that creates urgency to skip Phase 1.5. The incremental value of 72 is the "acknowledge briefly" instruction, which is standard conversational behavior and does not warrant a separate rule. Adding a reinforcement for a rule that already exists with identical scope creates redundancy without new mechanical value.

**Disposition:** Archived to `archived-narratives-2026-05-27.md` alongside proposals 64, 87, 93.

### Proposal 74 → FOLD TO PLAN A

Proposal 74 establishes that CEO addenda during plan execution flow downstream via verdict reasoning text, not upstream via blueprint file edits. This is a genuine new rule — Rule 35 covers dispatch-mode discrimination but does not address mid-plan communication flow. However, proposal 85 (part of Plan A's 14-rule Bellows Operational Workarounds scope) covers a closely related concern. The "Bellows Operational Workarounds" subsection is the natural home for rules about how information flows during Bellows-dispatched plan execution. Shipping 74 as a standalone orchestration rule here risks duplicating or conflicting with whatever shape Plan A gives to proposal 85.

Decision 2's constraint ("at least one must be demoted to archived or folded into Plan A's scope") is satisfied by archiving 72. Folding 74 into Plan A consolidates the mid-plan communication rules into one coherent subsection rather than scattering them across the Orchestration Plan Rules body.

**Disposition:** Deferred to Plan A's session. Not shipped in this plan. Plan A's scope list should include proposal 74 alongside proposal 85 for joint authoring.

---

## 5. Cluster 3 — Numbering

The new `## Plan Authoring Checklist` section uses its own **1-12 numbering scope**, independent of the Orchestration Plan Rules numbering. This is intentional: checklist items operate at a different lifecycle moment (post-composition, pre-deposit) and have a different enforcement mechanism (mechanical scan of a finished artifact vs. authoring discipline during composition). Numbering them 42-53 would falsely imply they are continuous with Rules 1-41, which would break the conceptual separation between "rules to follow while writing plans" and "checks to run on a finished plan before depositing it."

New **numbered rules** under `## Orchestration Plan Rules`:

| New Rule # | Title | Source Proposal |
|---|---|---|
| 42 | BACKLOG defer re-evaluation when manual fallback gets mechanized | 83 |
| 43 | Baton "On the horizon" cross-check against PROJECT_STATUS Completed | 96 |
| 44 | BACKLOG entry framing — scan Closed section before filing "never done" | 97 |

New **unnumbered technique** under `### Diagnostic Prompt Engineering`:

| Technique | Source Proposal |
|---|---|
| Timing and ordering claim verification | 76 |

Proposal 76 follows the existing DPE convention of bold-paragraph techniques (e.g., `**Scope enumeration.**`, `**Output format specification.**`), not the `### N. <Title>` numbered rule convention. This is consistent with how the DPE subsection is structured — it collects technique-level guidance, not mandatory numbered rules.

**Total after edits:** 44 numbered Orchestration Plan Rules + 6 DPE techniques + 12 Plan Authoring Checklist items.

---

## 6. Cluster 4 — Archived narratives file

Full Markdown content for `lessons-forge/knowledge/archived-narratives-2026-05-27.md`:

```markdown
# Archived Narratives — 2026-05-27 Lessons Forge Cycle

This file records Gate 1 archive-as-context dispositions from the 2026-05-27 Lessons Forge cycle. These proposals were reviewed during Gate 1 and classified as narratives or reinforcements that do not warrant new governance rules — either because the pattern is already captured, the structural fix has shipped, or the observation has no actionable intervention. They are preserved here as historical context.

---

## Proposal 64 — Leftover-after-ship tooling retirement

**Source lesson:** 2026-05-27 cycle, entry on leftover-after-ship tooling path
**Why archived:** Existing Phase 1.5 discipline catches the leftover-after-ship pattern at 100% rate. The tooling path (term-matching approach) was tried and retired. No new action until semantic comparison is available.
**Suggested action (verbatim):** Archive as context. Existing Phase 1.5 discipline catches the leftover-after-ship pattern at 100% rate. Tooling path (term-matching) was tried and retired. No new action until semantic comparison is available.

---

## Proposal 72 — Phase 1.5 reinforcement for substantive CEO openings

**Source lesson:** 2026-05-27 cycle, entry on Phase 1.5 skip under urgency
**Why archived:** Substantially overlaps Rule 33 (Phase 1.5 enforcement — happens FIRST regardless of task size), which already mandates Phase 1.5 before any investigation "regardless of how narrow the opening question seems." The incremental value (explicit "acknowledge briefly" instruction) does not warrant a separate rule. SA disposition during blueprint authoring.
**Suggested action (verbatim):** Reinforce PLANNER_TEMPLATE.md Phase 1.5 rule: when CEO opening message is substantive, acknowledge briefly and complete Phase 1.5 reads before any investigation. Protocol exists for high-urgency moments.

---

## Proposal 87 — Runner log step labels unreliable for dispatch tracking

**Source lesson:** 2026-05-27 cycle, entry on runner log `(step N)` label reliability
**Why archived:** Already noted in user memories. File-state (verdict-request filenames, plan filename prefix) is the authoritative dispatch-state tracking mechanism, not runner log labels. Archival captures the narrative without adding a governance rule.
**Suggested action (verbatim):** Archive as operational context — runner log `(step N)` labels are unreliable for dispatch-state tracking; use file-state (verdict-request filenames, plan filename prefix) as ground truth.

---

## Proposal 93 — git diff --stat gate blind spot

**Source lesson:** 2026-05-27 cycle, entry on gate-failure framing for blast-radius evaluation
**Why archived:** Structural fix shipped 2026-05-25 (scope_check gate now uses `--relative -- .` to scope diffs to project subtree). Entry documents the gate-failure framing lesson: evaluate blast radius by gate consumers, not surface output. The lesson is valid context but the fix is already in production code.
**Suggested action (verbatim):** Archive as context — `git diff --stat` gate blind spot is fixed (structural fix shipped 2026-05-25); entry documents the gate-failure framing lesson: evaluate blast radius by gate consumers, not surface output.
```

---

## 7. DEV apply order

DEV applies edits in this order. All edits target `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` except edit 4 which creates a new file. Top-to-bottom ordering ensures each text-based anchor remains stable after prior insertions.

1. **Edit 1 — Insert DPE technique (proposal 76).** `edit_block` on PLANNER_TEMPLATE.md. Anchor: the paragraph ending `Without this, agents may trace only one path and miss divergence.` followed by blank line and `### 28.`. Insert the new "Timing and ordering claim verification" paragraph between them.

2. **Edit 2 — Insert Rules 42-44 (proposals 83, 96, 97).** `edit_block` on PLANNER_TEMPLATE.md. Anchor: the paragraph starting `**Related session-10 patterns (not yet promoted to LESSONS):**` followed by blank line and `---`. Insert all three new rules as a block between the paragraph and the `---`.

3. **Edit 3 — Insert `## Plan Authoring Checklist` section.** `edit_block` on PLANNER_TEMPLATE.md. Anchor: `---` separator followed by blank line and `## Guardrails`. Insert the full checklist section (heading, preamble, 12 checks) between the `---` and `## Guardrails`, with appropriate `---` separators to maintain section boundaries.

4. **Edit 4 — Create archived-narratives file.** `write_file` to create `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` with the Cluster 4 content from Section 6 above.

**No commit in Step 2. No version bump. Only PLANNER_TEMPLATE.md is modified and archived-narratives-2026-05-27.md is created.**

---

## Output Receipt
**Agent:** Forge Systems Analyst
**Step:** 1
**Status:** Complete

### What Was Done
Produced the full edit-set blueprint for the Plan Authoring Checklist + Residual Scatter plan. Evaluated proposals 72 and 74 per Decision 2: archived 72 (overlaps Rule 33), folded 74 to Plan A (overlaps proposal 85). Blueprint specifies 12 checklist items, 3 new numbered rules (42-44), 1 DPE technique, and 4 archived narratives.

### Files Deposited
- `lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` — full blueprint with pre-edit verification, all four clusters, numbering reconciliation, and DEV apply order

### Files Created or Modified (Code)
- None (blueprint only)

### Decisions Made
- Proposal 72 → archived (Rule 33 overlap)
- Proposal 74 → Plan A fold (proposal 85 overlap)
- Checklist numbering: 1-12 independent scope, not continuous with Rules 1-41
- New rules numbered 42-44 under Orchestration Plan Rules
- Proposal 76 as unnumbered DPE technique (matches existing DPE convention)

### Flags for CEO
- PLANNER_TEMPLATE version is 4.54, not 4.53 as plan Context expected. No action needed — plan does not bump version.

### Flags for Next Step
- None
