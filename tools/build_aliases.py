"""Build the alias index: every attested spelling resolves to one concept.

This is what lets the standard hold a single derivation rule while the
familiar spellings still find the entry. Any tool that accepts a term should
resolve it through this index first.

One exception, from section 14: a value's name is unique within its
classification, not across the dictionary, because a column holds the values
of one classification and never two. So `makki` is a value of
`revelation_classification` and of `ayah_numbering_system`. Such a form maps
to the list of its concepts, and `<parent>:<form>` maps to each one, so a
caller that knows the column resolves without ambiguity. Any other shared
form is a clash and stops the build.
"""
import glob, json, os, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
OUT = os.path.join(ROOT, "standards/terminology/aliases.json")


def build():
    index, clashes, owners, values = {}, [], {}, {}
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        e = yaml.safe_load(open(path, encoding="utf-8"))
        concept = e["concept"]
        names = e.get("names", {})
        if e.get("kind") == "classification_value" and e.get("parent"):
            values[concept] = e["parent"]
        forms = {concept, names.get("code", concept)}
        display = names.get("display")
        if display:
            forms.add(display.lower().replace("-", "_").replace(" ", "_"))
        # `deprecated` names are deliberately not resolved: they belong to
        # another concept, which is why they were deprecated.
        for a in e.get("alternative_spellings", []) or []:
            forms |= {a, a.replace("-", "_"), a.replace("_", "-")}
        for f in forms:
            if f and concept not in owners.setdefault(f, []):
                owners[f].append(concept)
    for f, concepts in owners.items():
        if len(concepts) == 1:
            index[f] = concepts[0]
            continue
        parents = [values.get(c) for c in concepts]
        if all(parents) and len(set(parents)) == len(parents):
            index[f] = concepts
            for c, parent in zip(concepts, parents):
                index[f"{parent}:{f}"] = c
        else:
            clashes.append((f, concepts[0], concepts[1]))
    return index, clashes


if __name__ == "__main__":
    index, clashes = build()
    if clashes:
        # Nothing is written: a half-right index on disk is worse than the old one.
        print(f"{len(clashes)} spellings claimed by two concepts:")
        for f, a, b in clashes:
            print(f"  {f!r}: {a} and {b}")
        sys.exit(1)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    concepts = {c for v in index.values() for c in (v if isinstance(v, list) else [v])}
    shared = sorted(f for f, v in index.items() if isinstance(v, list))
    print(f"{len(index)} spellings resolving to {len(concepts)} concepts"
          + (f"; shared between classifications: {', '.join(shared)}" if shared else ""))
