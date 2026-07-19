---
name: policy-authoring
description: >-
  Drafts internal security and GRC policies, standards, and procedures from scratch or from
  framework requirements. Use when a user asks to "write a policy", "draft a standard",
  "create an acceptable use / access control / incident response policy", "document a
  procedure", or needs policy statements mapped to ISO 27001, NIST CSF, CIS, SOC 2, or
  regulatory controls. Produces testable statements plus a statement-to-control
  traceability table.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Produce security governance documents that auditors can test, employees can follow, and control owners can enforce. This skill covers the full document hierarchy — policy, standard, procedure, guideline — and enforces the two properties most drafts lack: every normative statement is testable, and every statement traces to at least one framework control it satisfies.

## When to use

- Drafting a new policy, standard, procedure, or guideline for a security program.
- Converting framework or regulatory requirements (e.g., ISO 27001 Annex A, PCI DSS, HIPAA Security Rule) into internal policy language.
- Restructuring a monolithic "security policy" into a proper hierarchy.
- Building out the policy set for a new program — see [references/policy-catalog.md](references/policy-catalog.md) for the recommended catalog.
- **Do NOT use** to critique or score an existing document — use [../policy-review/SKILL.md](../policy-review/SKILL.md).
- **Do NOT use** to design the exception process itself — link to it; the process lives in [../exception-management/SKILL.md](../exception-management/SKILL.md).
- **Do NOT use** to decide which regulations apply to the organization — run [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) first if scope is unclear.

## Inputs to gather

Ask before drafting; do not guess:

1. **Document type and topic** — policy, standard, procedure, or guideline; which subject (e.g., access control, cryptography).
2. **Target framework(s)/regulation(s)** — what the document must satisfy (ISO 27001:2022, SOC 2, CIS v8, NIST CSF 2.0, PCI DSS v4, HIPAA, etc.). This drives the traceability table.
3. **Scope** — legal entities, geographies, workforce categories (employees, contractors, third parties), systems/data in scope, explicit exclusions.
4. **Organizational context** — size, industry, regulated status, cloud vs. on-prem, existing tooling (named tools belong in standards/procedures, never in policy).
5. **Governance facts** — approving body, document owner role, review cadence (default: annual), where the exception process is documented, enforcement mechanism (usually the disciplinary process in HR policy).
6. **Sibling documents** — existing policies this one must not conflict with or duplicate (e.g., data classification levels defined elsewhere must be referenced, not redefined).
7. **House style** — existing template, numbering scheme, terminology (check against [../../context/glossary.md](../../context/glossary.md) for standard GRC terms).

If the user cannot answer 2, 3, or 5, propose defaults explicitly and mark them `[ASSUMPTION]` in the draft.

## Procedure

1. **Confirm the document type.** Apply the hierarchy strictly; misplaced content is the most common drafting defect:

   | Level | Answers | Contains | Changes | Approved by |
   |---|---|---|---|---|
   | **Policy** | WHY and WHAT (intent, rules) | Mandatory statements, roles, scope | Rarely (annual review) | Executive / board-level |
   | **Standard** | WHAT exactly (measurable specs) | Parameters: key lengths, password rules, baselines, approved tech | When technology changes | CISO / security function |
   | **Procedure** | HOW (step-by-step) | Ordered steps, actors, inputs/outputs, screenshots OK | Frequently | Process owner |
   | **Guideline** | RECOMMENDED how | Non-mandatory advice, only "should/may" | As needed | Process owner |

   If the user asks for "a password policy" that specifies 14-character minimums, split it: a one-line policy statement ("Authentication credentials MUST meet the Authentication Standard") plus a standard holding the parameters. Volatile detail in a policy forces executive re-approval for every tweak.

2. **Load the skeleton.** Start from [../../templates/policy-template.md](../../templates/policy-template.md). Mandatory elements — a document missing any of these is incomplete:
   - Purpose (2–4 sentences: risk addressed, obligations satisfied)
   - Scope (who, what, where; explicit exclusions)
   - Roles and responsibilities (by role title, never by person name)
   - Policy statements (the normative core, uniquely numbered, e.g., AC-01, AC-02)
   - Exceptions pointer (reference the exception process; never define approval workflows inline)
   - Enforcement (consequence of non-compliance, referencing the disciplinary process)
   - Review cadence (frequency + trigger events: major incident, reorg, regulatory change)
   - Version control block (version, date, author, approver, change summary)
   - Definitions (only terms used non-obviously; prefer linking a shared glossary)
   - Related documents (parent policy, child standards/procedures, sibling policies)

3. **Draft policy statements under plain-language rules.** RFC-2119-style keyword discipline:
   - **MUST / MUST NOT** ("shall") — mandatory; violation is a policy breach. Only use where the organization will actually enforce and can actually verify.
   - **SHOULD / SHOULD NOT** — expected; deviation requires a documented, justified decision. Do not use SHOULD as a euphemism for "we won't enforce this" — that belongs in a guideline.
   - **MAY** — genuinely optional. Rare in policies; delete the statement if nothing hinges on it.

   Per-statement rules (full set with before/after rewrites in [references/writing-rules.md](references/writing-rules.md)):
   - One requirement per statement. Split compound sentences.
   - Name the accountable role or population ("System owners MUST...", "All workforce members MUST NOT...").
   - Testable: an auditor must be able to design a pass/fail test from the sentence alone. Ban "appropriate", "adequate", "timely", "regularly", "where possible" unless the parameter is defined in a linked standard.
   - No product names, team names, or step-by-step instructions in a policy — push down to standard/procedure.
   - Active voice; present tense; under ~30 words per statement where possible.

4. **Map each statement to controls.** For every numbered statement, identify the framework control(s) it satisfies in each target framework. Use [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) for cross-framework equivalences and the relevant file under `../../context/frameworks/` for control identifiers. **Decision point:** if a statement maps to nothing in any target framework, either (a) it addresses a real organizational risk — keep it and record the risk as its justification, or (b) it is legacy noise — flag it for the user to cut. If a required control has no covering statement, draft one: the mapping is bidirectional.

5. **Write supporting sections.** Purpose and scope from inputs; roles as a short table (Owner, Approver, and each role named in a statement); exceptions section as one sentence pointing to the exception process ([../exception-management/SKILL.md](../exception-management/SKILL.md) describes what that process contains); enforcement referencing the disciplinary/contract-termination mechanism; review cadence with trigger events.

6. **Consistency pass.** Verify: terminology matches sibling documents and the glossary; no statement contradicts a sibling policy the user listed; classification levels, role titles, and system names match their authoritative sources; every cross-reference resolves to a real document.

7. **Produce the traceability table** (see Output format). This is a deliverable, not scaffolding — it feeds gap assessments ([../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md)), control mapping ([../control-mapping/SKILL.md](../control-mapping/SKILL.md)), and audit prep ([../audit-preparation/SKILL.md](../audit-preparation/SKILL.md)).

8. **Hand off.** Deliver the draft plus traceability table. Recommend a review pass with [../policy-review/SKILL.md](../policy-review/SKILL.md) before approval, and note that statements will later need test procedures ([../control-testing/SKILL.md](../control-testing/SKILL.md)).

## Output format

Two artifacts:

**1. The document**, following [../../templates/policy-template.md](../../templates/policy-template.md), with numbered statements. Excerpt of the expected style:

> **4. Policy statements**
>
> **AC-01.** System owners MUST grant access based on documented role profiles approved by the data owner.
> **AC-02.** Managers MUST certify the continued need for their direct reports' access at the frequency defined in the Access Review Standard.
> **AC-03.** IT operations MUST disable a departing workforce member's accounts by end of the last working day, as notified by HR.

**2. The traceability table** — one row per statement, one mapping column per target framework:

| Stmt | Statement summary | ISO 27001:2022 Annex A | CIS v8 | SOC 2 | Notes |
|---|---|---|---|---|---|
| AC-01 | Role-based access grants | A.5.15, A.5.18 | 6.1, 6.8 | CC6.1 | |
| AC-02 | Periodic access certification | A.5.18 | 6.8 | CC6.2 | Frequency in Access Review Standard |
| AC-03 | Leaver deprovisioning same day | A.5.18 | 6.2 | CC6.3 | Depends on HR notification SLA |
| — | *Uncovered control:* A.5.16 identity lifecycle | A.5.16 | 6.x | CC6.1 | **Gap — draft statement or justify** |

Close the table with any uncovered target controls and any unmapped statements, each with a recommended disposition.

## Quality checklist

- [ ] Document type matches content: no parameters in a policy, no step-by-step instructions above procedure level.
- [ ] All mandatory elements from step 2 present; version control block filled in.
- [ ] Every normative statement uses exactly one of MUST/MUST NOT/SHOULD/SHOULD NOT/MAY, names an accountable role or population, and contains one requirement.
- [ ] Zero occurrences of "appropriate/adequate/timely/regularly/periodically/where possible" without a linked standard defining the parameter.
- [ ] Every statement appears in the traceability table; every in-scope target control is covered or has a documented disposition.
- [ ] Exceptions section is a pointer, not an inline process; enforcement section references a real mechanism.
- [ ] No person names, product names, or team org-chart names in a policy-level document.
- [ ] All `[ASSUMPTION]` markers surfaced to the user in the handoff summary.

## References

- [references/policy-catalog.md](references/policy-catalog.md) — recommended policy set for a security program with scope of each
- [references/writing-rules.md](references/writing-rules.md) — style rules with before/after rewrites
- [../../templates/policy-template.md](../../templates/policy-template.md) — document skeleton
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) — cross-framework control equivalences
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md), [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md), [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md), [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md), [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md), [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md) — control identifiers for mapping
- [../../context/glossary.md](../../context/glossary.md) — standard GRC terminology
- [../policy-review/SKILL.md](../policy-review/SKILL.md) — review the finished draft
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — the process the exceptions section points to
- [../control-mapping/SKILL.md](../control-mapping/SKILL.md), [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md), [../control-testing/SKILL.md](../control-testing/SKILL.md) — downstream consumers of the traceability table

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
