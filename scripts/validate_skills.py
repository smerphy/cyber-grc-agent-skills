#!/usr/bin/env python3
"""Repository validator for the Cyber GRC Agent Skills library.

Checks, with no third-party dependencies:

1. Every skills/*/SKILL.md has YAML frontmatter with the required keys
   (name, description, license, metadata), the name matches its directory,
   the description is 100-1024 characters, the body contains the required
   H2 sections, and the body is under 450 lines.
2. Every relative markdown link in .md files under skills/, workflows/,
   context/, docs/, agents/, and templates/ resolves to an existing file
   or directory.
3. Every context pack (context/**/*.md) carries the verification footer
   with a parseable "Last reviewed: YYYY-MM" date; framework and
   regulation packs additionally carry a "## Primary sources" section.
4. Every workflow (workflows/*.md) has a yaml header block whose name
   matches the filename and whose skills_used all resolve to real skills.
5. Every persona (agents/*.md) has frontmatter with name/description and
   recommended_skills that all resolve to real skills.
6. Every CSV under templates/ parses with a consistent column count.

Run from the repo root:  python3 scripts/validate_skills.py
Optional:  --stale N   also list context packs whose "Last reviewed" date
                       is more than N months old (informational)
           --fail-stale  with --stale, treat stale packs as errors
Exits 1 with a per-file error report on any failure.
"""

import argparse
import csv
import datetime
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_KEYS = ("name", "description", "license", "metadata")
REQUIRED_SECTIONS = (
    "Purpose",
    "When to use",
    "Inputs to gather",
    "Procedure",
    "Output format",
    "Quality checklist",
    "References",
)
LINK_DIRS = ("skills", "workflows", "context", "docs", "agents", "templates")
DESC_MIN, DESC_MAX = 100, 1024
MAX_BODY_LINES = 450  # body must be strictly less than this

FENCE_RE = re.compile(r"^(```|~~~)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^()\s]+(?:\([^()]*\))?[^()]*)\)")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
TOP_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
NESTED_KEY_RE = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.+?)\s*$")
FOOTER_RE = re.compile(r"\*\*Verification note:\*\*.*Last reviewed:\s*(\d{4})-(\d{2})")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "ftp://", "tel:")

# Context packs that are methodological rather than framework/regulation
# summaries; they need the footer but not a Primary sources section.
PRIMARY_SOURCE_DIRS = ("context/frameworks", "context/regulations", "context/crosswalks")
PRIMARY_SOURCE_EXEMPT = {"context/glossary.md"}


def split_frontmatter(text):
    """Return (frontmatter_lines, body_text) or (None, text) if no frontmatter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, text


def parse_frontmatter(fm_lines):
    """Minimal hand-rolled parser for the flat YAML this repo uses.

    Supports:  key: value | key: >- (folded scalar) | key: + nested map
               key: + "- item" list lines.
    """
    data = {}
    current_key = None
    folded = False
    for line in fm_lines:
        if line.strip() and not line[0].isspace():
            m = TOP_KEY_RE.match(line)
            if not m:
                continue
            key, value = m.group(1), m.group(2).strip()
            current_key = key
            if value in (">", ">-", ">+", "|", "|-", "|+"):
                data[key] = ""
                folded = True
            else:
                data[key] = value.strip("'\"")
                folded = False
        elif line.strip() and current_key:
            if folded:
                data[current_key] = (data[current_key] + " " + line.strip()).strip()
            elif LIST_ITEM_RE.match(line):
                if not isinstance(data.get(current_key), list):
                    data[current_key] = []
                data[current_key].append(LIST_ITEM_RE.match(line).group(1).strip("'\""))
            else:
                if data.get(current_key) == "":
                    data[current_key] = {}
                if isinstance(data.get(current_key), dict):
                    m = NESTED_KEY_RE.match(line)
                    if m:
                        data[current_key][m.group(1)] = m.group(2).strip().strip("'\"")
    return data


def strip_code(text):
    """Remove fenced code blocks and inline code spans so example paths
    inside code are not treated as real links."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return re.sub(r"`[^`\n]*`", "", "\n".join(out))


def skill_exists(name):
    return os.path.isfile(os.path.join(REPO_ROOT, "skills", name, "SKILL.md"))


def check_skill(path, errors):
    rel = os.path.relpath(path, REPO_ROOT)
    with open(path, encoding="utf-8") as f:
        text = f.read()

    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        errors.setdefault(rel, []).append(
            "missing YAML frontmatter (file must start with '---' and close with '---')"
        )
        return

    fm = parse_frontmatter(fm_lines)
    for key in REQUIRED_KEYS:
        if key not in fm:
            errors.setdefault(rel, []).append(f"frontmatter missing required key: {key}")

    dir_name = os.path.basename(os.path.dirname(path))
    if fm.get("name") and fm["name"] != dir_name:
        errors.setdefault(rel, []).append(
            f"frontmatter name '{fm['name']}' does not match directory '{dir_name}'"
        )

    desc = fm.get("description")
    if isinstance(desc, str) and desc:
        if not (DESC_MIN <= len(desc) <= DESC_MAX):
            errors.setdefault(rel, []).append(
                f"description length {len(desc)} chars (must be {DESC_MIN}-{DESC_MAX})"
            )
    elif "description" in fm:
        errors.setdefault(rel, []).append("description is empty or not a string")

    body_lines = body.splitlines()
    if len(body_lines) >= MAX_BODY_LINES:
        errors.setdefault(rel, []).append(
            f"body is {len(body_lines)} lines (must be under {MAX_BODY_LINES})"
        )

    headings = {m.group(1).strip().lower() for line in body_lines if (m := H2_RE.match(line))}
    for section in REQUIRED_SECTIONS:
        if section.lower() not in headings:
            errors.setdefault(rel, []).append(f"missing required H2 section: '## {section}'")


def check_links(path, errors):
    rel = os.path.relpath(path, REPO_ROOT)
    with open(path, encoding="utf-8") as f:
        text = strip_code(f.read())

    checked = 0
    for m in LINK_RE.finditer(text):
        target = m.group(1).strip()
        # Drop an optional markdown link title: (path "title")
        target = target.split(" ")[0].strip("<>")
        # Drop anchor fragments.
        target = target.split("#")[0]
        if not target or target.startswith(SKIP_SCHEMES):
            continue
        if target.startswith("/"):
            errors.setdefault(rel, []).append(
                f"absolute link '{target}' (use a relative path)"
            )
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            msg = f"broken relative link: {target}"
            if msg not in errors.get(rel, []):
                errors.setdefault(rel, []).append(msg)
        checked += 1
    return checked


def check_context_pack(path, errors, reviewed_dates):
    """Verification footer + Last reviewed date; Primary sources for
    framework/regulation/crosswalk packs."""
    rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
    with open(path, encoding="utf-8") as f:
        text = f.read()

    m = FOOTER_RE.search(text)
    if not m:
        errors.setdefault(rel, []).append(
            "missing verification footer with parseable 'Last reviewed: YYYY-MM' date"
        )
    else:
        year, month = int(m.group(1)), int(m.group(2))
        if not (2020 <= year <= 2100 and 1 <= month <= 12):
            errors.setdefault(rel, []).append(
                f"implausible Last reviewed date: {m.group(1)}-{m.group(2)}"
            )
        else:
            reviewed_dates[rel] = (year, month)

    needs_sources = (
        any(rel.startswith(d + "/") for d in PRIMARY_SOURCE_DIRS)
        and rel not in PRIMARY_SOURCE_EXEMPT
    )
    if needs_sources and "## Primary sources" not in text:
        errors.setdefault(rel, []).append("missing '## Primary sources' section")


def check_workflow(path, errors):
    """Workflows carry a ```yaml header block with name/description/skills_used."""
    rel = os.path.relpath(path, REPO_ROOT)
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    block, in_yaml = [], False
    for line in lines:
        if line.strip().startswith("```"):
            if in_yaml:
                break
            if line.strip() == "```yaml":
                in_yaml = True
            continue
        if in_yaml:
            block.append(line)

    if not block:
        errors.setdefault(rel, []).append("missing ```yaml header block")
        return

    fm = parse_frontmatter(block)
    fname = os.path.splitext(os.path.basename(path))[0]
    if not fm.get("name"):
        errors.setdefault(rel, []).append("yaml header missing 'name'")
    elif fm["name"] != fname:
        errors.setdefault(rel, []).append(
            f"yaml header name '{fm['name']}' does not match filename '{fname}'"
        )
    if not fm.get("description"):
        errors.setdefault(rel, []).append("yaml header missing 'description'")
    skills_used = fm.get("skills_used")
    if not isinstance(skills_used, list) or not skills_used:
        errors.setdefault(rel, []).append("yaml header missing 'skills_used' list")
    else:
        for s in skills_used:
            if not skill_exists(s):
                errors.setdefault(rel, []).append(
                    f"skills_used entry '{s}' does not resolve to skills/{s}/SKILL.md"
                )


def check_agent(path, errors):
    """Personas carry frontmatter with name/description/recommended_skills."""
    rel = os.path.relpath(path, REPO_ROOT)
    with open(path, encoding="utf-8") as f:
        text = f.read()

    fm_lines, _body = split_frontmatter(text)
    if fm_lines is None:
        errors.setdefault(rel, []).append("missing YAML frontmatter")
        return
    fm = parse_frontmatter(fm_lines)
    fname = os.path.splitext(os.path.basename(path))[0]
    if not fm.get("name"):
        errors.setdefault(rel, []).append("frontmatter missing 'name'")
    elif fm["name"] != fname:
        errors.setdefault(rel, []).append(
            f"frontmatter name '{fm['name']}' does not match filename '{fname}'"
        )
    if not fm.get("description"):
        errors.setdefault(rel, []).append("frontmatter missing 'description'")
    rec = fm.get("recommended_skills")
    if not isinstance(rec, list) or not rec:
        errors.setdefault(rel, []).append("frontmatter missing 'recommended_skills' list")
    else:
        for s in rec:
            if not skill_exists(s):
                errors.setdefault(rel, []).append(
                    f"recommended_skills entry '{s}' does not resolve to skills/{s}/SKILL.md"
                )


def check_csv(path, errors):
    rel = os.path.relpath(path, REPO_ROOT)
    try:
        with open(path, encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
    except (csv.Error, UnicodeDecodeError) as exc:
        errors.setdefault(rel, []).append(f"CSV does not parse: {exc}")
        return
    if not rows:
        errors.setdefault(rel, []).append("CSV is empty")
        return
    width = len(rows[0])
    for i, row in enumerate(rows[1:], start=2):
        if row and len(row) != width:
            errors.setdefault(rel, []).append(
                f"row {i} has {len(row)} columns (header has {width})"
            )


def months_old(year, month, today=None):
    today = today or datetime.date.today()
    return (today.year - year) * 12 + (today.month - month)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stale", type=int, metavar="N",
                    help="list context packs last reviewed more than N months ago")
    ap.add_argument("--fail-stale", action="store_true",
                    help="with --stale, treat stale packs as errors")
    args = ap.parse_args()

    skills_dir = os.path.join(REPO_ROOT, "skills")
    errors = {}
    reviewed_dates = {}
    skill_count = 0
    link_count = 0
    file_count = 0
    context_count = 0
    workflow_count = 0
    agent_count = 0
    csv_count = 0

    # 1. Skill structure checks.
    if not os.path.isdir(skills_dir):
        print("ERROR: skills/ directory not found — run from the repo root.")
        sys.exit(1)

    for entry in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, entry)
        if not os.path.isdir(skill_path):
            continue
        skill_md = os.path.join(skill_path, "SKILL.md")
        if not os.path.isfile(skill_md):
            errors.setdefault(os.path.join("skills", entry), []).append("missing SKILL.md")
            continue
        skill_count += 1
        check_skill(skill_md, errors)

    # 2. Relative link checks across content directories.
    for dir_name in LINK_DIRS:
        base = os.path.join(REPO_ROOT, dir_name)
        if not os.path.isdir(base):
            continue
        for root, _dirs, files in os.walk(base):
            for fname in sorted(files):
                if fname.endswith(".md"):
                    file_count += 1
                    link_count += check_links(os.path.join(root, fname), errors)

    # 3. Context pack checks (footer, review date, primary sources).
    context_dir = os.path.join(REPO_ROOT, "context")
    for root, _dirs, files in os.walk(context_dir):
        for fname in sorted(files):
            if fname.endswith(".md"):
                context_count += 1
                check_context_pack(os.path.join(root, fname), errors, reviewed_dates)

    # 4. Workflow header checks.
    workflows_dir = os.path.join(REPO_ROOT, "workflows")
    if os.path.isdir(workflows_dir):
        for fname in sorted(os.listdir(workflows_dir)):
            if fname.endswith(".md"):
                workflow_count += 1
                check_workflow(os.path.join(workflows_dir, fname), errors)

    # 5. Persona frontmatter checks.
    agents_dir = os.path.join(REPO_ROOT, "agents")
    if os.path.isdir(agents_dir):
        for fname in sorted(os.listdir(agents_dir)):
            if fname.endswith(".md"):
                agent_count += 1
                check_agent(os.path.join(agents_dir, fname), errors)

    # 6. Template CSV checks.
    templates_dir = os.path.join(REPO_ROOT, "templates")
    if os.path.isdir(templates_dir):
        for fname in sorted(os.listdir(templates_dir)):
            if fname.endswith(".csv"):
                csv_count += 1
                check_csv(os.path.join(templates_dir, fname), errors)

    # 7. Optional staleness report.
    stale = []
    if args.stale is not None:
        for rel, (year, month) in sorted(reviewed_dates.items()):
            age = months_old(year, month)
            if age > args.stale:
                stale.append((rel, year, month, age))
        if stale:
            print(f"STALE: {len(stale)} context pack(s) last reviewed more than "
                  f"{args.stale} months ago:")
            for rel, year, month, age in stale:
                print(f"  {rel} (last reviewed {year}-{month:02d}, {age} months ago)")
            if args.fail_stale:
                for rel, year, month, age in stale:
                    errors.setdefault(rel, []).append(
                        f"stale: last reviewed {year}-{month:02d} ({age} months ago)"
                    )
        else:
            print(f"STALE: none older than {args.stale} months.")

    if errors:
        print(f"FAIL: {sum(len(v) for v in errors.values())} error(s) "
              f"in {len(errors)} file(s)\n")
        for rel in sorted(errors):
            print(f"  {rel}")
            for msg in errors[rel]:
                print(f"    - {msg}")
        sys.exit(1)

    print(f"OK: {skill_count} skills, {workflow_count} workflows, {agent_count} personas, "
          f"{context_count} context packs, {csv_count} CSVs validated; "
          f"{file_count} markdown files scanned, {link_count} relative links resolved.")


if __name__ == "__main__":
    main()
