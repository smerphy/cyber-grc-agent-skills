#!/usr/bin/env python3
"""MCP (Model Context Protocol) server for the Cyber GRC Agent Skills library.

Exposes the repository to any MCP-speaking client (Claude Desktop, Claude
Code, Cursor, ...) as five tools over stdio JSON-RPC:

  list_skills        - skill names + trigger descriptions
  get_skill          - full SKILL.md (optionally a reference file) for one skill
  get_file           - any markdown/CSV file in the repo by relative path
  search             - case-insensitive text search across the content dirs
  compute_deadlines  - regulatory notification deadlines from incident
                       timestamps (wraps scripts/deadline_calc.py)

Stdlib only. Register it from a client config (see .mcp.json.example):

  {"mcpServers": {"cyber-grc": {"command": "python3",
                                 "args": ["/path/to/repo/scripts/mcp_server.py"]}}}
"""

import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import deadline_calc  # noqa: E402

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "cyber-grc", "version": "1.2.0"}
CONTENT_DIRS = ("skills", "context", "workflows", "agents", "templates", "docs", "examples")
ALLOWED_EXT = (".md", ".csv", ".txt", ".json")

TOOLS = [
    {
        "name": "list_skills",
        "description": "List every Cyber GRC skill with its trigger description. Use first to find the right skill for a task.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "get_skill",
        "description": "Get a skill's full SKILL.md procedure, or one of its reference files. Load the SKILL.md before performing the task it covers.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "skill directory name, e.g. risk-assessment"},
                "reference": {"type": "string", "description": "optional references/ filename, e.g. scenario-library.md"},
            },
            "required": ["name"],
        },
    },
    {
        "name": "get_file",
        "description": "Read any content file by repo-relative path, e.g. context/regulations/gdpr.md or templates/risk-register.csv.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "repo-relative path"}},
            "required": ["path"],
        },
    },
    {
        "name": "search",
        "description": "Case-insensitive text search across skills, context packs, workflows, templates, personas, docs, and examples. Returns file paths with matching lines.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "description": "max matching files (default 10)"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "compute_deadlines",
        "description": "Compute regulatory breach/incident notification deadlines from incident timestamps, honoring each regime's clock-start semantics (awareness vs determination vs materiality determination). Call with no arguments to list available regime ids and their clock events.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "regimes": {"type": "array", "items": {"type": "string"},
                            "description": "regime ids, e.g. [\"gdpr\", \"nis2\", \"sec-8k\"]"},
                "when": {"type": "object",
                         "description": "clock-start timestamps, e.g. {\"awareness\": \"2026-07-14T06:40Z\", \"materiality_determination\": \"2026-07-16T17:00Z\"}",
                         "additionalProperties": {"type": "string"}},
            },
        },
    },
]


def safe_path(rel):
    resolved = os.path.realpath(os.path.join(REPO_ROOT, rel))
    if not resolved.startswith(os.path.realpath(REPO_ROOT) + os.sep):
        raise ValueError("path escapes the repository")
    top = os.path.relpath(resolved, REPO_ROOT).split(os.sep)[0]
    if top not in CONTENT_DIRS and os.path.dirname(os.path.relpath(resolved, REPO_ROOT)):
        raise ValueError(f"path must be under one of: {', '.join(CONTENT_DIRS)} (or a root file)")
    if not resolved.endswith(ALLOWED_EXT):
        raise ValueError(f"only {', '.join(ALLOWED_EXT)} files are served")
    if not os.path.isfile(resolved):
        raise ValueError(f"no such file: {rel}")
    return resolved


def tool_list_skills(_args):
    out = []
    skills_dir = os.path.join(REPO_ROOT, "skills")
    for entry in sorted(os.listdir(skills_dir)):
        skill_md = os.path.join(skills_dir, entry, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        with open(skill_md, encoding="utf-8") as f:
            text = f.read()
        m = re.search(r"^description:\s*>-?\s*\n((?:[ ]+.+\n)+)", text, re.M)
        desc = " ".join(line.strip() for line in m.group(1).splitlines()) if m else ""
        out.append(f"## {entry}\n{desc}")
    return "\n\n".join(out)


def tool_get_skill(args):
    name = args["name"]
    if args.get("reference"):
        rel = os.path.join("skills", name, "references", os.path.basename(args["reference"]))
    else:
        rel = os.path.join("skills", name, "SKILL.md")
    with open(safe_path(rel), encoding="utf-8") as f:
        return f.read()


def tool_get_file(args):
    with open(safe_path(args["path"]), encoding="utf-8") as f:
        return f.read()


def tool_search(args):
    query = args["query"].lower()
    max_results = int(args.get("max_results", 10))
    hits = []
    for dir_name in CONTENT_DIRS:
        base = os.path.join(REPO_ROOT, dir_name)
        if not os.path.isdir(base):
            continue
        for root, _dirs, files in os.walk(base):
            for fname in sorted(files):
                if not fname.endswith((".md", ".csv")):
                    continue
                path = os.path.join(root, fname)
                rel = os.path.relpath(path, REPO_ROOT)
                with open(path, encoding="utf-8", errors="replace") as f:
                    matches = [f"  L{i}: {line.strip()[:200]}"
                               for i, line in enumerate(f, 1) if query in line.lower()]
                if matches:
                    hits.append(f"{rel} ({len(matches)} match(es))\n" + "\n".join(matches[:5]))
                if len(hits) >= max_results:
                    return "\n\n".join(hits) + "\n\n(result cap reached)"
    return "\n\n".join(hits) if hits else f"No matches for '{args['query']}'."


def tool_compute_deadlines(args):
    regimes = deadline_calc.load_regimes()
    ids = args.get("regimes") or []
    when_raw = args.get("when") or {}
    if not ids:
        lines = ["Available regimes (pass ids in `regimes`):"]
        for rid, r in sorted(regimes.items()):
            bases = sorted({d["basis"] for d in r["deadlines"] if d["type"] != "text"})
            lines.append(f"- {rid}: {r['name']}" + (f" — clock events: {', '.join(bases)}" if bases else ""))
        return "\n".join(lines)
    when = {k: deadline_calc.parse_ts(v) for k, v in when_raw.items()}
    rows = deadline_calc.build_rows(ids, when, regimes)
    return deadline_calc.render(rows, when)


HANDLERS = {
    "list_skills": tool_list_skills,
    "get_skill": tool_get_skill,
    "get_file": tool_get_file,
    "search": tool_search,
    "compute_deadlines": tool_compute_deadlines,
}


def handle(request):
    method = request.get("method")
    rid = request.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": request.get("params", {}).get("protocolVersion", PROTOCOL_VERSION),
            "capabilities": {"tools": {}},
            "serverInfo": SERVER_INFO,
        }}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = request.get("params", {})
        name = params.get("name")
        handler = HANDLERS.get(name)
        if handler is None:
            return {"jsonrpc": "2.0", "id": rid,
                    "error": {"code": -32602, "message": f"unknown tool: {name}"}}
        try:
            text = handler(params.get("arguments") or {})
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"content": [{"type": "text", "text": text}]}}
        except Exception as exc:  # tool errors go back as tool results, not protocol errors
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"content": [{"type": "text", "text": f"ERROR: {exc}"}],
                               "isError": True}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if rid is None:  # notification (e.g. notifications/initialized) — no response
        return None
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": f"method not found: {method}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue
        response = handle(request)
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
