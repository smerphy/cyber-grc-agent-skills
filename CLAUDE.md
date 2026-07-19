# CLAUDE.md

Follow the repository-wide agent instructions in [AGENTS.md](AGENTS.md) — they define the three-layer model (personas → skills → context/templates), the operating rules (no fabricated compliance facts, verification footers, evidence over assertion), and the validation command.

Claude-specific notes:

- The directories under `skills/` follow the Agent Skills format (`SKILL.md` with `name`/`description` frontmatter). To make them invocable in Claude Code, copy or symlink individual skill directories into `.claude/skills/` (project) or `~/.claude/skills/` (user) — see [docs/integrations/claude.md](docs/integrations/claude.md).
- When editing content files, keep them provider-neutral: no tool names, no XML tags, no Claude-specific syntax. Provider-specific instructions belong only in `docs/integrations/`.
- After any content change, run `python3 scripts/validate_skills.py` from the repo root.
