# Executable: Gate 1 held-pair routing — proposals 378 + 389 → accepted|codify (the CEO's central-glossary ruling)

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-536** (Done 2026-08-25 — the 55-row Gate-1 routing and this plan's CLONE ORIGIN; its transaction form, addressing contract and dump-pair instrument are carried), and the CEO ruling recorded in the DECIDED block of `gate1-packet-2026-08-25.md` at the shop root (**PROVENANCE, not an input any step reads** — the payload is inline below).
**Created:** 2026-08-25
**Author:** Planner (session `b52c5d10`; the dispositions are the CEO's — this plan is the pen, not the decider)
**Slug:** `gate1-route-heldpair` (stable across any crash-redo re-deposit — the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 10
**cycle_tier:** T1
**qa_steps:** [2]
**Test Scope:** targeted (the 536 convention) — no code changes; Step 2 runs the whole single-module suite, Step 1 runs none.

⚠️ **ID NOTE:** `id_sequence` read **537** at authoring — a prediction, never an identity; watchers and verdicts key on the SLUG.

---

## Why this exists — the fork is RULED and the routing is the deliverable

Plan 536 routed 55 of the 57-proposal queue and deliberately HELD 378 and 389 as one linked design fork (the per-project knowledge-home consolidation). The CEO ruled on 2026-08-25 (evening, recorded verbatim in the packet's DECIDED block): **ONE central glossary, well-tagged, mapping entries to project(s)** — both rows therefore route `accepted|codify`, and Gate 2 executes one coherent edit against that ruling.

**THE PAYLOAD (byte-authoritative over any prose):**

- **CODIFY-2:** 378, 389 — `status='accepted'`, `route='codify'`, **`status_updated_by='ceo'`** (unlike 536's 55 rows: these two dispositions are the CEO's own ruling, and `'ceo'` is verified legal against the live CHECK constraint), `status_updated_at=:TS`.
- **ZERO `target_artifact` writes.** 378 already carries `PLANNER_TEMPLATE.md` (correct — the bin-retirement is a PT edit); 389 is NULL and Gate 2 assigns.

**Arithmetic anchor: after this write, `proposed` within 354–410 = 0, and the global `accepted|codify` population goes 28 → 30.** The `_TERMINAL_STATUSES` hazard from 536 widens accordingly: **no forge ingest between this routing and Gate 2 without checking the population; a Gate-2 plan finding fewer than 30 `accepted|codify` rows should HALT.**

**What this plan does NOT do:** no doctrine edit (Gate 2 owns the PT/glossary changes the ruling directs), no LESSONS.md touch, no FORWARD emission, no write to any row outside 378/389.

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---
---

## STEP 1 — DEV (the routing transaction)

> **FIRST — resolve the tree, then post a short visible chat message (1–2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename this plan file. Read your specialist file.
> ⚠️ **`ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT` (`cd "$ROOT"` and re-assert if not); print `$ROOT`.**
>
> ⚠️⚠️ **ADDRESSING CONTRACT — carried verbatim from 536, re-confirmed live the same day.** Your cwd is the **WORKTREE**; file deposits are worktree-relative so they enter `files_changed`. **The DB is UNTRACKED and does not exist in the worktree:** every `sqlite3` command addresses the CANONICAL absolute path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — a relative `lessons-forge.db` opens a fresh empty file and every count reads 0. The table is `lesson_proposals`.
>
> **Task A0 — PIN THE PRE-STATE; the write is licensed by it and ONLY it.**
> 1. `SELECT id, status, COALESCE(route,'-'), COALESCE(status_updated_by,'-'), COALESCE(status_updated_at,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals WHERE id IN (378,389) ORDER BY id;` — **must print exactly `378|proposed|-|-|-|PLANNER_TEMPLATE.md` and `389|proposed|-|-|-|-`.** Any other rows → **HALT, and REPORT THE CAUSE CORRECTLY:**
>    - **Both rows read `accepted|codify` with `status_updated_by='ceo'`** → an ALREADY-LANDED REDO; a prior dispatch committed and died before its log. Report it as such, do NOT re-run (the statement would match 0 and roll back), hand the state to the CEO.
>    - **Anything else** → a concurrent writer touched the pair. Do not improvise a reconciliation.
> 2. `SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 354 AND 410;` — **must print 2** (the range scope is deliberate, carried from 536's Q0.2: a concurrent cycle's new proposals at ids > 410 are not this plan's concern).
>
> **Task A1 — DERIVE THE PLAN ID AND BUILD THE PRE-IMAGE.**
> **A1.1** — Print your full plan path, then extract from the BASENAME with `re.findall(r'^(?:in-progress-)?executable-(\d+)\.md(?:\.pristine)?$', basename)`; **assert exactly one match** (zero or more → HALT and report the basename verbatim; the fullmatch anchoring is 536's carried guard against slug digits).
> **A1.2** — Dump the FULL disposition table to `knowledge/development/gate1-heldpair-pre-dump-2026-08-25.txt`: `SELECT id, status, COALESCE(route,'-'), COALESCE(status_updated_by,'-'), COALESCE(status_updated_at,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals ORDER BY id;` — redirect target worktree-relative; the SELECT reads the canonical absolute path. Six columns because the dump must RESTORE (both rows' stamps are NULL today) and must SEE any target write (this plan makes none).
>
> **Task B — ONE transaction, ONE UPDATE, in-transaction verification before COMMIT.** Canonical Python (`sqlite3`, `PRAGMA busy_timeout=5000`, `BEGIN IMMEDIATE`), NO heredoc, canonical absolute DB path. ⚠️ **`:TS` computed ONCE before `BEGIN IMMEDIATE`; print it; record it verbatim in the dev log.**
>
> 1. `UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_by='ceo', status_updated_at=:TS WHERE id IN (378,389) AND status='proposed';` — **rowcount must be exactly 2, or ROLLBACK + HALT.** The `AND status='proposed'` guard is the idempotence AND window guard (536's carried law). **The payload is an immutable input — a mismatch is never resolved by editing the list.**
>
> - **In-transaction posts, before COMMIT:** `proposed` within 354–410 = **0**; the `accepted|codify` id set within 354–410 has size 25 and CONTAINS both 378 and 389 (print the two rows); global `accepted|codify` = **30**. **Any mismatch → ROLLBACK + HALT with the numbers.**
> - Journal mode WAL (verified 2026-08-25); a persistent locked error → HALT verbatim; an exception before COMMIT is a clean retry-later state.
>
> **Task C — post-image + untouched-population proof:** dump the same SELECT to `knowledge/development/gate1-heldpair-post-dump-2026-08-25.txt`; `diff` pre vs post — **expected: exactly rows 378 and 389 change as specified, paired old/new lines, ZERO lines for any other id, ZERO `target_artifact` changes.** Paste the RAW diff in the dev log. A single foreign line → HALT; no compensating writes.
>
> **Task D — DEPOSIT AND COMMIT, in order.** **D1** — dev log at `knowledge/development/gate1-heldpair-dev-log-2026-08-25.md`: `$ROOT`, `<plan-id>`, both dump paths + line counts, the transaction script verbatim, the rowcount, the in-transaction posts, `:TS` verbatim, the RAW diff. **D2** — commit ALL THREE Scope files in ONE commit, pathspec naming exactly them; message `[<plan-id>] Step 1 — gate1 held-pair routing 378+389 (accepted|codify, ceo)`; commit only, NO push. **D3** — assert `git show --name-only --format= HEAD` prints exactly the three Scope files (no already-committed branch exists here: only D2 commits Scope files; a post-COMMIT death re-enters through A0's redo branch and HALTs). **D4** — `#### Prompt Feedback` only if any; **NO `#### Forward Register`, either step.**
>
> **Scope:**
> - `knowledge/development/gate1-heldpair-dev-log-2026-08-25.md`
> - `knowledge/development/gate1-heldpair-pre-dump-2026-08-25.txt`
> - `knowledge/development/gate1-heldpair-post-dump-2026-08-25.txt`
>
> **STOP. Do NOT proceed to Step 2. Wait for the verdict.**

**Deposits:**
- `lessons-forge/knowledge/development/gate1-heldpair-dev-log-2026-08-25.md`
- `lessons-forge/knowledge/development/gate1-heldpair-pre-dump-2026-08-25.txt`
- `lessons-forge/knowledge/development/gate1-heldpair-post-dump-2026-08-25.txt`

---
---

## STEP 2 — QA

> **FIRST — resolve the tree:** `ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT`; print it.
>
> **Task Q0 — RE-PIN (the DB is untracked; the pin is CONTENT, not git).**
> 1. `git -C "$ROOT" log -1 --oneline --` the three evidence files — newest commit touching any must be Step 1's; foreign → HALT.
> 2. `sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 354 AND 410;"` — **must print 0.**
>
> **MANDATORY — Rule 20 self-check (canonical block, the exact template)** from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path). Placeholders: `plan_slug`: `gate1-route-heldpair`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/gate1-route-heldpair-qa-2026-08-25.md`; `evidence_dir` derived from `pwd`; `required_evidence_files`: `[pytest_full.txt, routing-verification.txt, diff-audit.txt]`. **Deposit all three BEFORE running the block — it `sys.exit(1)`s on any missing OR ZERO-BYTE file.** Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, both byte-exact (em-dash U+2014).
>
> ⚠️ Immediately after the verification table write exactly `## Evidence and Narrative`. **Evidence rule:** RAW output, never a summary; backtick any ❌ marker inside quoted literals.
>
> **Verification table, one row per claim (HALT on any FAIL):**
> **1. THE WRITE LANDED, read from the DB.** Rows 378 and 389: `accepted|codify`, `status_updated_by='ceo'`, both `status_updated_at` equal to each other AND to the dev log's recorded `:TS` verbatim. Global `accepted|codify` = 30 (⚠️ a LOWER number means an ingest staled routed rows inside the verdict window — name the missing ids). → `routing-verification.txt`
> **2. UNTOUCHED POPULATION.** Re-run the diff of the committed dumps in this session: exactly 2 changed rows (378, 389), zero foreign ids, zero `target_artifact` changes; report changed-row and changed-line counts separately. → `diff-audit.txt`
> **3. THE DUMPS ARE THE COMMITTED ONES.** `git show HEAD:<path>` for both dumps matches the working tree byte-for-byte. → `diff-audit.txt`
> **4. FULL SUITE.** Run `src/test_lessons_forge.py` whole; raw summary line VERBATIM. **Measured at authoring 2026-08-25: `63 passed`** — a measurement, not a bar; higher is not a failure (report the delta); only a FAILURE or below-63 is a HALT. → `pytest_full.txt`
> **5. THE DB WAS NOT COMMITTED.** Both step commits show no `lessons-forge.db`; `git ls-files --error-unmatch lessons-forge.db` still errors. → `routing-verification.txt`
> **6. NOTHING ELSE MOVED.** `git status --porcelain` at `$ROOT` EMPTY; `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `PANEL_SEAT_TEMPLATE.md`, `LESSONS.md`, `knowledge/FORWARD.md` absent from both step commits.
>
> Then `## Evidence and Narrative`, then the Output Receipt. **`### Ledger Updates`** via Write/Edit, EXACTLY ONCE, `##`-level after `## Evidence and Narrative`, blank line after the last subsection; **OMIT `#### Forward Register` ENTIRELY.**
>
> **FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec naming exactly the Scope files; assert `git show --name-only --format= HEAD` prints exactly them. Commit only — NO push.
>
> **Scope:**
> - `knowledge/qa/gate1-route-heldpair-qa-2026-08-25.md`
> - `knowledge/qa/evidence/gate1-route-heldpair/pytest_full.txt`
> - `knowledge/qa/evidence/gate1-route-heldpair/routing-verification.txt`
> - `knowledge/qa/evidence/gate1-route-heldpair/diff-audit.txt`

**Deposits:**
- `lessons-forge/knowledge/qa/gate1-route-heldpair-qa-2026-08-25.md`
- `lessons-forge/knowledge/qa/evidence/gate1-route-heldpair/pytest_full.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-route-heldpair/routing-verification.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-route-heldpair/diff-audit.txt`

---

## Drafting Cycle

**Tier:** T1 — computed. T-2 fires (production-data mutation, 2 rows); T-5 does not (dump-pair recovery, precedent 536/326); T-8 does not (536 closed the SAME DAY, same table, same transaction shape, 55 rows to this plan's 2); T-6 does not (no doctrine edit).

**Clone-diff against `executable-536` (Done), three passes:** **Facts** — WAL ✓, `_TERMINAL_STATUSES` unchanged at :31 (`accepted` still absent; population 28 → 30 here) ✓, DB untracked ✓, both target rows' stamps NULL ✓, suite 63 ✓ (all re-verified live 2026-08-25, same session as 536's closure). **Artefacts** — addressing contract, `:TS` single bind, `status='proposed'` guard, immutable payload, six-column dump pair, single-commit Task D with no already-committed branch, anchored plan-id regex, range-scoped Q0, set-membership QA: ALL CARRIED; the four-statement structure collapses to one (the only statement), so 536's disjointness argument is vacuous here and REMOVED rather than carried as dead text. **Structure** — `status_updated_by` flips `'planner'` → `'ceo'` (the decider changed: 536 wrote the delegated non-author's dispositions; this writes the CEO's ruling), and the exhaustiveness polarity flips (536 deliberately left 2 rows; this one finishes the range to 0) — both stated where they bind (A0, Task B, QA row 1).

**Walks:** 2 — five lenses each, strictly sequential.
- Weak spots:          w1 1 folded — **1/1 pre-existing**, instruction-class. ⚠️ QA row 1 initially compared the two timestamps only to each other; equal-but-wrong (a second writer stamping both) would pass — now also compared to the dev log's recorded `:TS` verbatim, making the window guard real.
- Destruction:         w1 1 folded — **1/1 pre-existing.** A0's redo branch initially keyed on `accepted|codify` alone; a partial state (378 routed by a foreign writer, 389 untouched) matched neither branch cleanly — the redo reading now requires BOTH rows to carry the full target signature including `'ceo'`, and anything mixed falls to the concurrent-writer arm.
- Vulnerabilities:     w1 dry — within-payload swap is impossible at n=2 with one destination; the residual (a wrong payload authored here) is countered by the packet's DECIDED block naming both ids.
- Integration-record:  w1 1 folded — record-class: the hazard note initially said "28" where the post-write population is 30; corrected to the 28 → 30 form with the Gate-2 HALT bar at 30.
- ACID:                w1 dry — die before B → A0 re-pins; die after COMMIT → A0's redo branch detects the full signature and escalates; die between D2 and Step 2 → Q0.1 re-pins.
- **Walk 1 total: 3 findings, 3 folded — instruction 2 / record 1, 0 HIGH.**
- Weak spots:          w2 dry — the `:TS` three-way comparison re-derived: dev log value → both rows → equality, one chain, no gap.
- Destruction:         w2 dry — the redo/mixed/foreign triage re-walked against the folded A0; every state reaches exactly one arm.
- Vulnerabilities:     w2 dry.
- Integration-record:  w2 dry — 28 → 30 consistent at all three sites (header anchor, Task B post, QA row 1).
- ACID:                w2 dry.
- **Walk 2 total: 0 findings — instruction 0 / record 0, ALL FIVE LENSES DRY.**

**Closing:** ✅ **BAR MET at walk 2 — a dry confirming pass, all five lenses.** The §2.7 closing re-read ran after this record was written: arithmetic re-derived (w1 3 folded = lens 1 + lens 2 + lens 4; w2 zero), no instruction-stream defect found.

**Conformance (§5):** `cycle_check` and `plan_lint` both run at the deposit path resolution pre-deposit, in the lens-line representation 536's hold taught (the consumer's parse IS the record's required form); exit codes recorded, branched on. Any verdict but BAR_MET / exit 0 → do not deposit.

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py, /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/executable-536.md, /Users/marklehn/Developer/GitHub/gate1-packet-2026-08-25.md
writes: lessons-forge.db, knowledge/development/gate1-heldpair-dev-log-2026-08-25.md, knowledge/development/gate1-heldpair-pre-dump-2026-08-25.txt, knowledge/development/gate1-heldpair-post-dump-2026-08-25.txt, knowledge/qa/gate1-route-heldpair-qa-2026-08-25.md, knowledge/qa/evidence/gate1-route-heldpair/pytest_full.txt, knowledge/qa/evidence/gate1-route-heldpair/routing-verification.txt, knowledge/qa/evidence/gate1-route-heldpair/diff-audit.txt
open_forks: none — the 378/389 fork is RULED (gate1-packet-2026-08-25.md DECIDED block); Gate 2 executes the ruling
walks: 2
yields: 3, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A
