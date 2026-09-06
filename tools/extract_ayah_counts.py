"""Read the per-surah ayah counts of the six schools out of al-Bayan.

al-Dani gives every surah a section that states its count once — a base number,
then only the part that differs for the schools that differ:

    "two hundred and eighty-five in the two Madinans, the Makkan and the
     Damascene, and six in the Kufan, and seven in the Basran"

So the numbers cannot be read one at a time; the parts of the base have to
survive parsing, and a later part replaces the trailing part it covers. That is
what numparse-style component arithmetic below is for.

    python3 tools/extract_ayah_counts.py            # rebuild the registry
    python3 tools/extract_ayah_counts.py --check    # verify, write nothing

The only real proof this reads the book correctly is that it reconciles: the
114 Kufi counts must match the printed mushaf surah by surah, and each school's
column must sum to the total al-Dani states for that school, or differ from it
by exactly the residual TOLERATED records and the registry's header explains.
Both are checked on every run and printed; any other difference fails.

`--check` reads the committed registry and needs no copy of the book, so a
fresh clone checks offline. Rebuilding the registry fetches the book once and
caches it under tools/turath_cache/.
"""
import json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "tools/turath_cache/5542.json")
OUT = os.path.join(ROOT, "standards/terminology/registries/ayah_counts.tsv")
BOOK_URL = "https://files.turath.io/books-v3/5542.json"

SCHOOLS = ["madani_awwal", "madani_akhir", "makki", "kufi", "basri", "dimashqi"]

# The residual each column is allowed against al-Dani's stated total: one ayah
# in four schools, from the two sections (al-Saffat, al-Takwir) where he counts
# for Abu Jafar apart — see the registry header. Anything else is a regression.
TOLERATED = {"madani_awwal": 1, "madani_akhir": 1, "makki": 1, "dimashqi": 1}

# The totals al-Dani states for each school, with the page each is stated on.
ATTESTED = {"madani_awwal": (6217, "1/79"), "madani_akhir": (6214, "1/79"),
            "makki": (6219, "1/79"), "kufi": (6236, "1/80"),
            "basri": (6204, "1/80"), "dimashqi": (6226, "1/82")}

# The printed mushaf's counts, which are the Kufi school. Used only to check the
# reading of the book, never as its source.
MUSHAF_KUFI = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,
 98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,
 59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,
 28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,
 8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]

UNITS = {'واحده':1,'واحد':1,'احدي':1,'اثنتان':2,'اثنتا':2,'ثنتان':2,'ثنتا':2,'اثنان':2,
 'اثنتين':2,'ايتان':2,'ايتين':2,'ثلاث':3,'اربع':4,'خمس':5,'ست':6,'سبع':7,'ثمان':8,
 'ثماني':8,'تسع':9}
TENS = {'عشرون':20,'عشرين':20,'ثلاثون':30,'ثلاثين':30,'اربعون':40,'اربعين':40,'خمسون':50,
 'خمسين':50,'ستون':60,'ستين':60,'سبعون':70,'سبعين':70,'ثمانون':80,'ثمانين':80,'تسعون':90,
 'تسعين':90}
HUND = {'مئه':100,'مائه':100,'مئتا':200,'مئتان':200,'مائتا':200,'مائتان':200,'مئتي':200,
 'مائتي':200,'ثلاثمئه':300,'ثلاثمائه':300,'اربعمئه':400,'اربعمائه':400,'خمسمئه':500,
 'خمسمائه':500,'ستمئه':600,'ستمائه':600,'سبعمئه':700,'سبعمائه':700,'ثمانمئه':800,
 'ثمانمائه':800,'تسعمئه':900,'تسعمائه':900}

LABELS = [
 (r'المدني[_\s]الاول', ["madani_awwal"]), (r'المدني[_\s]الاخير', ["madani_akhir"]),
 (r'المدنيين', ["madani_awwal","madani_akhir"]), (r'المدنيان', ["madani_awwal","madani_akhir"]),
 (r'مدنيان', ["madani_awwal","madani_akhir"]), (r'مدنيين', ["madani_awwal","madani_akhir"]),
 (r'الكوفي', ["kufi"]), (r'كوفي', ["kufi"]),
 (r'البصري', ["basri"]), (r'بصري', ["basri"]),
 (r'الشامي', ["dimashqi"]), (r'شامي', ["dimashqi"]),
 (r'المكي', ["makki"]), (r'مكي', ["makki"]),
]
REST = r'الباقين|الباقون|باقي'
ALLSIX = r'جميع العدد|الجميع|جميع العدود|ليس فيها اختلاف|بلا اختلاف|لا اختلاف فيها'
LABEL_RE = re.compile('|'.join(p for p, _ in LABELS) + '|' + REST)


def norm(s):
    s = re.sub(r'[ً-ِّْٰۖ-ۜـ]', '', s)
    return (s.replace('أ','ا').replace('إ','ا').replace('آ','ا')
             .replace('ى','ي').replace('ة','ه'))


def components(words):
    """A number as its spoken parts: 285 -> [(100,200),(10,80),(1,5)]."""
    out, i = [], 0
    while i < len(words):
        raw = words[i]; w = raw.lstrip('و')
        nxt = words[i+1].lstrip('و') if i+1 < len(words) else ''
        if w in HUND: out.append((100, HUND[w])); i += 1; continue
        if w in TENS: out.append((10, TENS[w])); i += 1; continue
        if w in UNITS:
            if nxt in ('عشره','عشر'): out.append((10, 10+UNITS[w])); i += 2; continue
            out.append((1, UNITS[w])); i += 1; continue
        if w in ('عشره','عشر'): out.append((10, 10)); i += 1; continue
        # `wa-ayah` conjoined is the numeral one: "fifty and an ayah" is 51.
        # Bare `ayah` after a number is the counted noun: "two hundred ayahs".
        if w == 'ايه' and raw.startswith('و'): out.append((1, 1)); i += 1; continue
        i += 1
    return out


def replace(base, repl):
    """Apply a partial count to the base, part by part from the right."""
    if not repl: return sum(v for _, v in base)
    mag = max(m for m, _ in repl)
    if any(m == mag for m, _ in base):
        kept = [(m, v) for m, v in base if m > mag]
    else:
        low = min(m for m, _ in base)
        low_val = [v for m, v in base if m == low][0]
        # A round ten from twenty upward takes a unit beside it: 180 and "two"
        # is 182. A bare ten, or a teen, is replaced instead: 110 and "nine" is
        # 109, because ten and nine fill the same slot.
        kept = list(base) if (mag == 1 and low == 10 and low_val >= 20) \
               else [(m, v) for m, v in base if m > low]
    return sum(v for _, v in kept) + sum(v for _, v in repl)


def strip_labels(seg):
    for pat, _ in LABELS: seg = re.sub(pat, ' ', seg)
    return re.sub(REST, ' ', seg)


def read_counts(span):
    for m in re.finditer(r'وهي\s+([^.\n]{1,300})', span):
        sent = re.split(r'اختلافها|وفيها مما|ورؤوس الاي|وكلمها', m.group(1))[0].strip()
        if not re.search('|'.join(p for p, _ in LABELS) + '|' + ALLSIX, sent):
            continue
        if re.search(ALLSIX, sent) and not re.search('|'.join(p for p, _ in LABELS), sent):
            n = sum(v for _, v in components(re.split(ALLSIX, sent)[0].split()))
            if n: return {s: n for s in SCHOOLS}, sent
            continue
        joined = re.sub(r'(المدني)\s+(الاول|الاخير)', r'\1_\2', sent)
        clauses, num, labels = [], [], []
        for tok in re.split(r'\s+', joined):
            if not tok: continue
            if LABEL_RE.search(tok):
                labels.append(tok)
            elif labels and not components([tok]):
                continue          # an aside inside a run of school names
            else:
                if labels: clauses.append((num, labels)); num, labels = [], []
                num.append(tok)
        if labels: clauses.append((num, labels))

        out, base = {}, None
        for num_words, label_words in clauses:
            words = strip_labels(' '.join(num_words)).split()
            if base is None:
                base = components(words)
                if not base: break
                value = sum(v for _, v in base)
            else:
                value = replace(base, components(words))
            named = []
            for lw in label_words:
                for pat, sch in LABELS:
                    if re.search(pat, lw): named += sch; break
                else:
                    if re.search(REST, lw):
                        named += [x for x in SCHOOLS if x not in out]
            for x in named: out.setdefault(x, value)
        if len(out) == 6: return out, sent
    return None, None


def book():
    if not os.path.exists(CACHE):
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        req = urllib.request.Request(BOOK_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as r, open(CACHE, "wb") as f:
            f.write(r.read())
    d = json.load(open(CACHE, encoding="utf-8"))
    meta_keys = [k for k in d if k != "pages"]
    idx = d[meta_keys[1]]
    heads = next(v for v in idx.values()
                 if isinstance(v, list) and v and isinstance(v[0], dict))
    return heads, d["pages"]


def extract():
    heads, pages = book()
    surahs = [x for x in heads if x["title"].startswith("سورة")]
    res, failed = {}, []
    for n, x in enumerate(surahs, 1):
        start = x["page"] - 1
        end = surahs[n]["page"] if n < len(surahs) else len(pages)
        span = "\n".join(norm(p["text"]) for p in pages[start:end])
        i = span.find(norm(x["title"]))
        if i >= 0: span = span[i + len(norm(x["title"])):]
        got, _ = read_counts(span)
        if got: res[n] = got
        else: failed.append(n)
    return res, failed


def report(res, failed):
    ok = True
    print(f"read {len(res)} of 114 surah sections" + (f"; unparsed {failed}" if failed else ""))
    mism = [n for n in res if res[n]["kufi"] != MUSHAF_KUFI[n-1]]
    print(f"  Kufi against the printed mushaf, surah by surah: "
          f"{'all 114 agree' if not mism else f'{len(mism)} disagree: {mism}'}")
    ok &= not mism and not failed
    for s in SCHOOLS:
        total = sum(v[s] for v in res.values())
        want, page = ATTESTED[s]
        residual = total - want
        if residual == 0:
            flag = "matches"
        elif residual == TOLERATED.get(s, 0):
            flag = f"{residual:+d} against, the residual the header explains, for"
        else:
            flag = f"{residual:+d} against — NOT the tolerated residual — for"
            ok = False
        print(f"  {s:14} {total:5}  {flag} al-Dani's stated {want} ({page})")
    return ok


def committed():
    """The registry as committed, in the shape extract() returns."""
    res = {}
    for line in open(OUT, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        cells = line.rstrip("\n").split("\t")
        res[int(cells[0])] = {s: int(cells[i + 1]) for i, s in enumerate(SCHOOLS)}
    return res, [n for n in range(1, 115) if n not in res]


HEADER = '''# Per-surah ayah counts in the six schools of numbering.
#
# Generated by tools/extract_ayah_counts.py from al-Bayan fi Add Ay al-Quran by
# al-Dani, which gives every surah a section stating its count in each school.
# Do not edit by hand: rerun the tool.
#
# HOW FAR THIS IS VERIFIED — the numbers are only worth what the check is.
#   * All 114 Kufi counts match the printed mushaf surah by surah. The mushaf
#     prints the Kufi count, so this tests the reading of every section, not
#     just the arithmetic.
#   * Kufi sums to 6236 and Basri to 6204, the totals al-Dani states.
#   * The other four columns come to one more than the total he states. The
#     residual is disclosed rather than smoothed away, and the run prints it.
#     Two places in the book are the likely cause and neither is a parsing
#     failure: at al-Saffat and al-Takwir al-Dani gives a count for the reading
#     of Abu Jafar specifically, and whether "the count of Abu Jafar" is the
#     Madani Awwal school or an authority beside it is a real question about
#     the source, not something a tool should decide. Those two rows carry the
#     six schools as stated and leave Abu Jafar out of them.
#
# A number here is a count, not a boundary. Where two schools give a surah the
# same total they may still divide it differently, and that difference lives in
# the disputed boundaries, which this file does not carry.
#
# `ref` cites al-Bayan by volume/page for the school totals this reconciles to.
#
# surah\tmadani_awwal\tmadani_akhir\tmakki\tkufi\tbasri\tdimashqi\tref'''


def main():
    if "--check" in sys.argv:
        print("checking the committed registry")
        return 0 if report(*committed()) else 1
    res, failed = extract()
    ok = report(res, failed)
    if not ok:
        print("\nrefusing to write: the reading does not reconcile")
        return 1
    if failed:
        print("\nrefusing to write: some sections were not read")
        return 1
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HEADER + "\n")
        for n in sorted(res):
            row = [str(n)] + [str(res[n][s]) for s in SCHOOLS] + ["bayan_dani 1/79"]
            f.write("\t".join(row) + "\n")
    print(f"\nwrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
