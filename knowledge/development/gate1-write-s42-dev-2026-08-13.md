# Dev Note — Gate-1 routing write for proposals 337–346 (s42sweep)

**Plan:** `gate1-write-337-346-2026-08-13`
**Date:** 2026-08-14
**Step:** 1 (DEV)

## A0 Determination

**FRESH** — all ten proposals read `proposed|NULL|NULL` (status/route/stamp); deposit paths clean (`git status --porcelain` empty); no prior commit on `g1-s42-route.sql` (`git log --oneline -1` empty).

## Backup

**Path:** `/Users/marklehn/Developer/GitHub/lessons-forge/pre-g1s42-20260814_132031.db`
**Verification (immutable):** `BK=10`

## Pre-flight (Task C)

```
PRE=10
ACC0=0
TOT0=346
```

## Rehearsal (scratch copy)

All twelve sentinels matched targets. Capture: 336 lines. GLOBOK=10 confirms the Z-form representation matches the UPDATE's `strftime` output.

## Live Write Sentinels (Task D)

```
PRE=10
CH_I=3
CH_R=3
CH_A=4
GLOBOK=10
PROP_POST=0
ACC_POST=4
IMPL_POST=278
REF_POST=18
TOT=346
```

Exit code: 0. Stderr: empty. Capture: 336 lines.

## Post-COMMIT Read-back (Task E — fresh connection, read-only)

```
337|implemented|NULL|ceo|2026-08-14T13:21:27Z
338|implemented|NULL|ceo|2026-08-14T13:21:27Z
339|implemented|NULL|ceo|2026-08-14T13:21:27Z
340|accepted|codify|ceo|2026-08-14T13:21:27Z
341|accepted|codify|ceo|2026-08-14T13:21:27Z
342|accepted|codify|ceo|2026-08-14T13:21:27Z
343|reference|reference|ceo|2026-08-14T13:21:27Z
344|reference|reference|ceo|2026-08-14T13:21:27Z
345|reference|reference|ceo|2026-08-14T13:21:27Z
346|accepted|codify|ceo|2026-08-14T13:21:27Z
```

All ten rows match target values. Stamps are Z-form (`2026-08-14T13:21:27Z`). Actor is `ceo` on all ten.

#### Routing record

Three route sets written in one transaction, CEO-authorized (Gate-1 packet `gate1-packet-s42sweep-2026-08-13.md`, DECIDED block at commit `2db9b0e`, owner rider `f6e6b12`):

**I-set (implemented, route NULL) — proposals 337, 338, 339:**
Status set to `implemented`; route left NULL. These three have remedies that shipped BEFORE the proposals existed: 337's remedy is PT v4.88 Rule 85 (plan 389); 338 and 339's remedies are schema v0.3 + `walk_register_lint` guards (plan 392). Because Gate 1 never routed them to a Gate-2 codification plan, setting `route='codify'` would falsely assert they passed through codification. `implemented|NULL` has 89 precedents in the corpus (measured 2026-08-13) and is the honest record. The shipped-remedy evidence is carried in each row's existing `reasoning`/`suggested_action` text from the 399 classifier.

**R-set (reference, route reference) — proposals 343, 344, 345:**
Status set to `reference`; route set to `reference`. Live doctrine already carries each rule (§2.7 proposal-253 / 311 / count-in-prose bullets, each grep-verified present). Route is `reference` not `backlog` because `backlog` marks deferred work, and nothing here is deferred — the rule already exists. The corpus splits `reference` status: 9 `reference` / 6 `backlog` (measured 2026-08-13); these three join the `reference` route set.

**A-set (accepted, route codify) — proposals 340, 341, 342, 346:**
Status set to `accepted`; route set to `codify`. These are measured-uncovered proposals that become the Gate-2 queue of four.

### Ledger Updates

#### Prompt Feedback

No prompt feedback generated during this step.

#### Forward Register

NONE.
