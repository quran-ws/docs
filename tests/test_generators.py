"""Generated output is a function of its source: the same source gives the same
bytes, and the committed output is what the source gives today."""
import os

import generate_skill
import build_aliases
import build_registry_aliases
import generate_dabt

from conftest import ROOT


def test_skill_json_is_stable():
    entries = generate_skill.load()
    a, b = generate_skill.terminology(entries), generate_skill.terminology(entries)
    assert a == b
    assert a["version"]["snapshot"] == b["version"]["snapshot"]
    assert len(a["version"]["snapshot"]) == 16


def test_snapshot_changes_with_inputs(tmp_path, monkeypatch):
    before = generate_skill.content_hash()
    monkeypatch.setattr(generate_skill, "INPUTS", generate_skill.INPUTS + ("tests",))
    assert generate_skill.content_hash() != before


def test_dabt_entries_are_stable():
    assert generate_dabt.build() == generate_dabt.build()


def test_alias_indexes_match_committed():
    import json
    index, clashes = build_aliases.build()
    assert not clashes
    committed = json.load(open(os.path.join(ROOT, "standards/terminology/aliases.json"), encoding="utf-8"))
    assert index == committed
    index, clashes = build_registry_aliases.build()
    assert not clashes
    committed = json.load(open(os.path.join(ROOT, "standards/terminology/registry_aliases.json"), encoding="utf-8"))
    assert index == committed
