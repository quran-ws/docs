"""Render the dictionary pages from the concept files.

Section 29 of the standard: the machine-readable source is the dictionary, and
the human-readable page is generated from it. Nothing here is hand-written, so
the page cannot drift from the data.

Both locales come out of the same entries. Arabic reads `definition`, English
reads `definition_en`, and they are translations of one another, so the two
pages say the same thing by construction.

Each page has three parts:

  1. a lookup table, one row per concept sorted by code, so a reader who knows
     the code, the display name, the Arabic word or the idea can find the row
     and jump to the entry;
  2. a "by category" block listing every code under its category;
  3. the entries themselves, one per concept, grouped by category.

Every entry carries a stable anchor equal to its code (`<a id="ayah">`), on the
site and on GitHub alike, so `related`, `parent`, `part_of` and the lookup
table can link to it, and so a link survives a change of display name.

    python3 tools/generate_dictionary.py
"""
import glob, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
SOURCES = os.path.join(ROOT, "standards/terminology/sources.yml")

# Every category an entry may use, in page order. An entry whose category is
# not here stops the build: the page must never silently drop an entry.
CATEGORIES = [
    ("core", "الأساس", "Core"),
    ("structure", "البنية", "Structure"),
    ("text", "النص", "Text"),
    ("divisions", "أقسام القرآن", "Quran divisions"),
    ("surah_classification", "تصنيف السور", "Surah classification"),
    ("mushaf", "المصحف والتخطيط", "Mushaf and layout"),
    ("dabt", "الضبط وعلامات المصحف", "Dabt and Mushaf marks"),
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

BANNER_AR = """> مولّد من `standards/terminology/concepts/*.yml` — عدّل المدخل لا هذه الصفحة،
> ثم شغّل `python3 tools/build.py`."""
BANNER_EN = """> Generated from `standards/terminology/concepts/*.yml` — edit the entry, not
> this page, then run `python3 tools/build.py`."""

AR = {
    "code": "ar",
    "out": "content/ar/reference/dictionary.md",
    "label": 1,
    "definition": "definition", "purpose": "purpose",
    "boundaries": "boundaries", "note": "note",
    "front": """---
title: قاموس المصطلحات
description: المفاهيم المستخدمة في البرمجيات القرآنية، بتعريفاتها وأسمائها المعتمدة.
status: draft
sidebar:
  order: 2
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
""" + BANNER_AR + "\n",
    "lookup_h": "البحث السريع",
    "lookup_intro": "مدخل لكل مفهوم، مرتبة بالاسم. اضغط الاسم للوصول إلى المدخل كاملًا.",
    "lookup_cols": ["الاسم", "العرض", "العربية", "النوع", "المجال", "التعريف"],
    "bycat_h": "حسب المجال",
    "field_cols": ["الحقل", "القيمة"],
    "rows": {
        "plural": "`plural`", "kind": "`kind`", "parent": "الأب",
        "children": "الأبناء", "values": "القيم", "part_of": "جزء من",
        "origin": "الأصل", "tier": "المستوى", "status": "الحالة",
        "vocalized": "بالحركات", "arabic_plural": "الجمع",
        "transliteration": "النقحرة", "dabt": "اسمه في الضبط",
        "by_shape": "اسمه بشكله", "mushaf_introduction": "اسمه في تعريف المصحف",
        "symbol": "الرمز", "unicode": "المحارف", "mark_family": "عائلة العلامة",
        "registry": "السجل", "alternative": "تهجئات أخرى",
        "deprecated": "أسماء متروكة", "gloss": "مقابل إنجليزي",
        "display_evidence": "دليل اسم العرض",
    },
    "definition_label": "**التعريف:**", "purpose_label": "**الغرض:**",
    "related_label": "**مرتبط به:**", "sources_label": "**المصادر:**",
    "sep": "، ", "ltr": True,
}

EN = {
    "code": "en",
    "out": "content/en/reference/dictionary.md",
    "label": 2,
    "definition": "definition_en", "purpose": "purpose_en",
    "boundaries": "boundaries_en", "note": "note_en",
    "front": """---
title: Terminology dictionary
description: The concepts used in Quranic software, with their definitions and their adopted names.
status: draft
sidebar:
  order: 2
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
""" + BANNER_EN + "\n",
    "lookup_h": "Lookup",
    "lookup_intro": "One row per concept, sorted by code. Follow the code to the full entry.",
    "lookup_cols": ["code", "display", "Arabic", "kind", "category", "definition"],
    "bycat_h": "By category",
    "field_cols": ["field", "value"],
    "rows": {
        "plural": "`plural`", "kind": "`kind`", "parent": "Parent",
        "children": "Children", "values": "Values", "part_of": "Part of",
        "origin": "Origin", "tier": "Tier", "status": "Status",
        "vocalized": "Vocalized", "arabic_plural": "Arabic plural",
        "transliteration": "Transliteration", "dabt": "Dabt name",
        "by_shape": "Name by shape", "mushaf_introduction": "Mushaf introduction name",
        "symbol": "Symbol", "unicode": "Characters", "mark_family": "Mark family",
        "registry": "Registry", "alternative": "Other spellings",
        "deprecated": "Deprecated names", "gloss": "English gloss",
        "display_evidence": "Display evidence",
    },
    "definition_label": "**Definition:**", "purpose_label": "**Purpose:**",
    "related_label": "**Related:**", "sources_label": "**Sources:**",
    "sep": ", ", "ltr": False,
}


def load():
    out = []
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        out.append(yaml.safe_load(open(path, encoding="utf-8")))
    return out


def load_sources():
    if not os.path.exists(SOURCES):
        return {}
    return yaml.safe_load(open(SOURCES, encoding="utf-8")) or {}


def cell(text):
    """One line, safe inside a markdown table cell."""
    return re.sub(r"\s+", " ", str(text)).replace("|", "\\|").strip()


def first_sentence(text):
    text = re.sub(r"\s+", " ", text or "").strip()
    m = re.match(r"(.*?[.؟?!])(\s|$)", text)
    return m.group(1) if m else text


def ltr(value, loc):
    """Latin runs inside an Arabic cell keep their own direction."""
    return f'<span dir="ltr">{value}</span>' if loc["ltr"] else value


def codes(values, loc):
    return ltr(loc["sep"].join(f"`{v}`" for v in values), loc)


def dedupe(values):
    return list(dict.fromkeys(values or []))


class Index:
    """Everything an entry needs to know about the other entries."""

    def __init__(self, entries):
        self.by_code = {e["concept"]: e for e in entries}
        self.related = {e["concept"]: dedupe(e.get("related")) for e in entries}
        # Symmetrised: if A lists B, B shows A.
        for a, rel in list(self.related.items()):
            for b in rel:
                if b in self.related and a not in self.related[b] and a != b:
                    self.related[b].append(a)
        self.children = {}
        for e in entries:
            if e.get("parent"):
                self.children.setdefault(e["parent"], []).append(e["concept"])
        for k in self.children:
            self.children[k].sort()

    def link(self, code, loc):
        if code in self.by_code:
            return f"[`{code}`](#{code})"
        print(f"warning: link to unknown concept `{code}`", file=sys.stderr)
        return f"`{code}`"

    def links(self, values, loc):
        return ltr(loc["sep"].join(self.link(v, loc) for v in values), loc)


def registry_link(name, loc):
    return f"[`{name}`](/guidelines/{loc['code']}/reference/registries/#{name})"


def render_source(cite, sources, loc):
    src = sources.get(cite["id"]) or {}
    title = src.get("title", cite["id"])
    url = cite.get("url") or src.get("url")
    text = f"[{title}]({url})" if url else title
    if cite.get("ref"):
        text += f" — `{cite['ref']}`"
    return text


def heading(e, loc):
    n = e.get("names", {})
    display = n.get("display", e["concept"])
    arabic = n.get("arabic", {}).get("singular") or n.get("arabic", {}).get("vocalized", "")
    if not arabic:
        return f"### {display}"
    return f"### {arabic} — {display}" if loc["ltr"] else f"### {display} — {arabic}"


def render_entry(e, loc, idx, sources):
    code = e["concept"]
    n = e.get("names", {})
    ar = n.get("arabic", {}) or {}
    R = loc["rows"]
    lines = [f'<a id="{code}"></a>', "", heading(e, loc), "",
             f"<!-- source: standards/terminology/concepts/{code}.yml -->", ""]

    rows = [("`code`", ltr(f"`{n.get('code', code)}`", loc))]
    if e.get("plural"):
        rows.append((R["plural"], ltr(f"`{e['plural']}`", loc)))
    rows.append((R["kind"], ltr(f"`{e['kind']}`", loc)))
    if e.get("parent"):
        rows.append((R["parent"], idx.links([e["parent"]], loc)))
    if idx.children.get(code):
        label = R["values"] if e["kind"] == "classification" else R["children"]
        rows.append((label, idx.links(idx.children[code], loc)))
    if e.get("part_of"):
        rows.append((R["part_of"], idx.links([e["part_of"]], loc)))
    for key in ("origin", "tier", "status"):
        if e.get(key):
            rows.append((R[key], ltr(f"`{e[key]}`", loc)))
    if ar.get("vocalized"):
        rows.append((R["vocalized"], ar["vocalized"]))
    if ar.get("plural"):
        rows.append((R["arabic_plural"], ar["plural"]))
    if n.get("transliteration"):
        rows.append((R["transliteration"], ltr(n["transliteration"], loc)))
    for key in ("dabt", "by_shape", "mushaf_introduction"):
        if n.get(key):
            rows.append((R[key], n[key]))
    if e.get("symbol"):
        rows.append((R["symbol"], e["symbol"]))
    if e.get("unicode"):
        cps = loc["sep"].join(
            f"`{u['cp']}`" + (f" {u['name']}" if u.get("name") else "") for u in e["unicode"])
        rows.append((R["unicode"], ltr(cps, loc)))
    if e.get("mark_family"):
        rows.append((R["mark_family"], ltr(f"`{e['mark_family']}`", loc)))
    if e.get("registry"):
        rows.append((R["registry"], ltr(registry_link(e["registry"], loc), loc)))
    if e.get("alternative_spellings"):
        rows.append((R["alternative"], codes(dedupe(e["alternative_spellings"]), loc)))
    if e.get("deprecated"):
        rows.append((R["deprecated"], codes(dedupe(e["deprecated"]), loc)))
    if e.get("english_glosses"):
        rows.append((R["gloss"], codes(dedupe(e["english_glosses"]), loc)))
    if n.get("display_evidence"):
        rows.append((R["display_evidence"], ltr(cell(n["display_evidence"]), loc)))

    lines.append(f"| {loc['field_cols'][0]} | {loc['field_cols'][1]} |")
    lines.append("| --- | --- |")
    for k, v in rows:
        lines.append(f"| {k} | {cell(v)} |")
    lines.append("")
    if e.get(loc["definition"]):
        lines.append(f"{loc['definition_label']} {e[loc['definition']].strip()}")
        lines.append("")
    if e.get(loc["purpose"]):
        lines.append(f"{loc['purpose_label']} {e[loc['purpose']].strip()}")
        lines.append("")
    for b in e.get(loc["boundaries"], []) or []:
        lines.append(f"- {b.strip()}")
    if e.get(loc["boundaries"]):
        lines.append("")
    if e.get(loc["note"]):
        lines.append(f"> {e[loc['note']].strip()}")
        lines.append("")
    if idx.related.get(code):
        lines.append(f"{loc['related_label']} {idx.links(idx.related[code], loc)}")
        lines.append("")
    if e.get("sources"):
        lines.append(loc["sources_label"])
        lines.append("")
        for cite in e["sources"]:
            lines.append(f"- {render_source(cite, sources, loc)}")
        lines.append("")
    return "\n".join(lines)


def render_lookup(entries, labels, loc):
    cols = loc["lookup_cols"]
    lines = [f"## {loc['lookup_h']}", "", loc["lookup_intro"], "",
             "| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]
    for e in sorted(entries, key=lambda x: x["concept"]):
        n = e.get("names", {})
        ar = n.get("arabic", {}) or {}
        arabic = ar.get("singular") or ar.get("vocalized", "")
        lines.append("| " + " | ".join([
            f"[`{e['concept']}`](#{e['concept']})",
            cell(n.get("display", "")),
            cell(arabic),
            ltr(f"`{e['kind']}`", loc),
            ltr(f"`{e['category']}`", loc),
            cell(first_sentence(e.get(loc["definition"], ""))),
        ]) + " |")
    lines.append("")
    return "\n".join(lines)


def render_by_category(by_cat, labels, loc):
    lines = [f"## {loc['bycat_h']}", ""]
    for key, label in labels:
        group = sorted(e["concept"] for e in by_cat.get(key, []))
        if group:
            links = loc["sep"].join(f"[`{c}`](#{c})" for c in group)
            lines.append(f"- **{label}** — `{key}`: {ltr(links, loc)}")
    lines.append("")
    return "\n".join(lines)


def render(entries, loc, idx, sources):
    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    labels = [(row[0], row[loc["label"]]) for row in CATEGORIES]

    parts = [loc["front"], render_lookup(entries, labels, loc),
             render_by_category(by_cat, labels, loc)]
    total = 0
    for key, label in labels:
        group = sorted(by_cat.get(key, []), key=lambda x: x["concept"])
        if not group:
            continue
        parts.append(f"## {label} — `{key}`\n")
        for e in group:
            parts.append(render_entry(e, loc, idx, sources))
            total += 1
    if total != len(entries):
        sys.exit(f"error: {len(entries) - total} entries were not rendered")
    out = os.path.join(ROOT, loc["out"])
    open(out, "w", encoding="utf-8").write("\n".join(parts))
    print(f"{total} entries rendered into {os.path.relpath(out, ROOT)}")


def main():
    entries = load()
    known = {row[0] for row in CATEGORIES}
    missing = sorted({e["category"] for e in entries} - known)
    if missing:
        sys.exit(f"error: categories with no label in CATEGORIES: {missing}")
    idx = Index(entries)
    sources = load_sources()
    for loc in (AR, EN):
        render(entries, loc, idx, sources)


if __name__ == "__main__":
    main()
