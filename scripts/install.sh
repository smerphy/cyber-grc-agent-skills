#!/usr/bin/env bash
# Install Cyber GRC skills into Claude Code (project or user scope).
#
# Usage:
#   scripts/install.sh [--project | --user] [--link] [--list] [skill ...]
#
#   --project   install into ./.claude/skills of the current working directory (default)
#   --user      install into ~/.claude/skills (available in every project)
#   --link      symlink instead of copy (stays in sync with this repo checkout)
#   --list      list available skills and exit
#   skill ...   one or more skill names; omit to install all skills
#
# Examples:
#   scripts/install.sh --list
#   scripts/install.sh --user risk-assessment incident-regulatory-reporting
#   scripts/install.sh --project --link          # everything, symlinked, project scope
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"

scope="project"
mode="copy"
declare -a wanted=()

for arg in "$@"; do
  case "$arg" in
    --project) scope="project" ;;
    --user)    scope="user" ;;
    --link)    mode="link" ;;
    --list)
      echo "Available skills:"
      for d in "$SKILLS_SRC"/*/; do
        printf "  %s\n" "$(basename "$d")"
      done
      exit 0
      ;;
    -h|--help)
      sed -n '2,16p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    --*)
      echo "Unknown option: $arg (try --help)" >&2; exit 1 ;;
    *) wanted+=("$arg") ;;
  esac
done

if [ "$scope" = "user" ]; then
  target="$HOME/.claude/skills"
else
  target="$(pwd)/.claude/skills"
  if [ "$(pwd)" = "$REPO_ROOT" ]; then
    echo "Note: you are installing into the library repo itself. Run from your" >&2
    echo "project directory for a project-scoped install, or use --user." >&2
  fi
fi

if [ ${#wanted[@]} -eq 0 ]; then
  for d in "$SKILLS_SRC"/*/; do
    wanted+=("$(basename "$d")")
  done
fi

mkdir -p "$target"
installed=0
for name in "${wanted[@]}"; do
  src="$SKILLS_SRC/$name"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "SKIP: no such skill '$name' (see --list)" >&2
    continue
  fi
  dest="$target/$name"
  rm -rf "$dest"
  if [ "$mode" = "link" ]; then
    ln -s "$src" "$dest"
  else
    cp -R "$src" "$dest"
  fi
  installed=$((installed + 1))
  echo "installed: $name -> $dest"
done

echo
echo "$installed skill(s) installed ($mode, $scope scope)."
echo "Skills load automatically from their SKILL.md descriptions."
echo "Tip: context packs are referenced by relative paths inside each skill;"
echo "for full cross-linking keep a clone of the repo, or install with --link."
