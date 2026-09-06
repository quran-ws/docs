"""The alias indexes: every spelling resolves to one concept, in its namespace."""
import build_aliases
import build_registry_aliases


def test_concept_aliases():
    index, clashes = build_aliases.build()
    assert not clashes
    for concept in set(index.values()):
        assert index[concept] == concept
    assert index["waqf-lazim"] == index["waqf_lazim"] == "waqf_lazim"
    assert "waqf_jaiz" not in index          # a deprecated name does not resolve


def test_registry_namespaces():
    index, clashes = build_registry_aliases.build()
    assert not clashes
    assert index["qiraah"]["hamzah"] == "hamzah"
    assert index["rawi"]["hafs"] == "hafs"
    assert index["surah"]["al_fatiha"] == "fatihah"


def test_registry_reader():
    from registry import read, records
    header, rows = read("standards/terminology/registries/qiraat.tsv")
    assert header[0] == "code" and len(rows) == 49
    assert records("standards/terminology/registries/sajdah.tsv")[0]["surah"] == "araf"
