# Gate 2 Plan A — QA Report

**Plan:** 287
**Date:** 2026-07-30
**Step:** 3 (QA)

---

## Deliverable Verification

| Deliverable | Expected | Status | Evidence |
|-------------|----------|--------|----------|
| `DRAFTING_CYCLE.md` | v1.2, 7 edits + History row | ✅ | SHA `3951bcf8…` matches dev-log; 7 distinguishing strings found; History 1.2 row present at :166 |
| `PLANNER_TEMPLATE.md` | v4.81, 4 edits + LL row | ✅ | SHA `0c532…` matches dev-log; Rules 59/60, Checklist #4/#26 edits confirmed; LL row at :1882 |
| `RULE_20_SELF_CHECK_BLOCK.md` | Prose section + History row | ✅ | SHA `3accb…` matches dev-log; `## What This Block Verifies` present; History row at :139 |
| `lessons-forge.db` | 10 proposals flipped to `implemented` | ✅ | Per-id read-back: all 10 read `implemented`, `route='codify'`, timestamps match `YYYY-MM-DDTHH:MM:SSZ` |

Dev-log Output Receipt: **Complete**

---

## Verification Table

| Row | Claim | Status | Evidence |
|-----|-------|--------|----------|
| 0b | Blueprint SHA matches dev-log | ✅ | Committed: `7108258217c8…`, dev-log records: `7108258217c8…` — identical |
| 0 | Doc integrity — shasums match post-edit pins, porcelain clean | ✅ | `DRAFTING_CYCLE.md`: `3951bcf8bc2d9e5f85cf39241ec215e1831cdf07f3cb258bb455b09fab0baaf0` matches. `PLANNER_TEMPLATE.md`: `0c53222fbacdc89cb44899d2df400093a41bed52bdab12d41879ea6fee383e04` matches. `RULE_20_SELF_CHECK_BLOCK.md`: `3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644` matches. `git status --porcelain`: empty |
| 1 | Doctrine changed only in intended ways | ✅ | All three shasums differ from pre-edit pins (edited by design). `git show 3c327e3 --stat`: 3 files changed, 55 insertions(+), 10 deletions(-). All hunks attribute to named gap rows (see doc-integrity.txt). `git log 3c327e3..HEAD -- <three files>`: empty (no drift) |
| 2 | Lens count still five | ✅ | :29 `full five-lens walk`, :73 `run the five lenses`, :132 `all five` — all unchanged |
| 3 | DRAFTING_CYCLE.md version, History, clause survival | ✅ | :5 reads `**Version:** 1.2 (2026-07-30). Amended only through the Iteration Protocol (§6).` — clause survived. `## History` gained exactly one row (:166, 1.2). 1.1 row at :167 untouched |
| 3b | Must-survive clauses present | ✅ | `**Landing posture — warn-first (deliberate).**`: 1. Fenced Cycle Log example in §3: present (grep `Every plan declares its tier`=1). `merely QUOTE the pattern`: 1. `Worked example — convention changes.`: 1. `Grep the plan file for every step identified as QA`: 1. `no agent-discretion language`: 1 |
| 4 | Seven DRAFTING_CYCLE edits present | ✅ | 191: `diff the machinery against the **newest** same-class plan already shipped` (1). 194: `review-target rotation prevents the quiet step` (1). 195+parent: `delimiter-based split silently bisects` (1). 197: `the block collapses to a single line` (1). 198-doc: `negation-aware` (2, in :134 and History :166). 200-§2.7: `Lens attestation integrity` (1). 200-§4: `attestation integrity` appears in §4 :139 |
| 5 | PLANNER_TEMPLATE edits correct | ✅ | v4.81 at :5. `**Last Updated:** 2026-07-30 (v4.81)` at :6. Rule 59 (196) at :1099 in Rules section. Rule 60 (192) at :1105 in Rules section. Both after Rule 58 (:1093), ascending order, before `---` at :1115. NOT in Checklist section. Checklist #26 amended (fold-sweep, :1289). Checklist #4 amended to conditional form with `per Rule 60` cross-reference (:1155). `never hand-authored` compensating clause present. LL row PREPENDED at :1882. v4.80 LL row preserved at :1883 (`v4.80: The Drafting Cycle extracted`=1) |
| 6 | RULE_20_SELF_CHECK_BLOCK.md edits correct | ✅ | `## What This Block Verifies` section present at :28. All four §Q4(a) points documented (evidence-file presence, hedging-keyword absence, verification-heading coupling, status-column glyph constraint). Python block byte-identical: before=3044 bytes, after=3044 bytes, diff=empty. `## History` gained one row at :139 (PREPENDED above 2026-05-10 row at :140). No `**Version:**` line (grep=0). Approach path intact and adjacent: :45 `## Canonical Python Block`, :47 `Copy the block below verbatim`, :49 opening fence — consecutive, nothing inserted |
| 7 | 198-doc describes shipped behaviour, §4 no longer mandates opposite | ✅ | `git diff a59200b..HEAD --stat -- scripts/plan_lint.py`: empty, exit=0 — `a59200b` is still live. :134 now reads `negation-aware` dry detection and `Closing-presence check` as unconditional. :133 reads `line-anchored` for cold-panel check. Old clause `reads its whole-line status: it WARNs iff that line contains a fold-token` at :126: grep=0 (removed). Fold side NOT narrowed: :134 still reads `contains a fold-token (substring fold)` — the incumbent substring |
| 8 | Status flip complete, audit fields populated | ✅ | All 10 ids (191-200) read `implemented`, `route='codify'`, `status_updated_at='2026-07-30T23:47:27Z'`, `status_updated_by='ceo'`. Timestamp GLOB: 10/10 match `YYYY-MM-DDTHH:MM:SSZ`. HARD: `proposed` within 191-200 = 0. RECONCILE: `proposed` outside range = 0 |
| 8b | A0 state recorded, step consistent with it | ✅ | Dev-log records A0 state (1) fresh run. Evidence: all three pins matched pre-edit, porcelain empty, no `[287]` commit. Task F used `git diff` (correct for fresh run). Exactly one root doc commit: `git log 3c327e3^..HEAD -- <three files>` returns `3c327e3` only. Backup newly taken (consistent with fresh run). Flip executed fresh (precondition count was 10) |
| 8c | Version metadata and changelog intact | ✅ | `PLANNER_TEMPLATE.md:6` reads `**Last Updated:** 2026-07-30 (v4.81)` — consistent with :5. v4.80 LL row at :1883 preserved verbatim (`v4.80: The Drafting Cycle extracted`=1). Checklist #4 `no agent-discretion language` clause present (grep=1) |
| 9 | Ordering honoured (durable artifacts) | ✅ | DOC_SHA commit date: `2026-07-30T18:46:27-05:00` = `2026-07-30T23:46:27Z`. Flip `status_updated_at`: `2026-07-30T23:47:27Z`. Commit precedes flip by 60 seconds |
| 9b | Ordering honoured (narrative) | ✅ | Dev-log sequence: Tasks A-F (doc edits, diff review, commit at DOC_SHA) all precede Task G (precondition, backup, UPDATE, read-back). No ordering violation |
| 9c | Pre-flip gate ran | ✅ | Dev-log section (2) carries Task G1's six-condition checklist with evidence per condition: (1) A0 state, (2) all edits + must-survive greps, (3) lens count, (4) DOC_SHA, (5) G0 empty + exit=0, (6) backup + read-back=10 |
| 10 | Restore point exists | ✅ | `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate2-flip-20260730T234713Z.db` — 909312 bytes. Read-back (`?immutable=1`): 10 pre-flip `proposed` rows confirmed |
| 11 | Suite passes | ✅ | `python3 -m pytest src/ --tb=short -q`: 55 passed in 0.12s. Reconciles with most recent prior report (gate-1-route-session-12-captures-2026-07-29: 55 passed) |

---

## Rule 20 Self-Check

_Block copied from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (the file 199 edited — Python block confirmed byte-identical to pre-edit)._

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/287/knowledge/qa/evidence/gate2-plan-a-2026-07-30/
Files verified: 3
```

---

### Ledger Updates

#### Project Status

Gate 2 complete: ten proposals (191-200) codified across three doctrine files and flipped to `implemented`. `DRAFTING_CYCLE.md` v1.2, `PLANNER_TEMPLATE.md` v4.81. `proposed` = 0 within ids 191-200.

#### Prompt Feedback

- **(QA, plan 287, Step 3):** The `grep -F` discipline for literal bold-marker anchors is essential on the ugrep shim — without `-F`, patterns starting with `**` silently error and produce empty stdout that reads as "not found" having verified nothing. Confirmed during must-survive clause verification.

---

## Output Receipt

**Status:** Complete

### Deposits
- `knowledge/qa/gate2-plan-a-qa-2026-07-30.md` (this file)
- `knowledge/qa/evidence/gate2-plan-a-2026-07-30/doc-integrity.txt`
- `knowledge/qa/evidence/gate2-plan-a-2026-07-30/db-invariants.txt`
- `knowledge/qa/evidence/gate2-plan-a-2026-07-30/suite.txt`
