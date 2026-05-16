# diagnostic — Bellows watch canary for lessons-forge (Phase B.2 verification)

**Plan ID:** diagnostic-bellows-watch-canary-lessons-forge-2026-05-18
**Date:** 2026-05-18
**Project:** lessons-forge
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Priority:** 1
**Depends on:** none
**auto_close:** false

## Context

Phase B.2 added `lessons-forge/knowledge/decisions/` to the bellows watched_projects list and restarted the daemon. This canary verifies end-to-end dispatch on the new watch.

## STEP 1 — Echo + capture cwd + count watched projects

**Agent:** Developer

Single step. Three trivial mechanical actions, all reported in the Output Receipt's Flags for CEO field.

### Action

```bash
echo "Canary hello from lessons-forge submodule"
python3 -c "import os; print(f'cwd={os.getcwd()}')"
python3 -c "import json; cfg=json.load(open('/Users/marklehn/Developer/GitHub/bellows/config.json')); print(f'watched_count={len(cfg[\"watched_projects\"])}'); print(f'lessons_forge_watched={any(\"lessons-forge\" in p for p in cfg[\"watched_projects\"])}')"
```

### Deposits
- `knowledge/research/canary-lessons-forge-bellows-watch-2026-05-18.md` (canary findings: cwd, watched_count, lessons_forge_watched flag)

### Output Receipt requirements

Flags for CEO field MUST report verbatim:
- `cwd=<full path>` (literal, not paraphrased)
- `watched_count=<integer>`
- `lessons_forge_watched=<True|False>`
