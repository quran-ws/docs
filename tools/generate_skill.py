"""Build the agent skill: the standard and its dictionary, packaged for an AI.

Section 29 says the human-readable documents are output from the machine-readable
source. An agent reading a codebase needs the same thing in a third shape: the
rules as prose it can follow, the dictionary as data it can resolve names
against, and scripts that answer "is this name canonical" without a model having
to guess.

    python3 tools/generate_skill.py

Everything under skills/quranic-terminology/ is written by this script. The
prose it does not generate — the standard, the decision record, the dictionary —
is copied from content/en, so the skill cannot state a rule the standard does
not.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
from translit import code_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMS = os.path.join(ROOT, "standards/terminology")
CONCEPTS = os.path.join(TERMS, "concepts")
TEMPLATE = os.path.join(ROOT, "tools/skill_template")
OUT = os.path.join(ROOT, "skills/quranic-terminology")

# The prose the skill hands to a reader, copied rather than restated.
REFERENCES = [
    ("content/en/reference/standard.md", "standard.md"),
    ("content/en/reference/dictionary.md", "dictionary.md"),
    ("content/en/reference/decisions.md", "decisions.md"),
    ("content/en/reference/registries.md", "registries.md"),
]
# The pages link each other by the site's absolute path. Inside the skill they
# sit side by side, so the link becomes the file next door; an anchor stays.
SITE_LINK = re.compile(r"\(/guidelines/en/reference/(standard|dictionary|decisions|registries)/(#[^)]*)?\)")


def relink(text):
    return SITE_LINK.sub(lambda m: f"({m.group(1)}.md{m.group(2) or ''})", text)

FIELDS = ("kind", "category", "origin", "tier", "status", "plural", "parent",
          "registry", "definition_en", "purpose_en", "boundaries_en", "note_en",
          "alternative_spellings", "english_glosses", "deprecated", "related",
          "symbol", "mark_family")

DERIVED_PLURAL = re.compile(r"^[a-z][a-z_]*[aiu][a-z_]*$")


def load():
    out = []
    for path in sorted(glob.glob(os.path.join(CONCEPTS, "*.yml"))):
        out.append(yaml.safe_load(open(path, encoding="utf-8")))
    return out


def arabic_plurals(entry):
    """The Arabic plural as it would be spelled in code, when it derives.

    Section 11 forbids it as a name, so the audit needs to recognise it. An
    unvocalized plural cannot be derived, and a guess would be worse than a
    gap, so it is left out.
    """
    plural = (entry["names"].get("arabic") or {}).get("plural")
    if not plural:
        return []
    try:
        derived = code_spelling(plural)
    except ValueError as exc:
        print(f"warning: {entry['concept']}: arabic plural {plural!r} does not derive "
              f"({exc}); the audit will not recognise it", file=sys.stderr)
        return []
    return [derived] if DERIVED_PLURAL.match(derived) else []


REPO = "quran-ws/docs"   # the fallback when there is no git remote to read

# Everything the skill is built from. A change anywhere here is a new snapshot;
# a change anywhere else is not.
INPUTS = ("standards/terminology", "content/en/reference",
          "tools/translit.py", "tools/registry.py", "tools/unicode_props.py",
          "tools/skill_template")


def content_hash():
    """A hash of the inputs: the same inputs give the same stamp on any machine.

    A git commit would not: the skill is generated before the commit that
    carries it, so a commit stamp always names the previous commit and every
    rebuild rewrites it. The hash changes only when something the skill is made
    of changes, which is what "is my copy current" asks.
    """
    digest = hashlib.sha256()
    for top in INPUTS:
        path = os.path.join(ROOT, top)
        files = [path] if os.path.isfile(path) else sorted(
            os.path.join(d, f) for d, _, names in os.walk(path) for f in names
            if "__pycache__" not in d)
        for f in files:
            digest.update(os.path.relpath(f, ROOT).encode("utf-8") + b"\0")
            digest.update(open(f, "rb").read() + b"\0")
    return digest.hexdigest()[:16]


def version(release=None):
    """The snapshot this skill is, so `scripts/update_check.py` can tell whether
    a copy has fallen behind: it compares `snapshot` with the one published in
    the repository's own skill. `--release` adds the commit as a human label;
    it is never what the comparison reads.
    """
    if release is None:
        release = "--release" in sys.argv
    stamp = {"repo": REPO, "snapshot": content_hash(), "commit": None}
    try:
        remote = subprocess.run(["git", "-C", ROOT, "remote", "get-url", "origin"],
                                capture_output=True, text=True, check=True).stdout.strip()
        match = re.search(r"github\.com[:/](.+?)(?:\.git)?$", remote)
        if match:
            stamp["repo"] = match.group(1)
        if release:
            stamp["commit"] = subprocess.run(
                ["git", "-C", ROOT, "rev-parse", "--short=12", "HEAD"],
                capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    return stamp


def clean(value):
    """Folded YAML keeps a trailing newline; JSON should not carry it."""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def terminology(entries):
    concepts = {}
    for e in entries:
        names = e["names"]
        item = {"code": names["code"], "display": names.get("display"),
                "arabic": (names.get("arabic") or {}).get("vocalized"),
                "transliteration": names.get("transliteration")}
        for field in FIELDS:
            if e.get(field):
                item[field] = e[field]
        plurals = arabic_plurals(e)
        if plurals:
            item["arabic_plurals"] = plurals
        concepts[e["concept"]] = {k: clean(v) for k, v in item.items() if v is not None}

    aliases = json.load(open(os.path.join(TERMS, "aliases.json"), encoding="utf-8"))
    members = json.load(open(os.path.join(TERMS, "registry_aliases.json"), encoding="utf-8"))
    return {
        "standard": "Quranic Software Terminology Standard",
        "version": version(),
        "source": "https://github.com/quran-ws/docs",
        "note": "Generated by tools/generate_skill.py. Edit the concept files, not this.",
        "concepts": concepts,
        "aliases": aliases,
        "registry_members": members,
    }


SPELLING_TABLES = ("letter_names.tsv", "established_spellings.tsv",
                   "general_words.tsv", "connectives.tsv")
# translit.py finds its tables through one constant. Inside the skill they sit
# in data/spelling/, so the copy has that one line repointed, nothing else.
TABLES_DIR_LINE = re.compile(r"^TABLES_DIR = .*?\n(?:\s+.*?\n)*?(?=\n)", re.M)
SKILL_TABLES_DIR = ('TABLES_DIR = _os.path.join(_os.path.dirname(_os.path.dirname(\n'
                    '    _os.path.abspath(__file__))), "data", "spelling")\n')
# Modules the scripts import beside spell.py, copied whole.
SHARED_MODULES = ("registry.py",)


def write_speller():
    """Copy the derivation itself, so the skill spells names by the same function."""
    source = open(os.path.join(ROOT, "tools/translit.py"), encoding="utf-8").read()
    patched, count = TABLES_DIR_LINE.subn(SKILL_TABLES_DIR, source, count=1)
    if count != 1 or '"standards", "terminology", "data"' in patched:
        raise SystemExit("tools/translit.py: the TABLES_DIR assignment was not found, "
                         "so the skill's spell.py would not find its tables")
    tables = os.path.join(OUT, "data/spelling")
    os.makedirs(tables, exist_ok=True)
    for name in SPELLING_TABLES:
        shutil.copy(os.path.join(TERMS, "data", name), os.path.join(tables, name))
    open(os.path.join(OUT, "scripts/spell.py"), "w", encoding="utf-8").write(patched)
    for name in SHARED_MODULES:
        shutil.copy(os.path.join(ROOT, "tools", name), os.path.join(OUT, "scripts", name))


def strip_frontmatter(text):
    """The pages are Starlight pages; the skill wants the prose."""
    if text.startswith("---"):
        end = text.index("\n---", 3) + len("\n---")
        head = text[:end]
        title = re.search(r"^title: (.+)$", head, re.M)
        text = text[end:].lstrip("\n")
        if title:
            text = f"# {title.group(1).strip()}\n\n{text}"
    def aside(match):
        title, body = match.group(1), match.group(2).strip().splitlines()
        lines = [f"> **{title}**", ">"] if title else []
        return "\n".join(lines + [f"> {line}".rstrip() for line in body]) + "\n"

    return re.sub(r"^:::\w+(?:\[([^\]]*)\])?\s*\n(.*?)^:::\s*$",
                  aside, text, flags=re.M | re.S)


def slug(title):
    """The anchor GitHub and Starlight give a heading."""
    text = re.sub(r"[`*_]", "", title.strip().lower())
    return re.sub(r"[\s]+", "-", re.sub(r"[^\w\s-]", "", text)).strip("-")


def with_contents(text):
    """Prepend a numbered table of contents to a reference, under its title.

    The scripts cite the standard by section number and an agent must not have
    to count H2s in a 1,700-line file to find one. The number is the one the
    heading carries; a heading without one gets its ordinal, so the table is
    numbered either way and the numbers agree with the source's own.
    """
    headings = []
    for n, match in enumerate(re.finditer(r"^## (.+?)\s*$", text, re.M), 1):
        title = match.group(1)
        numbered = re.match(r"(\d+)\.\s+(.*)", title)
        number, name = (numbered.group(1), numbered.group(2)) if numbered else (str(n), title)
        headings.append(f"- {number}. [{name}](#{slug(title)})")
    if not headings:
        return text
    contents = "**Contents** — the scripts cite these numbers\n\n" + "\n".join(headings) + "\n\n"
    first_h1 = re.search(r"^# .+\n", text, re.M)
    cut = first_h1.end() if first_h1 else 0
    return text[:cut] + "\n" + contents + text[cut:].lstrip("\n")


SKILL_README = """# quranic-terminology

An agent skill for naming the concepts of Quranic software by the Quran.ws
Terminology Standard, and for auditing a codebase against it. It carries the
standard, its dictionary ({entries} concepts, {spellings} recorded spellings),
the registries of the closed sets, and scripts that resolve any spelling to its
canonical name, derive a name from vocalized Arabic, draft an entry for a new
concept, and report every identifier in a tree that the standard would write
differently. Everything here is generated from
<https://github.com/{repo}> by `tools/generate_skill.py`; snapshot
`{snapshot}`. Edit the source there, not this directory.

To install it in Claude Code as a plugin, run
`/plugin marketplace add {repo}` and then
`/plugin install quranic-terminology@quran-ws`; `/plugin update` keeps it
current. To install a copy instead, put this directory at
`~/.claude/skills/quranic-terminology/` (every project) or at
`<project>/.claude/skills/quranic-terminology/` (one project) and run
`python3 scripts/update_check.py` now and then to learn when the copy has
fallen behind. The scripts need Python 3 and nothing else. `SKILL.md` is what
the agent reads; start there.
"""


def write_assets_and_readme(data, entries):
    """The files beside the scripts: the audit configuration and the proposal
    template an agent copies, and a README for a person who finds the directory."""
    assets = os.path.join(TEMPLATE, "assets")
    if os.path.isdir(assets):
        shutil.copytree(assets, os.path.join(OUT, "assets"))
    readme = SKILL_README.format(entries=len(entries), spellings=len(data["aliases"]),
                                 repo=data["version"]["repo"],
                                 snapshot=data["version"]["snapshot"])
    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(readme)


def fill(text, values):
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    left = re.findall(r"\{\{(\w+)\}\}", text)
    if left:
        raise SystemExit(f"the template has placeholders nothing filled: {sorted(set(left))}")
    return text


def main():
    entries = load()
    data = terminology(entries)

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "data/registries"))
    os.makedirs(os.path.join(OUT, "references"))
    shutil.copytree(os.path.join(TEMPLATE, "scripts"), os.path.join(OUT, "scripts"))

    with open(os.path.join(OUT, "data/terminology.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    for tsv in sorted(glob.glob(os.path.join(TERMS, "registries/*.tsv"))):
        shutil.copy(tsv, os.path.join(OUT, "data/registries", os.path.basename(tsv)))
    shutil.copy(os.path.join(TERMS, "schema.json"), os.path.join(OUT, "data/schema.json"))
    write_speller()

    for source, name in REFERENCES:
        text = relink(strip_frontmatter(open(os.path.join(ROOT, source), encoding="utf-8").read()))
        if name == "standard.md":
            text = with_contents(text)
        open(os.path.join(OUT, "references", name), "w", encoding="utf-8").write(text)
    write_assets_and_readme(data, entries)

    categories = sorted({e["category"] for e in entries})
    registries = sorted(os.path.basename(p)[:-4]
                        for p in glob.glob(os.path.join(TERMS, "registries/*.tsv")))
    skill = fill(open(os.path.join(TEMPLATE, "SKILL.md"), encoding="utf-8").read(), {
        "ENTRIES": len(entries),
        "SPELLINGS": len(data["aliases"]),
        "CATEGORIES": ", ".join(f"`{c}`" for c in categories),
        "REGISTRIES": ", ".join(f"`{r}`" for r in registries),
        "ADOPTED": sum(1 for e in entries if e["status"] == "adopted"),
        "DRAFT": sum(1 for e in entries if e["status"] == "draft"),
        "SNAPSHOT": data["version"]["snapshot"],
        "REPO": REPO,
    })
    open(os.path.join(OUT, "SKILL.md"), "w", encoding="utf-8").write(skill)

    stamp = data["version"]
    print(f"skill written to {os.path.relpath(OUT, ROOT)}/ — "
          f"{len(entries)} entries, {len(data['aliases'])} spellings, "
          f"{len(registries)} registries, built from "
          f"{stamp['repo']} snapshot {stamp['snapshot']}"
          f"{' at ' + stamp['commit'] if stamp.get('commit') else ''}")


if __name__ == "__main__":
    main()
