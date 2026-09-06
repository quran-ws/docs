"""Check the entries against the standard's own rules, not just the schema.

`validate.py` asks whether an entry has the right shape. This asks whether it
obeys the rules the standard states in prose — the ones that were being checked
by hand, which is to say not checked.

    python3 tools/check_conformance.py

A departure that the decision record argues for is listed in DOCUMENTED below,
so the check stays useful: an undocumented mismatch is a finding, and a
documented one is a fact about the entry.
"""
import glob, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
from translit import code_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")

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

# Mismatches whose cause is in the tool, not the entry. Kept apart from
# DOCUMENTED so that a decision is never confused with a defect: these are
# meant to disappear, and the entry they name is already correct.
TOOL_DEFECTS = {
    "waqf_jaiz_mustawi_al_tarafayn":
        "translit.py drops the `al` of a construct that follows a definite head. "
        "`مُسْتَوِي الطَّرَفَيْن` alone gives `mustawi_al_tarafayn`, and inside "
        "`الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن` it gives `mustawi_tarafayn`. Section 8 "
        "keeps the `al` when the first word is indefinite, so the entry is right "
        "and the derivation is wrong.",
}


def load():
    entries = {}
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        e = yaml.safe_load(open(path, encoding="utf-8"))
        entries[e["concept"]] = e
    return entries


def check(entries):
    problems = []
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
            if (derived and derived != names.get("code")
                    and code not in DOCUMENTED and code not in TOOL_DEFECTS):
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

        # section 28 — an entry with no source is not adopted
        if e.get("status") == "adopted" and not e.get("sources"):
            problems.append(f"{code}: adopted with no source (section 28)")

    return problems


def main():
    entries = load()
    problems = check(entries)
    documented = sorted(c for c in DOCUMENTED if c in entries)
    if problems:
        print(f"{len(problems)} problems in {len(entries)} entries:")
        for p in problems:
            print(f"  {p}")
    else:
        print(f"ok — {len(entries)} entries obey the rules the standard states")
    if documented:
        print(f"\n{len(documented)} documented departures from the derivation:")
        for c in documented:
            print(f"  {c}: {DOCUMENTED[c]}")
    defects = sorted(c for c in TOOL_DEFECTS if c in entries)
    if defects:
        print(f"\n{len(defects)} entries held back by a defect in the tool, not in the entry:")
        for c in defects:
            print(f"  {c}: {TOOL_DEFECTS[c]}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
