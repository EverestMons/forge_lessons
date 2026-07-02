# Lessons Forge — Baton Stale-Pointer Close (plan 30 DB un-track)
**Date:** 2026-07-02 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Documentation Analyst) | **pause_for_verdict:** always

## CEO Context

Reconciliation on 2026-07-02 confirmed plan 30 (DB-out-of-git policy) resolved the `lessons-forge.db` git-tracking fork via option (b): the DB was un-tracked in lessons-forge commit `dabb301` ("un-track lessons-forge.db, add recovery docs (shop DB policy) [30]"), `*.db`/`*.db-shm`/`*.db-wal` are gitignored, and no `.db` file is tracked in any of the affected repos. The live ledgers already reflect closure — bellows FORWARD row 7 reads `closed-by-plan-30`, and shop FORWARD #1 (the `forge.db` 50MB warning) reads `closed-by-plan-30`. Two horizon bullets in `lessons-forge/NEXT_SESSION.md` still present these as open; this plan appends closed markers to both. `bellows/knowledge/BACKLOG-ARCHIVE.md` is frozen (2026-06-12) and is deliberately NOT touched — the FORWARD register is the live ledger and is already correct.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. Single-step plan — the agent executes Step 1 and the daemon pauses for CEO verdict at completion.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-baton-stale-pointers-plan-30-2026-07-02.md. Execute Step 1. Do NOT move the plan to Done until Step 1 is fully complete including verification.
```

---
---

## STEP 1 — DOCUMENTATION ANALYST

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> **Skip specialist file and glossary reads** — this is a two-edit baton annotation with exact old-strings and new-strings specified below. The single target file is `lessons-forge/NEXT_SESSION.md` (the repo-local session baton; it is NOT one of the three daemon-owned ledgers — PROJECT_STATUS.md / agent-prompt-feedback.md / FORWARD.md — so a direct edit is the correct mechanism here).
>
> **Edit A — close the `lessons-forge.db` git-tracking horizon bullet.** Use a single exact-string edit. `old_string` (verbatim, one line under `### Bellows reliability [carried, not lessons-forge]`):
>
> ```
> - `lessons-forge.db` git-tracking disposition (keep committing vs `git rm --cached` + bootstrap) — filed Bellows BACKLOG 2026-05-27.
> ```
>
> `new_string`:
>
> ```
> - `lessons-forge.db` git-tracking disposition (keep committing vs `git rm --cached` + bootstrap) — filed Bellows BACKLOG 2026-05-27. **CLOSED by plan 30 (DB-out-of-git policy):** option (b) taken — DB un-tracked in lessons-forge commit `dabb301` + recovery docs; bellows FORWARD row 7 marked closed-by-plan-30. No open decision remains.
> ```
>
> **Edit B — annotate the `forge.db` 50MB portion of the Forge cycle #14 horizon item.** The cycle #14 run and the retire-the-queue decision remain open — only the 50MB-warning clause is closed. `old_string` (verbatim, the line under `### Forge cycle #14 + canary follow-ups [carried]`):
>
> ```
> `forge.db` 50MB warning, retire-the-queue decision. Run `bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` before any Mac Forge work.
> ```
>
> `new_string`:
>
> ```
> Retire-the-queue decision still open. The `forge.db` 50MB warning is **CLOSED by plan 30** (DB-out-of-git policy; shop FORWARD #1 closed-by-plan-30 — forge.db un-tracked and gitignored). Run `bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` before any Mac Forge work.
> ```
>
> **Verify.** Read `lessons-forge/NEXT_SESSION.md` back and confirm: (1) the phrase `CLOSED by plan 30` appears exactly twice; (2) the phrase `filed Bellows BACKLOG 2026-05-27.` still appears exactly once (Edit A preserved the original text and appended, not replaced); (3) the `pre-scan-sync.sh` line still appears exactly once; (4) no other line of the file changed — `git diff --stat` shows exactly one file, and `git diff` shows exactly the two edits above. Any mismatch: halt and report the discrepancy in the Output Receipt without committing.
>
> **Commit.** `git add NEXT_SESSION.md && git commit -m "docs(lessons-forge): baton stale-pointer close — db-tracking fork + forge.db 50MB closed-by-plan-30"`. Record the commit hash in the Output Receipt.
>
> **Output Receipt.** Standard Output Receipt with status. Prompt feedback goes in the receipt's `### Ledger Updates` → `#### Prompt Feedback` channel (daemon-owned; do NOT edit any feedback file directly). No `#### Project Status` entry — this is ledger housekeeping, not a milestone. On full completion including verification, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
