"""Render the dictionary pages from the concept files.

Section 29 of the standard: the machine-readable source is the dictionary, and
the human-readable page is generated from it. Nothing here is hand-written, so
the page cannot drift from the data.

Both locales come out of the same entries. Arabic reads `definition`, English
reads `definition_en`, and they are translations of one another, so the two
pages say the same thing by construction.

    python3 tools/generate_dictionary.py
"""
import glob, os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")

CATEGORIES = [
    ("core", "الأساس", "Core"),
    ("structure", "البنية", "Structure"),
    ("text", "النص", "Text"),
    ("divisions", "أقسام القرآن", "Quran divisions"),
    ("surah_classification", "تصنيف السور", "Surah classification"),
    ("mushaf", "المصحف والتخطيط", "Mushaf and layout"),
    ("dabt", "الضبط", "Dabt"),
    ("mushaf_marks", "علامات المصحف", "Mushaf marks"),
    ("ayah_numbering", "عد الآي", "Ayah numbering"),
    ("revelation", "النزول", "Revelation"),
    ("qiraat", "القراءات", "Qiraat"),
    ("recitation", "التلاوة", "Recitation"),
    ("recitation_pace", "مراتب القراءة", "Recitation pace"),
    ("recitation_style", "أنماط الأداء", "Recitation style"),
    ("tajwid", "التجويد", "Tajwid"),
    ("waqf", "الوقف", "Waqf"),
    ("linguistics", "اللغة", "Linguistics"),
    ("translation", "الترجمة", "Translation"),
    ("tafsir", "التفسير", "Tafsir"),
    ("quranic_sciences", "علوم القرآن", "Quranic sciences"),
]
# Field values are written exactly as they appear in the concept file, so a
# reader can copy them into YAML. Their meaning belongs in the standard
# (sections 12 and 13), not repeated on every entry.

AR = {
    "out": "content/ar/03-terminology/dictionary.md",
    "label": 1,
    "definition": "definition", "purpose": "purpose",
    "boundaries": "boundaries", "note": "note",
    "front": """---
title: قاموس المصطلحات
description: المفاهيم المستخدمة في البرمجيات القرآنية، بتعريفاتها وأسمائها المعتمدة.
status: draft
sidebar:
  order: 2
---

:::caution[هذه الصفحة مولّدة]
مصدرها `standards/terminology/concepts/*.yml`. لا تعدلها هنا، بل عدل المدخل
ثم شغّل `python3 tools/generate_dictionary.py`.
:::
""",
    "rows": {"vocalized": "بالحركات", "symbol": "الرمز", "unicode": "المحارف",
             "alternative": "تهجئات أخرى", "deprecated": "أسماء متروكة",
             "gloss": "مقابل إنجليزي"},
    "definition_label": "**التعريف:**", "purpose_label": "**الغرض:**",
    "sep": "، ",
}

EN = {
    "out": "content/en/03-terminology/dictionary.md",
    "label": 2,
    "definition": "definition_en", "purpose": "purpose_en",
    "boundaries": "boundaries_en", "note": "note_en",
    "front": """---
title: Terminology dictionary
description: The concepts used in Quranic software, with their definitions and their adopted names.
status: draft
sidebar:
  order: 2
---

:::caution[This page is generated]
It comes from `standards/terminology/concepts/*.yml`. Do not edit it here: edit
the entry, then run `python3 tools/generate_dictionary.py`.
:::
""",
    "rows": {"vocalized": "Vocalized", "symbol": "Symbol", "unicode": "Characters",
             "alternative": "Other spellings", "deprecated": "Deprecated names",
             "gloss": "English gloss"},
    "definition_label": "**Definition:**", "purpose_label": "**Purpose:**",
    "sep": ", ",
}


def load():
    out = []
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        out.append(yaml.safe_load(open(path, encoding="utf-8")))
    return out


def render_entry(e, loc):
    n = e.get("names", {})
    arabic = n.get("arabic", {}).get("singular") or n.get("arabic", {}).get("vocalized", "")
    lines = [f"### {n.get('display', e['concept'])} — {arabic}".rstrip(" —")]
    lines.append("")
    rows = [("`code`", f"`{n.get('code', e['concept'])}`")]
    if e.get("plural"):
        rows.append(("`plural`", f"`{e['plural']}`"))
    rows.append(("`kind`", f"`{e['kind']}`"))
    if e.get("parent"):
        rows.append(("`parent`", f"`{e['parent']}`"))
    if n.get("arabic", {}).get("vocalized"):
        rows.append((loc["rows"]["vocalized"], n["arabic"]["vocalized"]))
    if e.get("symbol"):
        rows.append((loc["rows"]["symbol"], e["symbol"]))
    if e.get("unicode"):
        cps = loc["sep"].join(f"`{u['cp']}`" for u in e["unicode"])
        rows.append((loc["rows"]["unicode"], cps))
    if e.get("alternative_spellings"):
        rows.append((loc["rows"]["alternative"],
                     loc["sep"].join(f"`{a}`" for a in e["alternative_spellings"])))
    if e.get("deprecated"):
        rows.append((loc["rows"]["deprecated"],
                     loc["sep"].join(f"`{a}`" for a in e["deprecated"])))
    if e.get("english_glosses"):
        rows.append((loc["rows"]["gloss"],
                     loc["sep"].join(f"`{g}`" for g in e["english_glosses"])))

    lines.append("| | |")
    lines.append("| --- | --- |")
    for k, v in rows:
        lines.append(f"| {k} | {v} |")
    lines.append("")
    if e.get(loc["definition"]):
        lines.append(f"{loc['definition_label']} {e[loc['definition']].strip()}")
        lines.append("")
    if e.get(loc["purpose"]):
        lines.append(f"{loc['purpose_label']} {e[loc['purpose']].strip()}")
        lines.append("")
    for b in e.get(loc["boundaries"], []) or []:
        lines.append(f"- {b}")
    if e.get(loc["boundaries"]):
        lines.append("")
    if e.get(loc["note"]):
        lines.append(f"> {e[loc['note']].strip()}")
        lines.append("")
    return "\n".join(lines)


def render(entries, loc):
    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    parts, total = [loc["front"]], 0
    for row in CATEGORIES:
        key, label = row[0], row[loc["label"]]
        group = sorted(by_cat.get(key, []), key=lambda x: x["concept"])
        if not group:
            continue
        parts.append(f"\n## {label} — `{key}`\n")
        for e in group:
            parts.append(render_entry(e, loc))
            total += 1
    out = os.path.join(ROOT, loc["out"])
    open(out, "w", encoding="utf-8").write("\n".join(parts))
    print(f"{total} entries rendered into {os.path.relpath(out, ROOT)}")


def main():
    entries = load()
    for loc in (AR, EN):
        render(entries, loc)
    missing = {e["category"] for e in entries} - {row[0] for row in CATEGORIES}
    if missing:
        print("categories with no label:", missing)


if __name__ == "__main__":
    main()
