#!/usr/bin/env python3
"""Build per-persona knowledge bundles for providers that take file uploads.

For each persona in agents/, collects:
  1. the persona file itself (use as system prompt / GPT instructions),
  2. SKILL.md for every skill in its recommended_skills,
  3. context packs and templates those SKILL.md files link to directly,
  4. the skills' references/ files (dropped first when a file cap applies).

Outputs, under dist/:
  dist/<persona>/            full bundle directory
  dist/<persona>.zip         zip of the full bundle
  dist/<persona>-gpt20/      capped bundle (default 20 files) for Custom GPT
  dist/<persona>-gpt20.zip
Each bundle contains a MANIFEST.md explaining what's inside (and, for capped
bundles, what was omitted). Bundle files are flattened with path-derived names
(context__regulations__gdpr.md) because most upload UIs ignore directories.

Run from the repo root:  python3 scripts/build_bundles.py [--cap N] [persona ...]
Stdlib only.
"""

import argparse
import os
import re
import shutil
import sys
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(REPO_ROOT, "dist")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^()\s]+)\)")


def parse_recommended_skills(persona_path):
    skills, in_list = [], False
    with open(persona_path, encoding="utf-8") as f:
        for line in f.read().split("---", 2)[1].splitlines():
            if re.match(r"^recommended_skills:\s*$", line):
                in_list = True
                continue
            if in_list:
                m = re.match(r"^\s+-\s+(.+?)\s*$", line)
                if m:
                    skills.append(m.group(1).strip())
                elif line.strip() and not line[0].isspace():
                    break
    return skills


def linked_repo_files(md_path):
    """Repo files (context/, templates/, branding/) directly linked from a markdown file."""
    out = []
    base = os.path.dirname(md_path)
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    for m in LINK_RE.finditer(text):
        target = m.group(1).split("#")[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "/")):
            continue
        resolved = os.path.normpath(os.path.join(base, target))
        rel = os.path.relpath(resolved, REPO_ROOT)
        if rel.startswith(("context" + os.sep, "templates" + os.sep, "branding" + os.sep)) and os.path.isfile(resolved):
            out.append(rel)
    return out


def flat_name(rel):
    return rel.replace(os.sep, "__")


def collect(persona):
    """Return ordered list of (repo_rel_path, priority) — lower priority dropped first."""
    persona_rel = os.path.join("agents", persona + ".md")
    persona_path = os.path.join(REPO_ROOT, persona_rel)
    if not os.path.isfile(persona_path):
        raise SystemExit(f"ERROR: no persona agents/{persona}.md")

    files = {persona_rel: 0}                      # 0 = never drop
    context_files, reference_files = [], []

    for skill in parse_recommended_skills(persona_path):
        skill_md_rel = os.path.join("skills", skill, "SKILL.md")
        skill_md = os.path.join(REPO_ROOT, skill_md_rel)
        if not os.path.isfile(skill_md):
            print(f"  WARN: {persona}: skill '{skill}' not found, skipping")
            continue
        files[skill_md_rel] = 1                   # 1 = core skill
        for rel in linked_repo_files(skill_md):
            context_files.append(rel)
        ref_dir = os.path.join(REPO_ROOT, "skills", skill, "references")
        if os.path.isdir(ref_dir):
            for fname in sorted(os.listdir(ref_dir)):
                reference_files.append(os.path.join("skills", skill, "references", fname))

    for rel in context_files:
        files.setdefault(rel, 2)                  # 2 = linked context/templates
    for rel in reference_files:
        files.setdefault(rel, 3)                  # 3 = references (dropped first)
    return files


def write_bundle(persona, files, out_name, cap=None):
    ordered = sorted(files.items(), key=lambda kv: (kv[1], kv[0]))
    kept, dropped = [], []
    for rel, prio in ordered:
        # +1 accounts for MANIFEST.md itself.
        if cap is not None and len(kept) + 1 >= cap and prio >= 2:
            dropped.append(rel)
        else:
            kept.append(rel)
    # Enforce the cap strictly even if core files alone exceed it.
    if cap is not None and len(kept) + 1 > cap:
        overflow = kept[cap - 1:]
        kept = kept[: cap - 1]
        dropped = overflow + dropped

    bundle_dir = os.path.join(DIST, out_name)
    shutil.rmtree(bundle_dir, ignore_errors=True)
    os.makedirs(bundle_dir)

    for rel in kept:
        shutil.copyfile(os.path.join(REPO_ROOT, rel), os.path.join(bundle_dir, flat_name(rel)))

    manifest = [
        f"# Bundle: {out_name}",
        "",
        f"Persona bundle generated from the Cyber GRC Agent Skills repository.",
        f"Use `agents__{persona}.md` as the system prompt / GPT instructions and",
        "upload the remaining files as knowledge. File names encode their repo",
        "paths (`__` = `/`); relative links inside files refer to those paths.",
        "",
        "## Included",
        "",
    ]
    manifest += [f"- `{flat_name(rel)}`" for rel in kept]
    if dropped:
        manifest += [
            "",
            "## Omitted to stay under the file cap",
            "",
            "Fetch these from the repository if you need the depth:",
            "",
        ]
        manifest += [f"- `{rel}`" for rel in dropped]
    with open(os.path.join(bundle_dir, "MANIFEST.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(manifest) + "\n")

    zip_path = bundle_dir + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in sorted(os.listdir(bundle_dir)):
            zf.write(os.path.join(bundle_dir, fname), fname)

    total = len(kept) + 1
    print(f"  {out_name}: {total} files"
          + (f" ({len(dropped)} omitted for cap)" if dropped else "")
          + f" -> dist/{out_name}.zip")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("personas", nargs="*", help="persona names (default: all in agents/)")
    ap.add_argument("--cap", type=int, default=20,
                    help="file cap for the capped bundle variant (default 20; Custom GPT limit)")
    args = ap.parse_args()

    personas = args.personas or sorted(
        os.path.splitext(f)[0]
        for f in os.listdir(os.path.join(REPO_ROOT, "agents")) if f.endswith(".md")
    )
    os.makedirs(DIST, exist_ok=True)
    for persona in personas:
        print(f"{persona}:")
        files = collect(persona)
        write_bundle(persona, files, persona)
        write_bundle(persona, files, f"{persona}-gpt{args.cap}", cap=args.cap)


if __name__ == "__main__":
    main()
