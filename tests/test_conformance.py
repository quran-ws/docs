"""check_conformance.py, rule by rule, on entries built here."""
import check_conformance as cc

SOURCES = {"itqan": {"title": "x"}}
BASE = dict(kind="entity", category="core", origin="standard", tier="core", status="draft",
            names={"code": "x", "display": "X"}, definition="تعريف", definition_en="d",
            purpose="غرض", purpose_en="p")


def problems(**fields):
    entry = {**BASE, "concept": "x", **fields}
    entry["names"] = {**BASE["names"], **fields.get("names", {})}
    return cc.check({"x": entry}, SOURCES)


def has(items, text):
    return any(text in i for i in items)


def test_clean_entry():
    assert problems() == ([], [])


def test_plural_rule():
    assert has(problems(plural="xat")[0], "section 11")


def test_missing_parent():
    assert has(problems(parent="ghost")[0], "has no entry")


def test_value_parent_must_be_classification():
    entries = {"x": {**BASE, "concept": "x", "kind": "classification_value", "parent": "y"},
               "y": {**BASE, "concept": "y", "kind": "concept", "names": {"code": "y"}}}
    assert has(cc.check(entries, SOURCES)[0], "not a classification")


def test_boundaries_line_for_line():
    assert has(problems(boundaries=["a", "b"], boundaries_en=["a"])[0], "line for line")


def test_arabic_left_in_english():
    assert has(problems(definition_en="the آية")[0], "still has Arabic")
    assert not problems(definition_en="the «آية»")[0]


def test_latin_in_arabic_is_a_warning():
    p, w = problems(definition="تعريف Unicode")
    assert not p and has(w, "Latin words")
    assert not problems(definition="تعريف `Unicode` في dataset")[1]


def test_adopted_needs_source():
    assert has(problems(status="adopted")[0], "section 28")


def test_quranic_without_source_warns():
    p, w = problems(origin="quranic", names={"code": "x", "arabic": {"vocalized": "سُورَة"}})
    assert has(w, "no source yet")
    assert has(p, "derives to 'surah'")


def test_unknown_source():
    assert has(problems(sources=[{"id": "nope"}])[0], "not in sources.yml")
    assert not problems(sources=[{"id": "itqan"}])[0]


def test_part_of_must_exist():
    assert has(problems(part_of=["ghost"])[0], "part_of")


def test_drawn_fields_only_on_marks():
    assert has(problems(symbol="۝")[0], "only a mark")
    assert not problems(kind="mark", symbol="۝")[0]


def test_duplicates_in_lists():
    assert has(problems(alternative_spellings=["a", "a"])[0], "more than once")


def test_classification_needs_values():
    assert has(problems(kind="classification")[0], "section 13")
