"""Tests for scripts/project_status_markers.py — the DB-status → heading-marker projection."""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import project_status_markers as psm  # noqa: E402
from src.lessons_forge import parse_lessons_md, _key_heading  # noqa: E402

DDL = """
CREATE TABLE lesson_entries (
    id INTEGER PRIMARY KEY, source_file TEXT, source_heading TEXT, entry_date TEXT,
    raw_content TEXT, content_hash TEXT, tags TEXT, ingested_at TEXT);
CREATE TABLE lesson_proposals (
    id INTEGER PRIMARY KEY, entry_id INTEGER, category TEXT, status TEXT, route TEXT,
    target_artifact TEXT, duplicate_of INTEGER, suggested_action TEXT,
    proposed_at TEXT, status_updated_at TEXT, status_updated_by TEXT);
"""

LESSONS = """\
# Lessons

---

## 2026-05-01: Old em-dash entry  [tag: a] [status: codified] [target: X.md]

Body one.

---

## 2026-06-01: Learned entry  [tag: b] [status: learned] [target: X.md]

Body two.

---

## 2026-07-01: Bare entry  [tag: c]

Body three.

---

## 2026-08-30: Not ingested yet  [tag: d] [status: pending]

Body four.

---

## 2026-08-31: Stale-then-live  [tag: e] [status: pending]

Body five.
"""


def make_db(path: Path) -> None:
    con = sqlite3.connect(path)
    con.executescript(DDL)
    rows = [
        (1, "2026-05-01 — Old em-dash entry  [tag: a]"),   # old separator style
        (2, "2026-06-01: Learned entry  [tag: b]"),
        (3, "2026-07-01: Bare entry [tag: c]"),             # one space, not two
        (5, "2026-08-31: Stale-then-live  [tag: e]"),
    ]
    con.executemany("INSERT INTO lesson_entries (id, source_file, source_heading) VALUES (?, 'LESSONS.md', ?)", rows)
    con.executemany(
        "INSERT INTO lesson_proposals (id, entry_id, status, route, proposed_at, status_updated_at) VALUES (?,?,?,?,?,?)",
        [
            (10, 1, "reference", "reference", "2026-05-02", "2026-05-03"),
            (11, 2, "implemented", "codify", "2026-06-02", "2026-06-05"),
            (12, 3, "rejected", None, "2026-07-02", "2026-07-03"),
            (13, 5, "stale", None, "2026-08-31", "2026-09-01"),   # newest but stale
            (14, 5, "proposed", None, "2026-08-31", None),        # the live one
        ],
    )
    con.commit()
    con.close()


@pytest.fixture
def setup(tmp_path):
    lessons = tmp_path / "LESSONS.md"
    lessons.write_text(LESSONS, encoding="utf-8")
    db = tmp_path / "corpus.db"
    make_db(db)
    return lessons, db


def markers(path: Path) -> list[str]:
    import re
    out = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("## 20"):
            m = re.search(r"\[status:\s*([a-z-]+)\]", line)
            out.append(m.group(1) if m else "NONE")
    return out


def test_projects_db_status_replacing_or_appending_marker(setup):
    lessons, db = setup
    rc = psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    assert rc == 0
    assert markers(lessons) == ["reference", "implemented", "rejected", "pending", "proposed"]


def test_stale_proposal_is_ignored_when_a_live_one_exists(setup):
    lessons, db = setup
    psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    assert markers(lessons)[4] == "proposed"


def test_unmatched_entry_is_left_alone_by_default(setup):
    lessons, db = setup
    psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    assert markers(lessons)[3] == "pending"
    assert "## 2026-08-30: Not ingested yet  [tag: d] [status: pending]" in lessons.read_text()


def test_edit_is_key_and_hash_transparent(setup):
    lessons, db = setup
    before = parse_lessons_md(str(lessons))
    psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    after = parse_lessons_md(str(lessons))
    assert [_key_heading(e["source_heading"]) for e in before] == [_key_heading(e["source_heading"]) for e in after]
    assert [e["content_hash"] for e in before] == [e["content_hash"] for e in after]


def test_dry_run_writes_nothing_and_second_apply_is_idempotent(setup):
    lessons, db = setup
    original = lessons.read_text()
    assert psm.main(["--db", str(db), "--lessons", str(lessons)]) == 0
    assert lessons.read_text() == original
    psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    once = lessons.read_text()
    psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"])
    assert lessons.read_text() == once


def test_zero_byte_db_is_refused_as_a_decoy(setup):
    lessons, db = setup
    decoy = db.parent / "decoy.db"
    decoy.write_bytes(b"")
    assert psm.main(["--db", str(decoy), "--lessons", str(lessons)]) == 3


def test_refuses_when_a_proof_fails(setup, monkeypatch):
    lessons, db = setup
    monkeypatch.setattr(psm, "prove_inert", lambda *a, **k: ["forced failure"])
    original = lessons.read_text()
    assert psm.main(["--db", str(db), "--lessons", str(lessons), "--apply"]) == 2
    assert lessons.read_text() == original


def test_snapshot_loader_decodes_unistr(tmp_path):
    sql = tmp_path / "snap.sql"
    sql.write_text(DDL + "INSERT INTO lesson_entries (id, source_file, source_heading) VALUES (1,'LESSONS.md',unistr('2026-05-01: caf\\u00e9  [tag: a]'));\n")
    path = psm.load_snapshot(str(sql))
    con = sqlite3.connect(path)
    assert con.execute("select source_heading from lesson_entries").fetchone()[0] == "2026-05-01: café  [tag: a]"


def test_discovery_uses_env_and_skips_zero_byte_candidates(setup, monkeypatch, tmp_path):
    lessons, db = setup
    decoy = tmp_path / "decoy.db"
    decoy.write_bytes(b"")
    monkeypatch.setattr(psm, "DB_CANDIDATES", [decoy, db])
    monkeypatch.delenv("LESSONS_FORGE_DB", raising=False)
    assert psm.discover_db() == db
    monkeypatch.setenv("ELUVIAN_WRAP_ROOT", str(lessons.parent))
    assert psm.discover_lessons() == lessons
    assert psm.main(["--apply"]) == 0
    assert markers(lessons) == ["reference", "implemented", "rejected", "pending", "proposed"]


def test_no_db_anywhere_exits_3(setup, monkeypatch, tmp_path):
    lessons, db = setup
    monkeypatch.setattr(psm, "DB_CANDIDATES", [tmp_path / "absent.db"])
    monkeypatch.delenv("LESSONS_FORGE_DB", raising=False)
    assert psm.main(["--lessons", str(lessons)]) == 3
