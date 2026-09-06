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
 "fathatan": ["تَنْوِين النَّصْب"], "kasratan": ["تَنْوِين الخَفْض"],
 "dammatan": ["تَنْوِين الرَّفْع"],
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
 "muanaqah": ["تَعَانُق الوَقْف"], "waqf-mamnu": ["الوَقْف المَمْنُوع"],
 "saktah": ["عَلَامَة السَّكْت"], "seen-reading": ["سِين القِرَاءَة"],
 "imalah": ["الإمَالَة"], "ishmam": ["الإشْمَام"], "tashil": ["التَّسْهِيل"],
 "sajdah-sign": ["عَلَامَة مَوْضِع السَّجْدَة"],
 "sajdah-line": ["خَطّ مُوجِب السَّجْدَة"],
 "hizb": ["عَلَامَة التَّحْزِيب"],
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
}

FAMILY = {"حركة": "harakah", "تنوين": "tanwin", "نقط": "ijam", "إملائية": "imlaiyyah",
          "ضبط": "dabt", "وقف": "waqf", "علامة قراءة": "alamat_qiraah", "مستقل": "mustaqill"}


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
            "kind": "mark",
            "category": "dabt",
            "parent": "mushaf_mark",
            "origin": "quranic",
            "tier": "core",
            "status": "draft",
            "symbol": r[8].strip() or None,
            "definition": r[9].strip(),
            "purpose": r[14].strip(),
            "alternative_spellings": sorted(
                ({old, old.replace("-", "_"), disp_alias}
                 | PREVIOUS_NAMES.get(code, set()))
                - {code} - DEPRECATED_IDS
                - ({old, old.replace("-", "_")}
                   if old.replace("-", "_") in DEPRECATED_IDS else set())),
            **({"deprecated": [old, old.replace("-", "_")]}
               if old.replace("-", "_") in DEPRECATED_IDS else {}),
            "unicode": [],
            "mark_family": FAMILY.get(r[3].strip(), r[3].strip()),
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
