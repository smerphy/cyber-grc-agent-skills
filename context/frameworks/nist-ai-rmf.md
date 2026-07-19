# NIST AI Risk Management Framework (AI RMF 1.0)

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | US National Institute of Standards and Technology (NIST) |
| Current version | AI RMF 1.0 (NIST AI 100-1), January 2023 |
| Structure | 4 functions — Govern, Map, Measure, Manage — decomposed into categories (GOVERN 1-6, MAP 1-5, MEASURE 1-4, MANAGE 1-4) and subcategories |
| Certifiable? | No — voluntary framework, no certification or attestation scheme. Used as a self-assessment and maturity scaffold |
| Companions | AI RMF Playbook (online, suggested actions per subcategory); Generative AI Profile (NIST AI 600-1, July 2024); NIST-published crosswalks to other frameworks |
| Typical use | AI risk program design, AI governance maturity assessment, common vocabulary across legal/engineering/risk teams, scaffold when no AI regulation directly applies |
| Cost | Free — all documents publicly downloadable from NIST |

## What it is and is not

The AI RMF is a **voluntary risk management framework**, not a control catalog and not a law. It was mandated by the US National AI Initiative Act of 2020 and developed through public workshops and comment rounds. Like NIST CSF (see [nist-csf-2.md](nist-csf-2.md)), it describes outcomes, not implementations: subcategories say what a mature organization achieves, and the Playbook suggests (but never requires) actions.

Two practical consequences:

- **No conformance claim is verifiable.** "We follow NIST AI RMF" is a statement of orientation, not an audited status. In vendor reviews, ask *which* functions and categories are implemented and what evidence exists — see [Using this in assessments](#using-this-in-assessments).
- **It pairs with, rather than competes against, mandatory regimes.** Where the EU AI Act imposes obligations (see [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md)), the AI RMF supplies the risk-management practice that makes those obligations operable. Where nothing is mandated, it is the default scaffold.

## Trustworthy AI characteristics

The framework defines seven characteristics of trustworthy AI. These are the *measurement targets* — MEASURE activities evaluate systems against them:

1. **Valid and reliable** — the foundational characteristic; without it the others cannot hold. Accuracy, robustness, generalization beyond training conditions.
2. **Safe** — no endangerment of life, health, property, or environment under intended use or foreseeable misuse.
3. **Secure and resilient** — resistance to adversarial attack (evasion, poisoning, extraction, prompt-based attacks) and ability to degrade gracefully.
4. **Accountable and transparent** — clear responsibility for outcomes; appropriate information about the system available to those who need it.
5. **Explainable and interpretable** — mechanisms for understanding *how* outputs are produced (explainability) and *what they mean* in context (interpretability).
6. **Privacy-enhanced** — norms such as anonymity, confidentiality, and control protected through the lifecycle; overlaps with DPIA work — see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
7. **Fair — with harmful bias managed** — the framework distinguishes systemic, computational/statistical, and human-cognitive bias; all three need treatment, not just dataset bias.

Trade-offs between characteristics are explicit in the framework (e.g., explainability vs. accuracy, privacy vs. fairness testing that needs demographic data). Document the trade-off decisions; auditors and regulators increasingly ask for them.

## The four functions

**Govern is cross-cutting**: it applies to the whole organization and enables the other three, which operate per AI system or per use context. Map → Measure → Manage is roughly identify → evaluate → treat, iterated across the lifecycle.

### GOVERN (categories 1-6) — cultivate a risk management culture

| Category | Theme |
|---|---|
| GOVERN 1 | Policies, processes, and procedures for AI risk management in place, transparent, and implemented effectively — including legal/regulatory compliance, risk tolerance, AI system inventory, and decommissioning |
| GOVERN 2 | Accountability structures — roles, responsibilities, and lines of communication defined; workforce trained for their AI risk duties |
| GOVERN 3 | Workforce diversity, equity, inclusion, and accessibility reflected in AI risk decisions; human-AI oversight roles defined |
| GOVERN 4 | Organizational culture that considers and communicates AI risk — critical-thinking and safety-first mindset, documentation of impacts, incident information sharing |
| GOVERN 5 | Processes for robust engagement with relevant AI actors and external stakeholder feedback |
| GOVERN 6 | Policies and procedures for third-party AI risks — supply chain, third-party software/models/data, and contingency for third-party failures |

### MAP (categories 1-5) — establish context and identify risks

| Category | Theme |
|---|---|
| MAP 1 | Context established and understood — intended purposes, deployment setting, expectations, organizational risk tolerance |
| MAP 2 | Categorization of the AI system — task, methods, and knowledge limits |
| MAP 3 | AI capabilities, targeted usage, goals, and expected benefits and costs understood |
| MAP 4 | Risks and benefits mapped for all system components, including third-party software and data |
| MAP 5 | Impacts on individuals, groups, communities, organizations, and society characterized |

### MEASURE (categories 1-4) — assess, analyze, track

| Category | Theme |
|---|---|
| MEASURE 1 | Appropriate methods and metrics identified and applied |
| MEASURE 2 | Systems evaluated for the trustworthy characteristics — this is the TEVV (test, evaluation, verification, validation) core, including bias, robustness, security, and privacy evaluation |
| MEASURE 3 | Mechanisms for tracking identified AI risks over time |
| MEASURE 4 | Feedback about efficacy of measurement gathered and assessed |

### MANAGE (categories 1-4) — treat and monitor

| Category | Theme |
|---|---|
| MANAGE 1 | Risks prioritized and responded to based on Map and Measure outputs — treatment decisions (avoid/mitigate/transfer/accept) documented |
| MANAGE 2 | Strategies to maximize benefits and minimize negative impacts planned and implemented — including mechanisms to sustain value and to deactivate/supersede systems |
| MANAGE 3 | Third-party AI risks and benefits managed on an ongoing basis |
| MANAGE 4 | Risk treatments and plans monitored post-deployment — incident response, recovery, communication, user appeal/override paths, decommissioning |

Subcategory identifiers follow the pattern `FUNCTION X.Y` (e.g., GOVERN 1.6 covers the AI system inventory; MAP 5.1 covers impact identification). Consult the official text for the full subcategory list rather than relying on paraphrase.

## Profiles, actors, and lifecycle framing

Three framework concepts worth knowing beyond the core:

- **Profiles.** A profile is a selection and tailoring of subcategories for a use case, sector, or organization. The framework encourages **current profile vs. target profile** comparison — which is precisely a gap assessment, and the cleanest way to turn the framework into a roadmap. Sector and use-case profiles (generative AI being the flagship) narrow the framework to what matters for that context.
- **AI actors.** The framework assigns activities across the actor landscape — designers/developers, deployers, operators, TEVV specialists, impacted individuals and communities, and others. Use the actor lens when assigning subcategory ownership: many failed implementations assigned everything to a data-science team that controls neither procurement (GOVERN 6) nor deployment context (MAP 1).
- **Lifecycle.** Activities recur across design, development, deployment, operation, and decommissioning — the framework is explicit that risk management is iterative, not a pre-launch gate. Assessment implication: ask for *post-deployment* Measure and Manage evidence, not just launch reviews.

## Companion documents

- **AI RMF Playbook** — online companion mapping suggested actions, transparency/documentation guidance, and references to every subcategory. Explicitly non-exhaustive and non-mandatory; useful as an evidence-idea generator when building a control set.
- **AI RMF Roadmap and crosswalks** — NIST maintains crosswalks between the AI RMF and other instruments (including ISO/IEC standards and the EU AI Act; check NIST's AI Resource Center for the current set and versions before citing a specific mapping).
- **Profiles** — use-case or sector tailorings of the framework. The most important one so far is the Generative AI Profile, below.

Relationship to NIST CSF ([nist-csf-2.md](nist-csf-2.md)): deliberately parallel design — voluntary, outcome-based, function/category/subcategory structure, profiles, free. CSF 2.0's Govern function even mirrors the AI RMF's cross-cutting Govern. But scope differs: CSF manages cybersecurity risk; AI RMF manages the full socio-technical risk surface of AI (bias, safety, transparency, societal impact), of which security is one slice. Organizations running both should share governance machinery and keep the risk registers linked, not merged.

## Generative AI Profile (NIST AI 600-1, July 2024)

A cross-sectoral profile of the AI RMF for generative AI, responding to the 2023 US Executive Order on AI. It identifies **12 risk categories that are unique to or exacerbated by generative AI**, then maps ~200 suggested actions to AI RMF subcategories. The 12 GAI risk categories:

1. CBRN information or capabilities
2. Confabulation (the profile's term for hallucination — confidently produced false content)
3. Dangerous, violent, or hateful content
4. Data privacy
5. Environmental impacts
6. Harmful bias and homogenization
7. Human-AI configuration (over-reliance, automation bias, emotional entanglement, mis-calibrated trust)
8. Information integrity (mis/disinformation at scale)
9. Information security (both attacks *on* GAI systems — e.g., prompt injection, data poisoning — and GAI-*enabled* offensive capability)
10. Intellectual property
11. Obscene, degrading, and/or abusive content
12. Value chain and component integration (opaque third-party models, data, and components)

How to apply the profile in practice:

- Run the 12 categories as a per-system checklist during risk identification (MAP); record "considered, not applicable" decisions explicitly rather than skipping rows.
- Pull suggested actions from the profile for the categories that hit, and convert them into controls with owners and evidence expectations.
- Reassess on model swap, new data connections, or new tool/agent capability — GAI risk posture is configuration-sensitive, not set-and-forget.

The list is referenced as the genAI risk checklist by [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md), and it covers the LLM-specific risks (prompt injection, output over-reliance, data leakage) that generic IT risk lists miss.

## Mapping to EU AI Act and ISO/IEC 42001

The AI RMF is voluntary but maps cleanly onto the mandatory and certifiable regimes, so one program can serve all three:

| AI RMF | EU AI Act (high-risk provider obligations) | ISO/IEC 42001 |
|---|---|---|
| GOVERN | Quality management system (Art. 17), accountability, provider role duties | Clauses 4-7 (context, leadership, planning, support), Annex A governance controls |
| MAP | Risk management system (Art. 9) — risk identification; intended-purpose definition; data governance context | Clause 6 planning, AI system impact assessment, Annex A impact-assessment and lifecycle controls |
| MEASURE | Accuracy, robustness, cybersecurity (Art. 15); testing within Art. 9; logging (Art. 12) | Clause 9 performance evaluation, Annex A lifecycle/verification controls |
| MANAGE | Risk treatment within Art. 9; post-market monitoring and serious-incident reporting (Arts. 72-73); corrective actions | Clauses 8 and 10 (operation, improvement), third-party controls |

Treat the table as directional, not authoritative — use published crosswalks for anything contractual. Key differences to keep straight:

- **AI Act obligations are legal duties with penalties**; AI RMF alignment does not discharge them. Classification and obligation mapping come first — see [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md).
- **ISO 42001 is certifiable; AI RMF is not** (see [iso-42001.md](iso-42001.md)). Organizations wanting a demonstrable claim typically implement AI RMF practice inside a 42001 management system.
- The AI RMF is stronger than either on **measurement practice and socio-technical risk framing** (TEVV, bias taxonomy, human-AI configuration); borrow that content even when 42001 or the AI Act is the formal target.

## Using this in assessments

- **Use it as the default scaffold when nothing is mandated.** For organizations with no EU nexus and no sector AI rules, assess against the four functions anyway — it is the de facto common language and converts directly into a roadmap. The procedure and maturity scale live in [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
- **Assess Govern first, and organization-wide.** Map/Measure/Manage findings are unfixable without accountability structures, an inventory, and a risk-tolerance statement. A common failure mode: strong per-model TEVV (MEASURE 2) sitting inside a program with no GOVERN 1 policy layer and no third-party coverage (GOVERN 6 / MANAGE 3).
- **Score per function, not one blended number.** Function-level maturity (e.g., Govern 3, Map 2, Measure 1, Manage 2 on a five-level scale) is the useful output; a single "AI RMF score" hides exactly the gaps that matter.
- **For generative AI, always layer the GAI Profile.** Run the 12 risk categories as a checklist per system; record "considered, not applicable" explicitly. Confabulation, human-AI configuration, and value-chain integration are the three most often skipped.
- **Vendor claims of AI RMF alignment need decomposition.** Ask for: the AI system inventory practice, the risk tolerance statement, TEVV evidence for the product you are buying, and the incident/monitoring pathway. "Aligned to NIST AI RMF" without artifacts is marketing — treat as with unaccredited certificates under [iso-27001-2022.md](iso-27001-2022.md).
- **Express targets as a profile, not prose.** A current-vs-target profile at subcategory level doubles as the remediation backlog and the re-assessment baseline; free-text maturity narratives do neither.
- **Integrate, don't duplicate.** AI RMF findings should land in the enterprise risk register and existing control-testing universe with standard scales — the framework itself pushes integration with enterprise risk management, and an orphan "AI RMF tracker" is an anti-pattern. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) for folding AI controls into the common control set.
- **Evidence to request in an assessment:** AI policy and risk tolerance (GOVERN 1), RACI or equivalent (GOVERN 2), AI system inventory with decommissioning provisions (GOVERN 1.6), per-system context/impact documentation (MAP), test and evaluation reports against the trustworthy characteristics (MEASURE 2), risk register entries and treatment decisions (MANAGE 1), post-deployment monitoring output and incident records (MANAGE 4).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
