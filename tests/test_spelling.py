"""The golden cases in tools/test_translit.py, one test each."""
import pytest

import test_translit as golden
from translit import check_vocalized, code_spelling, display_spelling, split_preposition


@pytest.mark.parametrize("arabic,expected", sorted(set(golden.CASES)))
def test_code_spelling(arabic, expected):
    assert code_spelling(arabic) == expected


@pytest.mark.parametrize("arabic,expected", golden.DISPLAY_CASES)
def test_display_spelling(arabic, expected):
    assert display_spelling(arabic) == expected


@pytest.mark.parametrize("arabic", golden.REFUSED)
def test_unvocalized_is_refused(arabic):
    with pytest.raises(ValueError):
        check_vocalized(arabic)


def test_vocalized_passes():
    for arabic, _ in golden.CASES:
        check_vocalized(arabic)


def test_unmarked_initial_alif_is_refused():
    with pytest.raises(ValueError):
        code_spelling("استعاذة")


def test_preposition_split():
    assert split_preposition("بِالرَّأْي")[0] == "bi"
    assert split_preposition("لِلسُّكُون")[0] == "li"
    assert split_preposition("بَالِغ") == (None, "بَالِغ")


def test_cli(tmp_path, capsys):
    from translit import main
    assert main(["سُورَة", "--json"]) == 0
    out = capsys.readouterr().out
    assert '"code": "surah"' in out
    assert main(["سورة"]) == 1
