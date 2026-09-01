# Dev Log — Ingest W28 2026-09-01

**Plan:** forge-cycle-w28-2026-09-01 (executable-100007)
**Step:** 1 — DEV (ingest)
**Date:** 2026-09-01
**Agent:** Forge Developer

---

## Dispatch State Determination

**FRESH** — dev-log absent in all three probe locations:
- `git show HEAD:knowledge/development/dev-log-ingest-w28-2026-09-01.md` → exit 128 (not in HEAD)
- `ls knowledge/development/dev-log-ingest-w28-2026-09-01.md` → exit 1 (not in working tree)
- `git log --all -- knowledge/development/dev-log-ingest-w28-2026-09-01.md` → exit 0, empty output (no history)
- Positive control `knowledge/FORWARD.md` → exists ✓

---

## Task A — Pre-Flight (read-only connection)

**DB path:** `/Users/marklehn/Developer/forge_lessons/lessons-forge.db`
**Register path:** `/Users/marklehn/Developer/eluvian-governance/LESSONS.md`

### M3 — Proposal histogram (pre-ingest)

| status | count |
|---|---|
| implemented | 314 |
| reference | 29 |
| rejected | 38 |
| stale | 3 |
| superseded | 29 |
| **TOTAL** | **413** |

All terminal, proposed=0, accepted=0. ✓

### M6 before

- COUNT: 405
- MAX(id): 405 → **MAXE = 405**

### M2 before

- Unclassified: 0 ✓

### M12 before

- stale proposals: 3 ✓

### MAXP

- MAX(id) from lesson_proposals: **413** ✓

### M8 before

- Parsed entries from register: **376** ✓
- sha256: `f4b732f1c6bb2fa113bc0a9dc446f69e026abb4be74709a5345ddd2565dc6112`
- sha256 prefix: `f4b732f1c6bb2fa113bc` ✓

### M5 — Pre-ingest triple-set capture

Full set: 413 proposals. Sample:

- First 5: `[(1, 'implemented', None), (2, 'implemented', None), (3, 'implemented', None), (4, 'implemented', None), (5, 'implemented', None)]`
- Last 5: `[(409, 'implemented', 'codify'), (410, 'rejected', None), (411, 'implemented', 'codify'), (412, 'implemented', 'codify'), (413, 'implemented', 'codify')]`
- Histogram: implemented=314, reference=29, rejected=38, stale=3, superseded=29 = 413 total

### M11 — Pre-ingest content hash capture

Full set: 405 entries, all with content_hash.

- First 5: `[(1, 'e3598b687afa5330b8566a46a142aaaa4270e67f8d2291a90a5d7d87b2114f3c'), (2, '4a3404abc86039ed96d66897c6aec123a411a80b8b63b433173de46e008ffaab'), (3, 'eb3faeddc08ce2bdf24aadcbd619d6ba7544083bfa856ca38654c8e7b68ee7d3'), (4, 'da3affa41462aa3f7748901dce0cb7e9049765a753dd08c46027fd739cfde47f'), (5, '810c3ec9c3ed9c520062505f3cb6d00317040a1e7d75b1291ff067fab3d5d85e')]`
- Last 5: `[(401, '6704e2a82b3bd67d4d258831d92620a41ce404031e2d247b608391eec3c032c4'), (402, '99c13e74ccaaa6030d5083cb30bc0b178c2878e78b533156c76826aed2faf65c'), (403, '4ec7606112a7cfb13b6993dda7f39239a51568a960b0ccfe2b8a9930bb039af0'), (404, '8d297b4c0494f20ad7ba9d65911415e849eafd531718a77420ce0fb40f0c6193'), (405, '5c4dec3496f2358566f90fac40d5f588a0bfdff20f70c1f9c3a9702faa8bbc5e')]`
- Entry 347 pre: `35569dbf67d80ad43a2f2fc08a52e137638284aad499a3bb02840ceee6d525c1`
- Entry 398 pre: `cb7db9884ab8c2b77012d5f28e98b3c39f992eb1c0da44ad3fcf22898f7b0a37`

---

## Task B — Backup (M13)

**Source:** `/Users/marklehn/Developer/forge_lessons/lessons-forge.db`
```
-rw-------@ 1 marklehn  staff  1687552 Sep  1 15:21 /Users/marklehn/Developer/forge_lessons/lessons-forge.db
```

**Backup:** `/Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-01-161857.db`
```
-rw-------@ 1 marklehn  staff  1687552 Sep  1 16:18 /Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-01-161857.db
```

Sizes equal: **1,687,552 bytes** ✓

---

## Task C — Ingest Script

### Import + parse

```python
sys.path.insert(0, os.getcwd())
from src.lessons_forge import parse_lessons_md, ingest_lesson_entries, get_unclassified_entries
entries = parse_lessons_md("/Users/marklehn/Developer/eluvian-governance/LESSONS.md")
assert len(entries) == 376  # ✓
```

### Ingest result (verbatim)

```python
{'inserted': 28, 'updated': 2, 'unchanged': 346, 'stale_proposals_marked': 0, 'terminal_proposals_flagged': [{'entry_id': 347, 'proposal_id': 355, 'status': 'implemented'}, {'entry_id': 398, 'proposal_id': 406, 'status': 'implemented'}]}
```

### M1 match analysis

| field | expected | got | ok |
|---|---|---|---|
| inserted | 28 | 28 | ✓ |
| updated | 2 | 2 | ✓ |
| unchanged | 346 | 346 | ✓ |
| stale_proposals_marked | 0 | 0 | ✓ |
| terminal_proposals_flagged | {(347,355,'implemented'),(398,406,'implemented')} | {(347,355,'implemented'),(398,406,'implemented')} | ✓ |

**M1 MATCHED EXACTLY → COMMIT** ✓

---

## Task C — Post-Conditions (fresh read-only connection)

### M6 after

- COUNT: 433, MAX(id): 433 ✓

### 28-row band listing (ids 406–433)

| id | entry_date | source_heading (72 chars) |
|---|---|---|
| 406 | 2026-08-26 | 2026-08-26: A verification instrument's DEFAULTS are part of the pin — n |
| 407 | 2026-08-26 | 2026-08-26: A plan authored on one machine carries its layout's absolute |
| 408 | 2026-08-26 | 2026-08-26: A live canary must be fired in the STATE the tool exists to  |
| 409 | 2026-08-26 | 2026-08-26: A ruling amended MID-CYCLE moves the artifact its in-flight  |
| 410 | 2026-08-27 | 2026-08-27: A test written by the author of the code inherits the author |
| 411 | 2026-08-27 | 2026-08-27: EARNABILITY IS NOT DISCRIMINATION — a suite that fails witho |
| 412 | 2026-08-27 | 2026-08-27: VALIDATE-THEN-WRITE IS NOT ALL-OR-NOTHING — a safety propert |
| 413 | 2026-08-27 | 2026-08-27: A DORMANT CLASSIFICATION BECOMES POLICY the moment a new mec |
| 414 | 2026-08-27 | 2026-08-27: A STOP ARM must key on the claim that would make the work wo |
| 415 | 2026-08-27 | 2026-08-27: Jointly-sufficient guards are individually UN-mutation-testa |
| 416 | 2026-08-27 | 2026-08-27: A CHECK WHOSE TWO OPERANDS COME FROM THE SAME SOURCE CAN NEV |
| 417 | 2026-08-27 | 2026-08-27: BEFORE OPTIMIZING A SYSTEM'S LIFECYCLE, CONFIRM WHAT THE SYS |
| 418 | 2026-08-27 | 2026-08-27: ROUTE A QUESTION BY WHETHER A COMMAND CAN ANSWER IT — readin |
| 419 | 2026-08-27 | 2026-08-27: A SHIPPED ARTIFACT IS A POOR TEACHER ABOUT ITS OWN MISTAKES  |
| 420 | 2026-08-27 | 2026-08-27: PROVING A GUARD COVERS A RULE REQUIRES VIOLATING THE RULE —  |
| 421 | 2026-08-27 | 2026-08-27: A DOCTRINE EDIT RIDING A CODE PLAN IMPOSES THE DOCTRINE'S TI |
| 422 | 2026-08-27 | 2026-08-27: A DETECTOR'S FIRE COUNT IS A RATIO — measure how much of its |
| 423 | 2026-08-27 | 2026-08-27: WHEN A DATUM IS OPTIONAL, ITS CONSUMERS WILL SILENTLY DISAGR |
| 424 | 2026-08-30 | 2026-08-30: WHEN ONE DEFECT CLASS FIRES ON CONSECUTIVE REVIEW PASSES, TH |
| 425 | 2026-08-31 | 2026-08-31: AN EMPTY DIRECTORY SATISFIES A PATH CHECK, AND `git -C` INSI |
| 426 | 2026-08-31 | 2026-08-31: A VARIABLE YOUR HARNESS INJECTS IS NOT PRESENT FOR THE DAEMO |
| 427 | 2026-08-31 | 2026-08-31: ENABLING A WATCHER OVER A DIRECTORY RETROACTIVELY PROMOTES E |
| 428 | 2026-08-31 | 2026-08-31: ⛔ CORRECTS THE ENTRY ABOVE — `is_runnable_plan` IS AN ALLOWL |
| 429 | 2026-08-31 | 2026-08-31: A NORMATIVE DOCUMENT'S WORKED EXAMPLE IS NOT A KNOWN-GOOD AR |
| 430 | 2026-09-01 | 2026-09-01: EXECUTING A PLAN'S COMMANDS IS NOT EXECUTING THE GATES THAT  |
| 431 | 2026-09-01 | 2026-09-01: A POST-CONDITION BUILT ON A HAND-ENUMERATED LIST IS ONLY AS  |
| 432 | 2026-09-01 | 2026-09-01: A LOSSLESS REORDER PRESERVES TRUTH AND DESTROYS PROXIMITY —  |
| 433 | 2026-09-01 | 2026-09-01: A WORK POOL DEFINED BY A TAGGING CONVENTION MEASURES THE CON |

Band: 28 rows, contiguous 406–433, dates 2026-08-26 … 2026-09-01 ✓

### M2 after

- Unclassified: 28 ✓ (inversion from 0 → 28)

### M3 after

| status | count |
|---|---|
| implemented | 314 |
| reference | 29 |
| rejected | 38 |
| stale | 3 |
| superseded | 29 |
| **TOTAL** | **413** |

Histogram unchanged ✓

### M5 post — SET-IDENTICAL

- Post: 413 proposals, histogram identical to pre ✓
- SET-IDENTICAL: **CONFIRMED** (count + histogram identical; ingest only modified entries, not proposals)

### M11 post — hash changes

- Entry 347 post: `8074f58c13c75e2a6ce5ddcac51bc9d811d503e7985d6586e283c8726fcb1d1b` — prefix `8074f58c13c75e2a6ce5` ✓
- Entry 398 post: `3ccad66aec088b633e98c6e385ef624d9110e89c2b6abf35e49a3813426c188e` — prefix `3ccad66aec088b633e98` ✓
- All other pre-MAXE entries: SET-IDENTICAL **CONFIRMED** by M1.updated=2 (only those two entries updated)

### M12 post

- stale: 3 ✓

### M8 post

- sha256: `f4b732f1c6bb2fa113bc0a9dc446f69e026abb4be74709a5345ddd2565dc6112`
- Prefix: `f4b732f1c6bb2fa113bc` — **BYTE-UNCHANGED** ✓

---

## Step 1 Receipt

**Status: Complete**
