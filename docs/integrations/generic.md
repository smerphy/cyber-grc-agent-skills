# Using this repository with any LLM provider

Everything in this repo is plain markdown written in the imperative, so any capable instruction-following model can execute it — Gemini, Mistral, Llama, Qwen, DeepSeek, or anything behind an OpenAI-compatible endpoint. This page is the provider-agnostic pattern; [claude.md](claude.md) and [openai.md](openai.md) specialize it.

## The three-layer model

Assemble every session from three layers, top-down:

```
1. PERSONA    agents/<role>.md              → system prompt: who the agent is
2. SKILL      skills/<task>/SKILL.md        → the procedure: what to do, output format, QA checklist
3. KNOWLEDGE  context/*, templates/*,       → facts and skeletons: loaded only when
              skills/<task>/references/*      the skill's procedure calls for them
```

Rules of thumb:

- Exactly one persona per session.
- One skill at a time; workflows in `workflows/` tell you which skills to chain for multi-phase engagements.
- Layer 3 is pull, not push: the skill's links tell you which context/reference files matter. Loading all of `context/` up front wastes tokens and dilutes attention.

## Minimal prompt assembly recipe

1. Pick the persona matching the user's role → system (or first) message.
2. Pick the skill whose frontmatter `description` matches the task → inject its full body.
3. Read the skill's References section; inject only the context files the task actually touches.
4. State the task, then let the skill's "Inputs to gather" section drive what the agent asks for.

Copy-paste template:

```text
[system message]
<paste agents/grc-analyst.md>

[user message]
Follow this skill exactly — its Procedure step by step, its Output format for
the deliverable, and its Quality checklist before you present results:

--- SKILL ---
<paste skills/framework-gap-assessment/SKILL.md>
--- END SKILL ---

Reference material (use it; do not restate it):

--- CONTEXT: cis-controls-v8 ---
<paste context/frameworks/cis-controls-v8.md>
--- END CONTEXT ---

Task: Assess our current controls against CIS Controls v8 at IG2. I will
provide our control inventory when you ask for inputs.
```

If a linked file isn't loaded, instruct the agent to ask for it by path rather than guess at its contents. That single rule prevents most fabrication.

## RAG / retrieval guidance

If you index the repo into a vector store instead of pasting files:

- **Chunk on H2 boundaries.** Every content file uses `##` sections as its unit of meaning (a skill's Procedure, a regulation's notification rules). Split there; a fixed 500-token splitter will cut procedures mid-step.
- **Keep tables intact.** Crosswalks, deadline matrices, and scoring tables lose their meaning when a row is separated from its header. Treat a markdown table as an atomic chunk even when oversized.
- **Prepend file path + H1 to each chunk** (`context/regulations/nis2.md > Reporting obligations`) so retrieved fragments stay attributable and the model can request the full file.
- **Retrieve skills whole.** A skill is a procedure; executing step 4 without steps 1–3 produces confident nonsense. Use retrieval to *find* the right `SKILL.md`, then load the entire file. Chunked retrieval is for `context/` and `references/`.
- Index frontmatter descriptions separately as a routing table — they are written precisely for match-the-task retrieval.

## Token budgeting

Typical sizes (order of magnitude): persona 1–3k tokens, SKILL.md 2–5k, context pack 3–8k, reference file 3–10k.

| Priority | Load | When |
|---|---|---|
| Always | Persona + the one matching SKILL.md | Session start |
| On demand | Context files from the skill's References | When the procedure step needs the fact |
| On demand | `references/*.md` | When the procedure links them (question banks, rubrics) |
| Rarely | A second skill | Only at a workflow hand-off; drop the finished skill first |

Working budget for an 8k-context local model: persona + skill fits (~5–8k) but leaves no room for user documents — summarize context packs offline or use retrieval. At 32k+, persona + skill + two context packs + a user document is comfortable. Long-context models can hold a whole workflow's file set, but selective loading still improves instruction-following.

## Local / open-weight models

- The skills assume competent instruction-following and long-form structured output. Strong recent 30B+ open-weight instruct models handle them; small models tend to skip Procedure steps and drift from the Output format — re-inject the Output format section right before generation if you see drift.
- Quality checklists double as self-critique prompts: after the draft, send "Evaluate your output against the skill's Quality checklist; fix failures" as a second turn. This recovers much of the gap on smaller models.
- Never let a model answer regulatory specifics from its weights alone: deadlines and article numbers must come from a loaded `context/` file or be flagged as unverified. This rule matters *more* for local models with older or thinner training data.
- Every file ends its regulatory content with a last-reviewed footer — surface it to users when currency matters.

## See also

- [architecture.md](../architecture.md) — why the repo is structured this way
- [claude.md](claude.md) — Claude Code auto-loading, Projects, API, MCP
- [openai.md](openai.md) — Custom GPTs, vector stores, AGENTS.md convention
- [AGENTS.md](../../AGENTS.md) — the in-repo operating rules any agent should follow
