"""Unicode properties for a mark, read from the Unicode database.

Entries never hand-record what Unicode already defines: the properties are
generated, so they cannot drift from the standard they claim to describe.

    python3 tools/unicode_props.py U+06D8 U+06DC
"""
import sys
import unicodedata

# Blocks these marks fall in, with the official code chart for each.
BLOCKS = [
    (0x0600, 0x06FF, "Arabic", "https://unicode.org/charts/PDF/U0600.pdf"),
    (0x0750, 0x077F, "Arabic Supplement", "https://unicode.org/charts/PDF/U0750.pdf"),
    (0x08A0, 0x08FF, "Arabic Extended-A", "https://unicode.org/charts/PDF/U08A0.pdf"),
    (0xFB50, 0xFDFF, "Arabic Presentation Forms-A", "https://unicode.org/charts/PDF/UFB50.pdf"),
    (0xFE70, 0xFEFF, "Arabic Presentation Forms-B", "https://unicode.org/charts/PDF/UFE70.pdf"),
]

CATEGORY_NOTE = {
    "Mn": "nonspacing mark",
    "Lo": "letter — occupies its own position in the string",
    "Lm": "modifier letter — a letter, not a combining mark",
    "So": "symbol — standalone, not attached to a base letter",
}


def block_of(cp):
    for lo, hi, name, chart in BLOCKS:
        if lo <= cp <= hi:
            return name, chart
    return None, None


def properties(codepoint):
    """codepoint as an int or a "U+06D8" string."""
    cp = codepoint if isinstance(codepoint, int) else int(str(codepoint).replace("U+", ""), 16)
    ch = chr(cp)
    block, chart = block_of(cp)
    category = unicodedata.category(ch)
    return {
        "cp": f"U+{cp:04X}",
        "name": unicodedata.name(ch, None),
        "category": category,
        "category_note": CATEGORY_NOTE.get(category, ""),
        "combining_class": unicodedata.combining(ch),
        "block": block,
        "chart": chart,
    }


def reorders_with(codepoints):
    """Whether these marks are canonically reordered relative to each other.

    Marks with different non-zero combining classes are reordered by NFC and
    NFD, so two Mushaf texts that look identical can compare unequal. Marks
    sharing a combining class are never reordered, which makes the order they
    were stored in significant.
    """
    classes = {properties(cp)["combining_class"] for cp in codepoints}
    classes.discard(0)
    return len(classes) > 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(1)
    for a in args:
        p = properties(a)
        print(f"{p['cp']}  {p['name']}")
        print(f"    category {p['category']} ({p['category_note']})")
        print(f"    combining class {p['combining_class']}   block {p['block']}")
        print(f"    chart {p['chart']}")
