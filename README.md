# Cyber GRC Agent Skills

Portable, provider-neutral AI agent skills for cyber Governance, Risk & Compliance. Load them into Claude, ChatGPT, or any capable LLM and get an agent that runs gap assessments, maps controls across frameworks, determines breach notification obligations, drafts policies, prepares audits, and more — following practitioner-grade procedures instead of improvising.

Everything is plain markdown in the open [Agent Skills format](https://agentskills.io) (`SKILL.md` + progressive-disclosure references). No provider lock-in, no runtime dependencies, no API keys.

## What's inside

```
agents/       6 persona system prompts (GRC analyst, compliance officer, risk manager,
              internal auditor, privacy officer, AI governance lead)
skills/       17 task skills, each a SKILL.md procedure + references/ deep material
context/      Shared knowledge packs: 6 frameworks, 10 regulation files, crosswalks,
              glossary, risk-scoring methods
workflows/    8 multi-step playbooks chaining skills with decision gates
templates/    11 deliverable skeletons (risk register, DPIA, SoA, workpapers, ...)
docs/         Integration guides (Claude, OpenAI, generic) and architecture notes
scripts/      Validator for skill format and cross-file links (runs in CI)
```

### Skills

| Skill | What it does |
|---|---|
| [framework-gap-assessment](skills/framework-gap-assessment/SKILL.md) | Assess current state against NIST CSF 2.0, ISO 27001, CIS v8, SOC 2, 800-53, or PCI DSS; score maturity; produce a gap report and roadmap |
| [control-mapping](skills/control-mapping/SKILL.md) | Map controls across frameworks and from internal control sets, with partial-coverage ratings |
| [policy-authoring](skills/policy-authoring/SKILL.md) | Draft policies/standards/procedures with testable statements traced to framework controls |
| [policy-review](skills/policy-review/SKILL.md) | Review existing policies for testability, coverage, conflicts, and currency |
| [risk-assessment](skills/risk-assessment/SKILL.md) | Run a cyber risk assessment and write well-formed risk register entries |
| [exception-management](skills/exception-management/SKILL.md) | Process policy/control exceptions with risk-based approval, compensating controls, and expiry |
| [third-party-risk-assessment](skills/third-party-risk-assessment/SKILL.md) | Tier vendors, analyze questionnaires and SOC 2 reports, set contract requirements and monitoring |
| [grc-metrics-reporting](skills/grc-metrics-reporting/SKILL.md) | Design decision-driving KPIs/KRIs and board-level risk reporting |
| [audit-preparation](skills/audit-preparation/SKILL.md) | Build PBC lists, review evidence quality, and prep control owners for audit |
| [control-testing](skills/control-testing/SKILL.md) | Test control design and operating effectiveness with proper sampling and workpapers |
| [incident-regulatory-reporting](skills/incident-regulatory-reporting/SKILL.md) | Determine notification obligations after an incident, compute deadlines per regime, draft notifications |
| [regulatory-applicability](skills/regulatory-applicability/SKILL.md) | Determine which regulations and frameworks apply to an organization, with rationale |
| [dpia-privacy-assessment](skills/dpia-privacy-assessment/SKILL.md) | Screen for and conduct GDPR Art. 35 DPIAs focused on risks to individuals |
| [ai-governance](skills/ai-governance/SKILL.md) | Inventory and classify AI systems (EU AI Act), assess against NIST AI RMF, define AI controls |
| [soc2-readiness](skills/soc2-readiness/SKILL.md) | Prepare for SOC 2 Type I/II: criteria selection, system description, CC mapping, evidence dry run |
| [iso27001-readiness](skills/iso27001-readiness/SKILL.md) | Prepare for ISO 27001:2022 certification: ISMS scope, clauses 4–10, Statement of Applicability |
| [regulatory-horizon-scanning](skills/regulatory-horizon-scanning/SKILL.md) | Track upcoming regulatory change from authoritative sources and triage impact |

### Coverage

**Frameworks:** NIST CSF 2.0 · ISO/IEC 27001:2022 · CIS Controls v8/v8.1 · SOC 2 (TSC) · NIST SP 800-53 r5 (+800-171/CMMC notes) · PCI DSS v4 · NIST AI RMF · ISO/IEC 42001

**Regulations & laws:** EU GDPR · NIS2 · DORA · EU AI Act · HIPAA · CCPA/CPRA and US state privacy & breach laws · SOX (ITGC) · SEC cyber disclosure rules · GLBA / FTC Safeguards Rule · UK, Australia (APRA CPS 234, SOCI), Canada, Singapore, Brazil, China, Japan, India summaries

**Crosswalks:** domain-level control crosswalk across the six frameworks; breach-notification deadline matrix across all covered regimes.

## Quick start

### Claude Code

```bash
git clone https://github.com/smerphy/Cyber-GRC-Agent-Skills.git
# All skills, project-scoped:
mkdir -p .claude/skills && cp -r Cyber-GRC-Agent-Skills/skills/* .claude/skills/
# Or a single skill, user-scoped:
cp -r Cyber-GRC-Agent-Skills/skills/risk-assessment ~/.claude/skills/
```

Skills auto-trigger from their `description` frontmatter ("assess our gaps against ISO 27001" loads `framework-gap-assessment`). Details: [docs/integrations/claude.md](docs/integrations/claude.md).

### claude.ai (Projects)

Create a Project, set a persona from `agents/` as project instructions, upload the `SKILL.md` and `references/` files for the skills you need plus the `context/` files they link to.

### ChatGPT (Custom GPT) / OpenAI API

Custom GPT: paste a persona from `agents/` into Instructions; upload the relevant skills and context packs as knowledge files (curate per GPT — don't upload the whole repo). API: put persona + `SKILL.md` in the system/developer message, or index the repo into a vector store for file search. Details: [docs/integrations/openai.md](docs/integrations/openai.md).

### Any other provider

The three-layer assembly works in a plain prompt:

```
[system]  contents of agents/grc-analyst.md
[system]  contents of skills/incident-regulatory-reporting/SKILL.md
[user]    reference: contents of context/crosswalks/breach-notification-timelines.md
[user]    We detected unauthorized access to our EU customer database at 02:00 UTC today. <details...>
```

Details and RAG/chunking guidance: [docs/integrations/generic.md](docs/integrations/generic.md).

## Design

- **Three layers.** Personas define *who the agent is*, skills define *how a task is done*, context/templates define *what it needs to know and produce*. Compose them per task instead of one monolithic prompt.
- **Progressive disclosure.** Each `SKILL.md` stays small enough to load whole; depth (question banks, rubrics, per-regime detail) lives in `references/` and `context/` files loaded on demand. This keeps token cost proportional to the task.
- **Provider-neutral content.** No tool syntax, no vendor-specific markup anywhere in `skills/`, `context/`, `workflows/`, `agents/`, or `templates/`. Provider specifics are quarantined in `docs/integrations/`.
- **Anti-fabrication by construction.** Skills instruct the agent to tie conclusions to evidence, flag uncertainty, and never invent citations or compliance status. Regulatory files carry a `Last reviewed` date and a verification footer.
- **Validated.** `python3 scripts/validate_skills.py` checks frontmatter, required sections, and that every cross-file link resolves; it runs in CI on every PR.

Full rationale: [docs/architecture.md](docs/architecture.md).

## Workflows

For multi-phase engagements, `workflows/` chains skills with explicit decision gates: [new-regulation impact assessment](workflows/new-regulation-impact-assessment.md), [annual risk assessment](workflows/annual-risk-assessment.md), [vendor onboarding](workflows/vendor-onboarding.md), [audit readiness](workflows/audit-readiness.md), [incident regulatory response](workflows/incident-regulatory-response.md), [policy lifecycle](workflows/policy-lifecycle.md), [certification readiness](workflows/certification-readiness.md), and [AI system intake](workflows/ai-system-intake.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: follow the skill format, run the validator, never fabricate citations, update `Last reviewed` dates when touching regulatory content, and cite the official source in your PR. Do not contribute verbatim text from licensed standards (ISO, PCI DSS) — summaries and structure only.

## Important limitations

- **Not legal advice.** This library supports analysis; it does not replace qualified counsel. Notification decisions, regulator interaction, and legal interpretation need lawyer review.
- **Regulations change.** Content reflects public sources as of the `Last reviewed` date in each file (initial release: 2026-07). Verify deadlines, thresholds, and penalties against official texts before relying on them.
- **LLMs make mistakes.** These skills reduce, but cannot eliminate, model error. Keep a human accountable for every compliance decision.

## License

[MIT](LICENSE). Framework and regulation names belong to their respective owners; this repository contains original summaries and procedures, not reproductions of licensed standard text.
