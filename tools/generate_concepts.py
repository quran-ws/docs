"""Generate concept entries from the dictionary and the vocalization table.

Section 3 decides whether a term keeps its Arabic name; only then do sections
4 to 8 decide how to spell it. So `origin` drives the code name:

    quranic   → derived from names.arabic.vocalized
    borrowed  → the English term, which is the point of calling it borrowed
    standard  → the English name we coined for it
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import yaml
from translit import code_spelling, display_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT = os.path.join(ROOT, "content/ar/03-terminology/dictionary.md")
VOC = os.path.join(ROOT, "standards/terminology/data/vocalization.tsv")
OUT = os.path.join(ROOT, "standards/terminology/concepts")

SECTION_CATEGORY = {
    "Core": "core", "Structure": "structure", "Text": "text",
    "Quran Divisions": "divisions", "Surah Classification": "surah_classification",
    "Mushaf & Layout": "mushaf", "Mushaf Marks": "mushaf_marks",
    "Ayah Numbering": "ayah_numbering", "Revelation": "revelation",
    "Qiraat": "qiraat", "Recitation": "recitation",
    "Recitation Pace": "recitation_pace", "Recitation Style": "recitation_style",
    "Tajwid": "tajwid", "Waqf": "waqf", "Linguistics": "linguistics",
    "Translation": "translation", "Tafsir": "tafsir",
}
# Section 12's closed list absorbs the kinds the dictionary had invented.
KIND = {
    "textual_concept": "concept", "recitation_concept": "concept",
    "presentation_concept": "concept", "orthographic_concept": "concept",
    "text_unit": "unit", "technical_unit": "unit", "typographic_unit": "unit",
    "layout_unit": "unit", "linguistic_unit": "unit", "division": "entity",
    "recitation_feature": "concept", "recitation_practice": "concept",
    "practice": "concept", "discipline": "concept", "location": "property",
    "rasm_type": "classification_value", "quran_name": "classification_value",
}


def load_vocalization():
    rows = {}
    for r in csv.reader(open(VOC, encoding="utf-8"), delimiter="\t"):
        if not r or r[0].startswith("#"):
            continue
        rows[r[0]] = {"vocalized": r[1] if len(r) > 1 else "",
                      "origin": r[2] if len(r) > 2 else "quranic"}
    return rows


def field(body, name):
    m = re.search(rf"\*\*{name}:?\*\*\s*(.+?)(?:\n\n|\n\*\*|$)", body, re.S)
    return m.group(1).strip().strip("`") if m else None


def parse():
    text = open(DICT, encoding="utf-8").read()
    entries, section = [], None
    for m in re.finditer(r"^# \d+\. (.+?)$|^## (.+?)$(.*?)(?=^#{1,2} |\Z)", text, re.M | re.S):
        if m.group(1):
            section = m.group(1).strip()
            continue
        heading, body = m.group(2).strip(), m.group(3)
        canonical = field(body, "Canonical")
        if not canonical or section not in SECTION_CATEGORY:
            continue
        entries.append({
            "heading": heading, "section": section, "canonical": canonical, "body": body,
        })
    return entries


def build():
    voc = load_vocalization()
    made, missing = [], []
    for e in parse():
        canonical, body = e["canonical"], e["body"]
        v = voc.get(canonical)
        arabic_display = e["heading"].split(" — ")[-1].strip()
        if v is None:
            missing.append(canonical)
            continue
        origin = v["origin"]
        if origin == "quranic" and v["vocalized"]:
            code = code_spelling(v["vocalized"])
            display = display_spelling(v["vocalized"])
            # The dictionary's own English form wins as the display name.
            if not re.match(r"^[a-z_]+$", canonical):
                display = canonical
        else:
            code = canonical.lower().replace(" ", "_").replace("-", "_").replace("'", "")
            display = canonical if not re.match(r"^[a-z_]+$", canonical) else \
                " ".join(w.capitalize() for w in canonical.split("_"))

        raw_kind = field(body, "Kind") or "concept"
        kind = KIND.get(raw_kind, raw_kind)
        parent = field(body, "Parent")
        alts = []
        for label in ("Alternative", "Alternatives", "Alternative spelling",
                      "Alternative spellings", "Transliteration"):
            val = field(body, label)
            if val:
                alts += [a.strip().strip("`") for a in val.split(",")]
        entry = {
            "concept": code,
            "names": {
                "code": code,
                "display": display,
                **({"arabic": {"vocalized": v["vocalized"], "singular": arabic_display}}
                   if v["vocalized"] else {}),
            },
            "kind": kind,
            "category": SECTION_CATEGORY[e["section"]],
            **({"parent": parent.lower().replace(" ", "_").replace("-", "_")} if parent else {}),
            "origin": origin,
            "tier": "extended" if field(body, "Tier") == "extended" else "core",
            "status": "draft",
            **({"plural": (field(body, "Plural") or "").lower().replace(" ", "_").replace("-", "_")}
               if field(body, "Plural") else {}),
            "definition": (field(body, "Definition") or "").replace("\n", " ").strip(),
            "purpose": (field(body, "Purpose") or "").replace("\n", " ").strip(),
            **({"alternative_spellings": sorted({a.lower().replace(" ", "_") for a in alts if a} - {code})}
               if alts else {}),
            **({"english_glosses": [g.strip().strip("`") for g in
                (field(body, "English gloss") or field(body, "English glosses") or "").split(",") if g.strip()]}
               if (field(body, "English gloss") or field(body, "English glosses")) else {}),
            "sources": [],
        }
        made.append(entry)
    return made, missing


if __name__ == "__main__":
    made, missing = build()
    os.makedirs(OUT, exist_ok=True)
    written = 0
    for e in made:
        path = os.path.join(OUT, f"{e['concept']}.yml")
        if os.path.exists(path):          # never clobber a generated mark entry
            continue
        yaml.safe_dump(e, open(path, "w", encoding="utf-8"),
                       allow_unicode=True, sort_keys=False, width=88)
        written += 1
    print(f"{written} new entries written, {len(made)} parsed")
    if missing:
        print(f"{len(missing)} without a vocalization row: {', '.join(missing[:12])}")
