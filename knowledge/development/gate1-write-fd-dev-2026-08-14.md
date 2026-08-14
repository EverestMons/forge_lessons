# Dev Log — Gate-1 Routing Write for Proposals 347–352 (fold-damage)

**Plan:** `gate1-write-347-352-2026-08-14`
**Date:** 2026-08-14
**Step:** 1 (DEV)

## A0 — State Check

All six proposals 347–352: `proposed|NULL|NULL` (FRESH).
Accepted set: {340, 342, 346} — exactly 3.
Re-entry key: no prior commit on `g1-fd-route.sql`.
Branch: **FRESH**.

## E-a — Backup

Backup: `pre-g1fd-20260814_183734.db`
Verification: `BK=6` (file: URI with immutable=1).

## E-a2 — Pre-flight (ROLLBACK-guarded)

```
PRE_A=4
PRE_R=2
ACC=3
MAXID=352
```

All assertions passed.

## E-b — Write Execution

SQL file: `knowledge/development/g1-fd-route.sql`
Runner: `sqlite3 -bail <abs> ".timeout 5000" ".read <abs-sql>"`
Exit: 0, stderr empty.

### Sentinel Set (all twelve, in-transaction)

```
PRE_A=4
PRE_R=2
CHANGES_A=4
CHANGES_R=2
STAMP_A=4
STAMP_R=2
ACC_POST=7
PROP_POST=0
REF_POST=20
IMPL_POST=279
```

Capture: `route-capture.txt` — **346 lines**.

## E-c — Post-COMMIT Read-Back (fresh invocation, ASSERTED)

This is a POST-COMMIT fresh-connection read; it cites no in-transaction sentinel.

```
347|accepted|codify|ceo|2026-08-14T18:38:14Z
348|accepted|codify|ceo|2026-08-14T18:38:14Z
349|reference|reference|ceo|2026-08-14T18:38:14Z
350|accepted|codify|ceo|2026-08-14T18:38:14Z
351|reference|reference|ceo|2026-08-14T18:38:14Z
352|accepted|codify|ceo|2026-08-14T18:38:14Z
```

347/348/350/352 → `accepted|codify|ceo|2026-08-14T18:38:14Z` ✓
349/351 → `reference|reference|ceo|2026-08-14T18:38:14Z` ✓

## Baselines for QA

- FORWARD row count (`grep -c "^| "`): **18**
- Deposits: dev note + SQL + capture (this commit)
- Doctrine: NONE
- LESSONS: NONE
- FORWARD: NONE
