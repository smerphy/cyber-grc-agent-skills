# Agent instructions for this repository

This repository is a library of portable AI agent skills for cyber Governance, Risk & Compliance (GRC). If you are an AI agent operating in this repository — or loaded with its contents — follow these rules.

## How the repository is organized

| Layer | Path | What it is | When to load |
|---|---|---|---|
| Personas | `agents/` | System-prompt role definitions (GRC analyst, compliance officer, risk manager, internal auditor, privacy officer, AI governance lead, greybeard technical reviewer) | Pick one at session start to set role, tone, and boundaries |
| Skills | `skills/<name>/SKILL.md` | Step-by-step procedures for a specific GRC task | Load when the task matches the skill's `description` frontmatter |
| Skill references | `skills/<name>/references/` | Deep supporting material (question banks, rubrics, worked examples) | Load on demand from links in the SKILL.md — not up front |
| Context packs | `context/` | Framework and regulation knowledge (NIST CSF 2.0, ISO 27001, GDPR, NIS2, DORA, EU AI Act, …) | Load the specific file a skill links to |
| Workflows | `workflows/` | Multi-step playbooks chaining several skills with decision gates | Load for multi-phase engagements (audit readiness, incident regulatory response, …) |
| Templates | `templates/` | Deliverable skeletons (risk register, DPIA, SoA, workpapers, …) | Load when producing the corresponding deliverable |
| Branding | `branding/` | Report design and brand identity: user's logo/colors/fonts in `brand-profile.md`, report style specs in `styles/` (default: consulting-classic) | Load `brand-profile.md` before producing any formatted stakeholder deliverable |

## Operating rules

1. **Progressive disclosure.** Load a skill's `SKILL.md` first; pull `references/` files and `context/` packs only when the procedure directs you to. Do not bulk-load the repository.
2. **Never fabricate compliance facts.** Do not invent article numbers, control identifiers, deadlines, or an organization's compliance status. If a specific is not in the loaded material and you are not certain of it, say so and flag it for verification.
3. **Respect the verification footers.** Regulatory content carries a "Last reviewed" date. Regulations change; when currency matters (deadlines, penalties, scope thresholds), tell the user to verify against the official text and check the date.
4. **Not legal advice.** Output produced with these skills is analysis support, not legal advice. Recommend counsel review for legal interpretation, notification decisions, and regulator interaction.
5. **Evidence over assertion.** When assessing controls or compliance, tie every conclusion to named evidence. "No evidence provided" is a finding, not a pass.
6. **Stay within the skill's output format.** Each skill defines its deliverable structure and quality checklist — run the checklist before presenting results.
7. **Brand formatted deliverables.** Before producing a report, deck, or board pack for stakeholders, read `branding/brand-profile.md` and apply the selected style spec (default: `branding/styles/consulting-classic.md`) with the profile's overrides. Never invent brand elements for `DEFAULT` fields, and never strip verification footers or evidence citations for layout reasons. Working artifacts (registers, workpapers, logs) keep their native template formats.

## Validation

`python3 scripts/validate_skills.py` from the repo root validates skill frontmatter, required sections, and cross-file links. Run it after modifying any skill, workflow, persona, or context file.
