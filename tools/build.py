"""Run the whole build: derive, generate, check.

Every generated file in this repository comes from one of these steps, in this
order. Running them by hand in the wrong order produces a page generated from
data that a later step then changes, so there is one entry point:

    python3 tools/build.py
    python3 tools/build.py --keep-going    # run every step, report at the end

The order matters: the marks are generated before the indexes that read them,
the indexes before the checks, the checks before the pages, and the skill last,
because it packages everything the earlier steps produced.

A step marked optional is skipped, with a note, while its script does not exist
yet: the build stays green while a tool is being written.
"""
import argparse
import os
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

OPTIONAL = {"generate_tajwid_registry.py", "generate_registries.py", "check_example_files.py",
            "check_issue_templates.py"}

STEPS = [
    (["test_translit.py"], "the spelling rules still hold"),
    (["generate_dabt.py"], "the mark entries, generated from the registry"),
    (["build_aliases.py"], "the alias index"),
    (["generate_tajwid_registry.py"], "the tajwid rules registry, from its source"),
    (["build_registry_aliases.py"], "the member index"),
    (["extract_ayah_counts.py", "--check"], "the ayah counts still reconcile"),
    (["validate.py"], "every entry matches the schema"),
    (["check_issue_templates.py"], "the term form offers the schema's values"),
    (["check_conformance.py"], "every entry obeys the standard"),
    (["check_registries.py"], "every member of every closed set holds up"),
    (["generate_dictionary.py"], "the dictionary pages, Arabic and English"),
    (["generate_registries.py"], "the registry pages"),
    (["generate_pages.py"], "the guideline pages, from their rule files"),
    (["generate_standard.py"], "the Arabic naming standard, from its structured rules"),
    (["generate_glossary.py"], "the site glossary, from the dictionary"),
    (["check_examples.py"], "no stale name or section number in the prose"),
    (["check_example_files.py"], "the example files still say what the prose says"),
    (["generate_skill.py"], "the agent skill, with the dictionary it resolves against"),
]


def run(step):
    command = [sys.executable, os.path.join(TOOLS, step[0])] + list(step[1:])
    return subprocess.run(command, cwd=ROOT).returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keep-going", action="store_true",
                    help="run every step even after one fails")
    args = ap.parse_args()

    # The steps write straight to the terminal; the headers must not lag them.
    say = lambda text: print(text, flush=True)
    failed, skipped, ran = [], [], 0
    for step, what in STEPS:
        if not os.path.exists(os.path.join(TOOLS, step[0])):
            if step[0] in OPTIONAL:
                skipped.append(step[0])
                say(f"\n── {step[0]} — skipped, not written yet")
                continue
            say(f"\n── {step[0]} — missing")
            return 1
        say(f"\n── {step[0]} — {what}")
        ran += 1
        if run(step):
            failed.append(step[0])
            if not args.keep_going:
                say(f"\n{step[0]} failed; the steps after it did not run")
                return 1
    say("")
    if failed:
        say(f"{len(failed)} steps failed: {', '.join(failed)}")
        return 1
    note = f" ({len(skipped)} optional steps skipped: {', '.join(skipped)})" if skipped else ""
    say(f"ok — {ran} steps, everything generated is in step with its source{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
