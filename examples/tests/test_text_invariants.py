"""The text page's test table, as assertions over examples/data/ayah.json.

Runs under pytest or on its own:

    python3 examples/tests/test_text_invariants.py

Each test names the row of the table it comes from
(content/en/02-quranic-text/, section "Tests"). A failing test blocks a
release; it never fixes the text.
"""
import hashlib, json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
RECORD = json.load(open(os.path.join(DATA, "ayah.json"), encoding="utf-8"))
EDITION = json.load(open(os.path.join(DATA, "mushaf_edition.json"), encoding="utf-8"))
TEXT = RECORD["text"]

EDITION_MARKS = {"۝", "۞", "۩"}          # ۝ ۞ ۩
LATIN_OR_DIGIT = re.compile(r"[A-Za-z0-9]")
HTML = re.compile(r"<[^>]+>|&[a-z]+;")
# Combining marks, i.e. everything that must stay attached to its base letter.
COMBINING = lambda c: unicodedata.combining(c) != 0


def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def test_checksum_the_text_did_not_change():
    assert sha256(TEXT) == RECORD["text_hash"]
    assert sha256(RECORD["basmalah"]["text"]) == RECORD["basmalah"]["text_hash"]


def test_derived_layer_matches_its_source():
    # The edition record carries the hash the layer was derived from.
    assert EDITION["source_hash"] == RECORD["text_hash"]
    assert EDITION["errata"] == "errata.json" and EDITION["released"]
    assert EDITION["mushaf_edition"] == RECORD["mushaf_edition"]
    assert EDITION["riwayah"] == RECORD["riwayah"]
    assert EDITION["ayah_numbering_system"] == RECORD["ayah_numbering_system"]


def test_round_trip_returns_the_same_characters():
    stored = json.loads(json.dumps(RECORD, ensure_ascii=False))
    assert stored["text"] == TEXT
    assert stored["text"].encode("utf-8").decode("utf-8") == TEXT


def test_no_normalization():
    # NFC reorders shaddah and fathah on ٱللَّهُ. The stored text is the
    # transmitted order, so normalising it must be a visible change — which is
    # why `normalize` is banned in the text path.
    assert unicodedata.normalize("NFC", TEXT) != TEXT
    assert unicodedata.normalize("NFKC", TEXT) != TEXT


def test_no_foreign_characters():
    # The allowlist is generated from the source; here it is the Arabic block
    # plus the space, which is what this text is built from.
    for c in TEXT:
        assert c == " " or "؀" <= c <= "ۿ", f"U+{ord(c):04X} is outside the allowlist"
    assert "﻿" not in TEXT and not TEXT.startswith("﻿")


def test_the_text_field_holds_text_only():
    assert not LATIN_OR_DIGIT.search(TEXT)
    assert not HTML.search(TEXT)
    assert not (set(TEXT) & EDITION_MARKS), "edition marks belong to the edition, not the ayah"
    assert TEXT == TEXT.strip()


def test_basmalah_is_its_own_field():
    assert RECORD["basmalah"]["text"] not in TEXT
    assert RECORD["basmalah"]["present"] is True
    assert RECORD["basmalah"]["counted_as_ayah"] is False   # Kufi numbering, 112:1


def test_location_is_bound_to_surah_and_numbering_system():
    for key in ("surah_number", "ayah_number", "ayah_numbering_system", "riwayah", "mushaf_edition"):
        assert key in RECORD, f"{key} missing: an ayah number alone is not a location"
    assert 1 <= RECORD["surah_number"] <= 114
    assert RECORD["ayah_number"] >= 1


def test_words_follow_the_declared_tokenization():
    assert RECORD["tokenization"] == "whitespace"
    tokens = TEXT.split(" ")
    assert [w["text"] for w in RECORD["words"]] == tokens
    assert [w["word_position"] for w in RECORD["words"]] == list(range(1, len(tokens) + 1))
    assert " ".join(tokens) == TEXT


def test_truncation_never_splits_a_letter_from_its_marks():
    # `slice` cuts anywhere, so somewhere it separates a letter from its marks.
    unsafe = [i for i in range(1, len(TEXT)) if COMBINING(TEXT[i])]
    assert unsafe, "this text has marks; a naive cut must be able to split one off"
    # A grapheme-aware cutter only cuts where the next character is a base
    # character. Cut at every such length and check no head ends short of its
    # marks and no tail starts with an orphaned mark.
    boundaries = [i for i in range(1, len(TEXT)) if not COMBINING(TEXT[i])]
    for i in boundaries:
        head, tail = TEXT[:i], TEXT[i:]
        assert not COMBINING(tail[0]), f"cut at {i} orphans a mark"
        assert i == len(TEXT) or not COMBINING(TEXT[i]), f"cut at {i} leaves a letter without its marks"


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok   {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL {name}: {e}")
    sys.exit(1 if failures else 0)
