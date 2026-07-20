#!/usr/bin/env python3
"""Assemble site-src/ for the mkdocs documentation site.

Mirrors the repository's content directories into site-src/ (preserving
structure so relative links keep working) and creates index.md from
README.md. Run from the repo root before `mkdocs build`:

    python3 scripts/build_docs_site.py
    mkdocs build

Stdlib only.
"""

import os
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_SRC = os.path.join(REPO_ROOT, "site-src")

CONTENT_DIRS = ("skills", "context", "workflows", "agents", "templates", "branding", "docs", "examples")
ROOT_FILES = ("README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md",
              "CHANGELOG.md", "SECURITY.md", "LICENSE", "llms.txt")


def main():
    shutil.rmtree(SITE_SRC, ignore_errors=True)
    os.makedirs(SITE_SRC)

    for d in CONTENT_DIRS:
        src = os.path.join(REPO_ROOT, d)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(SITE_SRC, d))

    for f in ROOT_FILES:
        src = os.path.join(REPO_ROOT, f)
        if os.path.isfile(src):
            shutil.copyfile(src, os.path.join(SITE_SRC, f))

    # index.md is the site home; keep README.md too so links to it resolve.
    shutil.copyfile(os.path.join(REPO_ROOT, "README.md"),
                    os.path.join(SITE_SRC, "index.md"))

    total = sum(len(files) for _r, _d, files in os.walk(SITE_SRC))
    print(f"site-src/ assembled: {total} files")


if __name__ == "__main__":
    main()
