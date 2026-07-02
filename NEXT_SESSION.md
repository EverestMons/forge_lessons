# Lessons Forge — Next Session Baton

**Last session:** 2026-06-07 (Gate 1 disposition + Gate 2 codification — full cycle closed through Gate 2d, PLANNER_TEMPLATE v4.60)
**Last session focus:** Dispositioned the 9 proposals from the 2026-06-06 cycle (Gate 1), then ran a single SA->DEV->QA Bellows plan to codify the accepted set (Gate 2). 6 accepted, 3 rejected. The load-bearing Gate 1 finding: dedup against the LIVE v4.59 template showed 4 proposals were already covered by rules the 06-03 Gate 2 had ratified only four days earlier — the batch was catching its own tail (overlapping entries written in the same window those rules landed). Reviewing the prior session + git blame on the cited template lines is what surfaced this; the 06-06 classification report did no dedup (the classifier categorizes/routes, it does not check the template).

---

## In-flight threads (carry forward)

*(none — Gate 2 plan closed to `Done/` through QA 12/12; PLANNER_TEMPLATE v4.60 shipped; all submodule + governance commits pushed at session close)*

The 2026-06-06/2026-06-07 cycle is fully resolved end to end. No queued Lessons Forge task. The next cycle runs on demand when new LESSONS entries accumulate — derive its work list from `get_unclassified_entries(conn)` (now codified as Orchestration Rule #47).

---

## What shipped this session (2026-06-07 Gate 1 + Gate 2)

**Gate 1 disposition (6 accepted, 3 rejected):**
- **Rejected as already-covered** (dedup against live v4.59): 122/entry 93 (schema init_db+PRAGMA = Plan Authoring Checklist #12, added 05-27); 123/entry 116 (scope_check blueprint-FP interim discipline — superseded by Checklist #14's inline-target-paths fix, which removes the trigger); 125/entry 118 (clean-main-before-redispatch = Bellows Workaround #13). The last two were 06-03 Gate 2 rules, four days old.
- **Accepted -> codified:** 124/117, 126/119, 127/120, 128/121, 130/123.
- **Accepted -> already in BACKLOG (no template edit):** 129/entry 122 (structural; `__file__`-relative roots) — the bellows BACKLOG "Added 2026-06-06" item already captures it exactly. Marked `implemented`; no duplicate filed.

**Gate 2 codification (5 PLANNER_TEMPLATE.md edits, v4.59 -> v4.60):**
- **Orchestration Rule #47** (124) — derive the classification work list from `get_unclassified_entries(conn)`, never `needs_classification`, never a hand-copied NOT EXISTS query. *(Codified the helper, not the buggy SQL — the persisted caveat was honored and QA-verified: 0 occurrences of the buggy query string.)*
- **Orchestration Rule #48** (127) — gate-enforced QA actions require a mandatory top-of-step callout (name gate, quote byte-exact banner, state the table doesn't satisfy it, end with self-grep).
- **Quality Standards bullet** (128) — DEV self-verify + Planner review each run the FULL pytest suite to pass/fail and read the tail; Bellows gates do NOT include suite-green.
- **Checklist #16 STRENGTHEN** (126) — added the silent-no-pause note for an invalid `pause_for_verdict` token.
- **Guardrails recurring-bug bullet STRENGTHEN** (130) — added the inherited-frame clause (verify a handed-down fix against root cause before building).

**Process meta:** cross-repo Gate 2 (lessons-forge-dispatched plan editing governance-root PLANNER_TEMPLATE.md). DEV's Rule 23 commit produced the split-commit automatically (gov `754e1cb`). The Step 2 `scope_check` gate_failure was the benign cross-repo artifact — it fired on DEV's out-of-worktree QA evidence file because PLANNER_TEMPLATE.md is invisible to the worktree-scoped audit. Continue-over-failure with documented Rule 22(b) substance verification; teardown clean. Same pattern as the 06-03 cross-repo Gate 2.

---

## On the horizon (open items, none in-flight)

### `run_full_lessons_cycle` `needs_classification` over-report refactor (BACKLOG candidate) [carried]
The consumer-side fix (the helper) is codified and sufficient for correctness. The function still returns every parsed entry in `needs_classification` — the deeper return-shape root (entry 117's "candidate code fix, separate"). File in lessons-forge/Bellows BACKLOG; not blocking. **CLOSED 2026-07-02:** `needs_classification` now delegates to `get_unclassified_entries(conn)` post-duplicate-insertion; over-report regression test added; Rule #47 remains in force as defense-in-depth.

### 129 — `__file__`-relative roots marker walk-up [filed, audit-first conversion pending]
Already in bellows BACKLOG (2026-06-06): four latent `BELLOWS_ROOT = Path(__file__).parent` instances (bellows.py:23, planner.py:11, runner.py:20, verdict.py:13). Convert-with-proof of worktree-reachability, not blanket. Bellows reliability session.

### Bellows reliability [carried, not lessons-forge]
- Teardown Gap 3 (dirty-tree auto-stash) — recurring `worktree_teardown_dirty_tree` source; auto-stash carries unstash-conflict risk, DEFERRED.
- 16 stale `halted-*` plans sweep (per-file landed-check, no blanket delete).
- `lessons-forge.db` git-tracking disposition (keep committing vs `git rm --cached` + bootstrap) — filed Bellows BACKLOG 2026-05-27. **CLOSED by plan 30 (DB-out-of-git policy):** option (b) taken — DB un-tracked in lessons-forge commit `dabb301` + recovery docs; bellows FORWARD row 7 marked closed-by-plan-30. No open decision remains.

### Cross-project (not lessons-forge) [carried]
- **invoice-pulse T0.5.1 reconciliation** — next ungated step in fuel-bracket extrapolation.
- **email-PRO -> assigned-user feature** — gated on the two Windows prod-DB queries in `email-pro-user-lookup-prod-queries-2026-06-03.sql`.

### Forge cycle #14 + canary follow-ups [carried]
Retire-the-queue decision **CLOSED — CEO-ratified retirement 2026-07-02** (signal A from the 2026-05-27 canary; memo at `forge/knowledge/research/queue-retirement-decision-2026-07-02.md`; routine cycles never drain, no further canaries). The `forge.db` 50MB warning is **CLOSED by plan 30** (DB-out-of-git policy; shop FORWARD #1 closed-by-plan-30 — forge.db un-tracked and gitignored). Run `bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` before any Mac Forge work.

---

## DB state (post-Gate-2d 2026-06-07)

`lesson_proposals` ground-truth (total **130**):
- `implemented`: **90** (was 84; +6 this session — 124/126/127/128/130 template + 129 via existing BACKLOG)
- `superseded`: **25**
- `rejected`: **13** (was 10; +3 — 122/123/125 rejected as already-covered)
- `stale`: **2** (proposal 98/entry 93; proposal 121/entry 116 — both retained as history)
- `proposed`: **0** (clean)
- `accepted`: **0** (clean)

`lesson_entries`: **123**. No new entries this session (disposition + codification only).

---

## Operational notes for next session

- PLANNER_TEMPLATE.md at **v4.60**. Orchestration Rules now run through **#48**; Plan Authoring Checklist through **#18** (#16 strengthened).
- Daemon: bellows submodule advanced for verdict-artifact lifecycle commits only (no daemon code change, no restart required).
- Phase 1.5 next session: this baton + PROJECT_STATUS top entry + the horizon items above. Cycle fully closed; no in-flight orchestration.
- **Dedup discipline confirmed this cycle:** Gate 1 must dedup proposals against the LIVE template (and git-blame the cited lines when a "dup" is suspected), not trust the classification report or the baton's framing. Four of nine were already codified.
- **Use the helper:** any future cycle's work list comes from `get_unclassified_entries(conn)` — now Rule #47.
