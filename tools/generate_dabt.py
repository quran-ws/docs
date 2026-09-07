"""Generate the dabt mark entries from the registry.

`code` is derived from the vocalized technical name; every other name is
copied from the column that records it. Nothing here is invented: where the
registry says a name is absent, the field is null.
"""
import json, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import code_spelling, display_spelling, _bare
from unicode_props import properties, UNIDATA_VERSION
from registry import records

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "standards/terminology/data/dabt_marks.tsv")
OUT = os.path.join(ROOT, "standards/terminology/concepts")
SCHEMA = os.path.join(ROOT, "standards/terminology/schema.json")

# The registry's columns, by the header in its first row.
COL = {
    "id": "الاسم في الملفات", "codepoints": "المحارف", "family": "الفئة",
    "dabt": "الاسم الاصطلاحي في علم الضبط", "by_shape": "الاسم حسب كتابتها باللغة العربية",
    "intro": "الاسم بحسب ضبط المصحف", "symbol": "الرمز في المصحف كتابة",
    "definition": "الغرض في ضبط المصحف", "definition_en": "الغرض في ضبط المصحف (إنجليزي)",
}

# The phrase in the علم الضبط column that *names* the mark, as opposed to
# describing its shape. Choosing the phrase is editorial; spelling it is not.
NAMING_PHRASE = {
 "fatha": ["الفَتْحَة"], "kasra": ["الكَسْرَة"], "damma": ["الضَّمَّة"],
 "sukun": ["السُّكُون"], "shadda": ["الشَّدَّة"],
 "fathatan": ["تَنْوِين الفَتْح"], "kasratan": ["تَنْوِين الكَسْر"],
 "dammatan": ["تَنْوِين الضَّمّ"],
 "dot": ["النُّقْطَة"], "two-dots": ["النُّقْطَتَان"], "three-dots": ["الثَّلَاث نُقَط"],
 "hamza": ["الهَمْزَة"], "wasla": ["هَمْزَة الوَصْل"],
 "small-alef": ["الأَلِف المَحْذُوفَة"], "maddah": ["المَدَّة"],
 "small-waw": ["الوَاو الصَّغِيرَة"], "small-ya": ["اليَاء الصَّغِيرَة"],
 "small-noon": ["النُّون الصَّغِيرَة"],
 "sifr-mustadir": ["الصِّفْر المُسْتَدِير"], "sifr-mustatil": ["الصِّفْر المُسْتَطِيل"],
 "meem-iqlab": ["المِيم الصَّغِيرَة"],
 "waqf-jaiz": ["الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن"],
 "wasl-awla": ["الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى"],
 "waqf-awla": ["الوَقْف الجَائِز مَعَ كَوْنِ الوَقْف أَوْلَى"],
 "waqf-lazim": ["الوَقْف اللَّازِم"],
 "muanaqah": ["وَقْف المُعَانَقَة"], "waqf-mamnu": ["الوَقْف المَمْنُوع"],
 "saktah": ["عَلَامَة السَّكْتَة"], "seen-reading": ["سِين القِرَاءَة"],
 "imalah": ["الإِمَالَة"], "ishmam": ["الإِشْمَام"], "tashil": ["التَّسْهِيل"],
 "sajdah-sign": ["عَلَامَة السَّجْدَة"],
 "sajdah-line": ["خَطّ السَّجْدَة"],
 "hizb": ["عَلَامَة التَّقْسِيم"],
}

# Display forms that differ from the derived code, each with its evidence.
# Letter names take their spoken form: a letter's name *is* its pronunciation.
DISPLAY = {
    "noon": ("Noon", "GitHub phrase search: noon sakinah 478 vs nun sakinah 118"),
    "meem": ("Meem", "GitHub phrase search: meem sakinah 308 vs mim sakinah 57"),
    "seen": ("Seen", "letter name; unmeasurable directly, both forms are English words"),
}

# Section 20: a name merged away into this entry is deprecated, not an
# alternative spelling, and the note says what it was.
MERGED = {
    "sajdah-sign": (["alamat_mawdi_al_sajdah"],
                    "كان `alamat_mawdi_al_sajdah` مدخلًا مستقلًا يعرف الشيء نفسه، ثم دُمج في هذا المدخل.",
                    "`alamat_mawdi_al_sajdah` was a separate entry defining the same thing; it was merged into this one."),
    "hizb": (["alamat_al_tahzib"],
             "كان `alamat_al_tahzib` مدخلًا مستقلًا يعرف الشيء نفسه، ثم دُمج في هذا المدخل.",
             "`alamat_al_tahzib` was a separate entry defining the same thing; it was merged into this one."),
}

# A note is a fact about the entry that is not its definition.
NOTE = {
    "waqf-mamnu": ("مثبتة في سجل المصحف ولم ترد في هذه الطبعة البتة.",
                   "Registered in the mushaf registry but never used in this edition: zero occurrences."),
    "waqf-jaiz": ("كان `waqf_jaiz` اسم هذه العلامة في سجل المصحف، وهو اسم يصدق على ثلاث علامات جائزة، فأُهمل.",
                  "`waqf_jaiz` was this mark's id in the mushaf registry; it fits three permissible marks, so it is deprecated."),
}

# Section 17: where a mark is confused with what it marks, both entries say so.
BOUNDARIES = {
    "sajdah-sign": (["علامة السجدة رسم في المصحف، والسجدة موضع من النص يسجد عنده."],
                    ["The sajdah mark is a sign in the mushaf; the sajdah is the place in the text at which one prostrates."]),
    "saktah": (["علامة السكتة رسم في المصحف، والسكتة الوقفة نفسها."],
               ["The saktah mark is a sign in the mushaf; the saktah is the pause itself."]),
    "hizb": (["علامة التقسيم رسم في المصحف، والجزء والحزب وأرباعه أقسام من النص تدل عليها."],
             ["The division mark is a sign in the mushaf; the juz, the hizb and its quarters are divisions of the text it points to."]),
}
RELATED = {
    "sajdah-sign": ["sajdah", "sajdah_line"],
    "sajdah-line": ["sajdah_mark", "sajdah"],
    "saktah": ["saktah", "qiraah_mark"],
    "hizb": ["hizb", "rubu_al_hizb", "juz"],
    "meem-iqlab": ["noon_sakinah", "iqlab"],
    "wasla": ["hamzah"], "hamza": ["hamzat_al_wasl"],
    "small-alef": ["rasm", "orthographic_mark"],
    "waqf-lazim": ["waqf", "waqf_mark"], "waqf-mamnu": ["waqf", "waqf_mark"],
    "waqf-jaiz": ["waqf", "waqf_mark"], "wasl-awla": ["waqf", "waqf_mark"],
    "waqf-awla": ["waqf", "waqf_mark"], "muanaqah": ["waqf", "waqf_mark"],
    "shadda": ["harakah", "idgham"], "sukun": ["harakah", "noon_sakinah"],
    "fathatan": ["tanwin", "noon_sakinah"], "kasratan": ["tanwin", "noon_sakinah"],
    "dammatan": ["tanwin", "noon_sakinah"],
}
# Spellings a codebase actually uses for the mark, beyond its previous names.
EXTRA_ALIASES = {
    "hizb": {"hizb_mark", "rub_mark", "rub_el_hizb_mark", "juz_mark"},
    "sajdah-sign": {"sajda_mark", "sajdah_sign", "sajda_sign"},
    "meem-iqlab": {"iqlab_meem", "meem_iqlab"},
    "small-alef": {"dagger_alif", "small_alif", "superscript_alif"},
    "sukun": {"sukoon"}, "fathatan": {"tanween_fath"}, "kasratan": {"tanween_kasr"},
    "dammatan": {"tanween_damm"}, "maddah": {"madda"}, "shadda": {"tashdid", "tashdeed"},
    "wasla": {"hamzat_wasl", "alif_wasl", "wasl"},
}
# Sources beyond the registry row: the term in the tajwid dictionary.
EXTRA_SOURCES = {
    "waqf-lazim": [{"id": "quranpedia_tajweed", "ref": "122", "url": "https://tajweed.quranpedia.net/term/show/122"},
                   {"id": "qattan_mabahith", "ref": "1/152"}],
    "waqf-mamnu": [{"id": "qattan_mabahith", "ref": "1/152"}],
    "waqf-jaiz": [{"id": "qattan_mabahith", "ref": "1/152"}],
    "wasl-awla": [{"id": "qattan_mabahith", "ref": "1/152"}],
    "waqf-awla": [{"id": "qattan_mabahith", "ref": "1/152"}],
    "muanaqah": [{"id": "qattan_mabahith", "ref": "1/152"}],
    "saktah": [{"id": "quranpedia_tajweed", "ref": "126", "url": "https://tajweed.quranpedia.net/term/show/126"}],
    "wasla": [{"id": "quranpedia_tajweed", "ref": "127", "url": "https://tajweed.quranpedia.net/term/show/127"}],
    "ishmam": [{"id": "quranpedia_tajweed", "ref": "131", "url": "https://tajweed.quranpedia.net/term/show/131"}],
    "meem-iqlab": [{"id": "quranpedia_tajweed", "ref": "86", "url": "https://tajweed.quranpedia.net/term/show/86"}],
    "sajdah-sign": [{"id": "itqan", "ref": "1/381"}],
    "sajdah-line": [{"id": "itqan", "ref": "1/381"}],
}

# Registry ids that name a different concept in the dictionary: `hizb` is the
# division and `saktah` is the pause itself. Section 20 records a wrong name
# nowhere but in the boundaries of the right entry, so these ids are neither
# aliases nor deprecated names of the mark; BOUNDARIES states the confusion.
OTHER_CONCEPT_IDS = {"hizb", "saktah"}
# A former id of the mark that no longer names anything: deprecated, with a note.
DEPRECATED_IDS = {"waqf_jaiz"}

# Names an entry has carried before. They stay resolvable as alternative
# spellings, so a project that adopted an earlier name is not stranded.
PREVIOUS_NAMES = {
    "small_noon": {"nun_saghirah", "noon_saghirah"},
    "small_yaa": {"ya_saghirah", "yaa_saghirah"},
    "small_meem": {"mim_saghirah", "meem_saghirah"},
    "small_waw": {"waw_saghirah"},
    "rounded_zero": {"sifr_mustadir"},
    "rectangular_zero": {"sifr_mustatil"},
    "omitted_alif": {"alif_mahdhufah"},
    "three_dots": {"thalath_nuqat"},
    "dot": {"nuqtah"},
    "two_dots": {"nuqtatan"},
    "seen_al_qiraah": {"sin_qiraah"},
    "saktah_mark": {"alamat_al_sakt"},
    "sajdah_line": {"khatt_mujib_al_sajdah"},
    "waqf_al_muanaqah": {"taanuq_al_waqf", "waqf_al_muraqabah", "muraqabah"},
    "tanwin_al_fath": {"tanwin_al_nasb"},
    "tanwin_al_kasr": {"tanwin_al_khafd", "tanwin_al_jarr"},
    "tanwin_al_damm": {"tanwin_al_rafa"},
}

# The registry's own file id, in column 1, for the rows whose id is an Arabic
# phrase rather than a Latin one. It is the entry's name without the article,
# so it must resolve to it.
REGISTRY_SHORTHAND = {
    "tanwin_al_fath": {"tanwin_fath"},
    "tanwin_al_kasr": {"tanwin_kasr"},
    "tanwin_al_damm": {"tanwin_damm"},
}

# A mark's parent is its family. Before this, every mark hung off mushaf_mark
# while mark_family carried the real grouping, so the tree said one thing and
# the field said another. Families with no concept of their own — the catch-all
# `dabt` and the "stands alone" `mustaqill` — keep the generic parent.
FAMILY_PARENT = {
    "harakah": "harakah",
    "tanwin": "tanwin",
    "ijam": "ijam",
    "imlaiyyah": "orthographic_mark",
    "alamat_qiraah": "qiraah_mark",
    "waqf": "waqf_mark_type",
}
# A waqf mark is a value of the waqf-mark classification, not a mark of its own:
# section 27 gives waqf_lazim exactly this shape.
FAMILY_KIND = {"waqf": "classification_value"}

FAMILY = {"حركة": "harakah", "تنوين": "tanwin", "نقط": "ijam", "إملائية": "imlaiyyah",
          "ضبط": "dabt", "وقف": "waqf", "علامة قراءة": "alamat_qiraah", "مستقل": "mustaqill"}

# The registry answers "what does this mark do", which is the definition. Why we
# model it is a property of the family, not of the individual mark: every waqf
# mark is modelled for the same reason, and section 16 forbids a purpose that
# only restates the definition. So the purpose is written once per family, in
# both languages, exactly as section 27's own waqf_lazim example words it.
PURPOSE = {
    "harakah": (
        "نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم "
        "بدلًا من قراءة صورة الشكل.",
        "Used as a value of harakah, so that a letter's pronunciation is read from it in "
        "analysis, rendering and teaching rather than from the shape of the mark."),
    "tanwin": (
        "نستخدمها قيمة من قيم التنوين، فنقرأ منها نطق آخر الاسم وحكمه بدلًا من قراءة صورة الشكل.",
        "Used as a value of tanwin, so that the pronunciation of the noun's ending and its "
        "ruling are read from it rather than from the shape of the mark."),
    "ijam": (
        "نستخدمها قيمة من قيم النقط، فنميز بها الحرف عن الحرف الذي يشاركه في الرسم في التحليل والبحث.",
        "Used as a value of ijam, so that a letter is told apart from those sharing its "
        "skeleton in analysis and in search."),
    "imlaiyyah": (
        "نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.",
        "Used as a value of the orthographic marks, so that software can tell where the rasm "
        "departs from the pronunciation."),
    "waqf": (
        "نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في "
        "التطبيقات بدلًا من قراءة صورة الرمز.",
        "Used as a value of the waqf mark type, so that rendering, teaching and warnings in "
        "applications branch on it rather than on the shape of the sign."),
    "alamat_qiraah": (
        "نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.",
        "Used as a value of the qiraah marks, so that the reader is alerted to a particular "
        "delivery at its place."),
    "dabt": (
        "نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.",
        "Used as a mark of the mushaf, so that rendering and analysis know where it sits and "
        "what it points to."),
    "mustaqill": (
        "نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.",
        "Used as a mark of the mushaf, so that rendering and analysis know where it sits and "
        "what it points to."),
}


def parse_codepoints(cell):
    return [f"U+{m}" for m in re.findall(r"U\+([0-9A-Fa-f]{4,6})", cell or "")]


def display_for(code, parts):
    words = " ".join(display_spelling(p) for p in parts).split()
    out, ev = [], []
    for w in words:
        key = w.lower()
        key = key[3:] if key.startswith("al-") else key
        if key in DISPLAY:
            out.append(DISPLAY[key][0]); ev.append(DISPLAY[key][1])
        else:
            out.append(w)
    return " ".join(out), ("; ".join(dict.fromkeys(ev)) or None)


def unicode_fields():
    """The fields schema.json lets a unicode block carry.

    The block is read from the Unicode database of the running interpreter, so
    the database version is recorded beside it when the schema has a place for
    it: two builds on two Pythons then say why they differ.
    """
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    return set(schema["properties"]["unicode"]["items"]["properties"])


def build():
    rows = records(TSV, header_in_first_row=True)
    allowed = unicode_fields()
    unconsumed = [r[COL["id"]] for r in rows if r[COL["id"]] not in NAMING_PHRASE]
    if unconsumed:
        raise SystemExit(f"dabt_marks.tsv rows with no naming phrase, which would be "
                         f"silently dropped: {unconsumed} — add them to NAMING_PHRASE")
    entries = []
    for r in rows:
        old = r[COL["id"]]
        parts = NAMING_PHRASE[old]
        code = "_".join(code_spelling(p) for p in parts)
        disp, ev = display_for(code, parts)
        # The familiar form must resolve to the concept, so it becomes an alias.
        disp_alias = disp.lower().replace("-", "_").replace(" ", "_")
        intro = r[COL["intro"]]
        absent = "لَمْ تُذْكَر" in intro or "لَمْ تُفْرَد" in intro or "لَمْ تَرِد" in intro
        family = FAMILY.get(r[COL["family"]], r[COL["family"]])
        e = {
            "concept": code,
            "names": {
                "code": code,
                "display": disp,
                **({"display_evidence": ev} if ev else {}),
                "arabic": {"vocalized": " ".join(parts), "singular": _bare(" ".join(parts))},
                "dabt": r[COL["dabt"]],
                "by_shape": r[COL["by_shape"]] or None,
                "mushaf_introduction": None if absent else (intro or None),
            },
            "kind": FAMILY_KIND.get(family, "mark"),
            "category": "dabt",
            "parent": FAMILY_PARENT.get(family, "mushaf_mark"),
            "origin": "quranic",
            "tier": "core",
            "status": "draft",
            "symbol": r[COL["symbol"]] or None,
            # The definition column defines the mark; its English twin is that
            # same definition translated, not a second fact about the mark.
            "definition": r[COL["definition"]],
            "definition_en": r[COL["definition_en"]],
            "purpose": PURPOSE[family][0],
            "purpose_en": PURPOSE[family][1],
            **({"boundaries": BOUNDARIES[old][0], "boundaries_en": BOUNDARIES[old][1]}
               if old in BOUNDARIES else {}),
            "alternative_spellings": sorted(
                ({old, old.replace("-", "_"), disp_alias}
                 | PREVIOUS_NAMES.get(code, set())
                 | REGISTRY_SHORTHAND.get(code, set())
                 | EXTRA_ALIASES.get(old, set()))
                - {code} - DEPRECATED_IDS - OTHER_CONCEPT_IDS
                - ({old, old.replace("-", "_")}
                   if old.replace("-", "_") in DEPRECATED_IDS else set())),
            **({"deprecated": sorted(({old, old.replace("-", "_")}
                                       if old.replace("-", "_") in DEPRECATED_IDS else set())
                                      | set(MERGED.get(old, ([],))[0]))}
               if old.replace("-", "_") in DEPRECATED_IDS or old in MERGED else {}),
            **({"related": RELATED[old]} if old in RELATED else {}),
            **({"note": NOTE[old][0], "note_en": NOTE[old][1]} if old in NOTE else
               {"note": MERGED[old][1], "note_en": MERGED[old][2]} if old in MERGED else {}),
            "unicode": [],
            "mark_family": family,
            "sources": [{"id": "hafs_svg_registry", "ref": f"standard!{old}"}] + EXTRA_SOURCES.get(old, []),
        }
        for cp in parse_codepoints(r[COL["codepoints"]]):
            p = properties(cp)
            block = {k: p[k] for k in ("cp", "name", "category", "combining_class", "block")}
            if "unidata" in allowed:
                block["unidata"] = UNIDATA_VERSION
            e["unicode"].append(block)
            e["names"].setdefault("unicode", p["name"])
        entries.append(e)
    return entries


if __name__ == "__main__":
    import yaml
    os.makedirs(OUT, exist_ok=True)
    made = build()
    for e in made:
        path = os.path.join(OUT, f"{e['concept']}.yml")
        with open(path, "w", encoding="utf-8") as fh:
            yaml.safe_dump(e, fh, allow_unicode=True, sort_keys=False, width=88)
    print(f"{len(made)} entries written to standards/terminology/concepts/")
    renamed = [e for e in made
               if e["concept"] not in {a.replace("-", "_") for a in e["alternative_spellings"]}]
    print(f"{len(renamed)} renamed from the registry's id")
    for e in made:
        if e["names"]["display"] != " ".join(w.capitalize() for w in e["concept"].split("_")):
            print(f"  display differs: {e['concept']:26} → {e['names']['display']}")
