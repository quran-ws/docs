#!/usr/bin/env python3
"""Resolve a term to its entry in the terminology dictionary.

    python3 lookup.py aya              # any spelling resolves to its concept
    python3 lookup.py "Waqf Lazim" verse
    python3 lookup.py --search waqf    # every concept whose name or text matches
    python3 lookup.py --category qiraat
    python3 lookup.py --registry qiraat --member hafs
    python3 lookup.py aya --json

Resolving before answering is the point: the dictionary holds one canonical
name per concept, and every attested spelling of it, so a term that looks
unfamiliar is usually a spelling that is already recorded.
"""
import argparse
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(HERE), "data")
DATA = os.path.join(DATA_DIR, "terminology.json")
REGISTRIES = os.path.join(DATA_DIR, "registries")


def load():
    with open(DATA, encoding="utf-8") as fh:
        return json.load(fh)


def normalise(term):
    return term.strip().lower().replace("-", "_").replace(" ", "_")


def resolve(data, term):
    key = normalise(term)
    concept = data["aliases"].get(key)
    if concept:
        return concept, "alias"
    for code, e in data["concepts"].items():
        if key in {normalise(g) for g in e.get("english_glosses") or []}:
            return code, "gloss"
        if key in {normalise(d) for d in e.get("deprecated") or []}:
            return code, "deprecated"
    return None, None


def show(data, code, how, term):
    e = data["concepts"][code]
    note = {"alias": "", "gloss": " (an English gloss, not a name to use)",
            "deprecated": " (a deprecated name)"}[how]
    print(f"{term} → `{e['code']}`{note}")
    print(f"  display     {e.get('display')}")
    if e.get("arabic"):
        print(f"  arabic      {e['arabic']}")
    print(f"  kind        {e['kind']}    category {e['category']}    "
          f"origin {e['origin']}    status {e['status']}")
    if e.get("plural"):
        print(f"  plural      {e['plural']}")
    if e.get("parent"):
        print(f"  parent      {e['parent']}")
    if e.get("registry"):
        print(f"  registry    {e['registry']} (its members are rows, not entries)")
    print(f"  definition  {e.get('definition_en')}")
    print(f"  purpose     {e.get('purpose_en')}")
    for b in e.get("boundaries_en") or []:
        print(f"  boundary    {b}")
    if e.get("note_en"):
        print(f"  note        {e['note_en']}")
    if e.get("alternative_spellings"):
        print(f"  spellings   {', '.join(e['alternative_spellings'])}")
    if e.get("english_glosses"):
        print(f"  glosses     {', '.join(e['english_glosses'])} — search keys, not names")
    if e.get("deprecated"):
        print(f"  deprecated  {', '.join(e['deprecated'])}")
    if e.get("related"):
        print(f"  related     {', '.join(e['related'])}")


def search(data, needle):
    needle = needle.lower()
    hits = []
    for code, e in data["concepts"].items():
        haystack = " ".join(str(x) for x in [
            code, e.get("display"), e.get("arabic"), e.get("definition_en"),
            e.get("purpose_en"), " ".join(e.get("english_glosses") or []),
            " ".join(e.get("alternative_spellings") or [])]).lower()
        if needle in haystack:
            hits.append((code, e))
    for code, e in sorted(hits):
        print(f"{code:34} {e.get('display', ''):26} {e['category']}")
    print(f"{len(hits)} concepts")


def category(data, name):
    rows = [(c, e) for c, e in data["concepts"].items() if e["category"] == name]
    for code, e in sorted(rows):
        print(f"{code:34} {e.get('display', ''):26} {e['kind']}")
    print(f"{len(rows)} concepts in `{name}`")
    if not rows:
        print("categories:", ", ".join(sorted({e['category'] for e in data['concepts'].values()})))


def registry(name, member=None):
    path = os.path.join(REGISTRIES, f"{name}.tsv")
    if not os.path.exists(path):
        have = sorted(f[:-4] for f in os.listdir(REGISTRIES) if f.endswith(".tsv"))
        print(f"no registry `{name}`. registries: {', '.join(have)}")
        return 1
    # The registries carry their column names in the last comment line before
    # the rows, so the file reads as a comment block and then data.
    header, rows = [], []
    with open(path, encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if not row or not row[0].strip():
                continue
            if row[0].startswith("#"):
                header = [c.lstrip("# ").strip() for c in row]
            else:
                rows.append(row)
    if member:
        key = normalise(member)
        rows = [r for r in rows if any(normalise(cell) == key or key in normalise(cell)
                                       for cell in r)]
    if header:
        print("# " + " | ".join(header))
    for r in rows:
        print("\t".join(r))
    print(f"{len(rows)} rows")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="terms to resolve")
    ap.add_argument("--search", help="substring search over names and definitions")
    ap.add_argument("--category", help="list the concepts in a category")
    ap.add_argument("--registry", help="print a registry of a closed set")
    ap.add_argument("--member", help="filter the registry to matching rows")
    ap.add_argument("--json", action="store_true", help="print the entries as JSON")
    args = ap.parse_args()

    data = load()
    if args.registry:
        return registry(args.registry, args.member)
    if args.search:
        search(data, args.search)
        return 0
    if args.category:
        category(data, args.category)
        return 0
    if not args.terms:
        ap.print_help()
        return 2

    out, missing = {}, []
    for i, term in enumerate(args.terms):
        code, how = resolve(data, term)
        if not code:
            missing.append(term)
            continue
        if args.json:
            out[term] = data["concepts"][code]
        else:
            if i:
                print()
            show(data, code, how, term)
    if args.json:
        json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
        print()
    for term in missing:
        print(f"{term}: no concept. Try --search, and see the rule for accepting a new "
              f"term in references/standard.md.", file=sys.stderr)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
