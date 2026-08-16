# Executable: Gate-1 routing write for proposal 353 — `accepted|codify`, per the lessons-routing packet

**Type:** Executable
**Date:** 2026-08-15 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DB write) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `gate1-write-353-2026-08-15`
**Project:** lessons-forge
**dispatch_mode:** bellows
**Priority:** 1
**Depends on:** **`lessons-forge/knowledge/decisions/Done/executable-416.md`** — direct clone origin AND newest same-class (Gate-1 routing write, Done 2026-08-14), read SECTION BY SECTION; `/Users/marklehn/Developer/GitHub/gate1-packet-lessons-routing-2026-08-15.md` (the DECIDED block — the decision this plan executes); plans 423 and 427 (Done) and 425 (**halted** — substance landed at `8bfb954`, QA discharged by 427; the file is `halted-executable-425.md`, disposition pending — scout S0-6: the draft called all three "Done", contradicting its own table).

## Why
Gate 1 for proposal 353 is **DECIDED — CEO `codify`, 2026-08-15, planner-terminal session, on `gate1-packet-lessons-routing-2026-08-15.md`**, with the author-conflict disclosure in view and the CEO's stated basis recorded in the packet's DECIDED block — verbatim: **"codify. and the good news is that the cold reader is still catching it, so we have time to correct later if this doesn't work as expected"** *(scout S0-8: the draft had truncated the conditional clause without ellipsis — on the one plan whose record-fidelity the conflict disclosure makes load-bearing)*. This plan executes exactly that decision: **ONE row, `353` → `status='accepted', route='codify'`**, stamped `ceo`. It decides nothing.

⚠️ **The write's blast radius is one row and the plan proves it stays one row.** The corpus's five standing `accepted|codify` rows (340/342/346/350/352) must be byte-untouched — their stamps are the live evidence (`2026-08-14T13:21:27Z` ×3, `2026-08-14T18:38:14Z` ×2, all `ceo`), and a changed stamp on any of them is a HALT even if status and route look right. *(A count is not a value guard; a stamp is.)*

## What is already true — measured at authoring 2026-08-15, re-measured by Step 1 as its A0
| fact | value |
|---|---|
| 353 pre-write posture | `status='proposed', route=NULL, status_updated_at=NULL, status_updated_by=NULL` — **the clean sentinel: both stamps NULL** (the 416 posture) |
| `proposed` rows total | **1** (this one — the write drains `proposed` to zero) |
| the standing five | 340/342/346/350/352 all `accepted\|codify\|ceo`, stamps as quoted above |
| E0 / P0 | 345 / 353 |
| timestamp form | ⚠️ **Z-form via `strftime('%Y-%m-%dT%H:%M:%SZ','now')`** — the form 416 used and the form all five standing rows carry. **The corpus holds FOUR timestamp representations split on the Gate-1 boundary; never substitute another form.** |
| suite | 55 passed (`python3 -m pytest src/ -v`) |
| FORWARD | 18 rows |
| `decisions/` non-Done | `halted-executable-425.md` only (disposition pending, NOT this plan's business) |
| `id_sequence` | read **428** at authoring — a PREDICTION; re-read at deposit (consumed in-window four times this arc; 426 in flight, invoice-pulse, store-disjoint) |

## Rehearsed at authoring — executed against a scratch COPY, not argued
First run: `changes() = 1`, post-state `accepted|codify|ceo|2026-08-16T03:12:39Z`, stamp matches the Z-GLOB. **Re-run: `changes() = 0`** — the pre-state WHERE makes the write idempotent by construction. Standing five stamps byte-unchanged; distribution lands `accepted 6 / proposed 0`.

⚠️ **THE STAMP WILL CARRY TOMORROW'S DATE, AND THAT IS CORRECT.** `strftime('now')` is UTC and this session has crossed UTC midnight: the rehearsal stamped **`2026-08-16T…Z`** on a plan dated 2026-08-15 local. The five standing rows' stamps are same-day-UTC coincidences, not a rule. **QA's GLOB is date-generic by design; no check in this plan pins the stamp's DATE, and none may be "helpfully" added** — a 2026-08-15 pin would fail a correct run. *(The resume-glob-UTC class, and entry 344's midnight class, arriving in the corpus machinery itself; w0-2.)*

## The write — ONE transaction, exactly as 416's form
```
UPDATE lesson_proposals SET status='accepted', route='codify',
  status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo'
WHERE id = 353 AND status='proposed' AND route IS NULL;
```
⚠️ **The WHERE carries the pre-state** (`status='proposed' AND route IS NULL`) so a re-run or a raced row updates NOTHING — `changes()` must print **1** on the first run and **0** on any repeat — ⚠️ **read on the WRITING connection immediately after the UPDATE (it is per-connection state; a fresh connection ALWAYS returns 0 — measured, and demanding 1 from it would HALT a correct run — scout S0-1)**. Durability is then proven separately: the FRESH connection verifies the ROW STATE, never `changes()`. *(DC v2.11: in-transaction sentinels prove intent; the post-commit fresh READ-BACK proves durability.)*

## Ledger
- **C1 — one row moves.** Post-state: 353 `accepted|codify|ceo|<Z-stamp>`; `proposed` count 0; `accepted` set exactly `{340,342,346,350,352,353}` **by id**; the five prior stamps byte-identical to the quoted values. *(observer: QA rows 2–4)*
- **C2 — commit proven post-hoc.** `conn.commit()` explicit; every post-condition read from a FRESH connection. *(observer: Step 1 self-report + QA re-read)*
- **C3 — nothing else moves.** Entries 345 untouched; no doctrine file, no `LESSONS.md`, no report, no FORWARD row. *(observer: QA rows 5–6)*
- **C4 — worktree discipline.** All writes to the canonical DB at its ABSOLUTE path (the DB lives outside the worktree by design — `FORGE_GITHUB_ROOT` contract); all FILE deposits relative to the worktree root. ⚠️ Never write a TRACKED-OR-TRACKABLE file to a main-repo-rooted absolute path — the 425 teardown class. **Carve-out, measured: the DB backup is exempt** — `lessons-forge/.gitignore:6` covers `*.db`, so the backup is invisible to git and cannot collide with the teardown merge (precedent: 423's Step 1a wrote its backup identically from a worktree; teardown succeeded). *(w1-1: the S0-4 backup fold contradicted C4 as written — an agent following C4 literally would have refused its own backup step; the two folds never composed. The corrective cycle's w2-1 class, again.)* *(observer: teardown gate)*

## Freeze checklist (deposit path — items 1–3 BEFORE the copy, item 4 immediately AFTER)
1. `plan_lint` at a FAITHFUL deposit-shaped scratch mirror — never the real `decisions/`. **Expected, decidable: exit 0, ZERO `FAIL` lines, and any `(o1)` WARN names only a path verified REAL in the project** *(scout S0-5: "the measured set is the declared expected state" was circular — a check that accepts whatever it finds can never fail, and the set it would have blessed contained a FAIL)*. **Read the linter's OWN exit code, never a filter pipeline's** (scout S0-2's second half).
2. A0-fresh: 353 still `proposed|NULL|NULL|NULL`; the standing five's stamps byte-identical to the quoted values; porcelain clean.
3. **Read `id_sequence` AT deposit** and re-token every filename id site — it read 428 at authoring and has been consumed in-window four times this arc.
4. Residual-token probe with MEASURED expectations (a probe's expected count is measured against the deposit's own self-quoting sites, never declared zero — the 427 freeze lesson); the deposited file byte-identical to the linted mirror copy (`diff` empty — scout S0-7); post-deposit `ls`; commit the daemon's claim rename.

*(w0-1: 416 carries a three-item freeze block and this clone dropped it — the THIRD freeze-apparatus drop in one day, after Plan B's S1-13 and the corrective's S0-9. Recorded, not silently fixed.)*

## How to Run This Plan
**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

## Scope
- `knowledge/development/dev-log-gate1-write-353-2026-08-15.md`
- `knowledge/qa/gate1-write-353-qa-2026-08-15.md`
- `knowledge/qa/evidence/gate1-write-353-2026-08-15/`

---

## STEP 1 — DEV (the write; the only mutation)

> **FIRST — post a short visible chat message; do NOT rename this plan file.** You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`). Canonical DB at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`; `forge/forge.db` is a REAL but DIFFERENT database — never open it. First evidence line is `pwd`; every FILE you write is relative to it.
>
> **Scope:**
> - `knowledge/development/dev-log-gate1-write-353-2026-08-15.md`
>
> **A0 (narrowly keyed — first match wins):** read 353 fresh AND the standing five: (1) 353 == `proposed|NULL|NULL|NULL` **AND the five stamps byte-equal the quoted values** → **PROCEED** (the write is live; a raced Gate-2 flip of the queue is caught HERE, pre-write, not misread at QA row 3 as this plan's leak — scout S0-3). (2) `accepted|codify|ceo|<any Z-stamp>` AND `proposed` count 0 → **idempotent re-dispatch**: record it, run the post-conditions read-only, deposit, stop. (3) ANY other combination → HALT quoting the full row.
>
> **Backup first (416's E-a, dropped in the clone — scout S0-4; the previously named fallback is STALE, the newest pre-cycle backup predates row 353):**
> ```
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-g1w353-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> sqlite3 -readonly "file:$BK?immutable=1" 'PRAGMA integrity_check;'
> ```
> → `ok` (the `file:` URI and `?immutable=1` are BOTH load-bearing on a `.backup` output); backup counts == live (**345/353**). *(w1-2: the S0-4 fold wrote this with `<abs>`/`<UTC>` placeholder tokens where 423 used executable substitution — a placeholder an agent must interpret is one more site to get wrong, and the freeze's residual-token probe would have to carve exemptions for it.)*
>
> **Pre-write captures (read-only, raw):** the full row for 353; the five standing rows WITH their stamps (the byte-baseline QA row 3 compares against); `proposed` count (**1**); `SELECT COUNT(*) FROM lesson_proposals` (**353**); FORWARD baseline `grep -c "^| "` recorded raw (18 at authoring — the QA row compares DELTA against THIS capture, not an absolute — scout S0-10).
>
> **The write:** ONE transaction, the exact UPDATE from the plan body (WHERE carries the pre-state). `conn.commit()`. Record `changes()` == **1** from the WRITING connection immediately after the UPDATE (per-connection state — scout S0-1). Then — **fresh connection** — read back the ROW STATE: 353 == `accepted|codify|ceo` with a Z-stamp matching `20[0-9][0-9]-*Z` GLOB; `proposed` count **0**; total COUNT still **353**. Any mismatch → HALT, recording every measured value; **recovery is the `$BK` backup taken THIS run** (restore by copy after CEO review — never automatically), with the pre-write captured row as the single-row fallback recipe. *(w2-1: this parenthetical previously still said "this plan writes no new backup" — the exact text the S0-4 fold refuted — while the Backup-first block above mandated one; the fold added the new block and never swept the site it contradicted. The register even recorded that text as replaced. Unswept-fold class, sixth instance across today's cycles.)*
>
> **Deposit** the dev log with: A0 determination, the pre-write captures RAW, the UPDATE as executed, `changes()`, the fresh-connection read-back, `#### Prompt Feedback`, `#### Forward Register`: `NONE`. Commit cd-absolute, explicit pathspec, per-path `git log --oneline -1 --` assert.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate1-write-353-2026-08-15.md`
>
> **STOP. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt must be a PROCEED-value** (`Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`). **FIRST — visible chat message; do NOT rename this plan file.** You are Lessons Forge QA. DB **read-only** (`?mode=ro`, absolute); verification only, never repair. First evidence line `pwd`; `<tree-abs>` := that output; HALT if it equals the main repo.
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `gate1-write-353-2026-08-15`; `qa_report_path` `<tree-abs>/knowledge/qa/gate1-write-353-qa-2026-08-15.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/gate1-write-353-2026-08-15/`; `required_evidence_files` `["routing.txt", "untouched.txt", "pytest_targeted.txt"]`. EVERY file in that list AND the report written BEFORE the block; APPEND stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED`, both byte-exact; end with the self-grep. *(scout S0-2: the draft abbreviated "banner" without the literal — `plan_lint` check (c) FAILed exit 1, and the Planner's own mirror lint MISSED it by grepping for WARN|ERROR, filtering out the FAIL line and reading the pipeline's exit.)* Rule 19 verbatim; one glyph per cell; no `|` in cells.
>
> **Scope:**
> - `knowledge/qa/gate1-write-353-qa-2026-08-15.md`
> - `knowledge/qa/evidence/gate1-write-353-2026-08-15/`
>
> Table under `## Verification Table` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — Step 1's dev log: committed, porcelain clean. → `routing.txt`
> 1. **Targeted suite** — `python3 -m pytest src/ -v` from `<tree-abs>`, raw tail; baseline **55 passed**; a delta is reported with both numbers. → `pytest_targeted.txt`
> 2. **THE ROUTE LANDED** — 353 fresh: `accepted|codify|ceo`, stamp matching GLOB `20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z`; `proposed` count **0**. → `routing.txt`
> 3. ⚠️⚠️ **THE STANDING FIVE ARE BYTE-UNTOUCHED** — 340/342/346/350/352 each `accepted|codify|ceo` with stamps EXACTLY `2026-08-14T13:21:27Z` (340/342/346) and `2026-08-14T18:38:14Z` (350/352). **A changed stamp is a HALT even if status and route read right.** → `untouched.txt`
> 4. **Corpus shape** — `accepted` set == `{340,342,346,350,352,353}` by id; COUNT proposals **353**; entries **345**; STALE **3**. → `untouched.txt`
> 5. **Nothing else moved** — the full 8-status distribution vs the pinned pre-write baseline shifted by EXACTLY `proposed −1 / accepted +1`: implemented **281** · superseded **28** · reference **20** · rejected **15** · **accepted 6** · proposed **0** · stale **3** · ambiguous **0**. → `untouched.txt`
> 6. **Register posture** — `knowledge/FORWARD.md` delta vs Step 1's captured baseline is **ZERO** by the same probe form (⚠️ NOT `-F`; an in-window append is a finding, not a false pass — scout S0-10); `decisions/` top-level `.md` == `halted-executable-425.md` + this plan's own file (enumerate `-maxdepth 1 -name '*.md'`). → `untouched.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits cd-absolute, explicit pathspec, per-path `git log --oneline -1 --` assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-353-qa-2026-08-15.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-353-2026-08-15/routing.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-353-2026-08-15/untouched.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-353-2026-08-15/pytest_targeted.txt`

---

## Drafting Cycle
**Tier:** T1 — T-2 fires (one production-DB row moves); structure-for-structure clone of shipped 416, so T-8 silent.
**Walk register:** `governance/knowledge/research/walk-register-gate1-write-353-2026-08-15.md`, carrying a literal `**schema_version:** \`0.3\`` line above any table row.
**Status:** cycle CLOSED 2026-08-15 on a fully DRY walk. Walk count and per-finding detail live ONLY in the register.

**Per-lens lines** *(outcome-only; ids and dispositions in the register)*:
- **Weak spots:** the changes()-per-connection trap, the circular freeze item, A0 exhaustiveness; final walk dry.
- **Destruction:** the raced-queue pre-write key, the stale backup fallback, the backup-vs-C4 interaction; final walk dry.
- **Vulnerabilities:** the UTC-midnight stamp (declared, date-pinning forbidden), the malformed fence (measured against the real parsers), placeholder tokens; final walk dry.
- **Integration-record:** the truncated CEO quote restored verbatim, 425's true state, the surviving pre-fold text swept; final walk dry.
- **ACID:** one transaction, backup before write, idempotent-by-WHERE; dry at every walk.

**Closing:** the final walk read **DRY on all five lenses — instruction 0 / record 0**, no restructuring fold; §2's bar met on a dry pass, no residue. Evidenced — **16 of 16** re-verified at close (the 353 pre-write posture; the proposed count; the five stamps byte-equal; E0/P0; both table counts; STALE; FORWARD; the suite; the decisions/ set; the full CEO quote incl. its conditional; the gitignore *.db line; all 15 attribution ids resolving to register rows; the fences paired; post-strip parser integrity; both steps' scope extraction; the refuted phrase confined to its strike note); `fold_check` CLEAN; rehearsal previously reproduced by an independent cold reader. Fold-and-deposit exactly once.
**Walks:** recorded in the walk register, the single site for walk count, fold count and per-finding detail.
