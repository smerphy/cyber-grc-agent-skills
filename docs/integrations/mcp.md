# Using this repository as an MCP server

`scripts/mcp_server.py` exposes the library over the [Model Context Protocol](https://modelcontextprotocol.io) — stdio JSON-RPC, Python stdlib only, no dependencies, no network calls. Any MCP client (Claude Desktop, Claude Code, Cursor, and others) can then browse skills, pull context packs, search the corpus, and compute notification deadlines as native tools.

## Setup

Clone the repo, then register the server in your client's MCP config (see [.mcp.json.example](../../.mcp.json.example)):

```json
{
  "mcpServers": {
    "cyber-grc": {
      "command": "python3",
      "args": ["/absolute/path/to/Cyber-GRC-Agent-Skills/scripts/mcp_server.py"]
    }
  }
}
```

- **Claude Code:** place this as `.mcp.json` in your project root, or add via `claude mcp add cyber-grc -- python3 /path/to/scripts/mcp_server.py`.
- **Claude Desktop:** merge into `claude_desktop_config.json`.
- Requires Python 3.10+ on PATH.

## Tools exposed

| Tool | What it does |
|---|---|
| `list_skills` | Every skill with its trigger description — the entry point |
| `get_skill` | A skill's full `SKILL.md`, or one of its `references/` files |
| `get_file` | Any content file by repo-relative path (`context/regulations/gdpr.md`, `templates/risk-register.csv`, …) |
| `search` | Case-insensitive text search across skills, context, workflows, templates, personas, docs, examples |
| `compute_deadlines` | Concrete notification deadlines from incident timestamps, honoring per-regime clock-start semantics — wraps [`scripts/deadline_calc.py`](../../scripts/deadline_calc.py) and [`data/breach-timelines.json`](../../data/breach-timelines.json); call with no arguments to list regime ids |

Example `compute_deadlines` call an agent might make during an incident:

```json
{
  "regimes": ["gdpr", "nis2", "sec-8k"],
  "when": {
    "awareness": "2026-07-14T06:40Z",
    "materiality_determination": "2026-07-16T17:00Z"
  }
}
```

Returns a markdown deadline table sorted by due time, with hedged regimes flagged ⚠ for verification. Business-day math skips weekends only (not holidays); everything remains analysis support, not legal advice.

## Security notes

- The server only reads files inside the repository's content directories, only `.md/.csv/.txt/.json`, and rejects path traversal.
- It makes no network calls and executes nothing; the only write surface is stdout.
