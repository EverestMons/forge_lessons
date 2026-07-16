# Hash Normalization Fix — Step 1 Dev Log (Plan 204)

**Date:** 2026-07-16
**Plan:** 204 — Fix whitespace-only hash flips silently staling implemented proposals
**Step:** 1 (DEV — code only, no DB mutation)

## Task A — Normalize the hash input

### Normalization rule

`_normalize_for_hash(raw_content: str) -> str` strips from the tail of the body:
1. Empty/whitespace-only lines
2. Lines matching `^[ \t]*-{3,}[ \t]*$` (markdown horizontal-rule separators)

Repeated until the body ends in real content. The function operates on a **copy** — `raw_content` is stored verbatim and unnormalized in `lesson_entries.raw_content`.

### Why this is safe against real edits

The normalization only removes trailing artifacts that `parse_lessons_md` passively inherits from the next entry's separator. A substantive edit anywhere in the body — even at the very end — changes the normalized form and the hash. Test `test_hash_substantive_edit_changes_hash` asserts this directly. The separator pattern (`---` with optional whitespace) never appears in real lesson prose; it is exclusively a markdown section divider.

### Implementation

- New regex: `_TRAILING_SEPARATOR_RE = re.compile(r"^[ \t]*-{3,}[ \t]*$")`
- `_normalize_for_hash()` added as module-level helper in `src/lessons_forge.py`
- Hash computation in `_flush()` inside `parse_lessons_md` changed from `hashlib.sha256(raw_content.encode("utf-8"))` to `hashlib.sha256(_normalize_for_hash(raw_content).encode("utf-8"))`

## Task B — Terminal-status guard

### Guard rule

`_TERMINAL_STATUSES = frozenset(('implemented', 'rejected', 'superseded', 'reference'))`

The stale UPDATE in `ingest_lesson_entries` now excludes terminal statuses:
```sql
WHERE entry_id = ? AND status != 'stale' AND status NOT IN ('implemented','reference','rejected','superseded')
```

When a genuinely changed entry carries terminal-status proposals, those proposals are collected into `terminal_proposals_flagged` (list of `{entry_id, proposal_id, status}` dicts) and surfaced through `run_full_lessons_cycle`'s return dict. This ensures no CEO disposition is silently undone.

## Tests added

| # | Test name | What it asserts |
|---|---|---|
| 1 | `test_hash_trailing_separator_invariant` | Body ± trailing `\n---\n\n` produces identical hash |
| 2 | `test_hash_substantive_edit_changes_hash` | Real edit still changes hash |
| 3 | `test_raw_content_stored_verbatim_with_separator` | `raw_content` retains trailing separator |
| 4 | `test_terminal_status_guard[implemented/rejected/superseded/reference]` | Terminal proposals stay, appear in `terminal_proposals_flagged` |
| 5 | `test_nonterminal_still_stales` | `proposed` proposal still staled on genuine edit |
| 6 | `test_trailing_separator_only_delta_zero_stales` | Separator-only delta: `updated == 0`, zero stales |

## Self-verification

```
$ python3 -m pytest src/test_lessons_forge.py -v -k "hash or ingest or parse or stale or normal or terminal or separator or substantive or verbatim"

18 passed, 43 deselected in 0.18s
```

All 18 targeted tests passed. No regressions in existing parse/ingest/stale tests.

## Commit

`eb90935` — `fix: normalize hash input to prevent whitespace-only separator flips + guard terminal statuses [204]`

## Output Receipt

| Field | Value |
|---|---|
| Status | **Complete** |
| Plan | 204 Step 1 |
| Files changed | `src/lessons_forge.py`, `src/test_lessons_forge.py` |
| Commit | `eb90935` |
| Tests | 18 targeted passed, 0 failures |
| DB touched | No (code-only step) |

### Ledger Updates

#### Prompt Feedback

None — execution followed plan precisely.
