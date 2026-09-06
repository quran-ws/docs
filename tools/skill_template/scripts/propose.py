#!/usr/bin/env python3
"""Draft a dictionary entry for a concept the standard has no name for.

    python3 propose.py "رُبْع الحِزْب"                      # derive the name, draft the entry
    python3 propose.py rubu_al_hizb "رُبْع الحِزْب"          # the name you expect, checked
    python3 propose.py "خَتْمَة" --category recitation --kind entity --display Khatmah
    python3 propose.py "خَتْمَة" --out khatmah.yml           # write the draft, print the checklist

The three things the standard asks of a new term are done in order, and each
one can stop you: the vocalized Arabic is derived into the code spelling
(sections 4-8), so the name is never chosen; the dictionary is searched for the
concept under every spelling it knows, so a "new" term that already exists is
caught; and the entry is written in the shape of `data/schema.json`, with the
acceptance checklist of section 30 beside it. A proposal is a draft: it goes
upstream to the guidelines repository, not into this skill's data.

Exit codes: 0 drafted; 1 the Arabic is not vocalized, or the concept already
exists under another spelling; 2 usage.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
DATA = os.path.join(SKILL, "data", "terminology.json")
ASSETS = os.path.join(SKILL, "assets")
TEMPLATE = os.path.join(ASSETS, "proposal-template.yml")
CHECKLIST = os.path.join(ASSETS, "proposal-issue.md")

sys.path.insert(0, HERE)
try:
    import spell                     # the derivation, generated into this skill
except ImportError:                  # a checkout of the guidelines repository
    sys.path.insert(0, os.path.join(SKILL, "..", "..", "tools"))
    import translit as spell         # noqa: E402

KINDS = ("entity", "concept", "classification", "classification_value", "property",
         "role", "process", "content", "analysis", "mark", "unit")


def load(path=DATA):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def collisions(data, code, arabic):
    """Entries this proposal may duplicate: by name, by spelling, by Arabic, by words."""
    import lookup
    index = lookup.build_index(data)
    hits = {}
    for term in [code, code.replace("_", " "), arabic]:
        concept, how = lookup.resolve(index, term)
        if concept:
            hits.setdefault(concept, f"`{term}` resolves to it ({how})")
    for concept in lookup.nearest(data, index, code, limit=5):
        hits.setdefault(concept, "a near match by name or definition")
    return hits


def fill(template, values):
    out = template
    for key, value in values.items():
        out = out.replace("{{" + key + "}}", str(value))
    left = sorted(set(re.findall(r"\{\{(\w+)\}\}", out)))
    if left:
        raise SystemExit(f"the template has placeholders nothing filled: {left}")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="+", metavar="[NAME] ARABIC",
                    help="the vocalized Arabic, optionally preceded by the code name you expect")
    ap.add_argument("--display", help="the English display form, if usage has settled one")
    ap.add_argument("--kind", choices=KINDS, default="concept")
    ap.add_argument("--category", help="one of the dictionary's categories")
    ap.add_argument("--parent", help="the classification this is a value of, when kind is classification_value")
    ap.add_argument("--plural-arabic", help="the Arabic plural, if it has one")
    ap.add_argument("--out", help="write the YAML draft here instead of printing it")
    ap.add_argument("--json", action="store_true", help="print the derivation and collisions as JSON")
    ap.add_argument("--data", default=DATA)
    args = ap.parse_args(argv)

    if len(args.terms) > 2:
        ap.error("give the vocalized Arabic, optionally preceded by one code name")
    expected = args.terms[0] if len(args.terms) == 2 else None
    arabic = args.terms[-1]
    if not re.search(r"[؀-ۿ]", arabic):
        ap.error(f"{arabic!r} is not Arabic: the last argument is the vocalized Arabic name")

    try:
        spell.check_vocalized(arabic)
        code = spell.code_spelling(arabic)
        derived_display = spell.display_spelling(arabic)
    except ValueError as exc:
        print(f"error: {exc}\n  The code spelling is derived from the vowels; write them "
              f"(سُورَة, not سورة) and run again.", file=sys.stderr)
        return 1
    if not code:
        print(f"error: nothing derives from {arabic!r}", file=sys.stderr)
        return 1

    notes = []
    if expected and expected != code:
        notes.append(f"the name you expected, `{expected}`, is not what the Arabic derives to: "
                     f"the code is `{code}` (sections 4-8), with no exceptions for taste. "
                     f"If `{expected}` is an established spelling, that is a decision for the "
                     f"standard's tables, not for this entry.")

    data = load(args.data)
    found = collisions(data, code, arabic)
    exact = [c for c, why in found.items() if "resolves" in why]
    categories = sorted({e["category"] for e in data["concepts"].values()})
    category = args.category or "TODO"
    if args.category and args.category not in categories:
        notes.append(f"`{args.category}` is not a category; the categories are "
                     + ", ".join(categories))

    result = {"arabic": arabic, "code": code, "display": args.display or derived_display,
              "display_is_derived": not args.display, "collisions": found, "notes": notes}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 1 if exact else 0

    print(f"{arabic} → `{code}`  display {result['display']}"
          + ("  (derived: measure usage before recording it)" if not args.display else ""))
    for note in notes:
        print(f"note: {note}")
    if found:
        print("\nthe dictionary already has, or nearly has, this concept:")
        for concept, why in found.items():
            e = data["concepts"][concept]
            print(f"  `{concept}` ({e.get('display')}) — {why}\n      {e.get('definition_en')}")
    if exact:
        print(f"\nstop: `{code}` already resolves to an entry. Add the spelling to that entry "
              f"upstream if it is missing there; do not propose a second concept for it.")
        return 1

    template = open(TEMPLATE, encoding="utf-8").read()
    draft = fill(template, {
        "CODE": code, "DISPLAY": result["display"], "ARABIC": arabic,
        "ARABIC_PLURAL": args.plural_arabic or "",
        "PLURAL": code + "s", "KIND": args.kind, "CATEGORY": category,
        "PARENT": args.parent or "", "CATEGORIES": ", ".join(categories),
        "RELATED": "\n".join(f"  - {c}" for c in found) or "  []",
    })
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(draft)
        print(f"\ndraft written to {args.out}")
    else:
        print("\n" + draft)
    print(open(CHECKLIST, encoding="utf-8").read().replace("{{CODE}}", code))
    return 0


if __name__ == "__main__":
    sys.exit(main())
