"""Build the alias index: every attested spelling resolves to one concept.

This is what lets the standard hold a single derivation rule while the
familiar spellings still find the entry. Any tool that accepts a term should
resolve it through this index first.
"""
import glob, json, os, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
OUT = os.path.join(ROOT, "standards/terminology/aliases.json")


def build():
    index, clashes = {}, []
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        e = yaml.safe_load(open(path, encoding="utf-8"))
        concept = e["concept"]
        names = e.get("names", {})
        forms = {concept, names.get("code", concept)}
        display = names.get("display")
        if display:
            forms.add(display.lower().replace("-", "_").replace(" ", "_"))
        # `deprecated` names are deliberately not resolved: they belong to
        # another concept, which is why they were deprecated.
        for a in e.get("alternative_spellings", []) or []:
            forms |= {a, a.replace("-", "_"), a.replace("_", "-")}
        for f in forms:
            if not f:
                continue
            if f in index and index[f] != concept:
                clashes.append((f, index[f], concept))
            index[f] = concept
    return index, clashes


if __name__ == "__main__":
    index, clashes = build()
    json.dump(index, open(OUT, "w"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"{len(index)} spellings resolving to {len(set(index.values()))} concepts")
    if clashes:
        print(f"\n{len(clashes)} spellings claimed by two concepts:")
        for f, a, b in clashes:
            print(f"  {f!r}: {a} and {b}")
        sys.exit(1)
