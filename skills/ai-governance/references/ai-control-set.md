# Starter AI Control Catalog

Twenty-two AI-specific controls to seed an AI governance program. Each is mapped to NIST AI RMF 1.0 functions (GV = Govern, MP = Map, MS = Measure, MG = Manage) and ISO/IEC 42001:2023 Annex A areas. Select proportionately: the "Core" tier applies to any organization using AI in decisions about people or in customer-facing products; "Extended" adds depth for high-risk systems and AI builders. These controls complement — never replace — the existing security control set (access control, SDLC, logging, vendor management still apply to AI systems as ordinary IT systems).

ISO 42001 Annex A area key: A.2 AI policies; A.3 internal organization; A.4 resources for AI systems; A.5 assessing impacts of AI systems; A.6 AI system life cycle; A.7 data for AI systems; A.8 information for interested parties; A.9 use of AI systems; A.10 third-party and customer relationships.

## Governance and accountability

| ID | Control | Tier | AI RMF | ISO 42001 | Evidence examples |
|---|---|---|---|---|---|
| AI-01 | An approved AI policy defines permitted and prohibited AI uses, risk tiers, approval gates, and roles. Reviewed at least annually. | Core | GV | A.2 | Policy doc, approval record, review log |
| AI-02 | A named accountable owner exists for the AI governance program; each AI system has a named business owner and (where built in-house) a technical owner. | Core | GV | A.3 | RACI, inventory owner column |
| AI-03 | A complete AI system inventory is maintained covering built, bought, embedded, and internal LLM use; refreshed at least quarterly and gated into procurement and SDLC intake. | Core | GV, MP | A.6, A.9 | Inventory register, discovery method doc, procurement checklist |
| AI-04 | Each AI system is risk-classified (EU AI Act tier or equivalent internal scheme) with documented rationale before deployment and on material change. | Core | MP | A.5 | Classification records with rationale |
| AI-05 | Staff who develop, approve, or operate AI systems receive role-appropriate AI training (AI Act Art. 4 literacy at minimum; deeper for oversight roles). | Core | GV | A.3 | Training content, completion records |
| AI-06 | AI risks are recorded in the enterprise risk register using standard scales; AI risk acceptance follows the standard exception process with expiry. | Core | GV, MG | A.5 | Register extract, exception records |

## System lifecycle

| ID | Control | Tier | AI RMF | ISO 42001 | Evidence examples |
|---|---|---|---|---|---|
| AI-07 | Every AI system has model/system documentation: intended purpose, out-of-scope uses, model provenance, training-data description, known limitations, performance metrics. Kept current. | Core | MP, MS | A.4, A.6 | Model cards / system docs |
| AI-08 | Pre-deployment testing is performed and recorded against defined acceptance criteria: accuracy/quality, robustness, and — wherever outputs affect people — bias/fairness testing across relevant groups. | Core | MS | A.6 | Test plans, results, sign-off |
| AI-09 | An impact assessment is completed before deploying AI that affects individuals (privacy DPIA where personal data is processed; fundamental-rights/algorithmic impact assessment for high-risk uses). | Core | MP | A.5 | DPIA/FRIA records |
| AI-10 | Changes to models, training data, prompts/system instructions, and key parameters follow change management: reviewed, tested, approved, rollback-capable, logged. | Core | MG | A.6 | Change tickets, prompt version history |
| AI-11 | Deployed AI systems are monitored in production for performance degradation, drift, and anomalous behavior against defined thresholds; breaches trigger a defined response incl. suspension authority. | Core | MS, MG | A.6 | Monitoring dashboards, threshold doc, incident tickets |
| AI-12 | AI system inputs and outputs are logged to a level supporting traceability of consequential decisions and incident investigation, with retention meeting legal duties (e.g., AI Act deployer log retention of at least six months for high-risk systems). | Core | MS, MG | A.6 | Log config, retention schedule |
| AI-13 | Decommissioning of an AI system covers model artifact disposal, data disposition, dependent-process handover, and inventory update. | Extended | MG | A.6 | Decommission checklist |

## Human oversight and use

| ID | Control | Tier | AI RMF | ISO 42001 | Evidence examples |
|---|---|---|---|---|---|
| AI-14 | Consequential decisions supported by AI have defined human-oversight points; overseers have documented competence, authority to override or halt, and their intervention rate is monitored (to detect rubber-stamping). | Core | GV, MG | A.9 | Oversight design doc, override logs, intervention metrics |
| AI-15 | An internal LLM/genAI acceptable-use standard is published, covering approved tools, data-input rules, and output-review duties (see [llm-usage-policy-elements.md](llm-usage-policy-elements.md)); compliance is monitored. | Core | GV | A.2, A.9 | Standard, attestation records, DLP/egress reports |
| AI-16 | Users and affected persons are informed of AI interaction and AI-generated content where required (AI Act Art. 50, consumer law); synthetic content is marked. | Core | GV | A.8 | UI disclosures, content-marking config |
| AI-17 | A channel exists for affected persons and employees to contest AI-influenced decisions and report AI concerns; cases are tracked to resolution. | Extended | MG | A.8 | Appeals procedure, case log |

## Data and third parties

| ID | Control | Tier | AI RMF | ISO 42001 | Evidence examples |
|---|---|---|---|---|---|
| AI-18 | Data used to train, fine-tune, or ground AI systems is governed: documented provenance and lawful basis, quality and representativeness checks, bias examination, and access control on training corpora and vector stores. | Core | MP, MS | A.7 | Data sheets, lineage records, RAG corpus ACLs |
| AI-19 | Rules define which data classifications may be sent to which AI services under which contracts; enforced technically where feasible (egress controls, DLP, gateway/proxy for LLM APIs). | Core | GV, MG | A.7, A.9 | Data-flow matrix, gateway config |
| AI-20 | AI vendors and AI-enabled features pass third-party risk assessment with AI-specific due diligence (training on customer data, prompt retention, model provenance, sub-processors, AI Act role/tier) and contract clauses (no training on customer data without consent, incident notice, audit rights). | Core | GV, MG | A.10 | TPRM records, contract clauses |

## LLM-specific security

| ID | Control | Tier | AI RMF | ISO 42001 | Evidence examples |
|---|---|---|---|---|---|
| AI-21 | LLM applications that process untrusted content or can invoke tools/actions are assessed for prompt-injection and excessive-agency exposure before release and on significant change; mitigations (privilege limits on tools, input/output filtering, isolation of untrusted content from instructions, human approval for high-impact actions) are documented and tested, including adversarial testing for higher-risk apps. | Core | MS, MG | A.6 | Threat model, red-team/test reports, tool permission config |
| AI-22 | LLM outputs used in consequential decisions, code deployed to production, or external publication undergo defined review (human or validated automated checks); RAG systems require grounding/citation so reviewers can verify claims. | Core | MG | A.9 | Review procedure, spot-check records |

## Selection guidance

- **Everyone using AI at all**: AI-01 through AI-06, AI-15, AI-19, AI-20.
- **AI in decisions about people or customer-facing AI**: add AI-07 through AI-12, AI-14, AI-16, AI-22.
- **Building LLM apps with tools/RAG**: add AI-21, AI-18.
- **High-risk (EU AI Act) systems**: full set including Extended tier; map each control to the specific article it evidences (e.g., AI-08 → Art. 15, AI-14 → Art. 14/26, AI-12 → Art. 12/26) — see [eu-ai-act-obligations.md](eu-ai-act-obligations.md).

Test these controls through the standard program: design and operating-effectiveness testing per [../../control-testing/SKILL.md](../../control-testing/SKILL.md); coverage and exception metrics per [../../grc-metrics-reporting/SKILL.md](../../grc-metrics-reporting/SKILL.md).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
