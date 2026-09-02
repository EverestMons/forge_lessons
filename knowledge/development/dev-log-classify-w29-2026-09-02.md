# Dev Log — Classify W29 — 2026-09-02

**Plan:** forge-cycle-w29-2026-09-02  
**Step:** 2 (Lessons Agent — classify)  
**Agent:** Forge Lessons Agent  
**Date:** 2026-09-02  

---

## Dispatch-State Probe

**This step's dev-log path:** `knowledge/development/dev-log-classify-w29-2026-09-02.md`

| Check | Result |
|---|---|
| Committed HEAD | ABSENT |
| Working tree | ABSENT |
| `git log --all -- <path>` | ABSENT |
| Positive control (`knowledge/FORWARD.md`) | EXISTS ✓ |

**Determination:** FRESH — dev-log absent in all three places. Prior dispatch did not begin.

**Resume semantics check:** `get_unclassified_entries(conn)` returned 25 entries (ids 434–458) — proceeding as FRESH.

---

## Pre-Flight (Read-Only Connection)

### M2 — Unclassified entries
```
get_unclassified_entries(conn) = [434, 435, 436, 437, 438, 439, 440, 441, 442, 443,
                                   444, 445, 446, 447, 448, 449, 450, 451, 452, 453,
                                   454, 455, 456, 457, 458]
count = 25  ✓ (contiguous 434–458)
```

### Existing proposals for the 25 entries
```
SELECT COUNT(*) FROM lesson_proposals WHERE entry_id IN (434,...,458) = 0  ✓
```

### M3 Before — Status Histogram
```
total = 441
  accepted:    12
  implemented: 322
  reference:   34
  rejected:    41
  stale:        3
  superseded:  29
  proposed:     0 (no row)
```
Matches plan expectation: 441 total, accepted=12 ✓

### MAXP (captured)
```
SELECT MAX(id) FROM lesson_proposals = 441
```
MAXP = 441 (bound, not hard-coded) ✓

### M5 — Pre-existing triple-set capture
```
SELECT id, status, route FROM lesson_proposals WHERE id <= 441 ORDER BY id
→ 441 rows
Accepted subset (12):
  (415, 'accepted', 'codify')
  (417, 'accepted', 'codify')
  (418, 'accepted', 'codify')
  (419, 'accepted', 'codify')
  (421, 'accepted', 'codify')
  (422, 'accepted', 'codify')
  (425, 'accepted', 'codify')
  (430, 'accepted', 'codify')
  (431, 'accepted', 'codify')
  (434, 'accepted', 'codify')
  (435, 'accepted', 'codify')
  (437, 'accepted', 'codify')
Triple-set captured as Python set for post-condition comparison.
```

### M6 Before
```
SELECT COUNT(*), MAX(id) FROM lesson_entries → COUNT=458, MAX=458  ✓
```

---

## Classification

Taxonomy applied: ADR-002 six-value taxonomy per `agents/FORGE_LESSONS_AGENT.md`.  
All 25 entries classify as `governance_rule` (each proposes a documentary rule for PLANNER_TEMPLATE.md, MACHINE_SETUP.md, or COMPANY.md — per the decision tree: "if the lesson implies a rule change to PLANNER_TEMPLATE, COMPANY.md, or a specialist file, default to governance_rule").  
All 25 confidence=high (each entry clearly fits one category with cited evidence).  
All 25 route=NULL, status=proposed (default).  
AUTHOR-CONFLICT marker: reasoning text begins with `[AUTHOR-CONFLICT] ` for all entries with entry_date='2026-09-02' (ids 439–458, 20 entries) — by DATE, never by id range.

### DISPOSITION Lines (25)

DISPOSITION | entry=434 | proposal=442 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — designate one record as the authoritative source; make every other representation a tooling-generated projection, never hand-edited | markers: NONE
DISPOSITION | entry=435 | proposal=443 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — route cold reads to the machine holding no active claim; expect a packet, not a direct write | markers: NONE
DISPOSITION | entry=436 | proposal=444 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — checks for a single-home store carry the home as part of their contract; absence elsewhere reports INFO once, not WARN per tick | markers: NONE
DISPOSITION | entry=437 | proposal=445 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — when a second cold pathway is cheap, convene it; read the two reports as a pair for floor and blind-spot measurement | markers: NONE
DISPOSITION | entry=438 | proposal=446 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — run read-only surveys (fan-out, file:line, absences with probe) BEFORE sketching a design; deposit surveys under knowledge/research/ | markers: NONE
DISPOSITION | entry=439 | proposal=447 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — prove location-sensitive code in canonical checkout AND a worktree under it; state the parent each probe resolved | markers: AUTHOR-CONFLICT
DISPOSITION | entry=440 | proposal=448 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — before counting symbol mentions, enumerate and exclude machine-written lines (manifests, summaries, validation stanzas) | markers: AUTHOR-CONFLICT
DISPOSITION | entry=441 | proposal=449 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — a copies claim requires directory entry type, inode comparison, and a difference possible in principle; cmp via a symlink proves nothing | markers: AUTHOR-CONFLICT
DISPOSITION | entry=442 | proposal=450 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — a cold seat finding contradicting a ruling is a CEO question; pause fold, record ruling addendum, push, fold, re-pin in-flight plans | markers: AUTHOR-CONFLICT
DISPOSITION | entry=443 | proposal=451 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — every seat finding gets one disposition: folded, adjudicated-not-folded with reason + measurement, or recorded-unresolved; silent declines are misses | markers: AUTHOR-CONFLICT
DISPOSITION | entry=444 | proposal=452 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — reinterpreting doctrine to keep a cheaper arm is itself the finding; change the plan until the arm holds literally | markers: AUTHOR-CONFLICT
DISPOSITION | entry=445 | proposal=453 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — enumerate edit surface from the callee definition and count callers; list transitions that reach the end state without calling it | markers: AUTHOR-CONFLICT
DISPOSITION | entry=446 | proposal=454 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — budget the scout, execution seat, and capstone; cut warm walks first; give each seat something new to read | markers: AUTHOR-CONFLICT
DISPOSITION | entry=447 | proposal=455 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — before overriding a refusing gate, read the code path after acceptance; override only a formal failure whose substance was independently verified | markers: AUTHOR-CONFLICT
DISPOSITION | entry=448 | proposal=456 | category=governance_rule | remedy: update MACHINE_SETUP.md (§4 begun) and PLANNER_TEMPLATE.md — host long-running processes under an owner with matching lifetime; never a session background task | markers: AUTHOR-CONFLICT
DISPOSITION | entry=449 | proposal=457 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — treat declared path order and per-step Deposits split as gate contracts; run deposit extractor dry-run at walk 0 | markers: AUTHOR-CONFLICT
DISPOSITION | entry=450 | proposal=458 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — when implementation delivers less than a ruling promised, ship the honest smaller thing plus a superseding note in the ruling's record | markers: AUTHOR-CONFLICT
DISPOSITION | entry=451 | proposal=459 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — before a precondition keys on a status indicator, read its producing code and state its scope; prove restarts by process facts | markers: AUTHOR-CONFLICT
DISPOSITION | entry=452 | proposal=460 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — keep approval confirmations harness-generated, not paraphrased by the party wanting approval; quote standing authorizations verbatim | markers: AUTHOR-CONFLICT
DISPOSITION | entry=453 | proposal=461 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — at any system-of-record migration, enumerate and re-provide each guarantee the old substrate gave for free | markers: AUTHOR-CONFLICT
DISPOSITION | entry=454 | proposal=462 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — after changing a server surface, verify from the client's view; name the client-side step in the plan | markers: AUTHOR-CONFLICT
DISPOSITION | entry=455 | proposal=463 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — before offering a recalled fact as the basis for a recommendation, run the command that would falsify it | markers: AUTHOR-CONFLICT
DISPOSITION | entry=456 | proposal=464 | category=governance_rule | remedy: add rule to PLANNER_TEMPLATE.md — before quoting or running a command, read its --help or docstring and name the arm; name non-default arms explicitly | markers: AUTHOR-CONFLICT
DISPOSITION | entry=457 | proposal=465 | category=governance_rule | remedy: update COMPANY.md — define the role, name the machine; sweep in-flight artifacts as a DC fold round when a ruling changes a word's meaning | markers: AUTHOR-CONFLICT
DISPOSITION | entry=458 | proposal=466 | category=governance_rule | remedy: add rules to PLANNER_TEMPLATE.md — record panel rounds on cold-panel line only; place ## Drafting Cycle block above the first step heading | markers: AUTHOR-CONFLICT

---

## THE COMMIT

`conn.commit()` issued exactly ONCE after all 25 `insert_proposal()` calls.

---

## Post-Conditions (Fresh Read-Only Connection)

### M2 — Inversion (should be [])
```
get_unclassified_entries(conn) = []  count=0  ✓
```

### M3 After
```
total = 466
  accepted:    12  (unchanged ✓)
  implemented: 322
  proposed:    25  (new band, K=25)
  reference:   34
  rejected:    41
  stale:        3
  superseded:  29
K = 25  ✓
```

### M4 — New proposals all route=NULL, status='proposed'
```
SELECT COUNT(*) FROM lesson_proposals
  WHERE id > 441 AND (route IS NOT NULL OR status <> 'proposed') = 0  ✓
```

### M17 — One proposal per entry, all in band 434–458
```
SELECT entry_id, COUNT(*) FROM lesson_proposals WHERE id > 441
  GROUP BY entry_id HAVING COUNT(*) > 1 → 0 rows  ✓
SELECT COUNT(*) FROM lesson_proposals WHERE id > 441
  AND entry_id NOT BETWEEN 434 AND 458 → 0  ✓
```

### M5 — Pre-existing triple-set SET-IDENTICAL
```
Pre-flight set (441 rows) == post-commit re-select (441 rows WHERE id <= 441): TRUE  ✓
```

### M6 — Entries unchanged
```
COUNT=458, MAX=458  ✓
```

### M7 — AUTHOR-CONFLICT markers (both directions)
```
(i) entry_ids with AC reasoning in new band:
    {439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458}
    count=20
    entry_ids with entry_date='2026-09-02' in band 434–458:
    {439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458}
    count=20
    SET-IDENTICAL: TRUE  ✓
(ii) new proposals with AC marker but entry NOT dated 2026-09-02 = 0  ✓
```

### M12 — Stale
```
SELECT COUNT(*) FROM lesson_proposals WHERE status='stale' = 3  ✓
```

### M16 — No new duplicate proposals
```
SELECT COUNT(*) FROM lesson_proposals WHERE id > 441 AND category='duplicate' = 0  ✓
```

### M8 — Register sha unchanged
```
shasum -a 256 /Users/marklehn/Developer/eluvian-governance/LESSONS.md
ee0432aeb88a3dfed4e879e12fdae742dec2bd02764fae7db273d9f8557e9e21  ...LESSONS.md
sha-prefix: ee0432aeb88a3dfed4e8  ✓ (byte-unchanged)
```

---

## Summary

| Metric | Expected | Measured | Status |
|---|---|---|---|
| M2 post | [] | [] (count=0) | ✓ |
| M3 total | 441+25=466 | 466 | ✓ |
| M3 accepted | 12 | 12 | ✓ |
| M3 proposed | 25 (K≥25) | 25 | ✓ |
| M4 | 0 | 0 | ✓ |
| M17 dup | 0 rows | 0 rows | ✓ |
| M17 oob | 0 | 0 | ✓ |
| M5 | SET-IDENTICAL | TRUE | ✓ |
| M6 | COUNT=458, MAX=458 | COUNT=458, MAX=458 | ✓ |
| M7 (i) | 20=20 | 20=20 | ✓ |
| M7 (ii) | 0 | 0 | ✓ |
| M12 | 3 | 3 | ✓ |
| M16 | 0 | 0 | ✓ |
| M8 sha | ee0432aeb88a3dfed4e8 | ee0432aeb88a3dfed4e8 | ✓ |
| M15 DISPOSITION lines | 25 | 25 | ✓ |

**Step 2 complete. All metrics pass. One commit issued.**

---

## Output Receipt

**Status: Complete**  
**Deliverable:** `knowledge/development/dev-log-classify-w29-2026-09-02.md`  
**Deliverable:** `knowledge/development/evidence-classify-w29-2026-09-02.txt`  
**Proposals minted:** 442–466 (25 proposals, all governance_rule, route=NULL, status=proposed)  
**AUTHOR-CONFLICT markers:** 20 (entries 439–458, by entry_date='2026-09-02')  
**Commit:** follows after both files written  
