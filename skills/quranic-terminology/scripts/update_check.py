#!/usr/bin/env python3
"""Say whether this skill's copy of the standard is still current.

The dictionary changes: entries are added, a spelling is settled, a draft is
adopted. This skill carries a snapshot of it, stamped with a hash of the source
it was built from, and this compares that stamp with the copy published in the
repository.

    python3 update_check.py            # compare against the published skill
    python3 update_check.py --json
    python3 update_check.py --offline  # print the stamp without asking anything

Exit codes:
    0  current   the published snapshot is the one this skill carries
    1  behind    the published snapshot differs; refresh before an audit someone will act on
    2  unknown   the network was not reachable (offline, DNS, timeout)
    3  blocked   the published copy could not be read: not found, forbidden, rate limited

Only 1 is a finding about the skill. 2 and 3 are facts about the connection or
the repository: say which snapshot you used and carry on.

Set GITHUB_TOKEN to read a private repository or to lift a rate limit.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data", "terminology.json")
# The published copy of this very file. Its stamp is what a fresh build carries.
PUBLISHED = "https://raw.githubusercontent.com/{repo}/{ref}/skills/quranic-terminology/data/terminology.json"
TIMEOUT = 10

CURRENT, BEHIND, UNKNOWN, BLOCKED = 0, 1, 2, 3


def stamp(path=DATA):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    version = data.get("version") or {}
    return {
        "snapshot": version.get("snapshot"),
        "commit": version.get("commit"),
        "date": version.get("date"),
        "repo": version.get("repo") or "quran-ws/docs",
        "entries": len(data.get("concepts") or {}),
        "spellings": len(data.get("aliases") or {}),
    }


def fetch(source):
    """The stamp of the published copy, from a URL or a local path."""
    if "://" not in source:
        return stamp(source)
    headers = {"User-Agent": "quranic-terminology-skill", "Accept": "application/json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    request = urllib.request.Request(source, headers=headers)
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        data = json.load(response)
    version = data.get("version") or {}
    return {
        "snapshot": version.get("snapshot"),
        "commit": version.get("commit"),
        "date": version.get("date"),
        "entries": len(data.get("concepts") or {}),
        "spellings": len(data.get("aliases") or {}),
    }


def explain_http(exc, source, repo):
    """Turn an HTTP status into a sentence that says what to do about it."""
    code = exc.code
    remaining = exc.headers.get("X-RateLimit-Remaining") if exc.headers else None
    if code == 404:
        return ("not found — the repository is not public, or the published skill is not "
                f"at this path yet: {source}. Check `version.repo` ({repo}) in "
                "data/terminology.json, or set GITHUB_TOKEN if the repository is private.")
    if code in (403, 429) and (remaining == "0" or code == 429):
        reset = exc.headers.get("X-RateLimit-Reset") if exc.headers else None
        return ("rate limited by GitHub" + (f" until epoch {reset}" if reset else "")
                + " — set GITHUB_TOKEN to lift the limit, or retry later.")
    if code in (401, 403):
        return ("forbidden — the repository is private or the token is not allowed to read "
                "it. Set GITHUB_TOKEN with read access, or ask the maintainer.")
    return f"HTTP {code} from {source}: {exc.reason}"


def compare(mine, theirs):
    """Current when the content hashes agree; fall back to the commit if a side has no hash."""
    if mine.get("snapshot") or theirs.get("snapshot"):
        if mine.get("snapshot") and theirs.get("snapshot"):
            return mine["snapshot"] == theirs["snapshot"], "snapshot"
        if theirs.get("snapshot"):
            return False, "snapshot"   # the published copy is stamped and this one is not
        return None, "snapshot"        # the published copy predates the stamp
    if mine.get("commit") and theirs.get("commit"):
        return str(theirs["commit"]).startswith(str(mine["commit"])), "commit"
    return None, "none"


def describe(s):
    label = s.get("snapshot") or s.get("commit") or "unstamped"
    date = f" ({s['date']})" if s.get("date") else ""
    return f"{label}{date}, {s.get('entries', '?')} entries"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--offline", action="store_true", help="print the stamp only")
    ap.add_argument("--ref", default="main", help="branch or tag to compare against (default: main)")
    ap.add_argument("--source", help="URL or local path of a published terminology.json "
                                     "(default: the repository's skill on GitHub)")
    ap.add_argument("--data", default=DATA, help="this skill's terminology.json")
    args = ap.parse_args(argv)

    try:
        mine = stamp(args.data)
    except (OSError, ValueError) as exc:
        print(f"could not read {args.data}: {exc}", file=sys.stderr)
        return BLOCKED
    repo = mine["repo"]
    source = args.source or PUBLISHED.format(repo=repo, ref=args.ref)

    if args.offline:
        print(json.dumps({"status": "offline", "have": mine}, indent=1) if args.json else
              f"built from {repo} at {describe(mine)}"
              + (f", commit {mine['commit']}" if mine.get("commit") and mine.get("snapshot") else ""))
        return CURRENT

    try:
        theirs = fetch(source)
    except urllib.error.HTTPError as exc:
        reason, status, code = explain_http(exc, source, repo), "blocked", BLOCKED
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        reason, status, code = f"could not reach {source}: {exc}", "unknown", UNKNOWN
    else:
        reason = None
    if reason:
        if args.json:
            print(json.dumps({"status": status, "reason": reason, "have": mine}, indent=1))
        else:
            print(f"{status} — {reason}")
            print(f"using the snapshot as it is: {describe(mine)}")
        return code

    current, by = compare(mine, theirs)
    if current is None:
        result = {"status": "unknown", "reason": "neither copy carries a stamp to compare",
                  "have": mine, "published": theirs}
        print(json.dumps(result, indent=1) if args.json else
              f"unknown — {result['reason']}\nusing the snapshot as it is: {describe(mine)}")
        return UNKNOWN

    result = {"status": "current" if current else "behind", "compared": by,
              "have": mine, "published": theirs, "source": source}
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    elif current:
        print(f"current — the published skill carries the same {by}: {describe(mine)}")
    else:
        print(f"behind — this skill carries  {describe(mine)}")
        print(f"         the published one is {describe(theirs)}")
        print("\nTo refresh: `/plugin update quranic-terminology` if it was installed as a "
              "plugin; otherwise copy the published skills/quranic-terminology/ over this "
              "directory, or ask the maintainer for a rebuilt copy. Say which snapshot an "
              "audit used either way.")
    return CURRENT if current else BEHIND


if __name__ == "__main__":
    sys.exit(main())
