"""Canonical Code Spelling — deterministic Arabic to ASCII.

Implements sections 4 to 8 of the Quranic Software Terminology Standard as a
function, so that the code spelling of a term is derived rather than chosen.

Input must be vocalized: short vowels cannot be recovered from unvocalized
Arabic, and guessing them is exactly the opinion this is meant to remove.
"""

import csv as _csv
import os as _os

FATHA, KASRA, DAMMA, SUKUN, SHADDA = "َ", "ِ", "ُ", "ْ", "ّ"
FATHATAN, KASRATAN, DAMMATAN = "ً", "ٍ", "ٌ"
TANWIN = {FATHATAN, KASRATAN, DAMMATAN}
HARAKAT = {FATHA, KASRA, DAMMA, SUKUN, SHADDA} | TANWIN
DAGGER_ALIF, MADDA, SUPERSCRIPTS = "ٰ", "ٓ", "ۖۗۘۙۚۛۜ"

# Consonants. Emphatic and non-emphatic pairs collapse: the target is an
# ASCII-friendly identifier, not a reversible academic transliteration (section 4).
CONSONANTS = {
    "ب": "b", "ت": "t", "ث": "th", "ج": "j", "ح": "h",
    "خ": "kh", "د": "d", "ذ": "dh", "ر": "r", "ز": "z",
    "س": "s", "ش": "sh", "ص": "s", "ض": "d", "ط": "t",
    "ظ": "z", "غ": "gh", "ف": "f", "ق": "q", "ك": "k",
    "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w",
    "ي": "y", "ة": "h",
}
# Hamza in every seat, and ayn, carry no letter of their own (section 7).
SILENT = set("ءأإؤئع")
ALIFS = set("اآى")
VOWEL_OF = {FATHA: "a", KASRA: "i", DAMMA: "u", FATHATAN: "a", KASRATAN: "i", DAMMATAN: "u"}
VOWELS = set("aiu")


def _is_word_final(text, i):
    """True when nothing but vowel marks follows the letter at i."""
    return all(c in HARAKAT or c == DAGGER_ALIF for c in text[i + 1:])


def _load_letter_names():
    """The name of an Arabic letter is written as it is said: noon, not nun.

    A letter name carries no meaning beyond its sound, so spelling it letter by
    letter throws away the only thing it has. It also keeps `nun` and `sin`,
    which are ordinary English words, out of identifiers. Every other term
    follows the derivation.
    """
    path = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                         "standards/terminology/data/letter_names.tsv")
    names = {}
    if not _os.path.exists(path):
        return names
    with open(path, encoding="utf-8") as fh:
        for row in _csv.reader(fh, delimiter="\t"):
            if not row or row[0].startswith("#") or len(row) < 3:
                continue
            bare = "".join(c for c in row[1] if c not in HARAKAT and c != DAGGER_ALIF)
            names[bare] = row[2]
    return names


def _load_established():
    """Terms whose spelling is fixed by overwhelming use, not by derivation.

    `juz` is written that way in effectively every Quranic codebase, so
    deriving `juzu` would be correct and useless. Each row carries the
    measurement that justifies it, so the table cannot grow by taste.
    """
    path = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                         "standards/terminology/data/established_spellings.tsv")
    names = {}
    if not _os.path.exists(path):
        return names
    with open(path, encoding="utf-8") as fh:
        for row in _csv.reader(fh, delimiter="\t"):
            if not row or row[0].startswith("#") or len(row) < 2:
                continue
            names["".join(c for c in row[0] if c not in HARAKAT and c != DAGGER_ALIF)] = row[1]
    return names


def _load_general_words():
    """Ordinary Arabic words that are written in English (section 3).

    Section 3 decides whether a concept keeps its Arabic name. The same rule
    applies inside a compound: the Quranic word is transliterated, the ordinary
    word beside it is translated. `saghirah` carries nothing that `small` does
    not, so the mark is small_meem.
    """
    path = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                         "standards/terminology/data/general_words.tsv")
    words = {}
    if not _os.path.exists(path):
        return words
    with open(path, encoding="utf-8") as fh:
        for row in _csv.reader(fh, delimiter="\t"):
            if not row or row[0].startswith("#") or len(row) < 2:
                continue
            role = row[2].strip() if len(row) > 2 else "word"
            words["".join(c for c in row[0] if c not in HARAKAT and c != DAGGER_ALIF)] = (row[1], role)
    return words


LETTER_NAMES = None
ESTABLISHED = None
GENERAL_WORDS = None


def letter_name(word):
    """The established code name for a letter name, or None."""
    global LETTER_NAMES
    if LETTER_NAMES is None:
        LETTER_NAMES = _load_letter_names()
    bare = "".join(c for c in _strip(word) if c not in HARAKAT and c != DAGGER_ALIF)
    return LETTER_NAMES.get(bare)


def general_word(word):
    """The English form of an ordinary Arabic word, or None."""
    global GENERAL_WORDS
    if GENERAL_WORDS is None:
        GENERAL_WORDS = _load_general_words()
    bare = "".join(c for c in _strip(word) if c not in HARAKAT and c != DAGGER_ALIF)
    return GENERAL_WORDS.get(bare) or (GENERAL_WORDS.get(bare[2:]) if bare.startswith("ال") else None)


def _general(word):
    """(english, role) for an ordinary word, or (None, None)."""
    hit = general_word(word)
    return hit if hit else (None, None)


def established_name(word):
    """The established code spelling of a whole word, or None."""
    global ESTABLISHED
    if ESTABLISHED is None:
        ESTABLISHED = _load_established()
    bare = "".join(c for c in _strip(word) if c not in HARAKAT and c != DAGGER_ALIF)
    return ESTABLISHED.get(bare)


def _strip(text):
    out = []
    for ch in text:
        if ch in SUPERSCRIPTS or ch == MADDA:
            continue
        out.append(ch)
    return "".join(out)


def _harakah(text, i):
    """The vowel mark attached to the letter at i, skipping shadda."""
    j = i + 1
    while j < len(text) and text[j] == SHADDA:
        j += 1
    return text[j] if j < len(text) and text[j] in HARAKAT else None


def _shadda(text, i):
    """Shadda may be written before or after the vowel mark; accept either."""
    j = i + 1
    while j < len(text) and text[j] in HARAKAT:
        if text[j] == SHADDA:
            return True
        j += 1
    return False


def transliterate_word(word, construct=False):
    """`construct` marks a word bound to the next one, where a final ta
    marbutah is pronounced t: hamzat al-wasl, not hamzah al-wasl."""
    text = _strip(word)
    if construct:
        stripped = text.rstrip("".join(HARAKAT))
        if stripped.endswith("ة"):
            text = stripped[:-1] + "ت" + text[len(stripped):]
    out = []
    i = 0
    n = len(text)

    # A word-initial alif carries no consonant of its own; its vowel opens the
    # word. Alif al-wasl is ambiguous unvocalized (istiadhah, not astiadhah),
    # so an unmarked initial alif is refused rather than guessed.
    if n and text[0] in ALIFS | {"أ", "إ"}:
        v = _harakah(text, 0)
        if text[0] == "آ":
            out.append("a")
        elif text[0] == "إ" and not v:
            out.append("i")  # hamzah below an alif is always kasrah
        elif text[0] == "أ" and not v:
            raise ValueError(
                f"unvocalized initial hamzah in {word!r}: it may be fathah or dammah"
            )
        elif v and v != SUKUN:
            out.append(VOWEL_OF[v])
        else:
            raise ValueError(
                f"unvocalized initial alif in {word!r}: mark it (\u0627\u0650 / \u0627\u064e / \u0627\u064f)"
            )
        i = 1

    while i < n:
        ch = text[i]

        if ch in HARAKAT or ch == DAGGER_ALIF:
            i += 1
            continue

        # Nisba ending: a final doubled ya reduces to i (makki, not makkiyy).
        if ch == "ي" and _shadda(text, i) and i + 2 >= n - 1:
            rest = text[i + 2:].replace(SUKUN, "").replace(FATHA, "")
            if all(c in HARAKAT for c in rest):
                if not (out and out[-1] == "i"):
                    out.append("i")
                break

        if ch in SILENT:
            # Hamza and ayn carry no letter, but the vowel they carry survives:
            # muallim, not mullim.
            v = _harakah(text, i)
            if v and v != SUKUN and v not in TANWIN:
                out.append(VOWEL_OF[v])
            elif _is_word_final(text, i) and out and out[-1] not in VOWELS:
                # At the end of a word the letter would otherwise vanish and cut
                # the word short: rub, saba. Echo the vowel before it so the
                # word still ends where Arabic ends it (section 7).
                for prev in reversed(out):
                    if prev in VOWELS:
                        out.append(prev)
                        break
            i += 1
            continue

        if ch in ALIFS:
            # An alif after a fatha is that fatha lengthened, not a second a.
            if not (out and out[-1] == "a"):
                out.append("a")
            i += 1
            continue

        if ch in ("و", "ي"):
            prev = out[-1] if out else ""
            v = _harakah(text, i)
            long_vowel = {"و": ("u", "u"), "ي": ("i", "i")}[ch]
            # A waw or ya with no vowel of its own, after its matching short
            # vowel, is a long vowel and is never doubled in ASCII (section 6).
            if (v is None or v == SUKUN) and prev == long_vowel[0]:
                i += 1
                continue
            letter = CONSONANTS[ch]
            out.append(letter * (2 if _shadda(text, i) else 1))
            if v and v != SUKUN:
                out.append(VOWEL_OF[v])
            i += 1
            continue

        if ch in CONSONANTS:
            letter = CONSONANTS[ch]
            out.append(letter * (2 if _shadda(text, i) else 1))
            v = _harakah(text, i)
            if v and v != SUKUN and v not in TANWIN:
                out.append(VOWEL_OF[v])
            i += 1
            continue

        i += 1

    return "".join(out)


def _drop_article(word):
    """Strip a leading alif-lam, and the shadda by which a sun letter absorbs it.

    Only that one shadda goes: any later shadda is real gemination
    (al-dammah keeps the doubled mim, al-tilawah loses the doubled ta).
    """
    chars = list(word)
    i = 0
    seen = 0
    while i < len(chars) and seen < 2:
        if chars[i] in ("ا", "ل"):
            seen += 1
        i += 1
    rest = chars[i:]
    # Marks attached to the sun letter follow it directly; drop one shadda there.
    j = 1
    while j < len(rest) and rest[j] in HARAKAT:
        if rest[j] == SHADDA:
            del rest[j]
            break
        j += 1
    return "".join(rest)


def code_spelling(phrase, keep_leading_article=False):
    """Canonical Code Spelling of a full term, joined with underscores.

    A medial article is always rendered `al`, never assimilated to a sun letter,
    so that one convention holds across every term (section 8). A *leading*
    article is dropped: the term is `fathah`, not `al_fathah`.
    """
    words = [w for w in _strip(phrase).split() if w]

    def has_article(w):
        bare = "".join(c for c in w if c not in HARAKAT and c != DAGGER_ALIF)
        return bare.startswith("ال") and len(bare) > 2

    parts = []
    # An adjective translated into English moves in front of its noun, because
    # that is English word order: المِيم الصَّغِيرَة is small_meem, not meem_small.
    pending_adjective = None
    # A translated construct head moves to the end, for the same reason. A chain
    # of them reverses, because that is how English stacks qualifiers:
    # نَوْع عَلَامَة الوَقْف is waqf_mark_type.
    trailing_heads = []
    for idx, w in enumerate(words):
        # A definite first word makes a following definite word its adjective,
        # and an adjective's article is not part of the name: waqf_lazim.
        # An indefinite first word makes the pair a construct, whose article
        # is kept: rubu_al_hizb.
        adjective = idx > 0 and has_article(w) and has_article(words[0])
        construct = idx < len(words) - 1 and not adjective
        bare = "".join(c for c in w if c not in HARAKAT and c != DAGGER_ALIF)
        english, role = _general(w)
        if english:
            if adjective:
                pending_adjective = english
            elif role == "head" and idx < len(words) - 1:
                trailing_heads.append(english)
            else:
                parts.append(english)
            continue

        established = (established_name(w) or letter_name(w)
                       or ((established_name(_drop_article(w)) or letter_name(_drop_article(w)))
                           if has_article(w) else None))
        if established:
            if has_article(w) and (parts or keep_leading_article) and not adjective:
                parts.append("al")
            parts.append(established)
            continue

        if has_article(w):
            rest = _drop_article(w)
            if (parts and not adjective) or (not parts and keep_leading_article):
                parts.append("al")
            parts.append(transliterate_word(rest, construct))
        else:
            parts.append(transliterate_word(w, construct))
    if pending_adjective:
        parts.insert(0, pending_adjective)
    if trailing_heads:
        # English needs no article on the qualifier: saktah_mark, not al_saktah_mark.
        if parts and parts[0] == "al":
            parts.pop(0)
        parts.extend(reversed(trailing_heads))
    return "_".join(p for p in parts if p)


def display_spelling(phrase):
    """Display form: title case, with the article hyphenated as `al-`."""
    parts = code_spelling(phrase).split("_")
    out = []
    for p in parts:
        if p == "al" and out:
            out.append("al-")
        else:
            out.append(p.capitalize() if not (out and out[-1] == "al-") else p)
    joined = ""
    for p in out:
        if p == "al-":
            joined += " al-"
        elif joined.endswith("al-"):
            joined += p.capitalize()
        else:
            joined += (" " if joined else "") + p
    return joined.strip()


if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        print(f"{arg}\t{code_spelling(arg)}\t{display_spelling(arg)}")
