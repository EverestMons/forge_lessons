# Dev Log — Cycle Step 1 (Ingest) — 2026-08-07

**Plan:** executable-311
**Step:** 1 — Lessons Agent (ingest the whole corpus; no classification)
**Date:** 2026-08-07
**Dispatch determination:** FRESH — probe (i) exit 128 (not in HEAD), probe (ii) exit 1 (not in working tree), probe (iii) empty output with positive control confirmed (knowledge/FORWARD.md returned 5 commits), no bellows-preserved branches.

Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)

#### Pre-cycle baseline

**E0=214**
**P0=222**
sqlite_sequence agreement: E0_SEQ=214, P0_SEQ=222 (no gap)

**Backup (pristine, pre-cycle):** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-311-20260808T015514Z.db`
Backup integrity: ok
Backup counts: BK_ENTRIES=214, BK_PROPOSALS=222 (match live)

**Status distribution (zero-emitting):**
```
accepted|0
ambiguous|0
duplicate|0
implemented|169
proposed|0
reference|7
rejected|15
stale|3
superseded|28
```

**Category distribution:**
```
governance_rule|177
duplicate|19
instrumentation|11
structural|10
narrative|5
```

**Entry count:** 214
**Proposal count:** 222

**Sentinel — entry 214:**
content_hash=0017ec873912a6c75e3fb61f50b02813a3216c2c26356a02bcdf77d278987ae2

**STALE_COUNT=3**

#### NT (non-terminal set)

```
(empty — zero rows returned)
```

NT_COUNT=0

#### Doctrine pins

```
7cc27a3aac5b71393d09ab8d9690f27cf295dbadfb61912d1c3f9411c6aa42a3  /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md
807f6cd91065c78bce5b422cbf4e2f9d026d7cbda144597d040c7ffb05bdd6d1  /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md
d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0  /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md
```

#### Single-writer check

get_unclassified_entries: READ1=0, READ2=0, STABLE=True (pre-ingest; expected empty)
in-progress glob: 1 match — in-progress-executable-311.md (this plan's own file; normal state under bellows dispatch)
