"""audit_terminology.py against a small tree with known findings."""
import json
import os
import subprocess
import sys

import pytest

from conftest import SKILL_SCRIPTS

AUDIT = os.path.join(SKILL_SCRIPTS, "audit_terminology.py")
FIXTURE = {
    "a.py": ("suras = []\naya_key = 1\ntajweed_rules = {}\nverse_count = 3\n"
             "files = []\nwaqf_lazim = 1\nwaqfLazim = 2\nnun_saghirah = 3\n"
             "sifr_mustadir = 4\npage_number = 1\n"),
    "r.md": "# The verse\nsuras and ayat\n",
}


@pytest.fixture
def tree(tmp_path):
    for name, text in FIXTURE.items():
        (tmp_path / name).write_text(text, encoding="utf-8")
    return tmp_path


def run(*args):
    return subprocess.run([sys.executable, AUDIT, *args], capture_output=True, text=True)


def test_findings(tree):
    out = json.loads(run(str(tree), "--json").stdout)
    # a finding names the identifier it was found in; the form may be the
    # identifier itself or the part of it that matched
    seen = {(f["rule"], f["identifier"]) for f in out["findings"]}
    assert ("spelling", "suras") in seen
    assert ("spelling", "aya_key") in seen
    assert ("arabic_plural", "ayat") in seen
    # `tajweed` is the display name and also a recorded spelling; either rule
    # may claim it, but it is a finding
    assert any(f["identifier"] == "tajweed_rules" for f in out["findings"])
    assert ("gloss", "verse_count") in seen
    assert ("spelling", "nun_saghirah") in seen
    # `files` is not fil + s, and camelCase resolves to the canonical name
    assert not any(f["identifier"] == "files" for f in out["findings"])
    assert not any(f["identifier"] == "waqfLazim" for f in out["findings"])
    # prose may carry a gloss and the display name
    assert not any(f["file"].endswith(".md") and f["rule"] in ("gloss", "display_in_code")
                   for f in out["findings"])
    assert any(m["concept"] == "ayah" for m in out["mixed"])


def test_exit_codes(tree):
    assert run(str(tree), "--strict").returncode == 1
    assert run(str(tree)).returncode == 0


def test_clean_tree(tmp_path):
    (tmp_path / "ok.py").write_text("ayah = 1\nsurahs = []\nwaqf_lazim = 2\n", encoding="utf-8")
    result = run(str(tmp_path), "--strict")
    assert result.returncode == 0
    assert "ok —" in result.stdout
