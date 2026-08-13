# Executable: archive the two parked halted plans — lessons-forge

**Type:** Executable
**Project:** lessons-forge
**Depends on:** the two parked files (audits complete — 334's content fully landed via 348; 360's step 1 stands with corrective 362 Done), the halted-archival arc's validated move form (plans 252–256)
**Created:** 2026-08-13
**Author:** Planner
**Slug:** `archive-halted-lessons-forge-2026-08-13`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T0

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** `id_sequence` read at deposit, never at authoring.

---

## Why this exists

Two lessons-forge halted files are parked with audits complete and dispositions decided (archive): `halted-executable-334.md` (content landed via 348) and `halted-executable-360.md` (superseded-QA predecessor, corrective 362 Done). ⚠️ **`knowledge/decisions/archived-halted-plans/` does NOT exist in this project yet — the move creates it** (`mkdir -p` first; the halted-archival arc's independent-repo variant). **`scope_check` cannot verify rename destinations — THE MANIFEST IS THE MOVE GUARD.**

**The manifest (measured at authoring; any A0 mismatch → HALT):**

| file | sha256 |
|---|---|
| `knowledge/decisions/halted-executable-334.md` | `30c524f18420713f4b02bc51b6f17156aae421a95136963b0597f97a0045a053` |
| `knowledge/decisions/halted-executable-360.md` | `cb88956c26b6abbb67dc1eb41ee67cd8a203ca4253b549530f12cbfbaf7c1eef` |

---

## Scope

- `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-334.md`
- `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-360.md`
- `lessons-forge/knowledge/qa/evidence/archive-halted-lessons-forge-2026-08-13/manifest.txt`

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 (the only step). After completing it, STOP.
```

---

## STEP 1 — DEV (the move, manifest-guarded)

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting.** Do NOT rename this file. ⚠️ **THE WORKTREE RULE:** every git command runs from your cwd; never `-C` into another checkout for a WRITE.
>
> **Task A0 — branches, catch-all LAST.** (0) tree shape: `git rev-parse --show-toplevel` prints a tree containing `knowledge/decisions`. (1) **manifest gate:** `shasum -a 256` of each SOURCE path matches the manifest exactly. (2) destinations absent (the directory itself may be absent — that satisfies (2)).
> - **FRESH** = (0)+(1)+(2) hold → proceed. **RE-ENTRY** = sources absent AND both destinations present with matching shas → the move landed; write the manifest receipt if absent and report complete. **NONE-MATCH** = anything else → HALT quoting every measurement.
>
> **The move:** capture the pre-move `shasum` outputs; `mkdir -p knowledge/decisions/archived-halted-plans`; `git mv` each file in; **prove the post-condition** (each source ABSENT, each destination present with its manifest sha — after != before, never just exit codes). Write `knowledge/qa/evidence/archive-halted-lessons-forge-2026-08-13/manifest.txt` with the pre- and post-move raw outputs. Commit from cwd with a pathspec naming the two destinations + the manifest, subject `[<id from your plan filename>] archive-halted-lessons-forge-2026-08-13: two audited halted plans archived (manifest-guarded)`. Then STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-334.md`
> - `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-360.md`
> - `lessons-forge/knowledge/qa/evidence/archive-halted-lessons-forge-2026-08-13/manifest.txt`
>
> **Scope:**
> - `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-334.md`
> - `lessons-forge/knowledge/decisions/archived-halted-plans/halted-executable-360.md`
> - `lessons-forge/knowledge/qa/evidence/archive-halted-lessons-forge-2026-08-13/manifest.txt`

---

## Drafting Cycle

**Tier:** T0 — move-only, no tier trigger fires. **Floor pass (lens 4) run at authoring:** the halted-archival arc's independent-repo variant is the precedent; the scope-check-illusory lesson carried as the manifest guard; the dir-creation case declared in A0's (2). `plan_lint` mechanical preverify in lieu of a walk cycle (the CEO-sanctioned T0 path); result recorded in the deposit commit.
