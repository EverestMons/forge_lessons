# forge_lessons — executable: cycle W=29 — ingest + classify the 25 pending corpus entries (five of 2026-09-01, twenty of 2026-09-02), the second forge cycle on the mini (NO routing; Gate 1 follows outside, non-author)

**Date:** 2026-09-02 | **Project:** forge_lessons | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (the forge suite — 80 tests — run into a per-plan evidence file under the forge's OWN venv; the pins + fresh-connection post-conditions are the instrument for the DB) | **Execution:** Step 1 (DEV — ingest) → Step 2 (Lessons Agent — classify) → Step 3 (QA — report + probes + suite) | **qa_steps:** 3 | **pause_for_verdict:** always | **known_failures:** 0 | **Priority:** 2

**auto_close:** false

**Slug:** `forge-cycle-w29-2026-09-02`

**Depends on:** the CEO's "Proceed as recommended" (2026-09-02: apply the lesson items — the 25 pending entries first, mechanically); `Done/executable-100007.md` (W=28, closed 2026-09-01 — the NEWEST same-class plan and the clone origin: the first forge cycle on the mini, ingest + classify, no routing); the forge venv created 2026-09-02 by `scripts/bootstrap.sh` (thread 79) — the suite interpreter is now the project's own; the lessons-forge DB lives ONLY on the mini. Walk register: `/Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w29-2026-09-02.md`.

## CEO Context

**Ingest + classify only — NO ROUTING.** Every proposal this plan mints leaves `route` NULL and `status` `proposed`. Gate 1 follows OUTSIDE this plan under the 459 non-author law (*the classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner*): the cold non-author is the MacBook Air's session, by message, with the flips applied on the mini where the DB lives — the pathway proven for W=28's packet on 2026-09-01.

⚠️ **The DB holds 12 LIVE `accepted` proposals (415, 417, 418, 419, 421, 422, 425, 430, 431, 434, 435, 437 — Gate 2 owed, thread 76).** W=28's DB was all-terminal; this one is not. This plan must not touch them: M5's triple-set identity over every pre-existing proposal is the guard, and M3's histogram after must show `accepted` still 12.

⚠️ **Nothing updates at ingest this time.** Rehearsed 2026-09-02 with the real functions on a scratch copy of the live DB: `{inserted: 25, updated: 0, unchanged: 376, stale_proposals_marked: 0, terminal_proposals_flagged: []}`. W=28 expected two rider updates; this batch has none — the plan halts on ANY deviation from the dict above, including an unexpected update.

⚠️ **Corpus freeze — this deposit IS the freeze.** No `LESSONS.md` append (no wrap 3b sweep) from deposit until this plan closes: M8 pins the register's sha and Step 3 re-asserts it. The Planner has told the CEO; the plan runs tonight and closes in under an hour.

**Author-conflict disclosure, date-keyed:** the twenty entries dated **2026-09-02** (ids 439–458 after ingest) were written by two mini Planner sessions — eighteen by 1663ee38 (filed from memory overnight) and TWO by the authoring session of THIS plan (a9cd0af4, today's wrap sweep). All twenty are marked `[AUTHOR-CONFLICT]` for Gate 1's read — the marker is disclosure; over-marking costs one read, under-marking hides a conflict. The five dated 2026-09-01 (ids 434–438) were written by the Air's session and another mini session, neither this plan's author.

**Every path in this plan is the MINI's:** the DB `/Users/marklehn/Developer/forge_lessons/lessons-forge.db` and the register `/Users/marklehn/Developer/eluvian-governance/LESSONS.md` are the two deliberate absolute operands (both outside your worktree; the DB is untracked by policy). `src/paths.py` resolves relative to the checkout it runs from and finds NO DB inside a worktree — pass these two paths explicitly, never rely on discovery.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared; every value MEASURED 2026-09-02 on the mini (read-only against the live DB; the ingest dict from a scratch-copy rehearsal of the real functions). The agent re-measures each pre-flight; mismatch → HALT with measured vs expected. Bind every id and heading as a PARAMETER — batch headings contain backticks, apostrophes and quotes.**

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | ingest result | — | EXACTLY `{inserted: 25, updated: 0, unchanged: 376, stale_proposals_marked: 0}` with `terminal_proposals_flagged` EMPTY | the dict returned by `ingest_lesson_entries`; ANY deviation → `ROLLBACK` and HALT listing the measured dict |
| M2 | unclassified | **0** → **25** post-ingest | **0** post-classify (the inversion) | `get_unclassified_entries(conn)` on a FRESH read-only connection |
| M3 | P0 proposals | **441** — accepted 12 / implemented 322 / reference 34 / rejected 41 / stale 3 / superseded 29; proposed 0 | 441 + `K`, `K` ≥ 25; every pre-existing count UNCHANGED (accepted still 12) | `SELECT status, COUNT(*) … GROUP BY status` |
| M4 | new-proposal band | — | route NULL AND status `proposed`, every one | `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND (route IS NOT NULL OR status <> 'proposed')` → **0** (MAXP = the captured pre-flight MAX(id), 441 expected — bound, never hard-coded) |
| M5 | pre-existing proposal set | the full `(id, status, route)` triple-set for ids <= MAXP, captured pre-flight (441 rows, twelve of them `accepted`) | **SET-IDENTICAL** post (a count cannot see a value move; this is the guard on the 12 accepted) | full triple-set select, compared as sets |
| M6 | E0 entries | **433**, MAXE=433 | **458**; new band **434–458** contiguous, `entry_date` ∈ {2026-09-01 (5), 2026-09-02 (20)} | `SELECT COUNT(*), MAX(id)`; `SELECT id, entry_date FROM lesson_entries WHERE id > :MAXE ORDER BY id` |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **20** — exactly the proposals whose entry has `entry_date='2026-09-02'`, NEVER an id range | BOTH directions, parameter-bound: (i) the set of `entry_id` over new proposals whose reasoning LIKE '%[AUTHOR-CONFLICT]%' == the set of `lesson_entries.id` with `entry_date='2026-09-02'` in the band (20 = 20); (ii) zero new proposals carry the marker whose entry is dated otherwise |
| M8 | the register | parser yields **401** entries; sha256-prefix `ee0432aeb88a3dfed4e8` | **byte-unchanged** — this plan READS the register, never writes it | `shasum -a 256 /Users/marklehn/Developer/eluvian-governance/LESSONS.md`; `len(parse_lessons_md(<path>))` |
| M9 | the 25 prior reports (destructible, tracked) | `ls reports/*.md` → 25 files; `shasum -a 256 reports/*.md \| shasum -a 256 \| cut -c1-16` → `8f61939d22de31e3` (measured at authoring over the 25 names; re-derive, state it) | **all 25 byte-identical** (the listing hash unchanged, computed over the SAME 25 names — exclude today's) | worktree-anchored; recovery `git -C "$(pwd)" checkout -- reports/<file>` |
| M10 | today's report | ABSENT | exists at `"$(pwd)/reports/lessons-report-2026-09-02.md"`, none of M9 | ls + shasum, worktree-anchored (⚠️ the 425 trap: NEVER the main-repo absolute path) |
| M11 | content hashes of pre-existing entries | the `(id, content_hash)` set for ids <= MAXE (433 rows) | SET-IDENTICAL, no exceptions (M1 says updated 0) | full select, compared as sets |
| M12 | stale proposals | **3** | **3, unchanged** | `SELECT COUNT(*) FROM lesson_proposals WHERE status='stale'` |
| M13 | the backup | ABSENT | `/Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-02-<HHMMSS>.db` exists, byte size == the DB's size measured immediately before the copy (1,847,296 at authoring — re-measure) | `ls -l` both; the house `pre-<slug>-<ts>.db` convention; untracked (`*.db` ignored) |
| M14 | the suite | `80 passed` at forge_lessons HEAD `5a0f71d` under the forge's OWN venv (measured from a scratch clone, the worktree's shape) | the same line, raw, in the evidence file | `/Users/marklehn/Developer/forge_lessons/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider` from the WORKTREE toplevel (the venv lives in the canonical checkout, gitignored — absolute path; `python3` on this machine has NO pytest) |
| M15 | DISPOSITION lines | — | **25** in Step 2's dev log | `/usr/bin/grep -cF 'DISPOSITION | entry=' <dev log>` |
| M17 | new-proposal ↔ entry pairing | — | every new proposal's `entry_id` ∈ 434–458, and NO entry in the band carries more than one new proposal | `SELECT entry_id, COUNT(*) FROM lesson_proposals WHERE id > :MAXP GROUP BY entry_id HAVING COUNT(*) > 1` → 0 rows; `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND entry_id NOT BETWEEN :MAXE_pre+1 AND :MAXE_post` → 0 (with M17, K == 25 exactly unless the agent reports why) |
| M16 | duplicates on this batch | **0** (Planner-measured: `detect_duplicates` over the 25 rehearsal ids 434–458 against `PLANNER_TEMPLATE.md` returned `[]`) | **0** new `category='duplicate'` proposals | the classifier never assigns `duplicate`; recorded, and asserted as 0 post |

## MUST-PRESERVE

- ⚠️ **BACKUP BEFORE ANY WRITE (M13).** No write to the live DB before the copy exists and its size matches.
- ⚠️ **TRANSACTION-WRAPPED, SENTINEL-GATED ingest:** `BEGIN`; call; PRINT the returned dict; compare to M1 EXACTLY; `COMMIT` only on match; any deviation → `ROLLBACK`, report the measured dict, END THE STEP as blocked — never commit a mismatched ingest, never retry.
- ⚠️ **`insert_proposal` and `ingest_lesson_entries` DO NOT COMMIT.** One commit per step, after all writes; every post-condition on a FRESH read-only connection.
- ⚠️ **`insert_proposal`'s six required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — a SEVENTH positional binds to `status`. Pass everything after `confidence` BY KEYWORD (`route=None`).**
- ⚠️ **The twelve `accepted` proposals are not this plan's.** No UPDATE, no route, no status change anywhere in `lesson_proposals` for ids <= MAXP — M5 proves it.
- ⚠️ **Worktree discipline:** your cwd IS the claimed tree — never `cd` to the main checkout. Report output is worktree-anchored (`"$(pwd)/reports"`). `git add` by explicit pathspec, never `-A`. Agents do not push. Do NOT rename the plan file.

## STEP 1 — DEV (ingest; ONE commit; fresh-connection posts)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. You are the Forge Developer.
>
> **Task A — worktree discipline + dispatch state + pre-flight.** `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK. **Dispatch-state probe** on this step's dev-log path (committed HEAD; working tree; `git log --all -- <path>`), each exit code captured, paired with a positive control against `knowledge/FORWARD.md`; any hit → RESUME (see below); all absent → FRESH. State the determination first. Pre-flight on a READ-ONLY connection to the live DB (`sqlite3.connect("file:/Users/marklehn/Developer/forge_lessons/lessons-forge.db?mode=ro", uri=True)`): M3 (the status histogram, 441 with accepted 12), M6 before (433, MAXE captured), M2 (0), M8 (401 parsed from the register path — with `sys.path.insert(0, os.getcwd())` at the worktree toplevel and `from src.lessons_forge import parse_lessons_md` — the PACKAGE import, the suite's own style; the sha), M12 (3); capture **MAXE** = `SELECT MAX(id) FROM lesson_entries` and **MAXP** = `SELECT MAX(id) FROM lesson_proposals` (⚠️ bind the MEASURED values — a COUNT and a MAX can diverge); capture M5's triple-set and M11's `(id, content_hash)` set to the dev log. Any mismatch → HALT with both values. **RESUME semantics:** M6 already 458 AND the dev log's M1 dict present → the ingest landed on a prior run: do NOT re-ingest; re-run the posts read-only, record `RESUME (ingest already committed)`, reconstruct the lost in-run values honestly and LABEL them `RECONSTRUCTED (post-commit re-entry)`, never presented as the run's own output; E0 strictly between 433 and 458 → HALT (a single-transaction ingest cannot produce a partial band; a subset is positive evidence of a foreign writer).
>
> **Task B — backup (M13).** `ls -l` the live DB; `cp /Users/marklehn/Developer/forge_lessons/lessons-forge.db /Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-02-$(date +%H%M%S).db`; `ls -l` the copy; sizes must be equal — record both lines.
>
> **Task C — ONE python script (writing connection; NO commit until the dict matches).** `sys.path.insert(0, os.getcwd())` at the worktree toplevel; `from src.lessons_forge import parse_lessons_md, ingest_lesson_entries, get_unclassified_entries` (⚠️ `lessons_forge.py` imports `src.paths` inside two functions, so a bare `from lessons_forge import …` with `src/` on the path breaks the moment one of them runs); (1) `entries = parse_lessons_md("/Users/marklehn/Developer/eluvian-governance/LESSONS.md")` → assert `len(entries) == 401`; (2) open the live DB read-write (absolute path), `BEGIN`; (3) `result = ingest_lesson_entries(conn, entries)`; PRINT `result` verbatim; compare to **M1 EXACTLY** — the four counts AND `terminal_proposals_flagged == []`; on match `COMMIT`; on ANY deviation `ROLLBACK`, print `INGEST MISMATCH`, and end the step as blocked; (4) POSTS on a FRESH read-only connection: M6 after (458; the band `SELECT id, entry_date, substr(source_heading,1,72) FROM lesson_entries WHERE id > :MAXE ORDER BY id` — 25 rows, contiguous 434–458, five dated 2026-09-01 then twenty dated 2026-09-02), M2 (25), M3 (441, histogram unchanged, accepted 12), M5 (triple-set SET-IDENTICAL), M11 (SET-IDENTICAL, no exceptions), M12 (3), M8 (sha unchanged).
>
> **Task D — dev log + commit.** `knowledge/development/dev-log-ingest-w29-2026-09-02.md`: the dispatch-state determination, the pre-flight raws (M5 and M11 captures included), the M13 lines, the M1 dict verbatim, the 25-row band listing, the post raws. Commit at the WORKTREE toplevel: `git add knowledge/development/dev-log-ingest-w29-2026-09-02.md && git commit -m "[<id from your plan filename>] forge-cycle-w29(forge-cycle-w29-2026-09-02): ingest 25 (433->458; updated 0; proposals 441 unchanged, accepted 12 untouched)" -- knowledge/development/dev-log-ingest-w29-2026-09-02.md && git rev-parse HEAD` — the DB and the backup are untracked by policy and are NOT added.
>
> **Deposits:**
> - `knowledge/development/dev-log-ingest-w29-2026-09-02.md`
>
> **Scope:**
> - `knowledge/development/dev-log-ingest-w29-2026-09-02.md`

## STEP 2 — Lessons Agent: classify the 25 (no report, no routing)

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and YOU RUN IN A WORKTREE** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/forge_lessons/lessons-forge.db`. Open no OTHER database: a 0-byte `.db` anywhere is a decoy returning false absences, and any `.db` outside this repo is a different system's.
>
> **⚠️ NO ROUTING.** `route` stays **NULL** at insert and `status` stays at its default `proposed`. Gate 1 belongs to a non-author. **No ingest, no UPDATE, no delete.** Bind every entry id and heading as a PARAMETER; never interpolate a heading into a `sqlite3` CLI string.
>
> **Dispatch-state probe** on this step's dev-log path (three-place, positive control against `knowledge/FORWARD.md`). RESUME semantics (single-commit design): work list == 25 → a prior dispatch died pre-commit, proceed as FRESH and say so; work list == 0 → classification landed — do NOT re-insert; record `RESUME (classification already committed)`, re-run the posts read-only, deposit, stop; **work list strictly between 0 and 25 → HALT** (a single-commit classify cannot leave a partial band).
>
> **Pre-flight (read-only, raw output for each):** `get_unclassified_entries(conn)` == exactly ids 434–458 (25, contiguous) · `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id IN (<the 25 ids, parameter-bound>)` == **0** · **M3 before** (441, histogram, accepted 12) · capture **MAXP** (441 expected — bound, never hard-coded) · **M5** (capture the triple-set — the post-condition compares SET-IDENTITY) · **M6** (458).
>
> **Classify.** For each of the 25: parameter-bound `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`; apply the ADR-002 six-value taxonomy per the specialist file (never `duplicate` — M16); then, with `sys.path.insert(0, os.getcwd())` at the worktree toplevel and `from src.lessons_forge import insert_proposal, get_unclassified_entries` (the PACKAGE import), `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, target_layer=<layer>, target_artifact=<artifact or None>, route=None)` — everything after `confidence` BY KEYWORD. For each entry whose `entry_date` is `2026-09-02`, the reasoning text begins with `[AUTHOR-CONFLICT] ` (M7 — by DATE, never by id range). One line per entry in the dev log, exactly this form:
> ```
> DISPOSITION | entry=<id> | proposal=<id> | category=<c> | remedy: <one clause> | markers: <those that apply, or NONE>
> ```
> `markers: NONE` is legitimate and expected for the five 2026-09-01 entries. Post-condition M15: exactly 25 such lines in the dev log.
>
> **THE COMMIT.** ⚠️⚠️ `insert_proposal` DOES NOT COMMIT. Issue exactly ONE `conn.commit()` after all 25 inserts.
>
> **Post-conditions — ON A FRESH READ-ONLY CONNECTION:** M2 (the inversion — `[]`), M3 after (441 + K, record K; accepted still 12), M4 (0), M17 (0 rows / 0), M5 (SET-IDENTICAL), M6 (458), M7 (both directions, 20 = 20), M12 (3), M16 (0 new `duplicate`), M8 (sha unchanged).
>
> **Deposits.** `knowledge/development/dev-log-classify-w29-2026-09-02.md` (the pre-flight raws, the 25 DISPOSITION lines, the post raws) and `knowledge/development/evidence-classify-w29-2026-09-02.txt` (the raw SQL outputs of every post-condition). Commit at the WORKTREE toplevel: `git add knowledge/development/dev-log-classify-w29-2026-09-02.md knowledge/development/evidence-classify-w29-2026-09-02.txt && git commit -m "[<id>] forge-cycle-w29: classify 25 (proposals 441->466, route NULL, status proposed; 20 AUTHOR-CONFLICT by date)" -- knowledge/development/dev-log-classify-w29-2026-09-02.md knowledge/development/evidence-classify-w29-2026-09-02.txt`.
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-w29-2026-09-02.md`
> - `knowledge/development/evidence-classify-w29-2026-09-02.txt`
>
> **Scope:**
> - `knowledge/development/dev-log-classify-w29-2026-09-02.md`
> - `knowledge/development/evidence-classify-w29-2026-09-02.txt`

## STEP 3 — QA (report + probes + suite)

> **Step 2's Receipt status must be `Status: Complete`.** Dispatch-state probe first (three-place, positive control). **FIRST — post a short visible chat message (1–2 sentences).** You are the Forge QA agent.
>
> **MANDATORY — the Rule 20 self-check is gate-enforced** (`rule_20_self_check` greps the QA receipt for the byte-exact banner `Rule 20 — QA Self-Check Results` and the line `PASSED — SELF-CHECK PASSED`). The verification table does NOT satisfy it. Read the canonical block at the path the dispatcher's mandate names (this machine's `RULE_20_SELF_CHECK_BLOCK.md`; quote the path you were handed), copy its canonical Python block, fill the four placeholders below, run it, and paste its stdout into the receipt. Before finishing, `/usr/bin/grep -c 'Rule 20 — QA Self-Check Results' <receipt>` must print 1.
> - `plan_slug`: `forge-cycle-w29-2026-09-02`
> - `qa_report_path`: `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md`
> - `evidence_dir`: `"$(pwd)/knowledge/qa/evidence/forge-cycle-w29-2026-09-02"` (the QA's OWN worktree — never a main-tree path)
> - `required_evidence_files`: `["probes-raw.txt", "full-suite-forge-cycle-w29.txt"]`
>
> **Item 1 — the report.** `cd "$(git rev-parse --show-toplevel)"`; python (package import): `generate_lessons_report(conn, "2026-09-02", output_dir=os.path.join(os.getcwd(), "reports"))` — `cycle_date` is the PLAN's date (do NOT recompute from `date`); `output_dir` worktree-anchored (⚠️ the 425 trap — NEVER the main-repo path). M9's listing hash BEFORE and AFTER over the same 25 names (recovery `git -C "$(pwd)" checkout -- reports/<file>`); M10 (exists, none of M9). Quote the report's rendering of the new 25-proposal batch in the receipt — that is what Gate 1 reads. Commit: `git add reports/lessons-report-2026-09-02.md && git commit -m "[<id>] forge-cycle-w29: cycle report" -- reports/lessons-report-2026-09-02.md`.
> **Item 2 — DB probes on a FRESH read-only connection**, raw into `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/probes-raw.txt`: M2, M3 (accepted 12), M4, M17, M5 (re-selected, SET-IDENTICAL vs Step 2's capture), M6, M7 (both directions), M11 (vs Step 1's capture), M12, M16, M8's sha; M15 counted over Step 2's dev log.
> **Item 3 — the suite (M14).** From the worktree toplevel: `/Users/marklehn/Developer/forge_lessons/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider > knowledge/qa/evidence/forge-cycle-w29-2026-09-02/full-suite-forge-cycle-w29.txt 2>&1; echo "exit=$?" >> knowledge/qa/evidence/forge-cycle-w29-2026-09-02/full-suite-forge-cycle-w29.txt` — the file must carry the raw `80 passed` summary line and `exit=0`; a failure count > 0 is a Critical finding, not a note.
> **Item 4 — hygiene + receipt** `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md`: numstats (Step 1 commit 1 file; Step 2 commit 2 files; report commit 1 file); toplevel; `git reflog -n 5` → 0 amends; the per-item verification table `| Deliverable | Expected | Status (✅/❌) | Evidence |` citing the evidence files by path — ⚠️ the `rule_22_verification` gate substring-matches hedging vocabulary in positive-status rows: status cells carry the glyph only, and the word `proposed` (a real column value) is the term for the new band, never the p-word that means un-routed; the Rule 20 block's stdout. Commit the evidence dir by explicit pathspec: `git add knowledge/qa/evidence/forge-cycle-w29-2026-09-02/ && git commit -m "[<id>] forge-cycle-w29: QA evidence — probes, suite, receipt" -- knowledge/qa/evidence/forge-cycle-w29-2026-09-02/`.
>
> **Deposits:**
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md`
> - `reports/lessons-report-2026-09-02.md`
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/full-suite-forge-cycle-w29.txt`
>
> **Scope:**
> - `reports/lessons-report-2026-09-02.md`
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/full-suite-forge-cycle-w29.txt`
> - `knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md`

---

## Drafting Cycle

**Tier:** T1 — T-2 (production-data mutation: the canonical corpus DB) caps at T1; T-8 clone of `Done/executable-100007.md` (W=28) with every pin re-measured on this machine and the ingest rehearsed with the real functions. No panel (no direction-class finding at walk 1).

**Walk register:** /Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w29-2026-09-02.md

**Walk 0 (context pin, measured):** the corpus parsed (401) and its sha; the DB read-only (433 / 441, the histogram with its twelve live `accepted`, MAXE, MAXP, the stale count); the ingest REHEARSED with the real functions on a scratch copy (the exact dict, the band, the dates, the 20-by-date marker set); `detect_duplicates` over the rehearsal band; the reports listing hash over 25 names; the suite from a scratch clone under the forge's own venv; the `insert_proposal` signature read at source; the three-pass clone-diff against 100007 and its register; the consumer dry-run (§2.0) on the register's walk-0 line — class assigner `shop-infra`, extractor per step with the receipt first.

**Direction verdict (after walk 1): PROCEED.** Tested: the premise (25 entries new by content hash, none updating — rehearsed, not assumed; the twelve accepted proposals guarded by set identity), the mechanism (the parent's transaction-gated ingest and one-commit classify, every pin re-pinned), the scope (no routing; Gate 1 outside by the Air's session; Gate 2 tranche one drafted beside this plan, not inside it).

**Walks:**
- Weak spots:          w1 1 folded — instruction 1 / record 0 (M9's probe carried an authoring placeholder where the measured listing hash belongs — stated)
- Destruction:         w1 dry — the backup precedes every write; one transaction gated on the exact dict; the twelve accepted rows guarded by set identity; the reports guarded by the listing hash with a named recovery
- Vulnerabilities:     w1 dry — absolute operands for the DB and the register; the package import named at first use; every id and heading parameter-bound; the seventh-positional trap named; the report path worktree-anchored
- Integration-record:  w1 dry — the manifest is the emitter's, spliced at the freeze; the class the assigner measured; the Deposits block lists the receipt first (the gate's first-`.md` rule)
- ACID:                w1 dry — one commit per step; the DB and the backup untracked by policy; RESUME arms per step distinguish a pre-commit death from a landed step
- **Walk 1 total: 1 finding, 1 folded — instruction 1 / record 0; 0 of 1 fold-introduced.**
- Weak spots:          w2 dry — instruction 0 / record 0 — the folded pin re-read; every M-value re-checked against the register's measurements; the Cycle Log covered
- Destruction:         w2 dry — instruction 0 / record 0 — unchanged
- Vulnerabilities:     w2 dry — instruction 0 / record 0 — unchanged
- Integration-record:  w2 dry — instruction 0 / record 0 — `propagation_check` clean; the corpus freeze stated in-plan and told to the CEO
- ACID:                w2 dry — instruction 0 / record 0 — unchanged
- **Walk 2 total: 0 findings — instruction 0 / record 0, ALL FIVE LENSES DRY.** Instruction series 1 → 0.

**Conformance (§5):** first run at walk 0 (on v0) and re-run after walk 1's fold and at the freeze: `plan_lint` exit 0 / 0 FAIL at the faithful mirror — expected WARN set (o2)×7 (worktree-relative deposits, the parent's form); `cycle_check` BAR_MET; `fold_check` baseline re-saved at each intended change with a note; `propagation_check` exit 0.

**Closing:** ✅ **BAR MET — walk 2 dry (all five lenses) after walk 1's one fold; T1, no panel owed, none convened.** Substrate present (the register's rows entered from captured output and committed at the freeze; `fold_check` baseline). The closing-record re-read (§2.7) ran against this block, the register and the emitted manifest at the freeze.

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/eluvian-governance/LESSONS.md, /Users/marklehn/Developer/forge_lessons/lessons-forge.db, /Users/marklehn/Developer/forge_lessons/src/lessons_forge.py, /Users/marklehn/Developer/forge_lessons/agents/FORGE_LESSONS_AGENT.md, /Users/marklehn/Developer/forge_lessons/knowledge/decisions/Done/executable-100007.md
writes: lessons-forge.db, pre-ingest-2026-09-02-HHMMSS.db, knowledge/development/dev-log-ingest-w29-2026-09-02.md, knowledge/development/dev-log-classify-w29-2026-09-02.md, knowledge/development/evidence-classify-w29-2026-09-02.txt, reports/lessons-report-2026-09-02.md, knowledge/qa/evidence/forge-cycle-w29-2026-09-02/probes-raw.txt, knowledge/qa/evidence/forge-cycle-w29-2026-09-02/full-suite-forge-cycle-w29.txt, knowledge/qa/evidence/forge-cycle-w29-2026-09-02/qa-receipt.md
open_forks: Gate 1 outside this plan — the Air's session as the cold non-author, the twenty 2026-09-02 proposals carrying AUTHOR-CONFLICT for the CEO's own read; Gate 2 for whatever Gate 1 accepts; the corpus freeze window (no LESSONS.md append until close)
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=PASS
coherence: 2/2 walks have register rows

Rule 20 banner (byte-exact, produced by RUNNING the canonical block — never hand-authored):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```
