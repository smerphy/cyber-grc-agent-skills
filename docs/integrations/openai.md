# Using this repository with OpenAI

Four ways to run these skills on OpenAI's stack. The content is provider-neutral markdown; these are the assembly mechanics. See [generic.md](generic.md) for the underlying pattern.

## 0. Pre-built bundles (fastest path)

`python3 scripts/build_bundles.py` generates per-persona knowledge bundles under `dist/`: a full variant and a `-gpt20` variant capped at 20 files for Custom GPT knowledge limits (SKILL.md files and linked context packs are kept; deep reference files are dropped first, and every bundle's `MANIFEST.md` lists what was omitted and where to find it). Use the bundle's `agents__<persona>.md` as the Instructions text and upload the rest as knowledge files.

## 1. Custom GPTs

Build one GPT per role or engagement type, not one giant GPT for the whole repo.

1. **Instructions:** paste one persona file from `agents/` (e.g. `agents/compliance-officer.md`) into the GPT's Instructions. Append a routing rule:

   > You have skill files in your knowledge. When a task matches a skill's description, retrieve that SKILL.md and follow its Procedure, Output format, and Quality checklist exactly. Retrieve a skill's reference files or context files only when the procedure directs you to. Never invent regulatory citations; if a specific is not in your knowledge, say so.

2. **Knowledge:** upload the `SKILL.md` files, their `references/`, and the `context/` and `templates/` files those skills link to.
3. **Capabilities:** enable Code Interpreter if you want the GPT to fill CSV templates (e.g. `templates/risk-register.csv`); web browsing helps for `regulatory-horizon-scanning`.

**File-count limits force curation.** Custom GPT knowledge is capped at roughly 20 files (verify the current limit in OpenAI's docs). This repo contains far more than 20 markdown files, so build focused GPTs:

| GPT | Suggested knowledge (~files) |
|---|---|
| Privacy assistant | `dpia-privacy-assessment` + `incident-regulatory-reporting` SKILL.md + references; `context/regulations/gdpr.md`, `us-state-privacy.md`, `hipaa.md`; `context/crosswalks/breach-notification-timelines.md`; `templates/dpia-template.md` |
| Audit & certification | `soc2-readiness`, `iso27001-readiness`, `audit-preparation`, `control-testing` SKILL.md + key references; `context/frameworks/soc2-tsc.md`, `iso-27001-2022.md` |
| Risk office | `risk-assessment`, `third-party-risk-assessment`, `exception-management`, `grc-metrics-reporting` SKILL.md + references; `context/risk-scoring.md`; `templates/risk-register-guide.md` |

If you must squeeze under the limit, concatenate each skill with its references into a single file per skill (keep the H1/H2 structure intact so retrieval still lands on the right section).

## 2. Assistants / Responses API with file search

For programmatic use, upload the repo (or a curated subset) as a vector store and attach the `file_search` tool. Persona goes in `instructions`; skills and context are retrieved on demand.

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()
repo = Path("cyber-grc-agent-skills")

# One-time: build the vector store from skills + context + templates
paths = [p for d in ("skills", "context", "templates", "workflows")
         for p in (repo / d).rglob("*.md")]
store = client.vector_stores.create(name="cyber-grc-skills")
client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=store.id,
    files=[open(p, "rb") for p in paths],
)

# Per request
persona = (repo / "agents/grc-analyst.md").read_text()
response = client.responses.create(
    model="gpt-4.1",  # any current model with file_search support
    instructions=persona + "\n\nWhen a task matches a skill, retrieve its "
        "SKILL.md via file search and follow its Procedure, Output format, "
        "and Quality checklist. Retrieve references/context files only when "
        "the skill directs you to. Never invent regulatory citations.",
    tools=[{"type": "file_search", "vector_store_ids": [store.id]}],
    input="Run a gap assessment of our controls against CIS Controls v8, IG2.",
)
print(response.output_text)
```

Notes:

- Markdown uploads chunk well by default, but retrieval quality improves if you keep original filenames — the skill routing language ("framework-gap-assessment") then matches the source file.
- For highest fidelity on a known task, skip retrieval for the skill itself: inject the full `SKILL.md` into the input (pattern below) and use file search only for context packs.

## 3. Plain chat (no tooling)

Works in ChatGPT or any API call. Paste the persona into the system/developer message and the skill into the first user message:

```text
[system / developer]
<contents of agents/risk-manager.md>

[user]
Follow this skill exactly, including its Output format and Quality checklist:

<contents of skills/third-party-risk-assessment/SKILL.md>

Reference material:

<contents of context files the skill links to, as needed>

Task: Assess vendor XYZ, a SaaS payroll provider processing employee PII...
```

If the skill's procedure links a `references/` file you did not paste, the model will tell you it is missing — paste it in a follow-up turn rather than front-loading everything.

## 4. AGENTS.md convention (Codex and compatible agents)

The repo root contains an [AGENTS.md](../../AGENTS.md) following the open AGENTS.md convention. Coding/CLI agents that honor it (OpenAI Codex, and other tools adopting the convention) automatically read it when operated inside a clone of this repo, and receive the layer model, the skill-routing rule, and the accuracy rules with no further setup:

```bash
git clone https://github.com/<org>/cyber-grc-agent-skills.git
cd cyber-grc-agent-skills
codex   # or any AGENTS.md-aware agent; then just describe the GRC task
```

This is the lowest-friction option for terminal-based OpenAI agents: relative links between skills, context, and templates all resolve because the agent is working inside the real directory tree.

## Which one?

| You want | Use |
|---|---|
| A shared no-code assistant for a team | Custom GPT (curated per role) |
| Skills in your own product/pipeline with retrieval | Responses API + vector store |
| Quick one-off task, zero setup | Plain chat paste |
| Terminal agent working in the repo | AGENTS.md + Codex-style agent |

See also: [claude.md](claude.md), [generic.md](generic.md), and [architecture.md](../architecture.md).
