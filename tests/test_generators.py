"""Generated output is a function of its source: the same source gives the same
bytes, and the committed output is what the source gives today."""
import os

import generate_skill
import build_aliases
import build_registry_aliases
import generate_dabt

from conftest import ROOT


def test_dictionary_introduction_survives_generation(tmp_path):
    import generate_dictionary as dictionary
    entries = dictionary.load()
    index = dictionary.Index(entries)
    sources = dictionary.load_sources()
    for locale in (dictionary.AR, dictionary.EN):
        output = tmp_path / (locale["code"] + ".md")
        dictionary.render(entries, dict(locale, out=str(output)), index, sources)
        rendered = output.read_text()
        assert rendered.count('<a id="reading-entries"></a>') == 1
        assert rendered.index('id="reading-entries"') < rendered.index('## ' + locale['lookup_h'])
        assert rendered.count('<a id="contributing"></a>') == 1
        assert '(#contributing)' in rendered
        for entry in entries:
            assert f'<a id="{entry["concept"]}"></a>' in rendered


def test_skill_relinks_reader_and_contributor_pages():
    for source, expected in (
        ('[Read](../dictionary/#reading-entries)', '[Read](dictionary.md#reading-entries)'),
        ('[Contribute](../dictionary/#contributing)', '[Contribute](dictionary.md#contributing)'),
        ('[Read](../reference/dictionary/)', '[Read](dictionary.md)'),
    ):
        assert generate_skill.relink(source) == expected


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
