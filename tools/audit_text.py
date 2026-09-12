"""Recompute the figures the text page cites, from any Uthmani text file.

The page content/{ar,en}/quranic-text.md quotes counts from an audit of a
published text: how many ayahs NFC changes, bytes and codepoints, the
character allowlist, how many ayahs carry edition marks, the BOM, the
whitespace-token count. Numbers remembered in prose go stale; this recomputes
every one of them, so the page can cite a file, a hash and this command.

    python3 tools/audit_text.py quran-uthmani.txt
    python3 tools/audit_text.py quran-uthmani.txt --format tanzil --json
    python3 tools/audit_text.py quran-uthmani.txt --allowlist allowlist.txt

Formats:
  lines    one ayah per line (default)
  tanzil   `surah|ayah|text` per line, Tanzil's download format; comment lines
           starting with # are skipped
  json     a JSON array of objects with a `text` field, or of strings

The file is read as bytes and decoded as UTF-8 strictly; a BOM is reported,
never stripped.
"""
import argparse, collections, hashlib, json, os, sys, unicodedata

EDITION_MARKS = {"۝": "end of ayah ۝", "۞": "rub al-hizb ۞", "۩": "sajdah ۩"}
BOM = "﻿"


def read_ayahs(path, fmt):
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")           # strict: a bad byte is a finding, not a fix
    if fmt == "json":
        data = json.loads(text)
        items = [d["text"] if isinstance(d, dict) else d for d in data]
        return raw, [(i + 1, None, t) for i, t in enumerate(items)]
    ayahs = []
    for n, line in enumerate(text.split("\n"), 1):
        if not line:
            continue
        if fmt == "tanzil":
            if line.lstrip(BOM).startswith("#"):
                continue
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            ayahs.append((n, f"{parts[0].lstrip(BOM)}:{parts[1]}", parts[2]))
        else:
            ayahs.append((n, None, line))
    return raw, ayahs


def audit(raw, ayahs):
    texts = [t for _, _, t in ayahs]
    joined = "\n".join(texts)
    chars = collections.Counter(joined)
    chars.pop("\n", None)

    nfc_changed = [ref or n for n, ref, t in ayahs if unicodedata.normalize("NFC", t) != t]
    nfkc_changed = [ref or n for n, ref, t in ayahs if unicodedata.normalize("NFKC", t) != t]
    # The two ways NFC changes an Uthmani text: reordering marks, and composing.
    reorders = composes = 0
    for t in texts:
        nfc = unicodedata.normalize("NFC", t)
        if nfc == t:
            continue
        if len(nfc) == len(t):
            reorders += 1        # same characters, different order of marks
        else:
            composes += 1        # a base letter and a mark became one character

    bom_ayahs = [ref or n for n, ref, t in ayahs if BOM in t]
    marks = {}
    for cp, label in EDITION_MARKS.items():
        starts = sum(1 for t in texts if t.startswith(cp) or t.lstrip(BOM).startswith(cp))
        anywhere = sum(1 for t in texts if cp in t)
        marks[f"U+{ord(cp):04X}"] = {"mark": label, "ayahs_starting_with": starts,
                                     "ayahs_containing": anywhere, "occurrences": chars.get(cp, 0)}

    tokens = sum(len(t.split()) for t in texts)
    mark_tokens = sum(1 for t in texts for tok in t.split() if tok in EDITION_MARKS)

    return {
        "file_sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "codepoints": len(joined) - (len(texts) - 1),
        "ayahs": len(texts),
        "distinct_characters": len(chars),
        "allowlist": sorted(chars),
        "nfc_changes_ayahs": len(nfc_changed),
        "nfc_reorders_marks_only_in_ayahs": reorders,
        "nfc_composes_in_ayahs": composes,
        "nfkc_changes_ayahs": len(nfkc_changed),
        "bom_in_file": raw.startswith(BOM.encode("utf-8")),
        "bom_in_ayahs": bom_ayahs[:10],
        "edition_marks": marks,
        "whitespace_tokens": tokens,
        "whitespace_tokens_that_are_marks": mark_tokens,
    }


def describe(char):
    try:
        name = unicodedata.name(char)
    except ValueError:
        name = "<unnamed>"
    return f"U+{ord(char):04X} {name}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--format", choices=["lines", "tanzil", "json"], default="lines")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--allowlist", metavar="OUT", help="write the character allowlist, one codepoint per line")
    args = ap.parse_args()

    raw, ayahs = read_ayahs(args.file, args.format)
    result = audit(raw, ayahs)

    if args.allowlist:
        with open(args.allowlist, "w", encoding="utf-8") as out:
            for c in result["allowlist"]:
                out.write(f"{describe(c)}\n")

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"{os.path.basename(args.file)}  sha256 {result['file_sha256']}")
    print(f"  {result['ayahs']:,} ayahs, {result['bytes']:,} bytes, {result['codepoints']:,} codepoints, "
          f"{result['distinct_characters']} distinct characters")
    print(f"  NFC changes {result['nfc_changes_ayahs']:,} ayahs "
          f"(reorders marks only in {result['nfc_reorders_marks_only_in_ayahs']:,}, composes in "
          f"{result['nfc_composes_in_ayahs']:,}); NFKC changes {result['nfkc_changes_ayahs']:,}")
    print(f"  BOM: {'at the start of the file' if result['bom_in_file'] else 'not at the start of the file'}"
          + (f"; inside {len(result['bom_in_ayahs'])} ayah(s): {result['bom_in_ayahs']}" if result['bom_in_ayahs'] else ""))
    for cp, m in result["edition_marks"].items():
        print(f"  {cp} {m['mark']}: {m['ayahs_starting_with']:,} ayahs start with it, "
              f"{m['ayahs_containing']:,} contain it, {m['occurrences']:,} occurrences")
    print(f"  whitespace tokens: {result['whitespace_tokens']:,}, of which "
          f"{result['whitespace_tokens_that_are_marks']:,} are edition marks")
    print("  allowlist:")
    for c in result["allowlist"]:
        print(f"    {describe(c)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
