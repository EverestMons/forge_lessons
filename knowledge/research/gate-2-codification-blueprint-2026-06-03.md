# Gate 2 Codification Blueprint — 2026-06-03

**Author:** Forge Developer (SA role), Step 1
**Dedup baseline:** PLANNER_TEMPLATE.md v4.58 (live file as of 2026-06-03)
**Source proposals:** 19 accepted governance_rule proposals (IDs 99-121, excluding rejected 106/112)
**Locked merges:** 100+108, 113+115, 103+121 (3 pairs → 3 rules)
**Net distinct rules after merges:** 16 entries evaluated
**Net edits to PLANNER_TEMPLATE.md:** 15 (one proposal fully subsumed — see §Proposal 110)

---

## Dedup Pass Summary

Every proposal was deduplicated against the live v4.58 PLANNER_TEMPLATE.md. The following reconciliation decisions were made:

| Proposal(s) | Disposition | Rationale |
|---|---|---|
| 99 | APPEND-NEW | No existing checklist item covers parser-based header validation |
| 103+121 | APPEND-NEW (merged) | Existing items 1-2 cover Deposits block format, not step-body path naming for scope_check |
| 107 | APPEND-NEW | No existing item covers memory-based assertion avoidance |
| 114 | APPEND-NEW | No existing item covers verbatim convention-string copying |
| 116 | APPEND-NEW | Supplements 114 with specific dispatch-mode mechanization; distinct from Rule 35 conceptual coverage |
| 119 | APPEND-NEW | No existing item covers STEP header label format |
| 100+108 | STRENGTHEN-EXISTING WA#8 | Current WA#8 is narrower (check worktrees during execution); merged proposals broaden to all-edits-deferred + recovery cost |
| 104 | STRENGTHEN-EXISTING Rule 25 | Rule 25 already mandates reading verdict-request file; 104 adds explicit terminal-log caveat |
| 105 | APPEND-NEW | Distinct from WA#8 (which covers during-dispatch); 105 covers between-plans cleanliness |
| 110 | FULLY SUBSUMED | Rule 25 line 738 already states verbatim: verdicts to resolved/, NEVER to pending/ |
| 113+115 | STRENGTHEN-EXISTING WA#12 | Current WA#12 is the general recovery checklist; merged proposals add R2 Planner-direct close + claim-rename variant |
| 101 | APPEND-NEW | Rule 22(b) substance check exists but doesn't warn against pass-count headlines |
| 102 | APPEND-NEW | Adjacent to Rule 21 output-mode (liveness) but distinct (wall-clock bounding); no contradiction confirmed |
| 111 | APPEND-NEW | No existing workaround covers scope_check false-positive override pattern |
| 120 | APPEND-NEW | Rule 14 covers scope enumeration generically; 120 is specific to recognized-set consumer verification |
| 118 | APPEND-NEW | No existing section covers Lessons Forge Gate 1 routing discipline |

**Final counts:** 12 APPEND-NEW, 3 STRENGTHEN-EXISTING, 1 FULLY SUBSUMED (no edit).

---

## Per-Rule Dispositions

### Rule 1 — Proposal 99 (Plan Authoring Checklist #13)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 13. Verify plan header against current parser before deposit`

**Rule body:**

```
### 13. Verify plan header against current parser before deposit

Before depositing any plan to a Bellows-watched directory, verify the plan header fields by running `gates._parse_plan_header` (or its current equivalent) against the composed plan file. Header validity is on a freshness axis, not a familiarity axis — a header that parsed correctly months ago can predate a current gate or parser change. Never certify a header by pattern-matching old `Done/` artifacts or by visual resemblance to prior plans. If the parser rejects a field, fix the header before deposit.

Source: proposal 99, lesson 2026-06-03
```

---

### Rule 2 — Proposals 103+121 (Plan Authoring Checklist #14, merged)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 14. Name all target file paths literally in step bodies`

**Rule body:**

```
### 14. Name all target file paths literally in step bodies

Every file the agent will create, modify, or read as a prerequisite for edits must appear as a literal path in the step's body text — not only in the `**Deposits:**` block. Two clauses: (a) deposit file paths must also appear in the step prose so `scope_check` can authorize them — `scope_check` reads the step body text, not the `**Deposits:**` block, for file-modification authorization; (b) target file paths for DEV edits must be inlined in the DEV step body, not delegated to a referenced blueprint. `scope_check` extracts the step header line plus the first ~80 characters of the body as its plan-step context and cannot follow cross-step blueprint references. Indirect references ("add to the test module that covers X ... locate it via grep") cause `scope_check` FAIL despite the agent modifying the correct file.

Source: proposals 103 and 121, lesson 2026-06-03
```

---

### Rule 3 — Proposal 107 (Plan Authoring Checklist #15)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 15. No specific values from session memory in plan assertions`

**Rule body:**

```
### 15. No specific values from session memory in plan assertions

Never name specific test names, file paths, line numbers, or fixed-value counts inside plan body assertions from session memory. Assertions fail not because substance broke, but because the Planner mis-quoted the artifact. Two safe patterns: (a) soften to count-or-shape predicates ("all targeted tests pass," "the function exists in the handler file") rather than naming literals; (b) copy values verbatim from a fresh artifact read performed during plan composition. If the assertion requires a specific value, the value must come from a tool call, not from recall.

Source: proposal 107, lesson 2026-06-03
```

---

### Rule 4 — Proposal 114 (Plan Authoring Checklist #16)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 16. Copy strict convention strings from known-good artifacts`

**Rule body:**

```
### 16. Copy strict convention strings from known-good artifacts

Strict Bellows convention strings — header field names, dispatch mode values, directory names, lifecycle-prefix spellings, `pause_for_verdict` values — must be copied verbatim from a known-good artifact (a recent `Done/` plan, the Bellows README, or the relevant PLANNER_TEMPLATE rule), never authored from memory. Three failures in one session shared this root cause: a header field-line position error, a dispatch-mode typo, and a directory-name misspelling. Each was a machine-checked value that the Planner specified from recall rather than copy-paste.

Source: proposal 114, lesson 2026-06-03
```

---

### Rule 5 — Proposal 116 (Plan Authoring Checklist #17)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 17. Mechanize dispatch-mode validation`

**Rule body:**

```
### 17. Mechanize dispatch-mode validation

Before depositing a plan, validate the `**Dispatch Mode:**` field by copying it from a known-good `Done/` artifact's header or running the Bellows header validator. Do not rely on memory recall of the allowed values (`bellows`, `manual_bootstrap`). Despite Rule 35 and Checklist item 3 already covering dispatch mode, four rejections across three days demonstrated that memory-based authoring recurs when the rule layer relies on recall rather than mechanization. The mechanized check supplements the conceptual rule: Rule 35 says "distinguish the modes"; this check says "verify the string by copy, not recall."

Source: proposal 116, lesson 2026-06-03
```

---

### Rule 6 — Proposal 119 (Plan Authoring Checklist #18)

**Disposition:** APPEND-NEW
**Section home:** Plan Authoring Checklist
**Heading:** `### 18. Use strictly monotonic integer STEP header labels`

**Rule body:**

```
### 18. Use strictly monotonic integer STEP header labels

All `## STEP N` headers in a plan must use strictly monotonic integer labels: 1, 2, 3, and so on. Bellows's step parser is positional and 1-indexed — each `## STEP N` header becomes daemon-step 1, 2, 3, 4 regardless of the label's text content. Non-monotonic labels (2A, 2B) or non-integer labels cause the daemon's positional step count to diverge from the label the agent sees in the prompt, producing dispatch/prompt misalignment where the agent runs the wrong step body. Grep the plan for `## STEP` headers and confirm each label is a consecutive integer before deposit.

Source: proposal 119, lesson 2026-06-03
```

---

### Rule 7 — Proposals 100+108 (Bellows Operational Workarounds #8, STRENGTHEN)

**Disposition:** STRENGTHEN-EXISTING
**Target:** Bellows Operational Workarounds, `#### 8.` (v4.58 lines 1237-1241)
**Current heading:** `#### 8. Check for active worktrees before editing project files`
**New heading:** `#### 8. Defer all working-tree edits while a plan is in-flight`

**old_string (verbatim, for DEV exact-match):**

```
#### 8. Check for active worktrees before editing project files

Before editing any file under a project path during plan execution, check `.bellows-worktrees/` for active worktrees on the in-flight plan. If an active worktree exists for the plan's slug, the agent is executing in a worktree — direct file edits to the project's main working tree from outside the worktree are invisible to the agent and will conflict at teardown cherry-pick. When an active worktree is detected and the Planner or CEO needs to communicate a change to the executing agent, use the verdict-channel addendum (write the change into the verdict `{reason}` field for the current or next step) instead of editing files in the main working tree directly.

Source: proposal 73, lesson 2026-05-27
```

**new_string:**

```
#### 8. Defer all working-tree edits while a plan is in-flight

Do not edit any file under a project's working tree — source code, blueprints, knowledge deposits, specialist files, or any other file — between the moment a Bellows-dispatched plan is deposited to `knowledge/decisions/` and the moment that plan file reaches `Done/`. Two forms of damage result from mid-flight edits: (1) the uncommitted change trips `_teardown_worktree`'s dirty-tree pre-check (`worktree_teardown_dirty_tree`), so the plan cannot complete teardown; (2) the edit lands on local `main` but never reaches the step's detached-HEAD worktree, so the in-flight agent never sees it. Recovery cost per dirty-tree cycle: ~5–10 minutes (commit or stash the offending files, re-issue verdict, wait for teardown retry). When an active worktree exists and the Planner or CEO needs to communicate a change to the executing agent, use the verdict-channel addendum (write the change into the verdict `{reason}` field) instead of editing files in the main working tree. To verify whether a plan is in-flight: check `.bellows-worktrees/` for active worktrees on the project, or check `knowledge/decisions/` for `in-progress-*` or `verdict-pending-*` files.

Source: proposals 100 and 108, lesson 2026-06-03
```

---

### Rule 8 — Proposal 104 (Rule 25, STRENGTHEN)

**Disposition:** STRENGTHEN-EXISTING
**Target:** Rule 25, gate-failure evidence-string discrimination block (v4.58 lines 709-713)
**Edit type:** INSERT new paragraph AFTER line 713

**Insertion anchor — line-before (verbatim):**
`In both cases the top-level routing is unchanged — `gate_failure` still means halt and report to CEO. This note only tells the Planner which recovery to recommend in that report.`

**Insertion anchor — line-after (verbatim):**
`**Rule 22 routing on auto-proceed codes:** When the Pause Reason Code authorizes auto-proceed,`

**New paragraph to insert:**

```
**Verdict-request primacy over terminal log line.** The daemon emits `gates step N: passed=True, failures=0` in `run_plan` BEFORE calling `_teardown_worktree`. Teardown failures — including both `worktree_teardown_dirty_tree` and `worktree_teardown` variants described above — are invisible in the terminal log because they occur after the log line is written. The verdict-request Gate Result JSON is the only source that captures post-log failures. Always read the verdict-request file's `**Gate Result Passed:**` field and `**Pause Reason Code:**` before issuing any verdict; never use the terminal `passed=True` log line as a substitute for the verdict-request file's structured fields. Rule 25's existing scan-and-route discipline already mandates reading the verdict request — this paragraph makes explicit WHY the terminal log is an unsafe shortcut.

Source: proposal 104, lesson 2026-06-03
```

---

### Rule 9 — Proposal 105 (Bellows Operational Workarounds #13)

**Disposition:** APPEND-NEW
**Section home:** Bellows Operational Workarounds
**Heading:** `#### 13. Keep watched repo roots clean of uncommitted non-lifecycle files`

**Rule body:**

```
#### 13. Keep watched repo roots clean of uncommitted non-lifecycle files

Keep Bellows-watched repo roots free of uncommitted files that are not Bellows lifecycle artifacts (lifecycle artifacts: `in-progress-*`, `verdict-pending-*`, `executable-*`, `diagnostic-*` plan files managed by the daemon). The `_teardown_worktree` step (b2) runs a dirty-tree pre-check on local `main` and raises `worktree_teardown_dirty_tree` if any uncommitted file is NOT a recognized Bellows lifecycle artifact. Stray uncommitted files — draft documents, temporary scripts, forgotten staging files — block the cherry-pick on EVERY subsequent plan teardown until committed or removed. Before depositing a new plan, verify the project root is clean: `git status` should show only lifecycle-prefix plan files (which the daemon manages) and no untracked non-lifecycle files. Commit or remove stray files before the deposit.

Source: proposal 105, lesson 2026-06-03
```

---

### Rule 10 — Proposal 110 (FULLY SUBSUMED — no edit)

**Disposition:** FULLY SUBSUMED
**Rationale:** Rule 25, line 738 of v4.58, already states verbatim:

> "Verdict response files (the Planner's authoritative continue/stop decisions) are deposited to `bellows/verdicts/resolved/verdict-<plan-slug>-step-N.md` — NEVER to `bellows/verdicts/pending/`. The `pending/` directory holds Bellows-authored verdict REQUEST files (Bellows writes them when a plan pauses); the `resolved/` directory holds Planner-authored verdict RESPONSES. Bellows's `_consume_verdicts()` scanner reads only `resolved/`; verdicts misfiled into `pending/` are silently ignored and the plan strands indefinitely."

This is byte-for-byte identical in substance to proposal 110's requested action ("always write verdict response files to verdicts/resolved/ — no other directory is consumed by Bellows"). Additionally, Workaround #5 covers the filename-matching convention for files written to `resolved/`. No new text is needed. Proposal 110 should be advanced to `status='implemented'` with no PLANNER_TEMPLATE edit — the rule it requests already exists.

**FLAG FOR CEO:** Proposal 110 is fully subsumed. This reduces the distinct-edit count from 16 to 15. No text change to PLANNER_TEMPLATE.md.

---

### Rule 11 — Proposals 113+115 (Bellows Operational Workarounds #12, STRENGTHEN)

**Disposition:** STRENGTHEN-EXISTING
**Target:** Bellows Operational Workarounds, `#### 12.` (v4.58 lines 1267-1271)
**Current heading:** `#### 12. Final-step gate_failure recovery checklist` (retained)

**old_string (verbatim, for DEV exact-match):**

```
#### 12. Final-step gate_failure recovery checklist

When a plan's final step trips a `gate_failure` but the substantive work has been verified as shipped (deposits exist, code changes committed, tests passing), follow this recovery sequence: (1) verify substance shipped — read deposits, confirm file existence on disk, check `git log` for the agent's commits; (2) issue `verdict: stop` — a continue verdict on a gate-failed final step can trigger unpredictable behavior depending on which gate failed; (3) move the plan from `in-progress-*` (or `verdict-pending-*`) to `Done/halted-but-shipped-<canonical>` — the `halted-but-shipped-` prefix signals that the plan was halted by gate failure but the deliverables are verified-good; (4) archive verdict files — move the verdict request and any resolved verdict to `verdicts/pending/archived/`; (5) note the gate failure and recovery in `PROJECT_STATUS.md` with the `halted-but-shipped` disposition.

Source: proposal 89, lesson 2026-05-27
```

**new_string:**

```
#### 12. Final-step gate_failure recovery checklist

When a plan's final step trips a `gate_failure` but the substantive work has been verified as shipped (deposits exist, code changes committed, tests passing), follow this recovery sequence: (1) verify substance shipped — read deposits, confirm file existence on disk, check `git log` for the agent's commits; (2) issue `verdict: stop` — a continue verdict on a gate-failed final step can trigger unpredictable behavior depending on which gate failed; (3) move the plan from `in-progress-*` (or `verdict-pending-*`) to `Done/halted-but-shipped-<canonical>` — the `halted-but-shipped-` prefix signals that the plan was halted by gate failure but the deliverables are verified-good; (4) archive verdict files — move the verdict request and any resolved verdict to `verdicts/pending/archived/`; (5) note the gate failure and recovery in `PROJECT_STATUS.md` with the `halted-but-shipped` disposition.

**R2 Planner-direct close (standard recovery for lifecycle-artifact teardown conflicts).** When the `gate_failure` is specifically a worktree teardown cherry-pick conflict on lifecycle artifacts (not substance files), the recovery shape is R2 Planner-direct close: cherry-pick `--no-commit`, drop the conflicting lifecycle-artifact add from the index, stage substance, issue `verdict: stop`, commit Planner-direct, then remove the stranded worktree. Two confirmed variants produce this shape — (a) Planner-side edits to the project working tree during dispatch (see Workaround #8) creating dirty-tree conflicts, and (b) the agent's own claim-rename of `executable-*` to `in-progress-*` leaving an uncommitted lifecycle artifact on local `main` that conflicts with the teardown cherry-pick. Variant (b) is reduced by the v4.57 template change dropping the vestigial agent-side claim-rename instruction, but can still occur for pre-v4.57 plans or when the agent renames files outside the template's scope. Both variants follow the same mechanical R2 recovery; the discrimination between them is by the conflicting file's identity (project working-tree file vs. lifecycle-prefix rename). For evidence-string discrimination between `worktree_teardown_dirty_tree:` and `worktree_teardown:` variants at the Rule 25 routing level, see Rule 25's gate-failure evidence-string discrimination block.

Source: proposals 89 (original), 113, and 115, lesson 2026-06-03
```

---

### Rule 12 — Proposal 101 (Quality Standards, new bullet)

**Disposition:** APPEND-NEW
**Section home:** Quality Standards (line 1045)
**Edit type:** Append new bullet after last existing bullet (line 1059)

**Rule body (as bullet):**

```
- Substance-check QA feature assertions individually via Rule 22 verification — never accept a full-suite pass-count headline as independent verification. A pass-count headline rests on a single long run that cannot be reconstructed from the report; a hung-then-killed and a slow-then-completed run produce the same count. Verify each feature assertion in the QA report by reading the cited evidence file or deposit and confirming the specific claim, not by checking whether the aggregate number is green. (Source: proposal 101, lesson 2026-06-03)
```

---

### Rule 13 — Proposal 102 (Quality Standards, new bullet)

**Disposition:** APPEND-NEW
**Section home:** Quality Standards (line 1045)
**Edit type:** Append new bullet after proposal 101's bullet

**Rule body (as bullet):**

```
- When authoring test-execution instructions for QA or diagnostic steps, use a wall-clock bound external to pytest (e.g., `timeout 600 pytest ...` via shell) plus `--collect-only` for collection-time isolation. `pytest --timeout=N` bounds per-test execution only — it cannot catch hangs during collection/import, session/module-scoped fixture setup, or C-level/non-main-thread blocking. The external wall-clock bound catches all of these. `--collect-only` as a preliminary command isolates collection-time hangs from execution-time behavior, allowing targeted diagnosis. This supplements Rule 21's full-suite output mode (which keeps the run visible) with a hard bound that kills genuinely hung runs. (Source: proposal 102, lesson 2026-06-03)
```

---

### Rule 14 — Proposal 111 (Bellows Operational Workarounds #14)

**Disposition:** APPEND-NEW
**Section home:** Bellows Operational Workarounds
**Heading:** `#### 14. Planner override for scope_check false-positives on plan-required evidence files`

**Rule body:**

```
#### 14. Planner override for scope_check false-positives on plan-required evidence files

When `scope_check` (Gate 8) flags evidence files as out-of-scope despite the plan's step body instructing those exact deposits at those exact paths, the failure is a false positive caused by collective reference — the step's `**Deposits:**` block or prose references an evidence directory or a set of evidence files by pattern rather than listing each file individually. The `scope_check` gate extracts authorized paths from the step body text by literal substring match and cannot resolve collective references ("deposit evidence files per Rule 18" or "pipe output to the evidence directory"). When this pattern is identified — the files are plan-instructed, the paths match the plan's intent, and only the reference style caused the gate miss — the Planner override per Rule 22(d) is the correct disposition. Flag the false positive in the verdict response reasoning text and issue `verdict: continue`. This is a Planner judgment call, not automatic: the Planner must confirm each flagged file was genuinely plan-instructed before overriding.

Source: proposal 111, lesson 2026-06-03
```

---

### Rule 15 — Proposal 120 (Orchestration Plan Rules #45)

**Disposition:** APPEND-NEW
**Section home:** Orchestration Plan Rules
**Heading:** `### 45. SA blueprints must verify downstream consumers when adding to recognized-sets`

**Rule body:**

```
### 45. SA blueprints must verify downstream consumers when adding to recognized-sets

When an SA blueprint adds a new value to a recognized-set — an enum, a validator's allowed-values list, a routing table's branch set, a config's recognized-keys dictionary — the blueprint must enumerate ALL downstream consumers of that set (branches, validators, lookup functions, template conditionals) and specify how each handles the new value. The enumeration is mandatory because recognized-sets often have multiple independent consumers: a validator that checks membership, a routing function that branches on value, and a lookup function that maps value to behavior. An SA blueprint that specifies the validator insertion but omits the routing branch or lookup mapping produces a value that passes validation but has no effect (or raises an unhandled-value error) downstream. Grep the codebase for all references to the set name, the existing values, or the set's variable/constant name; each hit is a candidate consumer. If a consumer cannot handle the new value without a code change, the blueprint must specify that change.

Source: proposal 120, lesson 2026-06-03
```

---

### Rule 16 — Proposal 118 (Orchestration Plan Rules #46)

**Disposition:** APPEND-NEW
**Section home:** Orchestration Plan Rules
**Heading:** `### 46. Lessons Forge Gate 1 — reject daemon-bug workaround proposals`

**Rule body:**

```
### 46. Lessons Forge Gate 1 — reject daemon-bug workaround proposals

During Lessons Forge Gate 1 review, reject medium-confidence proposals flagged in classification as "Planner-side workaround for daemon bug" and route the underlying bug to the relevant project's BACKLOG rather than codifying the workaround as PLANNER_TEMPLATE governance. Workarounds for daemon bugs are inherently temporary — they document behavior the daemon should fix, not behavior the Planner should permanently adopt. Codifying them as governance rules entrenches the workaround and reduces pressure to fix the underlying bug. The correct disposition is: reject the proposal, file (or update) a BACKLOG entry for the underlying daemon bug, and note the rejection rationale in the Gate 1 disposition report. If the daemon bug is already in the BACKLOG, cross-reference it; if not, create a new entry. Proposals with high confidence or with workaround value independent of the bug fix (e.g., the workaround teaches a generally-useful discipline) may be accepted on merit — this rule targets the specific pattern of medium-confidence daemon-bug workarounds where the only value is mitigating a known fixable bug.

Source: proposal 118, lesson 2026-06-03
```

---

## Supplementary Edit — Workaround Preamble Numbering

**Disposition:** IN-PLACE EDIT
**Target:** Bellows Operational Workarounds preamble (v4.58 line 1191)

**old_string:** `Workarounds use independent numbering (1–12) scoped to this subsection.`
**new_string:** `Workarounds use independent numbering (1–14) scoped to this subsection.`

---

## Narrative Archive Blueprint

**File:** `lessons-forge/knowledge/archived-narratives-2026-06-03.md` (NEW file — do NOT append to the 05-27 file)

**Full content:**

```markdown
# Archived Narratives — 2026-06-03 Lessons Forge Cycle

This file records Gate 1 archive-as-context dispositions from the 2026-06-03 Lessons Forge cycle. These proposals were reviewed during Gate 1 and classified as narratives — observational context that does not warrant new governance rules because the observation prescribes no concrete governance change. They are preserved here as historical context.

---

## Proposal 109 — Wall-clock calibration — small-tier approximates medium-tier

**Source lesson:** 2026-06-03 cycle, entry on wall-clock calibration data for small-tier executables
**Why archived:** Observational timing data (Diagnostic Step 1: 11m 51s; Executable Step 1: 40m 28s; Executable Step 2: 20m 06s; ~72 min total agent runtime). Implies re-tiering but prescribes no concrete governance change — no specific documentary rule change proposed.
**Suggested action (verbatim):** Archive as context — wall-clock calibration data showing small-tier executables with comprehensive test coverage run closer to medium-tier (~72 min agent runtime).

---

## Proposal 117 — Verdict filename prefix tolerance

**Source lesson:** 2026-06-03 cycle, entry on verdict-response filename prefix tolerance
**Why archived:** Both prefixed verdict files consumed correctly; plans auto-moved to Done/ on continue-verdict consumption. Documentation drift between Bellows README specification (prefix strip required) and Bellows implementation (prefix tolerated). No PLANNER_TEMPLATE action proposed — observation is about Bellows internal documentation accuracy.
**Suggested action (verbatim):** Archive as context — Bellows tolerates verdict-response filenames with unstripped diagnostic-/executable- prefixes despite README specifying prefix strip; documentation drift between spec and implementation.
```

---

## Per-Edit Anchor Map for DEV

DEV must verify each anchor verbatim before editing. If any anchor or old_string fails to match, set Output Receipt status to `Partial` and halt.

### Edit 1 — Orchestration Plan Rules: append Rules 45-46

**Type:** INSERTION
**Anchor line-before (v4.58 line 941):**
```
Before filing a BACKLOG entry framed as "X was never done," "X is missing," or "X was not implemented," scan the BACKLOG's Closed section for prior entries addressing the same area. If a prior entry exists, reconcile: either (a) the prior entry's fix was incomplete and the new entry should reference it ("reopening BACKLOG #N — prior fix was scoped to Y, but Z remains"), or (b) the prior entry fully addressed the concern and the new filing is a misdiagnosis. Filing "never done" entries without checking Closed creates duplicate work items and erodes confidence in the BACKLOG as a reliable record of what has been addressed.
```
**Anchor line-after (v4.58 line 943):**
```
---
```
**Action:** Insert Rules 45 and 46 (with blank lines between) after line 941, before the `---` separator.
**Expected net line delta:** +22 lines

### Edit 2 — Plan Authoring Checklist: append items 13-18

**Type:** INSERTION
**Anchor line-before (v4.58 line 1021):**
```
Source: proposal 98, lesson 2026-05-27
```
**Anchor line-after (v4.58 line 1023):**
```
---
```
**Action:** Insert Checklist items 13 through 18 (with blank lines between) after line 1021, before the `---` separator.
**Expected net line delta:** +60 lines

### Edit 3 — Quality Standards: append two new bullets

**Type:** INSERTION
**Anchor line-before (v4.58 line 1059):**
```
- When a plan instructs an agent to commit a database file (or any file that might be in `.gitignore`), the Planner must verify the file's tracking status BEFORE writing the instruction. Possible verifications: read `.gitignore` directly, grep for the filename in `.gitignore`, or include `git ls-files | grep <filename>` in a diagnostic. If the file is ignored, the plan should either (a) instruct the agent to commit the source change alone and document the DB change in the dev log without committing it, or (b) explicitly use `git add -f` to force-add. Choosing without verification creates a recovery situation.
```
**Anchor line-after (v4.58 line 1061):**
```
---
```
**Action:** Insert two new bullet points after line 1059, before the `---` separator.
**Expected net line delta:** +6 lines

### Edit 4 — Rule 25: insert terminal-log caveat paragraph

**Type:** INSERTION
**Anchor line-before (v4.58 line 713):**
```
In both cases the top-level routing is unchanged — `gate_failure` still means halt and report to CEO. This note only tells the Planner which recovery to recommend in that report.
```
**Anchor line-after (v4.58 line 715):**
```
**Rule 22 routing on auto-proceed codes:** When the Pause Reason Code authorizes auto-proceed, the Planner takes the path in the verdict file's `Deposit:` field and applies Rule 22's (a)–(e) checks to that path.
```
**Action:** Insert one paragraph (with source footer) after line 713, before the blank line + `**Rule 22 routing on auto-proceed codes:**` heading.
**Expected net line delta:** +6 lines

### Edit 5 — WA#8: in-place STRENGTHEN

**Type:** IN-PLACE REPLACE (exact-match mandatory)
**old_string:** See Rule 7 above — the complete block from `#### 8. Check for active worktrees before editing project files` through `Source: proposal 73, lesson 2026-05-27` (v4.58 lines 1237-1241, 5 content lines)
**new_string:** See Rule 7 above — the new expanded block.
**Expected net line delta:** +6 lines (5 → 11 content lines)

### Edit 6 — WA#12: in-place STRENGTHEN

**Type:** IN-PLACE REPLACE (exact-match mandatory)
**old_string:** See Rule 11 above — the complete block from `#### 12. Final-step gate_failure recovery checklist` through `Source: proposal 89, lesson 2026-05-27` (v4.58 lines 1267-1271, 5 content lines)
**new_string:** See Rule 11 above — the new expanded block with R2 sub-section.
**Expected net line delta:** +8 lines (5 → 13 content lines)

### Edit 7 — Bellows Operational Workarounds: append WA#13 and WA#14

**Type:** INSERTION
**Anchor line-before:** The new WA#12's final line: `Source: proposals 89 (original), 113, and 115, lesson 2026-06-03` (post-Edit-6 state)
**Anchor line-after (v4.58 line 1273):**
```
---
```
**Action:** Insert WA#13 and WA#14 after the strengthened WA#12, before the `---` separator.
**Expected net line delta:** +20 lines

### Edit 8 — Workaround preamble numbering

**Type:** IN-PLACE REPLACE (exact-match mandatory)
**old_string:** `Workarounds use independent numbering (1–12) scoped to this subsection.`
**new_string:** `Workarounds use independent numbering (1–14) scoped to this subsection.`
**Expected net line delta:** 0

### Edit 9 — Narrative archive file creation

**Type:** NEW FILE
**Path:** `lessons-forge/knowledge/archived-narratives-2026-06-03.md`
**Action:** Create file with full content from the Narrative Archive Blueprint section above.

---

## DEV Edit Ordering

Recommended edit order to minimize anchor drift:

1. **Edit 4** (Rule 25 insertion) — early in the file, minimal downstream impact
2. **Edit 1** (Rules 45-46) — Orchestration Plan Rules section
3. **Edit 2** (Checklist 13-18) — Plan Authoring Checklist section
4. **Edit 3** (Quality Standards bullets) — Quality Standards section
5. **Edit 8** (WA preamble numbering) — small in-place edit, no line shift
6. **Edit 5** (WA#8 strengthen) — in-place replace, shifts later WA line numbers
7. **Edit 6** (WA#12 strengthen) — in-place replace, shifts lines after WA#12
8. **Edit 7** (WA#13, WA#14) — insertion after strengthened WA#12
9. **Edit 9** (narrative archive) — new file, no PLANNER_TEMPLATE impact

**Version field:** `**Version:** 4.58` at line 5 MUST remain unchanged. No version bump in this step.

---

## Output Receipt

**Agent:** Forge Developer (SA role)
**Step:** 1
**Status:** Complete

### What Was Done
Authored one SA blueprint resolving dedup, consolidation, placement, and anchor mapping for all 16 distinct rules from 19 accepted governance_rule proposals. Deduped every proposal against live PLANNER_TEMPLATE.md v4.58. One proposal (110) found fully subsumed by existing Rule 25 text — flagged for CEO. Blueprint specifies exact prose for 15 edits (12 APPEND-NEW, 3 STRENGTHEN-EXISTING) plus 1 supplementary preamble numbering fix, narrative archive for 2 narratives, and a per-edit anchor map with verbatim old_string targets for DEV.

### Files Deposited
- `lessons-forge/knowledge/research/gate-2-codification-blueprint-2026-06-03.md` — this file

### Decisions Made
- **Final disposition per rule:** 12 APPEND-NEW, 3 STRENGTHEN-EXISTING, 1 FULLY SUBSUMED (proposal 110)
- **Proposal 104 reconciliation:** Rule 25 already mandates reading the verdict-request file; 104 adds a terminal-log caveat paragraph inserted after the existing teardown-variant discrimination block — not a new numbered workaround, but a strengthening of Rule 25
- **Proposals 113+115 reconciliation:** Strengthen existing WA#12 by appending an R2 Planner-direct close sub-section with both variants; cross-references Rule 25's teardown-variant discrimination block rather than restating it
- **Proposal 110 reconciliation:** FULLY SUBSUMED by Rule 25 line 738 — identical substance already present; no edit, flag for CEO
- **Proposal 102 vs Rule 21:** Confirmed adjacent-but-distinct (Rule 21 = which tests/output mode; 102 = wall-clock bounding); no contradiction
- **Section homes for 101/102:** Quality Standards new bullets (no existing QA-discipline subsection; bullets match existing section format)
- **Section homes for 120/118:** Orchestration Plan Rules 45 and 46 (consistent with prior-cycle Rules 42-44 pattern)

### Flags for CEO
- **Proposal 110 fully subsumed.** Rule 25 (v4.58 line 738) already contains the exact substance of proposal 110 ("deposited to resolved/ — NEVER to pending/"). Recommend advancing proposal 110 to `status='implemented'` with no PLANNER_TEMPLATE edit. This reduces the distinct-edit count from 16 to 15.

### Flags for Next Step
- **DEV anchor map confirmed.** All 9 edits have verbatim anchor text cited from v4.58. DEV must verify each before editing.
- **Three in-place edits need exact-string care:** Edit 5 (WA#8), Edit 6 (WA#12), and Edit 8 (WA preamble numbering) all use exact old_string matching. Em-dashes (–), smart quotes, and whitespace must match precisely.
- **Edit ordering matters.** The recommended order (Edit 4 → 1 → 2 → 3 → 8 → 5 → 6 → 7 → 9) processes sections top-to-bottom to minimize anchor drift from earlier insertions.
- **Edit 7 depends on Edit 6.** WA#13 and WA#14 insert after the strengthened WA#12's new source footer line. DEV must complete Edit 6 before Edit 7.
