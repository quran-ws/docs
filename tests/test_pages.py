"""The guideline pages are data, and the Arabic never falls silently behind.

`content/pages/<page>.yml` is the source of each guideline page. These tests
say that every page file is well-formed, that the rendered Markdown is what the
generator produces from it, and that every Arabic field still translates the
English it was stamped against.
"""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import generate_pages as gp  # noqa: E402

PAGES = gp.load_pages()
STAMPS = gp.load_stamps()


def test_every_page_is_well_formed():
    problems = [p for name, page in PAGES.items() for p in gp.validate(name, page)]
    assert not problems, "\n".join(problems)


@pytest.mark.parametrize("name", sorted(PAGES))
def test_rendered_english_matches_the_source(name):
    path = os.path.join(gp.OUT["en"], f"{name}.md")
    assert os.path.exists(path), f"content/en/{name}.md is not rendered; run tools/generate_pages.py"
    assert open(path, encoding="utf-8").read() == gp.render(name, PAGES[name], "en")


@pytest.mark.parametrize("name", sorted(PAGES))
def test_rendered_arabic_matches_the_source(name):
    """An Arabic page exists exactly when its rule file is fully translated."""
    _, missing = gp.arabic_present(PAGES[name])
    path = os.path.join(gp.OUT["ar"], f"{name}.md")
    if missing:
        assert not os.path.exists(path), (f"content/ar/{name}.md exists but {len(missing)} units "
                                          f"are untranslated: {', '.join(missing)}")
    else:
        assert os.path.exists(path), f"content/ar/{name}.md is not rendered; run tools/generate_pages.py"
        assert open(path, encoding="utf-8").read() == gp.render(name, PAGES[name], "ar")


@pytest.mark.parametrize("name", sorted(PAGES))
def test_arabic_is_current(name):
    """Every Arabic unit was stamped against the English it now sits beside."""
    units = gp.english_units(PAGES[name])
    present, _ = gp.arabic_present(PAGES[name])
    stamped = STAMPS.get(name, {})
    stale = sorted(k for k in present if stamped.get(k) != units[k])
    assert not stale, (f"{name}: the English changed after the Arabic of {', '.join(stale)} was "
                       f"written. Revise the Arabic, then `python3 tools/generate_pages.py --stamp {name}`")


def test_rule_ids_are_unique_across_pages():
    seen = {}
    for name, page in PAGES.items():
        for section in page["sections"]:
            for rule in section["rules"]:
                assert rule["id"] not in seen, f"{rule['id']} is in both {seen[rule['id']]} and {name}"
                seen[rule["id"]] = name
