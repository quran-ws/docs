#!/usr/bin/env python3
"""Audit a codebase against the Quranic Software Terminology Standard.

Reads the identifiers in a tree and reports the names that the standard would
have written differently: a deprecated name, a spelling that is not the
canonical one, an English gloss standing in for a Quranic term, an Arabic
plural used as a collection name.

    python3 audit_terminology.py PATH [PATH ...]
    python3 audit_terminology.py src --json
    python3 audit_terminology.py src --strict     # exit 1 if there are errors

Every finding names the rule, the section of the standard behind it, and the
canonical name to use instead. Nothing is rewritten: the script reports, and
the decision to rename stays with whoever knows the code.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data", "terminology.json")

CODE_SUFFIXES = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".go", ".rs", ".java",
    ".kt", ".swift", ".rb", ".php", ".cs", ".c", ".h", ".cpp", ".hpp", ".dart",
    ".sql", ".graphql", ".gql", ".proto", ".json", ".yml", ".yaml", ".toml",
    ".prisma", ".vue", ".svelte", ".scala", ".ex", ".exs", ".sh",
}
PROSE_SUFFIXES = {".md", ".mdx", ".txt", ".rst", ".adoc"}
SKIP_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "out", "target",
    "__pycache__", ".venv", "venv", ".next", ".nuxt", ".cache", "coverage",
    ".mypy_cache", ".pytest_cache", "migrations_backup",
}
MAX_BYTES = 2_000_000

# An identifier as it is written in any of the languages above, before it is
# split: dots and hyphens included, so `ayah.aya_key` and `verse-list` are one
# run of text and their parts are checked together.
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_.\-]*")
CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

RULES = {
    "deprecated": ("error", "A deprecated name: it names a different concept."),
    "spelling": ("error", "Not the canonical code spelling (sections 4-8)."),
    "arabic_plural": ("error", "An Arabic plural used as a name (section 11)."),
    "display_in_code": ("warning", "The display name, used as an identifier (section 9)."),
    "gloss": ("warning", "An English gloss standing in for a Quranic term (sections 3, 19)."),
}


def load(path=DATA):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def parts_of(identifier):
    """Split an identifier into lowercase words, however it is cased."""
    out = []
    for chunk in re.split(r"[_.\-]+", identifier):
        if chunk:
            out += [p.lower() for p in CAMEL.split(chunk) if p]
    return out


def ngrams(parts, longest=4):
    """Every run of parts, longest first, so `waqf_lazim` beats `waqf`."""
    for size in range(min(longest, len(parts)), 0, -1):
        for start in range(0, len(parts) - size + 1):
            yield start, size, "_".join(parts[start:start + size])


def lookup(parts, index):
    """The findings in one identifier: the longest match wins its span."""
    found, taken = [], set()
    for start, size, gram in ngrams(parts):
        span = set(range(start, start + size))
        if span & taken:
            continue
        hit = index.get(gram)
        if hit:
            taken |= span
            found.append((gram, hit))
    return found


def build_index(data):
    """One map from a written form to (rule, concept, the form without its `s`)."""
    index = {}

    def put(form, rule, concept):
        form = form.lower().replace("-", "_").replace(" ", "_")
        if not form or form == concept:
            return
        index.setdefault(form, (rule, concept, form))

    # Order decides which rule claims a form, so the most specific goes first:
    # `tajweed` is the display name before it is merely a spelling.
    for concept, e in data["concepts"].items():
        for name in e.get("deprecated") or []:
            put(name, "deprecated", concept)
    for concept, e in data["concepts"].items():
        if e.get("display"):
            put(e["display"], "display_in_code", concept)
        for plural in e.get("arabic_plurals") or []:
            put(plural, "arabic_plural", concept)
        for gloss in e.get("english_glosses") or []:
            put(gloss, "gloss", concept)
    for form, concept in data["aliases"].items():
        put(form, "spelling", concept)
    # The canonical name itself, so that a tree writing it both ways is seen.
    for concept, e in data["concepts"].items():
        index[e["code"]] = ("canonical", concept, e["code"])
    # A collection is named by adding `s` (section 11), so `suras` is `sura`
    # made plural: the same finding, counted under the singular. Only `s` is
    # added — `es` would make `files` a plural of `fil`.
    for form, hit in list(index.items()):
        index.setdefault(form + "s", hit)
    return index


def files(paths):
    for path in paths:
        if os.path.isfile(path):
            yield path
            continue
        for root, dirs, names in os.walk(path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for name in sorted(names):
                suffix = os.path.splitext(name)[1].lower()
                if suffix in CODE_SUFFIXES or suffix in PROSE_SUFFIXES:
                    yield os.path.join(root, name)


def scan(paths, index, data):
    findings, used = [], {}
    for path in files(paths):
        try:
            if os.path.getsize(path) > MAX_BYTES:
                continue
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        prose = os.path.splitext(path)[1].lower() in PROSE_SUFFIXES
        for number, line in enumerate(text.splitlines(), 1):
            for match in IDENTIFIER.finditer(line):
                identifier = match.group(0)
                for form, (rule, concept, base) in lookup(parts_of(identifier), index):
                    used.setdefault(concept, {}).setdefault(base, 0)
                    used[concept][base] += 1
                    if rule == "canonical":
                        continue
                    # Prose is meant to carry the display name and may quote a
                    # gloss, so only a wrong name is a finding there.
                    if prose and rule in ("display_in_code", "gloss"):
                        continue
                    findings.append({
                        "rule": rule,
                        "severity": RULES[rule][0],
                        "file": path,
                        "line": number,
                        "identifier": identifier,
                        "found": form,
                        "concept": concept,
                        "canonical": data["concepts"][concept]["code"],
                        "display": data["concepts"][concept].get("display"),
                    })
    return findings, used


def canonical_uses(data, used):
    """Concepts written more than one way in this tree (section 26)."""
    out = []
    for concept, forms in sorted(used.items()):
        code = data["concepts"][concept]["code"]
        spellings = sorted(forms)
        if len(spellings) > 1:
            out.append({"concept": concept, "canonical": code,
                        "spellings": {f: forms[f] for f in spellings}})
    return out


def report(findings, mixed, data, limit):
    if not findings:
        print("ok — every name in this tree resolves to its canonical form")
    for rule in ("deprecated", "spelling", "arabic_plural", "display_in_code", "gloss"):
        group = [f for f in findings if f["rule"] == rule]
        if not group:
            continue
        severity, why = RULES[rule]
        print(f"\n{len(group)} {severity}: {rule} — {why}")
        for f in group[:limit]:
            entry = data["concepts"][f["concept"]]
            print(f"  {f['file']}:{f['line']}: {f['identifier']!r} has {f['found']!r} "
                  f"→ `{f['canonical']}` ({entry.get('display')})")
        if len(group) > limit:
            print(f"  … and {len(group) - limit} more")
    if mixed:
        print(f"\n{len(mixed)} concepts written more than one way (section 26):")
        for m in mixed:
            forms = ", ".join(f"{k} ×{v}" for k, v in m["spellings"].items())
            print(f"  {m['canonical']}: {forms}")
    errors = [f for f in findings if f["severity"] == "error"]
    print(f"\n{len(errors)} errors, {len(findings) - len(errors)} warnings, "
          f"{len(findings)} findings in total")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="files or directories to audit")
    ap.add_argument("--json", action="store_true", help="machine-readable findings")
    ap.add_argument("--strict", action="store_true", help="exit 1 when there are errors")
    ap.add_argument("--limit", type=int, default=20, help="findings printed per rule")
    ap.add_argument("--data", default=DATA, help="path to terminology.json")
    args = ap.parse_args()

    data = load(args.data)
    index = build_index(data)
    findings, used = scan(args.paths, index, data)
    mixed = canonical_uses(data, used)

    if args.json:
        json.dump({"findings": findings, "mixed": mixed}, sys.stdout,
                  ensure_ascii=False, indent=1)
        print()
        errors = [f for f in findings if f["severity"] == "error"]
    else:
        errors = report(findings, mixed, data, args.limit)
    return 1 if (args.strict and errors) else 0


if __name__ == "__main__":
    sys.exit(main())
