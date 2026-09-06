#!/usr/bin/env python3
"""Resolve a term to its entry in the terminology dictionary.

    python3 lookup.py aya              # any spelling resolves to its concept
    python3 lookup.py "Waqf Lazim" verse ayat "juz'" مصحف
    python3 lookup.py --search waqf    # every concept whose name or text matches
    python3 lookup.py --category qiraat
    python3 lookup.py --registry qiraat --member hafs
    python3 lookup.py aya --json       # any mode takes --json

Resolving before answering is the point: the dictionary holds one canonical
name per concept, and every attested spelling of it, so a term that looks
unfamiliar is usually a spelling that is already recorded. A term is matched
as written, then with its apostrophes, diacritics and doubled vowels folded,
then as Arabic with the vowel marks and a leading al- stripped. When nothing
resolves, the nearest entries are listed, so "no concept" is never the whole
answer.

Exit codes: 0 resolved, 1 something did not resolve or a list was empty,
2 usage.
"""
import argparse
import csv
import difflib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(HERE), "data")
DATA = os.path.join(DATA_DIR, "terminology.json")
REGISTRIES = os.path.join(DATA_DIR, "registries")

ARABIC = re.compile(r"[؀-ۿ]")
# Vowel marks, shaddah, sukun, tanwin, dagger alif, maddah, tatweel, Quranic annotation marks.
ARABIC_MARKS = re.compile(r"[ً-ْٰٓـۖ-ۭ]")
APOSTROPHES = "'’‘`ʿʾ"
HOW = {
    "alias": "",
    "arabic": " (matched on the Arabic name)",
    "gloss": " (an English gloss, not a name to use)",
    "plural": " (the code plural)",
    "arabic_plural": " (an Arabic plural — a collection is named with the code plural)",
    "deprecated": " (a deprecated name)",
}
# The columns a registry member is looked up by. A registry without any of them
# is matched on every column.
MEMBER_COLUMNS = ("code", "display", "alternative_spellings", "arabic", "other_arabic_names")


def load(path=DATA):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def normalise(term):
    """The written form as a key: lowercase, underscores, no apostrophes or diacritics."""
    key = unicodedata.normalize("NFKD", term.strip().lower())
    key = "".join(c for c in key if not unicodedata.combining(c) or ARABIC.match(c))
    for a in APOSTROPHES:
        key = key.replace(a, "")
    return re.sub(r"[\s\-]+", "_", key).strip("_")


def fold(key):
    """A looser key: doubled vowels collapsed, the way the code spelling writes them."""
    return re.sub(r"([aiu])\1+", r"\1", key)


def arabic_key(text):
    """Arabic without marks, with alif variants unified and a leading al- dropped."""
    bare = ARABIC_MARKS.sub("", text.strip())
    bare = re.sub("[أإآٱ]", "ا", bare).replace(" ", "_")
    return bare[2:] if bare.startswith("ال") and len(bare) > 3 else bare


def build_index(data):
    """Every written form → (concept, how). The first writer of a key wins, so
    the canonical forms and recorded spellings go in before the looser ones."""
    exact, folded, arabic = {}, {}, {}

    def put(form, concept, how):
        key = normalise(form)
        if key:
            exact.setdefault(key, (concept, how))
            folded.setdefault(fold(key), (concept, how))

    for form, concept in data["aliases"].items():
        put(form, concept, "alias")
    for concept, e in data["concepts"].items():
        if e.get("plural"):
            put(e["plural"], concept, "plural")
        for g in e.get("english_glosses") or []:
            put(g, concept, "gloss")
        for p in e.get("arabic_plurals") or []:
            put(p, concept, "arabic_plural")
        for d in e.get("deprecated") or []:
            put(d, concept, "deprecated")
        if e.get("arabic"):
            arabic.setdefault(arabic_key(e["arabic"]), (concept, "arabic"))
    return exact, folded, arabic


def resolve(index, term):
    exact, folded, arabic = index
    if ARABIC.search(term):
        return arabic.get(arabic_key(term), (None, None))
    key = normalise(term)
    return exact.get(key) or folded.get(fold(key)) or (None, None)


def haystack(code, e):
    return " ".join(str(x) for x in [
        code, e.get("display"), e.get("arabic"), e.get("definition_en"), e.get("purpose_en"),
        " ".join(e.get("english_glosses") or []), " ".join(e.get("alternative_spellings") or []),
        " ".join(e.get("deprecated") or [])]).lower()


def nearest(data, index, term, limit=6):
    """Candidates for a term that did not resolve: substring hits, then close spellings."""
    exact, _, arabic = index
    hits = []
    if ARABIC.search(term):
        key = arabic_key(term)
        hits = [c for k, (c, _) in arabic.items() if key and (key in k or k in key)]
    else:
        key = normalise(term)
        for part in [key] + [p for p in key.split("_") if len(p) > 2]:
            hits += [code for code, e in data["concepts"].items() if part in haystack(code, e)]
        close = difflib.get_close_matches(key, list(exact), n=limit, cutoff=0.75)
        hits += [exact[k][0] for k in close]
    seen, out = set(), []
    for c in hits:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out[:limit]


def show(data, code, how, term):
    e = data["concepts"][code]
    print(f"{term} → `{e['code']}`{HOW[how]}")
    if how == "deprecated":
        print("  deprecated  a retired name: it resolves so old data is not stranded, and it "
              "is not written in new code. What it used to mean is in the note and the "
              "related entries below.")
    print(f"  display     {e.get('display')}")
    if e.get("arabic"):
        print(f"  arabic      {e['arabic']}")
    print(f"  kind        {e['kind']}    category {e['category']}    "
          f"origin {e['origin']}    status {e['status']}")
    if e.get("plural"):
        print(f"  plural      {e['plural']}")
    if e.get("parent"):
        print(f"  parent      {e['parent']}")
    if e.get("part_of"):
        print(f"  part of     {e['part_of']}")
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
    if e.get("arabic_plurals"):
        print(f"  never       {', '.join(e['arabic_plurals'])} — the Arabic plural is not a name")
    if e.get("deprecated"):
        print(f"  deprecated  {', '.join(e['deprecated'])}")
    if e.get("related"):
        print(f"  related     {', '.join(e['related'])}")
    if e.get("status") != "adopted":
        print(f"  status      `{e['status']}`: a proposal, not a ruling — say so when you rely on it")


def rows_of(data, codes, extra):
    return [{"code": c, "display": data["concepts"][c].get("display"),
             "category": data["concepts"][c]["category"],
             "kind": data["concepts"][c]["kind"], **extra(c)} for c in codes]


def print_rows(rows, third):
    for r in rows:
        print(f"{r['code']:34} {(r.get('display') or ''):26} {r[third]}")


def search(data, needle, as_json):
    needle = needle.lower()
    codes = sorted(c for c, e in data["concepts"].items() if needle in haystack(c, e))
    rows = rows_of(data, codes, lambda c: {})
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
    else:
        print_rows(rows, "category")
        print(f"{len(rows)} concepts match `{needle}`")
    return 0 if rows else 1


def category(data, name, as_json):
    codes = sorted(c for c, e in data["concepts"].items() if e["category"] == name)
    rows = rows_of(data, codes, lambda c: {})
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
    else:
        print_rows(rows, "kind")
        print(f"{len(rows)} concepts in `{name}`")
    if not rows:
        have = sorted({e["category"] for e in data["concepts"].values()})
        print(f"no category `{name}`. categories: {', '.join(have)}", file=sys.stderr)
        return 1
    return 0


def read_registry(path):
    """A registry is a comment block, whose last line names the columns, then rows."""
    try:
        from registry import read      # the shared reader, generated beside this script
        return read(path)
    except ImportError:
        pass
    header, rows = [], []
    with open(path, encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if not row or not row[0].strip():
                continue
            if row[0].startswith("#"):
                header = [c.lstrip("# ").strip() for c in row]
            else:
                rows.append(row)
    return header, rows


def registry(name, member, as_json, registries=REGISTRIES):
    path = os.path.join(registries, f"{name}.tsv")
    have = sorted(f[:-4] for f in os.listdir(registries) if f.endswith(".tsv")) \
        if os.path.isdir(registries) else []
    if not os.path.exists(path):
        print(f"no registry `{name}`. registries: {', '.join(have)}", file=sys.stderr)
        return 1
    header, rows = read_registry(path)
    if member:
        key = normalise(member)
        akey = arabic_key(member) if ARABIC.search(member) else None
        columns = [i for i, h in enumerate(header) if h in MEMBER_COLUMNS] or range(len(header) or 99)

        def matches(row):
            for i in columns:
                if i >= len(row):
                    continue
                for cell in row[i].split(","):
                    cell = cell.strip()
                    if akey is not None:
                        if arabic_key(cell) == akey:
                            return True
                    elif normalise(cell) == key or fold(normalise(cell)) == fold(key):
                        return True
            return False
        rows = [r for r in rows if matches(r)]
    if as_json:
        print(json.dumps([dict(zip(header, r)) if header else r for r in rows],
                         ensure_ascii=False, indent=1))
    else:
        if header:
            print("# " + " | ".join(header))
        for r in rows:
            print("\t".join(r))
        print(f"{len(rows)} rows" + (f" match `{member}` in `{name}`" if member else f" in `{name}`"))
    return 0 if rows else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="terms to resolve, in any spelling or in Arabic")
    ap.add_argument("--search", help="substring search over names, spellings and definitions")
    ap.add_argument("--category", help="list the concepts in a category")
    ap.add_argument("--registry", help="print a registry of a closed set")
    ap.add_argument("--member", help="filter the registry to the rows naming this member")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--data", default=DATA, help="path to terminology.json")
    args = ap.parse_args(argv)

    try:
        data = load(args.data)
    except (OSError, ValueError) as exc:
        print(f"could not read {args.data}: {exc}", file=sys.stderr)
        return 2
    if args.registry:
        return registry(args.registry, args.member, args.json,
                        os.path.join(os.path.dirname(os.path.abspath(args.data)), "registries"))
    if args.search:
        return search(data, args.search, args.json)
    if args.category:
        return category(data, args.category, args.json)
    if not args.terms:
        ap.print_help()
        return 2

    index = build_index(data)
    out, missing = {}, []
    for i, term in enumerate(args.terms):
        code, how = resolve(index, term)
        if not code:
            missing.append(term)
            continue
        if args.json:
            out[term] = {"concept": code, "resolved_as": how, **data["concepts"][code]}
        else:
            if i:
                print()
            show(data, code, how, term)
    for term in missing:
        near = nearest(data, index, term)
        if args.json:
            out[term] = {"concept": None, "nearest": near}
        else:
            hint = ("nearest: " + ", ".join(f"`{c}`" for c in near)) if near else \
                "nothing close. Try --search with a word of the definition."
            print(f"{term}: no concept resolves to it. {hint}\n"
                  f"  If it is genuinely new, see section 30 of references/standard.md "
                  f"and scripts/propose.py.", file=sys.stderr)
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
