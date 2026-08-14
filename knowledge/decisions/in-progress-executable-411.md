# Lessons Forge — Cycle Run 2026-08-14, PLAN A: ingest the 6-entry fold-damage batch (classification held to Plan B)

**Date:** 2026-08-14 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 6) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-ingest-folddamage-2026-08-14`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Ingest only.** This plan takes the 6 un-ingested `LESSONS.md` entries (the fold-damage batch, appended 2026-08-14 at root commit `e0da6a8`) into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**.

**Clone lineage — measured, not recalled:** 247 → … → 357 → 381 → **397** (direct origin AND newest same-class; both roles resolve to the same plan, verified against `Done/` by ship date). ⚠️ **This plan was derived by READING 397 SECTION BY SECTION and re-deriving every value, NOT by token-swapping it** — the batch appended today includes the entry recording what a token-swapped derivation cost (17 of 18 origin-carried findings, one a run-halting BLOCKER). Applying that entry to its own ingest is deliberate.

### ⚠️⚠️ INHERITED FACTS FROM 397 THAT ARE FALSE HERE — every one re-measured 2026-08-14

1. **⚠️⚠️ `NT_COUNT` IS **3**, NOT 0 — AND 397's G1 WOULD HAVE HALTED THIS RUN.** Every prior ingest asserted an empty non-terminal set and made `NT_COUNT > 0` an unconditional HALT. **The Gate-2 queue is legitimately open: proposals 340, 342, 346 stand `accepted|codify`** (341 shipped as plan 405 today; 337/338/339 → `implemented`; 343/344/345 → `reference`). G1 is therefore re-keyed below to a **VALUE guard, not a count guard**: the non-terminal set must be EXACTLY `{340, 342, 346}`, named by id. A count-only check would pass a foreign in-window row that displaced one of ours.
2. **⚠️ THE EM-DASH UNIFORMITY IS BROKEN — only 3 of 6 headings carry ` — `** (positions 1, 2, 4). Every prior batch was uniform, and every prior plan wrote "the whole-heading fallback does not fire on this batch." **Here it FIRES for three entries.** Measured by running the real `run_full_lessons_cycle` against a scratch COPY of canonical: the fallback fires and produces **`duplicates_marked_count = 0`** — no duplicate proposal is created. That is an EXECUTED result, not an argument; G3's zero is expected on evidence rather than on the uniformity premise this batch no longer satisfies.
3. **THE BATCH IS 6**, all dated 2026-08-14, appended after the last ingest at root commit `e0da6a8`, at file positions **282–287 of 287 parsed**. Dry run (real `ingest_lesson_entries`, scratch copy, rolled back): **would_insert 6 / would_update 0 / unchanged 281**.
4. **BASELINES MOVED:** `E0 = 338`, `P0 = 346` (`sqlite_sequence` agrees). Status distribution (zero-emitting, all EIGHT statuses): implemented **279** · superseded **28** · reference **18** · rejected **15** · stale **3** · **accepted 3** · proposed 0 · ambiguous 0 — total 346. **`SURFACEABLE_BASE = 0`** (proposed + ambiguous — note this is 0 even though NT is 3, because all three non-terminals are `accepted`; the two quantities have come apart for the first time and must not be conflated). `STALE_COUNT = 3` (98/121/130).
5. **THE SENTINEL MOVES TO ENTRY 338** — content-hash `359bf0267d500f50e67b4748a974b468620d8eb25c58b1fd4c046d0fabffaf9a`, heading `2026-08-13: The daemon claims an uncommitted deposit within one second — commit the claimed rename, and predict ids, never mint [tag: operational-recovery]`. Named by id, never `MAX(id)`; parsed-match count measured **1**; not file-last (the 6 follow it).
6. **ONE HOSTILE HEADING** (apostrophe) at batch position **2** → predicted entry **340**. Bind headings as query parameters everywhere.
7. **THE DOCTRINE PINS MOVED AGAIN — DRAFTING_CYCLE is now v2.10** (plan 405, today):
   - v2.10, moved by plan 405 today (397 pinned `ea3049ce…` v2.9):
     `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → `943971f5f909b089cfb276de31ea8eaf2b2680b4e1ccc5378413f8df8fccb941`
   - v4.88, unchanged second cycle:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` → `4f33c3884b426189ba9f019c0722681a4446e5f9223b1f0f10c117f7de0691a0`
   - unchanged SIXTH cycle running:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` → `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0`
   ⚠️ **The interleaved descriptor lines are LOAD-BEARING, not decoration: the (q) resolver takes the FIRST path in a token's context window, so three consecutive `shasum` lines make each digest resolve against the PRECEDING pin's path — measured here as two false MISMATCHes before this form was restored from 397.**
8. **THE BACKUP GLOB POPULATION IS 13** (`data/backups/lessons-forge-pre-cycle-*.db`). ⚠️ **The `.db` suffix is load-bearing in every `find`: a bare prefix also matches `-wal`/`-shm` sidecars and returns ~3 per backup** (executed proof at the 405 cycle). The count is not the guard; the id token `-<id>-` is.
9. **The candidate pool** of parsed-and-matched ids measured **281**; `detect_duplicates` signature unchanged.
10. **`decisions/` state:** lessons-forge carries ZERO non-Done entries (re-measured). Other repos are out of scope for the single-writer check — it globs `in-progress-*.md` in THIS project only.

### ⚠️ NUMBERING
- **`lesson_entries.id` 339–344** — THIS batch's 6 (verified by executing the real cycle against a scratch copy: ids 339–344 assigned in parse order).
- **`lesson_proposals.id` 347–352** — Plan B's 6 (NOT this plan's; verified against `P0` at Plan B's own authoring). **The rehearsal confirmed `MAX(lesson_proposals.id)` stays 346 through the ingest.**
- **Never write a bare numeral in 339–352 without its namespace.** Derivation, not a gate: every step keys on the parser diff and `source_heading`.

### Residual risk register
- **Best verified:** every number above produced by running the real code read-only or against a scratch COPY — including a FULL `run_full_lessons_cycle` rehearsal that landed 6 entries with 0 duplicates and P0 unmoved.
- **⚠️ The batch fingerprint is the positional guard:** `a94061915743eb8e0cdfda6ea17ae8e73c48faa1f391cd6f355db53bdbf4cb1b`.
- **Genuinely new since 397:** an OPEN Gate-2 queue (item 1) and a NON-UNIFORM em-dash batch (item 2). Both invert a premise every prior plan in this lineage asserted.
- **⚠️ A parallel terminal is live** (invoice-pulse plans 409/410 in flight at authoring; store-disjoint from lessons-forge, but it shares the ROOT repo, so a root-HEAD move is expected — G2's arm is conditional on the path diff).

**Scope discipline:** cycle run only. Routes stay `NULL`; **no `insert_proposal` anywhere.** Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals 98/121/130 (`stale`) or 340/342/346 (the live Gate-2 queue). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is fingerprint-pinned.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate re-assert the non-terminal set is **exactly `{340, 342, 346}`** — a changed set means in-window routing, and a changed COUNT alone is not the test.
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` gained ZERO rows against the baseline the agent captures at Step 1a (probe form `grep -c "^| "`).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive single-write ingest (T-2 fires); structure-for-structure clone of shipped 397, so T-8 silent.

**Walk register:** `governance/knowledge/research/walk-register-cycle-ingest-folddamage-2026-08-14.md` (schema 0.3), committed per phase; any bundling DECLARED.

**Walk 0 (context pin):** the FALSE-HERE table IS the pin — batch 6/0/281 over 287 parsed at positions 282–287, fingerprint `a9406191…`, E0/P0 338/346, **NT 3 = exactly {340,342,346}**, STALE 3, SURFACEABLE 0, sentinel entry-338 `359bf026…` (1 parsed match), three doctrine pins (DC moved to v2.10 by 405), **em-dash 3 of 6 — fallback FIRES, 0 duplicates by execution**, 1 hostile heading (entry 340), glob 13, candidate pool 281, root HEAD `9ec1076` with `LESSONS.md` porcelain clean, lessons-forge `decisions/` zero non-Done. **Full-cycle rehearsal on a scratch copy: ingested 6, duplicates 0, entries 339–344, P0 unmoved at 346.**

**Clone-diff vs 397 — read SECTION BY SECTION, not token-swapped (applying entry 342-of-this-batch to its own ingest):** two inherited premises INVERTED and both are load-bearing — the empty-NT premise (G1 re-keyed to a named-id value guard) and the em-dash uniformity (G3's zero now rests on an executed rehearsal, not on the fallback being inert). Carried and verified: manifest-first, the three-place dispatch probe, the `.db`-scoped `find`, per-id sentinel naming, the fingerprint guard, G2's conditional HEAD arm, the deposit-completion resume. Nothing dropped — and that is stated per item below, not as a blanket claim.

**Walks (2 warm):**
- Weak spots:          w1 dry (pre-flight, manifest-first, the resume arms and every derived number re-read against the measured tables; the NT/SURFACEABLE divergence stated at both capture sites); w2 dry.
- Destruction:         w1 dry (single INSERT path; the backup precedes mutation; G1's re-key STRICTENS — a value guard subsumes the count test it replaces — and G7 is NEW, protecting the live Gate-2 queue this plan must not touch); w2 dry.
- Vulnerabilities:     w1 executed — the full-cycle rehearsal on a scratch copy (6 ingested, 0 duplicates, P0 unmoved), the dry run, the fingerprint, the sentinel, the pool, the pins, and the em-dash fallback's actual behaviour; w2 dry.
- Integration-record:  w1 dry (Deposits project-prefixed with Scope repo-relative per the lessons-forge convention; the 405 cycle's `.db`-scoped `find` and `file:…?immutable=1` hardenings carried FORWARD with their proofs; stray-origin-token sweep clean); w2 dry.
- ACID:                w1 dry (one write step, one gate window; G2→G1→1b pre-mutation; G7 closes the loop on the queue).

**Splits: w1 instruction 0 / record 0 — DRY (the five clone-diff findings all landed at walk 0) · w2 dry.**

**Conformance (§5):** faithful-mirror `plan_lint` at the deposit-shaped scratchpad mirror — NEVER the real `decisions/`. Measured set at the close run is what freeze item 3 binds to; this Cycle-Log fill is what clears the placeholder-lens WARN.

**Closing:** walk 2 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced). The section-by-section clone-diff at walk 0 is where this cycle's yield landed (5 findings, 2 of them premise inversions that would have HALTed the run); scout declined with reasoning; fold-and-deposit exactly once.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (ingest the 6; NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **⚠️ EXECUTION ORDER — exactly: Step 0 → 1a → 1a-ter → 1a-bis → G2 → G1 → 1b (the only mutation) → G3–G6 → the ONE deposit.** ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning the full 6-id work list is this plan's CORRECT closing state.
>
> **Step 0 — dispatch state.** Three-place probe on `knowledge/development/dev-log-folddamage-step-1-2026-08-14.md` (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each with its exit code captured; probe 3's exit carries NO signal — pair it with a positive control against `knowledge/FORWARD.md` before reading silence as no-hit. Any hit → RESUME. All absent → FRESH. State the determination first.
>
> **Single-writer check:** `get_unclassified_entries` stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY**; this plan's own file present is normal, ZERO matches means the probe is broken, any OTHER match → HALT.
>
> **⚠️ HALT DURABILITY:** on any HALT commit existing deposit files by explicit pathspec and record the gate, its measured value, and whether the ingest committed. **Authorized writes: the `.backup`, `run_full_lessons_cycle`, this step's deposit.**
>
> **Scope:**
> - `knowledge/development/dev-log-folddamage-step-1-2026-08-14.md`
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL id. VERIFY, **in exactly this form**: `sqlite3 -readonly "file:$BK?immutable=1" 'PRAGMA integrity_check;'` → `ok`. ⚠️ **The `file:` URI prefix and `?immutable=1` are BOTH load-bearing — `.backup` writes a WAL-header DB with no `-shm`, and a plain `sqlite3 -readonly "$BK"` fails with `unable to open database file (14)` (executed proof, 405 cycle).** Backup counts == live (fresh: **338 entries / 346 proposals**). Resume glob: `find … -name 'lessons-forge-pre-cycle-<id>-*.db'` — **`.db`-scoped; a bare prefix matches sidecars and returns ~3 per backup, firing a spurious HALT** — EARLIEST match, prove pristine by `MAX(id)` = 338/346.
>
> **Baseline capture (read-only, raw):** (1) the zero-emitting distribution over ALL EIGHT statuses (expected: implemented 279 · superseded 28 · reference 18 · rejected 15 · stale 3 · **accepted 3** · proposed 0 · ambiguous 0); (2) proposals by category; (3) total `lesson_entries` (338); (4) sentinel entry 338 hash == `359bf026…` (mismatch = HALT, not correction); (5) `STALE_COUNT=3`; (5b) `SURFACEABLE_BASE=0` ⚠️ **labelled distinctly from NT — they have come apart this cycle**; (6) `E0` == 338, `P0` == 346; (7) **NT capture BY ID, not by count:** `SELECT 'NT='||GROUP_CONCAT(id) FROM (SELECT id FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous') ORDER BY id);` → printed token required; silence = broken invocation → HALT; (8) FORWARD baseline `grep -c "^| "`, recorded raw. **Capture only — G1 owns the verdict.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write + `git commit` the stub `knowledge/development/dev-log-folddamage-step-1-2026-08-14.md`: `Status: Partial — in flight (pre-ingest stub)`; the absolute backup path; E0/P0; **the NT id-list line**; STALE; SURFACEABLE; the FORWARD baseline; the full distribution; the sentinel hash; **the three doctrine pins, raw, HALT unless all three print.** The final Receipt rewrites this file but carries any first-dispatch ingest dict forward verbatim.
>
> ### Step 1a-bis — pre-ingest guard (read-only)
> 1. `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")`; tally the whole-corpus dry run by `source_heading` lookup. **FRESH → assert `would_insert == 6` AND `would_update == 0`** (Planner measured 6 / 0 / 281 over 287 parsed). **RESUME → `would_update == 0` and `would_insert ∈ {0, 6}`** — anything in 1..5 = foreign writer → HALT.
> 1b. **THE BATCH FINGERPRINT:** sha256 of `"\n".join(<would-insert headings in parse order>)` == **`a94061915743eb8e0cdfda6ea17ae8e73c48faa1f391cd6f355db53bdbf4cb1b`** (first heading starts `2026-08-14: A fold is the only edit`, last starts `2026-08-14: A session that crosses midnight`). Mismatch → HALT. **RESUME with `would_insert == 0` → SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** parsed entry matching entry 338's heading — exactly 1 match, hash equal → PASS; else HALT.
> 3. **Duplicate pre-check.** (a) pre-existing ids — mirror the ingest's candidate construction (parsed-and-matched, ~**281**; PRINT the list length first, HALT if 0 or wildly off); `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. (b) the 6 parsed batch entries: criterion 1 **UNFALSIFIABLE** (the reference carries no Tag: lines — inert); criterion 2 the `_EM_DASH_SEP` title-substring — ⚠️ **only 3 of 6 headings carry the separator, so the WHOLE-HEADING FALLBACK FIRES for the other three. This is the first batch in this lineage where it does. Report what it returns; the Planner's rehearsal of the REAL cycle against a scratch copy measured `duplicates_marked_count = 0`, so 0 is expected ON EVIDENCE — but a hit here is a finding, not a contradiction, and HALTs.** **POSITIVE CONTROL from ONE read:** byte length + the LOWERCASE sentinel `orchestration plan rules` in the lowered in-memory string; zero length or missing sentinel → every zero is void → HALT.
> 4. Record actuals — measured numbers, never a pre-composed "empty" string.
>
> ### Gates run pre-mutation
> - **G2 — provenance:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (didn't run); non-empty output → HALT (never ingest an uncommitted corpus). Record `rev-parse --short HEAD` (authoring: `9ec1076`; **a mismatch is EXPECTED — a parallel terminal shares this repo**: run `git diff --stat 9ec1076..HEAD -- LESSONS.md` — empty → reconcile-note and PROCEED; non-empty → HALT, the fingerprint premise fell). Confirm the stub carries the three pins.
> - **⚠️⚠️ G1 — the non-terminal precondition, RE-KEYED AS A VALUE GUARD (this is the arm 397's form would have failed):** capture the NT id-list and `STALE_COUNT`. Arms in order, first match wins: (1) **NT is EXACTLY `340,342,346` AND `STALE_COUNT == 3`** → PASS (the live Gate-2 queue; on a step-0 RESUME record `PASS (resume, pre-mutation)`). (2) **NT contains ANY id outside that set** → HALT naming every id, status and route — that is in-window foreign routing. (3) **NT is MISSING any of the three** → HALT: a queue row was consumed under this plan. (4) **`STALE_COUNT != 3`** → HALT. ⚠️ **A count-only check (`NT_COUNT == 3`) is NOT sufficient — it passes a foreign row that displaced one of ours.**
>
> ### Step 1b — the ingest (ONCE)
> Open canonical read-WRITE. **`run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()`. **IMMEDIATELY append the verbatim returned dict to the stub and commit it again.** Print all seven keys. ⚠️ Re-verify the function against live source before running (authoring source-read + a full rehearsal: parses → ingests → builds candidates → `detect_duplicates` → inserts a `duplicate` proposal per hit → returns `get_unclassified_entries`; it does NOT classify) — changed behaviour → HALT.
>
> ### Post-mutation gates (report EVERY gate as a table row; run all before halting)
> - **G3 — `duplicates_marked_count == 0`**; scoped resume form `SELECT COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 338`. A zero is valid ONLY against 1a-bis's positive control.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty.**
> - **G5 — work exists:** `ingested_count == 6` → PASS. `== 0` + Complete receipt (DB-confirm `COUNT(*) WHERE id > 338` == 6) → idempotent re-dispatch note, stop. `== 0` + stub/absent receipt → deposit-completion resume from the stub. **∉ {0, 6} → HALT.**
> - **G6 — work-list reconciliation:** every id in `needs_classification` is `> 338` and `≤ 344` (range computed from confirmed E0). Outside-range → HALT + the `### Deferred entries (G6 candidate)` section AND the arithmetic 6-line anchor.
> - **G7 — the queue is untouched:** the non-terminal set is STILL exactly `340,342,346` after the ingest, and `MAX(lesson_proposals.id)` is still **346** (the rehearsal confirmed the ingest creates no proposal). Any change → HALT.
>
> **Self-report:** `SELECT id, source_heading FROM lesson_entries WHERE id > 338 ORDER BY id` → **6 rows (339–344)**, recorded as `- ingested entry=<id>` lines; `get_unclassified_entries()` == exactly those 6. **Receipt status from the CLOSED SET**, carrying: the dict verbatim; the G1–G7 table; the baseline distribution + sentinel + STALE + SURFACEABLE + the NT id-list + FORWARD; E0/P0; the 6-line anchor; the backup path labelled `pristine (pre-cycle)`; `#### Files Created or Modified` split committed/untracked; `#### Doctrine pins` verbatim from the stub. RAW output throughout; canonical Python file-write; explicit-pathspec commit with post-commit `git show --name-only --format= HEAD` + `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-folddamage-step-1-2026-08-14.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`), with the single G6-deferral exception.
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No classification.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-ingest-folddamage-2026-08-14`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-ingest-folddamage-qa-2026-08-14.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/`; `required_evidence_files` `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`. All four files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim; end with the self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-folddamage-qa-2026-08-14.md`
> - `knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/schema.txt`
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY (baseline 55 passed at authoring; a delta is reported, never asserted).
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY the 6 ids — NOT `[]`.** An empty work list means something CLASSIFIED the batch. `[]` → ❌ Critical.
> 3. **The 6 landed, only those** — `SELECT id, source_heading FROM lesson_entries WHERE id IN (<the 6>)` → 6 rows, headings equal to the anchor **bound as query parameters** (one carries an apostrophe — entry 340); reconcile `COUNT(*)` derivation `338 + 6 = 344`. → `invariants.txt`
> 4. **Plan-204 held, NO proposal created** — stale still 3; entry-338 hash `359bf026…` unchanged; dict's `updated_count`/`terminal_proposals_flagged` from the Receipt; ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 346 UNCHANGED**; the FULL zero-emitting 8-status distribution before/after, every bucket unchanged; **the non-terminal set still EXACTLY `340,342,346` by id** (a count is not the guard — the id set is). → `hash-trap.txt`
> 5. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`.
> 6. **Fingerprint provenance** — recompute the batch fingerprint over the 6 anchor headings read FROM THE DB (parse order = id order): == `a9406191…`; and `LESSONS.md` porcelain still clean at root.
> 7. **Register posture** — lessons-forge `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (other repos out of scope); `knowledge/FORWARD.md` delta against Step 1's captured baseline is **ZERO** by the same probe form (any new row is a finding: a `NONE.`-item row = a regression of plan 376's guard, a real-text row = foreign writer).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-folddamage-qa-2026-08-14.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/hash-trap.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/schema.txt`
