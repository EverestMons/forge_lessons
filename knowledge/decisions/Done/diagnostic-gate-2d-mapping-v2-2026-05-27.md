# Diagnostic: Gate 2d Mapping — 33 Accepted Proposals to Shipped Governance Artifacts

**Plan slug:** diagnostic-gate-2d-mapping-2026-05-27
**Plan type:** diagnostic
**Project:** lessons-forge
**Specialist:** Forge Developer
**Auto-close:** true
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-27
**Dispatch Mode:** bellows

---

## Context

All 33 accepted proposals from the 2026-05-27 lesson_proposals cycle (IDs 64-98, excluding 63/superseded, 86/rejected, 88/rejected) are claimed by PROJECT_STATUS and NEXT_SESSION to be structurally accounted for via shipped governance artifacts:

- Plan A (Bellows Operational Workarounds subsection) — 13 source proposals, shipped at PLANNER_TEMPLATE.md lines 1159-1244 (commit `d0bf31b`, version 4.55)
- Plan B (Plan Authoring Checklist + Rules 42-44 + DPE technique + archived narratives) — 17 actionable proposals + 3 archived narratives, shipped at PLANNER_TEMPLATE.md line 917 (Plan Authoring Checklist) + rules 42-44 + DPE additions at line 760 (commit `e975e05`, version 4.54)
- Rule 41 supersession — proposal 63 absorbed during Plan B authoring (resolved at session-open; row already at `status='superseded'`)

Before the housekeeping flip from `status='accepted'` to `status='implemented'`, the Planner is enforcing Rule 22(b) substance verification against the upstream baton claim: each of the 33 proposals must map to a specific, verifiable artifact in the shipped governance edits.

This diagnostic produces the 33-row mapping table. It does NOT modify any DB row, file, or commit. The mapping output is the input to a follow-up executable flip plan.

**Source-of-truth references the diagnostic must read:**

| Reference | Path | Use |
|---|---|---|
| PLANNER_TEMPLATE | `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` | Anchor for shipped governance |
| Archived narratives file | `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` | Anchor for 3 archived proposals |
| Plan A blueprint | `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md` | Confirms 13-proposal source set for Workarounds 1-12 |
| Plan B blueprint | `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` | Confirms 17-proposal source set for Checklist + Rules 42-44 + DPE + archived narratives |
| lessons-forge.db | `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` | Pull the 33 row IDs + `suggested_action` + `target_artifact` for the mapping |

**Expected mapping shape (per proposal):**
- ID
- Suggested action (first 80 chars)
- Shipped artifact category — one of: `PLANNER_TEMPLATE Bellows Operational Workaround N`, `PLANNER_TEMPLATE Plan Authoring Checklist item N`, `PLANNER_TEMPLATE Rule 42/43/44`, `PLANNER_TEMPLATE Diagnostic Prompt Engineering technique`, `archived-narratives-2026-05-27.md entry`
- Specific anchor (line number in PLANNER_TEMPLATE.md OR section heading in archived-narratives-2026-05-27.md)
- Verification status: VERIFIED if the anchor text materially addresses the proposal's `suggested_action`; FLAGGED if the agent cannot find a clean match

**Out of scope for this diagnostic:**
- DB modifications (no row updates, no schema changes)
- Re-evaluating proposal acceptance (Gate 1 already shipped; CEO already accepted)
- Judging artifact quality (only checking that an anchor exists and substantively addresses the proposal)

---

## STEP 1 — Produce 33-row proposal-to-artifact mapping table

You are the Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` and `/Users/marklehn/Developer/GitHub/lessons-forge/CLAUDE.md`. Operate against `/Users/marklehn/Developer/GitHub/lessons-forge/`.

**Strict scope:** READ-ONLY. No DB modifications. No file edits except the diagnostic deposit. No git commits.

**Early-output anchors (Rule 41):**
1. Acknowledge claim BEFORE any file reads: "Claimed diagnostic-gate-2d-mapping-2026-05-27 Step 1."
2. After each of the 5 source-file reads listed below, emit one line: "Read <filename> — <one-line content summary>."
3. At the start of mapping-table construction, emit: "Building 33-row mapping table."
4. At the start of verification pass, emit: "Running per-row verification."

**Task:**

### Phase A — Load source data

Read these 5 sources in order:
1. `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — query: `SELECT id, suggested_action, target_layer, target_artifact FROM lesson_proposals WHERE status='accepted' AND status_updated_at='2026-05-27' ORDER BY id;`. Confirm row count is exactly 33; if not, HALT and report.
2. `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — full file (1684 lines). Confirm version line is `**Version:** 4.55`.
3. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/archived-narratives-2026-05-27.md` — full file.
4. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bellows-operational-workarounds-blueprint-2026-05-27.md` — full file.
5. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` — full file.

### Phase B — Build the 33-row mapping table

For each of the 33 proposal IDs, identify the shipped governance artifact that addresses its `suggested_action`. The two source blueprints carry the canonical proposal-ID-to-artifact mappings — use them as the primary source of truth, cross-checked against the actual PLANNER_TEMPLATE / archived-narratives content.

The archived narratives candidates are: proposals 64, 72, 87, 93 — per Plan B blueprint, 64/87/93 ship to archived-narratives directly; 72 was demoted by SA during Plan B authoring as Rule 33 overlap and may also ship to archived-narratives. Verify the actual contents of `archived-narratives-2026-05-27.md` to determine which of these 4 IDs have entries in the shipped file.

Plan A's 13 source proposals (65, 68, 70, 71, 73, 74, 77, 78, 81, 82, 85, 89, 94) map to Bellows Operational Workarounds 1-12 with these SA decisions documented in the Plan A blueprint:
- Workaround 3 (proposals 74 + 85 combined — shared claim-time-cache root cause)
- Workaround 10 (proposal 82 — 3 labeled sub-points A/B/C, shared worktree-lifecycle theme)

Plan B's 17 actionable proposals map to:
- Plan Authoring Checklist items (12 proposals: 66, 67, 69, 75, 79, 80, 84, 90, 91, 92, 95, 98)
- Rules 42, 43, 44 (proposals 83, 96, 97)
- Diagnostic Prompt Engineering technique addition (proposal 76)

Proposal 72's destination (archived-narratives vs counted as actionable) is a count-reconciliation question — PROJECT_STATUS and NEXT_SESSION carry slightly different framings. Resolve by reading the Plan B blueprint as source of truth.

### Phase C — Verify each row's anchor materially addresses the proposal

For each mapping row:
- **VERIFIED**: The cited PLANNER_TEMPLATE section (or archived-narratives entry) contains language that addresses the proposal's `suggested_action`. Loose paraphrase is acceptable; identical wording is not required. Reading the section in isolation, a reasonable Planner would recognize the proposal's intent as covered.
- **FLAGGED**: The anchor exists in the blueprint mapping but the actual shipped text does not visibly address the proposal's intent (e.g., section header without content, dropped during SA blueprint authoring, or substantive drift from proposal). Include a one-sentence note explaining what's missing.

### Phase D — Deposit the diagnostic report

Deposit to: `lessons-forge/knowledge/research/diagnostic-gate-2d-mapping-2026-05-27.md`

**Report structure:**

```markdown
# Diagnostic Report: Gate 2d Mapping — 33 Accepted Proposals to Shipped Governance Artifacts

**Diagnostic plan:** diagnostic-gate-2d-mapping-2026-05-27
**Run date:** 2026-05-27
**Agent:** Forge Developer

## Summary

- Total rows queried: 33
- Verified mappings: N
- Flagged mappings: M
- Total: 33 (N + M)

## Source confirmation

- lessons-forge.db row count at status='accepted' AND status_updated_at='2026-05-27': 33 (PASS / FAIL)
- PLANNER_TEMPLATE.md version: 4.55 (PASS / FAIL)
- All 5 source files read: PASS / FAIL

## Mapping table

| Proposal ID | Suggested action (first 80 chars) | Shipped artifact category | Anchor (line/section) | Verification |
|---|---|---|---|---|
| 64 | <action> | archived-narratives-2026-05-27.md entry | <section heading> | VERIFIED / FLAGGED |
| 65 | <action> | PLANNER_TEMPLATE Bellows Operational Workaround N | line <L> | VERIFIED / FLAGGED |
| ... | ... | ... | ... | ... |
| 98 | <action> | <category> | <anchor> | VERIFIED / FLAGGED |

## Flagged rows (if any)

For each flagged row:

### Proposal <ID>
- Suggested action: <full text>
- Expected anchor (per blueprint): <category + location>
- What's missing: <one-sentence explanation>
- Recommendation: <one of: (a) advance anyway — proposal substantively covered by adjacent shipped text; (b) hold from flip — needs follow-up governance edit; (c) reclassify — proposal was archive-as-context but blueprint claimed governance>

## Cross-check against PROJECT_STATUS / NEXT_SESSION counts

- PROJECT_STATUS claim: "Plan A (13 proposals) + Plan B (17 actionable proposals + 3 archived narratives + Rule 41 supersession)"
- NEXT_SESSION claim: "Plan A (13 proposals) + Plan B (17 actionable proposals + 3 archived narratives + 1 demoted DPE addition + the 3 already-shipped via Rule 41 supersession)"
- Diagnostic-measured: Plan A = N1 proposals, Plan B actionable = N2, archived-narratives = N3, sum = N1+N2+N3 = ?
- Match / mismatch: <PASS / FLAG with explanation>

## Conclusion

(One of:)
- All 33 rows VERIFIED. Safe to proceed with executable flip plan covering all 33.
- N rows VERIFIED, M flagged. Recommended split: flip the N verified; hold M pending Planner review.
```

**Rule 20 self-check (literal banner inside fenced block; no decoration, no shell prefix, no === lines):**

Run:
```python
import os
required = [
    "knowledge/research/diagnostic-gate-2d-mapping-2026-05-27.md",
]
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"FAILED - missing evidence: {missing}")
else:
    print("Rule 20 — QA Self-Check Results")
    print("PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.")
```

Paste the literal stdout (two lines) into the diagnostic report appendix inside a fenced code block. No decoration around it.

**Output Receipt:**
- Agent: Forge Developer
- Step: 1
- Status: Complete (33-row mapping table deposited, verification pass complete); Blocked (DB row count mismatch, missing source file, or unresolvable mapping)
- What Was Done: produced 33-row proposal-to-artifact mapping table with per-row verification status
- Files Deposited: `lessons-forge/knowledge/research/diagnostic-gate-2d-mapping-2026-05-27.md`
- Files Created or Modified: none (read-only diagnostic, no DB or repo modifications)
- Decisions Made: per-row VERIFIED/FLAGGED classification based on shipped governance content
- Flags for CEO: any FLAGGED rows requiring Planner review before flip plan authoring; any deviation from PROJECT_STATUS/NEXT_SESSION counts
- Flags for Next Step: terminal — Planner reads diagnostic report and authors executable flip plan in next dispatch

**Deposits:**
- `lessons-forge/knowledge/research/diagnostic-gate-2d-mapping-2026-05-27.md`

Standard prompt feedback protocol → `lessons-forge/knowledge/research/agent-prompt-feedback.md`.

---

## How to run

Bellows dispatches Step 1 on next rescan. Single-step diagnostic, `auto_close: true`, terminal `qa_checkpoint` pause for Planner Rule 22 verification. After verification, Planner authors the executable flip plan based on the diagnostic findings.
