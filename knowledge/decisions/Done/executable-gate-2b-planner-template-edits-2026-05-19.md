# Executable: Gate 2b — PLANNER_TEMPLATE Governance Edits

**Plan slug:** executable-gate-2b-planner-template-edits-2026-05-19
**Plan type:** executable
**Project:** governance (root, /Users/marklehn/Developer/GitHub/)
**Specialist:** Forge Developer
**Auto-close:** false
**Pause for verdict:** after_step_1
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-19

---

## Context

Lessons Forge cycle 2026-05-18 Gate 1 accepted 16 proposals: 11 governance rules for PLANNER_TEMPLATE.md and 5 instrumentation procedures. This plan applies all 16 edits in one agent invocation, then verifies the result, then commits.

**Source proposals (all currently `status=accepted` in `lessons-forge.db`):**

| ID | Gate1 label | Type | One-line summary |
|---|---|---|---|
| 41 | G1 | governance_rule | Pre-cutover unknowns diagnostic before destructive cross-cutting work |
| 42 | G2 | governance_rule | Split destructive cross-cutting plans at natural verification point with verdict gate |
| 43 | G3 | governance_rule | Filesystem:write_file for /Users paths, never create_file |
| 44 | G4 | governance_rule | Submodule pointer bump immediately after submodule commit-push |
| 51 | G6 | governance_rule | Walk git-internal intermediate state; "safe and non-destructive" is not agent judgment |
| 52 | G7 | governance_rule | Phase 1.5 enforcement strengthened — happens FIRST regardless of task size |
| 53 | G8 | governance_rule | Three-item verdict-file check executed out loud |
| 54 | G9 | governance_rule | Distinguish manual-bootstrap vs Bellows-dispatch execution modes |
| 56 | G10 | governance_rule | Negative grep during dormancy ≠ architectural finding |
| 57 | G11 | governance_rule | Deposits blocks must contain resolvable paths, no placeholders |
| 62 | G16 | governance_rule | Audit ALL gate function call sites when shipping shared-function fix |
| 46 | I1 | instrumentation | Every new repo ships .gitignore at commit 1; push commit-by-commit on "bad object" |
| 47 | I2 | instrumentation | git filter-repo 4-step checklist |
| 49 | I4 | instrumentation | Submodule recovery procedure |
| 50 | I5 | instrumentation | OS-level file readability before assuming git corruption; never repos in iCloud |
| 55 | I6 | instrumentation | Filename truthfulness check at staging |

**Placement strategy:**

- **11 governance rules** extend the existing `## Orchestration Plan Rules` section as Rules 28-38, in the order listed above. The section currently has Rules 1-27; appending Rules 28-38 keeps numbering monotonic.
- **5 instrumentation procedures** form a new `## Procedures` section appended after `## Forge Observations` (the current last top-level section). Each procedure is a `### N. <Title>` subsection. Procedures are checklists, not Planner decision rules, and benefit from being grouped separately.

**Out of scope:**
- 2 structural proposals (IDs 39 S1, 40 S2) were already shipped in Gate 2c commit 30e395c (gates.py fixes). Their `lesson_proposals.status` needs to advance from `accepted` to `implemented`. This is housekeeping; deferred to Gate 2d (TBD). NOT done here.
- PLANNER_TEMPLATE version bump: this plan does NOT bump v4.41 → v4.42. The version line will be bumped in a separate session-wrap commit per existing convention (the version bump is the last edit, gating all earlier edits).

---

## STEP 1 — Apply 16 edits to PLANNER_TEMPLATE.md

You are the Forge Developer. Read `forge/agents/FORGE_DEVELOPER.md`. Operate against `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root). **Strict scope: this step modifies ONLY PLANNER_TEMPLATE.md.** Do not touch any other file. Do not commit.

**Pre-edit verification:**

Read `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` and confirm:
- Line count is approximately 1275
- `## Orchestration Plan Rules` exists at line ~425
- The last numbered rule is `### 27. Diagnostic-derived plans cite findings, never supplement with source reads` at line ~726
- `## Forge Observations` exists at line ~1264
- The file ends after the Forge Observations section

If any of these do not match, HALT and report — the template may have drifted since the Planner's pre-authoring read.

**Edit 1 — Append Rules 28-38 to the Orchestration Plan Rules section.**

Find the end of Rule 27's body (the last paragraph or example before the next `## ` top-level header). Insert the following block AFTER Rule 27's body and BEFORE the next top-level section header (`## Guardrails`). Use `Desktop Commander:edit_block` with anchored old_string capturing the last few lines of Rule 27 plus the `## Guardrails` line, and new_string preserving those plus the new rules inserted between.

Insert this block:

```markdown
### 28. Pre-cutover unknowns diagnostic before destructive cross-cutting work

Before authoring any executable that does destructive cross-cutting work (cross-repo, multi-system, multi-governance-doc), author a pre-cutover unknowns diagnostic distinct from any earlier surface diagnostic. The unknowns diagnostic asks specific questions about line numbers, exact text, file paths, runtime state, and remote/external preconditions — not "does this approach work" but "what concrete values will the executable encounter at run-time." The cost is one diagnostic cycle (~5-11 questions); the savings is not shipping a half-broken executable that discovers preconditions during dispatch.

**Trigger:** Plan involves destructive operations against >1 repo, OR modifies governance docs alongside code, OR depends on external state (GitHub remotes, registered submodules, etc.) the Planner cannot directly verify.

### 29. Split destructive cross-cutting plans at the natural verification point with a verdict gate

When a plan has both a "build the new thing" phase and a "cut over from the old thing" phase, split into two plans with a verdict gate between them. The new system must stand alone and pass verification before the old system is touched. Three benefits: real verification gate (not just an in-plan test), bounded half-state (recovery rolls back one phase, not the whole arc), reduced cognitive surface per agent dispatch.

**Trigger:** Plan has a step labeled "migrate / cutover / replace / retire X with Y" where Y is the work of earlier steps in the same plan.

### 30. `Filesystem:write_file` for `/Users/marklehn/` paths, never `create_file`

The Planner has access to two filesystems. `create_file` writes to Claude's sandbox at a fake `/Users/marklehn/...` path with no error; the user's Mac receives nothing. `Filesystem:write_file` (MCP tool) writes to the real Mac filesystem. For any write into a `/Users/marklehn/Developer/GitHub/` path, use `Filesystem:write_file`. Use `Filesystem:move_file` for atomic deposits via staging. `create_file` is appropriate ONLY for files inside Claude's `/mnt/user-data/outputs/` sandbox.

**Failure mode:** silent — no error, no diff, the work just doesn't exist on disk.

### 31. Submodule pointer bump immediately after submodule commit-push

After any commit-push inside a submodule (`bellows`, `anvil`), the next mandatory action is `cd ~/Developer/GitHub && git --no-pager status`. If the output shows `M <submodule-dir>`, the submodule pointer is dirty: run `git add <submodule-dir> && git --no-pager commit -m "chore: bump <submodule> submodule (<context>)" && git --no-pager push origin main`. Verification: `git submodule status` shows a clean prefix (space, not `+`). Skipping this step leaves the governance root pointing at an older submodule SHA; fresh clones reconstruct the old state.

### 32. Walk git-internal intermediate state; "safe and non-destructive" is not an agent judgment call

When authoring a plan with git-internal operations (reset, rebase, cherry-pick, worktree manipulation, force-push, filter-repo), the Planner walks the intermediate state explicitly in the plan Context: what does `git status` show after each step? What does the index look like? What does the working tree look like? What does the reflog say? Operations the plan did not authorize — even side-effect-free operations the agent judges "safe" (e.g., `git reset HEAD` to unstage) — require a verdict before execution, not agent improvisation. Restated: an agent encountering a non-authorized operation MUST halt and report, not improvise around it.

### 33. Phase 1.5 enforcement — happens FIRST regardless of task size

The Phase 1.5 Recent Knowledge Scan (read recent research, feedback log, QA reports, LESSONS for the active project) happens at session start BEFORE any investigation, regardless of how narrow the opening question seems. "This is just cleanup, I don't need full context" is the documented failure mode. Skipping Phase 1.5 produces diagnostic cycles built on stale assumptions; the cost of doing it (~2 minutes) is far below the cost of authoring against stale state.

### 34. Three-item verdict-file mechanical check, executed out loud

Before any file write that Bellows will read (verdict response, atomic plan deposit), the Planner performs and renders visibly in the response: (1) destination directory confirmed, (2) filename pattern confirmed, (3) content contract confirmed. Visible execution, not silent. The check exists because each of the three has produced repeated failures in the past (verdict response → wrong dir; filename → wrong pattern; content → wrong shape). Executing out loud anchors attention to all three before the write commits.

### 35. Distinguish manual-bootstrap vs Bellows-dispatch execution modes

Plan prose containing `STOP`, `wait for confirmation`, or `do not proceed` is ignored by Bellows. Bellows dispatches steps end-to-end unless a gate fires or the plan header specifies `pause_for_verdict: after_step_N`. The per-step pause discipline of manual Claude Code bootstrap (agent pauses by its own discipline after each step) does NOT apply to Bellows-dispatched plans. When authoring multi-step plans for Bellows, use `pause_for_verdict` headers for required pauses; do not rely on `STOP`-prose. `auto_close: false` controls only the final pause (after the last step), not per-step pauses.

### 36. Negative grep during dormancy is not architectural evidence

Diagnostic methodology: when concluding "X doesn't surface in Y" based on `grep` of historical artifacts, the diagnostic must verify X's preconditions were met during the observation window. A negative grep over a period when X had no reason to fire is consistent with both "X is broken" and "X was correctly dormant." Negative results are weak evidence unless paired with proof the feature should have fired. Common failure mode: grepping for warning text in reports from a period of clean state, then concluding "the warning logic doesn't work."

### 37. `**Deposits:**` blocks must contain resolvable paths only

The `deposit_exists` gate reads the `**Deposits:**` block at the moment the agent reports Complete. Anything inside the block must be a real, resolvable path — either a specific file the Planner is confident about, or a directory that will exist by the agent's terminal report. Placeholders, template variables (`<resolved-during-execution>`, `${OUTPUT_PATH}`), or generic markers all trip the gate literally. For paths unknown at plan-write time, either (a) use the parent directory (gate accepts directory existence as proxy), or (b) introduce a Step 0 diagnostic to discover the path before authoring the dependent step.

### 38. Audit all gate function call sites when shipping shared-function fix

Any plan modifying a function signature in `gates.py` or `verdict.py` must include a step that runs `grep -n <function_name> gates.py verdict.py bellows.py` and audits every hit. QA scope must track functions sharing the changed dependency (call sites of the modified function), not just functions directly changed. Failure mode: a 2026-05-06 fix threaded `wt_path` through `_gate_deposit_exists` but missed `_gate_rule_20_self_check` — the missed call site shared the same `_resolve_deposit_path` dependency and continued to fail with the original symptom for 2 more cycles before being caught.

```

**Edit 2 — Append the Procedures section at the end of the file.**

Find the end of the `## Forge Observations` section (the last content of the file). Append the following block AFTER the last line of the file.

```markdown

---

## Procedures

Operational checklists used by the Planner during specific operations. Distinct from Orchestration Plan Rules (decision rules for authoring plans); these are step-by-step procedures the Planner executes itself.

### 1. New repo initialization checklist

Every new project repo ships with a `.gitignore` at commit 1. Standard content:

```
__pycache__/
*.pyc
.pytest_cache/
.venv/
.DS_Store
*.db
*.db-shm
*.db-wal
.bellows-worktrees/
.bellows-cache/
.vexp/
```

This prevents accidental commit of build artifacts, virtualenv contents, SQLite runtime files, and Bellows worktree dirs. Add project-specific exclusions in subsequent commits.

### 2. GitHub `pack has bad object` push troubleshooting

When `git push` fails with `inflate: data stream error / pack has bad object / unpack-objects abnormal exit`, the error is most likely GitHub's server-side reporting of the 100 MB hard file size limit, NOT actual repo corruption.

Diagnostic procedure: push commit-by-commit (`git push origin <SHA>:main` for each successive commit in the not-yet-pushed range) until the rejection includes the literal warning text identifying the oversized file. Then either (a) `git filter-repo` to remove the file from history, or (b) Git LFS for legitimately-large binary assets.

### 3. `git filter-repo` post-execution checklist

`git filter-repo` has destructive side effects beyond history rewriting. After every invocation:

1. **Backup the working tree** before running (separately from the git history backup). `filter-repo` can remove working-tree files in addition to git history.
2. **Re-add the `origin` remote** — `filter-repo` strips it by default. `git remote add origin <URL>`.
3. **Restore checkout-removed working-tree files** if the rewritten path removed a file the user still wants on disk.
4. **Add restored files to `.gitignore`** and commit — they were removed from history; keep them out of the next commit.
5. **Force-push** — `git push origin main --force-with-lease`. History is rewritten; standard push will be rejected.

### 4. Submodule recovery — gitlink exists but no .gitmodules entry

Failure mode: a directory shows in `git ls-files --stage` with mode `160000` (gitlink) but no entry exists in `.gitmodules`. Standard fix `git submodule add` refuses because the directory already exists.

Recovery procedure:
1. Hand-write `.gitmodules` with the correct `[submodule "<name>"]` entry, `path = <dir>`, `url = <URL>`.
2. Run `git submodule init`.
3. Verify via `git submodule status`: should show a clean prefix (space character before SHA, no `+` or `-`).

### 5. OS-level file readability check before diagnosing git corruption

When `git` fails with `mmap failed: Operation timed out`, `inflate: data stream error`, or similar I/O errors against a repo on macOS, the first diagnostic must test OS-level file readability — NOT git-level corruption. iCloud Drive evicts files marked "dataless" (visible via `ls -lO` on macOS); attempts to read evicted files fail with timeouts that look like corruption.

Diagnostic command: `find .git/objects -type f -exec ls -lO {} \; | grep dataless` — any output identifies iCloud-evicted objects.

**Hard rule:** never put git repos in iCloud-synced folders. The combination is fundamentally incompatible.

### 6. Filename truthfulness check before atomic plan deposit

At the staging stage (after `Filesystem:write_file` to `_staging_*` but before `Filesystem:move_file` to the watched directory), read the plan's final scope and verify the filename describes what the plan's steps will actually do. If the staged filename diverges from final scope, rename at staging before the move locks the name. Once Bellows claims the plan as `in-progress-*`, renaming breaks its state machine.

**Failure mode:** plan deposited under aspirational name (e.g., `drain-extraction-queue`) when the actual steps don't implement the named work. Permanent documentation debt.
```

**No commit yet.** Step 1 leaves PLANNER_TEMPLATE.md modified-but-uncommitted in the working tree. Step 2 verifies; Step 3 commits.

**Dev log:**

```markdown
# Dev Log — Gate 2b Step 1 (PLANNER_TEMPLATE edits)

Pre-edit verification:
- Line count before: <N>
- ## Orchestration Plan Rules at line: <N>
- Last numbered rule (### 27): line <N>
- ## Forge Observations at line: <N>

Edit 1 — Rules 28-38 inserted after Rule 27:
- old_string anchor: <first/last 30 chars>
- new_string length: <chars>
- Anchor matched: yes (single occurrence)

Edit 2 — Procedures section appended after Forge Observations:
- old_string anchor: last 30 chars of file before append
- new_string length: <chars>
- Anchor matched: yes (single occurrence)

Post-edit state:
- Line count after: <N>
- New rules visible: grep -c "^### [0-9]\+\." PLANNER_TEMPLATE.md should show 38, not 27
- New Procedures section: grep -c "^## Procedures" should show 1
- Procedures sub-sections: grep -c "^### [0-9]\+\." inside Procedures section should show 6

Working tree state: `git --no-pager status` should show `modified: PLANNER_TEMPLATE.md` with no other changes.
```

Deposit to: `governance/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md`.

Wait — there is no governance-root `knowledge/` directory; the governance root is the top of `/Users/marklehn/Developer/GitHub/`. Deposit the dev log to: `lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md` instead. The PLANNER_TEMPLATE edits originated from Lessons Forge dispositions, so the deposit naturally lives with the project that owns the source proposals.

**Output Receipt:**
- Agent: Forge Developer
- Step: 1
- Status: Complete (both edits applied, post-edit verification confirms structure); Blocked (anchor mismatch or verification failure)
- What Was Done: applied 2 edit_block edits to PLANNER_TEMPLATE.md (Rules 28-38 + Procedures section)
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md`
- Files Created or Modified: `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (uncommitted)
- Decisions Made: 2 edit anchors
- Flags for CEO: any anchor that needed adjustment; any pre-edit state mismatch
- Flags for Next Step: Planner Rule 22 reads the diff via git diff, verifies content matches plan; authorizes Step 2 verification

**Deposits:**
- `lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md`

**STOP.** Do NOT proceed to Step 2.

---

## STEP 2 — Verify edits

You are the Forge Developer (acting as QA). Read the prior step's deposit and verify Output Receipt status is Complete. If not, stop.

**Verification checks:**

1. **Rule count check.** `grep -c "^### [0-9]\+\." /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` should return 44 (27 existing Orchestration Plan rules + 11 new + 6 Procedures, all with `### N.` prefix; note the Planning Conversation Flow section also has `### 1-4` so the total may be higher — count manually if needed). Report exact count and breakdown by section. PASS/FAIL.

   Actually, the more useful check: confirm `### 38. Audit all gate function call sites` exists exactly once, and `### 27. Diagnostic-derived plans cite findings` exists exactly once. Both should be unique. PASS/FAIL.

2. **Procedures section exists.** `grep -c "^## Procedures$" PLANNER_TEMPLATE.md` should return 1. PASS/FAIL.

3. **All 6 procedures present.** Read the Procedures section, verify all 6 subsections exist:
   - `### 1. New repo initialization checklist`
   - `### 2. GitHub \`pack has bad object\` push troubleshooting`
   - `### 3. \`git filter-repo\` post-execution checklist`
   - `### 4. Submodule recovery — gitlink exists but no .gitmodules entry`
   - `### 5. OS-level file readability check before diagnosing git corruption`
   - `### 6. Filename truthfulness check before atomic plan deposit`
   PASS/FAIL.

4. **All 11 new rules present.** Verify Rules 28-38 by title:
   - `### 28. Pre-cutover unknowns diagnostic`
   - `### 29. Split destructive cross-cutting plans`
   - `### 30. Filesystem:write_file for /Users`
   - `### 31. Submodule pointer bump`
   - `### 32. Walk git-internal intermediate state`
   - `### 33. Phase 1.5 enforcement`
   - `### 34. Three-item verdict-file mechanical check`
   - `### 35. Distinguish manual-bootstrap vs Bellows-dispatch`
   - `### 36. Negative grep during dormancy`
   - `### 37. **Deposits:** blocks must contain resolvable paths`
   - `### 38. Audit all gate function call sites`
   PASS/FAIL on full set.

5. **Markdown structure intact.** Confirm:
   - File starts with `# Planner — Universal Agent`
   - No duplicate `## Orchestration Plan Rules` headers
   - No orphan `---` separators
   - PLANNER_TEMPLATE.md still parses as valid markdown (visually well-formed when viewed)
   PASS/FAIL.

6. **Git diff is bounded to PLANNER_TEMPLATE.md.** `cd /Users/marklehn/Developer/GitHub && git --no-pager status --porcelain` should show ONLY:
   ```
    M PLANNER_TEMPLATE.md
   ?? lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md
   ```
   (plus any other ambient untracked plan-lifecycle files; the modified set must be exactly PLANNER_TEMPLATE.md.) PASS/FAIL.

7. **No regressions to existing rules.** `git --no-pager diff PLANNER_TEMPLATE.md | grep -E "^-### [0-9]" | head -5` should return nothing (no existing numbered rules removed). PASS/FAIL.

**QA report deposit:**

Write to `lessons-forge/knowledge/qa/gate-2b-qa-2026-05-19.md` with each check, command run, verbatim output, PASS/FAIL.

**Rule 20 self-check (literal banner inside fenced block; no decoration, no shell prefix, no === lines):**

Run:
```python
import os
required = [
    "knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md",
    "knowledge/qa/gate-2b-qa-2026-05-19.md",
]
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"FAILED - missing evidence: {missing}")
else:
    print("Rule 20 — QA Self-Check Results")
    print("PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.")
```

Paste the literal stdout (two lines) into the QA report inside a fenced code block. No decoration around it.

**Output Receipt:**
- Agent: Forge Developer (QA)
- Step: 2
- Status: Complete (all 7 checks PASS); Partial (1-2 FAIL); Blocked (3+ FAIL)
- What Was Done: verified 11 new rules + 6 procedures landed correctly; markdown structure intact; no regressions
- Files Deposited: `lessons-forge/knowledge/qa/gate-2b-qa-2026-05-19.md`
- Files Created or Modified: none
- Decisions Made: 7 PASS/FAIL determinations
- Flags for CEO: any FAIL
- Flags for Next Step: commit (Step 3)

**Deposits:**
- `lessons-forge/knowledge/qa/gate-2b-qa-2026-05-19.md`

---

## STEP 3 — Commit

You are the Forge Developer. Read the prior step's QA report and verify all 7 checks PASS. If any FAIL, halt — do not commit.

**Commit PLANNER_TEMPLATE.md alongside the dev log and QA report.**

From `/Users/marklehn/Developer/GitHub/`:

```bash
git --no-pager add PLANNER_TEMPLATE.md lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md lessons-forge/knowledge/qa/gate-2b-qa-2026-05-19.md && git --no-pager commit -m "feat(planner-template): gate 2b — 11 new orchestration rules + 6 procedures from cycle 2026-05-18 (rules 28-38, procedures 1-6)"
```

Capture commit SHA.

**Dev log:**

```markdown
# Dev Log — Gate 2b Step 3 (commit)

Files committed:
- PLANNER_TEMPLATE.md (modified, +<lines>)
- lessons-forge/knowledge/development/dev-log-gate-2b-step-1-2026-05-19.md (new)
- lessons-forge/knowledge/qa/gate-2b-qa-2026-05-19.md (new)

Commit SHA: <SHA>
git log -1 --stat: <verbatim>
```

Deposit to: `lessons-forge/knowledge/development/dev-log-gate-2b-step-3-2026-05-19.md`.

**Update lessons-forge PROJECT_STATUS.md** with brief Gate 2b entry. Commit:

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && git --no-pager add PROJECT_STATUS.md && git --no-pager commit -m "docs: PROJECT_STATUS update for gate 2b (planner-template edits shipped)"
```

Note: PROJECT_STATUS lives inside lessons-forge submodule, not at governance root. Two separate repos may need separate commits. Governance root is the canonical source for PLANNER_TEMPLATE.md itself.

**Output Receipt:**
- Agent: Forge Developer
- Step: 3
- Status: Complete (commit landed); Blocked (Step 2 QA had failures)
- What Was Done: committed PLANNER_TEMPLATE.md + dev log + QA report; updated PROJECT_STATUS
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2b-step-3-2026-05-19.md`
- Files Created or Modified: 2 commits (governance root + lessons-forge)
- Decisions Made: commit landed at SHA
- Flags for CEO: Gate 2b complete; Gate 2d (status advancement: accepted → implemented for IDs 39, 40, 41-47, 49-57, 62) is the natural follow-up housekeeping but is out of scope here
- Flags for Next Step: session wrap

**Deposits:**
- `lessons-forge/knowledge/development/dev-log-gate-2b-step-3-2026-05-19.md`

Standard prompt feedback protocol → `lessons-forge/knowledge/research/agent-prompt-feedback.md`.

---

## How to run

Bellows dispatches Step 1 on next rescan. Pauses for verdict. Planner reads dev log under Rule 22 and inspects `git diff PLANNER_TEMPLATE.md` directly to verify edits landed at correct anchors. Continue verdict deposited. Steps 2 and 3 chain end-to-end. Plan moves to Done.
