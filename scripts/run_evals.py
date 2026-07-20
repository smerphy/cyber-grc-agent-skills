#!/usr/bin/env python3
"""Run the eval scenarios in evals/scenarios/ against answers.

Two modes:

  Grade pre-produced answers (one markdown file per scenario id):
    python3 scripts/run_evals.py --answers /path/to/answers

  Generate answers with a command that reads the prompt on stdin and
  writes the answer to stdout, then grade them:
    python3 scripts/run_evals.py --exec 'claude -p' --answers /tmp/eval-answers

Grading is pattern-based (see evals/README.md for the honest limits):
each rubric check passes if ANY of its case-insensitive regexes matches
the answer; forbidden checks subtract their penalty if matched. A
scenario passes at or above its rubric threshold. Exit code 1 if any
scenario fails or is missing an answer. Stdlib only.
"""

import argparse
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCENARIOS_DIR = os.path.join(REPO_ROOT, "evals", "scenarios")


def load_scenarios(only=None):
    out = []
    for entry in sorted(os.listdir(SCENARIOS_DIR)):
        sdir = os.path.join(SCENARIOS_DIR, entry)
        if not os.path.isdir(sdir):
            continue
        if only and entry not in only:
            continue
        with open(os.path.join(sdir, "prompt.md"), encoding="utf-8") as f:
            prompt = f.read()
        with open(os.path.join(sdir, "rubric.json"), encoding="utf-8") as f:
            rubric = json.load(f)
        out.append({"id": entry, "prompt": prompt, "rubric": rubric})
    return out


def grade(answer, rubric):
    results, earned, total = [], 0.0, 0.0
    for check in rubric["checks"]:
        total += check["points"]
        hit = any(re.search(p, answer, re.I | re.S) for p in check["any"])
        if hit:
            earned += check["points"]
        results.append(("PASS" if hit else "MISS", check["points"], check["id"], check["description"]))
    for check in rubric.get("forbidden", []):
        hit = any(re.search(p, answer, re.I | re.S) for p in check["any"])
        if hit:
            earned -= check["penalty"]
            results.append(("VIOLATION", -check["penalty"], check["id"], check["description"]))
    score = max(0.0, earned) / total if total else 0.0
    return score, results


def main():
    ap = argparse.ArgumentParser(description="Grade eval scenarios for the Cyber GRC skills library.")
    ap.add_argument("--answers", required=True, metavar="DIR",
                    help="directory of <scenario-id>.md answer files (created if --exec)")
    ap.add_argument("--exec", dest="exec_cmd", metavar="CMD",
                    help="shell command that reads a prompt on stdin and prints the answer")
    ap.add_argument("--scenario", action="append", metavar="ID",
                    help="run only this scenario id (repeatable)")
    ap.add_argument("--timeout", type=int, default=600, help="per-scenario --exec timeout seconds")
    args = ap.parse_args()

    scenarios = load_scenarios(args.scenario)
    if not scenarios:
        print("No scenarios found.", file=sys.stderr)
        sys.exit(1)
    os.makedirs(args.answers, exist_ok=True)

    failures = 0
    for sc in scenarios:
        answer_path = os.path.join(args.answers, sc["id"] + ".md")
        if args.exec_cmd:
            print(f"[{sc['id']}] generating answer via: {args.exec_cmd}")
            proc = subprocess.run(args.exec_cmd, shell=True, input=sc["prompt"],
                                  capture_output=True, text=True, timeout=args.timeout,
                                  cwd=REPO_ROOT)
            if proc.returncode != 0:
                print(f"[{sc['id']}] FAIL: generator exited {proc.returncode}: {proc.stderr[:400]}")
                failures += 1
                continue
            with open(answer_path, "w", encoding="utf-8") as f:
                f.write(proc.stdout)
        if not os.path.isfile(answer_path):
            print(f"[{sc['id']}] FAIL: no answer file at {answer_path}")
            failures += 1
            continue
        with open(answer_path, encoding="utf-8") as f:
            answer = f.read()

        score, results = grade(answer, sc["rubric"])
        threshold = sc["rubric"].get("threshold", 0.7)
        verdict = "PASS" if score >= threshold else "FAIL"
        if verdict == "FAIL":
            failures += 1
        print(f"\n[{sc['id']}] {sc['rubric'].get('title', sc['id'])}")
        print(f"  score {score:.0%} (threshold {threshold:.0%}) -> {verdict}")
        for status, points, cid, desc in results:
            mark = {"PASS": "+", "MISS": "-", "VIOLATION": "!"}[status]
            print(f"  {mark} [{status:9s}] {points:+.0f}  {cid}: {desc}")

    print(f"\n{'ALL SCENARIOS PASS' if failures == 0 else f'{failures} scenario(s) failed'}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
