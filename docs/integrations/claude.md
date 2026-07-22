# Using this repository with Claude

Four ways to run these skills on Anthropic's stack, from zero-setup to fully programmatic. The content itself is provider-neutral markdown — see [generic.md](generic.md) for the assembly pattern these instructions implement.

## 1. Claude Code (CLI and IDE)

Claude Code natively understands the Agent Skills format used by `skills/`: each skill is a directory with a `SKILL.md` whose frontmatter `description` tells the agent when to load it. Skills placed in a skills directory are discovered automatically and loaded on demand — you do not paste anything.

**Plugin install** (simplest — the repo is a Claude Code plugin; brings all skills, and the personas in `agents/` become invocable agents):

```
/plugin marketplace add smerphy/cyber-grc-agent-skills
/plugin install cyber-grc@cyber-grc-skills
```

**Install script** (pick individual skills, copy or symlink, project or user scope):

```bash
scripts/install.sh --list
scripts/install.sh --user risk-assessment incident-regulatory-reporting
scripts/install.sh --project --link    # everything, symlinked
```

The manual equivalents:

**Per-project install** (recommended — skills travel with the repo you're working in):

```bash
git clone https://github.com/<org>/cyber-grc-agent-skills.git
mkdir -p /path/to/your-project/.claude/skills
cp -r cyber-grc-agent-skills/skills/* /path/to/your-project/.claude/skills/
```

**Per-user install** (available in every project):

```bash
mkdir -p ~/.claude/skills
cp -r cyber-grc-agent-skills/skills/* ~/.claude/skills/
```

**Symlink instead of copy** to pick up `git pull` updates automatically:

```bash
for d in /path/to/cyber-grc-agent-skills/skills/*/; do
  ln -s "$d" ~/.claude/skills/"$(basename "$d")"
done
```

Notes:

- Skills' relative links (`../../context/...`) resolve against the repo layout. Either work inside a clone of this repo, or also copy `context/` and `templates/` somewhere the agent can read and tell it where they are. Simplest reliable setup: open Claude Code **inside the cloned repo** — the root `CLAUDE.md` auto-loads and points the agent at [AGENTS.md](../../AGENTS.md), the layer model, and the validator.
- Trigger a skill implicitly by describing the task ("run a gap assessment against CIS v8") — the frontmatter description does the routing — or explicitly ("use the framework-gap-assessment skill").
- Curate if you don't need all 17 skills; fewer descriptions means cheaper, more accurate routing.

## 2. claude.ai Projects

For chat-based use without any tooling:

1. Create a Project.
2. Set the Project's custom instructions to the contents of one persona file from `agents/` (e.g. `agents/grc-analyst.md`).
3. Upload as project knowledge:
   - the `SKILL.md` files for the skills you need,
   - their `references/*.md` files,
   - the `context/` files those skills link to (e.g. `context/regulations/gdpr.md` for privacy work),
   - relevant `templates/` files.
4. Ask for the task in the skill's trigger language; the model retrieves the matching skill from project knowledge and follows it.

Curate per project — a "Privacy" project needs `dpia-privacy-assessment`, `incident-regulatory-reporting`, the GDPR/state-privacy/HIPAA context packs, and the DPIA template, not the SOC 2 material. Because uploaded files are flattened into a knowledge store, relative links between files won't be clickable; the file names still let the model ask for or find the right document, so keep the original filenames when uploading.

## 3. Claude API

Assemble the three layers into a request: persona as the system prompt, skill body injected alongside the task, context files added only as needed.

```python
import anthropic
from pathlib import Path

repo = Path("cyber-grc-agent-skills")
persona = (repo / "agents/risk-manager.md").read_text()
skill = (repo / "skills/risk-assessment/SKILL.md").read_text()
context = (repo / "context/risk-scoring.md").read_text()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-5",       # any current Claude model
    max_tokens=4096,
    system=persona,
    messages=[{
        "role": "user",
        "content": (
            "Follow this skill exactly, including its output format and "
            "quality checklist:\n\n<skill>\n" + skill + "\n</skill>\n\n"
            "Reference material:\n\n" + context + "\n\n"
            "Task: Assess cyber risks for our new customer-facing "
            "payments API and produce risk register entries."
        ),
    }],
)
print(response.content[0].text)
```

Practical notes:

- Load `SKILL.md` always; load `references/` and `context/` files only when the skill's procedure calls for them (progressive disclosure keeps prompts small). For multi-turn agents, resolve the skill's relative links to file paths and fetch on demand.
- Persona + skill + one or two context packs typically fits well under 30k tokens. If you cache, put the stable persona/skill blocks first and mark them for prompt caching.
- For a persistent agent, expose the repo via file tools and reproduce the routing rule from [AGENTS.md](../../AGENTS.md): scan frontmatter descriptions, load the match.

## 4. MCP (Model Context Protocol)

Any MCP-capable Claude surface (Claude Code, Claude Desktop, API with MCP connector) can serve this repo through a filesystem MCP server, letting the agent browse and load files itself instead of you injecting them:

```bash
# Example: reference filesystem server, scoped to the repo clone
npx -y @modelcontextprotocol/server-filesystem /path/to/cyber-grc-agent-skills
```

Register it in your client's MCP config (e.g. Claude Desktop's `claude_desktop_config.json` or `claude mcp add` in Claude Code), then instruct the agent — or let the root `CLAUDE.md`/`AGENTS.md` instruct it — to route via frontmatter descriptions and follow relative links on demand. Scope the server to the repo directory only; read-only is sufficient.

## Which one?

| You want | Use |
|---|---|
| Skills auto-loaded while working in a terminal/IDE | Claude Code |
| A no-code shared assistant for a GRC team | claude.ai Project |
| Skills embedded in your own product or pipeline | Claude API |
| An agent that self-serves files across surfaces | MCP filesystem server |

See also: [architecture.md](../architecture.md) for the three-layer model these setups implement, and [openai.md](openai.md) / [generic.md](generic.md) for other providers.
