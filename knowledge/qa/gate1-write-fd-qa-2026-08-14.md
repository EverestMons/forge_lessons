# QA Report — Gate-1 Routing Write for Proposals 347–352 (fold-damage)

**Plan:** `gate1-write-347-352-2026-08-14`
**Date:** 2026-08-14
**Step:** 2 (QA)
**Executor:** QA agent (independent dispatch — Step 1 commit `a6ec776` predates this context)

## Precondition

Step 1 ran as its own dispatch. `git log --oneline -1 -- knowledge/development/g1-fd-route.sql` returns:

```
a6ec776 [416] Step 1 Complete: Gate-1 routing write for proposals 347-352 — 4 accepted|codify (347,348,350,352), 2 reference (349,351), all 12 sentinels exact
```

This commit was made before this QA context began and not by this context. Independence confirmed.

## Deliverable Verification Table

| Item | Check | Result | Raw evidence |
|------|-------|--------|--------------|
| 1 | Deliverables committed (Rule 17) — `git log --oneline -1` for each of 3 paths | ✅ | All three paths resolve to `a6ec776`; porcelain clean (exit=0, no output) |
| 2 | Targeted suite `python3 -m pytest src/ -v` | ✅ | 55 passed in 0.11s (baseline 55; delta 0) |
| 3 | C5 commit shape — single non-amend commit, exactly 3 paths | ✅ | `git show --name-only --format= a6ec776` lists exactly: `knowledge/development/g1-fd-route.sql`, `knowledge/development/gate1-write-fd-dev-2026-08-14.md`, `knowledge/qa/evidence/gate1-write-347-352-2026-08-14/route-capture.txt`; parent count = 1 |
| 4 | C6 standing queue — 340/342/346 `accepted\|codify` with pre-existing stamps | ✅ | `340\|accepted\|codify\|ceo\|2026-08-14T13:21:27Z`, `342\|accepted\|codify\|ceo\|2026-08-14T13:21:27Z`, `346\|accepted\|codify\|ceo\|2026-08-14T13:21:27Z` — stamps `13:21:27Z` differ from this run's `18:38:14Z`; scoping did not leak |
| 5 | C1/C2/C3/C4 write re-verify (POST-COMMIT fresh-connection read) | ✅ | See Item 5 detail below |
| 6 | Corpus preservation — entries=344, proposals=352 | ✅ | `ENTRIES=344`, `PROPOSALS=352` — routing write created no row |
| 7 | Register posture — decisions/ non-Done = this plan only; FORWARD delta ZERO | ✅ | `decisions/` non-Done contents: `in-progress-executable-416.md` + `archived-halted-plans` (standing directory); FORWARD row count = 18 (matches dev note baseline 18; delta 0) |
| 8 | Raw output throughout | ✅ | All commands run foreground; raw output included inline and in `probes-raw.txt` |

## Item 5 Detail — Post-COMMIT Fresh-Connection Read

This re-verify is a POST-COMMIT fresh-connection read and cites no in-transaction sentinel (DC v2.10 §2.7).

### Per-id read-back (347–352)

```
347|accepted|codify|ceo|2026-08-14T18:38:14Z
348|accepted|codify|ceo|2026-08-14T18:38:14Z
349|reference|reference|ceo|2026-08-14T18:38:14Z
350|accepted|codify|ceo|2026-08-14T18:38:14Z
351|reference|reference|ceo|2026-08-14T18:38:14Z
352|accepted|codify|ceo|2026-08-14T18:38:14Z
```

347/348/350/352 → `accepted|codify|ceo|<Z-stamp>` ✓
349/351 → `reference|reference|ceo|<Z-stamp>` ✓

### Aggregate counts

- `ACC=7` with id set `{340,342,346,347,348,350,352}`
- `PROP=0`
- `REF=20` with route split: `REF_ROUTE=14`, `BK_ROUTE=6`; backlog ids = `{161,169,291,294,299,301}` (unchanged)
- `IMPL=279`

### Capture diff

Re-ran the EXACT capture SELECT from `g1-fd-route.sql` line 5:

```sql
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 352 AND id NOT IN (347,348,349,350,351,352) ORDER BY id;
```

Result: 346 lines. `diff` against deposited `route-capture.txt`: **exit 0, no delta**.

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/gate1-write-347-352-2026-08-14/
Files verified: 2
```

