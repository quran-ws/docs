"""Check the files under examples/ against the standard.

The examples are what a project copies, so an alias in them is a defect, not a
spelling: every domain name must be the canonical `code` (or its plural), every
classification value a registry member, and the text record clean. The tests
under examples/tests/ must also pass, and every `examples/…` path a page
mentions must exist.

    python3 tools/check_example_files.py

Five checks:
  1. names   — identifiers in .sql, .prisma, .yml and JSON keys resolve to a
               canonical code or plural; generic words are listed in ALLOW
  2. values  — values of classification fields are registry members or
               classification values, written as their code
  3. text    — data/ayah.json: hash matches, no BOM, no edition marks, no digits,
               no Latin, no HTML, and NFC would change it (it is not normalised)
  4. tests   — examples/tests/*.py run (and *.js, when node is installed)
  5. paths   — every `examples/…` path in content/, README.md, CONTRIBUTING.md,
               STRUCTURE.md and examples/README.md exists
"""
import glob, hashlib, json, os, re, subprocess, sys, unicodedata

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES = os.path.join(ROOT, "examples")
TERMS = os.path.join(ROOT, "standards/terminology")

# Words that name no Quranic concept and are allowed as they are. Everything
# else that looks like an identifier must resolve to a canonical name.
ALLOW = {
    # generic data words
    "id", "ids", "code", "name", "text", "hash", "version", "publisher", "retrieved",
    "present", "count", "counts", "number", "position", "order", "offset", "before",
    "after", "kind", "summary", "date", "url", "note", "license", "encoding",
    "source", "dataset", "release", "notice", "required", "found", "by", "confirmed",
    "reported", "fixed", "in", "to", "covers", "error", "no", "such", "key", "deprecated",
    "tokenization", "whitespace", "sha256", "utf", "codepoint", "erratum", "errata",
    "transmission", "display", "get", "path", "query", "example", "default", "true",
    "false", "null", "view", "window", "people", "person", "translated", "server", "client",
    # SQL
    "create", "table", "not", "auto", "increment", "primary", "unique", "integer",
    "varchar", "char", "boolean", "text", "date", "constraint", "foreign", "references",
    "character", "set", "collate", "utf8mb4", "bin", "select", "insert", "into", "values",
    "from", "join", "on", "where", "update", "alter", "add", "column", "modify", "drop",
    "comment", "as", "and", "or", "fk", "uq", "pk", "unit", "start", "end", "confirmed", "on", "fixed", "derived", "released", "m", "w", "q", "r", "c", "use", "removed",
    # Prisma
    "datasource", "db", "provider", "mysql", "env", "generator", "prisma", "js", "model",
    "int", "string", "datetime", "map", "relation", "fields", "autoincrement",
    # OpenAPI
    "openapi", "info", "title", "description", "paths", "operationid", "parameters",
    "schema", "type", "minimum", "maximum", "enum", "responses", "content", "application",
    "json", "ref", "components", "schemas", "object", "properties", "items", "format",
    "nullable", "additionalproperties", "boolean", "array", "string", "integer", "s",
    "operationid", "operation", "search", "counted", "location", "time", "covers",
    "database",
}
# Identifier suffixes that attach to a concept name: ayah_id, surah_number, text_hash.
SUFFIXES = ("_id", "_ids", "_number", "_position", "_count", "_order", "_hash", "_text",
            "_present", "_source_hash", "_version", "_key", "_classification")
# Fields whose values are members of a closed set, and where the set is defined.
CLASSIFIED = {
    "ayah_numbering_system": ("registry", "ayah_numbering_system"),
    "riwayah": ("registry", "riwayah"),
    "qiraah": ("registry", "qiraah"),
    "rawi": ("registry", "rawi"),
    "surah": ("registry", "surah"),
    "revelation_classification": ("concept", "revelation_classification"),
    "rasm": ("concept", "rasm"),
    "kind": ("errata_kind", None),
}
ERRATA_KINDS = {"source_error", "transmission_error", "display_error"}
EDITION_MARKS = {"۝", "۞", "۩"}


def load_names():
    aliases = json.load(open(os.path.join(TERMS, "aliases.json"), encoding="utf-8"))
    registry = json.load(open(os.path.join(TERMS, "registry_aliases.json"), encoding="utf-8"))
    codes, plurals, children = set(), {}, {}
    for path in glob.glob(os.path.join(TERMS, "concepts/*.yml")):
        entry = yaml.safe_load(open(path, encoding="utf-8"))
        code = entry["names"]["code"]
        codes.add(code)
        if entry.get("plural"):
            plurals[entry["plural"]] = code
        if entry.get("parent"):
            children.setdefault(entry["parent"], set()).add(code)
    return aliases, registry, codes, plurals, children


def camel_to_snake(word):
    if word.isupper() or word.islower():
        return word.lower()
    return re.sub(r"(?<!^)(?=[A-Z])", "_", word).lower()


def check_name(name, names, where, problems):
    aliases, registry, codes, plurals, children = names
    name = camel_to_snake(name)
    if name in ALLOW or name.isdigit():
        return
    base = name
    for suffix in SUFFIXES:
        if name.endswith(suffix) and name[:-len(suffix)]:
            base = name[:-len(suffix)]
            break
    for candidate in (name, base):
        if candidate in codes or candidate in plurals:
            return
        if candidate in aliases:
            problems.append(f"  {where}: {name!r} is an alias of {aliases[candidate]!r}; "
                            f"examples use the canonical name")
            return
        for kind, members in registry.items():
            if candidate in members:
                if members[candidate] != candidate:
                    problems.append(f"  {where}: {name!r} is an alias of the {kind} member "
                                    f"{members[candidate]!r}")
                return
    # Compound names: the parts must segment into allowed words and canonical
    # names, where a canonical name may itself span several parts
    # (fk_ayahs_mushaf_edition = fk + ayahs + mushaf_edition).
    if segments(name.split("_"), codes, plurals):
        return
    problems.append(f"  {where}: {name!r} resolves to no concept, member or allowed word")


def segments(parts, codes, plurals):
    if not parts:
        return True
    for n in range(len(parts), 0, -1):
        piece = "_".join(parts[:n])
        if piece in ALLOW or piece in codes or piece in plurals:
            if segments(parts[n:], codes, plurals):
                return True
    return False


IDENT = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\b")


def strip_comments(text, ext):
    if ext in (".sql",):
        text = re.sub(r"--.*", "", text)
    if ext in (".prisma",):
        text = re.sub(r"//.*", "", text)
    text = re.sub(r"'[^']*'", "", text)      # string literals
    return text


PROSE_KEYS = {"description", "summary", "title", "example"}


def yaml_names(node, found, path_key=None):
    """Keys, path segments, parameter names, enum and default values; not prose."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in PROSE_KEYS:
                continue
            if isinstance(k, str):
                if k.startswith("/"):
                    for seg in k.strip("/").split("/"):
                        found.add(seg.strip("{}"))
                elif k.startswith("$"):
                    pass
                else:
                    found.add(k)
            if k in ("name", "default", "operationId") and isinstance(v, str):
                found.add(v)
            elif k == "enum" and isinstance(v, list):
                found.update(str(x) for x in v)
            else:
                yaml_names(v, found)
    elif isinstance(node, list):
        for v in node:
            yaml_names(v, found)
    return found


def check_names(names, problems):
    for path in sorted(glob.glob(os.path.join(EXAMPLES, "**/*.*"), recursive=True)):
        rel = os.path.relpath(path, ROOT)
        ext = os.path.splitext(path)[1]
        if ext in (".sql", ".prisma"):
            text = strip_comments(open(path, encoding="utf-8").read(), ext)
            for name in sorted(set(IDENT.findall(text))):
                check_name(name, names, rel, problems)
        elif ext in (".yml", ".yaml"):
            doc = yaml.safe_load(open(path, encoding="utf-8"))
            for name in sorted(yaml_names(doc, set())):
                if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
                    check_name(name, names, rel, problems)
        elif ext == ".json":
            data = json.load(open(path, encoding="utf-8"))
            for key in sorted(json_keys(data)):
                check_name(key, names, rel, problems)


def json_keys(node, found=None):
    found = set() if found is None else found
    if isinstance(node, dict):
        for k, v in node.items():
            found.add(k)
            json_keys(v, found)
    elif isinstance(node, list):
        for v in node:
            json_keys(v, found)
    return found


def json_pairs(node, out=None):
    out = [] if out is None else out
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str):
                out.append((k, v))
            json_pairs(v, out)
    elif isinstance(node, list):
        for v in node:
            json_pairs(v, out)
    return out


def check_values(names, problems):
    aliases, registry, codes, plurals, children = names
    for path in sorted(glob.glob(os.path.join(EXAMPLES, "data/*.json"))):
        rel = os.path.relpath(path, ROOT)
        for key, value in json_pairs(json.load(open(path, encoding="utf-8"))):
            if key not in CLASSIFIED:
                continue
            where, name = CLASSIFIED[key]
            if where == "registry":
                members = registry.get(name, {})
                if value not in members:
                    problems.append(f"  {rel}: {key} = {value!r} is not a member of the {name} registry")
                elif members[value] != value:
                    problems.append(f"  {rel}: {key} = {value!r} is an alias of {members[value]!r}")
            elif where == "concept":
                allowed = children.get(name, set()) | {name}
                if value not in allowed and value not in codes:
                    problems.append(f"  {rel}: {key} = {value!r} is not a value of {name}")
                elif value in aliases and aliases[value] != value:
                    problems.append(f"  {rel}: {key} = {value!r} is an alias of {aliases[value]!r}")
            elif where == "errata_kind" and value not in ERRATA_KINDS:
                problems.append(f"  {rel}: kind = {value!r} is not one of {sorted(ERRATA_KINDS)}")


def check_text(problems):
    path = os.path.join(EXAMPLES, "data/ayah.json")
    rel = os.path.relpath(path, ROOT)
    record = json.load(open(path, encoding="utf-8"))
    text = record["text"]
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != record["text_hash"]:
        problems.append(f"  {rel}: text_hash does not match the text")
    if "﻿" in text:
        problems.append(f"  {rel}: the text contains U+FEFF")
    if set(text) & EDITION_MARKS:
        problems.append(f"  {rel}: the text contains an edition mark (۝ ۞ ۩)")
    if re.search(r"[A-Za-z0-9<>&]", text):
        problems.append(f"  {rel}: the text contains Latin, digits or markup")
    if unicodedata.normalize("NFC", text) == text and unicodedata.normalize("NFD", text) == text:
        problems.append(f"  {rel}: the text is already normalised; the example must show the transmitted order")
    if record["basmalah"]["text"] in text:
        problems.append(f"  {rel}: the basmalah is inside the ayah text; it is its own field")


def check_tests(problems):
    for path in sorted(glob.glob(os.path.join(EXAMPLES, "tests/*.py"))):
        result = subprocess.run([sys.executable, path], capture_output=True, text=True)
        if result.returncode:
            problems.append(f"  {os.path.relpath(path, ROOT)} failed:\n{result.stdout}{result.stderr}")
    node = None
    for candidate in ("node", "nodejs"):
        try:
            subprocess.run([candidate, "--version"], capture_output=True, check=True)
            node = candidate
            break
        except (OSError, subprocess.CalledProcessError):
            continue
    for path in sorted(glob.glob(os.path.join(EXAMPLES, "tests/*.js"))):
        if not node:
            print(f"  skipped {os.path.relpath(path, ROOT)}: node is not installed")
            continue
        result = subprocess.run([node, path], capture_output=True, text=True)
        if result.returncode:
            problems.append(f"  {os.path.relpath(path, ROOT)} failed:\n{result.stdout}{result.stderr}")


PATH_REF = re.compile(r"`?(examples/[A-Za-z0-9_./-]+)`?")


def check_paths(problems):
    pages = glob.glob(os.path.join(ROOT, "content/**/*.md"), recursive=True)
    pages += [os.path.join(ROOT, f) for f in ("README.md", "CONTRIBUTING.md", "STRUCTURE.md",
                                               "examples/README.md")]
    for page in pages:
        if not os.path.exists(page):
            continue
        text = open(page, encoding="utf-8").read()
        for ref in sorted(set(PATH_REF.findall(text))):
            ref = ref.rstrip(".,)")
            if ref.endswith("/") or "…" in ref:
                continue
            if not os.path.exists(os.path.join(ROOT, ref)):
                problems.append(f"  {os.path.relpath(page, ROOT)}: {ref!r} does not exist")
    # And the paths examples/README.md lists in its table.
    table = open(os.path.join(EXAMPLES, "README.md"), encoding="utf-8").read()
    for ref in re.findall(r"^\| `([^`]+)` \|", table, flags=re.M):
        if not os.path.exists(os.path.join(EXAMPLES, ref)):
            problems.append(f"  examples/README.md: {ref!r} does not exist")


def main():
    names = load_names()
    problems = []
    for what, fn in (("names", lambda p: check_names(names, p)),
                     ("values", lambda p: check_values(names, p)),
                     ("text", check_text), ("tests", check_tests), ("paths", check_paths)):
        before = len(problems)
        fn(problems)
        print(f"  {what:6s} {'ok' if len(problems) == before else str(len(problems) - before) + ' problems'}")
    if problems:
        print(f"{len(problems)} problems:")
        print("\n".join(problems))
        return 1
    print("ok — every example name is canonical, every value a member, the text clean, "
          "the tests green, and every path real")
    return 0


if __name__ == "__main__":
    sys.exit(main())
