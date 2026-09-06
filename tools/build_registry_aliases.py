"""Build the registry alias index: every attested spelling of every member.

`build_aliases.py` does this for concepts, in one flat namespace, because a
concept name is meant to be unique across the whole standard. Members are not:
Hamzah is a reciter and also the mark, al-Tariq is a surah and tariq is a step
in a chain of transmission. Neither name is wrong, and neither should be bent
to keep the other happy.

So this index is namespaced by kind. `hamzah` still resolves to the mark;
`qiraah:hamzah` resolves to the reciter. A caller that knows which column it is
filling — and a caller always does — asks inside that namespace.

    python3 tools/build_registry_aliases.py
"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRIES = os.path.join(ROOT, "standards/terminology/registries")
OUT = os.path.join(ROOT, "standards/terminology/registry_aliases.json")

# Which column names the kind of each row. A registry with no such column is
# one kind throughout, named after the file.
KIND_COLUMN = {"qiraat": "kind"}
SINGULAR = {"surahs": "surah", "sajdah": "mawdi_al_sajdah",
            "ayah_numbering": "ayah_numbering_system"}


def read(path):
    header, rows = None, []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("#"):
            fields = line.lstrip("#").strip().split("\t")
            if len(fields) > 1:
                header = fields
            continue
        if line.strip():
            rows.append(line.split("\t"))
    return header, rows


def build():
    index, clashes = {}, []
    for path in sorted(glob.glob(os.path.join(REGISTRIES, "*.tsv"))):
        name = os.path.basename(path)[:-4]
        header, rows = read(path)
        if not header:
            continue
        col = {c: i for i, c in enumerate(header)}
        if "code" not in col:
            continue

        for row in rows:
            get = lambda c: row[col[c]].strip() if c in col and col[c] < len(row) else ""
            code = get("code")
            kind = get(KIND_COLUMN[name]) if name in KIND_COLUMN else SINGULAR.get(name, name)
            forms = {code}
            for field in ("display", "transliteration", "arabic"):
                v = get(field)
                if v:
                    forms.add(v.lower().replace("-", "_").replace(" ", "_"))
            for a in filter(None, (x.strip() for x in get("alternative_spellings").split(","))):
                forms |= {a, a.replace("-", "_"), a.replace("_", "-")}

            bucket = index.setdefault(kind, {})
            for f in forms:
                if not f:
                    continue
                if f in bucket and bucket[f] != code:
                    clashes.append((kind, f, bucket[f], code))
                bucket[f] = code
    return index, clashes


if __name__ == "__main__":
    index, clashes = build()
    json.dump(index, open(OUT, "w"), ensure_ascii=False, indent=1, sort_keys=True)
    total = sum(len(v) for v in index.values())
    members = sum(len(set(v.values())) for v in index.values())
    print(f"{total} spellings resolving to {members} members "
          f"in {len(index)} namespaces: {', '.join(sorted(index))}")
    if clashes:
        print(f"\n{len(clashes)} spellings claimed twice inside one namespace:")
        for kind, f, a, b in clashes:
            print(f"  {kind}:{f!r} — {a} and {b}")
        sys.exit(1)
