# QA Report — Gate-1 routing write for proposals 333–336

**Plan:** executable-384 (gate1-write-333-336-2026-08-13)
**Date:** 2026-08-13
**Step:** 2 (QA)

## Deliverable Verification

| # | Check | Expected | Observed | Status |
|---|-------|----------|----------|--------|
| 1 | Routes landed: 333–336 `accepted\|codify\|ceo` Z-stamped | 4 rows `accepted\|codify\|ceo\|<Z>` | 333 `accepted\|codify\|ceo\|2026-08-13T17:21:10Z`, 334 same, 335 same, 336 same; diff vs deposited readback: EMPTY | ✅ |
| 2 | Blast radius: outside-range capture unchanged | 332 lines, diff empty | 332 lines, diff vs deposited: EMPTY; no impossible-id, no deleted-row, no concurrent change | ✅ |
| 3 | Corpus: `accepted\|codify`=4, `proposed`=0, `reference` STATUS=15 (9 ref + 6 backlog), `stale`=3 (98/121/130), `implemented`=271, total=336 | All counts match | ACCEPTED_CODIFY=4, PROPOSED=0, REFERENCE_STATUS=15, REFERENCE_ROUTE=9, BACKLOG_ROUTE=6, STALE=3 (98,121,130), IMPLEMENTED=271, TOTAL=336, BACKLOG_IDS=161,169,291,294,299,301 | ✅ |
| 4 | Tests: single module, pytest foreground, baseline 55/0 | 55 passed, 0 failed | 55 passed, 0 failed; delta 0; exactly 1 test file found | ✅ |
| 5 | Consumer semantics: `get_unclassified_entries`=`[]`; entries 325–328 present; entry-324 hash intact | `[]`, 4 present, hash `04d2bff7...` | UNCLASSIFIED=[], 325–328 all present, ENTRY324_HASH=04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a | ✅ |

**Verdict:** All 5 rows ✅. No ❌.

## Evidence and Narrative

All five QA checks passed with exact matches to plan-specified expected values.

**Row 1:** Fresh readback query re-run independently confirms all four proposals (333, 334, 335, 336) carry `accepted|codify|ceo` with Z-format timestamp `2026-08-13T17:21:10Z`. Byte-for-byte diff against the Step 1 deposited `routing-readback.txt` is empty.

**Row 2:** The exact capture SELECT from G2 (the `outside-range-ids` query) was re-run read-only. Output is 332 lines. Diff against the Step 1 deposited `outside-range-ids.txt` is empty. No impossible ids (>336 in range), no deleted rows, no concurrent mutations detected.

**Row 3:** All corpus shape counts match the plan's expected values exactly. The route split guard (9 `reference` + 6 `backlog` = 15 `reference` STATUS) is unchanged. The six backlog ids (161, 169, 291, 294, 299, 301) match. The three stale ids (98, 121, 130) match.

**Row 4:** `find` discovered exactly one test file (`src/test_lessons_forge.py`). Pytest ran foreground: 55 passed, 0 failed. Baseline was 55/0; delta is 0.

**Row 5:** `get_unclassified_entries(conn)` returns `[]` — routing does not un-classify. The four source entries 325–328 are present and unchanged. The sentinel entry-324 content_hash `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` is intact.

**Receipt:** Step 2 QA complete. All five verification rows pass. Sentinels from Step 1 confirmed: PRE=4, BK=4, CHANGES_A=4, GLOBOK_A=4, capture=332 lines. Evidence deposited to `knowledge/qa/evidence/gate1-write-333-336-2026-08-13/`.

### Ledger Updates

#### Prompt Feedback

NONE

#### Forward Register

NONE
