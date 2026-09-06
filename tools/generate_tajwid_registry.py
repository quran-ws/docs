"""Generate registries/tajwid_rules.tsv from the tajweed-engine rule corpus.

The dictionary defines what a `hukm_al_tajwid` is, and what `izhar`, `idgham`,
`madd` and the rest are. The 58 hukums of the engine are the members of that
set: each one is a name, a place in the taxonomy (topic, category, school) and
an attestation, which is what a registry holds and an entry does not (section 13).

    python3 tools/generate_tajwid_registry.py          # write the registry
    python3 tools/generate_tajwid_registry.py --check  # exit 1 if it is stale

Input:  standards/terminology/data/tajweed_engine_rules.json
Output: standards/terminology/registries/tajwid_rules.tsv

The corpus writes its labels without tashkeel, and sections 4-8 derive a code
from vocalized Arabic, so the vocalized form of every label is kept here, in
VOCALIZED, and the code is derived from it by tools/translit.py on every run.
The engine's own kebab id goes to `alternative_spellings`, so a dataset keyed
the engine's way resolves to the same member. A hukum the corpus adds and this
table does not know is an error, not a silent gap.

The output is deterministic: same input, same table, same bytes.
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import code_spelling, display_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "standards/terminology/data/tajweed_engine_rules.json")
OUT = os.path.join(ROOT, "standards/terminology/registries/tajwid_rules.tsv")

# The engine's label, vocalized, and the dictionary concept the hukum is a
# case of. Where two hukums carry the same label and differ only by school,
# the school is written into the name, because two members cannot share a
# code. Where a label is bare («الإظهار» under the mutamathilayn category), the
# category is written in, so the member does not shadow the concept.
VOCALIZED = {
    # التفخيم والترقيق
    "tafkheem-rank-1-jazari": ("مَرْتَبَة التَّفْخِيم الأُولَى عِنْدَ اِبْن الجَزَرِيّ", "tafkhim"),
    "tafkheem-rank-2-jazari": ("مَرْتَبَة التَّفْخِيم الثَّانِيَة عِنْدَ اِبْن الجَزَرِيّ", "tafkhim"),
    "tafkheem-rank-3-jazari": ("مَرْتَبَة التَّفْخِيم الثَّالِثَة عِنْدَ اِبْن الجَزَرِيّ", "tafkhim"),
    "tafkheem-rank-4-jazari": ("مَرْتَبَة التَّفْخِيم الرَّابِعَة عِنْدَ اِبْن الجَزَرِيّ", "tafkhim"),
    "tafkheem-rank-5-relative-jazari": ("مَرْتَبَة التَّفْخِيم النِّسْبِيّ الخَامِسَة عِنْدَ اِبْن الجَزَرِيّ", "tafkhim"),
    "tafkheem-rank-1-tahhan": ("مَرْتَبَة التَّفْخِيم الأُولَى عِنْدَ اِبْن الطَّحَّان", "tafkhim"),
    "tafkheem-rank-2-tahhan": ("مَرْتَبَة التَّفْخِيم الثَّانِيَة عِنْدَ اِبْن الطَّحَّان", "tafkhim"),
    "tafkheem-rank-3-relative-tahhan": ("مَرْتَبَة التَّفْخِيم النِّسْبِيّ الثَّالِثَة عِنْدَ اِبْن الطَّحَّان", "tafkhim"),
    "always-tarqeeq": ("الحُرُوف المُرَقَّقَة دَائِمًا", "tarqiq"),
    "ikhfa-ghunnah-tarqeeq": ("غُنَّة الإِخْفَاء الحَقِيقِيّ المُرَقَّقَة", "tarqiq"),
    "ikhfa-ghunnah-tafkheem": ("غُنَّة الإِخْفَاء الحَقِيقِيّ المُفَخَّمَة", "tafkhim"),
    "lam-jalalah-tafkheem": ("لَام لَفْظ الجَلَالَة المُفَخَّمَة", "tafkhim"),
    "lam-jalalah-tarqeeq": ("لَام لَفْظ الجَلَالَة المُرَقَّقَة", "tarqiq"),
    "raa-tafkheem": ("تَفْخِيم الرَّاء", "tafkhim"),
    "raa-tarqeeq": ("تَرْقِيق الرَّاء", "tarqiq"),
    "raa-either-permissible": ("جَوَاز الوَجْهَيْن فِي الرَّاء", "tafkhim,tarqiq"),
    "alef-tafkheem": ("الأَلِف المُفَخَّمَة", "tafkhim"),
    "alef-tarqeeq": ("الأَلِف المُرَقَّقَة", "tarqiq"),
    # علاقات الحروف
    "mutamathilain-idgham-kamil": ("إِدْغَام المُتَمَاثِلَيْن الكَامِل", "idgham,mutamathilan"),
    "mutamathilain-izhar": ("إِظْهَار المُتَمَاثِلَيْن", "izhar,mutamathilan"),
    "mutajanisain-idgham-naqis": ("إِدْغَام المُتَجَانِسَيْن النَّاقِص", "idgham,mutajanisan"),
    "mutajanisain-ikhfa-shafawi": ("الإِخْفَاء الشَّفَوِيّ فِي المُتَجَانِسَيْن", "ikhfa,mutajanisan"),
    # النون والتنوين
    "izhar-halqi-noon": ("إِظْهَار النُّون الحَلْقِيّ", "izhar"),
    "izhar-halqi-tanween": ("إِظْهَار التَّنْوِين الحَلْقِيّ", "izhar"),
    "idgham-bi-ghunnah-noon": ("إِدْغَام النُّون بِغُنَّة", "idgham"),
    "idgham-bi-ghunnah-tanween": ("إِدْغَام التَّنْوِين بِغُنَّة", "idgham"),
    "idgham-bila-ghunnah-noon": ("إِدْغَام النُّون بِغَيْر غُنَّة", "idgham"),
    "idgham-bila-ghunnah-tanween": ("إِدْغَام التَّنْوِين بِغَيْر غُنَّة", "idgham"),
    "idgham-kamil-noon": ("إِدْغَام النُّون الكَامِل", "idgham"),
    "idgham-kamil-tanween": ("إِدْغَام التَّنْوِين الكَامِل", "idgham"),
    "idgham-naqis-noon": ("إِدْغَام النُّون النَّاقِص", "idgham"),
    "idgham-naqis-tanween": ("إِدْغَام التَّنْوِين النَّاقِص", "idgham"),
    "iqlab-noon": ("قَلْب النُّون السَّاكِنَة", "iqlab"),
    "iqlab-tanween": ("قَلْب التَّنْوِين", "iqlab"),
    "ikhfa-haqiqi-noon": ("الإِخْفَاء الحَقِيقِيّ لِلنُّون", "ikhfa"),
    "ikhfa-haqiqi-tanween": ("الإِخْفَاء الحَقِيقِيّ لِلتَّنْوِين", "ikhfa"),
    "izhar-mutlaq": ("الإِظْهَار المُطْلَق", "izhar"),
    # الميم الساكنة
    "idgham-shafawi-meem": ("إِدْغَام المِيم السَّاكِنَة", "idgham,meem_sakinah"),
    "ikhfa-shafawi-meem": ("إِخْفَاء المِيم السَّاكِنَة", "ikhfa,meem_sakinah"),
    "izhar-shafawi-meem": ("إِظْهَار المِيم السَّاكِنَة", "izhar,meem_sakinah"),
    # المشددتان
    "noon-mushaddadah": ("النُّون المُشَدَّدَة", "ghunnah"),
    "meem-mushaddadah": ("المِيم المُشَدَّدَة", "ghunnah"),
    # المد
    "madd-tabee-kalimi": ("المَدّ الطَّبِيعِيّ الكَلِمِيّ", "madd_tabii"),
    "leen-waw": ("الوَاو اللَّيِّنَة", "madd_al_lin"),
    "leen-yaa": ("اليَاء اللَّيِّنَة", "madd_al_lin"),
    "madd-iwad": ("مَدّ العِوَض عَن التَّنْوِين", "madd_al_iwad"),
    "madd-silah-sughra": ("مَدّ الصِّلَة الصُّغْرَى", "madd_al_silah"),
    "seven-alefs": ("الأَلِفَات السَّبْع", "madd_tabii"),
    "seven-alefs-khulf": ("الأَلِفَات السَّبْع بِخُلْف", "madd_tabii"),
    "madd-badal": ("مَدّ البَدَل وَشِبْه البَدَل", "madd_al_badal"),
    "madd-muttasil": ("المَدّ الوَاجِب المُتَّصِل", "madd_muttasil"),
    "madd-munfasil": ("المَدّ الجَائِز المُنْفَصِل", "madd_munfasil"),
    "madd-lazim-kalimi-muthaqqal": ("المَدّ اللَّازِم الكَلِمِيّ المُثَقَّل", "madd_lazim"),
    "madd-lazim-kalimi-mukhaffaf": ("المَدّ اللَّازِم الكَلِمِيّ المُخَفَّف", "madd_lazim"),
    "madd-lazim-harfi": ("المَدّ اللَّازِم الحَرْفِيّ", "madd_lazim"),
    # القلقلة
    "qalqalah-sughra": ("القَلْقَلَة الصُّغْرَى", "qalqalah"),
    "qalqalah-mutatarrifa": ("القَلْقَلَة المُتَطَرِّفَة", "qalqalah"),
    "qalqalah-kubra": ("القَلْقَلَة الكُبْرَى", "qalqalah"),
}

# The engine names a school on the ranks of tafkhim only; every other hukum is
# the common doctrine of the riwayah the corpus covers.
SCHOOL_CODE = {"ibn-al-jazari": "ibn_al_jazari", "ibn-al-tahhan": "ibn_al_tahhan"}

HEADER = ["code", "arabic", "display", "concept", "topic", "category", "school",
          "alternative_spellings", "ref"]

HEAD_NOTE = """\
# The rulings of tajwid — أحكام التجويد — as the tajweed-engine corpus enumerates them.
#
# GENERATED by tools/generate_tajwid_registry.py from
# standards/terminology/data/tajweed_engine_rules.json (version {version},
# riwayah {riwayah}). Do not edit by hand: change the corpus, or the vocalized
# labels in the generator, and run it again.
#
# WHY THIS IS A REGISTRY
# `hukm_al_tajwid` is the concept and has its dictionary entry, as do the
# families a ruling belongs to: izhar, idgham, iqlab, ikhfa, the kinds of madd,
# qalqalah, tafkhim and tarqiq. A hukum is a member of that set: what is true of
# it is its name, its place in the corpus (topic, category, school) and the
# rules the engine attaches to it, which is a row and not an entry (section 13).
#
# THE CODES ARE DERIVED
# The corpus writes its labels without tashkeel. The generator keeps a vocalized
# form of every label and derives the code from it by tools/translit.py, so the
# registry obeys sections 4 to 8 like every other name in the standard. Two
# consequences: where the engine gives two rulings the same label and a
# different school (the ranks of tafkhim), the school is part of the name; and
# where a label is bare («الإظهار» under the mutamathilayn), the category is
# written in so the member does not shadow the concept.
#
# `concept` names the dictionary entry or entries the hukum is a case of.
# `topic`, `category` and `school` are the engine's own ids, kept as they are so
# a reader can find the hukum in the corpus. `alternative_spellings` carries the
# engine's kebab id, so a dataset keyed its way resolves to the same member.
#
# `ref` cites the corpus by hukum id, as sources.yml asks.
#
# {header}
"""


def rows(corpus):
    unknown = [h["id"] for h in corpus["hukums"] if h["id"] not in VOCALIZED]
    if unknown:
        raise SystemExit("hukums with no vocalized label in VOCALIZED: " + ", ".join(unknown))
    stale = sorted(set(VOCALIZED) - {h["id"] for h in corpus["hukums"]})
    if stale:
        raise SystemExit("VOCALIZED names hukums the corpus no longer has: " + ", ".join(stale))
    cat = {c["id"]: c for c in corpus["categories"]}
    out = []
    for h in corpus["hukums"]:
        arabic, concept = VOCALIZED[h["id"]]
        code = code_spelling(arabic)
        school = (h.get("school") or {}).get("id", "")
        out.append([
            code, arabic, display_spelling(arabic), concept,
            cat[h["category"]]["topic"], h["category"],
            SCHOOL_CODE.get(school, school),
            ",".join(sorted({h["id"], h["id"].replace("-", "_")} - {code})),
            f"tajweed_engine {h['id']}",
        ])
    codes = [r[0] for r in out]
    dup = sorted({c for c in codes if codes.count(c) > 1})
    if dup:
        raise SystemExit("derived codes collide: " + ", ".join(dup))
    return out


def render(corpus):
    head = HEAD_NOTE.format(version=corpus.get("version", "?"),
                            riwayah=corpus.get("riwayah", "?"),
                            header="\t".join(HEADER))
    body = "".join("\t".join(r) + "\n" for r in rows(corpus))
    return head + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if the registry is stale")
    args = ap.parse_args()
    corpus = json.load(open(CORPUS, encoding="utf-8"))
    text = render(corpus)
    current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    if args.check:
        if current != text:
            print(f"{os.path.relpath(OUT, ROOT)} is stale — run tools/generate_tajwid_registry.py")
            return 1
        print(f"ok — {os.path.relpath(OUT, ROOT)} is current ({len(corpus['hukums'])} hukums)")
        return 0
    if current == text:
        print(f"unchanged — {os.path.relpath(OUT, ROOT)} ({len(corpus['hukums'])} hukums)")
        return 0
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)} ({len(corpus['hukums'])} hukums)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
