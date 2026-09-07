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
        got, how = lookup.resolve(index, entry["code"])
        assert concept in got.split("|"), (concept, got)
        if how == "shared":      # a value of two classifications (section 14)
            assert lookup.resolve(index, f"{entry['parent']}:{entry['code']}") == (concept, "alias")


def test_registry(capsys):
    assert lookup.registry("surahs", "fatihah", False, REGISTRIES) == 0
    assert "fatihah" in capsys.readouterr().out
    assert lookup.registry("no_such_registry", None, False, REGISTRIES) == 1


def test_member_resolves(capsys):
    import json
    data = ["--data", os.path.join(SKILL, "data", "terminology.json")]
    main = lambda args: lookup.main(args + data)
    assert main(["qaloun", "sousi", "shuba"]) == 0
    out = capsys.readouterr().out
    assert "qaloun → `qalun`, a member of registry `qiraat`" in out
    assert "sousi → `susi`" in out and "shuba → `shubah`" in out
    assert main(["douri", "--json"]) == 0
    got = json.loads(capsys.readouterr().out)["douri"]
    assert got["member"] == "duri" and got["kind"] == "rawi" and got["row"]["code"] == "duri"
    # a form a concept and a member share goes to the concept
    assert main(["hamza"]) == 0
    assert "hamza → `hamzah`" in capsys.readouterr().out
