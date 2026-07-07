"""Lessons Forge — DB initialization for lessons-forge.db."""
from __future__ import annotations

import sqlite3


def init_db(conn: sqlite3.Connection) -> None:
    """Create lesson_entries and lesson_proposals tables with indexes."""
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")

    conn.executescript("""
        CREATE TABLE IF NOT EXISTS lesson_entries (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file     TEXT    NOT NULL,
            source_heading  TEXT    NOT NULL,
            entry_date      TEXT,
            raw_content     TEXT    NOT NULL,
            content_hash    TEXT    NOT NULL,
            tags            TEXT,
            ingested_at     TEXT    NOT NULL,
            UNIQUE(source_file, source_heading)
        );

        CREATE INDEX IF NOT EXISTS idx_lesson_entries_source
            ON lesson_entries(source_file);
        CREATE INDEX IF NOT EXISTS idx_lesson_entries_date
            ON lesson_entries(entry_date);
        CREATE INDEX IF NOT EXISTS idx_lesson_entries_hash
            ON lesson_entries(content_hash);

        CREATE TABLE IF NOT EXISTS lesson_proposals (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
            category            TEXT    NOT NULL CHECK(category IN ('structural', 'instrumentation', 'governance_rule', 'language', 'narrative', 'duplicate')),
            subcategory         TEXT,
            suggested_action    TEXT    NOT NULL,
            reasoning           TEXT    NOT NULL,
            confidence          TEXT    NOT NULL CHECK(confidence IN ('low', 'medium', 'high')),
            status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')),
            target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure', 'governance', 'language', 'none')),
            target_artifact     TEXT,
            duplicate_of        INTEGER,
            route               TEXT    CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference')),
            proposed_at         TEXT    NOT NULL,
            status_updated_at   TEXT,
            status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))
        );

        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_entry
            ON lesson_proposals(entry_id);
        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_status
            ON lesson_proposals(status);
        CREATE INDEX IF NOT EXISTS idx_lesson_proposals_category
            ON lesson_proposals(category);
    """)

    # Migration: add route column to existing DBs that lack it
    cols = {row[1] for row in conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()}
    if "route" not in cols:
        conn.execute(
            "ALTER TABLE lesson_proposals ADD COLUMN "
            "route TEXT CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference'))"
        )

    conn.commit()
