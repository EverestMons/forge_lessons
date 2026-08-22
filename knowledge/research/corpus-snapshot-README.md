# Corpus snapshots — why these exist

`lessons-forge.db` is **untracked by shop policy** (`CLAUDE.md`, since 2026-06-12). Diagnostic-498 (2026-08-21) established what that costs:

- The **file** (`LESSONS.md`) is the system of record for entry CONTENT.
- The **DB** is the system of record for ROUTING AND STATUS — and nothing else can reconstruct it.

Re-ingesting `LESSONS.md` would recreate `lesson_entries` but lose all **378 proposals**, including **284 status decisions made by the CEO** over four months. It would also not recover the **57 entries** that exist only in the DB, having been removed from `LESSONS.md` during the pre-2026-05-18 heading-format era.

A snapshot is therefore a `.dump` of the WHOLE database, not just the proposals table.

## Restoring

```bash
sqlite3 /path/to/restored.db < corpus-snapshot-YYYY-MM-DD.sql
```

Verify with the counts recorded in the snapshot's commit message.

## When to snapshot

Before any executable that MUTATES the corpus DB — in particular the taxonomy extension (adding CODE / glossary / CLAUDE.md / DELETE rungs to `target_layer`) and any annotation pass that writes back proposal state.

⚠️ Each snapshot is ~1.2 MB of SQL. These are point-in-time recovery artifacts, not a version history — do not take one per session. Take one before a mutation, and prune superseded ones once a newer snapshot has been verified to restore.
