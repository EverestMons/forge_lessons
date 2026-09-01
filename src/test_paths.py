"""Tests for src/paths.py — layout-independent resolution of the forge's inputs."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import paths  # noqa: E402


def test_env_root_wins(tmp_path, monkeypatch):
    (tmp_path / "LESSONS.md").write_text("# x\n")
    monkeypatch.setenv("ELUVIAN_WRAP_ROOT", str(tmp_path))
    assert paths.governance_root() == tmp_path
    assert paths.lessons_md() == tmp_path / "LESSONS.md"
    assert paths.planner_template() == tmp_path / "PLANNER_TEMPLATE.md"


def test_mini_layout_sibling_governance(tmp_path, monkeypatch):
    dev = tmp_path / "Developer"
    (dev / "eluvian-governance").mkdir(parents=True)
    (dev / "eluvian-governance" / "LESSONS.md").write_text("# x\n")
    (dev / "forge_lessons").mkdir()
    monkeypatch.delenv("ELUVIAN_WRAP_ROOT", raising=False)
    monkeypatch.setattr(paths, "REPO", dev / "forge_lessons")
    assert paths.governance_root() == dev / "eluvian-governance"


def test_shop_layout_parent_root(tmp_path, monkeypatch):
    gh = tmp_path / "GitHub"
    (gh / "lessons-forge").mkdir(parents=True)
    (gh / "LESSONS.md").write_text("# x\n")
    (gh / "bellows").mkdir()
    monkeypatch.delenv("ELUVIAN_WRAP_ROOT", raising=False)
    monkeypatch.setattr(paths, "REPO", gh / "lessons-forge")
    assert paths.governance_root() == gh
    assert paths.artifact_roots() == [gh, gh / "bellows"]


def test_db_path_skips_decoys_and_honors_env(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    (repo / "data").mkdir(parents=True)
    (repo / "lessons-forge.db").write_bytes(b"")          # decoy
    (repo / "data" / "lessons-forge.db").write_bytes(b"x")
    monkeypatch.setattr(paths, "REPO", repo)
    monkeypatch.delenv("LESSONS_FORGE_DB", raising=False)
    assert paths.db_path() == repo / "data" / "lessons-forge.db"
    other = tmp_path / "elsewhere.db"
    other.write_bytes(b"x")
    monkeypatch.setenv("LESSONS_FORGE_DB", str(other))
    assert paths.db_path() == other


def test_nothing_found_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "REPO", tmp_path / "nowhere" / "repo")
    monkeypatch.delenv("ELUVIAN_WRAP_ROOT", raising=False)
    monkeypatch.delenv("LESSONS_FORGE_DB", raising=False)
    assert paths.governance_root() is None
    assert paths.lessons_md() is None
    assert paths.db_path() is None
    assert paths.artifact_roots() == []
