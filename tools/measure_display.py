"""Measure which English spelling of a term is dominant, so `display` is set
by evidence rather than by taste.

GitHub phrase search, quoted so the terms must be adjacent. Unquoted queries
are AND over the whole file and are useless here: they rank `mim sakinah`
above `noon sakinah` purely on unrelated `mim` tokens.

    python3 tools/measure_display.py            # measure the contested set
    python3 tools/measure_display.py "a" "b"    # compare two phrases

Results are cached, because the search API rate-limits aggressively.
"""
import json, os, subprocess, sys, time

CACHE = os.path.join(os.path.dirname(__file__), "display_measurements.json")

# Terms whose English form is contested. Left is the letter-based derivation,
# right the form common in English-language Quranic writing.
CONTESTED = [
    ("nun sakinah", "noon sakinah"),
    ("mim sakinah", "meem sakinah"),
    ("mim mushaddad", "meem mushaddad"),
    # ("sin", "seen") — unmeasurable: both are ordinary English words, so the
    # counts reflect English prose, not Quranic usage. Decided by pattern instead.
    ("tajwid", "tajweed"),
    ("tafkhim", "tafkheem"),
    ("tarqiq", "tarqeeq"),
    ("qiraah", "qiraat"),
    ("madd tabii", "madd tabee"),
    ("idgham naqis", "idgham naqees"),
]


# A single-token query is only meaningful when the token is not itself an
# English word. Anything here must be measured inside a qualifying phrase.
ENGLISH_COLLISIONS = {"sin", "seen", "nun", "noon", "madd", "min", "man"}


def count(phrase):
    if phrase in ENGLISH_COLLISIONS:
        raise ValueError(
            f"{phrase!r} is an English word; measure it in a phrase such as "
            f"'{phrase} sakinah', or the count is English prose, not usage")
    out = subprocess.run(
        ["gh", "api", "-X", "GET", "search/code", "-f", f'q="{phrase}"',
         "-f", "per_page=1", "--jq", ".total_count"],
        capture_output=True, text=True)
    try:
        return int(out.stdout.strip())
    except ValueError:
        return None


def load():
    return json.load(open(CACHE)) if os.path.exists(CACHE) else {}


def save(d):
    json.dump(d, open(CACHE, "w"), ensure_ascii=False, indent=1, sort_keys=True)


def measure(pairs, delay=4):
    data = load()
    for a, b in pairs:
        key = f"{a} | {b}"
        if key in data and data[key].get("a") is not None:
            continue
        na, nb = count(a), None
        time.sleep(delay)
        if na is not None:
            nb = count(b)
            time.sleep(delay)
        data[key] = {"a": na, "b": nb}
        save(data)
        if na is None or nb is None:
            print(f"{key}: rate limited, stopping"); break
        winner = a if na >= nb else b
        print(f"{a:16} {na:>6}   {b:16} {nb:>6}   → {winner}")
    return data


if __name__ == "__main__":
    pairs = [tuple(sys.argv[1:3])] if len(sys.argv) >= 3 else CONTESTED
    measure(pairs)
