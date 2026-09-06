"""Check the entries against the standard's own rules, not just the schema.

`validate.py` asks whether an entry has the right shape. This asks whether it
obeys the rules the standard states in prose — the ones that were being checked
by hand, which is to say not checked.

    python3 tools/check_conformance.py

A departure that the decision record argues for is listed in DOCUMENTED below,
so the check stays useful: an undocumented mismatch is a finding, and a
documented one is a fact about the entry.

A problem fails the build. A warning is printed and counted, and does not: it
marks work the entry still owes — a source it has not cited yet — rather than
a rule it breaks.
"""
import glob, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
from translit import code_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
SOURCES = os.path.join(ROOT, "standards/terminology/sources.yml")

ARABIC = re.compile(r"[\u0600-\u06FF]")
# A run of Latin letters inside Arabic prose. Backticked code and the words
# below are how an Arabic sentence legitimately names a Latin thing.
LATIN = re.compile(r"[A-Za-z]{2,}")
LATIN_ALLOWED = {"dataset"}
LIST_FIELDS = ("alternative_spellings", "english_glosses", "deprecated", "related",
               "part_of", "boundaries", "boundaries_en")
# Fields that describe a drawn sign. A mark carries them; so does a value of the
# waqf-mark classification, because those values are drawn too; nothing else.
DRAWN_FIELDS = ("symbol", "unicode", "mark_family")
DRAWN_CLASSIFICATION = "waqf_mark_type"

# Codes that deliberately are not the derivation of their Arabic name. Each one
# is argued in content/*/03-terminology/decisions.md; the reason is repeated
# here so a reader of the check knows it was a decision and not a slip.
DOCUMENTED = {
    "ayah_numbering_madani_awwal": "section 14 — the value takes its parent's name; `add` is an English verb",
    "ayah_numbering_madani_akhir": "section 14 — the value takes its parent's name; `add` is an English verb",
    "ayah_numbering_makki": "section 14 — `makki` is taken by revelation_classification",
    "ayah_numbering_basri": "section 14 — the value takes its parent's name; `add` is an English verb",
    "ayah_numbering_dimashqi": "section 14 — the value takes its parent's name; `add` is an English verb",
    "ayah_numbering_kufi": "section 14 — the value takes its parent's name; `add` is an English verb",
}

def load():
    entries = {}
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        e = yaml.safe_load(open(path, encoding="utf-8"))
        entries[e["concept"]] = e
    return entries


def load_sources():
    return yaml.safe_load(open(SOURCES, encoding="utf-8")) or {}


def check(entries, sources=None):
    """(problems, warnings) — see the module docstring for the difference."""
    problems, warnings = [], []
    if sources is None:
        sources = load_sources()
    children = collections.Counter(e.get("parent") for e in entries.values())

    for code, e in sorted(entries.items()):
        names = e.get("names", {})
        arabic = (names.get("arabic") or {}).get("vocalized")

        # sections 4 to 8 — a quranic name's code is derived, not chosen
        if e.get("origin") == "quranic" and arabic:
            try:
                derived = code_spelling(arabic)
            except Exception as exc:
                problems.append(f"{code}: cannot derive from {arabic!r} — {exc}")
                derived = None
            if derived and derived != names.get("code") and code not in DOCUMENTED:
                problems.append(
                    f"{code}: code is {names.get('code')!r}, {arabic!r} derives to {derived!r} "
                    f"— add it to DOCUMENTED with its reason, or fix one of the two")

        # section 13 — a classification with no values is a name with nothing under it
        if e["kind"] == "classification" and not children.get(code):
            problems.append(f"{code}: a classification with no values (section 13)")

        # section 14 — a value states its parent, and the parent exists
        parent = e.get("parent")
        if parent and parent not in entries:
            problems.append(f"{code}: parent {parent!r} has no entry")
        # section 13 — a value's parent is the classification it is a value of
        if (e["kind"] == "classification_value" and parent in entries
                and entries[parent]["kind"] != "classification"):
            problems.append(f"{code}: a classification_value whose parent {parent!r} "
                            f"is a {entries[parent]['kind']}, not a classification (section 13)")

        # part_of is containment; what contains the entry must exist
        part_of = e.get("part_of") or []
        for whole in ([part_of] if isinstance(part_of, str) else part_of):
            if whole not in entries:
                problems.append(f"{code}: part_of {whole!r}, which has no entry")

        # only a drawn sign has a shape: a mark, or a value of the waqf-mark
        # classification, which is drawn in the mushaf too
        drawn = e["kind"] == "mark" or (
            e["kind"] == "classification_value" and parent == DRAWN_CLASSIFICATION)
        for field in DRAWN_FIELDS:
            if e.get(field) and not drawn:
                problems.append(f"{code}: has {field}, and only a mark or a value of "
                                f"{DRAWN_CLASSIFICATION} is drawn")

        # a list that names something twice names it once
        for field in LIST_FIELDS:
            values = e.get(field) or []
            if isinstance(values, str):
                continue
            dupes = sorted({v for v in values if values.count(v) > 1})
            if dupes:
                problems.append(f"{code}: {field} lists {dupes} more than once")

        # section 11 — the plural is the code plus s, never an Arabic plural
        # and never the plural of the English gloss
        if e.get("plural") and e["plural"] != names.get("code", code) + "s":
            problems.append(f"{code}: plural is {e['plural']!r}, section 11 gives "
                            f"{names.get('code', code) + 's'!r}")

        # a related link that points nowhere is a link the reader cannot follow
        for r in e.get("related") or []:
            if r not in entries:
                problems.append(f"{code}: related points at {r!r}, which has no entry")

        # section 19 — a gloss is not a spelling of the name
        glosses = {g.lower().replace(" ", "_") for g in e.get("english_glosses") or []}
        alts = set(e.get("alternative_spellings") or [])
        if glosses & alts:
            problems.append(f"{code}: {sorted(glosses & alts)} listed as both a gloss "
                            f"and an alternative spelling (section 19)")

        # section 27 — the entry is bilingual: every Arabic field has its English
        # twin, and a twin is a translation, so a list translates line for line
        for ar, en in (("definition", "definition_en"), ("purpose", "purpose_en"),
                       ("boundaries", "boundaries_en"), ("note", "note_en")):
            if e.get(ar) and not e.get(en):
                problems.append(f"{code}: has {ar} and no {en} (section 27)")
            if e.get(en) and not e.get(ar):
                problems.append(f"{code}: has {en} and no {ar} (section 27)")
            if ar == "boundaries" and e.get(en) and len(e[en]) != len(e.get(ar) or []):
                problems.append(f"{code}: {len(e.get(ar) or [])} boundaries and "
                                f"{len(e[en])} in {en} — they translate line for line")

        # an English field written in Arabic is an untranslated field. A name
        # quoted as «…» is the Arabic being talked about, not text left behind.
        for en in ("definition_en", "purpose_en", "note_en"):
            value = e.get(en)
            if value and ARABIC.search(re.sub(r"«[^»]*»", "", value)):
                problems.append(f"{code}: {en} still has Arabic in it outside «…»")

        # Arabic prose that names a Latin thing does it in backticks
        for ar in ("definition", "purpose", "note"):
            value = e.get(ar)
            if not value:
                continue
            bare = re.sub(r"`[^`]*`", "", value)
            latin = sorted({w for w in LATIN.findall(bare) if w.lower() not in LATIN_ALLOWED})
            if latin:
                warnings.append(f"{code}: {ar} has Latin words outside backticks: {latin}")

        # section 28 — an entry with no source is not adopted, and a Quranic
        # concept with no source has not been documented yet
        if e.get("status") == "adopted" and not e.get("sources"):
            problems.append(f"{code}: adopted with no source (section 28)")
        if e.get("origin") == "quranic" and not e.get("sources"):
            warnings.append(f"{code}: origin quranic with no source yet (section 28)")
        for src in e.get("sources") or []:
            if src.get("id") not in sources:
                problems.append(f"{code}: cites source {src.get('id')!r}, which is not "
                                f"in sources.yml")

    return problems, warnings


def main():
    entries = load()
    problems, warnings = check(entries)
    documented = sorted(c for c in DOCUMENTED if c in entries)
    if problems:
        print(f"{len(problems)} problems in {len(entries)} entries:")
        for p in problems:
            print(f"  {p}")
    else:
        print(f"ok — {len(entries)} entries obey the rules the standard states")
    if warnings:
        unsourced = sum(1 for w in warnings if "no source yet" in w)
        print(f"\n{len(warnings)} warnings ({unsourced} quranic entries still without a source):")
        for w in warnings:
            print(f"  {w}")
    if documented:
        print(f"\n{len(documented)} documented departures from the derivation:")
        for c in documented:
            print(f"  {c}: {DOCUMENTED[c]}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
