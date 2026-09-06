"""Canonical Code Spelling — deterministic Arabic to ASCII.

Implements sections 4 to 8 of the Quranic Software Terminology Standard as a
function, so that the code spelling of a term is derived rather than chosen.

Input must be vocalized: short vowels cannot be recovered from unvocalized
Arabic, and guessing them is exactly the opinion this is meant to remove.
"""

import csv as _csv
import os as _os

# Where the spelling tables live. The skill's copy of this module repoints this
# one line at its own data/spelling/ directory (tools/generate_skill.py).
TABLES_DIR = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                          "standards", "terminology", "data")

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


def _table(name):
    """Rows of a spelling table, comments and blank lines dropped.

    A missing table is an error, not an empty table: deriving `nun_sakinah`
    because letter_names.tsv was not found would be a wrong answer given with
    confidence, and a copy of this module with no tables beside it must say so.
    """
    path = _os.path.join(TABLES_DIR, name)
    if not _os.path.exists(path):
        raise FileNotFoundError(f"spelling table {name} not found in {TABLES_DIR}")
    with open(path, encoding="utf-8") as fh:
        return [row for row in _csv.reader(fh, delimiter="\t")
                if row and row[0].strip() and not row[0].startswith("#")]


def _bare(text):
    """The letters alone: harakat and the dagger alif removed."""
    return "".join(c for c in text if c not in HARAKAT and c != DAGGER_ALIF)


def _load_letter_names():
    """The name of an Arabic letter is written as it is said: noon, not nun.

    A letter name carries no meaning beyond its sound, so spelling it letter by
    letter throws away the only thing it has. It also keeps `nun` and `sin`,
    which are ordinary English words, out of identifiers. Every other term
    follows the derivation.
    """
    return {_bare(row[1]): row[2] for row in _table("letter_names.tsv") if len(row) >= 3}


def _load_established():
    """Terms whose spelling is fixed by overwhelming use, not by derivation.

    `juz` is written that way in effectively every Quranic codebase, so
    deriving `juzu` would be correct and useless. Each row carries the
    measurement that justifies it, so the table cannot grow by taste.
    """
    return {_bare(row[0]): row[1] for row in _table("established_spellings.tsv") if len(row) >= 2}


def _load_general_words():
    """Ordinary Arabic words that are written in English (section 3).

    Section 3 decides whether a concept keeps its Arabic name. The same rule
    applies inside a compound: the Quranic word is transliterated, the ordinary
    word beside it is translated. `saghirah` carries nothing that `small` does
    not, so the mark is small_meem.
    """
    return {_bare(row[0]): (row[1], row[2].strip() if len(row) > 2 else "word")
            for row in _table("general_words.tsv") if len(row) >= 2}


def _load_connectives():
    """Words that join the parts of a name and carry nothing into it (section 14).

    `مَعَ كَوْنِ` in الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى says how the two halves
    relate, which the order of the English words already says. The name is
    waqf_jaiz_wasl_awla.
    """
    return {_bare(row[0]) for row in _table("connectives.tsv")}


LETTER_NAMES = None
ESTABLISHED = None
GENERAL_WORDS = None
CONNECTIVES = None


def letter_name(word):
    """The established code name for a letter name, or None."""
    global LETTER_NAMES
    if LETTER_NAMES is None:
        LETTER_NAMES = _load_letter_names()
    return LETTER_NAMES.get(_bare(_strip(word)))


def general_word(word):
    """The English form of an ordinary Arabic word, or None."""
    global GENERAL_WORDS
    if GENERAL_WORDS is None:
        GENERAL_WORDS = _load_general_words()
    bare = _bare(_strip(word))
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
    return ESTABLISHED.get(_bare(_strip(word)))


def is_connective(word):
    """Whether the word joins the parts of a name without belonging to it."""
    global CONNECTIVES
    if CONNECTIVES is None:
        CONNECTIVES = _load_connectives()
    return _bare(_strip(word)) in CONNECTIVES


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


def _drop_case_ending(text):
    """Drop a final short vowel: names are written in pausal form.

    Fully vocalized Arabic marks the case ending — الْقُرْآنُ, السُّورَةُ — and it
    is not part of the name. Without this, well-marked input gives `quranu` and
    `surahu`. Arabic itself drops it when stopping on the word.
    """
    i = len(text) - 1
    while i >= 0 and (text[i] in SUPERSCRIPTS or text[i] == MADDA):
        i -= 1
    if i >= 0 and text[i] in {FATHA, KASRA, DAMMA} | TANWIN:
        # Only when a consonant carries it; a bare vowel on an alif is the word.
        j = i - 1
        while j >= 0 and text[j] == SHADDA:
            j -= 1
        if j >= 0 and text[j] not in HARAKAT:
            return text[:i] + text[i + 1:]
    return text


def transliterate_word(word, construct=False):
    """`construct` marks a word bound to the next one, where a final ta
    marbutah is pronounced t: hamzat al-wasl, not hamzah al-wasl."""
    text = _drop_case_ending(_strip(word))
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


# Prepositions written as one letter joined to the next word (section 8). The
# letter carries a kasrah, which is what tells بِالرَّأْي (bi + al-ray) apart from
# بَالِغ. Before the article, لِ swallows the article's alif: لِلسُّكُون.
PREPOSITIONS = {"ب": "bi", "ل": "li"}


def split_preposition(word):
    """(preposition, rest) when the word is a one-letter preposition on a definite
    noun, else (None, word). The rest is the noun with its article restored."""
    if len(word) > 3 and word[0] in PREPOSITIONS and word[1] == KASRA:
        rest = word[2:]
        bare = _bare(rest)
        if bare.startswith("ال"):
            return PREPOSITIONS[word[0]], rest
        if word[0] == "ل" and bare.startswith("ل") and len(bare) > 2:
            return "li", "ا" + rest
    return None, word


def check_vocalized(phrase):
    """Raise ValueError naming the first word that carries no vowel mark.

    Short vowels cannot be recovered from unvocalized Arabic, and guessing them
    is exactly the opinion the derivation exists to remove. A word the tables
    settle by its letters alone — a letter name, an established spelling, an
    ordinary word, a connective — needs no marks.
    """
    for w in _strip(phrase).split():
        bare = _bare(w)
        if len(bare) <= 2 or any(c in HARAKAT for c in w):
            continue
        if letter_name(w) or established_name(w) or general_word(w) or is_connective(w):
            continue
        if bare.startswith("ال") and (letter_name(w[2:]) or established_name(w[2:])):
            continue
        raise ValueError(f"{w!r} is not vocalized: the derivation needs the short vowels")


def code_spelling(phrase, keep_leading_article=False):
    """Canonical Code Spelling of a full term, joined with underscores.

    A medial article is always rendered `al`, never assimilated to a sun letter,
    so that one convention holds across every term (section 8). A *leading*
    article is dropped: the term is `fathah`, not `al_fathah`. A one-letter
    preposition is its own part, and the noun it governs keeps its article:
    tafsir_bi_al_ray, madd_arid_li_al_sukun. A connective (connectives.tsv) is
    dropped: waqf_jaiz_wasl_awla.
    """
    words = [w for w in _strip(phrase).split() if w and not is_connective(w)]
    # A word marked `with_head` is translated only beside a head word, where the
    # compound is an English phrase (orthographic_mark); alone it is the Arabic
    # term (rasm_imlai).
    has_head = any(_general(w)[1] == "head" for w in words)

    def has_article(w):
        bare = _bare(w)
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
        preposition, w = split_preposition(w)
        if preposition:
            parts.append(preposition)
        # A definite word makes a following definite word its adjective, and an
        # adjective's article is not part of the name: waqf_lazim. An indefinite
        # word makes the pair a construct, whose article is kept: rubu_al_hizb.
        # The word that decides is the one right before, wherever the phrase
        # opened: in الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن the genitive after the
        # indefinite head keeps its `al` — waqf_jaiz_mustawi_al_tarafayn. A noun
        # governed by a preposition opens a phrase of its own and is never an
        # adjective.
        adjective = (idx > 0 and has_article(w) and has_article(words[idx - 1])
                     and not preposition)
        # A word is a construct head only when the next word is its genitive:
        # a noun followed by its own adjective keeps the pausal h (section 5),
        # qalqalah_sughra, and so does the genitive itself, madd_al_silah_sughra.
        following = words[idx + 1] if idx < len(words) - 1 else None
        next_is_adjective = (following is not None and has_article(following)
                             and has_article(w) and not split_preposition(following)[0])
        construct = following is not None and not adjective and not next_is_adjective
        english, role = _general(w)
        if role == "with_head" and not has_head:
            english = None
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
        elif p in PREPOSITIONS.values() and out:
            out.append(p)
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


def main(argv=None):
    import argparse, json, sys
    ap = argparse.ArgumentParser(
        prog="spell", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="The display form printed here is derived. An entry's recorded `display`\n"
               "may differ where usage was measured (tajwid → Tajweed): the entry wins.")
    ap.add_argument("terms", nargs="+", help="vocalized Arabic terms, one per argument")
    ap.add_argument("--json", action="store_true", help="one JSON object per term")
    ap.add_argument("--keep-leading-article", action="store_true",
                    help="keep a leading al: al_fathah rather than fathah")
    args = ap.parse_args(argv)
    failed = 0
    out = []
    for term in args.terms:
        try:
            check_vocalized(term)
            code = code_spelling(term, args.keep_leading_article)
            display = display_spelling(term)
        except ValueError as exc:
            failed += 1
            if args.json:
                out.append({"arabic": term, "error": str(exc)})
            else:
                print(f"{term}\terror: {exc}", file=sys.stderr)
            continue
        if args.json:
            out.append({"arabic": term, "code": code, "display": display,
                        "note": "display is derived; an entry's measured display wins"})
        else:
            print(f"{term}\t{code}\t{display}")
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
