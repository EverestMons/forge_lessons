# Executable: Gate 1 route assignment — proposals 223–273 (44 accepted→codify, 7 parked→shape-decision)

**Type:** Executable
**Project:** lessons-forge
**Depends on:** the classified batch from executable-311 (Done — 51 proposals, all `governance_rule`, confidence `high`); the CEO routing session of 2026-08-08 (packet `gate1-packet-2026-08-08.md` at the shop root — PROVENANCE ONLY, this plan is self-contained and no step reads it).
**Created:** 2026-08-08
**Author:** Planner
**dispatch_mode:** bellows
**pause_for_verdict:** always
**qa_steps:** [2]
**Priority:** 10
**cycle_tier:** T1
**Test Scope:** targeted (the 311 header convention; Rule 21 justification carried in Step 2 — the single-module suite where targeted = full)

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** Bellows mints the id from `id_sequence` at claim. **Re-read `id_sequence` at deposit** (three in-window drifts this week: 310→311, 321, 323).

---

## Why this exists — the routing IS the deliverable; the decisions are already made

Gate 1 for the 311 batch: the CEO routed all 51 proposals on 2026-08-08. This plan writes those dispositions to the canonical corpus DB in one transaction and proves the write touched exactly the intended rows. **The decision payload is carried INLINE below (the two id lists + the encoding); the packet is provenance, not an input any step reads** — a plan self-contained beats a cross-tree read (277's V1).

**The encoding, from measured precedent (rows 161/169 are the standing CEO-parked form):**
- **44 items → `status='accepted'`, `route='codify'`** — the Gate-2-consumable state.
- **7 items (the shape-decision cluster A) → `status='reference'`, `route='backlog'`** — the CEO-parked form; the shape-decision session re-opens them BY THIS LIST, and their `reference` status is reversible by that session's own plan.
- **All 51: `status_updated_by='ceo'`, `status_updated_at=<transaction time>`** — the dispositions are the CEO's; this plan is the pen, not the decider.

**THE TWO LISTS (the payload — byte-authoritative over any prose):**
- **CODIFY-44:** 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 245, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272, 273
- **PARK-7 (cluster A):** 233, 238, 246, 247, 258, 259, 271
- Arithmetic anchor: 44 + 7 = 51 = the full contiguous id range 223–273. ⚠️ **252, 260, 261 route CODIFY deliberately** — each has a codifiable half (252's closing-line ordering; 260's §3 phrasing rule; 261's three (D)-residues), and their shape/bellows halves are carried by the packet's record, not by these rows.

**What this plan does NOT do:** no LESSONS.md touch (the freeze rule is not in play — routing writes only the proposals table); no doctrine edit (Gate-2 plans own those); no FORWARD emission (the four Rule-46 bellows halves and the two census candidates ride the session wrap, per the packet).

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---
---

## STEP 1 — DEV (the routing transaction)

> **FIRST — post a short visible chat message (1–2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename this plan file. Read your specialist file. ⚠️⚠️ **ADDRESSING CONTRACT (Destruction lens, the 317 masked-state hazard): your cwd is the WORKTREE — all file deposits are worktree-relative so they enter `files_changed` and merge. The DB is UNTRACKED and therefore DOES NOT EXIST in the worktree: every `sqlite3` command addresses the CANONICAL absolute path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — never a relative `lessons-forge.db`, which would open a fresh empty file in the worktree and every count would read 0. A deposit written to the canonical tree instead of the worktree passes deposit_exists while dodging files_changed — the 317-measured masked state; do not mix the two directions up.** The table is `lesson_proposals`.
>
> **Task A0 — PIN THE PRE-STATE; the write is licensed by it and ONLY it.**
> 1. `sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';"` — **must print exactly 51. Any other number → HALT** (a concurrent cycle or session touched the batch; do not improvise a reconciliation).
> 2. `sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*), MIN(id), MAX(id) FROM lesson_proposals WHERE status='proposed';"` — **must print exactly `51|223|273`: with ids unique (PK), 51 rows spanning 223–273 inclusive IS the contiguity proof, order-independent (lens 1: GROUP_CONCAT ordering is idiom, not spec).** Any other triple → **HALT.** Print the GROUP_CONCAT id list too, as display for the dev log, never as the gate.
> 3. **Dump the FULL disposition table to the pre-image:** `sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT id, status, COALESCE(route,'-'), COALESCE(status_updated_by,'-') FROM lesson_proposals ORDER BY id;" > knowledge/development/gate1-pre-dump-2026-08-08.txt` (the redirect target is worktree-relative — the deposit direction) — **this file is the untouched-population proof's left side; deposit it.**
>
> **Task B — ONE transaction, two UPDATEs, in-transaction verification before COMMIT.** Canonical Python (`sqlite3` module, `BEGIN IMMEDIATE`), NO heredoc:
> - `UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_by='ceo', status_updated_at=<ISO-now> WHERE id IN (<CODIFY-44 list verbatim>) AND status='proposed';` — **rowcount must be exactly 44 or ROLLBACK+HALT.**
> - `UPDATE lesson_proposals SET status='reference', route='backlog', status_updated_by='ceo', status_updated_at=<ISO-now> WHERE id IN (233,238,246,247,258,259,271) AND status='proposed';` — **rowcount must be exactly 7 or ROLLBACK+HALT.**
> - In-transaction posts, before COMMIT: `proposed` count now 0; `accepted/codify` in 223–273 = 44; `reference/backlog` in 223–273 = 7. **Any mismatch → ROLLBACK + HALT with the numbers.**
> - **Lock behaviour, stated (lens 3; journal mode is WAL, verified live):** the script sets `PRAGMA busy_timeout=5000` before `BEGIN IMMEDIATE`; a persistent `OperationalError: database is locked` → **HALT with the error verbatim** — an exception before COMMIT rolls back and leaves the DB untouched, so a lock failure is a clean retry-later state, never a half-write.
> - ⚠️ **The `AND status='proposed'` guard on both UPDATEs is load-bearing:** it makes the transaction idempotence-safe (a redo after a crash-between-commit-and-log re-matches 0 rows and HALTs loudly instead of silently double-stamping timestamps). **It is ALSO the A0-to-transaction window guard (a1, stated not accidental): if a writer slips between A0's pin and BEGIN IMMEDIATE, the rowcounts diverge from 44/7 and the transaction rolls back — the pin is advisory, the rowcounts are the gate.**
> - **The dev log RECORDS the transaction timestamp value verbatim (a1)** — it is QA item 1(d)'s comparator; a window test without its recorded reference is unrunnable.
> - ⚠️⚠️ **THE TWO LISTS ARE IMMUTABLE INPUTS (Destruction lens): a rowcount mismatch is NEVER resolved by editing a list — not by dropping an id to make 44 match, not by adding one. The only response to any mismatch is ROLLBACK + HALT with the numbers. The script embeds both lists verbatim from this plan, and the dev log pastes the script so the verdict reader can diff them against the plan's payload.**
> - The Python script opens the CANONICAL absolute DB path (the addressing contract above).
>
> **Task C — post-image + the untouched-population proof (a count is not a value guard):**
> 1. Dump the same full table to `knowledge/development/gate1-post-dump-2026-08-08.txt` (same SELECT, same ORDER BY).
> 2. `diff` pre vs post: **the diff must show EXACTLY the 51 rows for ids 223–273 changing as specified — as PAIRED old/new lines (~102 changed lines plus markers, unified form) — and ZERO lines for any other id (lens 1: "51 lines" would misread the paired form as a failure).** Paste the RAW diff in the dev log. **A single foreign line → the wrong-write proof → HALT and report; do NOT attempt a compensating write.**
>
> **No test run in this step — deliberate, stated (lens 1, from 311's measured precedent):** this plan changes NO code; its writes are DB rows and markdown. The repo's suite is the single module `src/test_lessons_forge.py`, and Step 2 runs it whole. A DEV test run here would measure nothing this step touched.
>
> **Scope:**
> - `knowledge/development/gate1-routing-dev-log-2026-08-08.md`
> - `knowledge/development/gate1-pre-dump-2026-08-08.txt`
> - `knowledge/development/gate1-post-dump-2026-08-08.txt`
>
> ⚠️ **`lessons-forge.db` is deliberately ABSENT from Scope and from the commit: the DB is UNTRACKED by shop policy (plan 30, commit `dabb301` un-tracked it) — `git add`ing it would re-track it AGAINST that policy (lens 1, probe-confirmed). The DB mutation's evidence IS the dump pair; the dumps commit, the DB never does.**
>
> **Deposit the dev log** with: both dumps' paths + line counts, the transaction script text, both rowcounts, the in-transaction post numbers, **the transaction timestamp value verbatim (QA 1(d)'s comparator — c1: it was mandated above but missing from this content list, the producing-step handshake class of proposal 225, sitting in the very batch this plan routes)**, the RAW pre/post diff. **Commit with the pathspec on the COMMIT naming exactly the three Scope files; post-commit assertion `git show --name-only --format= HEAD` printing exactly those three.** `#### Prompt Feedback` in `### Ledger Updates`.
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

**Deposits:**
- `lessons-forge/knowledge/development/gate1-routing-dev-log-2026-08-08.md`
- `lessons-forge/knowledge/development/gate1-pre-dump-2026-08-08.txt`
- `lessons-forge/knowledge/development/gate1-post-dump-2026-08-08.txt`

---
---

## STEP 2 — QA

> **Task Q0 — RE-PIN (the DB is untracked, so the pin is CONTENT, not git — lens 1):** (1) `git -C /Users/marklehn/Developer/GitHub/lessons-forge log -1 --oneline -- knowledge/development/gate1-routing-dev-log-2026-08-08.md knowledge/development/gate1-pre-dump-2026-08-08.txt knowledge/development/gate1-post-dump-2026-08-08.txt` — the newest commit touching any evidence file must be Step 1's; foreign → **HALT.** (2) `sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';"` — **must print 0** (the post-state; a nonzero here means a verdict-window write re-opened the batch → HALT).

1. **Read-only re-verification, from the DB not the dev log** (`sqlite3 -readonly`, canonical absolute path per the addressing contract): (a) `proposed` = 0; (b) `SELECT id FROM lesson_proposals WHERE status='accepted' AND route='codify' AND id BETWEEN 223 AND 273 ORDER BY id;` — **line-per-id output (ORDER BY is deterministic by spec — lens 3: the GROUP_CONCAT form carried the same ordering idiom lens 1 evicted from A0, the fold-sweep class) diffed against the CODIFY-44 list written as 44 lines**; (c) the same form for reference/backlog, diffed against the seven lines 233, 238, 246, 247, 258, 259, 271; (d) every one of the 51 rows carries `status_updated_by='ceo'` and a `status_updated_at` matching the transaction time the dev log records — **a window test against the recorded value, NEVER a calendar-day test (Destruction lens: a dispatch crossing midnight, or the UTC/local seam, false-HALTs a same-day check — the resume-glob lesson's cousin)**; (e) **the CONSUMER check (lens 4): the canonical work-list semantics hold post-routing — run the `get_unclassified_entries` equivalent (entries whose only proposals are `stale`) and confirm NO entry in the routed batch's entry set re-queued: `accepted` and `reference` proposals both keep their entries dispositioned per the helper's own docstring. Paste query + raw output.** **Paste each query WITH its raw output.**
2. **Untouched-population proof, independently re-derived — with the verdict-window split (a1: the DEV→QA gate is an arbitrary wall-clock window over a LIVE shared DB and the parallel terminal is demonstrably active):** re-dump the full table (same SELECT/ORDER BY) → `knowledge/qa/gate1-qa-dump-2026-08-08.txt`; `diff` against the Step-1 PRE-dump and PARTITION the differing lines: (i) **within ids 223–273:** must be EXACTLY the 51 specified changes — anything else is a foreign write to the routed batch → **HALT**; (ii) **outside 223–273** (new proposal rows from a concurrent ingest, other-id status advances): **concurrent activity — NAME each line in the report, verify none touches 223–273, and do NOT halt on it** (the bookend doctrine: name the delta, never force reconciliation, never punish legitimate parallel work). **This re-derives Task C from the QA side — do not reuse Step 1's diff.**
3. **The suite:** `python3 -m pytest src/ --tb=short -q 2>&1 | cat` → `knowledge/qa/full-suite.txt` (RAW, whole output incl. the summary line — never a summary). **Rule 21 justification, re-verified not inherited (311's form): the repo's suite is the single module `src/test_lessons_forge.py`, so this run is simultaneously targeted and full — the sixth data point of the CEO-tracked single-module precedent; report the collected count against 311's measured 55, actual over expected.**
4. **QA Receipt with the canonical Rule 20 self-check block**, one verification row per item above.
   - `required_evidence_files`: `[gate1-qa-dump-2026-08-08.txt, full-suite.txt]`
   - ⚠️ Deposit both BEFORE running the block — it `sys.exit(1)`s if any is missing or empty.
   - ⚠️⚠️ **Include the block's literal stdout. The banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must appear BYTE-EXACT (em-dash U+2014). If it prints FAILED, HALT.**

> **Scope:**
> - `knowledge/qa/gate1-routing-qa-report-2026-08-08.md`
> - `knowledge/qa/gate1-qa-dump-2026-08-08.txt`
> - `knowledge/qa/full-suite.txt`

**Deposits:**
- `lessons-forge/knowledge/qa/gate1-routing-qa-report-2026-08-08.md`
- `lessons-forge/knowledge/qa/gate1-qa-dump-2026-08-08.txt`
- `lessons-forge/knowledge/qa/full-suite.txt`

### Output Receipt (Step 2, terminal)

Close with `### Status` (**Complete**), `### Deposits`, `### Ledger Updates` with **`#### Forward Register`: the word NONE** (the four Rule-46 bellows halves + two census candidates ride the session wrap by CEO-approved packet, NOT this channel) and **`#### Prompt Feedback`**.

**STOP. Terminal step. Wait for CEO verdict.**

---

## Method + boundaries

- **The tooling's `set_proposal_route` helper (`src/lessons_forge.py:255`) is deliberately BYPASSED, stated not silent (lens 4):** it sets `route` ONLY — no status, no `status_updated_by`/`_at` — so 51 helper calls plus separate status writes would fracture the atomicity the single two-UPDATE transaction provides. The transaction writes the same enum values the helper validates (`codify`/`backlog` ∈ `_VALID_ROUTES`).
- **The DB is the CANONICAL corpus store (T-2) and it is UNTRACKED by shop policy (plan 30, `dabb301`)** — no step stages or commits it; its mutation is evidenced by the committed dump pair and re-derived at QA. The write surface is exactly two UPDATE statements over 51 pinned rows; **no INSERT, no DELETE, no schema touch, no `lesson_entries` touch.** If anything beyond the two lists needs writing, HALT — the routing decisions are the CEO's and this plan carries all of them.
- **No re-dating: deposit basenames embed 2026-08-08; a later run keeps the authored date** (the resume-glob UTC lesson; the deposit gate matches basenames).
- **Lint the FINAL text before the cp to `knowledge/decisions/`** — the daemon claims within seconds.
- **HALT ROUTING — inputs each step reads; missing/unreadable → HALT:** Step 1: `lessons-forge.db`, the specialist file. Step 2: `lessons-forge.db`, the Step-1 dev log + PRE-dump (the diff's left side), `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`.
- **Half-complete state, stated:** the transaction is atomic — it lands whole or rolls back; a death between COMMIT and the dev-log commit leaves a correct DB with missing evidence, and the redo's `AND status='proposed'` guards then match 0 rows and HALT loudly (the recovery is a fresh plan reading the actual state, never a blind re-run). **The mid-QA member too (a1): a HALT between evidence deposit and receipt leaves evidence without a receipt — redo-safe via the no-re-date same-basename overwrite.** Acceptable and stated.
- ⚠️ **`grep -F` mandatory for literals** (ugrep shim). The shell is zsh — no bare globs.
- ⚠️ **Agents run `git add` and `git commit` only. No push.**
- Where a step cannot be completed as written, **HALT and report** — never substitute.

---

## Drafting Cycle

**This section is a RECORD, not instructions.** Gate-matching strings are described here, never quoted.

**Tier:** T1 — triggers fired: T-2 (production-data mutation — the canonical proposals table, 51 of 273 rows; the every-row clause does NOT fire, so T2 is not demanded). T-8 does not fire (route-assignment executables are a shipped class — the 2026-07-07 Gate 1 precedent; encoding from measured rows 161/169). T-6 does not fire (no doctrine/gate/template edit — Gate-2 plans own those).

**Expected lint:** EARNED at the §5 pass at close (post-c2, 2026-08-08): **8 PASS · 0 WARN · exit 0**, plus shipped o1's informational accounting line running clean on this plan itself (candidates=9, excluded=6 — the plan's own Deposits/Scope entries, correctly excluded — fired=0). The mid-cycle closing-fold WARN cleared EARNED when aC's dry re-read reached the ACID line. Re-checked after every edit (§3); a divergence at deposit is a defect to resolve, not to ship.

**Walks:** 1 (four lenses + a1 apart), plus confirming c1 (four-lens) and aC (ACID confirming, apart) — each phase its own turn under CEO direction, per-phase committed. ⚠️ This header has now lagged TWICE in this cycle (at a1, and again at aC still stopping at a1 after c1 ran) — proposal 258's class, fifth occurrence across four artifacts, each caught only by the apart-ACID record read.

- Weak spots:          w1 4 folded, all probe-confirmed (1.2 the DB is UNTRACKED by plan-30 policy — removed from Scope/Deposits/commit, Q0 re-based to content pins + evidence-file git pin, the git-log-on-DB check would have FALSE-HALTED every run and the commit would have RE-TRACKED against policy; 1.1 the targeted `-k` collected ZERO tests — DEV test run dropped with stated reason, QA runs `pytest src/` with 311's measured single-module Rule-21 justification, sixth data point; 1.1 contiguity proof re-based to COUNT/MIN/MAX arithmetic, order-independent; 1.1 diff expectation stated as paired lines ~102).
- Destruction:         w1 3 folded (2.1 MATERIAL: the addressing contract — the untracked DB does not exist in the worktree, so relative sqlite opens an EMPTY file and every count reads 0, while canonical-tree deposits dodge files_changed = the 317 masked state; cwd=worktree for deposits, canonical ABSOLUTE path for every DB command, both directions stated; 2.2 the two lists made IMMUTABLE — a rowcount mismatch is never resolved by editing a list, script pasted for payload diff; 2.2 QA's same-day timestamp test → window-vs-recorded-value, the UTC-midnight false-HALT).
- Vulnerabilities:     w1 2 folded + 1 verified-clean (3.1 WAL confirmed live + busy_timeout/lock-HALT semantics stated — an exception before COMMIT is a clean rollback, never a half-write; 3.2 QA's byte-for-byte list checks still carried the GROUP_CONCAT ordering idiom lens 1 evicted from A0 — the fold-sweep class — replaced with ORDER BY line-output diffs; 3.3 the suite is PROBE-CONFIRMED isolated — :memory: DBs + tempfile fixtures, never the real DB — recorded as verified, not assumed).
- Integration-record:  w1 4 folded (4.1 the shipped (h) check caught THIS draft's stale "no lens has read" Closing live — the second artifact this week, and the shipped o1's first in-the-wild INFO line ran clean on this draft (candidates=9 excluded=6 fired=0); 4.1 `set_proposal_route` bypass stated with reason — the helper is route-only, the transaction supersedes it for atomicity; 4.1 Test Scope header field added per 311's newest-same-class convention; 4.2 QA gains the consumer check — get_unclassified semantics hold post-routing, accepted AND reference both keep entries dispositioned per the helper's docstring).
- ACID:                a1 5 folded, apart (5.3 LOADED — the QA dump-diff gains the verdict-window PARTITION: within-range foreign lines HALT, outside-range lines are named-not-punished concurrent activity (the parallel terminal is live); 5.2 the rowcount-as-window-guard invariant stated not accidental; 5.1 the mid-QA evidence-without-receipt member stated; the dev log must record the transaction timestamp (QA 1(d)'s comparator had no producer); record read caught the Walks-header lag — fourth artifact running, proposal 258's class). aC 1 folded then re-read dry, apart (c1's fold re-verified — 225 ∈ CODIFY-44, producer/consumer sites agree; the Walks header lagged a SECOND time in this cycle, synced).

**Conflicts:** none yet. Constraints append at the END as earned, never inserted above an existing entry.

**Confirming:** c1 (four lenses, from the bytes, rotated to payload lists / Receipt / header / Method) — 1 folded (the dev-log content list omitted the transaction timestamp its own mandate created two bullets above — proposal 225's producing-step handshake class, live in the plan routing that proposal; all other regions dry, incl. both retraction-wording sites and the tier line's parseability). **c2 (four lenses, full fresh read + the §5 conformance run) — DRY AT ZERO, per-lens: Weak spots dry · Destruction dry · Vulnerabilities dry · Integration-record dry.**

**Closing:** the last event is a lens pass — c2, a full four-lens fresh read, returned dry at zero. Cycle: w1 18+1 (per-lens turns, a1 apart) → c1 1 → aC 1-then-dry (apart) → c2 dry. **21 folds + 1 verified-clean, all landed, per-phase committed; lint EARNED at 0 WARN with shipped o1 clean on the plan itself.** Deposit once, on CEO release, with the id re-read from `id_sequence` at deposit per the header note; runs independent of any bellows-repo plan (disjoint files). (The prior form of this line still asserted zero lens coverage after three passes and was caught by the SHIPPED (h) check during a lens-4 lint probe; the first retraction wording here then re-tripped (h) by QUOTING the caught phrase — the 305-measured retraction-text class, resolved by describing it instead. Two shipped-check catches on one line.)
