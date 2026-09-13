"""The Arabic standard preserves structured rules and their stable links."""
from copy import deepcopy

import pytest

import generate_standard as standard
import check_examples


@pytest.fixture
def page():
    return {
        "title": "المعيار", "description": "وصف المعيار", "intro": "مقدمة",
        "status": "draft", "order": 1,
        "rules": [{"id": "005", "category": "الترجمة", "name": "ترتيب الصفة",
                   "description": "تسبق الصفة الاسم.", "examples": ["`small_meem`"]}],
    }


@pytest.mark.parametrize("field", sorted(standard.RULE_FIELDS))
def test_missing_rule_field_is_rejected(page, field):
    del page["rules"][0][field]
    assert standard.validate(page)


@pytest.mark.parametrize("rid", [5, "5", "05", "0005", "٠٠٥", None])
def test_id_requires_three_ascii_digits_as_text(page, rid):
    page["rules"][0]["id"] = rid
    assert any("three-digit" in error for error in standard.validate(page))


def test_duplicate_id_is_rejected(page):
    page["rules"].append(deepcopy(page["rules"][0]))
    assert any("duplicate" in error for error in standard.validate(page))


@pytest.mark.parametrize("examples", [[], "example", [""], [None], ["   "]])
def test_empty_or_malformed_examples_are_rejected(page, examples):
    page["rules"][0]["examples"] = examples
    assert any("examples" in error for error in standard.validate(page))


def test_unknown_rule_link_is_rejected(page):
    page["rules"][0]["description"] += " [قاعدة](#rule-999)"
    assert any("unknown rule 999" in error for error in standard.validate(page))


def test_reordering_preserves_rule_links_and_example_text(page):
    second = dict(page["rules"][0], id="019", category="التهجئة")
    page["rules"].append(second)
    before = standard.render(page)
    page["rules"].reverse()
    after = standard.render(page)
    for rid in ("005", "019"):
        assert f'id="rule-{rid}"' in before and f'id="rule-{rid}"' in after
    assert after.index("### 019.") < after.index("### 005.")
    assert "\n\n`small_meem`\n" in after


def test_example_tables_code_and_prose_remain_separate_blocks(page):
    table = "| الاسم | الصيغة |\n| --- | --- |\n| الميم | `meem` |"
    code = "```text\nayah_key = surah_number:ayah_number\n2:255\n```"
    note = "توضيح بعد المثال."
    page["rules"][0]["examples"] = [table, code, note]
    rendered = standard.render(page)
    assert table + "\n\n" + code + "\n\n" + note + "\n" in rendered
    assert "\n- |" not in rendered
    assert "\n- ```" not in rendered


def test_source_is_valid_and_generated_page_is_current():
    assert not standard.check()
    page = standard.load()
    assert standard.render(page) == standard.render(page)


def test_check_detects_stale_output_without_rewriting(tmp_path, monkeypatch, page):
    output = tmp_path / "standard.md"
    output.write_text("old page", encoding="utf-8")
    monkeypatch.setattr(standard, "OUTPUT", output)
    monkeypatch.setattr(standard, "load", lambda: page)
    assert any("stale" in error for error in standard.check())
    assert output.read_text(encoding="utf-8") == "old page"


def test_structured_arabic_and_legacy_english_are_checked_separately():
    limit, problems = check_examples.section_counts()
    assert not problems
    assert limit == 31
    assert not check_examples.check_rule_references()


def test_legacy_section_validation_still_rejects_invalid_references(tmp_path, monkeypatch):
    prose = tmp_path / "old.md"
    prose.write_text("section 32", encoding="utf-8")
    monkeypatch.setattr(check_examples, "reference_files", lambda: iter([str(prose)]))
    assert check_examples.check_section_references(31)


def test_new_rule_validation_rejects_invalid_references(tmp_path, monkeypatch):
    prose = tmp_path / "new.md"
    prose.write_text("[rule](#rule-999)", encoding="utf-8")
    monkeypatch.setattr(check_examples, "reference_files", lambda: iter([str(prose)]))
    assert check_examples.check_rule_references()
