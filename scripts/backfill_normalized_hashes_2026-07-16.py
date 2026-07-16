#!/usr/bin/env python3
"""Backfill content_hash in lesson_entries using normalized hashing (plan 204 Step 2).

Re-hashes currently-parsed LESSONS.md entries via _normalize_for_hash so the
stored hashes match what the fixed parser now produces. Updates content_hash
ONLY — never touches lesson_proposals or raw_content.
"""
import os
import sqlite3
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lessons_forge import parse_lessons_md, _normalize_for_hash
import hashlib

CANONICAL_DB = "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db"
LESSONS_MD = "/Users/marklehn/Developer/GitHub/LESSONS.md"


def main():
    conn = sqlite3.connect(CANONICAL_DB)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")

    # Snapshot proposal status distribution BEFORE
    before_dist = dict(conn.execute(
        "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status"
    ).fetchall())
    print(f"Proposal status distribution BEFORE: {before_dist}")

    # Parse current LESSONS.md
    entries = parse_lessons_md(LESSONS_MD)
    print(f"Parsed {len(entries)} entries from LESSONS.md")

    # Backfill: match by source_heading, recompute hash, update if changed
    updated = 0
    unchanged = 0
    not_found = 0

    for entry in entries:
        row = conn.execute(
            "SELECT id, content_hash FROM lesson_entries "
            "WHERE source_file = 'LESSONS.md' AND source_heading = ?",
            (entry["source_heading"],),
        ).fetchone()

        if row is None:
            not_found += 1
            print(f"  WARNING: no DB row for heading: {entry['source_heading'][:60]}")
            continue

        db_id, stored_hash = row
        normalized = _normalize_for_hash(entry["raw_content"])
        new_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

        if stored_hash == new_hash:
            unchanged += 1
        else:
            conn.execute(
                "UPDATE lesson_entries SET content_hash = ? WHERE id = ?",
                (new_hash, db_id),
            )
            updated += 1

    conn.commit()

    print(f"\nBackfill results: updated={updated}, unchanged={unchanged}, not_found={not_found}")

    # Snapshot proposal status distribution AFTER
    after_dist = dict(conn.execute(
        "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status"
    ).fetchall())
    print(f"Proposal status distribution AFTER:  {after_dist}")

    # Assert distributions are identical
    assert before_dist == after_dist, (
        f"CRITICAL: proposal distributions changed!\n"
        f"  BEFORE: {before_dist}\n"
        f"  AFTER:  {after_dist}"
    )
    print("ASSERTION PASSED: proposal status distribution unchanged.")

    # Verify no lesson_proposals statements were issued (structural — this script
    # only issues SELECT against lesson_proposals, never UPDATE/INSERT/DELETE)

    # Idempotency check: re-run should report 0 changes
    re_updated = 0
    for entry in entries:
        row = conn.execute(
            "SELECT id, content_hash FROM lesson_entries "
            "WHERE source_file = 'LESSONS.md' AND source_heading = ?",
            (entry["source_heading"],),
        ).fetchone()
        if row is None:
            continue
        db_id, stored_hash = row
        normalized = _normalize_for_hash(entry["raw_content"])
        new_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        if stored_hash != new_hash:
            re_updated += 1

    print(f"\nIdempotency check: {re_updated} rows would change on re-run")
    assert re_updated == 0, f"NOT IDEMPOTENT: {re_updated} rows would change on re-run"
    print("ASSERTION PASSED: backfill is idempotent.")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
