# CLAUDE.md

## Execution Protocol (Eluvian Standard)

This project follows the Eluvian execution protocol defined in `PLANNER_TEMPLATE.md § Execution Model`. The full specification for RUN EXE, RUN DIAG, execution claiming (`in-progress-` prefix), cross-plan dependencies, and priority ordering lives there. Key points repeated here for agent convenience:

### RUN EXE
Scan `knowledge/decisions/` for `executable-` files. Skip `in-progress-` and `Done/`. **BEFORE executing, RENAME the file:**
```python
import shutil
shutil.move("knowledge/decisions/executable-foo.md", "knowledge/decisions/in-progress-executable-foo.md")
```
Execute Step 1, wait for CEO confirmation ("ok") before proceeding to Step 2. Continue step by step. After the final step completes, move to Done (strip prefix), then scan for next executable. If no more executables: **"NO EXE"**.

### RUN DIAG
Scan `knowledge/decisions/` for `diagnostic-` files. Skip `in-progress-` and `Done/`. **BEFORE executing, RENAME the file:**
```python
import shutil
shutil.move("knowledge/decisions/diagnostic-foo.md", "knowledge/decisions/in-progress-diagnostic-foo.md")
```
Execute investigation, deposit findings to `knowledge/research/`. Move to Done (strip prefix). If no more diagnostics: **"NO DIAG"** and stop. Do NOT scan for executables. RUN DIAG only cares about diagnostics.

### Claiming + Dependencies
- `in-progress-` prefix = claimed by another session, SKIP IT
- `**Depends on:**` header field = check `Done/` for prerequisites before executing
- `**Priority:**` header field = lower number runs first
- Stale `in-progress-` files (>30 min unmodified) may be reclaimed

---

## Database Files

`lessons-forge.db` is local operational state, untracked as of 2026-06-12 (shop policy). The `-shm` and `-wal` companions are never committed.

**Home (CEO decision 2026-09-01): the Mac mini**, at `<repo>/lessons-forge.db` — the same host as the tuyere production database. There is exactly ONE live copy; every other checkout is database-less. Migrated 2026-09-01 from the shop MacBook by restoring `knowledge/research/corpus-snapshot-2026-09-01.sql` and proving equality with `scripts/fingerprint_db.py` (row-level SHA-256 over both tables, identical on both machines: `9d9fa77d…5330`). Snapshots deposited under `knowledge/research/` are the backup channel. Every path default resolves through `src/paths.py` (`ELUVIAN_WRAP_ROOT`, `LESSONS_FORGE_DB` override); nothing names a machine layout literally. A 0-byte `.db` at any candidate path is a decoy from a misdirected `sqlite3` call — delete it.
