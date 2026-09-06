"""lookup.py resolves every recorded spelling, and says how it resolved."""
import os

import lookup
import pytest

from conftest import SKILL

REGISTRIES = os.path.join(SKILL, "data", "registries")


@pytest.fixture(scope="module")
def index(skill_data):
    return lookup.build_index(skill_data)


def test_resolve(skill_data, index):
    assert lookup.resolve(index, "aya") == ("ayah", "alias")
    assert lookup.resolve(index, "Waqf-Lazim") == ("waqf_lazim", "alias")
    assert lookup.resolve(index, "verse")[0] == "ayah"
    assert lookup.resolve(index, "waqf_jaiz")[1] == "deprecated"
    assert lookup.resolve(index, "no_such_thing") == (None, None)


def test_every_code_resolves_to_itself(skill_data, index):
    for concept, entry in skill_data["concepts"].items():
        assert lookup.resolve(index, entry["code"])[0] == concept


def test_registry(capsys):
    assert lookup.registry("surahs", "fatihah", False, REGISTRIES) == 0
    assert "fatihah" in capsys.readouterr().out
    assert lookup.registry("no_such_registry", None, False, REGISTRIES) == 1
