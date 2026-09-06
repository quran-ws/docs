"""Run the whole build: derive, generate, check.

Every generated file in this repository comes from one of these steps, in this
order. Running them by hand in the wrong order produces a page generated from
data that a later step then changes, so there is one entry point:

    python3 tools/build.py
    python3 tools/build.py --keep-going    # run every step, report at the end

The order matters: the marks are generated before the indexes that read them,
the indexes before the checks, the checks before the pages, and the skill last,
because it packages everything the earlier steps produced.
"""
import argparse
import os
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

STEPS = [
    (["test_translit.py"], "the spelling rules still hold"),
    (["generate_dabt.py"], "the mark entries, generated from the registry"),
    (["build_aliases.py"], "the alias index"),
    (["build_registry_aliases.py"], "the member index"),
    (["extract_ayah_counts.py", "--check"], "the ayah counts still reconcile"),
    (["validate.py"], "every entry matches the schema"),
    (["check_conformance.py"], "every entry obeys the standard"),
    (["check_registries.py"], "every member of every closed set holds up"),
    (["generate_dictionary.py"], "the dictionary pages, Arabic and English"),
    (["check_examples.py"], "no stale name in the prose"),
    (["generate_skill.py"], "the agent skill, with the dictionary it resolves against"),
]


def run(step, keep_going):
    command = [sys.executable, os.path.join(TOOLS, step[0])] + list(step[1:])
    result = subprocess.run(command, cwd=ROOT)
    return result.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keep-going", action="store_true",
                    help="run every step even after one fails")
    args = ap.parse_args()

    failed = []
    for step, what in STEPS:
        print(f"\n── {step[0]} — {what}")
        code = run(step, args.keep_going)
        if code:
            failed.append(step[0])
            if not args.keep_going:
                print(f"\n{step[0]} failed; the steps after it did not run")
                return code
    print()
    if failed:
        print(f"{len(failed)} steps failed: {', '.join(failed)}")
        return 1
    print(f"ok — {len(STEPS)} steps, everything generated is in step with its source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
