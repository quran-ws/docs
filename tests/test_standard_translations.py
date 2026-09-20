"""Keep rule references and technical examples aligned across translations."""
import re
from pathlib import Path

import check_examples
from conftest import ROOT


def editions():
    return {lang: (Path(ROOT) / path).read_text(encoding="utf-8")
            for lang, path in check_examples.STANDARD.items()}


def rule_sections(text):
    # The developer guide follows the final numbered rule.
    text = text.split('\n## Using names in software')[0]
    text = text.split('\n## استخدام الأسماء في البرمجيات')[0]
    parts = re.split(r'<a id="rule-(\d{3})"></a>', text)
    return dict(zip(parts[1::2], parts[2::2]))


def test_rule_ids_and_technical_examples_match():
    pages = {lang: rule_sections(text) for lang, text in editions().items()}
    expected = [f"{i:03}" for i in range(1, 74)]
    assert list(pages["ar"]) == list(pages["en"]) == expected
    for rule in expected:
        ar, en = pages["ar"][rule], pages["en"][rule]
        assert sorted(re.findall(r'`([^`\n]+)`', ar)) == sorted(re.findall(r'`([^`\n]+)`', en)), rule
        assert re.findall(r'^```[^\n]*\n(.*?)^```', ar, re.M | re.S) == re.findall(
            r'^```[^\n]*\n(.*?)^```', en, re.M | re.S), rule
        assert sum(line.startswith('|') for line in ar.splitlines()) == sum(
            line.startswith('|') for line in en.splitlines()), rule


def test_rule_checker_rejects_translation_missing_an_anchor(tmp_path, monkeypatch):
    pages = editions()
    pages['en'] = pages['en'].replace('<a id="rule-026"></a>', '')
    paths = {}
    for lang, text in pages.items():
        path = tmp_path / (lang + '.md')
        path.write_text(text, encoding='utf-8')
        paths[lang] = str(path)
    monkeypatch.setattr(check_examples, 'STANDARD', paths)
    monkeypatch.setattr(check_examples, 'reference_files', lambda: iter([]))
    errors = check_examples.check_rule_references()
    assert any('en standard' in error for error in errors)
    assert any('same rule IDs' in error for error in errors)
