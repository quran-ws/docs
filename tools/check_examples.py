"""Check that every name used in the prose actually exists.

Examples go stale silently: a concept is renamed, and the page that documents
the rule keeps showing the old name. This has already happened three times, so
it is checked rather than remembered.

Names shown deliberately as wrong — the "avoid" side of an example — are listed
in COUNTER_EXAMPLES. Everything else must resolve through aliases.json.

    python3 tools/check_examples.py
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIASES = os.path.join(ROOT, "standards/terminology/aliases.json")
PAGES = ["content/ar/03-terminology/standard.md",
         "content/ar/01-intro/writing-style.md",
         "content/ar/01-intro/writing-guides.md",
         "content/en/01-intro/writing-style.md",
         "content/en/01-intro/writing-guides.md",
         "tools/README.md", "CONTRIBUTING.md", "STRUCTURE.md"]

# Shown on purpose as the wrong form, so they must NOT resolve.
COUNTER_EXAMPLES = {
    "al_fathah", "al_sukun", "al_ishmam", "al_tashil", "hamzah_al_wasl",
    "alamah_al_tahzib", "waqf_al_lazim", "noon_al_sakinah", "rasm_al_uthmani",
    "quran_section", "quran_type", "mushaf_type", "revelation_classification_makki",
    "customer_identifier_value",
}
# Vocabulary of the standard itself: field names, kinds, categories, source ids.
SCHEMA_WORDS = {
    # data files referred to by name in the prose
    "established_spellings", "letter_names", "dabt_marks", "general_words",
    "display_evidence", "alternative_spellings", "english_glosses", "by_shape",
    "mushaf_introduction", "combining_class", "do_not_confuse_with", "arabic_status",
    "classification_value", "text_unit", "layout_unit", "word_root",
    "textual_concept", "recitation_concept", "typographic_unit", "linguistic_unit",
    "technical_unit", "presentation_concept", "orthographic_concept", "rasm_type",
    "quran_name", "recitation_feature", "recitation_practice",
    "surah_classification", "ayah_numbering", "mushaf_marks", "recitation_pace",
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
    "test_translit", "build_aliases", "generate_dabt", "generate_dictionary",
    "generate_concepts", "unicode_props", "measure_display", "check_examples",
}


def main():
    aliases = json.load(open(ALIASES))
    problems = []
    for rel in PAGES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for name in sorted(set(re.findall(r"\b([a-z][a-z0-9]*(?:_[a-z0-9]+)+)\b", text))):
            if name in SCHEMA_WORDS or name in COUNTER_EXAMPLES:
                continue
            if name not in aliases:
                problems.append(f"  {rel}: {name!r} resolves to no concept")
    for name in sorted(COUNTER_EXAMPLES):
        if name in aliases:
            problems.append(f"  {name!r} is listed as a counter-example but resolves to "
                            f"{aliases[name]!r} — it is no longer wrong")
    if problems:
        print(f"{len(problems)} problems:")
        print("\n".join(problems))
        return 1
    print("ok — every name in the prose resolves, and every counter-example still doesn't")
    return 0


if __name__ == "__main__":
    sys.exit(main())
