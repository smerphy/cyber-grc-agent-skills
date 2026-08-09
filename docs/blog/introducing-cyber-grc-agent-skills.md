# Introducing Cyber GRC Agent Skills: teach your AI agent to do GRC work properly

*2026-08-09 · 8 min read*

Ask a capable LLM to "assess our gaps against ISO 27001" and you will get something that looks like a gap assessment. Look closer and the cracks show: control numbers that don't exist, a maturity scale invented mid-answer, findings with no evidence trail, and a confident tone that survives all of it. The model isn't incompetent — it's unmanaged. Nobody told it what a defensible gap assessment actually requires, so it improvised one.

[Cyber GRC Agent Skills](https://github.com/smerphy/cyber-grc-agent-skills) is our answer: an open-source, MIT-licensed library of **21 task skills, 49 framework and regulation knowledge packs, 23 multi-step workflows, 7 personas, and 11 deliverable templates** for cyber governance, risk, and compliance — written the way an experienced practitioner works, in plain markdown any AI provider can load.

## The problem: improvisation is the failure mode

GRC work punishes improvisation harder than almost any other domain an AI agent touches. A fabricated article number in a breach notification memo, a control tested against the wrong criteria, a risk score from a made-up matrix — these aren't style problems. They're the difference between analysis you can put in front of a regulator and analysis that creates new liability.

General-purpose models fail at GRC in predictable ways:

- **They fabricate specifics.** Article numbers, control IDs, notification deadlines — the more confident the prose, the less anyone checks.
- **They skip the procedure.** A real control test has a defined population, a sampling method, and a workpaper trail. An improvised one has vibes.
- **They can't tell you what they don't know.** "No evidence provided" should be a finding; an unmanaged model treats it as an invitation.
- **They drift with the regulations.** Compliance knowledge has a shelf life, and a model's training cutoff is nobody's review date.

None of this is fixed by a bigger model. It's fixed by giving the model the same things you'd give a new analyst: procedures, reference material, templates, and rules about what it may not make up.

## The design: three layers plus guardrails

The library follows the open [Agent Skills format](https://agentskills.io) — each skill is a `SKILL.md` procedure with progressive-disclosure references — organized in layers that compose per task instead of one monolithic prompt:

1. **Personas** (`agents/`) define *who the agent is*: a GRC analyst, a compliance officer, an internal auditor, a privacy officer — or the greybeard, a senior technical reviewer whose job is hunting fatal flaws in architectures and DR claims.
2. **Skills** (`skills/`) define *how a task is done*: framework gap assessment, risk assessment, control testing, DPIA, incident regulatory reporting, third-party risk, and sixteen more. Each is a step-by-step procedure with inputs to gather, a defined output format, and a quality checklist the agent runs before presenting results.
3. **Context and templates** (`context/`, `templates/`) define *what the agent needs to know and produce*: 19 framework packs (NIST CSF 2.0 through TISAX), 26 regulation packs (GDPR through India's DPDP Act), crosswalks, and deliverable skeletons.

On top sit **workflows** — 23 playbooks that chain skills through multi-phase engagements with explicit decision gates, named roles per step, and a failure-modes section drawn from real practice. There's a workflow for running a penetration test end to end, one for managing a regulator examination (counsel first, single point of contact, never volunteer beyond scope), one for M&A security due diligence, one for the quarterly board reporting cycle, and nineteen more across security review, assurance, privacy, and resilience.

And because a report worth reading is worth formatting: a **branding layer** lets you drop in your logo, palette, and tone once, and every formatted deliverable applies them. Four report styles ship in the box, defaulting to a strategy-consulting format — answer-first structure, action titles, a one-page executive summary — with alternates for audit-house findings reports, TL;DR-first tech docs, and numbered-paragraph regulator filings.

## The rules that make it trustworthy

The content is only half the library. The other half is the discipline around it:

- **Anti-fabrication by construction.** Skills instruct the agent to tie every conclusion to named evidence and to flag uncertainty instead of papering over it. Regulatory specifics appear only where they're verifiable; everywhere else the instruction is explicit: *verify against the official text*.
- **Primary sources, verified.** Every framework and regulation pack ends with links to the official text — checked at review time, not pasted from memory.
- **Freshness is tracked, not assumed.** Every pack carries a "Last reviewed" date and a verification footer. A monthly automation flags packs going stale; `--stale N` reports them locally.
- **Everything is validated.** A CI-enforced validator checks skill structure, all 1,700+ cross-file links, verification footers, workflow headers, and the sync between the human-readable breach-notification matrix and its machine-readable counterpart. A broken link or a drifted deadline fails the build.
- **The advice itself is regression-tested.** An eval harness holds scenarios with machine-gradable rubrics — required findings *and forbidden wrong claims* (like "you can file a GDPR notification next week"). Change the content, rerun the evals, catch the regression.

## More than markdown

Some GRC facts deserve to be computed, not recalled. The library ships a machine-readable dataset of breach-notification deadlines across every covered regime — each with its clock-start semantics, because GDPR's 72 hours from *awareness* and the SEC's four business days from *materiality determination* are different clocks entirely. A stdlib-only calculator turns incident timestamps into a sorted deadline table, and an MCP server exposes the whole library — skills, search, deadline computation — as native tools to any MCP client.

## Does it work at a sane cost?

Yes. Progressive disclosure keeps token cost proportional to the task: an agent loads one persona, one skill, and only the context files the skill links to — typically 15–20K tokens of loadout, on the order of **$0.10–0.15 per substantive task** on a mid-tier model. Bulk-loading the repository is explicitly against the operating rules, and the architecture makes the right thing the cheap thing.

## Get started in one command

For Claude Code:

```
/plugin marketplace add smerphy/cyber-grc-agent-skills
/plugin install cyber-grc@cyber-grc-skills
```

Then just ask: *"assess our gaps against ISO 27001"*, *"we found unauthorized access to a customer database Thursday night — what are our notification obligations?"*, *"review this vendor's SOC 2 report"*. Skills auto-trigger from their descriptions.

Every other path is documented too: [claude.ai Projects](../integrations/claude.md), [Custom GPTs and the OpenAI API](../integrations/openai.md) with pre-built per-persona bundles, [any provider via plain prompt assembly](../integrations/generic.md), or the [MCP server](../integrations/mcp.md).

## What this is not

It is not legal advice, and it says so — output produced with these skills is analysis support, with counsel review recommended for legal interpretation, notification decisions, and regulator interaction. It is not a GRC platform; it's the missing procedural layer for the AI agents you already use. And it is not finished: regulations change monthly, and the maintenance model is built for that.

## Contribute

The accuracy bar is the contribution bar: primary-sourced claims, verification footers, validator-clean PRs. If you know a regime we hedged on, a framework we haven't covered, or a workflow your team runs that ours doesn't capture — [contributions are open](https://github.com/smerphy/cyber-grc-agent-skills/blob/main/CONTRIBUTING.md).

Start here: [README](https://github.com/smerphy/cyber-grc-agent-skills) · [architecture](../architecture.md) · [the skills catalog](https://github.com/smerphy/cyber-grc-agent-skills#skills)

---

*Cyber GRC Agent Skills is MIT-licensed and provider-neutral. Nothing in this post or the library constitutes legal advice.*
