# Executable: Gate-1 routing write for proposals 347–352 — 4 → `accepted|codify`, 2 → `reference`, per the fold-damage packet

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-414 (Done — classified the six, stamps NULL), executable-411 (Done — ingested the batch), `/Users/marklehn/Developer/GitHub/gate1-packet-folddamage-2026-08-14.md` (the DECIDED block, root `eabc73f`)
**Created:** 2026-08-14
**Author:** Planner
**Slug:** `gate1-write-347-352-2026-08-14`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted (single module, session-verified; QA row 4 re-derives; baseline 55 passed)

⚠️ **ID NOTE:** id read at deposit (a read-only PREDICTION; the daemon mints at claim).

⚠️ **Derived by READING 402 SECTION BY SECTION, not token-swapping it** — proposal **350**, routed by this very plan, is the rule that mandates exactly that.

## Why

Gate 1 for the six is DECIDED — **CEO instructions "agree with codify" then "proceed with the 7", 2026-08-14, this session, on `gate1-packet-folddamage-2026-08-14.md` (root `eabc73f`)** — reversible on CEO review:

- **A-set `347, 348, 350, 352` → `accepted|codify`** — 347 the fold-post-condition unit + 348 the machine-contract check (the pair the CEO approved on 2026-08-14 as `fold_check` + ONE §2.7 bullet, a sixth lens explicitly declined); 350 the clone-derivation rule (the CEO's call on the packet's one open question); 352 the midnight-date clause.
- **R-set `349, 351` → `reference|reference`** — live doctrine carries both rules; these are instances that sharpen them.

**There is NO backlog route and NO FORWARD row this run.** The Gate-2 queue goes 3 → **7** (340, 342, 346 standing; 347, 348, 350, 352 added).

⚠️ **Sentinel posture — the CLEANEST case, RE-MEASURED not inherited: all six prior stamps are NULL** (`status_updated_at` AND `status_updated_by` both NULL per id, measured at authoring — 414's classifier set `proposed_at` only). **So `status_updated_at IS NOT NULL` with the bare Z-GLOB is a COMPLETE value guard and NO prior-value exclusion is needed.** ⚠️ **This INVERTS 402's posture**, where all ten rows shared a live stamp and the one-value exclusion carried the guard; carrying that exclusion here would be a guard against a value that does not exist.

**Per-id categories, measured (stated so nobody infers uniformity):** 347 `structural`, 348 `structural`, 349 `governance_rule`, 350 `governance_rule`, 351 `governance_rule`, 352 `governance_rule` — **a 2/4 split, not uniform.**

## Scope

- **One DB write session, TWO scoped UPDATEs in ONE transaction** at the canonical absolute path; `status_updated_by='ceo'` (the Gate-1 authority). No doctrine touch, no LESSONS touch, no FORWARD touch by any step (receipts say `NONE`).
- Env facts: `grep` is a ugrep shim — `-F` for literals, and a zero-match `grep -c` prints `0` and EXITS 1 (read the count, never the exit code); `--` before dash-leading literals; shell state does not persist between invocations; **the canonical DB is named by ABSOLUTE path — a bare relative name CREATES an empty file**; `find` uses `-name`, never a bare glob.
- **Post-write expected corpus (every number measured 2026-08-14, live):** `accepted` = **7** (3 standing + 4 new), `proposed` = **0**, `reference` STATUS = **20** with route split **14 `reference` + 6 `backlog`** (the six pre-existing backlog-route ids 161/169/291/294/299/301 are UNCHANGED — this run writes no backlog row), `implemented` = 279, `stale` = 3, `superseded` = 28, `rejected` = 15, total **352**.

## Freeze checklist (items 1–4 BEFORE the copy, item 5 immediately AFTER)

1. Substitute the read id at the bootstrap `<id>` site; probe in OCCURRENCE form: `grep -oF -- '<id' <deposit-path> | wc -l` (the value is MEASURED at the freeze, never predicted here — the 405/342 lesson).
2. **Diff the draft against the mirror immediately before the copy** — an empty diff is the deposit precondition.
3. Final `plan_lint` at the FAITHFUL scratchpad mirror (NEVER the real `decisions/` — the daemon claims AND DISPATCHES same-second, proven live three times this session); the WARN set must match the measured set recorded in the Cycle Log's Conformance line.
4. A0-fresh re-check: all six still `proposed` with NULL stamps; `accepted` still 3 with the id set `{340, 342, 346}`.
5. Post-copy, same minute: `ls` the real `decisions/` — the claim reads `in-progress-executable-<READ-ID>.md` (mismatch = foreign in-window consumption — report, never re-copy).

## Conflict Ledger

- **C1 — the write is a scoped compare-and-swap, TWO statements:** A-set `id IN (347,348,350,352) AND status='proposed'`; R-set `id IN (349,351) AND status='proposed'`. A row already moved is a no-op that the sentinels expose. *(observer: QA Item 5)*
- **C2 — sentinels BY NAME, counted:** PRE_A=4, PRE_R=2 (asserted TWICE — E-a2's rollback-guarded pre-flight BEFORE any write, then in-txn), BK=6, CHANGES_A=4, CHANGES_R=2, STAMP_A=4, STAMP_R=2, ACC_POST=7, PROP_POST=0, REF_POST=20, IMPL_POST=279 — **twelve**, counted. Capture inside the txn `id <= 352 AND id NOT IN (347,348,349,350,351,352)`, SIX columns → **346 rows**. *(observer: QA Item 5)*
- **C3 — the stamp guard needs no exclusion** (the Why's sentinel posture): `status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z'` is complete because every prior value is NULL. *(observer: QA Item 5's per-id read)*
- **C4 — ⚠️ DURABILITY IS PROVEN POST-COMMIT** (DC v2.10 §2.7, shipped by plan 405 today): every sentinel above prints BEFORE the COMMIT, so a ROLLBACK run emits byte-identical success evidence with nothing written. **Task E-c's fresh-invocation read-back is the ONLY durability proof, and it is ASSERTED.** *(observer: QA Item 5, which states it is a post-COMMIT fresh-connection read)*
- **C5 — one action per ops compound with its own post-condition close** (PT §85 is the cd-absolute + failable-close half; the one-action half is this plan's discipline). No `--amend`. *(observer: QA Item 3)*
- **C6 — the standing queue is untouched:** 340/342/346 keep `accepted|codify` and their existing stamps; the capture proves it. *(observer: QA Item 5)*

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---

## STEP 1 — DEV (the routing write)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename this file. Own working tree; canonical DB by ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (`forge/forge.db` is a DIFFERENT database — never open it).
>
> **Task A0 — branches, catch-all LAST.**
> **(1) STATE:** `sqlite3 -readonly <abs> "SELECT id||'|'||status||'|'||COALESCE(route,'NULL')||'|'||COALESCE(status_updated_at,'NULL') FROM lesson_proposals WHERE id BETWEEN 347 AND 352 ORDER BY id;"`
> **(2) STANDING QUEUE:** the `accepted` id set is exactly `{340, 342, 346}`.
> **(3) RE-ENTRY key:** `git log --oneline -1 -- knowledge/development/g1-fd-route.sql` — subject carries this plan's slug?
> - **FRESH** = all six `proposed|NULL|NULL` AND (2) holds AND (3) no → Task B.
> - **RE-ENTRY (complete)** = (3) yes AND all six carry their decided routes → re-run E-c's read-back fresh and report complete. **Tail half-state:** if the dev note lacks the sentinel/read-back section, re-append from E-c's fresh read plus the committed capture's line count (mark `re-derived on re-entry`; CHANGES_A/CHANGES_R are unreconstructable — say so rather than invent them); if the capture or dev note sits uncommitted, complete Task E's closing commit for exactly those paths.
> - **NONE-MATCH** = anything else — including any row already moved, any missing/extra id in the standing queue, or a non-NULL stamp on one of the six → **HALT quoting every measurement.**
>
> **Task E-a — backup + evidence dir.** `mkdir -p knowledge/qa/evidence/gate1-write-347-352-2026-08-14`. **A `pre-g1fd-*.db` backup already on the lessons-forge root → REUSE via `find … -name 'pre-g1fd-*.db'` (⚠️ `.db`-SCOPED — a bare prefix matches `-wal`/`-shm` sidecars and returns ~3 per backup, HALTing the recovery arm spuriously; executed proof, 405 cycle), never a second; >1 match → HALT.** Otherwise: `sqlite3 -bail <abs> ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-g1fd-$(date -u +%Y%m%d_%H%M%S).db"`. Verify **in exactly this form**: `sqlite3 -readonly "file:<backup>?immutable=1" "SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 347 AND 352 AND status='proposed';"` → **BK=6**. ⚠️ **The `file:` URI and `?immutable=1` are BOTH load-bearing — a plain `sqlite3 -readonly <backup>` fails with `(14)`** (executed proof, 405).
>
> **Task E-a2 — live pre-flight, ROLLBACK-guarded, BEFORE any write:** `sqlite3 -bail <abs> ".timeout 5000" "BEGIN IMMEDIATE; SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (347,348,350,352) AND status='proposed'; SELECT 'PRE_R='||COUNT(*) FROM lesson_proposals WHERE id IN (349,351) AND status='proposed'; SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted'; SELECT 'MAXID='||MAX(id) FROM lesson_proposals; ROLLBACK;"` → assert **PRE_A=4, PRE_R=2, ACC=3, MAXID=352**; any off → HALT, NOTHING written.
>
> **Task E-b — the write** (file `knowledge/development/g1-fd-route.sql`, exactly; runner `sqlite3 -bail <abs> ".timeout 5000" ".read <abs-sql>"`, exit 0 + empty stderr):
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (347,348,350,352) AND status='proposed';
> SELECT 'PRE_R='||COUNT(*) FROM lesson_proposals WHERE id IN (349,351) AND status='proposed';
> .output /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/gate1-write-347-352-2026-08-14/route-capture.txt
> SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 352 AND id NOT IN (347,348,349,350,351,352) ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (347,348,350,352) AND status='proposed';
> SELECT 'CHANGES_A='||changes();
> UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (349,351) AND status='proposed';
> SELECT 'CHANGES_R='||changes();
> SELECT 'STAMP_A='||COUNT(*) FROM lesson_proposals WHERE id IN (347,348,350,352) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> SELECT 'STAMP_R='||COUNT(*) FROM lesson_proposals WHERE id IN (349,351) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> SELECT 'ACC_POST='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
> SELECT 'PROP_POST='||COUNT(*) FROM lesson_proposals WHERE status='proposed';
> SELECT 'REF_POST='||COUNT(*) FROM lesson_proposals WHERE status='reference';
> SELECT 'IMPL_POST='||COUNT(*) FROM lesson_proposals WHERE status='implemented';
> COMMIT;
> ```
> Assert **PRE_A=4, PRE_R=2, CHANGES_A=4, CHANGES_R=2, STAMP_A=4, STAMP_R=2, ACC_POST=7, PROP_POST=0, REF_POST=20, IMPL_POST=279**; capture **346 lines**. ⚠️⚠️ **Every sentinel prints BEFORE the COMMIT — a rollback run produces perfect sentinels and a full capture with NOTHING written (C4; DC v2.10 §2.7). E-c is the ONLY durability proof.**
>
> **Task E-c — post-COMMIT read-back, FRESH invocation, ASSERTED:** `sqlite3 -bail -readonly <abs> ".timeout 5000" "SELECT id||'|'||status||'|'||route||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id BETWEEN 347 AND 352 ORDER BY id;"` → 347/348/350/352 read `accepted|codify|ceo|<Z-stamp>` and 349/351 read `reference|reference|ceo|<Z-stamp>`; **any other read → HALT loudly (the COMMIT did not land — do NOT re-run; name the backup)**. Then append the FULL sentinel set (all twelve, each spelled — ⚠️ CHANGES_A/CHANGES_R are the only proof THIS run wrote and have no other durable site) plus the read-back RAW to `knowledge/development/gate1-write-fd-dev-2026-08-14.md`, and **commit the dev note + `g1-fd-route.sql` + `route-capture.txt`** (ONE compound, cd-first, pathspec naming all three, no amend — an uncommitted deposit fails the gate). Then STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate1-write-fd-dev-2026-08-14.md`
> - `lessons-forge/knowledge/development/g1-fd-route.sql`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-347-352-2026-08-14/route-capture.txt`
>
> **Scope:**
> - `knowledge/development/gate1-write-fd-dev-2026-08-14.md`
> - `knowledge/development/g1-fd-route.sql`
> - `knowledge/qa/evidence/gate1-write-347-352-2026-08-14/route-capture.txt`

---

## STEP 2 — QA

> ⚠️⚠️ **PRECONDITION — Step 1 ran as its own dispatch:** `git log --oneline -1 -- knowledge/development/g1-fd-route.sql` names the Step-1 commit, made before this step began and not by this context. Otherwise mark the independence gap plainly. **No Monitor anywhere; every command foreground. Verification only — a FAIL is reported, never repaired.**
>
> **(A) Rule 20 self-check block** — the canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (read live). Canonical header `Rule 20 — QA Self-Check Results`; on full pass the canonical line `PASSED — SELF-CHECK PASSED`. `required_evidence_files` = the evidence-directory subset of `## Scope`.
>
> **(B) Deliverable verification:**
> - **Item 1 — deliverables (Rule 17):** per path `git log --oneline -1 -- <path>` (empty = ❌) + porcelain with echoed exit.
> - **Item 2 — targeted suite:** `python3 -m pytest src/ -v`, raw tail → `probes-raw.txt`; value cell `<N> passed` (baseline 55; a delta is reported, never asserted).
> - **Item 3 — C5 commit shape:** `git show --name-only --format=` lists exactly the three deposited paths; single non-amend commit (one parent); toplevel printed.
> - **Item 4 — C6, the standing queue:** 340/342/346 still `accepted|codify` **with their PRE-EXISTING stamps** (i.e. NOT this run's) — a changed stamp on any of the three means the write's scoping leaked → ❌ Critical.
> - **Item 5 — C1/C2/C3/C4, the write (read-only re-verify):** per id 347–352 the decided status+route with `ceo` and a Z-stamp; `accepted` = **7** with the id set `{340,342,346,347,348,350,352}` named; `proposed` = **0**; `reference` = **20** with route split 14/6 and the six backlog ids unchanged; `implemented` = 279; re-run the EXACT capture SELECT (copy from `g1-fd-route.sql`, never re-type) and diff vs the deposited 346-line `route-capture.txt` — any delta partitioned (impossible-id → FAIL; deleted-row → FAIL; else concurrent, named). **State explicitly that this re-verify is a POST-COMMIT fresh-connection read and cites no in-transaction sentinel** (DC v2.10 §2.7 binds this item).
> - **Item 6 — corpus preservation:** entries still 344; `lesson_proposals` still 352 (a routing write creates no row).
> - **Item 7 — register posture:** lessons-forge `decisions/` non-Done contents = this plan's own `in-progress-*` file ONLY; `knowledge/FORWARD.md` delta ZERO against the baseline captured in Step 1's dev note (probe form `grep -c "^| "`) — any new row is a finding.
> - **Item 8 — raw output throughout.**
>
> Commit the receipt + raw file (cd-first, pathspec exactly them, no amend), then STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-fd-qa-2026-08-14.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-347-352-2026-08-14/probes-raw.txt`
>
> **Scope:**
> - `knowledge/qa/gate1-write-fd-qa-2026-08-14.md`
> - `knowledge/qa/evidence/gate1-write-347-352-2026-08-14/probes-raw.txt`

---

## Drafting Cycle

**Tier:** T1 — production-data mutation (T-2); structure-for-structure clone of shipped 402 keeps T-8 silent; both parent cycles (411, 414) closed with every gate first-run clean.

**Walk register:** `governance/knowledge/research/walk-register-gate1-write-347-352-2026-08-14.md` (schema 0.3), committed per phase.

**Walk 0 (context pin, measured 2026-08-14):** all six rows `proposed|route NULL|stamp NULL` per id; categories 2 `structural` + 4 `governance_rule` (NOT uniform); ACC 3 = `{340,342,346}`; REF 18 (route split 12 reference + 6 backlog, ids 161/169/291/294/299/301); PROP 6; IMPL 279; MAXID 352; capture 346 rows; suite 55 passed. **Clone origin AND newest same-class = 402** (`gate1-write-337-346`, Done 2026-08-14 — both roles resolve to the same plan, measured by ship date against the Gate-1-write class; ⚠️ the literal phrase `newest same-class` is load-bearing for plan_lint check (k), which fired on an earlier form of this line — the THIRD literal-keyed check this session). **Clone-diff vs 402, read section-by-section (the rule this plan routes):** 402's THREE route sets collapse to TWO here (no `implemented` set — nothing in this batch has a shipped remedy); ⚠️ **402's one-value stamp exclusion is DROPPED with its premise measured absent** — all six priors are NULL, so the bare Z-GLOB is complete and carrying the exclusion would guard a value that does not exist; the standing-queue guard (C6) is NEW, because 402 ran with `accepted` = 0 and this plan runs with three rows it must not touch; the `.db`-scoped backup form and the `file:…?immutable=1` verify are carried FORWARD with their executed proofs; E-c's asserted read-back is carried and now also mandated by DC v2.10 §2.7, which 405 shipped after 402 ran.

**Walks (2 warm):**
- Weak spots:          w1 dry (A0's four arms, the reuse arm, and every sentinel re-read against the rehearsal); w2 dry.
- Destruction:         w1 dry (C6 is a NEW guard protecting three rows this plan must not touch — additive to 402's posture, relaxing nothing; the dropped one-value exclusion is a guard whose PREMISE was measured absent, not a weakening); w2 dry.
- Vulnerabilities:     w1 EXECUTED — the full two-set write rehearsed on a scratch DB copy: **all twelve sentinels exact** (PRE_A=4, PRE_R=2, CHANGES_A=4, CHANGES_R=2, STAMP_A=4, STAMP_R=2, ACC_POST=7, PROP_POST=0, REF_POST=20, IMPL_POST=279), capture **346 lines**, post-COMMIT read-back correct per id, **the standing queue's stamps UNCHANGED** (still `2026-08-14T13:21:27Z`, not this run's), and an idempotent re-run returning CHANGES_A=0/CHANGES_R=0 with ACC_POST still 7; w2 dry.
- Integration-record:  w1 dry (Deposits project-prefixed, Scope repo-relative; stray-token sweep for `337`/`346`-as-A-set/`s42sweep` clean); w2 dry.
- ACID:                w1 dry (two steps, one gate window; both UPDATEs in ONE transaction so no half-routed state exists; E-c the durability proof per DC v2.10); w2 dry.

**Splits: w1 instruction 0 / record 0 — DRY (the clone-diff findings landed at walk 0) · w2 dry.**

**Conformance (§5):** faithful-mirror `plan_lint` at the deposit-shaped scratchpad mirror — NEVER the real `decisions/`. The measured set at the close run is what freeze item 3 binds to; the placeholder-lens WARN clears when this Walks block fills.

**Closing:** walk 2 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced). The section-by-section clone-diff and the scratch-copy rehearsal are where this cycle's assurance came from; fold-and-deposit exactly once.
