"""Render the dictionary page from the concept files.

Section 29 of the standard: the machine-readable source is the dictionary, and
the human-readable page is generated from it. Nothing here is hand-written, so
the page cannot drift from the data.

    python3 tools/generate_dictionary.py
"""
import glob, os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
OUT = os.path.join(ROOT, "content/ar/03-terminology/dictionary.md")

CATEGORY_AR = [
    ("core", "الأساس"), ("structure", "البنية"), ("text", "النص"),
    ("divisions", "أقسام القرآن"), ("surah_classification", "تصنيف السور"),
    ("mushaf", "المصحف والتخطيط"), ("dabt", "الضبط"),
    ("mushaf_marks", "علامات المصحف"), ("ayah_numbering", "عد الآي"),
    ("revelation", "النزول"), ("qiraat", "القراءات"),
    ("recitation", "التلاوة"), ("recitation_pace", "مراتب القراءة"),
    ("recitation_style", "أنماط الأداء"), ("tajwid", "التجويد"),
    ("waqf", "الوقف"), ("linguistics", "اللغة"),
    ("translation", "الترجمة"), ("tafsir", "التفسير"),
    ("quranic_sciences", "علوم القرآن"),
]
# Field values are written exactly as they appear in the concept file, so a
# reader can copy them into YAML. Their Arabic meaning belongs in the standard
# (sections 12 and 13), not repeated on every entry.


def load():
    out = []
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        out.append(yaml.safe_load(open(path, encoding="utf-8")))
    return out


def render_entry(e):
    n = e.get("names", {})
    lines = [f"### {n.get('display', e['concept'])} — {n.get('arabic', {}).get('singular') or n.get('arabic', {}).get('vocalized', '')}".rstrip(" —")]
    lines.append("")
    rows = [("`code`", f"`{n.get('code', e['concept'])}`")]
    if e.get("plural"):
        rows.append(("`plural`", f"`{e['plural']}`"))
    rows.append(("`kind`", f"`{e['kind']}`"))
    if e.get("parent"):
        rows.append(("`parent`", f"`{e['parent']}`"))
    if n.get("arabic", {}).get("vocalized"):
        rows.append(("بالحركات", n["arabic"]["vocalized"]))
    if e.get("symbol"):
        rows.append(("الرمز", e["symbol"]))
    if e.get("unicode"):
        cps = "، ".join(f"`{u['cp']}`" for u in e["unicode"])
        rows.append(("المحارف", cps))
    if e.get("alternative_spellings"):
        rows.append(("تهجئات أخرى", "، ".join(f"`{a}`" for a in e["alternative_spellings"])))
    if e.get("deprecated"):
        rows.append(("أسماء متروكة", "، ".join(f"`{a}`" for a in e["deprecated"])))
    if e.get("english_glosses"):
        rows.append(("مقابل إنجليزي", "، ".join(f"`{g}`" for g in e["english_glosses"])))

    lines.append("| | |")
    lines.append("| --- | --- |")
    for k, v in rows:
        lines.append(f"| {k} | {v} |")
    lines.append("")
    if e.get("definition"):
        lines.append(f"**التعريف:** {e['definition'].strip()}")
        lines.append("")
    if e.get("purpose"):
        lines.append(f"**الغرض:** {e['purpose'].strip()}")
        lines.append("")
    for b in e.get("boundaries", []) or []:
        lines.append(f"- {b}")
    if e.get("boundaries"):
        lines.append("")
    if e.get("note"):
        lines.append(f"> {e['note'].strip()}")
        lines.append("")
    return "\n".join(lines)


def main():
    entries = load()
    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    parts = ["""---
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
"""]
    total = 0
    for key, label in CATEGORY_AR:
        group = sorted(by_cat.get(key, []), key=lambda x: x["concept"])
        if not group:
            continue
        parts.append(f"\n## {label} — `{key}`\n")
        for e in group:
            parts.append(render_entry(e))
            total += 1
    open(OUT, "w", encoding="utf-8").write("\n".join(parts))
    print(f"{total} entries rendered into {os.path.relpath(OUT, ROOT)}")
    missing = {e["category"] for e in entries} - {k for k, _ in CATEGORY_AR}
    if missing:
        print("categories with no Arabic label:", missing)


if __name__ == "__main__":
    main()
