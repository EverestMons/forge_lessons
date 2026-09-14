# forge_lessons — executable: cycle W=30 — ingest + classify the 122 pending corpus entries (dated 2026-09-02 to 2026-09-12) in three batches, the third forge cycle on the mini (NO routing; Gate 1 follows outside, non-author)

**Date:** 2026-09-12 | **Project:** forge_lessons | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (the forge suite — 80 tests — run into a per-plan evidence file under the forge's OWN venv; the pins + fresh-connection post-conditions are the instrument for the DB) | **Execution:** Step 1 (DEV — ingest) → Step 2 (Lessons Agent — classify batch A) → Step 3 (Lessons Agent — classify batch B) → Step 4 (Lessons Agent — classify batch C) → Step 5 (QA — report + probes + suite) | **qa_steps:** 5 | **pause_for_verdict:** always | **known_failures:** 0 | **Priority:** 2

**auto_close:** false

**Post-close:** no restart — no code changes. Four Planner acts after the close, in order: (1) Gate 1 — a fresh session that authored none of these entries reads `reports/lessons-report-2026-09-12.md`, the three classify dev logs and the three flagged entries (98, 106, 368) and writes a routing packet in W=29's form (governance `gate1-packet-2026-09-02.md`), each proposal checked against the live doctrine and the shipped code, so a lesson applied since it was written is routed `reference` with its site named; (2) the packet's flips applied on the mini, after a `pre-g1w30-<ts>.db` backup made with the backup API; (3) `scripts/project_status_markers.py --db /Users/marklehn/Developer/forge_lessons/lessons-forge.db --lessons /Users/marklehn/Developer/eluvian-governance/LESSONS.md --apply`, which gives the 122 `[status: pending]` markers their proposals' statuses — a register write, so it waits for this plan's close, when the corpus freeze ends; (4) Gate 2 for what Gate 1 accepts, beside W=29's twenty-three.

**Slug:** `forge-cycle-w30-2026-09-12`

**Depends on:** the CEO's "Let's run the lessons forge now" (2026-09-12, after ten days without a cycle — W=29 ran 2026-09-02); `Done/executable-100020.md` (W=29 — the NEWEST same-class plan and the clone origin: ingest + classify, no routing, closed 2026-09-02); the forge venv (thread 79); the lessons-forge DB lives ONLY on the mini. Walk register: `/Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w30-2026-09-12.md`.

## CEO Context

**Ingest + classify only — NO ROUTING.** Every proposal this plan mints leaves `route` NULL and `status` `proposed`. Gate 1 follows OUTSIDE this plan under the 459 non-author law (*the classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner*): a fresh session that authored none of these entries — W=29's Gate 1 was a fresh Claude Code session on the mini (22366c52) — with the flips applied on the mini, where the DB lives. Gate 1's method already checks each proposal against the live doctrine and the shipped code, which is where a lesson applied since it was written is recorded (`reference`, the site named).

**Three batches.** 122 entries is five times W=29's 25 (175,896 characters of lesson text), so the classification runs as three Lessons Agent steps of 41, 41 and 40 entries, each committing its own range; a step that dies re-runs only its range.

⚠️ **The DB holds 23 LIVE `accepted` proposals (442–456, 458–464, 466 — W=29's Gate 1 codify set, Gate 2 owed).** This plan must not touch them: M5's triple-set identity over every pre-existing proposal is the guard, and M3's histogram after must show `accepted` still 23.

⚠️ **Three pre-existing entries UPDATE at ingest, and their proposals are flagged, not staled.** Entries 98 and 106 gained inline riders on 2026-09-08 (governance `1f242128`, the CEO's ruling on thread 191) and entry 368 on 2026-09-07 (`5e0088ac`); their proposals are terminal (103 and 111 `implemented`, 376 `rejected`), so the ingest records them in `terminal_proposals_flagged` and leaves their status alone — and no classification step will read the new rider text. The QA step names the three for Gate 1; 368's rider sits under a REJECTED proposal. Rehearsed 2026-09-12 with the real functions on a backup-API copy of the live DB: `{inserted: 122, updated: 3, unchanged: 398, stale_proposals_marked: 0, terminal_proposals_flagged: [{entry_id: 98, proposal_id: 103, status: implemented}, {entry_id: 106, proposal_id: 111, status: implemented}, {entry_id: 368, proposal_id: 376, status: rejected}]}`. The plan halts on ANY deviation from that dict.

⚠️ **Corpus freeze — this deposit IS the freeze.** No `LESSONS.md` append (no wrap 3b sweep) from deposit until this plan closes: M8 pins the register's sha and Step 5 re-asserts it.

**Author-conflict disclosure, date-keyed:** the 108 entries dated **2026-09-04 or later** were written chiefly by the authoring session of THIS plan (d04ebd33, from its first wrap on 2026-09-04 at 13:46), with a few by other sessions (42ce7e32 and 3b6ea354 on 2026-09-04, 5f165f0d on 2026-09-06) — all 108 are marked `[AUTHOR-CONFLICT]` for Gate 1's read; over-marking costs one read, under-marking hides a conflict. The 14 dated 2026-09-02 and 2026-09-03 were written by other sessions and carry no marker.

**Every path in this plan is the MINI's:** the DB `/Users/marklehn/Developer/forge_lessons/lessons-forge.db` and the register `/Users/marklehn/Developer/eluvian-governance/LESSONS.md` are the two deliberate absolute operands (both outside your worktree; the DB is untracked by policy). `src/paths.py` resolves relative to the checkout it runs from and finds NO DB inside a worktree — pass these two paths explicitly, never rely on discovery.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared; every value MEASURED 2026-09-12 on the mini (read-only against the live DB; the ingest dict from a backup-API-copy rehearsal of the real functions). The agent re-measures each pre-flight; mismatch → HALT with measured vs expected. Bind every id and heading as a PARAMETER — batch headings contain backticks, apostrophes and quotes.**

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | ingest result | — | EXACTLY `{inserted: 122, updated: 3, unchanged: 398, stale_proposals_marked: 0}` with `terminal_proposals_flagged` EXACTLY the three `{entry_id: 98, proposal_id: 103, status: implemented}`, `{entry_id: 106, proposal_id: 111, status: implemented}`, `{entry_id: 368, proposal_id: 376, status: rejected}` | the dict returned by `ingest_lesson_entries`; ANY deviation → `ROLLBACK` and HALT listing the measured dict |
| M2 | unclassified | **0** → **122** post-ingest | **81** after batch A, **40** after batch B, **0** after batch C (the inversion) | `get_unclassified_entries(conn)` on a FRESH read-only connection |
| M3 | P0 proposals | **466** — accepted 23 / implemented 334 / reference 35 / rejected 42 / stale 3 / superseded 29; proposed 0 | 466 + `K`, `K` ≥ 122; every pre-existing count UNCHANGED (accepted still 23) | `SELECT status, COUNT(*) … GROUP BY status` |
| M4 | new-proposal band | — | route NULL AND status `proposed`, every one | `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND (route IS NOT NULL OR status <> 'proposed')` → **0** (MAXP = the captured pre-flight MAX(id), 466 expected — bound, never hard-coded) |
| M5 | pre-existing proposal set | the full `(id, status, route)` triple-set for ids <= MAXP, captured pre-flight (466 rows, twenty-three of them `accepted`) | **SET-IDENTICAL** post, after every step (a count cannot see a value move; this is the guard on the 23 accepted and on the three flagged) | full triple-set select, compared as sets |
| M6 | E0 entries | **458**, MAXE=458 | **580**; new band **459–580** contiguous; `entry_date` counts 2026-09-02 (8), 2026-09-03 (6), 2026-09-04 (14), 2026-09-05 (3), 2026-09-06 (11), 2026-09-07 (12), 2026-09-08 (20), 2026-09-09 (15), 2026-09-10 (11), 2026-09-11 (13), 2026-09-12 (9) | `SELECT COUNT(*), MAX(id)`; `SELECT id, entry_date FROM lesson_entries WHERE id > :MAXE ORDER BY id` |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **108** — exactly the proposals whose entry has `entry_date >= '2026-09-04'`, NEVER an id range | BOTH directions, parameter-bound: (i) the set of `entry_id` over new proposals whose reasoning LIKE '%[AUTHOR-CONFLICT]%' == the set of band entry ids with `entry_date >= '2026-09-04'` (108 = 108); (ii) zero new proposals carry the marker whose entry is dated earlier |
| M8 | the register | parser yields **523** entries; sha256-prefix `0c99d2073e5072f83058` | **byte-unchanged** — this plan READS the register, never writes it | `shasum -a 256 /Users/marklehn/Developer/eluvian-governance/LESSONS.md`; `len(parse_lessons_md(<path>))` |
| M9 | the 26 prior reports (destructible, tracked) | 26 files; the listing hash `1fb34ee52650fd5c` — the exact command sits in Step 5 Item 1 | **all 26 byte-identical** (the listing hash unchanged, computed over the SAME 26 names — exclude today's) | worktree-anchored; recovery `git -C "$(pwd)" checkout -- reports/<file>` |
| M10 | today's report | ABSENT | exists at `"$(pwd)/reports/lessons-report-2026-09-12.md"`, none of M9 | ls + shasum, worktree-anchored (⚠️ the 425 trap: NEVER the main-repo absolute path) |
| M11 | content hashes of pre-existing entries | the `(id, content_hash)` set for ids <= MAXE (458 rows) | SET-IDENTICAL EXCEPT exactly entries 98, 106 and 368, whose new hashes equal the parser's for their headings (M1's three updates) | full select, compared as sets, the three exceptions named |
| M12 | stale proposals | **3** | **3, unchanged** | `SELECT COUNT(*) FROM lesson_proposals WHERE status='stale'` |
| M13 | the backup | ABSENT | `/Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-12-<HHMMSS>.db` made with the SQLite backup API (the DB runs in WAL mode — a plain `cp` of the main file can miss pages still in the `-wal`); the copy's `PRAGMA integrity_check` reads `ok` and its `lesson_entries` and `lesson_proposals` counts equal the live DB's (458 and 466) | the backup call, then the checks on the copy; the house `pre-<slug>-<ts>.db` convention; untracked (`*.db` ignored) |
| M14 | the suite | `80 passed` at forge_lessons HEAD `dacccbb` under the forge's OWN venv (measured from a scratch archive, the worktree's shape) | the same line, raw, in the evidence file | `/Users/marklehn/Developer/forge_lessons/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider` from the WORKTREE toplevel (the venv lives in the canonical checkout, gitignored — absolute path) |
| M15 | DISPOSITION lines | — | **41**, **41** and **40** in the three classify dev logs (122 in all) | the lines that carry the `DISPOSITION` form with its `entry=` field in each classify dev log — the exact command sits in each classify step's post-conditions, outside this table |
| M16 | duplicates on this batch | **0** (Planner-measured: `detect_duplicates` over the 122 rehearsal ids against `PLANNER_TEMPLATE.md`, and against `DRAFTING_CYCLE.md`, returned `[]`) | **0** new `category='duplicate'` proposals | the classifier never assigns `duplicate`; recorded, and asserted as 0 post |
| M17 | new-proposal ↔ entry pairing | — | every new proposal's `entry_id` ∈ 459–580, and NO entry in the band carries more than one new proposal | `SELECT entry_id, COUNT(*) FROM lesson_proposals WHERE id > :MAXP GROUP BY entry_id HAVING COUNT(*) > 1` → 0 rows; `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND entry_id NOT BETWEEN :MAXE_pre+1 AND :MAXE_post` → 0 (with M17, K == 122 exactly unless the agent reports why) |
| M18 | the batch ranges | — | batch A = entry ids MAXE+1 to MAXE+41 (459–499), batch B = MAXE+42 to MAXE+82 (500–540), batch C = MAXE+83 to MAXE+122 (541–580) — bound from the MAXE Step 1 measured, never hard-coded | each classify step reads the bound from Step 1's dev log and states it before its first insert |

## MUST-PRESERVE

- ⚠️ **BACKUP BEFORE ANY WRITE (M13).** No write to the live DB before the backup-API copy exists and its checks pass.
- ⚠️ **TRANSACTION-WRAPPED, SENTINEL-GATED ingest:** `BEGIN`; call; PRINT the returned dict; compare to M1 EXACTLY — the four counts and the three flags; `COMMIT` only on match; any deviation → `ROLLBACK`, report the measured dict, END THE STEP as blocked — never commit a mismatched ingest, never retry.
- ⚠️ **`insert_proposal` and `ingest_lesson_entries` DO NOT COMMIT.** One commit per step, after all writes; every post-condition on a FRESH read-only connection.
- ⚠️ **`insert_proposal`'s six required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — a SEVENTH positional binds to `status`. Pass everything after `confidence` BY KEYWORD (`route=None`).**
- ⚠️ **The twenty-three `accepted` proposals and the three flagged proposals are not this plan's.** No UPDATE, no route, no status change anywhere in `lesson_proposals` for ids <= MAXP — M5 proves it after every step.
- ⚠️ **A classify step inserts only for its own batch range (M18).** An entry outside the range is never read for insertion; an entry in the range that already has a non-stale proposal is a RESUME signal, never a second insert.
- ⚠️ **Worktree discipline:** your cwd IS the claimed tree — never `cd` to the main checkout. Report output is worktree-anchored (`"$(pwd)/reports"`). `git add` by explicit pathspec, never `-A`. Agents do not push. Do NOT rename the plan file.

## STEP 1 — DEV (ingest; ONE commit; fresh-connection posts)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. You are the Forge Developer.
>
> **Task A — worktree discipline + dispatch state + pre-flight.** `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK. **Dispatch-state probe** on this step's dev-log path (committed HEAD; working tree; `git log --all -- <path>`), each exit code captured, paired with a positive control against `knowledge/FORWARD.md`; any hit → RESUME (see below); all absent → FRESH. State the determination first. Pre-flight on a READ-ONLY connection to the live DB (`sqlite3.connect("file:/Users/marklehn/Developer/forge_lessons/lessons-forge.db?mode=ro", uri=True)`): M3 (the status histogram, 466 with accepted 23), M6 before (458, MAXE captured), M2 (0), M8 (523 parsed from the register path — with `sys.path.insert(0, os.getcwd())` at the worktree toplevel and `from src.lessons_forge import parse_lessons_md` — the PACKAGE import, the suite's own style; the sha), M12 (3); capture **MAXE** = `SELECT MAX(id) FROM lesson_entries` and **MAXP** = `SELECT MAX(id) FROM lesson_proposals` (⚠️ bind the MEASURED values — a COUNT and a MAX can diverge) and write both, with M18's three ranges computed from MAXE, as the dev log's first lines; capture M5's triple-set and M11's `(id, content_hash)` set to the dev log. Any mismatch → HALT with both values. **RESUME semantics:** M6 already 580 AND the dev log's M1 dict present → the ingest landed on a prior run: do NOT re-ingest; re-run the posts read-only, record `RESUME (ingest already committed)`, reconstruct the lost in-run values honestly and LABEL them `RECONSTRUCTED (post-commit re-entry)`, never presented as the run's own output; E0 strictly between 458 and 580 → HALT (a single-transaction ingest cannot produce a partial band; a subset is positive evidence of a foreign writer).
>
> **Task B — backup (M13).** In one python invocation: `src = sqlite3.connect("file:/Users/marklehn/Developer/forge_lessons/lessons-forge.db?mode=ro", uri=True)`; `dst = sqlite3.connect("/Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-12-" + time.strftime("%H%M%S") + ".db")`; `src.backup(dst)`; then on `dst`: `PRAGMA integrity_check` (must print `ok`) and the two counts (458 and 466); close both; `ls -l` the copy. Record every line.
>
> **Task C — ONE python script (writing connection; NO commit until the dict matches).** `sys.path.insert(0, os.getcwd())` at the worktree toplevel; `from src.lessons_forge import parse_lessons_md, ingest_lesson_entries, get_unclassified_entries` (⚠️ `lessons_forge.py` imports `src.paths` inside two functions, so a bare `from lessons_forge import …` with `src/` on the path breaks the moment one of them runs); (1) `entries = parse_lessons_md("/Users/marklehn/Developer/eluvian-governance/LESSONS.md")` → assert `len(entries) == 523`; (2) open the live DB read-write (absolute path), `BEGIN`; (3) `result = ingest_lesson_entries(conn, entries)`; PRINT `result` verbatim; compare to **M1 EXACTLY** — the four counts AND `terminal_proposals_flagged` equal to the three dicts, in any order; on match `COMMIT`; on ANY deviation `ROLLBACK`, print `INGEST MISMATCH`, and end the step as blocked; (4) POSTS on a FRESH read-only connection: M6 after (580; the band `SELECT id, entry_date, substr(source_heading,1,72) FROM lesson_entries WHERE id > :MAXE ORDER BY id` — 122 rows, contiguous 459–580, dated as M6 states), M2 (122), M3 (466, histogram unchanged, accepted 23), M5 (triple-set SET-IDENTICAL), M11 (SET-IDENTICAL except exactly 98, 106 and 368, each now equal to the parser's hash for its heading), M12 (3), M8 (sha unchanged).
>
> **Task D — dev log + commit.** `knowledge/development/dev-log-ingest-w30-2026-09-12.md`: MAXE, MAXP and M18's ranges first; the dispatch-state determination, the pre-flight raws (M5 and M11 captures included), the M13 lines, the M1 dict verbatim, the 122-row band listing, the post raws. Commit at the WORKTREE toplevel: `git add knowledge/development/dev-log-ingest-w30-2026-09-12.md && git commit -m "[<id from your plan filename>] forge-cycle-w30(forge-cycle-w30-2026-09-12): ingest 122 (458->580; updated 3, flagged 3; proposals 466 unchanged, accepted 23 untouched)" -- knowledge/development/dev-log-ingest-w30-2026-09-12.md && git rev-parse HEAD` — the DB and the backup are untracked by policy and are NOT added.
>
> **Deposits:**
> - `knowledge/development/dev-log-ingest-w30-2026-09-12.md`
>
> **Scope:**
> - `knowledge/development/dev-log-ingest-w30-2026-09-12.md`

## STEP 2 — Lessons Agent: classify batch A (no report, no routing)

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. Then `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK; every command below runs from there.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and YOU RUN IN A WORKTREE** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/forge_lessons/lessons-forge.db`. Open no OTHER database: a 0-byte `.db` anywhere is a decoy returning false absences, and any `.db` outside this repo is a different system's.
>
> **⚠️ NO ROUTING.** `route` stays **NULL** at insert and `status` stays at its default `proposed`. Gate 1 belongs to a non-author. **No ingest, no UPDATE, no delete.** Bind every entry id and heading as a PARAMETER; never interpolate a heading into a `sqlite3` CLI string.
>
> **Your range:** batch A — read MAXE from the first lines of `knowledge/development/dev-log-ingest-w30-2026-09-12.md` and state the range `MAXE+1` to `MAXE+41` (459–499 expected) before any insert (M18).
>
> **Dispatch-state probe** on this step's dev-log path (three-place, positive control against `knowledge/FORWARD.md`). RESUME semantics (single-commit design): the work list's members in your range == all 41 → proceed as FRESH (a prior dispatch, if any, died pre-commit — say so); == none → classification landed — do NOT re-insert; record `RESUME (classification already committed)`, re-run the posts read-only, deposit, stop; **strictly between → HALT** (a single-commit classify cannot leave a partial range).
>
> **Pre-flight (read-only, raw output for each):** `get_unclassified_entries(conn)` == exactly the 122 ids of the band (M2) · `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id BETWEEN :lo AND :hi` == **0** for your range · **M3 before** (466, histogram, accepted 23) · capture **MAXP_A** = `SELECT MAX(id) FROM lesson_proposals` (466 expected — bound, never hard-coded) · **M5** (compare the triple-set to Step 1's capture — SET-IDENTICAL) · **M6** (580).
>
> **Classify.** For each entry in your range: parameter-bound `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`; apply the ADR-002 six-value taxonomy per the specialist file (never `duplicate` — M16); then, with `sys.path.insert(0, os.getcwd())` at the worktree toplevel and `from src.lessons_forge import insert_proposal, get_unclassified_entries` (the PACKAGE import), `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, target_layer=<layer>, target_artifact=<artifact or None>, route=None)` — everything after `confidence` BY KEYWORD. For each entry whose `entry_date` is `2026-09-04` or later, the reasoning text begins with `[AUTHOR-CONFLICT] ` (M7 — by DATE, never by id range). An entry whose heading reads `RIDER on …` names its parent entry's heading in the reasoning. One line per entry in the dev log, exactly this form:
> ```
> DISPOSITION | entry=<id> | proposal=<id> | category=<c> | remedy: <one clause> | markers: <those that apply, or NONE>
> ```
>
> **THE COMMIT.** ⚠️⚠️ `insert_proposal` DOES NOT COMMIT. Issue exactly ONE `conn.commit()` after the range's 41 inserts.
>
> **Post-conditions — ON A FRESH READ-ONLY CONNECTION:** M2 (81 remain — exactly the band minus your range), M3 (466 + 41; accepted still 23), M4 (0), M17 (0 rows / 0), M5 (SET-IDENTICAL), M6 (580), M7 for your range (both directions), M12 (3), M16 (0 new `duplicate`), M8 (sha unchanged), M15 — `grep -c -F 'DISPOSITION | entry=' knowledge/development/dev-log-classify-w30a-2026-09-12.md` prints 41.
>
> **Deposits.** `knowledge/development/dev-log-classify-w30a-2026-09-12.md` (the range, the pre-flight raws, the 41 DISPOSITION lines, the post raws) and `knowledge/development/evidence-classify-w30a-2026-09-12.txt` (the raw SQL outputs of every post-condition). Commit at the WORKTREE toplevel: `git add knowledge/development/dev-log-classify-w30a-2026-09-12.md knowledge/development/evidence-classify-w30a-2026-09-12.txt && git commit -m "[<id>] forge-cycle-w30: classify batch A (41; route NULL, status proposed)" -- knowledge/development/dev-log-classify-w30a-2026-09-12.md knowledge/development/evidence-classify-w30a-2026-09-12.txt`.
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-w30a-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30a-2026-09-12.txt`
>
> **Scope:**
> - `knowledge/development/dev-log-classify-w30a-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30a-2026-09-12.txt`

## STEP 3 — Lessons Agent: classify batch B (no report, no routing)

> **Step 2's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. Then `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK; every command below runs from there. Step 2's text binds this step in full — the specialist file, the absolute DB path, NO ROUTING, the parameter binding, the classification call, the `[AUTHOR-CONFLICT] ` rule by date, the RIDER rule, the DISPOSITION line form, the single commit, the RESUME semantics — with these differences only:
>
> **Your range:** batch B — `MAXE+42` to `MAXE+82` (500–540 expected), read from Step 1's dev log and stated before any insert. **Pre-flight:** the work list == exactly the 81 ids of batches B and C; zero proposals on your range; M3 (466 + 41, accepted 23); **MAXP_B** captured; M5 SET-IDENTICAL; M6 (580). **Post-conditions:** M2 (40 remain — exactly batch C), M3 (466 + 82; accepted still 23), M4, M17, M5, M6, M7 for your range, M12, M16, M8, M15 — `grep -c -F 'DISPOSITION | entry=' knowledge/development/dev-log-classify-w30b-2026-09-12.md` prints 41.
>
> **Deposits.** `knowledge/development/dev-log-classify-w30b-2026-09-12.md` and `knowledge/development/evidence-classify-w30b-2026-09-12.txt`, committed at the WORKTREE toplevel: `git add knowledge/development/dev-log-classify-w30b-2026-09-12.md knowledge/development/evidence-classify-w30b-2026-09-12.txt && git commit -m "[<id>] forge-cycle-w30: classify batch B (41; route NULL, status proposed)" -- knowledge/development/dev-log-classify-w30b-2026-09-12.md knowledge/development/evidence-classify-w30b-2026-09-12.txt`.
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-w30b-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30b-2026-09-12.txt`
>
> **Scope:**
> - `knowledge/development/dev-log-classify-w30b-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30b-2026-09-12.txt`

## STEP 4 — Lessons Agent: classify batch C (no report, no routing)

> **Step 3's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. Then `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK; every command below runs from there. Step 2's text binds this step in full, with these differences only:
>
> **Your range:** batch C — `MAXE+83` to `MAXE+122` (541–580 expected), read from Step 1's dev log and stated before any insert. **Pre-flight:** the work list == exactly the 40 ids of batch C; zero proposals on your range; M3 (466 + 82, accepted 23); **MAXP_C** captured; M5 SET-IDENTICAL; M6 (580). **Post-conditions:** M2 (0 — the inversion, `[]`), M3 (466 + 122; accepted still 23), M4, M17, M5, M6, M7 over the WHOLE band (108 = 108, both directions), M12, M16, M8, M15 — `grep -c -F 'DISPOSITION | entry=' knowledge/development/dev-log-classify-w30c-2026-09-12.md` prints 40.
>
> **Deposits.** `knowledge/development/dev-log-classify-w30c-2026-09-12.md` and `knowledge/development/evidence-classify-w30c-2026-09-12.txt`, committed at the WORKTREE toplevel: `git add knowledge/development/dev-log-classify-w30c-2026-09-12.md knowledge/development/evidence-classify-w30c-2026-09-12.txt && git commit -m "[<id>] forge-cycle-w30: classify batch C (40; route NULL, status proposed; 108 AUTHOR-CONFLICT by date over the band)" -- knowledge/development/dev-log-classify-w30c-2026-09-12.md knowledge/development/evidence-classify-w30c-2026-09-12.txt`.
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-w30c-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30c-2026-09-12.txt`
>
> **Scope:**
> - `knowledge/development/dev-log-classify-w30c-2026-09-12.md`
> - `knowledge/development/evidence-classify-w30c-2026-09-12.txt`

## STEP 5 — QA (report + probes + suite)

> **Step 4's Receipt status must be `Status: Complete`.** Dispatch-state probe first (three-place, positive control). **FIRST — post a short visible chat message (1–2 sentences).** You are the Forge QA agent.
>
> **MANDATORY — the Rule 20 self-check is gate-enforced** (`rule_20_self_check` greps the QA receipt for the byte-exact banner `Rule 20 — QA Self-Check Results` and the line `PASSED — SELF-CHECK PASSED`). The verification table does NOT satisfy it. Read the canonical block at `/Users/marklehn/Developer/eluvian-governance/RULE_20_SELF_CHECK_BLOCK.md`, copy its canonical Python block, fill the four placeholders below, run it, and paste its stdout into the receipt. Before finishing, `grep -c -F 'Rule 20 — QA Self-Check Results' <receipt>` must print 1.
> - `plan_slug`: `forge-cycle-w30-2026-09-12`
> - `qa_report_path`: `"$(pwd)/knowledge/qa/evidence/forge-cycle-w30-2026-09-12/qa-receipt.md"` (absolute, the QA's OWN worktree)
> - `evidence_dir`: `"$(pwd)/knowledge/qa/evidence/forge-cycle-w30-2026-09-12/"` (the QA's OWN worktree — never a main-tree path)
> - `required_evidence_files`: `["probes-raw.txt", "full-suite-forge-cycle-w30.txt"]`
>
> **Item 1 — the report.** `cd "$(git rev-parse --show-toplevel)"`; python (package import): `generate_lessons_report(conn, "2026-09-12", output_dir=os.path.join(os.getcwd(), "reports"))` — `cycle_date` is the PLAN's date (do NOT recompute from `date`); `output_dir` worktree-anchored (⚠️ the 425 trap — NEVER the main-repo path). M9's listing hash BEFORE and AFTER over the same 26 names, from the worktree toplevel — `find reports -maxdepth 1 -name '*.md' ! -name 'lessons-report-2026-09-12.md' | sort | xargs shasum -a 256 | shasum -a 256 | cut -c1-16` prints `1fb34ee52650fd5c` both times (recovery `git -C "$(pwd)" checkout -- reports/<file>`); M10 (exists, none of M9). Quote the report's rendering of the new 122-proposal batch in the receipt, and name the three flagged entries (98, 106, 368 — their proposals and statuses from M1) beside it — that is what Gate 1 reads. Commit: `git add reports/lessons-report-2026-09-12.md && git commit -m "[<id>] forge-cycle-w30: cycle report" -- reports/lessons-report-2026-09-12.md`.
> **Item 2 — DB probes on a FRESH read-only connection**, raw into `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/probes-raw.txt`: M2, M3 (accepted 23), M4, M17, M5 (re-selected, SET-IDENTICAL vs Step 1's capture), M6, M7 (both directions, over the band), M11 (vs Step 1's capture, the three exceptions named), M12, M16, M8's sha; M15 counted over the three classify dev logs.
> **Item 3 — the suite (M14).** From the worktree toplevel: `/Users/marklehn/Developer/forge_lessons/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider > knowledge/qa/evidence/forge-cycle-w30-2026-09-12/full-suite-forge-cycle-w30.txt 2>&1; echo "exit=$?" >> knowledge/qa/evidence/forge-cycle-w30-2026-09-12/full-suite-forge-cycle-w30.txt` — the file must carry the raw `80 passed` summary line and `exit=0`; a failure count > 0 is a Critical finding, not a note.
> **Item 4 — hygiene + receipt** `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/qa-receipt.md`: numstats (Step 1 commit 1 file; each classify commit 2 files; the report commit 1 file); toplevel; `git reflog -n 8` → 0 amends; the per-item verification table `| Deliverable | Expected | Status (✅/❌) | Evidence |` citing the evidence files by path — ⚠️ the `rule_22_verification` gate substring-matches hedging vocabulary in positive-status rows: status cells carry the glyph only, and the word `proposed` (a real column value) is the term for the new band, never the p-word that means un-routed; the Rule 20 block's stdout. Commit the evidence dir by explicit pathspec: `git add knowledge/qa/evidence/forge-cycle-w30-2026-09-12/ && git commit -m "[<id>] forge-cycle-w30: QA evidence — probes, suite, receipt" -- knowledge/qa/evidence/forge-cycle-w30-2026-09-12/`.
>
> **Deposits:**
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/qa-receipt.md`
> - `reports/lessons-report-2026-09-12.md`
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/full-suite-forge-cycle-w30.txt`
>
> **Scope:**
> - `reports/lessons-report-2026-09-12.md`
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/full-suite-forge-cycle-w30.txt`
> - `knowledge/qa/evidence/forge-cycle-w30-2026-09-12/qa-receipt.md`

---

## Drafting Cycle

**Tier:** **T1** — T-2 (production-data mutation: the canonical corpus DB) caps at T1; T-8 clone of `Done/executable-100020.md` (W=29) with every pin re-measured on this machine, the ingest rehearsed with the real functions, and the classification split into three batch steps. **Walk register:** /Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w30-2026-09-12.md
**Walks:** walk 0 pinned (M1–M18 measured on forge_lessons `dacccbb`; the ingest rehearsed on a backup-API copy; clone-diff against `Done/executable-100020.md` run: FACTS, ARTEFACTS, STRUCTURE; the standing rules and the parent's register diffed; the depositor and the pre-check dry-run); `fold_check --save-baseline` ARMED on v0 before any fold; re-saved after every intended edit; every lens commit through `/Users/marklehn/Developer/bellows/scripts/lens_commit.py`, the tool run bare, its exit read; no lens or walk number in any `--desc`; `lens_order_check` after every lens commit, and before the receipt on a copy of the draft in a scratch project-shaped repository.

- Weak spots:          w1 2 folded — instruction 2 / record 0; w2 dry
- Destruction:          w1 dry; w2 dry
- Vulnerabilities:      w1 dry; w2 dry
- Integration-record:   w1 1 folded — instruction 0 / record 1; w2 dry
- ACID:                 w1 dry; w2 dry
**Closing:** WARM close after walk 2 — BAR MET (T1), forge cycle W=30. Two walks, findings by class — walk 1: 3 (instruction 2 / record 1), walk 2: 0; the manifest's `yields` counts the instruction class alone, 2, 0. Walk 1 gave M15 and M9 as the exact commands they are measured with (M9's reproduced `1fb34ee52650fd5c` in the canonical checkout at the fold) and named the four acts after the close; walk 2 dry across all five lenses. Dry pass: walk 2 meets §2's bar — instruction 0 / record 0. Origin (diagnostic): 0 of 3 fold-introduced. The ingest was rehearsed at walk 0 on a backup-API copy of the live DB (`inserted 122, updated 3, unchanged 398, stale 0`, three terminal flags); propagation_check's flags are restated values, ordering and arithmetic none.

## Cycle Manifest
tier: T1
target: lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/eluvian-governance/LESSONS.md, /Users/marklehn/Developer/forge_lessons/lessons-forge.db, /Users/marklehn/Developer/forge_lessons/src/lessons_forge.py, /Users/marklehn/Developer/forge_lessons/agents/FORGE_LESSONS_AGENT.md, /Users/marklehn/Developer/forge_lessons/knowledge/decisions/Done/executable-100020.md
writes: lessons-forge.db, pre-ingest-2026-09-12-HHMMSS.db, knowledge/development/dev-log-ingest-w30-2026-09-12.md, knowledge/development/dev-log-classify-w30a-2026-09-12.md, knowledge/development/evidence-classify-w30a-2026-09-12.txt, knowledge/development/dev-log-classify-w30b-2026-09-12.md, knowledge/development/evidence-classify-w30b-2026-09-12.txt, knowledge/development/dev-log-classify-w30c-2026-09-12.md, knowledge/development/evidence-classify-w30c-2026-09-12.txt, reports/lessons-report-2026-09-12.md, knowledge/qa/evidence/forge-cycle-w30-2026-09-12/probes-raw.txt, knowledge/qa/evidence/forge-cycle-w30-2026-09-12/full-suite-forge-cycle-w30.txt, knowledge/qa/evidence/forge-cycle-w30-2026-09-12/qa-receipt.md
open_forks: 1. Gate 1 outside this plan — a fresh non-author session, the 108 date-marked proposals carrying AUTHOR-CONFLICT for its read and the CEO's; 2. Gate 2 for whatever Gate 1 accepts, beside W=29's twenty-three still owed; 3. the three flagged entries (98, 106, 368) — an inline rider on a terminal entry is never re-classified by the forge's design, and 368's sits under a rejected proposal; 4. the corpus freeze window (no LESSONS.md append until close)
walks: 2
yields: 2, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=VACUOUS, propagation_check=DIVERGENT:134
coherence: 2/2 body walks named in the register (3 register rows; walk-token match, NOT row coverage)
fold_baseline: governance/knowledge/decisions/drafts/.executable-forge-cycle-w30.md.foldcheck.json
