# Repository architecture

How this repository is designed, why, and the rules every file follows. Read this before contributing content; read [CONTRIBUTING.md](../CONTRIBUTING.md) for the mechanics of submitting a change.

## Design goals

1. **Portable.** Every content file is plain markdown that works in any capable LLM agent — Claude, ChatGPT, Gemini, local models. No provider-specific syntax, no tool names, no XML control tags. Provider-specific setup lives only in [docs/integrations/](integrations/generic.md).
2. **Progressive disclosure.** An agent should never need to load the whole repository. Each layer is small enough to load on demand, and each file tells the agent exactly which other files to pull and when.
3. **Practitioner-grade accuracy.** Regulatory and framework specifics are either precise and verifiable or deliberately generic. Nothing is invented. Every file carrying such specifics ends with a verification footer and a last-reviewed date.

## The Agent Skills open format

Skills follow the Agent Skills format: a directory per skill containing a `SKILL.md` with YAML frontmatter plus optional `references/` files.

```
skills/risk-assessment/
├── SKILL.md            # frontmatter + procedure, < 500 lines
└── references/
    ├── scenario-library.md
    └── risk-statement-patterns.md
```

The frontmatter is the loading contract:

```yaml
---
name: risk-assessment          # must equal the directory name
description: >-                # 100-1024 chars; what it does AND when to use it,
  ...                          # including trigger phrases — this is all an agent
license: MIT                   # reads before deciding to load the skill
metadata:
  version: "1.0.0"
  domain: cyber-grc
---
```

Why this format:

- **The description is the router.** Agents scan frontmatter descriptions cheaply, then load only the matching skill body. This is why descriptions must state trigger phrases ("gap assessment", "map controls to...") rather than marketing copy.
- **The body is the working set.** `SKILL.md` targets 150–350 lines and never exceeds 450 — small enough to sit in context alongside the user's actual documents.
- **`references/` is the third tier.** Question banks, per-framework tables, and worked examples go there. The procedure links to them; the agent fetches them only when a step requires it. A reference file is self-contained (own H1, no frontmatter) and can be long (200–600 lines).

## Directory layout

| Path | Contents |
|---|---|
| `agents/` | Persona files: system-prompt role definitions (GRC analyst, compliance officer, risk manager, internal auditor, privacy officer, AI governance lead) |
| `skills/<name>/SKILL.md` | One procedure per skill, in the format above |
| `skills/<name>/references/` | Deep supporting material for that skill only |
| `context/README.md` | Index of all 105 context packs, grouped by region and framework family — the way into the knowledge layer |
| `context/frameworks/` | 40 framework and standard packs: the NIST family, ISO/IEC, audit and attestation schemes, payments and financial sector, cloud and government assurance, OT, and threat-informed baselines |
| `context/regulations/` | 65 regulation packs: EU, UK, US federal and state, Asia-Pacific, the Americas, rest of Europe, Middle East and Africa, plus the global jurisdiction index in `other-jurisdictions.md` |
| `context/crosswalks/` | Cross-framework mappings and the breach-notification deadline matrix |
| `context/glossary.md`, `context/risk-scoring.md` | Shared terminology and scoring method notes |
| `workflows/` | Multi-phase playbooks that chain several skills with decision gates |
| `templates/` | Deliverable skeletons (risk register, DPIA, policy, workpapers) |
| `docs/` | Human-facing documentation: this file plus per-provider integration guides |
| `scripts/` | Contributor tooling — currently the validator |

## The three-layer model

```
Layer 1: PERSONA   (agents/*.md)          — who the agent is: role, tone, boundaries
Layer 2: SKILL     (skills/*/SKILL.md)    — what to do: procedure, output format, QA checklist
Layer 3: KNOWLEDGE (context/, templates/, skills/*/references/)
                                          — what to know: framework facts, deadlines, skeletons
```

A working session is assembled top-down: pick one persona, load the skill matching the task, then pull only the knowledge files that skill links to. Layers are strictly separated:

- Personas contain **no procedures** — they set role and judgment norms.
- Skills contain **no framework fact dumps** — they link to `context/` instead of restating control counts or article numbers. One-line anchors (e.g. "NIS2 requires a 24-hour early warning") are fine when they drive a decision step; the authoritative detail lives in the context pack.
- Context packs contain **no procedures** — they are reference material, deliberately reusable by every skill.

This separation is what keeps 17 skills and 105 context packs from becoming 17 copies of the same GDPR summary — and what keeps a regulatory change a one-file fix.

## Context pack structure

A context pack is one instrument — a law, rule, framework, standard or scheme — in one file: `context/regulations/<name>.md` for a legal instrument, `context/frameworks/<name>.md` for a framework or assurance scheme. The library holds 105 of them. A pack has no frontmatter, starts with its own H1 (the instrument's full name plus its citation, e.g. "EU Data Act (Regulation (EU) 2023/2854)"), and contains facts only — the procedure that uses those facts belongs in a skill.

Every pack follows the same section set, in this order:

| Section | Contents |
|---|---|
| `## At a glance` | Attribute/detail table: instrument and citation, regulator or publisher, status and key dates, who is covered, structure, penalties or assessment model, relationship to neighbouring regimes |
| `## What it is` | What the instrument does and why it exists |
| `## Who it covers / Scope` | The coverage tests, including extraterritorial reach, thresholds and exclusions |
| `## Core obligations` | The substantive duties, cited. Frameworks use `## Structure and requirements` instead |
| `## Enforcement and penalties` | Who enforces, on what evidence, with what consequences. Frameworks use `## Assessment, certification and evidence` |
| `## Timeline and status` | In-force dates, phase-ins, pending amendments and open items, stated as of the review date |
| `## Key obligations for security/GRC teams` | What a practitioner actually has to do — the bridge to the skills layer |
| `## Interplay` | How the instrument stacks with neighbouring regimes and frameworks, linking to their packs |
| `## Primary sources` | The official texts the pack was written from, each with its URL. Required |
| Verification footer | The standard footer with `Last reviewed: YYYY-MM`. Required |

Packs in the library run roughly 90–200 lines. When an instrument does not fit, split it by layer — DORA and its RTS/ITS technical standards, NIS2 and its implementing regulation plus national transposition, are separate packs that cross-link — rather than writing one sprawling file.

### Entry points into the knowledge layer

An agent reaches a pack through one of four routes, so a new pack is wired into the relevant ones or it will not be found:

- [`context/README.md`](../context/README.md) — the index: one row per pack, grouped by region and framework family.
- [`context/regulations/other-jurisdictions.md`](../context/regulations/other-jurisdictions.md) — the global jurisdiction index: one row per country giving core law(s), regulator and headline breach clock, routing to the pack that holds the detail.
- [`context/crosswalks/breach-notification-timelines.md`](../context/crosswalks/breach-notification-timelines.md) and [`context/crosswalks/framework-crosswalk.md`](../context/crosswalks/framework-crosswalk.md) — the deadline matrix and the domain-level control mapping. A regime with a notification clock, or a framework with a control set, belongs in the relevant one.
- The skills themselves: a skill's `## References` section and its `references/` files link the packs its procedure needs — for example the jurisdiction-ordered applicability trees in [`skills/regulatory-applicability/references/applicability-decision-trees.md`](../skills/regulatory-applicability/references/applicability-decision-trees.md), which answer "in scope or not" and then hand off to the pack for the substance.

## Naming conventions

- Directories and files: `kebab-case`, lowercase, `.md` extension. Skill directories name the task, not the framework, unless the skill is framework-specific (`soc2-readiness`, `iso27001-readiness`).
- Skill frontmatter `name` must exactly equal its directory name (validated).
- Framework files carry the version in the name where versions matter: `nist-csf-2.md`, `cis-controls-v8.md`, `pci-dss-4.md`, `iso-27001-2022.md`.
- H2 sections in every `SKILL.md`, in order: Purpose, When to use, Inputs to gather, Procedure, Output format, Quality checklist, References (validated).

## Cross-linking rules

- **Relative paths only.** From a `SKILL.md`: `../../context/regulations/gdpr.md` for context, `../control-testing/SKILL.md` for a sibling skill, `references/question-bank.md` for its own references. Absolute paths and bare filenames that guess at location are rejected by the validator.
- **Link, don't duplicate.** If a fact lives in a context pack, link to it. Duplication is how regulatory content rots.
- **Every skill's References section** lists, in order: its own `references/` files, then context files, then related skills. "When to use" must name the better skill for adjacent tasks — e.g. a skill's own `SKILL.md` saying "for X, use `[control-mapping](../control-mapping/SKILL.md)` instead" (a path relative to that skill's directory, per the rule above).
- All relative links across `skills/`, `workflows/`, `context/`, `docs/`, `agents/`, and `templates/` are checked by CI; a broken link fails the build.

## Provider neutrality

Content files must run unmodified on any provider. Concretely:

- No tool or function names ("use the web_search tool"), no provider product names ("ask Claude to..."), no XML tags, no model-specific prompt tricks.
- Instructions are written to the agent in the imperative ("Score each risk...", "Ask the user for..."), which every instruction-following model handles.
- Anything provider-specific — file-upload limits, vector-store setup, skill auto-loading — belongs in `docs/integrations/` ([Claude](integrations/claude.md), [OpenAI](integrations/openai.md), [generic](integrations/generic.md)) and nowhere else.

## Versioning and review policy for regulatory content

Regulations and frameworks change; a skills library that silently goes stale is worse than none. Rules:

1. **Verification footer.** Every file containing regulatory or framework specifics (article numbers, deadlines, control counts, penalty figures) ends with a standard footer stating that details reflect publicly available sources as of a date, plus `Last reviewed: YYYY-MM`.
2. **Touch the date when you touch the facts.** Any PR that changes a regulatory or framework specific must update that file's last-reviewed date and cite the official source in the PR description (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
3. **Skill versions.** `metadata.version` in skill frontmatter follows semver: patch for wording fixes, minor for added steps/references, major for a changed output format or procedure restructure.
4. **Precision or nothing.** A specific citation (article, section, deadline, count) appears only when verified against the official text. When uncertain, the obligation is described generically with no invented citation — an unsourced "Art. 34(7)" is a defect, not a detail.
5. **No licensed standard text.** Paid standards (ISO 27001/27002, PCI DSS) are summarized at domain level — structure, themes, control intent — never reproduced verbatim. See the scope boundaries in [CONTRIBUTING.md](../CONTRIBUTING.md).
6. **Primary sources, not secondary.** Every context pack ends with a `## Primary sources` list of the official texts it was written from — the official journal or statute book, the regulator's own guidance, the standards body's page — each with its URL. Where an official source could not be retrieved and a secondary one carried a point, the list says so on that line. Trade press, vendor blogs and consultancy summaries are not sources for a specific.
7. **Every fact traceable.** A reader must be able to get from any specific in a pack to the source that supports it: the citation in the body, the source in the `## Primary sources` list, the date in the footer. Facts that cannot make that trip are stated generically or left out.

## Validation

`python3 scripts/validate_skills.py` from the repo root enforces the mechanical rules above: frontmatter keys, name/directory match, description length, required H2 sections, body length, and repository-wide relative-link integrity. CI runs it on every push and pull request (`.github/workflows/validate.yml`).
