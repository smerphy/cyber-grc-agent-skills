---
name: ai-governance
description: >-
  Builds and assesses AI governance programs: inventories AI systems (including
  vendor-embedded AI and internal LLM use), classifies them under EU AI Act
  risk tiers with GPAI considerations, maps obligations by role, assesses
  maturity against NIST AI RMF 1.0 and ISO/IEC 42001, and defines AI-specific
  controls. Use when a user says "AI governance", "EU AI Act", "classify our AI
  systems", "AI risk", "AI RMF", "ISO 42001", "LLM policy", or "are we allowed
  to use this AI tool".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Stand up or assess AI governance that is regulator-ready and integrated with the existing GRC program rather than a parallel bureaucracy. Covers the three anchor frameworks — EU AI Act (Regulation (EU) 2024/1689) for legal obligations, NIST AI RMF 1.0 (Govern / Map / Measure / Manage) for risk management practice, and ISO/IEC 42001:2023 for a certifiable AI management system — and the LLM-specific risks (prompt injection, data leakage, ungoverned output use) that generic IT controls miss.

## When to use

- Building an AI governance program from scratch, or assessing an existing one.
- Classifying specific AI systems under the EU AI Act and mapping the resulting obligations (provider vs deployer).
- Writing or reviewing an AI risk assessment, AI system inventory, or internal genAI acceptable-use standard.
- Evaluating an AI vendor or an AI feature a vendor added to an existing product.
- **Not for:** privacy impact assessment of an AI system's personal-data processing — use [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) (run both for AI touching personal data; cross-reference the outputs). Full third-party due diligence workflow — use [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) with the AI questions from this skill. Drafting the policy document itself end-to-end — use [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md) with [references/llm-usage-policy-elements.md](references/llm-usage-policy-elements.md) as the content spec.

## Inputs to gather

1. **Organizational footprint**: EU nexus (established in EU? placing AI systems on the EU market? outputs used in the EU?), sectors served, whether the org develops AI, buys it, or both. Other applicable AI rules (e.g., Colorado's AI law, sectoral model-risk guidance such as SR 11-7 for banks) — route the applicability question through [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md).
2. **Known AI usage**: developed models, purchased AI products, AI features inside existing SaaS, internal LLM/chatbot usage, API usage of foundation models, agents.
3. **Existing GRC assets**: risk register and methodology, TPRM process, policy framework, control catalog, exception process — integrate, do not duplicate.
4. **Discovery sources** for the inventory: procurement records, SSO/app logs, expense reports, network egress to known AI endpoints, engineering dependency manifests, vendor notices announcing AI features.
5. **Ambition level**: legal-compliance floor only, AI RMF-aligned risk management, or ISO 42001 certification target.

## Procedure

1. **Inventory AI systems.** Build one register with a row per system. Capture: name; business purpose; owner; lifecycle stage; build vs buy; underlying model(s) and provider; data in (categories, incl. personal/confidential data) and data out; autonomy level (assistive → agentic); affected people (employees, customers, public); deployment geography. Explicitly hunt for the three commonly missed classes: **embedded AI** (features vendors switched on inside tools you already own), **shadow AI** (staff using consumer LLMs with company data), and **internal LLM use** (copilots, RAG over internal documents, agents). An inventory that lists only data-science projects is incomplete by construction.
2. **Classify each system under the EU AI Act.** For each row determine:
   - **Role**: provider (develops/places on market under own name), deployer (uses under own authority), importer, or distributor. Substantially modifying a system or white-labeling it can convert a deployer into a provider.
   - **Tier**: prohibited practice (Art. 5) → stop immediately and escalate; high-risk (Annex III use cases such as employment, credit, essential services, biometrics, education — or a safety component of Annex I regulated products); limited/transparency-risk (Art. 50: chatbots, synthetic content, emotion recognition, deepfakes); or minimal risk. Note the Art. 6(3) filter: an Annex III-listed system may escape high-risk classification if it performs only narrow procedural/preparatory tasks — but the assessment must be documented and the system registered.
   - **GPAI angle**: if you provide a general-purpose model, Chapter V obligations apply (heavier if it is classified as having systemic risk); if you build **on** a GPAI model, you are typically a downstream provider or deployer of an AI system, not a GPAI provider.
   - Classification procedure and role-determination practice notes: [references/eu-ai-act-obligations.md](references/eu-ai-act-obligations.md). Statutory detail (tier lists, obligations, timeline, penalties): [../../context/regulations/eu-ai-act.md](../../context/regulations/eu-ai-act.md).
   - **Decision point:** no EU nexus → skip AI Act obligations but keep the tiering as an internal risk-severity proxy; it is the de facto common language.
3. **Map obligations per classification.** Produce an obligation matrix (system × obligation × owner × status × deadline). High-risk as provider means the full Art. 9–15 stack (risk management system, data governance, technical documentation, logging, transparency to deployers, human oversight, accuracy/robustness/cybersecurity) plus QMS, conformity assessment, registration, post-market monitoring, and serious-incident reporting. High-risk as deployer means Art. 26 duties (use per instructions, assign competent human oversight, input-data relevance, monitoring, log retention, informing workers and affected persons) and, for some deployers, a fundamental-rights impact assessment (Art. 27).
4. **Assess against NIST AI RMF 1.0.** Rate current practice per function — **Govern** (accountability structures, policy, risk tolerance, culture), **Map** (context, categorization, impact identification per system), **Measure** (metrics, TEVV — test/evaluation/verification/validation, bias and robustness testing), **Manage** (risk treatment, prioritization, incident response, third-party monitoring) — scoring each function with the shared five-level maturity scale in [../framework-gap-assessment/references/maturity-scale.md](../framework-gap-assessment/references/maturity-scale.md). For generative AI, apply the NIST Generative AI Profile (AI 600-1) risk list. Output: per-function gaps feeding step 5. If the target is a certifiable management system, additionally gap-assess against ISO/IEC 42001 clauses 4–10 and Annex A using [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md).
5. **Define AI-specific controls.** Select from the starter catalog in [references/ai-control-set.md](references/ai-control-set.md) (~20 controls mapped to AI RMF functions and ISO 42001 Annex A areas). Minimum viable set for any org using AI in decisions about people: model documentation (purpose, data, limitations, performance); pre-deployment testing incl. bias where people are affected; defined human-oversight points with authority to override; input/output logging; drift and performance monitoring with thresholds; change management for models and prompts. **LLM-specific controls** — treat these as first-class, not exotic: prompt-injection exposure assessment for any LLM app touching untrusted content or wielding tools; data-leakage prevention for prompts (what data classes may be sent to which models under which contracts); mandatory human review of LLM output used in consequential decisions or published externally; grounding/citation requirements for RAG systems. The internal acceptable-use standard content spec is in [references/llm-usage-policy-elements.md](references/llm-usage-policy-elements.md).
6. **Integrate with existing GRC — do not build a parallel program.**
   - **Risk register**: AI risks enter the same register with the same scoring scales ([../risk-assessment/SKILL.md](../risk-assessment/SKILL.md), [../../context/risk-scoring.md](../../context/risk-scoring.md)). Add AI-specific risk statements (biased outcomes, hallucinated output acted upon, model supply-chain compromise, regulatory non-compliance per tier), not a separate AI matrix.
   - **TPRM**: AI vendors and AI features flow through the existing process ([../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md)) with added questions: training on customer data? retention of prompts? model provenance? sub-processors for inference? AI Act role and tier of the vendor's product? Contract clauses: no training on your data without consent, breach/incident notice covering model incidents, audit rights.
   - **Exceptions**: uses outside the approved list go through [../exception-management/SKILL.md](../exception-management/SKILL.md) with expiry dates — not silent tolerance.
   - **Testing and metrics**: AI controls enter the control-testing universe ([../control-testing/SKILL.md](../control-testing/SKILL.md)); report inventory coverage, classification completion, high-risk obligation status, and exception count via [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md).
7. **Operate the loop.** Set cadences: inventory refresh (quarterly, plus procurement gate so new AI enters at purchase); reclassification on material change (new use case, new autonomy, new geography); monitoring review; incident pathway that recognizes AI-specific events (serious incidents for high-risk systems have regulatory reporting duties — coordinate with [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md)); horizon scanning for the fast-moving rulebook via [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md).

## Output format

Deliver three artifacts:

**1. AI system inventory & classification register** (table):

| ID | System | Owner | Build/Buy | Role (AI Act) | Tier | GPAI? | Personal data | Affected people | Status |
|---|---|---|---|---|---|---|---|---|---|
| AI-007 | Resume screening (vendor X feature) | Head of TA | Buy (embedded) | Deployer | High-risk (Annex III — employment) | No | Yes | Job applicants | Obligations mapped; oversight gap open |
| AI-012 | Internal RAG assistant on policy docs | CIO | Build on GPAI API | Deployer of AI system | Minimal (internal, non-consequential) | Downstream | Incidental | Employees | Approved with AUP controls |

**2. Obligation & gap matrix**: system × obligation (statutory or framework) × current state × gap × owner × deadline. Group by tier; prohibited findings at top with immediate-stop actions.

**3. Control implementation plan**: selected controls from the catalog, mapped to AI RMF function and ISO 42001 area, with owner, evidence expected, and test approach. Include the risk-register entries created and the TPRM/policy/exception hooks established.

State the classification rationale in one or two sentences per system — auditors and market-surveillance authorities ask "why is this not high-risk," and an unexplained tier is an unsupported tier.

## Quality checklist

- [ ] Inventory covers built, bought, embedded, and shadow AI — discovery method documented, not just self-report
- [ ] Every system has an AI Act role AND tier with written rationale; Art. 6(3) carve-out claims are documented, not assumed
- [ ] Any Art. 5 prohibited-practice finding triggered an immediate escalation, not a backlog item
- [ ] Obligations distinguish provider vs deployer duties — no copy-pasting the provider list onto systems you merely use
- [ ] NIST AI RMF assessment covers all four functions; genAI systems assessed against the Generative AI Profile risk list
- [ ] LLM-specific controls (prompt injection, prompt data leakage, output review) present wherever LLMs are in scope
- [ ] AI risks live in the enterprise register with standard scales — no orphan AI risk matrix
- [ ] AI vendors route through existing TPRM with the added AI question set and contract clauses
- [ ] Serious-incident reporting duty for high-risk systems is wired into incident response
- [ ] Applicability timeline checked against current date — obligations already in force flagged as compliance gaps, not roadmap items

## References

- [references/eu-ai-act-obligations.md](references/eu-ai-act-obligations.md) — classification quick-reference, role determination, obligation-to-control mapping
- [references/ai-control-set.md](references/ai-control-set.md) — starter AI control catalog mapped to AI RMF and ISO 42001
- [references/llm-usage-policy-elements.md](references/llm-usage-policy-elements.md) — required elements of an internal LLM/genAI acceptable-use standard
- [../../context/regulations/eu-ai-act.md](../../context/regulations/eu-ai-act.md) — EU AI Act overview
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — scoring scales and aggregation pitfalls
- [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) — privacy assessment for AI systems processing personal data
- [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) — vendor AI due diligence
- [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) — ISO 42001 gap assessment mechanics
- [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md) — drafting the AI/genAI policy documents
- [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md) — tracking AI regulatory change

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
