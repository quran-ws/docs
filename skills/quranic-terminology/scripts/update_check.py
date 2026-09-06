#!/usr/bin/env python3
"""Say whether this skill's copy of the standard is still current.

The dictionary changes: entries are added, a spelling is settled, a draft is
adopted. This skill carries a snapshot, stamped with the commit it was built
from, and this asks GitHub whether the terminology has moved since.

    python3 update_check.py            # compare against the published repository
    python3 update_check.py --json
    python3 update_check.py --offline  # print the stamp without asking anything

Exit codes: 0 current, 1 behind, 2 could not tell (offline, rate limited).
A network failure is never treated as a finding: the audit still runs, it just
runs against the snapshot it has.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data", "terminology.json")
# The paths a name can change under. Anything else in the repository may move
# without this snapshot being stale.
WATCHED = "standards/terminology"
API = "https://api.github.com/repos/{repo}/commits?path={path}&per_page=1"
TIMEOUT = 10


def stamp():
    with open(DATA, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("version", {}), data


def latest(repo):
    url = API.format(repo=repo, path=WATCHED)
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "quranic-terminology-skill",
    })
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        commits = json.load(response)
    if not commits:
        return None
    head = commits[0]
    return {"commit": head["sha"][:12],
            "date": head["commit"]["committer"]["date"],
            "message": head["commit"]["message"].splitlines()[0],
            "url": head["html_url"]}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--offline", action="store_true", help="print the stamp only")
    args = ap.parse_args()

    version, data = stamp()
    repo = version.get("repo", "quran-ws/guidelines")
    mine = {"commit": version.get("commit"), "date": version.get("date"),
            "entries": len(data.get("concepts", {})), "repo": repo,
            "source": data.get("source")}

    if args.offline:
        print(json.dumps(mine, indent=1) if args.json else
              f"built from {repo}@{mine['commit']} ({mine['date']}), "
              f"{mine['entries']} entries")
        return 0

    try:
        head = latest(repo)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        message = f"could not reach {repo}: {exc}"
        print(json.dumps({"status": "unknown", "reason": str(exc), "have": mine}, indent=1)
              if args.json else
              f"{message}\nusing the snapshot as it is: {WATCHED}@{mine['commit']}")
        return 2

    current = bool(head) and head["commit"].startswith(str(mine["commit"]))
    result = {"status": "current" if current else "behind", "have": mine, "latest": head}
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    elif current:
        print(f"current — {WATCHED} is at {head['commit']} ({head['date']}), "
              f"which is what this skill was built from")
    else:
        print(f"behind — this skill was built from {mine['commit']} ({mine['date']})")
        print(f"         {WATCHED} is now at {head['commit']} ({head['date']})")
        print(f"         {head['message']}")
        print(f"         {head['url']}")
        print("\nTo refresh: clone https://github.com/{0} and run "
              "`python3 tools/generate_skill.py`,\nthen copy skills/quranic-terminology/ "
              "over this directory.".format(repo))
    return 0 if current else 1


if __name__ == "__main__":
    sys.exit(main())
