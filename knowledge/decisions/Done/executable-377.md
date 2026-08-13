# Executable: flip proposal 331 `reference` → `implemented` — the cold-front decision's lifecycle close

**Type:** Executable
**Project:** lessons-forge
**Depends on:** proposal 331 / entry 323 (measured at authoring: `reference | 2026-08-12T17:12:07Z | ceo | governance_rule` — the A0 gate re-verifies), the shape packet + CEO Fork-B pick (2026-08-13) + plan 373 Done (`DRAFTING_CYCLE v2.7` — the decision 331 requested is made AND shipped; governance FORWARD row 2 closed citing it), the Gate-1 write plans' compare-and-swap flip form (360 step 1 / 353)
**Created:** 2026-08-13
**Author:** Planner
**Slug:** `flip-331-2026-08-13`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** `id_sequence` read at deposit, never at authoring.

---

## Why this exists

Proposal 331 (cold-front timing) was routed `reference|backlog` with governance FORWARD row 2 as its schedule. That schedule is now DISCHARGED: the packet was assembled, the CEO decided (Fork B + R1a, 2026-08-13), and plan 373 shipped the decision as DRAFTING_CYCLE v2.7 — row 2 reconciled closed citing all three. The proposal's lifecycle close is this flip. T-2 fires (a production-data mutation) → T1 cycle; never manual (standing directive).

---

## Ledger

- **C1 — compare-and-swap, never a blind UPDATE:** the WHERE clause carries `id=331 AND status='reference'`; `changes()` must be exactly 1. *(observer: the in-step raw output)*
- **C2 — a VALUE guard, not a count guard:** the post-state SELECT shows `implemented` with a fresh `status_updated_at` and `status_updated_by='ceo'` (the decision was the CEO's; the constraint allows planner/ceo/auto — verified live at authoring). *(observer: the in-step raw output)*
- **C3 — the singleton blast radius proven:** total `implemented` count is captured before and after and differs by exactly +1; no other row's status changes (`status_updated_at` max over id != 331 unchanged). *(observer: the in-step raw output)*

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 (the only step). After completing it, STOP.
```

---

## Scope

- `lessons-forge/knowledge/qa/evidence/flip-331-2026-08-13/flip-evidence.txt`

---

## STEP 1 — DEV (the flip, compare-and-swap)

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting.** Do NOT rename this file. ⚠️ **THE WORKTREE RULE:** writes only from cwd. **The DB is addressed by ABSOLUTE path** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — a bare relative name CREATES an empty file). **Environment facts:** `grep` is a ugrep shim (`-F` literals; zero-count `grep -c` exits 1 — read the count).
>
> **Task A0 — branches, catch-all LAST.** (0) tree shape. (1) PRE-STATE gate: `SELECT id, status, status_updated_at, status_updated_by FROM lesson_proposals WHERE id=331` reads exactly `331|reference|2026-08-12T17:12:07Z|ceo` (measured at authoring — a different status means the flip already happened or the row moved: if `implemented`, verify the evidence file exists and report complete; anything else → HALT quoting the row).
> - **FRESH** = (1) reads `reference` → proceed. **RE-ENTRY** = (1) reads `implemented` AND the evidence deposit exists → report complete. **NONE-MATCH** → HALT.
>
> **The flip.** Capture pre-state raw: the 331 row + `SELECT COUNT(*) FROM lesson_proposals WHERE status='implemented'` + `SELECT MAX(status_updated_at) FROM lesson_proposals WHERE id != 331`. Then in ONE sqlite3 invocation: `UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id=331 AND status='reference'; SELECT changes();` — **changes() must print exactly 1; any other value → HALT loudly, the swap failed.** Capture post-state raw: the 331 row, the implemented count (pre+1 expected — verify, report actual), the MAX(status_updated_at) over id != 331 (must equal the pre-value — C3's no-other-row guard). Write ALL raw outputs to `knowledge/qa/evidence/flip-331-2026-08-13/flip-evidence.txt`. Commit it from cwd, pathspec exactly it, subject `[<id from your plan filename>] flip-331-2026-08-13: proposal 331 reference -> implemented|ceo (cold-front decision shipped as DC v2.7 by plan 373)`. STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/evidence/flip-331-2026-08-13/flip-evidence.txt`
>
> **Scope:**
> - `lessons-forge/knowledge/qa/evidence/flip-331-2026-08-13/flip-evidence.txt`

---

## Drafting Cycle

**Tier:** T1 — T-2 fires (production-data mutation), singleton row.

**Walk 0 (v2.7, measured):** the 331 row read live (`reference|2026-08-12T17:12:07Z|ceo|governance_rule`); the `status_updated_by` CHECK constraint read live (`planner/ceo/auto`); newest same-class = the Gate-1 write flips (360 step 1, its compare-and-swap + changes() form carried; delta owned — single row vs batch, so the tranche machinery is dropped and the singleton guards C1–C3 replace it). **Scout: not convened (T1, Planner's call — a one-row swap with three in-step guards).** **Direction verdict: PROCEED.**

**Walks:** 2. Walk 1 — Weak spots 1 fold (the RE-ENTRY branch first keyed only on status without requiring the evidence deposit — a crashed post-flip run would report complete with no evidence; fixed to the conjunctive form now in A0); Destruction/Vulnerabilities/Integration/ACID dry (the timestamp-format check against the LF corpus four-forms memory: `strftime` Z-form matches the row's existing `2026-08-12T17:12:07Z` representation — verified same form). Walk 2 — all five lenses DRY, instruction 0 / record 0.

**Closing:** walk 2 DRY — instruction 0 / record 0; the last event before deposit is a dry lens pass.
