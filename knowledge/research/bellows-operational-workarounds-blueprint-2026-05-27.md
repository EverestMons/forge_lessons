# Blueprint: Bellows Operational Workarounds — 2026-05-27

**Plan:** `executable-planner-template-bellows-operational-workarounds-2026-05-27`
**Step:** 1 (SA blueprint)
**Date:** 2026-05-27

---

## 1. Subsection header text

The new `### Bellows Operational Workarounds` subsection is placed as the final subsection of `## Bellows Execution Model (Layer 1 Autonomous Dispatch)` — after `### Restart Discipline` ends (line 1157) and before the `---` separator (line 1159) preceding `## Manual Execution Model`. The heading level is `### ` (L3), matching all existing Bellows Execution Model subsections (`### What Bellows Is`, `### Plan Lifecycle States`, `### Restart Discipline`, etc.). Individual workarounds use `#### N.` (L4) — one level deeper than the subsection heading, which is the correct hierarchical depth since the subsection itself is L3.

**Full intro text:**

```markdown
### Bellows Operational Workarounds

These workarounds document operational procedures and constraints that arise from Bellows daemon behavior that is correct-as-designed but requires specific Planner or operator awareness to avoid failure modes. Each workaround addresses a gap between what the Planner or agent might assume and what Bellows actually does — claim-time caching, filename-prefix watching, teardown cherry-pick semantics, or daemon restart behavior.

Workarounds use independent numbering (1–12) scoped to this subsection. When the underlying daemon behavior is fixed — typically via a BACKLOG entry shipped as an executable plan — the corresponding workaround is deprecated and removed. The independent numbering convention signals deprecate-wholesale semantics: workarounds can be retired individually without renumbering Orchestration Plan Rules, and the entire subsection can be removed when all underlying daemon behaviors are resolved.
```

---

## 2. Final rule-count breakdown

### Decision A: Proposal 82 split

**Decision:** 1 numbered workaround with three labeled sub-points (A), (B), (C).

**Reasoning:** The three sub-rules share the common theme of "worktree lifecycle awareness" — they all concern the Planner/operator recognizing and responding to worktree state during Bellows-dispatched plan execution. They would all deprecate at the same time (when daemon worktree handling improves — better pruning, better empty-detection, better restart-state tracking). Keeping them as labeled sub-points under a single workaround communicates their shared scope and shared deprecation trigger. Three separate workarounds would scatter a unified concern across three independent numbers and obscure the fact that they share a single root context. The Plan Authoring Checklist precedent groups related mechanical checks as single entries; the same principle applies here.

### Decision B: Proposals 74+85 join

**Decision:** Single combined workaround covering both shapes.

**Reasoning:** Both proposals address the claim-time cache constraint as their root cause. Proposal 85 establishes the foundational constraint ("Bellows caches plan content at claim-time; it does NOT re-read mid-execution"), and proposal 74 derives the communication rule from that constraint ("addenda flow downstream via verdict reasoning text, not upstream via blueprint file edits"). Separating them would create two adjacent workarounds where the second requires reading the first to understand why the rule exists — a sign they belong together. The combined workaround first states the mechanism (claim-time caching), then derives both consequences (target fresh-read documents; use verdict reasoning text). The combined shape is more actionable because an operator encountering the cache constraint immediately sees both response patterns in one place.

### Final count

**12 workarounds.** Baseline 13 proposals → minus 1 for the 74+85 join → 12 numbered workarounds. Proposal 82 stays as 1 workaround with 3 sub-points (no net count change from baseline).

---

## 3. Per-workaround blueprint

### Workaround 1

**Working title:** Use structured JSON fields for log analysis, not raw_output grep

**Rule body:**

When analyzing `bellows/logs/*.json` for permission denials or other structured events, use the `parsed.permission_denials` array (or the relevant `parsed.*` field), not `grep`/substring-match against `raw_output`. The `raw_output` field contains tool-registry echoes where tool names and permission-related strings appear as part of the agent's available-tool inventory dump, not as actual denial events. Substring matching against `raw_output` produces systematic false positives — the 2026-05-26 WebSearch/WebFetch audit found a 22× false-positive rate (676 grep hits vs. 3 actual denial events) from this exact pattern. Always load the JSON and query the structured `parsed` fields.

**Cross-reference footer:** None — defensive analysis technique, not a daemon bug.

**Source attribution:** Source: proposal 65, lesson 2026-05-27

---

### Workaround 2

**Working title:** Serialize same-project plans by default

**Rule body:**

Serialize same-project plans by default. Parallel dispatch (via `parallel-N-` prefix) is safe only when plans target different git roots or when one plan does not write to `PROJECT_STATUS.md` or the project's feedback log. Two plans dispatched in parallel within the same project that both append to shared bookkeeping files (`PROJECT_STATUS.md`, `agent-prompt-feedback.md`) will conflict at worktree teardown — the second cherry-pick aborts because the first plan's append altered the same byte ranges. Sequential dispatch eliminates the teardown conflict entirely; the cost is wall-clock time, which is always cheaper than manual conflict-resolution surgery.

**Cross-reference footer:**

Workaround for: bellows/knowledge/BACKLOG.md "Parallel-diagnostic cherry-pick conflicts on shared bookkeeping files at teardown" (added 2026-05-22)

**Source attribution:** Source: proposal 68, lesson 2026-05-27

---

### Workaround 3

**Working title:** Target fresh-read documents for mid-plan communication, not cached plan files

**Rule body:**

Bellows caches plan content at claim-time — the `executable-*` → `in-progress-*` rename writes a `.bellows-cache/*.pristine` shadow copy, and the agent's bootstrap prompt is generated from this cached content. Bellows does NOT re-read plan content mid-execution. Two consequences follow. First, verdict-time overrides (CEO addenda during plan execution) must target documents the next agent reads fresh — UXD design files, DEV logs, research deposits, or the verdict reasoning text itself — not the cached plan file. Edits to the plan file after dispatch are invisible to the executing agent. Second, CEO addenda during plan execution flow downstream via verdict reasoning text, not upstream via blueprint file edits. Blueprints are fixed artifacts after dispatch; the verdict `{reason}` field is the only communication channel that reaches the agent at step-resume time.

**Cross-reference footer:** None — claim-time cache is the daemon's design contract.

**Source attribution:** Source: proposals 74 and 85, lesson 2026-05-27

---

### Workaround 4

**Working title:** Restrict Planner renames to safe lifecycle destinations only

**Rule body:**

The Planner's safe rename destinations for plan files in `knowledge/decisions/` are: `Done/<canonical>` (strip lifecycle prefix), `halted-<canonical>`, `obsolete-<canonical>`, and `_staging_*` (temp paths). Never rename through `verdict-pending-*`, `in-progress-*`, or other daemon-watched prefixes — these are Bellows's lifecycle states, and renaming a file into one of them triggers the watcher's `on_moved` handler, which treats the file as a new plan event. Specifically: renaming a file to `verdict-pending-*` causes Bellows to treat it as a stale verdict-pending plan on the next rescan; renaming to `in-progress-*` is interpreted as an already-claimed plan. The only safe Planner-initiated rename destinations are the four listed above.

**Cross-reference footer:** None — daemon-watched filename-prefix semantics, no daemon-side fix candidate.

**Source attribution:** Source: proposal 70, lesson 2026-05-27

---

### Workaround 5

**Working title:** Match verdict-response filenames to request filenames exactly

**Rule body:**

When writing a verdict response file to `bellows/verdicts/resolved/`, copy the verdict-request filename exactly, replacing the `verdict-request-` prefix with `verdict-`. Do not add suffixes, timestamps, or other qualifiers. Before writing, check `verdicts/resolved/` for an existing `processed-verdict-*` file with the same slug-step combination — if one exists from a prior consumption cycle, it indicates the verdict was already processed and a new write would create a duplicate. The `_consume_verdicts()` parser matches verdict files to pending plans by slug and step number extracted from the filename; non-canonical filenames silently fail to match and are left unprocessed in `resolved/`.

**Cross-reference footer:** None — verdict filename discipline; daemon-side parser is correct as-built.

**Source attribution:** Source: proposal 81, lesson 2026-05-27

---

### Workaround 6

**Working title:** Use only recognized pause_for_verdict values

**Rule body:**

The `pause_for_verdict` header field accepts exactly three values: `always`, `after_step_1`, and `after_qa_step`. Any other value — including typos, `never`, `none`, `false`, or empty strings after trimming — silently evaluates to no-pause (the `header_says_pause()` function returns `False` for unrecognized values). There is no validation error or warning for most invalid values (a WARN is emitted only for non-empty unrecognized values since v4.47, but it does not block dispatch). When authoring multi-step plans, always use one of the three recognized values verbatim. The Planner's Plan Authoring Checklist should catch unrecognized values at deposit time; this workaround documents the daemon-side behavior for the case where a non-standard value reaches dispatch.

**Cross-reference footer:** None — silent-no-pause-on-invalid-value is daemon parser permissiveness; no fix filed.

**Source attribution:** Source: proposal 94, lesson 2026-05-27

---

### Workaround 7

**Working title:** Account for daemon restart when planning in-plan filesystem migrations

**Rule body:**

When a fix-plan changes daemon code that runs on every rescan cycle, in-plan filesystem migrations against files the old code touches are ineffective until the daemon restarts. The running daemon continues executing pre-fix code through the entire fix-plan's lifecycle — including through the plan's own DEV and QA steps. A plan that (a) fixes a rescan-cycle code path and (b) attempts an in-plan filesystem migration that depends on the fix has a structural ordering problem: the migration runs under the old code, which may undo, re-trigger, or misinterpret the migration. Three resolution strategies exist: (1) post-restart manual action (document the migration in the plan's Output Receipt, execute after daemon restart), (2) daemon-pause (stop Bellows before the migration step, restart after), or (3) self-healing convergence (design the fix so the new code converges to correct state regardless of pre-fix filesystem state on first post-restart rescan).

**Cross-reference footer:** None — restart-discipline cost; documented in `### Restart Discipline` subsection above.

**Source attribution:** Source: proposal 71, lesson 2026-05-27

---

### Workaround 8

**Working title:** Check for active worktrees before editing project files

**Rule body:**

Before editing any file under a project path during plan execution, check `.bellows-worktrees/` for active worktrees on the in-flight plan. If an active worktree exists for the plan's slug, the agent is executing in a worktree — direct file edits to the project's main working tree from outside the worktree are invisible to the agent and will conflict at teardown cherry-pick. When an active worktree is detected and the Planner or CEO needs to communicate a change to the executing agent, use the verdict-channel addendum (write the change into the verdict `{reason}` field for the current or next step) instead of editing files in the main working tree directly.

**Cross-reference footer:** None — worktree-active-during-edit; no daemon-side fix filed.

**Source attribution:** Source: proposal 73, lesson 2026-05-27

---

### Workaround 9

**Working title:** Verify origin delivery before authoring worktree recovery commits

**Rule body:**

Before authoring recovery commits for a worktree teardown `gate_failure`, run `git fetch origin` and check whether the agent's work already landed on `origin` via the worktree's direct push. Bellows worktrees push commits directly to origin during execution; the teardown cherry-pick onto local `main` is a secondary delivery path. A teardown `gate_failure` (cherry-pick conflict) does not mean the work is lost — it means the local `main` branch didn't receive the commit, but `origin/main` may already have it. If `git log origin/main` shows the agent's commit(s), the recovery path is `git reset --hard origin/main` (or `git pull --ff-only`) on local `main`, not authoring new recovery commits that duplicate already-shipped work.

**Cross-reference footer:** None — omitted. The plan's mapping table flagged a loose relationship to BACKLOG entry "Worktree teardown cherry-pick conflict on dirty PROJECT_STATUS.md" (added 2026-05-22), but proposal 77's concern (checking origin before authoring recovery commits) is orthogonal to that entry's concern (dirty working tree during cherry-pick). The BACKLOG entry addresses the cherry-pick conflict mechanism; proposal 77 addresses avoiding unnecessary recovery by checking origin first. The cross-reference would be misleading.

**Source attribution:** Source: proposal 77, lesson 2026-05-27

---

### Workaround 10

**Working title:** Worktree lifecycle awareness — prune, halt, and recognize fresh-claim

**Rule body:**

Three worktree lifecycle situations require specific operator or Planner responses:

**(A) Pre-flight stale worktree prune.** Before dispatching a new plan to a project, check `.bellows-worktrees/` for stale worktrees from prior plan runs. Stale worktrees (from halted or failed plans whose teardown didn't complete) consume disk space and can cause `git worktree add` failures if the branch name collides. Prune stale worktrees via `git worktree remove <path>` before dispatch.

**(B) Halt on second consecutive teardown-empty for same step.** If Bellows reports a teardown-empty result (worktree had no commits to cherry-pick) for the same plan-step combination twice consecutively, halt and investigate. A single teardown-empty can occur legitimately (agent read files but made no changes). Two consecutive teardown-empties for the same step indicate the agent is being dispatched but producing no output — likely a bootstrap-prompt or permission issue that the agent cannot self-report because it has no output channel outside the worktree commit.

**(C) Recognize daemon-restart fresh-claim state.** After a daemon restart, Bellows re-scans `knowledge/decisions/` and may re-claim `in-progress-*` plans that were mid-execution before the restart. The re-claimed plan starts from the beginning of its current step, not from where the prior agent left off — Bellows has no step-resume state. If a re-claimed plan's prior agent already completed substantive work (commits pushed to origin, deposits written to the worktree), the fresh-claim dispatch will duplicate that work. When this state is detected (plan was `in-progress-*` before restart, agent output from prior run exists), issue a `verdict: stop` and close the plan manually rather than allowing the fresh-claim dispatch to proceed.

**Cross-reference footer:** None — worktree lifecycle awareness; no daemon-side prune scheduled.

**Source attribution:** Source: proposal 82, lesson 2026-05-27

---

### Workaround 11

**Working title:** Reconcile local/origin divergence at session start

**Rule body:**

At session start, run `git fetch origin && git status` for each active project. If local `main` and `origin/main` have diverged — particularly if `git diff main origin/main` shows empty (identical content, different commit histories from cherry-pick vs. direct-push delivery paths) — resolve via `git reset --hard origin/main`. This situation arises when a prior session's worktree teardown cherry-picked commits onto local `main` while the worktree also pushed directly to `origin/main`, creating parallel commit histories with identical content. Left unresolved, the divergence causes every subsequent `git push` to fail or require force-push. The empty-diff check confirms the histories are content-identical before the hard reset.

**Cross-reference footer:** None — origin/local divergence symptom on local recovery, not a daemon bug.

**Source attribution:** Source: proposal 78, lesson 2026-05-27

---

### Workaround 12

**Working title:** Final-step gate_failure recovery checklist

**Rule body:**

When a plan's final step trips a `gate_failure` but the substantive work has been verified as shipped (deposits exist, code changes committed, tests passing), follow this recovery sequence: (1) verify substance shipped — read deposits, confirm file existence on disk, check `git log` for the agent's commits; (2) issue `verdict: stop` — a continue verdict on a gate-failed final step can trigger unpredictable behavior depending on which gate failed; (3) move the plan from `in-progress-*` (or `verdict-pending-*`) to `Done/halted-but-shipped-<canonical>` — the `halted-but-shipped-` prefix signals that the plan was halted by gate failure but the deliverables are verified-good; (4) archive verdict files — move the verdict request and any resolved verdict to `verdicts/pending/archived/`; (5) note the gate failure and recovery in `PROJECT_STATUS.md` with the `halted-but-shipped` disposition.

**Cross-reference footer:** None — final-step gate_failure recovery flow; the gate-failure pause itself is correct behavior.

**Source attribution:** Source: proposal 89, lesson 2026-05-27

---

## 4. Insertion-point specification

**Target file:** `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (current v4.54, 1598 lines)

**Insertion location:** After `### Restart Discipline` content ends (line 1157) and before the `---` separator (line 1159). The new subsection is the final subsection of `## Bellows Execution Model (Layer 1 Autonomous Dispatch)` (line 1035).

**Surrounding context lines:**

| Anchor | Line | Content |
|---|---|---|
| Last Restart Discipline content | 1157 | Ends with: `...means the gate trip is a known cost of parser fix-plans, not a signal to halt.` |
| Blank line | 1158 | (empty) |
| Section separator (DEV inserts BEFORE this) | 1159 | `---` |
| Blank line | 1160 | (empty) |
| Next section | 1161 | `## Manual Execution Model (RUN EXE / RUN DIAG / Bootstrap)` |

**DEV edit anchor:** The `old_string` for the Edit tool should capture the blank line + `---` + blank line + `## Manual Execution Model` sequence at lines 1158–1161. The `new_string` inserts the full `### Bellows Operational Workarounds` subsection (heading, intro, all 12 workarounds) before the `---`, preserving the `---` and `## Manual Execution Model` unchanged after the insertion.

**No version bump.** The `**Version:** 4.54` line at line 5 stays unchanged. Version bump happens at session-wrap, not in this plan.

---

## 5. BACKLOG verification

Direct read of `/Users/marklehn/Developer/GitHub/bellows/knowledge/BACKLOG.md` Open section completed. Results:

### Confirmed mappings

| Proposal | BACKLOG match? | Entry title (verbatim) | Date |
|---|---|---|---|
| 68 | **Yes** | "Parallel-diagnostic cherry-pick conflicts on shared bookkeeping files at teardown" | added 2026-05-22 |

### Mapping corrections from Context section

| Proposal | Context section said | SA finding | Action |
|---|---|---|---|
| 77 | "Loosely related — Worktree teardown cherry-pick conflict on dirty PROJECT_STATUS.md (added 2026-05-22). SA decides if cross-ref is accurate enough to cite, or omit footer" | **Omit.** Proposal 77 (checking origin before authoring recovery commits) is orthogonal to the BACKLOG entry's concern (dirty working tree causes cherry-pick abort). Both involve worktree teardown context but address different failure modes. A cross-reference would imply the BACKLOG fix would deprecate the workaround, which it would not — the origin-check discipline is valid regardless of whether the dirty-tree cherry-pick bug is fixed. | No cross-reference footer on Workaround 9 |

### All other proposals confirmed as no-match

| Proposal | Context section said | SA confirms |
|---|---|---|
| 65 | No — defensive analysis technique | Confirmed. No BACKLOG entry about log analysis false positives. |
| 70 | No — daemon-watched filename-prefix semantics | Confirmed. No BACKLOG entry about filename-prefix watching behavior. |
| 71 | No — restart-discipline cost | Confirmed. Restart Discipline is documented in PLANNER_TEMPLATE, not a BACKLOG item. |
| 73 | No — worktree-active-during-edit | Confirmed. No BACKLOG entry about worktree-aware file editing. |
| 74 | No — claim-time cache design choice | Confirmed. Claim-time caching is design, not a bug. |
| 78 | No — origin/local divergence symptom | Confirmed. No BACKLOG entry about session-start divergence. |
| 81 | No — verdict filename discipline | Confirmed. Daemon-side parser is correct; the discipline is Planner-side. |
| 82 | No — worktree lifecycle awareness | Confirmed. No BACKLOG entry about worktree pruning, teardown-empty, or fresh-claim. |
| 85 | No — claim-time cache design contract | Confirmed. Same as proposal 74. |
| 89 | No — gate_failure recovery flow | Confirmed. Gate-failure pause is correct behavior. |
| 94 | No — daemon parser permissiveness | Confirmed. No fix filed for silent-no-pause. |

### Additional BACKLOG matches checked

Scanned all 9 Open entries in BACKLOG.md against the 13 proposals. No additional matches found beyond proposal 68. The Open entries cover: `rule_22_verification` (c) false positives (2026-05-27), hedging-detector false positives (2026-05-27), orphan-guard renormalization (2026-05-27), worktree teardown cherry-pick (2026-05-22), parallel-diagnostic cherry-pick (2026-05-22 — matches proposal 68), Bellows status UI (2026-05-21), deposits parser parenthetical qualifiers (2026-05-21), no-match verdict warning rate-limit (2026-05-21), and `_extract_step_text` regex case-sensitivity (2026-05-13). None of the remaining 8 Open entries map to any of the 13 proposals beyond the confirmed match.

---

## Output Receipt

**Agent:** Forge Systems Analyst
**Step:** 1
**Status:** Complete

### What Was Done

Produced the full SA blueprint for the new `### Bellows Operational Workarounds` subsection under `## Bellows Execution Model` in PLANNER_TEMPLATE.md v4.54. Blueprint specifies 12 numbered workarounds derived from 13 source proposals, with two SA decisions resolving the rule count: proposal 82 ships as 1 workaround with 3 labeled sub-points (A/B/C), and proposals 74+85 ship as 1 combined workaround. BACKLOG cross-reference verification confirmed 1 match (proposal 68) and corrected 1 loose mapping (proposal 77 → omit). Insertion-point specification anchored to lines 1157–1161 of the current file.

### Files Deposited

- `lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md` — full blueprint with subsection header text, rule-count decisions, 12 per-workaround blueprints, insertion-point specification, and BACKLOG verification

### Decisions Made

- Proposal 82 split: **1 workaround with 3 sub-points** — shared worktree-lifecycle theme, shared deprecation trigger, compact grouping preferred
- Proposals 74+85 join: **single combined workaround** — claim-time cache is the shared root cause, mechanism + consequence belong together
- Final rule count: **12 workarounds** (13 proposals minus 1 for the 74+85 join)
- Proposal 77 BACKLOG mapping: **omitted** (orthogonal concerns; cross-reference would be misleading)

### Flags for CEO

- **BACKLOG mapping correction:** Proposal 77's loose mapping to "Worktree teardown cherry-pick conflict on dirty PROJECT_STATUS.md" was evaluated and omitted. The plan's Context section flagged this as an SA decision — SA decided the mapping is too loose to cite. The proposal 77 workaround (check origin before authoring recovery commits) addresses a different failure mode than the BACKLOG entry (dirty working tree during cherry-pick). No other BACKLOG mapping corrections.
- **Rule count 12 vs. headline 14:** The plan's NEXT_SESSION.md headline target was "14 rules" (informational, not binding). The blueprint produces 12 workarounds. The difference: proposals 82 ships as 1 (not 3), and proposals 74+85 join into 1 (not 2). The substantive content coverage is identical — all 13 proposals are represented. The lower count reflects tighter authoring, not dropped scope.

### Flags for Next Step

- **DEV anchor lines confirmed:** Line 1157 (end of Restart Discipline), line 1159 (`---`), line 1161 (`## Manual Execution Model`). DEV should anchor the Edit old_string on the blank line + `---` + blank line sequence at lines 1158–1160, inserting the new subsection above the `---`.
- **Heading level:** Individual workarounds use `#### N.` (L4), not `### N.` (L3). This differs from the Plan Authoring Checklist precedent (which uses `### N.` because the section is `## ` L2). The Bellows Operational Workarounds subsection is `### ` L3, so items are one level deeper at `#### ` L4. DEV should verify this matches the heading hierarchy.
- **Prose style:** Workaround rule bodies are single-paragraph prose (matching the plan's specification). Workaround 10 is the exception — it uses three labeled sub-points (A/B/C) per the SA decision on proposal 82. Each sub-point has a bold label and 2-3 sentence body.
- **Cross-reference footer placement:** Only Workaround 2 (proposal 68) has a cross-reference footer. The footer line appears after a blank line following the rule body, before the Source attribution footer. All other workarounds skip directly from rule body to Source attribution.
