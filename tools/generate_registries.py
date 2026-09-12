"""Render the registries page from the registry files.

A registry (section 13 of the standard) enumerates the members of a concept
that has a closed set of them: the 114 surahs, the ten qiraat and their
riwayat, the six ayah numbering systems and their counts, the places of
prostration. The members live in `standards/terminology/registries/*.tsv`;
this page shows them so that a reader of the site can see the list the
dictionary entry points at.

Every registry file follows one shape, and this script reads nothing else:

  - lines starting with `#` are commentary; the first one is the registry's
    title, and the last one is the header row, tab-separated;
  - every other line is a row, tab-separated, in the header's columns.

A registry that appears tomorrow renders with no change here, and a registry
whose header cannot be found stops the build rather than rendering wrong.

Each registry gets a stable anchor equal to its file name (`<a id="surahs">`),
which is what a dictionary entry's `registry` field links to.

    python3 tools/generate_registries.py
"""
import glob, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRIES = os.path.join(ROOT, "standards/terminology/registries")
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")

BANNER_AR = """> مولّد من `standards/terminology/registries/*.tsv` — عدّل السجل لا هذه الصفحة،
> ثم شغّل `python3 tools/build.py`."""
BANNER_EN = """> Generated from `standards/terminology/registries/*.tsv` — edit the registry,
> not this page, then run `python3 tools/build.py`."""

# The registry's Arabic title, where one is known. A new registry falls back to
# its English title until a line is added here.
TITLES_AR = {
    "surahs": "أسماء السور",
    "qiraat": "القراءات والرواة والروايات",
    "ayah_numbering": "أنظمة عد الآي",
    "ayah_counts": "أعداد آي السور في أنظمة العد",
    "sajdah": "مواضع السجدة",
    "tajwid_rules": "أحكام التجويد",
    "tariq": "الطرق",
}

AR = {
    "code": "ar",
    "out": "content/ar/reference/registries.md",
    "front": """---
title: السجلات
description: أفراد المجموعات المغلقة التي يشير إليها القاموس؛ السور والقراءات وأنظمة عد الآي ومواضع السجدة.
status: draft
sidebar:
  order: 4
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
""" + BANNER_AR + """

السجل يعدد أفراد مفهوم له مجموعة مغلقة من الأفراد؛ والمفهوم نفسه له مدخل في
[القاموس](/guidelines/ar/reference/dictionary/)، والسجل يحمل ما لا يحمله المدخل: القائمة.
""",
    "concept": "المفهوم", "file": "الملف", "rows": "الصفوف",
}

EN = {
    "code": "en",
    "out": "content/en/reference/registries.md",
    "front": """---
title: Registries
description: The members of the closed sets the dictionary points at; surahs, qiraat, ayah numbering systems, places of prostration.
status: draft
sidebar:
  order: 4
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
""" + BANNER_EN + """

A registry enumerates the members of a concept that has a closed set of them.
The concept itself has an entry in the
[dictionary](/guidelines/en/reference/dictionary/); the registry carries
what the entry does not: the list.
""",
    "concept": "Concept", "file": "File", "rows": "Rows",
}


def read_registry(path):
    """(title, header, rows) from one TSV; the title and header are the first
    and last commentary lines."""
    comments, rows = [], []
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("#"):
            comments.append(line[1:].strip())
        elif line.strip():
            rows.append(line.split("\t"))
    if not comments:
        sys.exit(f"error: {os.path.relpath(path, ROOT)} has no commentary; a title and a header row are required")
    headers = [c for c in comments if "\t" in c]
    if not headers:
        sys.exit(f"error: {os.path.relpath(path, ROOT)} has no tab-separated header row in its commentary")
    header = [h.strip() for h in headers[-1].split("\t")]
    # The first comment line is the title. An Arabic gloss in it belongs to the
    # Arabic page, which has its own titles, so the English heading keeps only
    # the Latin segments.
    title = " — ".join(seg for seg in comments[0].rstrip(".").split(" — ")
                       if not re.search(r"[\u0600-\u06FF]", seg))
    for row in rows:
        if len(row) > len(header):
            sys.exit(f"error: {os.path.relpath(path, ROOT)} has a row wider than its header: {row[:2]}")
        row.extend([""] * (len(header) - len(row)))
    return title, header, rows


def concepts_by_registry():
    out = {}
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        e = yaml.safe_load(open(path, encoding="utf-8"))
        if e.get("registry"):
            out.setdefault(e["registry"], []).append(e["concept"])
    return out


def cell(text):
    return re.sub(r"\s+", " ", str(text)).replace("|", "\\|").strip()


def render_registry(name, title, header, rows, concepts, loc):
    label = TITLES_AR.get(name, title) if loc["code"] == "ar" else title
    lines = [f'<a id="{name}"></a>', "", f"## {label} — `{name}`", "",
             f"<!-- source: standards/terminology/registries/{name}.tsv -->", ""]
    meta = []
    if concepts.get(name):
        links = "، ".join(f"[`{c}`](/guidelines/{loc['code']}/reference/dictionary/#{c})"
                          for c in concepts[name]) if loc["code"] == "ar" else \
                ", ".join(f"[`{c}`](/guidelines/{loc['code']}/reference/dictionary/#{c})"
                          for c in concepts[name])
        meta.append(f"{loc['concept']}: {links}")
    meta.append(f"{loc['file']}: `standards/terminology/registries/{name}.tsv`")
    meta.append(f"{loc['rows']}: {len(rows)}")
    lines.append(" · ".join(meta))
    lines.append("")
    lines.append("| " + " | ".join(f"`{h}`" for h in header) + " |")
    lines.append("|" + " --- |" * len(header))
    for row in rows:
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")
    lines.append("")
    return "\n".join(lines)


def main():
    paths = sorted(glob.glob(os.path.join(REGISTRIES, "*.tsv")))
    if not paths:
        sys.exit("error: no registries found")
    concepts = concepts_by_registry()
    registries = [(os.path.splitext(os.path.basename(p))[0],) + read_registry(p) for p in paths]
    for loc in (AR, EN):
        parts = [loc["front"]]
        for name, title, header, rows in registries:
            parts.append(render_registry(name, title, header, rows, concepts, loc))
        out = os.path.join(ROOT, loc["out"])
        open(out, "w", encoding="utf-8").write("\n".join(parts))
        print(f"{len(registries)} registries rendered into {os.path.relpath(out, ROOT)}")
    orphans = sorted(set(concepts) - {r[0] for r in registries})
    if orphans:
        sys.exit(f"error: entries name registries that do not exist: {orphans}")


if __name__ == "__main__":
    main()
