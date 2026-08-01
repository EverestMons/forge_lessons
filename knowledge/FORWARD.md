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
