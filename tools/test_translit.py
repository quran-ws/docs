"""Golden cases for Canonical Code Spelling.

Every Arabic-origin term in the dictionary appears here. If the rules in
sections 4 to 8 change, this file is what says which spellings change with them.

    python3 tools/test_translit.py
"""
from translit import code_spelling, display_spelling

CASES = [
    # section 5 — ta marbutah becomes a final h
    ("سُورَة", "surah"), ("آيَة", "ayah"), ("رِوَايَة", "riwayah"),
    ("قِرَاءَة", "qiraah"), ("بَسْمَلَة", "basmalah"), ("فَاصِلَة", "fasilah"),
    ("سَكْتَة", "saktah"), ("خَتْمَة", "khatmah"), ("سَجْدَة", "sajdah"),
    ("كَلِمَة", "kalimah"), ("صَفْحَة", "safhah"), ("اِسْتِعَاذَة", "istiadhah"),
    # section 6 — long vowels are never doubled
    ("تَجْوِيد", "tajwid"), ("تَفْسِير", "tafsir"), ("طَرِيق", "tariq"),
    ("نُزُول", "nuzul"), ("تَرْتِيل", "tartil"), ("تَحْقِيق", "tahqiq"),
    ("تَدْوِير", "tadwir"), ("مِيزَان", "mizan"),
    # section 7 — hamza and ayn carry no letter, but keep their vowel
    ("إِعْرَاب", "irab"), ("رُكُوع", "ruku"), ("جُزْء", "juz"),
    ("مُقْرِئ", "muqri"), ("مُعَلِّم", "muallim"), ("عُثْمَانِيّ", "uthmani"),
    # shadda doubles the consonant, in either mark order
    ("مُجَوَّد", "mujawwad"), ("مُرَتَّل", "murattal"), ("مُفَصَّل", "mufassal"),
    # nisba endings reduce to a single i
    ("مَكِّيّ", "makki"), ("مَدَنِيّ", "madani"), ("مَثَانِي", "mathani"),
    # plain consonant clusters
    ("مُصْحَف", "mushaf"), ("حِزْب", "hizb"), ("ثُمْن", "thumn"),
    ("مَنْزِل", "manzil"), ("وَقْف", "waqf"), ("حَدْر", "hadr"),
    ("رَسْم", "rasm"), ("جَذْر", "jadhr"), ("حَرْف", "harf"),
    # letter names are written as they are said, not derived letter by letter
    ("النُّون الصَّغِيرَة", "noon_saghirah"),
    ("المِيم الصَّغِيرَة", "meem_saghirah"),
    ("سِين القِرَاءَة", "seen_al_qiraah"),
    ("اليَاء الصَّغِيرَة", "yaa_saghirah"),
    ("الوَاو الصَّغِيرَة", "waw_saghirah"),
    ("الأَلِف المَحْذُوفَة", "alif_mahdhufah"),
    ("الجِيم", "jeem"),
    ("الصَّاد", "saad"),
    # but only letter NAMES: every other term still derives
    ("تَجْوِيد", "tajwid"),
    ("مَكِّيّ", "makki"),
    ("الحَرْف المُقَطَّع", "harf_muqatta"),
    # section 8 — the article is always al, never assimilated to a sun letter
    ("رُبْع الحِزْب", "rub_al_hizb"),
    ("سُجُود التِّلَاوَة", "sujud_al_tilawah"),
    ("أَسْبَاب النُّزُول", "asbab_al_nuzul"),
    ("وَقْف المُعَانَقَة", "waqf_al_muanaqah"),
]

DISPLAY_CASES = [
    ("رُبْع الحِزْب", "Rub al-Hizb"),
    ("سُجُود التِّلَاوَة", "Sujud al-Tilawah"),
    ("أَسْبَاب النُّزُول", "Asbab al-Nuzul"),
    ("تَجْوِيد", "Tajwid"),
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

    total = len(CASES) + len(DISPLAY_CASES)
    if failures:
        print(f"FAILED {len(failures)} of {total}")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"ok — {total} cases")


if __name__ == "__main__":
    main()
