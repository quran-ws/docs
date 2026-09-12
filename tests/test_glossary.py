"""content/glossary.json is generated from the dictionary and every term resolves."""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_glossary_is_current():
    r = subprocess.run([sys.executable, "tools/generate_glossary.py", "--check"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_every_term_is_a_concept_with_both_texts():
    doc = json.loads((ROOT / "content" / "glossary.json").read_text(encoding="utf8"))
    assert doc["terms"], "empty glossary"
    for t in doc["terms"]:
        assert (ROOT / "standards" / "terminology" / "concepts" / f"{t['id']}.yml").exists(), t["id"]
        assert t["explain"] and t["forDevs"] and t["arabic"], t["id"]


def test_licensing_pages_have_the_same_sections():
    en = (ROOT / "content" / "en" / "licensing.md").read_text(encoding="utf8")
    ar = (ROOT / "content" / "ar" / "licensing.md").read_text(encoding="utf8")
    count = lambda s: sum(1 for l in s.splitlines() if l.startswith("## "))
    assert count(en) == count(ar), f"licensing.md: {count(en)} English sections, {count(ar)} Arabic"
