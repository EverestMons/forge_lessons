# Dev Log: forge-project-marker-strip — 2026-08-26

## Anchor Probes

- **Arm probe** (`/usr/bin/grep -cF "status|target|project" src/lessons_forge.py`): 0 before edit (confirmed count-1 of original `status|target` pattern at line 52)
- **Test probe** (`/usr/bin/grep -cF "test_key_heading_strips_project_marker" src/test_lessons_forge.py`): 0 before edit
- State: (0,0) — full run

## Changes

**Task B — the arm:** `_STATUS_TARGET_MARKER_RE` alternation widened from `(?:status|target)` to `(?:status|target|project)` at `src/lessons_forge.py:52`.

**Task C — two tests:** appended after `test_key_heading_preserves_tag_markers` in `src/test_lessons_forge.py`:
- `test_key_heading_strips_project_marker` — single and multi-value `[project:]` stripped, `[tag:]` preserved
- `test_key_heading_strips_project_with_status_and_target` — `[project:]` composes with `[status:]` and `[target:]` in any order

## Targeted Run Output

```
........                                                                 [100%]
8 passed, 57 deselected in 0.05s
```

8 passed (all `key_heading` tests), 0 failed. Plan predicted 4 (2 existing + 2 new); the `-k "key_heading"` filter matches 8 tests total — yours supersede per Numbers discipline.
