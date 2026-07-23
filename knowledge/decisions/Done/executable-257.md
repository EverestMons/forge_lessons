# Lessons Forge — Cycle Run 2026-07-22 (ingest + classify the 15-entry 07-21/07-22 batch, classification SPLIT 8+7)
**Date:** 2026-07-22 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (Lessons Agent — ingest + classify first 8) → Step 2 (Lessons Agent — classify remaining 7) → Step 3 (DEV — report) → Step 4 (QA) | **qa_steps:** 4 | **pause_for_verdict:** always

## CEO Context

Cycle run only: ingest the un-ingested LESSONS.md entries and classify them into proposals. Gate 1 (route disposition) and Gate 2 (codification) are separate plans with CEO decisions between. Direct precedent: **247 → 248 → 249** ran this exact shape one batch ago (v4.76 → v4.77).

**Batch size is 15 — the largest this corpus has ingested in one cycle** (247 ran 12, the prior max). **Parser-verified at authoring time** (`parse_lessons_md` on the live file vs the canonical DB, read-only): LESSONS.md holds **121** entries, exactly **15** have headings whose `content_hash` is not in `lesson_entries`, and `get_unclassified_entries()` returns **`[]`** — so post-ingest the work list is exactly these 15. **2 are dated 2026-07-21** (the false-FAIL-check risk class; the drafting-cycle-cannot-validate-an-executable-check limit — session-3's two owed entries) and **13 are dated 2026-07-22** (the halted-archival arc's method + process lessons: the three-rung successor ladder, diagnostic-substance-is-findings, directory-deposit-unfalsifiable, grep-is-ignore-aware, remedy-recreates-the-disease, run-the-procedure-not-the-claims, restructuring-for-DRY-trades-a-surface, generalising-waters-down, deliverable-shape-is-unasked, read-the-record-before-deriving, worktree-OUTPUT-paths-must-be-working-tree-relative, a-mechanical-conformance-pass-belongs-in-the-cycle, pre-stated-conclusions-anchor-toward-the-cheap-disposition).

**⭐ CEO DECISION 2026-07-22 — classification is SPLIT across two verdict-gated steps (8 + 7), NOT a single step.** 15 is 1.25× the prior max and `reasoning` is the only field Gate 1 reads; a single agent degrading over 15 entries produces thin reasoning on the last few that passes every gate silently. Step 1 ingests the whole corpus and classifies the **first 8** work-list entries (ascending `id`); Step 2 re-derives the work list via `get_unclassified_entries` (the remaining 7) and classifies them. The split is the context-saturation mitigation (the "rotate the reviewer when late walks go quiet" entry is itself in this batch); each half is well under the proven-safe 12.

**⚠️ NUMBERING DISAMBIGUATION.** File-position counts (121 entries) and **DB row ids** (`lesson_entries.id`, `lesson_proposals.id`) are different namespaces. The agent derives every DB id from `get_unclassified_entries` / the ingest return — never hand-types a batch id. This plan deliberately names no batch entry id.

**⚠️ The corpus row count is 163, NOT 121 — do not read that as corruption.** `lesson_entries` holds **163** rows while the file has 121 entries; the surplus are orphan rows from headings reworded over the project's history. All 163 are classified (that is why `get_unclassified_entries()` is `[]`). **After this cycle expect 178 rows (163 + 15), and 186 proposals (171 + 15).** A reader who assumes "121 + 15" will see 178 and cry corruption — it is expected.

**⚠️ E0 / P0 — the resume-invariant handles.** Authoring-time values (confirm at Step 1a, do NOT assume; HALT if either differs on a fresh run): **`E0 = MAX(id) FROM lesson_entries = 163`, `P0 = MAX(id) FROM lesson_proposals = 171`.** The 15 batch entries permanently occupy ids **164–178** no matter how many dispatches classification takes. **`entry_id > 163` is the canonical handle for "this cycle's entries"; `route IS NULL` is NOT a usable handle** (pre-existing proposals already carry NULL routes — `route IS NULL` selects the whole historical set, not this cycle's 15). On a RESUME use the recorded `E0`/`P0` from the prior dispatch's deposit; do NOT re-run `MAX(id)` (post-ingest it returns 178/186 and would exclude this cycle's own rows).

**⚠️ G1 precondition (fresh-run safety) — measured 0 at authoring.** The ingest's update path stales **non-terminal** proposals (`proposed`/`accepted`/`ambiguous`); the plan-204 `_TERMINAL_STATUSES` guard protects only `implemented`/`rejected`/`superseded`/`reference`/`stale`. Measured: **ZERO** non-terminal proposals in the corpus → the fresh-run ingest is provably non-destructive. Confirm from your own baseline; any non-terminal proposal on a fresh run voids the safety → HALT before the ingest.

**⚠️ The `updated_count` / hash-trap watch (plan-204's live test).** Appending this batch gave the previously-last-ingested entry a trailing `---` — the exact trigger that used to flip a `content_hash` over whitespace. **Target: entry id 163** — *"2026-07-21: Context saturation is a reviewer failure mode…"*, `content_hash` `4e3392b1a766170f…` (record the full hash from your baseline). **Expectation: `updated_count == 0` and `terminal_proposals_flagged` empty. Verify and report the ACTUAL values; do not force the number.** Non-zero either way is a loud finding — HALT and diagnose (whitespace-only = a 204 regression; substantive = an unexpected edit the CEO must confirm).

**⚠️ The plan-154 dedup advisory is RETIRED — do NOT expect advisory lines** (plan 207 removed `detect_recently_implemented_overlaps`). Any `Recently-implemented overlap:` line in the report is a regression → HALT.

**Do NOT dedup against PLANNER_TEMPLATE.** Classification classifies on merits; **Gate 1** dedups against the LIVE template. If any batch entry's substance may already be codified (several refine `## The Drafting Cycle`), FLAG it in the synthesis for Gate 1 — do NOT skip or downgrade it (that makes a Gate 1 decision without a CEO). Verify any codification claim against the live template before repeating it.

**Cluster structure to name for Gate 1** (the same service 247 gave the 155-159 cluster): several entries refine **`## The Drafting Cycle`** (the mechanical-conformance-pass, deliverable-shape-is-unasked, restructuring-for-DRY, generalising-waters-down, remedy-recreates-the-disease, run-the-procedure, read-the-record, pre-stated-conclusions-anchor). A second cluster is **halted-triage method** (successor-ladder, diagnostic-substance-is-findings, directory-deposit-unfalsifiable, grep-ignore-aware). Name the clusters so Gate 1 can route coherently, not as scattered edits.

**Scope discipline:** cycle run only. Routes stay `NULL` at insert — the CEO assigns at Gate 1. **Do NOT edit PLANNER_TEMPLATE.md** (codification is Gate 2). **⚠️ Do NOT append to LESSONS.md while this plan is deposited-but-un-run** — the cycle parser-pins its batch at 15; a mid-flight append makes every count wrong and turns G6 into a halt (memory `lessons-forge-cycle-pins-batch-by-parser-count`).

**No diagnostic precedes this plan, deliberately** (recurring-cycle practice, per 247/243): every unknown was measured inline at authoring against live data — batch delta (15), G1 precondition (0 non-terminal), E0/P0 (163/171), the hash-trap target (id 163), LESSONS provenance (clean, root HEAD `9974f14`). If you would rather see a diagnostic first, say so.

**Deposit-once discipline:** deposited exactly once. **Authoring self-check:** `bellows/scripts/plan_lint.py` run at authoring — exit 0, (a)-(d) PASS; the known-benign `scope_check`-on-tests WARNs (Steps quote "named test" text from lesson entries) are expected — do NOT add test files to scope to silence them (memory `benign-gate-failure-classes`).

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/in-progress-executable-<id>.md (daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — Lessons Agent (ingest whole corpus + classify the FIRST 8)

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read your specialist `agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). **Its DB paths are written relative to the GitHub root, and you run in a worktree** — `lessons-forge/lessons-forge.db` resolves to nothing from where you stand. **Every canonical-DB access in this plan uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **Working location — the plan-225 trap.** Run commands from **your own working tree** and write every file there. **The ONLY exception is canonical-DB access, by the ABSOLUTE path above.** Do NOT `cd` to the main tree: report/deposit writes resolve RELATIVE paths, so a main-tree cwd puts output in main while you commit in the worktree — exactly the untracked-file collision that tore down plan 225.
>
> **Single-writer assumption.** Before Step 1a, confirm no concurrent cycle: `get_unclassified_entries` stable across two reads a moment apart, and no `in-progress-*lessons*` plan in `knowledge/decisions/`. If either suggests a concurrent writer, HALT.
>
> **Scope:**
> - `knowledge/development/classifications-summary-part1-2026-07-22.md`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-22.md`
>
> **Step 1a — restore point, then baseline. Before touching anything.** Back up canonical with `.backup` (NOT `cp` — a live WAL exists), to the MAIN tree by ABSOLUTE path (a worktree-local backup is destroyed by teardown): `mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups && sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<UTC-timestamp-colon-free>.db'"`. `.gitignore` matches `*.db`, so it is not committed — confirm absent in `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain`. **State the absolute backup path in your dev log.**
>
> **Then capture the baseline** (read-only), verbatim in the dev log: proposals by `status`, proposals by `category`, total `lesson_entries` count, and the id + `content_hash` of the entry currently last-ingested by file position (**confirm it is id 163**, *"2026-07-21: Context saturation…"*, hash `4e3392b1a766170f…` — the hash-trap target). **Also capture the two FIXED constants: `E0 = SELECT MAX(id) FROM lesson_entries`, `P0 = SELECT MAX(id) FROM lesson_proposals`. Confirm `E0 = 163`, `P0 = 171`; if either differs on a fresh run, HALT** (every downstream count derives from them). On a RESUME read E0/P0 from the prior deposit — do NOT re-run `MAX(id)`. **State `E0` and `P0` on their own line in the Output Receipt.**
>
> **⚠️ G1 fresh-run precondition:** the baseline must show zero `proposed`/`accepted`/`ambiguous` proposals; any such → HALT before the ingest (resume exempt — see G-timing).
>
> **Step 1b — run the ingest (ONCE, this step only).** Open canonical **read-WRITE** (plain `sqlite3.connect("/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db")` — NOT `?mode=ro`). Call `run_full_lessons_cycle(conn)` (its `lessons_md_path` defaults to `/Users/marklehn/Developer/GitHub/LESSONS.md` — confirm that is what it read). **`conn.commit()` after it returns** — this is the SQLite transaction, NOT a git commit; the DB is gitignored and no `.md` deposit exists yet; skip it and a step death LOSES the ingest. **This is a WHOLE-CORPUS re-hash**, not a tail append — any edit anywhere in LESSONS.md since the last cycle lands here as `updated_count`. **Record and PRINT the actual returned dict:** `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `terminal_proposals_flagged`, `needs_classification`.
>
> ## Step 1 gates — G1 through G6 (report EVERY one as a table row with its measured value + PASS/HALT)
>
> **Timing:** G2 pre-ingest; G1 pre-ingest on a fresh run (defer verdict past the no-op ingest on a resume); G3–G6 read the Step-1b dict.
> - **G1 — non-terminal precondition** (fresh-run; resume-exempt). Baseline zero `proposed`/`accepted`/`ambiguous` → PASS; else HALT before ingest. On a resume (`ingested_count==0`, `needs_classification` non-empty) record `PASS (resume)`.
> - **G2 — LESSONS.md provenance.** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md` **empty** (use `git -C <absolute root>` — a bare `git status` from the submodule worktree passes VACUOUSLY because LESSONS.md is absent there; **this batch contains the entry naming that exact failure class** — do not let this gate fall to the lesson it ingests), and record `git -C /Users/marklehn/Developer/GitHub rev-parse HEAD` (expected `9974f14`). Dirty → HALT.
> - **G3 — `duplicates_marked_count == 0`** (silent-drop guard). Non-zero → HALT and name which entry ids + why.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty** (hash-trap watch on entry id 163). Non-zero either way → HALT and show the diff, classifying whitespace-only (204 regression) vs substantive (unexpected edit, CEO confirms).
> - **G5 — there is work to do.** `ingested_count == 0` AND `needs_classification` empty → disambiguate: (a) truly nothing → HALT; (b) proposals for this cycle exist but deposits absent → deposit-completion resume, re-generate deposits from committed DB, STOP. `ingested_count==0` but `needs_classification` non-empty → `PASS (resume)`.
> - **G6 — work-list reconciliation.** `needs_classification` should be exactly the 15 batch entries. `needs_classification` LARGER than the batch → an older entry surfaced (a prior proposal went `stale`, the 204 signature) → HALT; the CEO chooses (i) classify batch + extra, (ii) batch only + record the deferred id(s) under `### Deferred entries (CEO-approved)`, or (iii) investigate first. Reconcile explicitly: list the ingested ids, list the work list, name any work-list entry NOT in this batch.
>
> **After the gate table: if all PASS (or `PASS (resume)`), continue to classification. Any HALT — stop and report; the ingest stays committed (G1 made it safe).**
>
> ### Classification — the FIRST 8 only (this step)
>
> **Derive the work list from `get_unclassified_entries` (Rule #47 — never hand-copied). Classify the first 8 in ASCENDING `id` order.** For each: read `id, source_heading, raw_content, tags, entry_date` from `lesson_entries`, apply ADR-002, and call `insert_proposal(conn, category, suggested_action, reasoning, confidence, ...)` — all four are REQUIRED positional args:
> - `category` ∈ `structural`/`instrumentation`/`governance_rule`/`language`/`narrative` (never hand-assign `duplicate`).
> - `suggested_action` — concrete natural-language recommendation (what changes, where).
> - `reasoning` — **quoted evidence** citing specific `raw_content` text from THAT entry, naming its id. Do NOT carry any claim from this plan's CEO Context into a `reasoning` field — the entry is the only source. If you cannot cite specific `raw_content`, STOP and report rather than writing a generic justification (a thin proposal passes every gate — worse than a halt).
> - `confidence` ∈ `low`/`medium`/`high`.
> Set `target_layer`/`target_artifact` per the specialist (a `governance_rule` gets `target_layer='governance'`, `target_artifact='PLANNER_TEMPLATE.md'`). Only `route` and `subcategory` stay `None`. Use `status='ambiguous'` only for a genuine no-fit (call it out by id at the TOP of the summary).
>
> **`conn.commit()` after each `insert_proposal` (or after the 8th at latest)** — incremental commit reduces worst-case loss and composes with the resume ladder. **Then git-commit the two `.md` deposits.**
>
> **Self-report:** print `SELECT id, entry_id, status, category FROM lesson_proposals WHERE entry_id > 163 ORDER BY id` — expect **8 rows** after this step (entry_ids among 164–178). Put it in the Output Receipt.
>
> **Deposit:** `knowledge/development/classifications-summary-part1-2026-07-22.md` (the cycle dict, the 8 classifications' per-entry reasoning, the cluster synthesis for Gate 1, any `ambiguous` flagged by id) + `knowledge/development/dev-log-cycle-step-1-2026-07-22.md` with an Output Receipt containing, each on its own labelled line: (1) the cycle dict verbatim; (2) the G1–G6 gate table; (3) the pre-cycle baseline (status/category distributions, entry count, boundary entry id+hash); (4) `E0` and `P0`; (5) the self-reported 8-row created-proposal list; (6) the absolute backup path; (7) any flags. Canonical Python file-write — no heredoc. Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-part1-2026-07-22.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — Lessons Agent (classify the REMAINING 7)

---

> **Before starting, read the Step 1 deposits and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2. You are the Forge Lessons Agent — same specialist, same working-location + absolute-DB-path rules as Step 1. **Open a fresh read-WRITE connection** (no `conn` carries over).
>
> **The ingest is DONE (Step 1). This step classifies ONLY the remainder.** Read `E0 = 163` and `P0 = 171` from Step 1's Output Receipt (do NOT re-run `MAX(id)`).
>
> **Scope:**
> - `knowledge/development/classifications-summary-part2-2026-07-22.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-22.md`
>
> **Precondition (report as a row):** `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id > 163` == **8** (Step 1's classifications are present). If not 8, HALT and report (Step 1 incomplete or a concurrent writer).
>
> **Derive the work list from `get_unclassified_entries` — it now returns exactly the 7 entries Step 1 did NOT classify** (it excludes any entry already holding a non-stale proposal). Expect **7** entries, all with `id` in 164–178. If it returns other than 7, or any id ≤ 163, HALT and reconcile (a ≤163 id means an older entry went `stale` — the 204 signature). Classify ALL of them, ascending `id`, under the **same classification contract as Step 1** (four required args; `reasoning` quotes `raw_content`; `target_layer`/`target_artifact` set; never carry CEO-Context claims into `reasoning`; STOP rather than write thin reasoning).
>
> **`conn.commit()` after each `insert_proposal`. Then git-commit the two `.md` deposits.**
>
> **Self-report:** print `SELECT id, entry_id, status, category FROM lesson_proposals WHERE entry_id > 163 ORDER BY id` — expect **15 rows now** (all batch entries classified, entry_ids 164–178, one proposal each). Also `SELECT COUNT(*) FROM lesson_proposals WHERE id > 171` — expect **15**. Put both in the Output Receipt. Confirm `get_unclassified_entries()` is now `[]` (or exactly a G6-approved deferral).
>
> **Deposit:** `knowledge/development/classifications-summary-part2-2026-07-22.md` (the 7 classifications' reasoning + any `ambiguous` by id) + `knowledge/development/dev-log-cycle-step-2-2026-07-22.md` with an Output Receipt: (1) the precondition count (8); (2) the 7-entry work list; (3) the full 15-row created-proposal list + the `id > 171` count (15); (4) `get_unclassified_entries()` now `[]`; (5) any flags. Canonical Python file-write — no heredoc. Commit both. `#### Prompt Feedback` in `### Ledger Updates`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-part2-2026-07-22.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — DEV (generate the report)

---

> **Before starting, read the Step 1 + Step 2 deposits and confirm both Output Receipts Complete; otherwise halt and report.** Post a short visible chat message. You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Same working-location + absolute-DB rules. **Open read-only:** `sqlite3.connect("file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro", uri=True)`.
>
> **Scope:**
> - `reports/lessons-report-2026-07-22.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-07-22.md`
>
> **Before generating: if `reports/lessons-report-2026-07-22.md` already exists, HALT** (`generate_lessons_report` overwrites unconditionally; a re-run would destroy the first run's only record). Verified at authoring: no 07-22 report exists.
>
> Run `generate_lessons_report(conn, "2026-07-22")`. **Two halt conditions (regressions):** (1) any `- **Route:**` line appears (all routes are NULL this cycle — plan-128 conditional render) → HALT; (2) any `Recently-implemented overlap:` line appears (plan 207 retired that detector) → HALT.
>
> `generate_lessons_report` resolves `output_dir="reports"` RELATIVE to cwd — run `pwd` before the call, capture the path the function RETURNS, state that absolute path in the dev log, and confirm the returned filename matches Scope (report the actual if it differs, do not rename). Print the report head (~80 lines).
>
> **Deposit:** the report + `knowledge/development/dev-log-cycle-step-3-2026-07-22.md` (Output Receipt: report length, proposals surfaced, route-line count, advisory-line count). Canonical Python file-write — no heredoc. Commit both. `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-22.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 4. Wait for CEO verdict.**

---
---

## STEP 4 — QA

---

> **Before starting, read the Step 1–3 deposits and confirm all Output Receipts Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 4 (QA). You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Same working-location + absolute-DB rules. **Verification + reporting only — no product-code changes; if a test fails, report it, do NOT fix it.** Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, `## Rule 20 — QA Self-Check Results` and a line `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner.
>
> **Evidence-source rule.** Every SQL/PRAGMA row states which DB it ran against (canonical = `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`). Deposit **RAW command output, never a summary of it** (memory `qa-evidence-raw-output`).
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-22.md`
>
> Verification table, one row per claim, each with a DB-source column (HALT on any FAIL):
> 1. **Full suite** — `python3 -m pytest src/ -v` to an explicit pass/fail, raw tail shown. **Compute the baseline yourself from `--collect-only` and reconcile against the most recent prior QA in `knowledge/qa/`** (the 2026-07-21 cycle QA recorded 55 — reconciliation only, do NOT carry it forward as the expected). Confirm 0 regressions.
> 2. `get_unclassified_entries(conn)` on canonical returns `[]` (or exactly a Step-1/2 `### Deferred entries (CEO-approved)` list — quote both heading and query output).
> 3. **Invariants** on canonical, scope = `WHERE entry_id > 163` (read `E0`=163 from Step 1's receipt; do NOT scope by `route IS NULL` — pre-existing NULL routes make that select the whole historical set). Over exactly that set (**expect 15 rows**): dangling 0, invalid category 0, invalid confidence 0, every one `route IS NULL`; and target fields SET — every non-`ambiguous` proposal has `target_layer IS NOT NULL` + `target_artifact IS NOT NULL`, and every `governance_rule` carries `target_layer='governance'` + `target_artifact='PLANNER_TEMPLATE.md'`. **A scoped count ≠ 15 is a FAIL** (<15 = a batch entry unclassified/dropped; >15 = a duplicate proposal). Cross-check `SELECT COUNT(*) FROM lesson_proposals WHERE id > 171` == 15. Reconcile against Steps 1+2 self-reported lists.
> 4. **The 204 fix held.** Read the pre-cycle baseline from Step 1's dev log (status/category distributions, entry count, entry-163 `content_hash`); if missing, HALT (unverifiable). Re-read from canonical now and diff: `stale` not grown, no proposal moved off a terminal status, entry id 163's hash unchanged. Report `updated_count` + `terminal_proposals_flagged` as Step 1 recorded.
> 5. **Report** exists, proposal counts match DB, zero `- **Route:**` lines, zero `Recently-implemented overlap:` lines, and `detect_recently_implemented_overlaps` is still absent from `src/` (plan 207 intact).
> 6. **No schema drift** — `.schema lesson_entries` / `.schema lesson_proposals` on canonical vs `src/db.py` DDL. Any delta is a FAIL.
> 7. **PLANNER_TEMPLATE.md UNCHANGED by this cycle.** ⚠️ `lessons-forge` is a submodule; `PLANNER_TEMPLATE.md` is tracked by the ROOT repo and does NOT exist in your worktree — a plain `git diff` from here passes VACUOUSLY (**this batch contains the lesson naming that exact failure**). Run against root: `git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md` and show the exit code (0 = pass; any diff = FAIL).
> 8. **Post-cycle DB counts** — entries total (**expect 178** = 163 + 15; the 163 includes orphan rows, NOT the file's 121 — do not flag 178 as anomalous), proposals by status + category, stated as actuals.
> 9. **Classification depth spot-check (context-saturation watch).** Scope as row 3 (`entry_id > 163`); take the **three highest proposal ids** (the last classified — most exposed) and for each confirm its `reasoning` genuinely quotes its entry's `raw_content`. **Use the EXTRACTION-FREE check** (a quoted-span regex FALSE-FAILs on nested quotes + markdown markers — measured on 247's data): (a) `canon(s)` = normalize curly→straight quotes, strip `*_`` ` characters, collapse whitespace, strip, lowercase; (b) longest common substring via `difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(...)`; (c) PASS if match **>= 40 chars**. **Report the measured longest-match length per proposal as a number** + PASS/FAIL + the proposal/entry ids. (On 247 all passed 97–300 chars; a result near 40 is itself worth a note.) This is the mechanical backstop for the split's saturation mitigation.
>
> If any row fails, report and HALT — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-07-22.md` — the table with DB-source column, raw full-suite tail, the Rule 20 banner + PASSED line, Output Receipt. Canonical Python file-write — no heredoc. Commit it. In `### Ledger Updates` include `#### Project Status` (one milestone paragraph: cycle 2026-07-22 complete — the 15-entry 07-21/07-22 batch ingested and classified across a split 8+7, report deposited, corpus integrity held; Gate 1 route disposition pending, incl. the Drafting-Cycle-refinements and halted-triage-method clusters) and `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-22.md`
>
> **STOP. Do NOT move the plan to Done until the CEO issues a verdict.**
