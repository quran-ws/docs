#!/usr/bin/env python3
"""Render the adab rules an agent skill carries, from the guideline sources.

The QuranTech skill (quran-ws/qurantech-skill) states rules about handling the
text. Those rules are owned here, so the skill's list is generated from the
rule files and each line names the rule it comes from. Writes to stdout, or to
the path given as the first argument.
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "content" / "pages"
SITE = "https://quran.ws/docs/guidelines"

# (page, rule id) in the order the skill lists them
RULES = [
    ("quranic-text", "never-edit-in-place"),
    ("quranic-text", "never-type-the-text"),
    ("quranic-text", "no-normalisation"),
    ("quranic-text", "no-generic-cleanup"),
    ("quranic-text", "edition-marks-are-not-text"),
    ("quranic-text", "font-coverage"),
    ("engineering", "no-fallback-fonts"),
    ("quranic-text", "numbering-systems-differ"),
    ("quranic-text", "basmalah-is-a-field"),
    ("quranic-text", "location-is-a-triple"),
    ("quranic-text", "never-trim-to-fit"),
    ("quranic-text", "fragments-read-as-fragments"),
    ("quranic-text", "no-partial-render"),
    ("quranic-text", "text-only-where-it-belongs"),
    ("quranic-text", "fail-loudly"),
    ("quranic-text", "no-silent-update"),
    ("engineering", "no-autoplay"),
]


def load(page):
    return yaml.safe_load((PAGES / f"{page}.yml").read_text(encoding="utf8"))


def numbered(doc):
    out = {}
    for i, section in enumerate(doc["sections"], 1):
        for j, rule in enumerate(section.get("rules", []), 1):
            out[rule["id"]] = (f"{i}.{j}", rule)
    return out


def main():
    docs = {p: numbered(load(p)) for p in {p for p, _ in RULES}}
    titles = {p: load(p)["title"] for p in docs}
    lines = [
        "## Text integrity and display",
        "",
        "These rules are the Quran.ws guidelines, stated once there and copied here by",
        "`tools/generate_adab.py` in quran-ws/docs. Each line names its rule; the page",
        "carries the example and the check that catches a violation.",
        "",
    ]
    for page, rid in RULES:
        number, rule = docs[page][rid]
        lines.append(f"- **{rule['rule']}** ({titles[page]} {number}, {SITE}/{page}/)")
    text = "\n".join(lines) + "\n"
    if len(sys.argv) > 1:
        pathlib.Path(sys.argv[1]).write_text(text, encoding="utf8")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
