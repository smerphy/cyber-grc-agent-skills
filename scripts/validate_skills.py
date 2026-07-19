#!/usr/bin/env python3
"""Repository validator for the Cyber GRC Agent Skills library.

Checks, with no third-party dependencies:

1. Every skills/*/SKILL.md has YAML frontmatter with the required keys
   (name, description, license, metadata), the name matches its directory,
   the description is 100-1024 characters, the body contains the required
   H2 sections, and the body is under 500 lines.
2. Every relative markdown link in .md files under skills/, workflows/,
   context/, docs/, agents/, and templates/ resolves to an existing file
   or directory.

Run from the repo root:  python3 scripts/validate_skills.py
Exits 1 with a per-file error report on any failure.
"""

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
SKIP_SCHEMES = ("http://", "https://", "mailto:", "ftp://", "tel:")


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
    """Minimal hand-rolled parser for the flat-plus-one-level YAML this repo uses.

    Supports:  key: value | key: >- (folded multiline scalar) | key: + nested map.
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


def main():
    skills_dir = os.path.join(REPO_ROOT, "skills")
    errors = {}
    skill_count = 0
    link_count = 0
    file_count = 0

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

    if errors:
        print(f"FAIL: {sum(len(v) for v in errors.values())} error(s) "
              f"in {len(errors)} file(s)\n")
        for rel in sorted(errors):
            print(f"  {rel}")
            for msg in errors[rel]:
                print(f"    - {msg}")
        sys.exit(1)

    print(f"OK: {skill_count} skills validated, {file_count} markdown files scanned, "
          f"{link_count} relative links resolved.")


if __name__ == "__main__":
    main()
