# Workflow: AI System Intake

```yaml
name: ai-system-intake
description: >-
  Governance gate for any proposed AI system — built, bought, or embedded in a
  vendor product: inventory entry, EU AI Act classification, DPIA screening and
  assessment where triggered, risk assessment, control requirements, vendor
  assessment for third-party systems, a formal approval gate, and ongoing
  monitoring registration.
skills_used:
  - ai-governance
  - dpia-privacy-assessment
  - risk-assessment
  - third-party-risk-assessment
typical_duration: 1-2 weeks for low-risk internal tools; 4-8 weeks for high-risk or personal-data-heavy systems
roles:
  - ai-governance-lead
  - privacy-officer
  - risk-manager
  - grc-analyst
```

## Trigger

- A team proposes building, buying, or piloting an AI system, or enabling an AI feature inside an existing vendor product (the most commonly missed trigger — vendor AI feature toggles are intake events).
- Discovery of AI already in use without intake ("shadow AI") — run retroactively; the in-use period is a finding.
- Material change to an approved system: new model, new data source, new use case, new user population. Re-run from step 2.

## Prerequisites

- An AI inventory as system of record (see [ai-governance](../skills/ai-governance/SKILL.md) for the schema) and a published intake form/channel teams actually know about.
- A defined approval authority matrix: who approves at each risk level (the ai-governance-lead alone for low risk; an AI governance committee or executive for high risk).
- The organization's EU AI Act applicability position established via [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) — whether and where the organization acts as provider, deployer, importer, or distributor (see [EU AI Act](../context/regulations/eu-ai-act.md)).

## Steps

### 1. Intake and inventory entry — grc-analyst with the proposing team

- **Skill:** [ai-governance](../skills/ai-governance/SKILL.md) (intake step)
- **Inputs:** completed intake form: purpose and use case, model type and provenance (built / fine-tuned / API / vendor-embedded), data in (training, fine-tuning, prompts/context) and data out, users and affected persons, autonomy level (human-in-the-loop or not), jurisdictions of deployment.
- **Actions:** record the system in the AI inventory with status "in intake." Verify answers against the actual design — intake forms describe intentions; classification depends on facts. Identify the accountable business owner.
- **Outputs:** inventory entry; verified fact base for classification.

### 2. EU AI Act classification — ai-governance-lead

- **Skill:** [ai-governance](../skills/ai-governance/SKILL.md) (classification step)
- **Inputs:** fact base; organizational role position (provider vs deployer — obligations differ substantially).
- **Actions:** where the Act applies, classify against its risk tiers: prohibited practices (stop immediately and redesign — these are banned, not manageable); high-risk (Annex-listed use cases such as employment, credit, education, essential services — triggers the heavy obligation set: risk management system, data governance, technical documentation, logging, human oversight, accuracy/robustness); limited-risk transparency obligations (e.g., disclosing AI interaction, labeling synthetic content); minimal risk. Check GPAI-related duties where the organization provides or materially modifies general-purpose models. Run the same pass against the other AI regimes the deployment touches: [US state and local AI laws](../context/regulations/us-state-ai-laws.md) reach developers and deployers of systems used in consequential decisions, hiring tools and frontier models, and other jurisdictions route from the [global jurisdiction index](../context/regulations/other-jurisdictions.md). Where no AI-specific law applies, classify anyway using the Act's tiers as an internal risk taxonomy — it is a sound severity scale regardless of jurisdiction. Document the classification rationale; borderline calls go to counsel.
- **Outputs:** classification record with rationale in the inventory.
- **Decision gate:** prohibited-practice hit → workflow stops, proposal returned for redesign, decision logged. High-risk → the full obligation track in step 5 is mandatory, and timelines lengthen; tell the business owner now, not at approval.

### 3. DPIA screening, and DPIA if triggered — privacy-officer

- **Skill:** [dpia-privacy-assessment](../skills/dpia-privacy-assessment/SKILL.md)
- **Inputs:** fact base: personal data categories in training data, prompts, outputs, and logs; affected data subjects; jurisdictions.
- **Actions:** screen for DPIA triggers. Under GDPR Art. 35 a DPIA is required where processing is likely to result in high risk — AI systems frequently qualify via systematic evaluation/profiling with significant effects, large-scale processing of special categories, or new-technology criteria on supervisory authorities' lists. If triggered, run the full DPIA now, in parallel with steps 4-6, covering AI-specific privacy issues: training-data provenance and lawful basis, memorization/regurgitation risk, prompts and outputs as personal data, data subject rights execution against models, and cross-border transfers to model providers. A negative GDPR screen does not end the step: [US state privacy laws](../context/regulations/us-state-privacy.md) carry their own data protection assessment duties for profiling and other higher-risk processing, and other jurisdictions' privacy packs (routed from the [global jurisdiction index](../context/regulations/other-jurisdictions.md)) state theirs. If nothing is triggered, record the screening outcome and reasoning — the negative determination is itself required evidence.
- **Outputs:** screening record; completed DPIA with mitigations where triggered.
- **Decision gate:** a DPIA concluding high residual risk that cannot be mitigated requires prior consultation with the supervisory authority under GDPR Art. 36 before processing starts — this blocks approval in step 7 until resolved.

### 4. Risk assessment — risk-manager with the business owner

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md)
- **Inputs:** fact base; classification; DPIA findings; the org's standard risk methodology.
- **Actions:** assess beyond privacy: harmful/wrong output and hallucination impact on the specific use case, bias and discrimination exposure, security (prompt injection, data leakage through outputs, model supply chain), IP (training-data provenance, output ownership), operational dependence and model-drift, and reputational exposure. Score against the standard appetite so AI risks land in the same register and language as everything else — a separate AI risk universe fragments governance.
- **Outputs:** risk assessment with scored scenarios; register entries for material risks.

### 5. Control requirements — ai-governance-lead with grc-analyst

- **Skill:** [ai-governance](../skills/ai-governance/SKILL.md) (control catalog step)
- **Inputs:** classification tier; risk assessment; DPIA mitigations.
- **Actions:** assemble the control set proportionate to tier: baseline for all systems (inventory currency, acceptable-use rules, output-handling guidance, incident route); plus for personal-data systems (DPIA mitigations, data minimization in prompts/logs, retention limits); plus for high-risk (documented human oversight with real override authority, logging sufficient for reconstruction, pre-deployment testing including adversarial testing, accuracy monitoring, technical documentation, user-facing transparency). Assign each control an owner and an evidence artifact. Where [NIST AI RMF](../context/frameworks/nist-ai-rmf.md) or [ISO/IEC 42001](../context/frameworks/iso-42001-ai-management.md) structures the org's AI program, map the control set to it rather than inventing a parallel scheme; [CSA's AI Controls Matrix](../context/frameworks/csa-ccm-star.md) and the [OWASP GenAI material](../context/frameworks/owasp-application-security.md) are control-level sources for the technical layer.
- **Outputs:** control requirements list with owners; implementation status tracked to done.

### 6. Vendor assessment (third-party systems only) — grc-analyst

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md), AI-specific module from [ai-governance](../skills/ai-governance/SKILL.md)
- **Inputs:** vendor documentation; contract drafts.
- **Actions:** run the [vendor-onboarding workflow](vendor-onboarding.md) with AI-specific additions: does the vendor train on customer data (and can it be disabled contractually), data residency and subprocessor model chain, model change notification commitments, transparency/documentation sufficient for our own deployer obligations, and indemnities for output-related claims. For vendor-embedded AI features in an already-onboarded product, a delta assessment of the feature suffices — but it must actually happen.
- **Outputs:** vendor assessment; AI-specific contract requirements.

### 7. Approval gate — authority per matrix (ai-governance-lead for low tiers; committee for high)

- **Skill:** [ai-governance](../skills/ai-governance/SKILL.md) (approval step)
- **Inputs:** complete package: inventory entry, classification, DPIA/screening, risk assessment, control status, vendor assessment.
- **Actions:** approve / approve-with-conditions / reject, recorded with rationale. Conditions get owners and dates and are tracked to closure — an unmet condition past its date suspends the approval. Residual risks above appetite route through [exception-management](../skills/exception-management/SKILL.md) with the approver the appetite statement requires.
- **Outputs:** recorded approval decision; conditions tracker; inventory status → "approved" or "rejected."
- **Decision gate:** no production use before approval. Pilots with real data are production for this purpose.

### 8. Monitoring registration — grc-analyst

- **Skill:** [ai-governance](../skills/ai-governance/SKILL.md) (monitoring step)
- **Inputs:** approval record; control set.
- **Actions:** register the system for ongoing oversight: periodic review cadence by tier (high-risk at least annually), re-intake triggers (model change, new data source, new use case, vendor feature changes), incident routing for AI-specific failures (harmful outputs, suspected bias, data leakage) into both IR and, where reportable, [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md), and performance/drift monitoring ownership for high-risk systems.
- **Outputs:** monitoring plan in inventory; intake closed.

## Outputs summary

| Output | Step | Record |
|--------|------|--------|
| Inventory entry + fact base | 1 | AI inventory |
| AI Act classification + rationale | 2 | AI inventory |
| DPIA screening / DPIA | 3 | Privacy records (Art. 30/35 evidence) |
| Risk assessment | 4 | Risk register |
| Control requirements + status | 5 | Control inventory |
| Vendor assessment (if third-party) | 6 | Vendor file |
| Approval decision + conditions | 7 | Governance record |
| Monitoring plan | 8 | AI inventory |

## Failure modes

- **Feature-flag blindness.** Vendor flips on an AI feature in an existing product; nobody runs intake because "we already assessed that vendor." Make vendor AI-feature enablement an explicit trigger.
- **Classification by aspiration.** Classifying on the sanitized intake form rather than the actual design; the "internal productivity tool" that actually scores job applicants is high-risk however it is described.
- **DPIA as paperwork after the fact.** Running the DPIA post-launch, which forfeits its design influence and, where Art. 36 consultation would have been required, creates an unlawful-processing problem no retrofit fixes.
- **Approval without conditions tracking.** Conditional approvals whose conditions nobody revisits — functionally unconditional approvals with better optics. Suspend on overdue conditions.
- **One-time gate.** Treating intake as the end. Models drift, vendors swap models, use cases creep. Step 8's re-intake triggers are what makes the register truthful in a year.
- **Parallel AI bureaucracy.** A separate AI risk scale, separate register, and separate committee disconnected from enterprise risk governance — high-risk AI decisions end up invisible to the people accountable for enterprise risk. Reuse the standard methodology and registers throughout.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
