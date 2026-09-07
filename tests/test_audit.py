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
    # `files` is no entry plus s, and camelCase resolves to the canonical name
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


def test_registry_members(tmp_path):
    (tmp_path / "m.py").write_text(
        "riwayahs = ['hafs', 'qaloun', 'douri', 'sousi', 'shuba']\n"
        "system = 'madani-first'\nold = 'madani_awwal'\npos = 3\nsimple = 'x'\nelephant = 1\n", encoding="utf-8")
    out = json.loads(run(str(tmp_path), "--json").stdout)
    by = {f["found"]: f for f in out["findings"]}
    # a KFGQPC spelling of a rawi is an error naming the registry code
    for found, code in (("qaloun", "qalun"), ("douri", "duri"), ("sousi", "susi"), ("shuba", "shubah")):
        assert by[found]["rule"] == "member" and by[found]["canonical"] == code, found
        assert "Rawi" in by[found]["display"]
    # a member's own code is never a finding
    assert "hafs" not in by
    # a value's code is unique within its classification: `madani-first` is
    # the code, so it is clean; the old spelling points at the code, not the id
    assert "madani_first" not in by
    assert by["madani_awwal"]["rule"] == "spelling" and by["madani_awwal"]["canonical"] == "madani_first"
    # `pos` is a position far more often than a part of speech; `simple` is a
    # plain word; a surah named by an ordinary word is a hint, not a ruling
    assert by["pos"]["rule"] == "generic" and by["pos"]["severity"] == "warning"
    assert by["simple"]["rule"] == "generic"
    assert by["elephant"]["rule"] == "generic" and by["elephant"]["canonical"] == "fil"


def test_external_names_are_read_past(tmp_path):
    """A name the project quotes rather than chooses is not a finding."""
    (tmp_path / "load.py").write_text(
        'PACKAGE = "UthmanicHafs-v-3.0.zip"\n'
        'SIGN = "ARABIC START OF RUB EL HIZB"\n'
        'surah = row["sura_no"]\n'
        'sura = 1\n', encoding="utf-8")
    (tmp_path / ".terminology.json").write_text(json.dumps({
        "external_names": ["Uthmanic[A-Za-z0-9.\\-]*", "ARABIC [A-Z ]+", "sura_no"],
    }), encoding="utf-8")
    out = json.loads(run(str(tmp_path), "--json").stdout)
    # the vendor's package, the Unicode name and the vendor's column are quoted;
    # the project's own `sura` is still a finding
    assert sorted({f["found"] for f in out["findings"]}) == ["sura"]
    assert out["summary"]["external_names"] == 3


def test_external_names_must_be_a_regular_expression(tmp_path):
    (tmp_path / "a.py").write_text("ayah = 1\n", encoding="utf-8")
    (tmp_path / ".terminology.json").write_text(
        json.dumps({"external_names": ["("]}), encoding="utf-8")
    result = run(str(tmp_path))
    assert result.returncode == 2
    assert "not a regular expression" in result.stderr
