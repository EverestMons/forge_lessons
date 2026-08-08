# Lessons Forge — Forward Register

> Standing queue of deferred work and parked CEO decisions for the lessons-forge
> project. Persists across sessions until acted on.
>
> **How rows arrive:** the daemon appends them post-merge from a plan's Output Receipt
> `#### Forward Register` section (`bellows.py:_append_forward_row`). **Agents never write
> to this file directly** — a plan that needs an item recorded emits it in its Receipt.
>
> **Why this file exists (created 2026-08-01):** it did not, and `bellows.py:1417` resolves
> the append destination to `<project>/knowledge/FORWARD.md`. With the file absent the daemon
> logged `no FORWARD.md in project, skipping forward append` and returned — **so every Rule 46
> routing from this project was silently discarded by design.** Measured: plan 288 emitted a
> correctly formatted three-item block and no row landed anywhere. The daemon was behaving
> exactly as written; the destination had never been configured.
>
> **Reconciliation:** at session wrap, each open entry is checked against lifecycle DB state
> for closure (PLANNER_TEMPLATE.md Rule 42).

---

| # | Added | Item | Type | Plan-id link | Status |
|---|---|---|---|---|---|
| 1 | 2026-08-02 | gates.py:449 per-step span regex — the final step's span runs to end-of-file and absorbs the trailing Drafting Cycle block; recorded by Gate 2 plan 291, which codified proposal 206 into §3 but is governance-only and not chartered to edit the gate; §4's enforced behaviour is unchanged by that amendment. | deferred-work | — | open |
| 2 | 2026-08-03 | (Three items listed above under Forward Register section.) | deferred-work | — | open |
| 3 | 2026-08-03 | - generate_lessons_report (src/lessons_forge.py:593) writes with no explicit encoding= — verified at authoring, the line is with open(output_path, "w") as f:. | deferred-work | — | open |
| 4 | 2026-08-03 | - detect_duplicates returns [] on a failed reference read, so a read failure is indistinguishable from "no duplicates". | deferred-work | — | open |
| 5 | 2026-08-03 | - run_full_lessons_cycle drops the staled-proposal count. | deferred-work | — | open |
| 6 | 2026-08-03 | - Row 2 of this register is a parser artifact recording zero items and should be superseded. | deferred-work | — | open |
| 7 | 2026-08-03 | - `PLANNER_TEMPLATE.md` Rule 55 — a recorded PID goes stale across a daemon restart, so `ps -p` on a stale record reports a live process as dead; the positive confirmation must resolve, and the record be re-established when it does not. Measured 2026-08-03: recorded pid 86216 dead, live daemon 96240. Those PIDs are a point-in-time observation and are evidence, not current state — any liveness check must be re-run now, never inherited from this line. | deferred-work | — | open |
| 8 | 2026-08-03 | - `sanitize_items` retains a literal leading `- ` on appended rows, so rows after the first render inconsistently with row 1. | deferred-work | — | open |
| 9 | 2026-08-07 | `get_unclassified_entries` returns the full remainder with no ordering contract stated in its docstring; the tranche discipline depends on ascending-id order — worth a one-line documented guarantee (lessons-forge-owned, small). | deferred-work | — | open |
| 10 | 2026-08-07 | `get_unclassified_entries` returns the full remainder with no ordering contract stated in its docstring; the tranche discipline depends on ascending-id order — worth a one-line documented guarantee (lessons-forge-owned, small). | deferred-work | — | open |
