"""Render the Arabic naming standard; --check validates without writing."""
import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content/standards/terminology.ar.yml"
OUTPUT = ROOT / "content/ar/reference/standard.md"
SOURCE_REL = SOURCE.relative_to(ROOT).as_posix()
RULE_FIELDS = {"id", "category", "name", "description", "examples"}
RULE_ID = re.compile(r"[0-9]{3}")
RULE_LINK = re.compile(r"#rule-([0-9]+)")


def load():
    return yaml.safe_load(SOURCE.read_text(encoding="utf-8"))


def validate(page):
    problems = []
    if not isinstance(page, dict):
        return ["standard: expected a mapping"]
    for field in ("title", "description", "intro"):
        if not isinstance(page.get(field), str) or not page[field].strip():
            problems.append(f"standard: `{field}` must be nonempty text")
    if page.get("status") not in ("draft", "proposed", "adopted"):
        problems.append("standard: invalid status")
    if type(page.get("order")) is not int or page["order"] < 1:
        problems.append("standard: order must be a positive integer")
    rules = page.get("rules")
    if not isinstance(rules, list) or not rules:
        return problems + ["standard: rules must be a nonempty list"]
    seen = set()
    for index, rule in enumerate(rules, 1):
        if not isinstance(rule, dict):
            problems.append(f"rule at position {index}: expected a mapping")
            continue
        rid = rule.get("id")
        where = f"rule {rid!r} (position {index})"
        if set(rule) != RULE_FIELDS:
            problems.append(f"{where}: expected fields {', '.join(sorted(RULE_FIELDS))}")
        if not isinstance(rid, str) or not RULE_ID.fullmatch(rid):
            problems.append(f"{where}: id must be a quoted three-digit string")
        elif rid in seen:
            problems.append(f"{where}: duplicate id")
        else:
            seen.add(rid)
        for field in ("category", "name", "description"):
            if not isinstance(rule.get(field), str) or not rule[field].strip():
                problems.append(f"{where}: `{field}` must be nonempty text")
        examples = rule.get("examples")
        if not isinstance(examples, list) or not examples or any(
                not isinstance(item, str) or not item.strip() for item in examples):
            problems.append(f"{where}: examples must be a nonempty list of nonempty text")
    for rid in RULE_LINK.findall(yaml.safe_dump(page, allow_unicode=True)):
        if rid not in seen:
            problems.append(f"standard: link to unknown rule {rid}")
    return problems


def render(page):
    front = {
        "title": page["title"], "description": page["description"],
        "status": page["status"], "generated": SOURCE_REL,
        "sidebar": {"order": page["order"]},
    }
    lines = ["---", yaml.safe_dump(front, allow_unicode=True, sort_keys=False).rstrip(),
             "---", "", page["intro"].strip(), ""]
    categories = {}
    for rule in page["rules"]:
        categories.setdefault(rule["category"], []).append(rule)
    for category, rules in categories.items():
        lines += [f"## {category}", ""]
        for rule in rules:
            lines += [f'<a id="rule-{rule["id"]}"></a>', "",
                      f'### {rule["id"]}. {rule["name"]}', "",
                      rule["description"].strip(), "", "**أمثلة**", ""]
            for example in rule["examples"]:
                # Each example is a Markdown block: table, code fence or prose.
                # A list prefix would nest the block and break table rendering.
                lines += [example.strip(), ""]
    return "\n".join(lines).rstrip() + "\n"


def check():
    page = load()
    problems = validate(page)
    if not problems and (not OUTPUT.exists() or
                         OUTPUT.read_text(encoding="utf-8") != render(page)):
        problems.append("Arabic standard is stale; run tools/generate_standard.py")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    args = parser.parse_args()
    try:
        page = load()
        problems = check() if args.check else validate(page)
    except (OSError, yaml.YAMLError) as exc:
        print(f"standard: {exc}")
        return 1
    if problems:
        print("\n".join(problems))
        return 1
    if not args.check:
        rendered = render(page)
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"ok — Arabic standard: {len(page['rules'])} rules, "
          f"{len({rule['category'] for rule in page['rules']})} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
