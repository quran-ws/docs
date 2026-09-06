"""Check that every name used in the prose actually exists.

Examples go stale silently: a concept is renamed, and the page that documents
the rule keeps showing the old name. This has already happened three times, so
it is checked rather than remembered.

Names shown deliberately as wrong — the "avoid" side of an example — are listed
in COUNTER_EXAMPLES. Everything else must resolve through aliases.json, or —
for a member of a closed set, such as a rawi — through registry_aliases.json.

Three more things go stale the same way and are checked here too:
  * a reference to "section N" of the standard, once the sections are numbered
    in their headings, must name a section that exists, in every file under
    content/, tools/, standards/ and skills/;
  * the English and Arabic standard must carry the same numbered H2 sequence;
  * a YAML example in the standard that shows an entry (`concept: …`) must parse,
    each field it shows must satisfy schema.json, and where the entry exists the
    example must show what the file says.

    python3 tools/check_examples.py
"""
import glob, json, os, re, sys
import yaml
from jsonschema import Draft202012Validator

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIASES = os.path.join(ROOT, "standards/terminology/aliases.json")
REGISTRY_ALIASES = os.path.join(ROOT, "standards/terminology/registry_aliases.json")
SCHEMA = os.path.join(ROOT, "standards/terminology/schema.json")
CONCEPTS = os.path.join(ROOT, "standards/terminology/concepts")
STANDARD = {"en": "content/en/03-terminology/standard.md",
            "ar": "content/ar/03-terminology/standard.md"}
PAGES = [STANDARD["ar"], STANDARD["en"],
         "content/ar/03-terminology/decisions.md",
         "content/en/03-terminology/decisions.md",
         "content/ar/02-quranic-text/index.md",
         "content/en/02-quranic-text/index.md",
         "content/ar/01-intro/writing-style.md",
         "content/ar/01-intro/writing-guides.md",
         "content/en/01-intro/writing-style.md",
         "content/en/01-intro/writing-guides.md",
         "tools/README.md", "README.md", "CONTRIBUTING.md", "STRUCTURE.md"]
# Where a "section N" may be written, and the forms it takes.
REFERENCE_TREES = ["content", "tools", "standards", "skills", "README.md",
                   "CONTRIBUTING.md", "STRUCTURE.md"]
REFERENCE_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".tsv", ".txt"}
SECTION_REF = re.compile(r"(?:\bsections?\s+|القسم\s+|القسمين\s+|§\s?)(\d+)(?:\s*(?:to|–|-|و|,|and)\s*(\d+))?")
NUMBERED_H2 = re.compile(r"^## (\d+)\.\s", re.M)
H2 = re.compile(r"^## ", re.M)
YAML_BLOCK = re.compile(r"^```yaml\s*\n(.*?)^```", re.M | re.S)
# Keys an example may show that are not entry fields: `canonical` names the
# rule being illustrated, not a field of the entry.
EXAMPLE_ONLY_KEYS = {"canonical"}

# Shown on purpose as the wrong form, so they must NOT resolve.
COUNTER_EXAMPLES = {
    "al_fathah", "al_sukun", "al_ishmam", "al_tashil", "hamzah_al_wasl",
    "waqf_al_lazim", "noon_al_sakinah", "rasm_al_uthmani",
    "quran_section", "quran_type", "mushaf_type", "revelation_classification_makki",
    "customer_identifier_value",
    # decisions.md argues against these forms by name
    "abu_amrw", "add_kufi", "dots_three", "embracing_waqf",
    "waqf_type", "recitation_type", "item_type", "data_type", "al_waqf_lazim_mark",
    "mawadi_al_sajdah", "sajdat_at_tilawah", "orthographic_rasm", "qalqalat_sughra",
    "mustawi_al_tarafayn", "nasikh_walmansukh", "paired_waqf", "ras_al_ayah_mark",
    "waqf_jaiz_mustawi_tarafayn", "waqf_muanaqah",
}
# Vocabulary of the standard itself: field names, kinds, categories, source ids.
SCHEMA_WORDS = {
    # data files referred to by name in the prose
    "established_spellings", "letter_names", "dabt_marks", "general_words",
    "display_evidence", "alternative_spellings", "english_glosses", "by_shape",
    "definition_en", "purpose_en", "boundaries_en", "note_en",
    "mushaf_introduction", "combining_class", "do_not_confuse_with", "arabic_status",
    "classification_value", "text_unit", "layout_unit", "word_root",
    "textual_concept", "recitation_concept", "typographic_unit", "linguistic_unit",
    "technical_unit", "presentation_concept", "orthographic_concept", "rasm_type",
    "quran_name", "recitation_feature", "recitation_practice",
    "surah_classification", "ayah_numbering", "mushaf_marks", "recitation_pace",
    "quranic_sciences",
    "recitation_style", "waqf_mark_type", "waqf_ruling", "surah_group",
    "ayah_numbering_system", "revelation_order", "revelation_classification",
    "recitation_performance_style", "instructional_ayah_repetition",
    "surah_id", "ayah_id", "word_id", "mushaf_id", "surah_number", "ayah_number",
    "page_number", "word_position", "token_position", "line_position",
    "display_order", "has_sajdah", "is_active", "is_included", "ayah_parts",
    "data_wid", "letter_names", "code_spelling",
    # data file names referenced in prose
    "dabt_marks", "tajweed_engine_rules", "hafs_svg_glossary", "hafs_svg_structure",
    "hafs_svg_word_attributes", "hafs_svg_main_structure",
    "writing_guides", "writing_style",
    "qattan_mabahith", "quranpedia_tajweed", "jamharah_dictionary",
    "tajweed_engine", "hafs_svg_registry",
    "search_key", "utf8mb4_bin", "part_of", "mark_family",
    "test_translit", "build_aliases", "generate_dabt", "generate_dictionary",
    "check_conformance", "tool_defects",
    "unicode_props", "measure_display", "check_examples", "check_example_files",
    "generate_registries", "generate_tajwid_registry", "audit_text",
    "test_text_invariants", "quran_text", "check_issue_templates",
    # names the standard uses as illustrations, not as entries
    "waqf_lazim_mark", "tafsir_bi_al_ray", "alamat_qiraah", "with_head", "snake_case",
    "start_ms", "end_ms", "recitation_id", "display_measurements",
    "unidata_version", "requirements", "build_yml", "pages_yml",
    "check_registries", "build_registry_aliases", "registry_aliases",
    "extract_ayah_counts", "ayah_counts", "turath_cache",
    "generate_skill", "skill_template", "audit_terminology", "update_check",
    # registry file names, and the sources their rows cite
    "qiraat_ayah_map", "ghayat_al_nihayah", "bayan_dani", "nasser_transmission",
}


def section_counts():
    """How many sections each standard has, and the numbers its H2s carry.

    Before the headings are numbered the count is the H2 count; once they are,
    the sequence itself is checked to be 1..N in both languages.
    """
    counts, sequences, problems = {}, {}, []
    for lang, rel in STANDARD.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        numbers = [int(n) for n in NUMBERED_H2.findall(text)]
        sequences[lang] = numbers
        counts[lang] = len(numbers) if numbers else len(H2.findall(text))
        if numbers and numbers != list(range(1, len(numbers) + 1)):
            problems.append(f"  {rel}: numbered headings run {numbers[:3]}…{numbers[-3:]}, "
                            f"not 1..{len(numbers)}")
    if len(sequences) == 2 and sequences["en"] != sequences["ar"]:
        problems.append(f"  the English standard numbers {len(sequences['en'])} sections "
                        f"and the Arabic {len(sequences['ar'])}; they mirror each other")
    return min(counts.values()) if counts else None, problems


def reference_files():
    for top in REFERENCE_TREES:
        path = os.path.join(ROOT, top)
        if os.path.isfile(path):
            yield path
            continue
        for d, dirs, names in os.walk(path):
            dirs[:] = [x for x in dirs if x not in {"node_modules", "dist", ".astro", "__pycache__"}]
            for n in sorted(names):
                if os.path.splitext(n)[1] in REFERENCE_SUFFIXES:
                    yield os.path.join(d, n)


def check_section_references(limit):
    problems = []
    for path in reference_files():
        text = open(path, encoding="utf-8", errors="ignore").read()
        for number, line in enumerate(text.splitlines(), 1):
            for m in SECTION_REF.finditer(line):
                for n in (m.group(1), m.group(2)):
                    if n and int(n) > limit:
                        problems.append(f"  {os.path.relpath(path, ROOT)}:{number}: "
                                        f"refers to section {n}; the standard has {limit}")
    return problems


def check_yaml_examples():
    """Every entry shown in the standard is a true excerpt of an entry."""
    problems = []
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    for rel in STANDARD.values():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in YAML_BLOCK.finditer(text):
            block = m.group(1)
            if not re.search(r"^concept:", block, re.M):
                continue
            line = text[:m.start()].count("\n") + 1
            where = f"  {rel}:{line}"
            try:
                shown = yaml.safe_load(block)
            except yaml.YAMLError as exc:
                problems.append(f"{where}: YAML does not parse — {str(exc).splitlines()[0]}")
                continue
            if not isinstance(shown, dict) or not shown.get("concept"):
                continue    # the empty template, which shows the shape and no entry
            fields = {k: v for k, v in shown.items() if k not in EXAMPLE_ONLY_KEYS}
            # An excerpt shows some fields of an entry, and some keys of an
            # object field, so what an object requires is not asked of it.
            partial = {"type": "object", "additionalProperties": False,
                       "properties": {k: {kk: vv for kk, vv in schema["properties"].get(k, {}).items()
                                          if kk != "required"} for k in fields}}
            for err in Draft202012Validator(partial).iter_errors(fields):
                problems.append(f"{where}: {'.'.join(str(p) for p in err.path) or '(root)'}: "
                                f"{err.message[:100]}")
            entry_path = os.path.join(CONCEPTS, f"{shown['concept']}.yml")
            if not os.path.exists(entry_path):
                continue
            entry = yaml.safe_load(open(entry_path, encoding="utf-8"))
            for k, v in fields.items():
                actual = entry.get(k)
                if isinstance(v, dict) and isinstance(actual, dict):
                    diff = {kk for kk, vv in v.items() if norm(actual.get(kk)) != norm(vv)}
                    if diff:
                        problems.append(f"{where}: {k}.{'/'.join(sorted(diff))} differs from "
                                        f"concepts/{shown['concept']}.yml")
                elif norm(actual) != norm(v):
                    problems.append(f"{where}: {k} differs from concepts/{shown['concept']}.yml")
    return problems


def norm(value):
    return " ".join(value.split()) if isinstance(value, str) else value


def main():
    aliases = json.load(open(ALIASES, encoding="utf-8"))
    members = set()
    if os.path.exists(REGISTRY_ALIASES):
        for names in json.load(open(REGISTRY_ALIASES, encoding="utf-8")).values():
            members.update(names)
    # a registry is named by its file: `tajwid_rules` is a set, not a member
    registries = {os.path.basename(p)[:-4]
                  for p in glob.glob(os.path.join(ROOT, "standards/terminology/registries/*.tsv"))}
    # section 20 — a deprecated name keeps resolving, from the entry that
    # deprecated it; the skill's lookup.py reads the same field
    deprecated = set()
    for path in glob.glob(os.path.join(CONCEPTS, "*.yml")):
        entry = yaml.safe_load(open(path, encoding="utf-8")) or {}
        deprecated.update(entry.get("deprecated") or [])
    members |= deprecated
    problems = []
    for rel in PAGES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for name in sorted(set(re.findall(r"\b([a-z][a-z0-9]*(?:_[a-z0-9]+)+)\b", text))):
            if name in SCHEMA_WORDS or name in COUNTER_EXAMPLES or name in registries:
                continue
            # section 11 — a collection is the code plus s, so `harf_muqattas` is a name
            plural_of = name[:-1] if name.endswith("s") else None
            if plural_of in aliases or plural_of in members:
                continue
            if name not in aliases and name not in members:
                problems.append(f"  {rel}: {name!r} resolves to no concept or member")
    for name in sorted(COUNTER_EXAMPLES):
        if name in aliases:
            problems.append(f"  {name!r} is listed as a counter-example but resolves to "
                            f"{aliases[name]!r} — it is no longer wrong")

    limit, heading_problems = section_counts()
    problems += heading_problems
    if limit:
        problems += check_section_references(limit)
    problems += check_yaml_examples()

    if problems:
        print(f"{len(problems)} problems:")
        print("\n".join(problems))
        return 1
    print(f"ok — every name in the prose resolves, every counter-example still doesn't, "
          f"every section reference is within {limit}, and every YAML example is a true excerpt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
