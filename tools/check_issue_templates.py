"""Check that the term proposal form offers the same values as the schema.

`.github/ISSUE_TEMPLATE/term.yml` has a dropdown for each of `kind`,
`category`, `origin` and `tier`. The values live in
`standards/terminology/schema.json`; the form is a copy, and copies go stale.
This compares the two, and `--fix` rewrites the form's options from the schema
in place, keeping everything else in the file as it is.

    python3 tools/check_issue_templates.py
    python3 tools/check_issue_templates.py --fix
"""
import argparse, json, os, re, sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "standards/terminology/schema.json")
FORM = os.path.join(ROOT, ".github/ISSUE_TEMPLATE/term.yml")
FIELDS = ["kind", "category", "origin", "tier"]


def schema_enums():
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    return {field: schema["properties"][field]["enum"] for field in FIELDS}


def form_options(text):
    form = yaml.safe_load(text)
    found = {}
    for item in form.get("body", []):
        if item.get("type") == "dropdown" and item.get("id") in FIELDS:
            found[item["id"]] = list(item["attributes"].get("options", []))
    return found


def rewrite(text, field, values):
    """Replace the options list of one dropdown, by text, so nothing else moves."""
    # The block: `id: <field>` … `options:` then the indented `- value` lines.
    pattern = re.compile(
        r"(    id: " + re.escape(field) + r"\n(?:(?!  - type:).*\n)*?      options:\n)"
        r"((?:        - .*\n)+)")
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"{FORM}: no options block found for {field!r}")
    new_block = "".join(f"        - {value}\n" for value in values)
    return text[:match.start(2)] + new_block + text[match.end(2):]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true",
                    help="rewrite the form's options from the schema")
    args = ap.parse_args()

    enums = schema_enums()
    text = open(FORM, encoding="utf-8").read()
    options = form_options(text)
    problems = []
    for field in FIELDS:
        if field not in options:
            problems.append(f"  {field}: the form has no dropdown with this id")
            continue
        if options[field] != enums[field]:
            missing = [v for v in enums[field] if v not in options[field]]
            extra = [v for v in options[field] if v not in enums[field]]
            detail = []
            if missing:
                detail.append("missing " + ", ".join(missing))
            if extra:
                detail.append("not in the schema: " + ", ".join(extra))
            if not detail:
                detail.append("same values, different order")
            problems.append(f"  {field}: {'; '.join(detail)}")

    if problems and args.fix:
        for field in FIELDS:
            if field in options:
                text = rewrite(text, field, enums[field])
        open(FORM, "w", encoding="utf-8").write(text)
        print(f"rewrote the options of {', '.join(f for f in FIELDS if f in options)} "
              f"in {os.path.relpath(FORM, ROOT)}")
        problems = [p for p in problems if "no dropdown" in p]

    if problems:
        print(f"{len(problems)} problems in {os.path.relpath(FORM, ROOT)} "
              f"(run with --fix to rewrite from the schema):")
        print("\n".join(problems))
        return 1
    print("ok — the term form offers the schema's kinds, categories, origins and tiers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
