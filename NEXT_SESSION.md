# Lessons Forge — Next Session Baton

**Last session:** 2026-06-03 (Gate 2 codification + Gate 2d)
**Last session focus:** 2026-06-03 cycle Gate 2 — codified 19 accepted `governance_rule` proposals (15 PLANNER_TEMPLATE edits after 3 merges + 1 fully-subsumed) into v4.59 via a single SA->DEV->QA executable plan; archived 2 narratives; advanced all 21 (19 rules + 2 narratives) to `status='implemented'`. Plan shipped clean end-to-end through Bellows.

---

## In-flight threads (carry forward)

*(none — 2026-06-03 cycle closed through Gate 2d across DB, governance, and bookkeeping)*

---

## What shipped this session (2026-06-03 Gate 2)

- **PLANNER_TEMPLATE.md v4.58 -> v4.59.** 15 edits from 19 accepted proposals:
  - Plan Authoring Checklist #13-18 (99; 103+121 merged; 107; 114; 116; 119)
  - Orchestration Plan Rules #45 (120) and #46 (118 — Gate 1 rejects daemon-bug workarounds -> BACKLOG)
  - Quality Standards: 2 bullets (101 per-feature substance-check; 102 external wall-clock + `--collect-only`)
  - Rule 25: terminal-log-primacy caveat paragraph (104)
  - Bellows Operational Workarounds: strengthen #8 (100+108, defer-all-edits + ~5-10 min cost), strengthen #12 (113+115, R2 Planner-direct close + claim-rename variant), new #13 (105 clean roots), new #14 (111 scope_check Rule 22(d) override); preamble renumbered 1-14
- **Proposal 110** (verdict responses to resolved/) — FULLY SUBSUMED by existing Rule 25 (L738); advanced to implemented with no edit.
- **2 narratives archived** to `knowledge/archived-narratives-2026-06-03.md`: 109 (wall-clock calibration ~72 min), 117 (verdict-prefix tolerance).
- **Dedup baseline correction:** cycle summary said v4.55, but live file was v4.58. 104/113/115 reconciled against v4.57 (vestigial-claim-rename drop + Rule 25 teardown-variant discrimination) rather than duplicated.

---

## On the horizon (open items, none in-flight)

### Recommended next reliability cut — Bellows teardown Gap 3 (dirty-tree auto-stash)
The dirty-tree teardown pre-check (`worktree_teardown_dirty_tree`) is the recurring failure source this session referenced. Auto-stash of dirty non-lifecycle files before teardown cherry-pick would remove the manual commit/stash recovery cycle (~5-10 min each, now documented in Workaround #8). Recommended as the next Bellows reliability session.

### `lessons-forge.db` git tracking disposition (carried)
DB is tracked; `*.db` ignore convention exists elsewhere. De-facto behavior remains commit-on-state-change (2026-06-03 Gate 2d committed the advanced DB, consistent with 2026-05-27). Decision still open: keep committing vs `git rm --cached` + bootstrap story. Not blocking. Filed in Bellows BACKLOG (2026-05-27).

### Cross-project (not lessons-forge)
- **invoice-pulse T0.5.1 reconciliation** — next ungated step in the fuel-bracket extrapolation work.
- **email-PRO -> assigned-user feature** — gated on the two Windows prod-DB queries in `email-pro-user-lookup-prod-queries-2026-06-03.sql`.

### Forge cycle #14 + canary follow-ups (carried)
`forge.db` 50MB warning, retire-the-queue decision. Not blocking. Run `bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` before any Mac Forge work.

---

## DB state (post-Gate-2d 2026-06-03)

`lesson_proposals` table (ground-truth counts):
- `status='implemented'`: **85**
- `status='rejected'`: **10**
- `status='superseded'`: **25**
- `status='stale'`: **1**
- `status='accepted'`: **0** (clean)
- Total: **121**

This cycle advanced 21 rows (99-121: 19 rules + 2 narratives) to implemented; 106 + 112 stayed rejected (daemon-bug workarounds routed to BACKLOG per new Rule 46). Note: 1 `stale` row sits in the historical 1-98 range (pre-existing; not touched this session) — minor count anomaly vs the 2026-05-27 baton's stated 65-implemented, worth a glance if doing DB archaeology, not blocking.

---

## Operational notes for next session

- Daemon: bellows submodule advanced this session for verdict-artifact commits only (no daemon code change, no restart required).
- PLANNER_TEMPLATE.md at **v4.59**.
- Phase 1.5 next session: this baton + PROJECT_STATUS top entry + the on-horizon items above. 2026-06-03 cycle fully closed; no in-flight context to carry.
- Resolved-this-session (no longer open candidates): `ceo_flags` FP on benign confirmation text (hit again at Step 2 as a false positive; underlying daemon FP still in BACKLOG); verdict-prefix tolerance (archived as narrative 117).
