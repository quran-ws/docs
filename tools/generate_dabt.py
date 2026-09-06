"""Generate the dabt mark entries from the registry.

`code` is derived from the vocalized technical name; every other name is
copied from the column that records it. Nothing here is invented: where the
registry says a name is absent, the field is null.
"""
import csv, os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from translit import code_spelling, display_spelling
from unicode_props import properties

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "standards/terminology/data/dabt_marks.tsv")
OUT = os.path.join(ROOT, "standards/terminology/concepts")

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
 "waqf-jaiz": ["الوَقْف الجَائِز", "مُسْتَوِي الطَّرَفَيْن"],
 "wasl-awla": ["الوَقْف الجَائِز", "الوَصْل أَوْلَى"],
 "waqf-awla": ["الوَقْف الجَائِز", "الوَقْف أَوْلَى"],
 "waqf-lazim": ["الوَقْف اللَّازِم"],
 "muanaqah": ["وَقْف المُعَانَقَة"], "waqf-mamnu": ["الوَقْف المَمْنُوع"],
 "saktah": ["عَلَامَة السَّكْتَة"], "seen-reading": ["سِين القِرَاءَة"],
 "imalah": ["الإمَالَة"], "ishmam": ["الإشْمَام"], "tashil": ["التَّسْهِيل"],
 "sajdah-sign": ["عَلَامَة السَّجْدَة"],
 "sajdah-line": ["خَطّ السَّجْدَة"],
 "hizb": ["عَلَامَة التَّقْسِيم"],
}

# Display forms that differ from the derived code, each with its evidence.
# Letter names take their spoken form: a letter's name *is* its pronunciation.
DISPLAY = {
    "nun": ("Noon", "GitHub phrase search: noon sakinah 478 vs nun sakinah 118"),
    "mim": ("Meem", "GitHub phrase search: meem sakinah 308 vs mim sakinah 57"),
    "sin": ("Seen", "letter name; unmeasurable directly, both forms are English words"),
}

# Registry ids that name a different concept in the dictionary. These are wrong
# names, not alternative spellings, so they are recorded as deprecated and kept
# out of the alias index: `hizb` is the division, `saktah` is the pause itself.
DEPRECATED_IDS = {"hizb", "saktah", "waqf_jaiz"}

# Names this repository itself published before the letter-name rule. They must
# keep resolving, so they are carried as aliases rather than dropped.
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
    "sajdah_mark": {"alamat_mawdi_al_sajdah"},
    "division_mark": {"alamat_al_tahzib"},
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
        "تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم "
        "بدل قراءة صورة الشكل.",
        "Used as a value of harakah, so that a letter's pronunciation is read from it in "
        "analysis, rendering and teaching rather than from the shape of the mark."),
    "tanwin": (
        "تستخدم قيمةً من قيم التنوين، ليقرأ منها نطق آخر الاسم وحكمه بدل قراءة صورة الشكل.",
        "Used as a value of tanwin, so that the pronunciation of the noun's ending and its "
        "ruling are read from it rather than from the shape of the mark."),
    "ijam": (
        "تستخدم قيمةً من قيم النقط، ليتميز بها الحرف عما يشاركه في الرسم في التحليل والبحث.",
        "Used as a value of ijam, so that a letter is told apart from those sharing its "
        "skeleton in analysis and in search."),
    "imlaiyyah": (
        "تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.",
        "Used as a value of the orthographic marks, so that where the rasm departs from the "
        "pronunciation of a word is known."),
    "waqf": (
        "تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في "
        "التطبيقات بدل قراءة صورة الرمز.",
        "Used as a value of the waqf mark type, so that rendering, instruction and warnings in "
        "applications branch on it rather than on the shape of the sign."),
    "alamat_qiraah": (
        "تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.",
        "Used as a value of the qiraah marks, so that the reader is alerted to a particular "
        "delivery at its place."),
    "dabt": (
        "تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.",
        "Used as a mark of the Mushaf, so that its place and what it points to are known in "
        "rendering and in analysis."),
    "mustaqill": (
        "تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.",
        "Used as a mark of the Mushaf, so that its place and what it points to are known in "
        "rendering and in analysis."),
}


def parse_codepoints(cell):
    return [f"U+{m}" for m in re.findall(r"U\+([0-9A-Fa-f]{4,6})", cell or "")]


def display_for(code, parts):
    words = " ".join(display_spelling(p) for p in parts).split()
    out, ev = [], []
    for w in words:
        key = w.lower().lstrip("al-")
        if key in DISPLAY:
            out.append(DISPLAY[key][0]); ev.append(DISPLAY[key][1])
        else:
            out.append(w)
    return " ".join(out), ("; ".join(dict.fromkeys(ev)) or None)


def build():
    rows = list(csv.reader(open(TSV), delimiter="\t"))
    entries = []
    for r in rows[1:]:
        old = r[1]
        if old not in NAMING_PHRASE:
            continue
        parts = NAMING_PHRASE[old]
        code = "_".join(code_spelling(p) for p in parts)
        disp, ev = display_for(code, parts)
        # The familiar form must resolve to the concept, so it becomes an alias.
        disp_alias = disp.lower().replace("-", "_").replace(" ", "_")
        intro = r[7].strip()
        absent = "لَمْ تُذْكَر" in intro or "لَمْ تُفْرَد" in intro or "لَمْ تَرِد" in intro
        family = FAMILY.get(r[3].strip(), r[3].strip())
        e = {
            "concept": code,
            "names": {
                "code": code,
                "display": disp,
                **({"display_evidence": ev} if ev else {}),
                "arabic": {"vocalized": parts[0] if len(parts) == 1 else " ".join(parts)},
                "dabt": r[5].strip(),
                "by_shape": r[6].strip() or None,
                "mushaf_introduction": None if absent else (intro or None),
            },
            "kind": FAMILY_KIND.get(family, "mark"),
            "category": "dabt",
            "parent": FAMILY_PARENT.get(family, "mushaf_mark"),
            "origin": "quranic",
            "tier": "core",
            "status": "draft",
            "symbol": r[8].strip() or None,
            # Column 10 defines the mark; column 15 is that same definition in
            # English, not a second fact about the mark.
            "definition": r[9].strip(),
            "definition_en": r[14].strip(),
            "purpose": PURPOSE[family][0],
            "purpose_en": PURPOSE[family][1],
            "alternative_spellings": sorted(
                ({old, old.replace("-", "_"), disp_alias}
                 | PREVIOUS_NAMES.get(code, set())
                 | REGISTRY_SHORTHAND.get(code, set()))
                - {code} - DEPRECATED_IDS
                - ({old, old.replace("-", "_")}
                   if old.replace("-", "_") in DEPRECATED_IDS else set())),
            **({"deprecated": [old, old.replace("-", "_")]}
               if old.replace("-", "_") in DEPRECATED_IDS else {}),
            "unicode": [],
            "mark_family": family,
            "sources": [{"id": "hafs_svg_registry", "ref": f"standard!{old}"}],
        }
        for cp in parse_codepoints(r[2]):
            p = properties(cp)
            e["unicode"].append({k: p[k] for k in ("cp", "name", "category", "combining_class", "block")})
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
