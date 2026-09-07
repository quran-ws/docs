"""Validate every concept file against the entry schema.

    python3 tools/validate.py
"""
import glob, json, os, sys
import yaml
from jsonschema import Draft202012Validator

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "standards/terminology/schema.json")
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")


def main():
    validator = Draft202012Validator(json.load(open(SCHEMA, encoding="utf-8")))
    files = sorted(glob.glob(os.path.join(CONCEPTS, "*.yml")))
    failures = 0
    for path in files:
        entry = yaml.safe_load(open(path, encoding="utf-8"))
        errors = sorted(validator.iter_errors(entry), key=lambda e: [str(p) for p in e.path])
        if errors:
            failures += 1
            print(f"\n{os.path.basename(path)}")
            for e in errors[:5]:
                where = ".".join(str(p) for p in e.path) or "(root)"
                print(f"  {where}: {e.message[:110]}")
        # the file name must be the concept, or nothing can find it
        stem = os.path.splitext(os.path.basename(path))[0]
        if entry.get("concept") != stem:
            failures += 1
            print(f"\n{os.path.basename(path)}: concept is {entry.get('concept')!r}, file says {stem!r}")
    print(f"\n{len(files) - failures} of {len(files)} entries valid")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
