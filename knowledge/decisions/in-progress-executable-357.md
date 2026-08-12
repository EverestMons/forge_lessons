# Lessons Forge — Cycle Run 2026-08-12, PLAN A: ingest the 6-entry cold-panel batch (classification held to Plan B)

**Date:** 2026-08-12 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 6) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-ingest-cold-panel-2026-08-12`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Ingest only.** This plan takes the 6 un-ingested `LESSONS.md` entries (the cold-panel evidence batch, appended 2026-08-12 at root commits `041b0ef` + `eea5694`) into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**, authored against the work list this plan leaves behind. The A/B split is carried from the 339/340 lineage — the split collapses the verdict-gate guard matrix to ONE write step, ONE gate, ONE window — and is kept even at 6-entry scale because the newest same-class shipped that way and the structural reason (not the batch size) was the licence.

**Clone lineage — measured, not recalled:** 247 → 257 → 274 → 281 → 283 → 288 → 296 → 311 → **339** (direct origin and newest same-class; its Step 1 is the lineage's most-reviewed artifact). Cycle-class diff run at walk 0, every inherited fact RE-MEASURED 2026-08-12 read-only against live canonical.

### ⚠️⚠️ INHERITED FACTS FROM 339 THAT ARE FALSE HERE — every one re-measured 2026-08-12

1. **⚠️⚠️ `NT` IS EMPTY — `NT_COUNT = 0`. 339's central hazard is GONE, and its G1/receipt machinery built for the 42-row Gate-2 queue has NO OBJECT.** Plan 356 drained the queue this morning (`accepted|codify` → 0, the three PT rows `implemented`). The run is back to 311's non-destructive-by-construction shape — **and per 339's own doctrine that safety is a MEASUREMENT, not a construction: `would-UPDATE = 0` re-measured immediately pre-mutation (Step 1a-bis), G1 re-asserts `NT_COUNT = 0` live.** The collapse of the 42-id list machinery (339's Receipt item 5, the id-for-id QA reconciliation, the window-0 carve-out) is a **verified subtraction**: its premise (`status='accepted' AND route='codify'` rows exist) measured FALSE at authoring, and G1 arm 2 HALTs if it becomes true again in-window.
2. **THE BATCH IS 6, uniform and late:** all six dated 2026-08-12, appended after the last ingest, sitting at file positions 262–267 of 267 parsed. Dry run measured **would_insert 6 / would_update 0 / unchanged 261** over 267 parsed headings. **Never derive the batch from a date filter; the parser diff is authoritative.**
3. **BASELINES MOVED:** `E0 = 318`, `P0 = 326` (`sqlite_sequence` agrees on both). Status distribution (zero-emitting, all EIGHT schema statuses): implemented **265** · superseded **28** · rejected **15** · reference **15** · stale **3** · accepted **0** · proposed **0** · ambiguous **0** — total 326. **`SURFACEABLE_BASE = 0`** (proposed + ambiguous). `STALE_COUNT = 3` (proposals 98/121/130, settled 2026-07-16 — leave untouched). Whole-corpus `DUP_COUNT = 19` (baseline; G3 uses the batch-scoped form).
4. **THE HASH-TRAP SENTINEL IS ENTRY 318** — hash `260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8`, heading `2026-08-11: Four doctrine defects found by reading doctrine AS PROSE — the panel's prose-debt extension [tag: governance]`. Named by id, never `MAX(id)`. Not file-last (the 6 follow it), so the trailing-separator trap cannot reach it; regression sentinel for `_normalize_for_hash` only.
5. **TWO OF THREE DOCTRINE PINS MOVED** (authoring `shasum -a 256`, live tree): `DRAFTING_CYCLE.md` `817677db4a3df2a50bdaf345138e441533dc30690e6ced378482573fb79b79b6` (v2.5; 339: `0964e1a7…`) · `PLANNER_TEMPLATE.md` `8aac8aa9f107fc9b7b4dc7b7241ea9a253d57d07aab2877c81b748a88f84a58e` (v4.87, moved TODAY by plan 356) · `RULE_20_SELF_CHECK_BLOCK.md` `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0` (**unchanged third cycle running**). Agent re-measures at Step 1a-ter; these are the authoring reference.
6. **THE EM-DASH ASYMMETRY IS GONE: 6 of 6 headings carry ` — `** (339 had 24-of-41). The whole-heading fallback branch of `detect_duplicates` does not fire on this batch; say so rather than reporting a uniform "no hits."
7. **THREE HEADINGS ARE SHELL-HOSTILE** (apostrophes only — no quotes, no backticks): batch positions 1, 2 and 6 → predicted entry ids **319, 320, 324**. Bind headings as query parameters everywhere; never interpolate into a shell string.
8. **THE BACKUP GLOB POPULATION IS 10** (was 9 at 339). The count is NOT the guard; the id token `-<id>-` is. Derive resume dates from the actual filename, never the local dispatch date.
9. **`detect_duplicates` SIGNATURE:** `(conn, entry_ids, reference_files=None)` — verified against live source at authoring; the candidate pool of parsed-and-matched ids measured **261** (57 orphans excluded, 318 − 261 + 204-era artifacts reconciled by the parser diff itself).

### ⚠️ NUMBERING — one band, stated once
- **`lesson_entries.id` 319–324** — THIS batch's 6 entries (after ingest; assigned in parse order, verified by source read: `ingest_lesson_entries` iterates the parser's list with AUTOINCREMENT).
- **`lesson_proposals.id` 327–332** — Plan B's 6 proposals (NOT this plan's; nothing here creates them).
- **Never write a bare numeral in 319–332 without its namespace** ("entry 319", "proposal 327"). This plan's own id and the plan-356/354/355 ids are a third space.
- Derivation, not a gate: every step keys on the parser diff and `source_heading`, never a predicted id; heading wins on any disagreement.

### Residual risk register
- **Best verified:** every number above produced this session by running the real code read-only against live canonical (the 6/0/261 dry run; E0/P0 with `sqlite_sequence` agreement; the 8-status zero-emitting distribution; NT/STALE/DUP; entry-318's hash; three pins; 6/6 em-dash; 3 hostile headings; 55 collected tests; fingerprint below).
- **Not carried:** the placement scout, tag precedents, routing analysis — Plan B's, authored from the landed work list.
- **⚠️ The batch fingerprint is the plan's positional guard** (Step 1a-bis item 1b) — counts alone cannot see a swap.
- **Genuinely new since 339:** none — this run exercises 311's empty-NT shape with 339's hardened machinery; the NT-empty G1 arms below are REBUILT (339's arms assumed 42 and are all unreachable here; do not carry them).

**Scope discipline:** cycle run only. Routes stay `NULL`; **no `insert_proposal` anywhere in this plan.** Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`. Do NOT touch proposals 98/121/130 (`stale`, settled). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is fingerprint-pinned, and PLANNER_TEMPLATE v4.87's corpus-freeze rule (shipped TODAY by plan 356) now codifies exactly this prohibition; `halted-executable-334.md` in `decisions/` is PARKED and does not freeze, per the same rule's boundary.

**Concurrency:** dispatch with NO other lessons-forge cycle in flight. The parallel terminal currently runs an invoice-pulse cycle (id 355 lineage) — different project, no shared store; the single-writer probes below still run. **Root HEAD at authoring `da595b9` — a HEAD mismatch at G2 is a reconcile-note, not a halt; two foreign commits landed on root DURING this plan's authoring window** (walk-register rows, LESSONS.md untouched, verified by path diff).

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict (`pause_for_verdict` is a header contract the runtime does not police).
- At every gate re-assert `accepted|codify` count is **0** (one command; a non-zero means in-window routing — investigate before continuing).
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` gained **ZERO rows** (this plan emits none; a row appearing = the QA agent's habit or a foreign writer — check the transcript FIRST, in that order).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive single-write ingest; the destructive premise that made 339 a T2 measured ABSENT (NT = 0, live). Clone of 339's final form at 6-entry scale; walk-0 clone-diff run against 339 as newest same-class, all deltas enumerated in the FALSE-HERE table above.

**Walk 0 (context pin):** the FALSE-HERE table IS the pin — E0/P0 318/326, NT 0, STALE 3, DUP 19, batch 6/0/261, fingerprint `1e3eb3de…`, sentinel entry-318 `260857bb…`, three doctrine pins (two moved, R20 unchanged), 6/6 em-dash, 3 hostile ids, glob 10, tests 55, root HEAD `da595b9`, `detect_duplicates(conn, entry_ids)` signature verified. Clone-diff verdict: 2 dropped-with-premise-measured-false (the 42-id machinery, the window-0 carve-out), G1 rebuilt for empty NT, everything else carried re-tokened.

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 1 folded — instruction, clone-adaptation (G5's arms carried 339's `ingested_count ∈ {0, 41}` prose in one site while every gate here keys on 6; swept to `{0, 6}` and the G6 range re-derived `E0+1..E0+6` = 319–324 at both sites).
- Destruction:         w1 dry (single INSERT path; backup verified before mutation; no guard relaxed — the subtractions all carry their measured-false premise inline).
- Vulnerabilities:     w1 executed — the dry-run/fingerprint/sentinel battery re-run clean same-session; hostile headings bind as parameters at every site; the zero-emitting forms carry their printed-token guards; `?immutable=1` for backup reads carried.
- Integration-record:  w1 dry (lineage table verbatim-extended; the v4.87 corpus-freeze cross-reference verified against the live template — the rule this plan cites shipped today and its boundary names the exact `halted-*` file present).
- ACID:                w1 dry (one write step, one gate window; G1–G6 ordering carried from 339 with G2/G1 pre-mutation; half-states owned by Step 0's three-place probe + G5's arms; the backup is the durability floor).

**Walk-1 split: instruction 1 / record 0.** Re-opens; walk 2 owed.

**Walk 2** (whole artifact; new surface = the walk-1 sweep):
- All five lenses:     w2 dry — the `{0, 6}` sweep verified at every arm site (grep-enumerated); battery stable; lint at the FAITHFUL mirror **EXIT 0, ZERO WARNs** ~~(the two known-benign steps-mention-tests rows)~~ **struck: that expectation was RECALLED from 339, not measured — the predicted-number class, caught when the lint actually ran; the measured bare-mirror set is THREE (o1) path WARNs, all mirror-fidelity artifacts clearing when the four real files are copied in**; Closing asserts the dry close.

**Walk-2 split: instruction 0 / record 0 — DRY. The walk phase meets the §2 bar on the dry branch; T1, no panel owed.**

**Conformance (§5):** run at shape-stability post-walk-1 and re-run post-walk-2 at the deposit-shaped scratchpad mirror (NEVER at the real `decisions/` — the daemon claims and DISPATCHES a plan-shaped file same-second, proven live 2026-08-12). **Measured: EXIT 0, ZERO WARNs at the FAITHFUL mirror** — fidelity requires copying FOUR real files into the mirror root (`src/test_lessons_forge.py`, `src/db.py`, `agents/FORGE_LESSONS_AGENT.md`, `knowledge/FORWARD.md`); a bare mirror shows THREE (o1) path WARNs, which are mirror artifacts, not plan defects (fidelity, not suppression). Last run: at deposit.

**Closing:** walk 2 dry — instruction 0 / record 0; closed on the dry branch after 2 walks; clone-diff at walk 0 per §2.6; residue: none.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (ingest the 6; NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1-2 sentences): starting, and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.** Run from your own working tree; the only main-tree writes are the `.backup` and the DB mutation (both gitignored).
>
> **⚠️ EXECUTION ORDER — exactly: Step 0 → 1a → 1a-ter → 1a-bis → G2 → G1 → 1b (the only mutation) → G3–G6 → the ONE deposit.** ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning the full 6-id work list is this plan's CORRECT closing state.
>
> **Step 0 — dispatch state.** Probe three places (capture every exit code; silence is not a determination): (1) `git -C <your worktree> show HEAD:knowledge/development/dev-log-cycle-step-1-2026-08-12.md`; (2) the working tree; (3) `git log --all -- <that path>` PLUS `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'` — probe 3's exit code carries NO signal; pair with a positive control against `knowledge/FORWARD.md` and only then read silence as no-hit. Any hit → RESUME (the stub's recorded values are authoritative). All absent → FRESH. State the determination first in the dev log.
>
> **Single-writer check:** (1) `get_unclassified_entries` stable across two reads; (2) `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **this plan's OWN renamed file present is the normal state; ZERO matches means the probe is broken** (re-verify the path); any OTHER lessons/cycle match → HALT. `halted-executable-334.md` is expected and parked — not a match.
>
> **⚠️ HALT DURABILITY:** on any HALT, commit existing deposit files by explicit pathspec; record the gate, its measured value, and whether the ingest committed. **DO NOT REPAIR — authorized writes: the `.backup`, `run_full_lessons_cycle`, this step's deposit.**
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-step-1-2026-08-12.md`
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL id from your plan filename. Do NOT inline `$(date …)` between single-quoted parts. VERIFY: `sqlite3 "file:<backup>?immutable=1" 'PRAGMA integrity_check;'` → `ok` (⚠️ `?immutable=1`, never `?mode=ro`, for backup reads — sidecars absent); backup counts == live counts (fresh: **318 entries / 326 proposals**; on RESUME do not assert them). Resume glob: `-<id>-` token, ends `.db`, EARLIEST match, prove pristine by `MAX(id)` = 318/326.
>
> **Baseline capture (read-only, raw output):** (1) the zero-emitting status distribution over ALL EIGHT statuses (expected: implemented 265 · superseded 28 · rejected 15 · reference 15 · stale 3 · accepted 0 · proposed 0 · ambiguous 0); (2) proposals by category; (3) total `lesson_entries` (318); (4) sentinel entry 318 hash == `260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8` (mismatch = HALT, not correction); (5) `STALE_COUNT=3` labelled; (5b) `SURFACEABLE_BASE=0` labelled; (6) `E0 = MAX(id) FROM lesson_entries` == **318**, `P0` == **326** (differing → HALT — but on a "fresh" read of E0=324, search `bellows-preserved/*` for the stub before diagnosing); (7) **NT capture:** `SELECT 'NT_COUNT=' || COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous');` → printed token required; silence = broken invocation → HALT. **Capture only — G1 owns the verdict.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write + `git commit` the stub `knowledge/development/dev-log-cycle-step-1-2026-08-12.md`: `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)`; the absolute backup path; E0/P0; the NT_COUNT line; STALE_COUNT; SURFACEABLE_BASE; the full status/category distribution; the sentinel hash; **the three doctrine pins — `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`, raw, HALT unless all three print** (G2 and the Receipt CITE this capture; neither re-measures). **THE OVERWRITE RULE:** the final Receipt rewrites this file but carries any first-dispatch ingest dict forward verbatim; on a resume the stub's values are authoritative.
>
> ### Step 1a-bis — pre-ingest guard (read-only)
> 1. From your worktree, `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` (the same parser the ingest calls); tally the whole-corpus dry run by `source_heading` lookup. **FRESH → assert `would_insert == 6` AND `would_update == 0`** (Planner measured 6 / 0 / 261 over 267 parsed). **RESUME → `would_update == 0` and `would_insert ∈ {0, 6}`** — anything in 1..5 = foreign writer → HALT. ⚠️ `would_update == 0` stays load-bearing as a plan-204-regression detector even with NT empty.
> 1b. **THE BATCH FINGERPRINT:** sha256 of `"\n".join(<would-insert headings in parse order>)`. **Expected `1e3eb3de7465542429ec912ee6857b402619c5e74be5ab86bf95b4b388b8e1f0`** (first heading starts `2026-08-12: The cold panel's operational layer is lore`, last starts `2026-08-12: The warm walk's mechanical/judgment split`). Mismatch → HALT (the batch is not the batch this plan pinned; a legitimate post-authoring append is still a HALT — CEO re-parameterizes). **RESUME with `would_insert == 0` → the digest is `sha256("")` = `e3b0c442…` and can never match: SKIP, record `FINGERPRINT=n/a (post-ingest resume)`.**
> 2. **Sentinel:** parsed entry matching entry 318's heading — exactly 1 match, hash equal → PASS; else HALT (classify whitespace-only vs substantive).
> 3. **Duplicate pre-check, both paths:** (a) pre-existing ids — mirror the ingest's candidate construction (parsed-and-matched; ~**261** ids; PRINT the list length first, HALT if 0 or wildly off — the function's empty-list early-return examines nothing); `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. (b) the 6 parsed batch entries (no ids yet — replicate the detector's current source read-only; reference at ABSOLUTE `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`): criterion 1 reported as **UNFALSIFIABLE (reference carries no Tag: lines — inert)**, criterion 2 the `_EM_DASH_SEP` title-substring — **all 6 headings carry the separator; the whole-heading fallback does not fire on this batch.** Any hit → HALT. **POSITIVE CONTROL from ONE read:** byte length + the LOWERCASE sentinel `orchestration plan rules` in the lowered in-memory string (the detector lowercases; a cased probe against it is entry-303's class); zero length or missing sentinel → every zero is void → HALT.
> 4. Record actuals — measured numbers, never a pre-composed "empty" string.
>
> ### Gates run pre-mutation
> - **G2 — provenance:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (didn't run); non-empty output → HALT (never ingest an uncommitted corpus). Record `rev-parse --short HEAD` (authoring: `da595b9`; mismatch = reconcile-note, near-certain). Confirm the stub carries the three pins.
> - **⚠️⚠️ G1 — the non-terminal precondition, REBUILT FOR EMPTY NT (339's arms assumed 42 and are unreachable):** capture `NT_COUNT` and `STALE_COUNT`. Arms in order, first match wins: (1) **`NT_COUNT == 0` AND `STALE_COUNT == 3`** → PASS (on a step-0 RESUME record `PASS (resume, pre-mutation)`). (2) **`NT_COUNT > 0`** → HALT naming every id, status, route — with NT empty at authoring, ANY non-terminal row is in-window foreign routing; no carve-out exists on this run (the window-0 Gate-2 carve-out's premise — a queued batch — measured absent). (3) **`STALE_COUNT != 3`** (either direction) → HALT.
>
> ### Step 1b — the ingest (ONCE)
> Open canonical read-WRITE. **`run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()`. **IMMEDIATELY append the verbatim returned dict to the stub and commit it again** (the dict is unreproducible). Print all seven keys. ⚠️ **Re-verify the function against live source before running** (authoring source-read: parses → ingests → builds candidate ids from parsed-and-matched → `detect_duplicates` → inserts a `duplicate` proposal per hit → returns `get_unclassified_entries`; it does NOT classify) — changed behaviour → HALT.
>
> ### Post-mutation gates (report EVERY gate as a table row; run all before halting)
> - **G3 — `duplicates_marked_count == 0`**; scoped resume form `SELECT COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 318` (whole-corpus DUP is 19 by baseline and would false-HALT). A zero is valid ONLY against 1a-bis's positive control; control absent → `HALT (unverified)`.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty** (detector; on failure diff `status='stale'` vs baseline, name the backup).
> - **G5 — work exists:** `ingested_count == 6` → PASS. `== 0` + Complete receipt (DB-confirm `COUNT(*) WHERE id > 318` == 6) → idempotent re-dispatch note, stop. `== 0` + stub/absent receipt → deposit-completion resume: regenerate the Receipt FROM THE STUB (pins never re-measured; dict verbatim or declared absent; E0/P0/backup/sentinel/STALE/SURFACEABLE/distribution all stub-sourced). **∉ {0, 6} → HALT.**
> - **G6 — work-list reconciliation:** every id in `needs_classification` is `> 318` and `≤ 324` (range computed from confirmed E0, never from the list). Outside-range → HALT; write the `### Deferred entries (G6 candidate)` section (bare ids, one per line; approval = the CEO continue on this halt) AND the arithmetic 6-line ingested-entry anchor.
>
> **Self-report:** `SELECT id, source_heading FROM lesson_entries WHERE id > 318 ORDER BY id` → **6 rows (319–324)**, recorded as `- ingested entry=<id>` lines; `get_unclassified_entries()` == exactly those 6, verbatim. **Receipt status from the CLOSED SET** (Complete / Complete-idempotent / Partial-HALTED-at-gate / Partial-in-flight-stub), carrying: the dict verbatim; the G1–G6 table; the baseline distribution + sentinel + STALE + SURFACEABLE; E0/P0; the NT_COUNT line; the 6-line anchor; the backup path labelled `pristine (pre-cycle)`; `#### Files Created or Modified` split `##### Committed deposits` / `##### Untracked artifacts`; flags; `#### Doctrine pins` verbatim from the stub. RAW output throughout; canonical Python file-write, no heredoc; commit by explicit pathspec with post-commit `git show --name-only --format= HEAD` + `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-08-12.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`), with the single G6-deferral exception (`HALTED at G6` token + a `### Deferred entries (G6 candidate)` section — this step running IS the approval; open your message with `OPERATING UNDER G6 DEFERRAL: ids <list>`).
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No classification.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-ingest-cold-panel-2026-08-12`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-ingest-qa-2026-08-12.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/`; `required_evidence_files` `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`. All four files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim in the deposited report; end with the self-grep. ⚠️ Rule 19 verbatim: a check you cannot complete is `❌` with a reason, never a hedged `✅`. Status column exactly one glyph; no `|` in table cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-qa-2026-08-12.md`
> - `knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/schema.txt`
>
> **IN-WINDOW RECONCILIATION:** whole-corpus rows adjudicate in two parts — (a) HARD by id against Step 1's 6-line anchor (validate: 6 integers, none blank; missing/truncated → dependent rows `❌ (unverifiable)`, NO predicate fallback); (b) RECONCILE everything outside the set (report, note, still `✅`).
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — scoped to the Receipt's `##### Committed deposits`; per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY (baseline 55 collected; delta reported never asserted).
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY the 6 ids — NOT `[]`.** The inversion every prior cycle QA invites: an empty work list means something CLASSIFIED the batch, which nothing here is authorized to do. `[]` → ❌ Critical.
> 3. **The 6 landed, only those** — `SELECT id, source_heading FROM lesson_entries WHERE id IN (<the 6>)` → 6 rows, headings equal to the anchor **bound as query parameters** (three carry apostrophes — ids 319/320/324); reconcile `COUNT(*)` derivation `318 + 6 = 324`. → `invariants.txt`
> 4. **Plan-204 held, NO proposal created** — stale still 3 (98/121/130); entry-318 hash `260857bb…` unchanged; dict's `updated_count`/`terminal_proposals_flagged` from the Receipt; ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 326 UNCHANGED** (327+ means the detector fired and G3 should have halted); **the FULL zero-emitting 8-status distribution before/after, every bucket unchanged against the Receipt's item — a count is not a value guard**; `NT_COUNT` still 0. → `hash-trap.txt`
> 5. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`.
> 6. **Fingerprint provenance** — recompute the batch fingerprint over the 6 anchor headings read FROM THE DB (parse order = id order): == `1e3eb3de…`; and `LESSONS.md` porcelain still clean at root.
> 7. **Corpus-freeze posture** — `accepted|codify` count still **0**; `halted-executable-334.md` still the only non-Done `decisions/` entry (a second = in-window deposit, report ids).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-qa-2026-08-12.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/hash-trap.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-cold-panel-2026-08-12/schema.txt`
