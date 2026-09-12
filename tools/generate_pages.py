#!/usr/bin/env python3
"""Render the guideline pages from their rule files.

A guideline page is written once, as data, in `content/pages/<page>.yml`: a
title, an intro, and sections of rules. Every rule is one sentence, an optional
example and note, and the check that catches a violation. The English page is
rendered from it always, and the Arabic page once every field of the page has
its Arabic beside it. The two languages never drift into two files that have
to be kept in step by hand.

    python3 tools/generate_pages.py            # render every page, both languages
    python3 tools/generate_pages.py --check    # report what is untranslated or stale
    python3 tools/generate_pages.py --stamp    # record that the Arabic matches the English

The stamp is a hash of the English text each Arabic field was translated from,
kept in `content/pages/translations.json`. `tests/test_pages.py` fails when an
English rule changed after its Arabic was stamped, so a stale translation is
caught in CI, not noticed by a reader. After translating or revising the
Arabic, run `--stamp` to record the new baseline.

Fields of a page file:

    title, description, status, order, intro           # the page
    sections: [ {title, lead, rules: [...]} ]           # its sections
    rules:    [ {id, rule, example, note, checked_by} ] # its rules

Each text field has an `_ar` twin. `example_ar` is optional and falls back to
`example`, since most examples are code and language-neutral. `id` is a stable
kebab-case name a page or a test can cite; the rendered number (2.3) is not
stable and is not cited.
"""
import argparse
import hashlib
import json
import os
import re
import sys

import yaml

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
PAGES = os.path.join(ROOT, "content", "pages")
STAMPS = os.path.join(PAGES, "translations.json")
OUT = {"en": os.path.join(ROOT, "content", "en"), "ar": os.path.join(ROOT, "content", "ar")}

PAGE_FIELDS = ("title", "description", "intro")
SECTION_FIELDS = ("title", "lead")
RULE_FIELDS = ("rule", "example", "note", "checked_by")
CHECKED_BY = {"en": "Checked by", "ar": "يفحصه"}
ID = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")


def load_pages():
    pages = {}
    for name in sorted(os.listdir(PAGES)):
        if name.endswith(".yml"):
            with open(os.path.join(PAGES, name), encoding="utf-8") as f:
                pages[name[:-4]] = yaml.safe_load(f)
    return pages


def load_stamps():
    if not os.path.exists(STAMPS):
        return {}
    with open(STAMPS, encoding="utf-8") as f:
        return json.load(f)


def field(obj, key, lang):
    """The text of `key` in `lang`; an Arabic example falls back to the English one."""
    if lang == "en":
        return obj.get(key)
    value = obj.get(f"{key}_ar")
    if value is None and key == "example":
        return obj.get("example")
    return value


def digest(text):
    return hashlib.sha1(" ".join(str(text).split()).encode("utf-8")).hexdigest()[:12]


def english_units(page):
    """Every translatable unit of a page, keyed, with the hash of its English."""
    units = {"_page": digest("\n".join(str(page.get(k) or "") for k in PAGE_FIELDS))}
    for i, section in enumerate(page.get("sections") or [], 1):
        units[f"_section-{i}"] = digest("\n".join(str(section.get(k) or "") for k in SECTION_FIELDS))
        for rule in section.get("rules") or []:
            units[rule["id"]] = digest("\n".join(str(rule.get(k) or "") for k in RULE_FIELDS))
    return units


def arabic_present(page):
    """Which units carry Arabic, and which required fields are missing it."""
    present, missing = set(), []
    if all(page.get(f"{k}_ar") for k in PAGE_FIELDS):
        present.add("_page")
    else:
        missing.append("_page")
    for i, section in enumerate(page.get("sections") or [], 1):
        key = f"_section-{i}"
        if section.get("title_ar") and (not section.get("lead") or section.get("lead_ar")):
            present.add(key)
        else:
            missing.append(key)
        for rule in section.get("rules") or []:
            required = ["rule", "checked_by"] + [k for k in ("note",) if rule.get(k)]
            if all(rule.get(f"{k}_ar") for k in required):
                present.add(rule["id"])
            else:
                missing.append(rule["id"])
    return present, missing


def validate(name, page):
    problems = []
    for k in ("title", "description", "status", "order", "intro", "sections"):
        if page.get(k) in (None, "", []):
            problems.append(f"{name}: `{k}` is missing")
    if page.get("status") not in ("draft", "proposed", "adopted"):
        problems.append(f"{name}: status {page.get('status')!r} is not draft, proposed or adopted")
    seen = set()
    for i, section in enumerate(page.get("sections") or [], 1):
        if not section.get("title"):
            problems.append(f"{name}: section {i} has no title")
        if not section.get("rules"):
            problems.append(f"{name}: section {i} has no rules")
        for rule in section.get("rules") or []:
            rid = rule.get("id")
            if not rid or not ID.match(rid):
                problems.append(f"{name}: section {i}: rule id {rid!r} is not kebab-case")
            elif rid in seen:
                problems.append(f"{name}: rule id {rid!r} is used twice")
            seen.add(rid)
            for k in ("rule", "checked_by"):
                if not rule.get(k):
                    problems.append(f"{name}: rule {rid!r} has no `{k}`")
            if rule.get("rule") and not str(rule["rule"]).rstrip().endswith((".", "؟", "!")):
                problems.append(f"{name}: rule {rid!r} is not a sentence: {rule['rule']!r}")
            for k in rule:
                if k.removesuffix("_ar") not in RULE_FIELDS + ("id",):
                    problems.append(f"{name}: rule {rid!r} has an unknown field `{k}`")
    return problems


def render(name, page, lang):
    p = lambda key: field(page, key, lang)
    lines = ["---",
             f"title: {yaml_scalar(p('title'))}",
             f"description: {yaml_scalar(p('description'))}",
             f"status: {page['status']}",
             f"generated: content/pages/{name}.yml",   # the source; the page carries no other trace of it
             "sidebar:",
             f"  order: {page['order']}",
             "---",
             "",
             p("intro").rstrip(),
             ""]
    for i, section in enumerate(page["sections"], 1):
        s = lambda key: field(section, key, lang)
        lines += [f"## {i}. {s('title')}", ""]
        if s("lead"):
            lines += [str(s("lead")).rstrip(), ""]
        for j, rule in enumerate(section["rules"], 1):
            r = lambda key: field(rule, key, lang)
            lines += [f"**{i}.{j}** {str(r('rule')).strip()}", ""]
            if r("example"):
                lines += [str(r("example")).rstrip(), ""]
            if r("note"):
                lines += [str(r("note")).strip(), ""]
            lines += [f"*{CHECKED_BY[lang]}:* {str(r('checked_by')).strip()}", ""]
    return "\n".join(lines).rstrip() + "\n"


def yaml_scalar(text):
    text = " ".join(str(text).split())
    return json.dumps(text, ensure_ascii=False) if re.search(r"[:#\[\]{}&*!|>'\"%@`]", text) else text


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    current = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if current != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False


def report(pages, stamps):
    """Untranslated and stale units, per page; empty when Arabic is complete and current."""
    findings = {}
    for name, page in pages.items():
        units = english_units(page)
        present, missing = arabic_present(page)
        stale = [k for k in present if stamps.get(name, {}).get(k) != units[k]]
        if missing or stale:
            findings[name] = {"untranslated": missing, "stale": stale}
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="only report untranslated and stale Arabic")
    ap.add_argument("--stamp", nargs="*", metavar="PAGE",
                    help="record the current English as the baseline of the Arabic present")
    args = ap.parse_args()

    pages = load_pages()
    problems = [p for name, page in pages.items() for p in validate(name, page)]
    if problems:
        print(f"{len(problems)} problems in content/pages/:")
        print("\n".join("  " + p for p in problems))
        return 1
    stamps = load_stamps()

    if args.stamp is not None:
        for name in args.stamp or pages:
            units = english_units(pages[name])
            present, _ = arabic_present(pages[name])
            stamps[name] = {k: units[k] for k in sorted(present)}
        with open(STAMPS, "w", encoding="utf-8") as f:
            json.dump(stamps, f, indent=2, ensure_ascii=False, sort_keys=True)
            f.write("\n")
        print(f"stamped {', '.join(args.stamp or pages)}")

    findings = report(pages, stamps)
    if args.check:
        for name, f in findings.items():
            for kind in ("untranslated", "stale"):
                if f[kind]:
                    print(f"{name}: {len(f[kind])} {kind}: {', '.join(f[kind])}")
        print("ok — every page is translated and current" if not findings else "")
        return 0

    for name, page in pages.items():
        changed = write(os.path.join(OUT["en"], f"{name}.md"), render(name, page, "en"))
        _, missing = arabic_present(page)
        ar_path = os.path.join(OUT["ar"], f"{name}.md")
        if missing:
            print(f"{name}: English rendered{' (changed)' if changed else ''}; "
                  f"Arabic skipped, {len(missing)} units untranslated")
        else:
            changed_ar = write(ar_path, render(name, page, "ar"))
            stale = findings.get(name, {}).get("stale", [])
            print(f"{name}: rendered in both languages"
                  + (f", {len(stale)} Arabic units stale — run --stamp after revising them" if stale else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
