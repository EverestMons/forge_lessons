# Gate 1 Routing Dev Log — 2026-08-25

**Plan ID:** 536
**ROOT:** `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/536`
**Transaction timestamp:** `2026-08-25T22:58:03Z`

## A0 — Pre-state pin

```
SELECT COUNT(*), MIN(id), MAX(id) FROM lesson_proposals WHERE status='proposed';
→ 57|354|410
```

Held rows:
```
SELECT id, status, COALESCE(route,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals WHERE id IN (378,389) ORDER BY id;
→ 378|proposed|-|PLANNER_TEMPLATE.md
→ 389|proposed|-|-
```

## A1 — Plan ID and pre-image

Plan path: `/Users/marklehn/Developer/GitHub/bellows/.bellows-cache/executable-536.md.pristine`
Basename: `executable-536.md.pristine`
Regex match: `['536']` → Plan ID: **536**

Pre-image dump: `knowledge/development/gate1-pre-dump-2026-08-25.txt` — 410 lines
Post-image dump: `knowledge/development/gate1-post-dump-2026-08-25.txt` — 410 lines

## B — Transaction script

```python
import sqlite3
from datetime import datetime, timezone

DB_PATH = "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db"

# Compute TS once BEFORE the transaction
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"TRANSACTION TIMESTAMP: {ts}")

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA busy_timeout=5000;")

# BEGIN IMMEDIATE
conn.execute("BEGIN IMMEDIATE;")

try:
    # Statement 1: CODIFY-23
    codify_ids = (354,355,361,364,365,366,368,370,372,373,379,383,384,385,386,387,390,393,395,401,406,407,409)
    placeholders = ",".join("?" * len(codify_ids))
    cur = conn.execute(
        f"UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_by='planner', status_updated_at=? WHERE id IN ({placeholders}) AND status='proposed';",
        (ts,) + codify_ids
    )
    print(f"Statement 1 (codify) rowcount: {cur.rowcount}")
    assert cur.rowcount == 23, f"HALT: codify rowcount {cur.rowcount} != 23"

    # Statement 2: REJECT-23
    reject_ids = (356,357,358,359,362,363,367,374,375,376,377,380,381,382,392,394,396,397,398,399,400,404,410)
    placeholders = ",".join("?" * len(reject_ids))
    cur = conn.execute(
        f"UPDATE lesson_proposals SET status='rejected', status_updated_by='planner', status_updated_at=? WHERE id IN ({placeholders}) AND status='proposed';",
        (ts,) + reject_ids
    )
    print(f"Statement 2 (reject) rowcount: {cur.rowcount}")
    assert cur.rowcount == 23, f"HALT: reject rowcount {cur.rowcount} != 23"

    # Statement 3: REFREF-6
    refref_ids = (388,391,402,403,405,408)
    placeholders = ",".join("?" * len(refref_ids))
    cur = conn.execute(
        f"UPDATE lesson_proposals SET status='reference', route='reference', status_updated_by='planner', status_updated_at=? WHERE id IN ({placeholders}) AND status='proposed';",
        (ts,) + refref_ids
    )
    print(f"Statement 3 (ref/reference) rowcount: {cur.rowcount}")
    assert cur.rowcount == 6, f"HALT: ref/reference rowcount {cur.rowcount} != 6"

    # Statement 4: REFBACK-3
    refback_ids = (360,369,371)
    placeholders = ",".join("?" * len(refback_ids))
    cur = conn.execute(
        f"UPDATE lesson_proposals SET status='reference', route='backlog', status_updated_by='planner', status_updated_at=? WHERE id IN ({placeholders}) AND status='proposed';",
        (ts,) + refback_ids
    )
    print(f"Statement 4 (ref/backlog) rowcount: {cur.rowcount}")
    assert cur.rowcount == 3, f"HALT: ref/backlog rowcount {cur.rowcount} != 3"

    # In-transaction verification
    cur = conn.execute("SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 354 AND 410;")
    proposed_count = cur.fetchone()[0]
    assert proposed_count == 2

    cur = conn.execute("SELECT GROUP_CONCAT(id) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 354 AND 410 ORDER BY id;")
    proposed_ids = cur.fetchone()[0]
    assert proposed_ids == "378,389"

    cur = conn.execute("""
        SELECT status, COALESCE(route,'-'), COUNT(*)
        FROM lesson_proposals WHERE id BETWEEN 354 AND 410
        GROUP BY status, COALESCE(route,'-') ORDER BY status, COALESCE(route,'-');
    """)
    groups = cur.fetchall()
    expected = {('accepted','codify'):23, ('proposed','-'):2, ('reference','backlog'):3, ('reference','reference'):6, ('rejected','-'):23}
    actual = {(g[0],g[1]):g[2] for g in groups}
    assert actual == expected

    conn.commit()
except Exception as e:
    conn.rollback()
    raise
finally:
    conn.close()
```

## B — Rowcounts and in-transaction verification

| Statement | Expected | Actual |
|-----------|----------|--------|
| 1 — codify | 23 | 23 |
| 2 — reject | 23 | 23 |
| 3 — ref/reference | 6 | 6 |
| 4 — ref/backlog | 3 | 3 |

In-transaction posts:
- Proposed count (354–410): **2**
- Proposed ids: **378,389**
- Group counts: `accepted|codify|23`, `proposed|-|2`, `reference|backlog|3`, `reference|reference|6`, `rejected|-|23`

**COMMITTED SUCCESSFULLY**

## C — Post-image diff

Changed rows: **55** (110 changed lines in paired old/new form)
Foreign ids: **0**
Target artifact changes: **0**
Rows 378 and 389: **unchanged**

### RAW diff

```
354,388c354,388
< 354|proposed|-|-|-|DRAFTING_CYCLE.md
< 355|proposed|-|-|-|-
< 356|proposed|-|-|-|-
< 357|proposed|-|-|-|-
< 358|proposed|-|-|-|PLANNER_TEMPLATE.md
< 359|proposed|-|-|-|DRAFTING_CYCLE.md
< 360|proposed|-|-|-|plan_lint.py
< 361|proposed|-|-|-|DRAFTING_CYCLE.md
< 362|proposed|-|-|-|PANEL_SEAT_TEMPLATE.md
< 363|proposed|-|-|-|-
< 364|proposed|-|-|-|-
< 365|proposed|-|-|-|-
< 366|proposed|-|-|-|PLANNER_TEMPLATE.md
< 367|proposed|-|-|-|-
< 368|proposed|-|-|-|-
< 369|proposed|-|-|-|-
< 370|proposed|-|-|-|-
< 371|proposed|-|-|-|-
< 372|proposed|-|-|-|-
< 373|proposed|-|-|-|-
< 374|proposed|-|-|-|DRAFTING_CYCLE.md
< 375|proposed|-|-|-|DRAFTING_CYCLE.md
< 376|proposed|-|-|-|PANEL_SEAT_TEMPLATE.md
< 377|proposed|-|-|-|-
< 378|proposed|-|-|-|PLANNER_TEMPLATE.md
< 379|proposed|-|-|-|DRAFTING_CYCLE.md
< 380|proposed|-|-|-|PLANNER_TEMPLATE.md
< 381|proposed|-|-|-|PLANNER_TEMPLATE.md
< 382|proposed|-|-|-|-
< 383|proposed|-|-|-|DRAFTING_CYCLE.md
< 384|proposed|-|-|-|-
< 385|proposed|-|-|-|PLANNER_TEMPLATE.md
< 386|proposed|-|-|-|PLANNER_TEMPLATE.md
< 387|proposed|-|-|-|-
< 388|proposed|-|-|-|-
---
> 354|accepted|codify|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 355|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 356|rejected|-|planner|2026-08-25T22:58:03Z|-
> 357|rejected|-|planner|2026-08-25T22:58:03Z|-
> 358|rejected|-|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 359|rejected|-|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 360|reference|backlog|planner|2026-08-25T22:58:03Z|plan_lint.py
> 361|accepted|codify|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 362|rejected|-|planner|2026-08-25T22:58:03Z|PANEL_SEAT_TEMPLATE.md
> 363|rejected|-|planner|2026-08-25T22:58:03Z|-
> 364|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 365|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 366|accepted|codify|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 367|rejected|-|planner|2026-08-25T22:58:03Z|-
> 368|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 369|reference|backlog|planner|2026-08-25T22:58:03Z|-
> 370|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 371|reference|backlog|planner|2026-08-25T22:58:03Z|-
> 372|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 373|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 374|rejected|-|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 375|rejected|-|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 376|rejected|-|planner|2026-08-25T22:58:03Z|PANEL_SEAT_TEMPLATE.md
> 377|rejected|-|planner|2026-08-25T22:58:03Z|-
> 378|proposed|-|-|-|PLANNER_TEMPLATE.md
> 379|accepted|codify|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 380|rejected|-|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 381|rejected|-|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 382|rejected|-|planner|2026-08-25T22:58:03Z|-
> 383|accepted|codify|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 384|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 385|accepted|codify|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 386|accepted|codify|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 387|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 388|reference|reference|planner|2026-08-25T22:58:03Z|-
390,410c390,410
< 390|proposed|-|-|-|-
< 391|proposed|-|-|-|-
< 392|proposed|-|-|-|-
< 393|proposed|-|-|-|-
< 394|proposed|-|-|-|PLANNER_TEMPLATE.md
< 395|proposed|-|-|-|-
< 396|proposed|-|-|-|PLANNER_TEMPLATE.md
< 397|proposed|-|-|-|-
< 398|proposed|-|-|-|-
< 399|proposed|-|-|-|DRAFTING_CYCLE.md
< 400|proposed|-|-|-|-
< 401|proposed|-|-|-|-
< 402|proposed|-|-|-|-
< 403|proposed|-|-|-|-
< 404|proposed|-|-|-|-
< 405|proposed|-|-|-|-
< 406|proposed|-|-|-|-
< 407|proposed|-|-|-|PLANNER_TEMPLATE.md
< 408|proposed|-|-|-|-
< 409|proposed|-|-|-|-
< 410|proposed|-|-|-|-
---
> 390|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 391|reference|reference|planner|2026-08-25T22:58:03Z|-
> 392|rejected|-|planner|2026-08-25T22:58:03Z|-
> 393|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 394|rejected|-|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 395|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 396|rejected|-|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 397|rejected|-|planner|2026-08-25T22:58:03Z|-
> 398|rejected|-|planner|2026-08-25T22:58:03Z|-
> 399|rejected|-|planner|2026-08-25T22:58:03Z|DRAFTING_CYCLE.md
> 400|rejected|-|planner|2026-08-25T22:58:03Z|-
> 401|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 402|reference|reference|planner|2026-08-25T22:58:03Z|-
> 403|reference|reference|planner|2026-08-25T22:58:03Z|-
> 404|rejected|-|planner|2026-08-25T22:58:03Z|-
> 405|reference|reference|planner|2026-08-25T22:58:03Z|-
> 406|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 407|accepted|codify|planner|2026-08-25T22:58:03Z|PLANNER_TEMPLATE.md
> 408|reference|reference|planner|2026-08-25T22:58:03Z|-
> 409|accepted|codify|planner|2026-08-25T22:58:03Z|-
> 410|rejected|-|planner|2026-08-25T22:58:03Z|-
```
