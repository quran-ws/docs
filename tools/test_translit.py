"""Golden cases for Canonical Code Spelling.

Every Arabic-origin term in the dictionary appears here. If the rules in
sections 4 to 8 change, this file is what says which spellings change with them.

    python3 tools/test_translit.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import code_spelling, display_spelling, check_vocalized

CASES = [
    # section 5 — ta marbutah becomes a final h
    ("سُورَة", "surah"), ("آيَة", "ayah"), ("رِوَايَة", "riwayah"),
    ("قِرَاءَة", "qiraah"), ("بَسْمَلَة", "basmalah"),
    ("سَكْتَة", "saktah"), ("خَتْمَة", "khatmah"), ("سَجْدَة", "sajdah"),
    ("كَلِمَة", "kalimah"), ("صَفْحَة", "safhah"), ("اِسْتِعَاذَة", "istiadhah"),
    # section 6 — long vowels are never doubled
    ("تَجْوِيد", "tajwid"), ("تَفْسِير", "tafsir"), ("طَرِيق", "tariq"),
    ("نُزُول", "nuzul"), ("تَرْتِيل", "tartil"), ("تَحْقِيق", "tahqiq"),
    ("تَدْوِير", "tadwir"), ("مِيزَان", "mizan"),
    # section 7 — hamza and ayn carry no letter, but keep their vowel
    ("إِعْرَاب", "irab"), ("رُكُوع", "ruku"), ("جُزْء", "juz"),
    # A word-final ayn or hamzah echoes the vowel before it, so the word does
    # not end short. After a vowel there is nothing to echo and it stays.
    ("رُبْع", "rubu"), ("جَمْع", "jama"), ("قَطْع", "qata"), ("الشَّفْع", "shafa"),
    ("الرَّفْع", "rafa"), ("البَدْء", "bada"), ("السَّبْع", "saba"),
    ("المَمْنُوع", "mamnu"), ("المُقَطَّع", "muqatta"), ("مَوَاضِع", "mawadi"),
    ("الدُّعَاء", "dua"), ("الإِمْلَاء", "imla"),
    ("مَقْطَع", "maqta"),
    # Medial ayn and hamzah are unaffected.
    ("مُعَلِّم", "muallim"), ("مُقْرِئ", "muqri"), ("عُثْمَانِيّ", "uthmani"),
    # shadda doubles the consonant, in either mark order
    ("مُجَوَّد", "mujawwad"), ("مُرَتَّل", "murattal"), ("مُفَصَّل", "mufassal"),
    # nisba endings reduce to a single i
    ("مَكِّيّ", "makki"), ("مَدَنِيّ", "madani"), ("مَثَانِي", "mathani"),
    # plain consonant clusters
    ("مُصْحَف", "mushaf"), ("حِزْب", "hizb"), ("ثُمْن", "thumn"),
    ("مَنْزِل", "manzil"), ("وَقْف", "waqf"), ("حَدْر", "hadr"),
    ("رَسْم", "rasm"), ("جَذْر", "jadhr"), ("حَذْف", "hadhf"),
    # letter names are written as they are said, not derived letter by letter
    # An ordinary Arabic word is translated and moves in front, per section 3.
    ("النُّون الصَّغِيرَة", "small_noon"),
    ("الصِّفْر المُسْتَدِير", "rounded_zero"), ("الثَّلَاث نُقَط", "three_dots"),
    ("النُّقْطَة", "dot"), ("النُّقْطَتَان", "two_dots"),
    ("المِيم الصَّغِيرَة", "small_meem"),
    ("سِين القِرَاءَة", "seen_al_qiraah"),
    ("اليَاء الصَّغِيرَة", "small_yaa"),
    ("الوَاو الصَّغِيرَة", "small_waw"),
    ("الأَلِف المَحْذُوفَة", "omitted_alif"),
    ("الجِيم", "jeem"),
    ("النُّون السَّاكِنَة", "noon_sakinah"),
    ("المِيم السَّاكِنَة", "meem_sakinah"),
    ("الصَّاد", "saad"),
    # but only letter NAMES: every other term still derives
    # the mark takes its name from what it marks, as waqf_mark and sajdah_mark do
    ("عَلَامَة الآيَة", "ayah_mark"),
    # a place, a science and a role, each derived by the same rules
    ("الحَرْف المُقَطَّع", "muqatta_letter"), ("المُتَشَابِهَات", "mutashabihat"),
    ("مَوْضِع السَّجْدَة", "sajdah_place"),
    ("المُفَسِّر", "mufassir"),
    # section 8 — the article is always al, never assimilated to a sun letter
    ("رُبْع الحِزْب", "rubu_al_hizb"),
        # the surah card and the ayah modal
        ("أَسْمَاء السُّورَة", "surah_names"),
    ("التَّفْسِير المَأْثُور", "tafsir_mathur"), ("النُّزُول", "nuzul"),
    # the three parts of speech
    ("القِسْم", "qism"), ("الفِعْل", "fil"),
    ("سُجُود التِّلَاوَة", "sujud_al_tilawah"),
    ("أَسْبَاب النُّزُول", "asbab_al_nuzul"),
    ("وَقْف المُعَانَقَة", "waqf_al_muanaqah"),
    # the word that decides whether a definite word is an adjective is the one
    # right before it: after an indefinite construct head the genitive keeps al
    ("الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن", "waqf_jaiz_mustawi_al_tarafayn"),
    ("مُسْتَوِي الطَّرَفَيْن", "mustawi_al_tarafayn"),
    # section 14 — a connective (connectives.tsv) carries nothing into the name
    ("الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى", "waqf_jaiz_wasl_awla"),
    ("الوَقْف الجَائِز مَعَ كَوْنِ الوَقْف أَوْلَى", "waqf_jaiz_waqf_awla"),
    ("عَلَامَة الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى", "waqf_jaiz_wasl_awla_mark"),
    # section 8 — a one-letter preposition is its own part; the noun keeps its
    # article, and لِ gives the article back the alif it swallowed
    ("التَّفْسِير بِالرَّأْي", "tafsir_bi_al_ray"),
    ("المَدّ العَارِض لِلسُّكُون", "madd_arid_li_al_sukun"),
    ("بَالِغ", "baligh"),
    # but a preposition on an indefinite noun cannot be told from the noun's
    # own first letter (بِنَاء), so it stays joined
    ("إِدْغَام النُّون بِغُنَّة", "idgham_al_noon_bighunnah"),
    # section 5 — a noun followed by its adjective is not a construct head, and
    # neither is a genitive: the ta marbutah stays h
    ("القَلْقَلَة الصُّغْرَى", "qalqalah_sughra"),
    ("مَدّ الصِّلَة الصُّغْرَى", "madd_al_silah_sughra"),
    ("لَام لَفْظ الجَلَالَة المُفَخَّمَة", "laam_lafz_al_jalalah_mufakhkhamah"),
    ("لَام", "laam"),
    # a `with_head` word is translated only beside a head word
    ("العَلَامَة الإِمْلَائِيَّة", "orthographic_mark"),
    ("الرَّسْم الإِمْلَائِيّ", "rasm_imlai"),
]

# Unvocalized input is refused, not guessed.
REFUSED = ["سورة", "استعاذة", "الوقف اللازم"]

DISPLAY_CASES = [
    ("رُبْع الحِزْب", "Rubu al-Hizb"),
    ("سُجُود التِّلَاوَة", "Sujud al-Tilawah"),
    ("أَسْبَاب النُّزُول", "Asbab al-Nuzul"),
    ("تَجْوِيد", "Tajwid"),
    ("التَّفْسِير بِالرَّأْي", "Tafsir bi al-Ray"),
]


def main():
    failures = []
    for arabic, expected in CASES:
        got = code_spelling(arabic)
        if got != expected:
            failures.append(f"  code_spelling({arabic!r}) = {got!r}, expected {expected!r}")
    for arabic, expected in DISPLAY_CASES:
        got = display_spelling(arabic)
        if got != expected:
            failures.append(f"  display_spelling({arabic!r}) = {got!r}, expected {expected!r}")

    for arabic in REFUSED:
        try:
            check_vocalized(arabic)
            failures.append(f"  check_vocalized({arabic!r}) accepted unvocalized input")
        except ValueError:
            pass

    total = len(CASES) + len(DISPLAY_CASES) + len(REFUSED)
    duplicates = {c for c in CASES if CASES.count(c) > 1}
    if duplicates:
        failures.append(f"  duplicate golden cases: {sorted(duplicates)}")
    if failures:
        print(f"FAILED {len(failures)} of {total}")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"ok — {total} cases")


if __name__ == "__main__":
    main()
