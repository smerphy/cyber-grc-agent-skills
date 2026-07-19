# Data Protection Impact Assessment (DPIA)

**How to use:** Aligned to GDPR Art. 35. Complete the screening first; if a DPIA is required, work through every section — the risk table in Section 6 is the core. For the full method, screening criteria, and question bank, use [../skills/dpia-privacy-assessment/SKILL.md](../skills/dpia-privacy-assessment/SKILL.md); for GDPR context, [../context/regulations/gdpr.md](../context/regulations/gdpr.md). Adapt terminology when using this for non-GDPR privacy impact assessments (e.g., US state laws — see [../context/regulations/us-state-privacy.md](../context/regulations/us-state-privacy.md)).

## Document control

| Attribute | Value |
|---|---|
| DPIA ID | [DPIA-YYYY-NNN] |
| Processing activity | [Name, and ROPA reference if held] |
| Assessor | [Role] |
| DPO consulted | [Name/role, date] |
| Version / date | [1.0 / YYYY-MM-DD] |
| Status | [Draft / DPO review / Approved / Prior consultation] |

## 1. Screening result

*Art. 35(1) requires a DPIA where processing is "likely to result in a high risk" to individuals, in particular Art. 35(3): (a) systematic and extensive automated evaluation/profiling with legal or similarly significant effects; (b) large-scale processing of special categories (Art. 9) or criminal-offence data (Art. 10); (c) systematic large-scale monitoring of publicly accessible areas. Also check your supervisory authority's published Art. 35(4) list.*

| Question | Answer | Notes |
|---|---|---|
| Does the processing meet an Art. 35(3) criterion or an item on the supervisory authority's list? | [Y/N] | [Which one] |
| Does it meet two or more high-risk indicators (e.g., evaluation/scoring, systematic monitoring, sensitive data, large scale, matching/combining datasets, vulnerable subjects, innovative technology, blocking access to a service)? | [Y/N] | [Which indicators] |
| **Screening outcome** | [DPIA required / not required] | [If not required, record rationale and stop; retain this screening] |

## 2. Description of the processing

*Art. 35(7)(a): systematic description of the envisaged processing and its purposes, including legitimate interest where relied on.*

- **Purpose(s) and lawful basis:** [Purpose; Art. 6 basis; Art. 9 condition if special categories]
- **Data categories:** [Be exhaustive; flag special categories and children's data]
- **Data subjects:** [Categories and approximate numbers; note vulnerable groups]
- **Data flows:** [Source → systems → outputs. Attach or link a flow diagram; name every system that stores or transits the data]
- **Retention:** [Period per data category and deletion mechanism — "indefinite" is a finding, not an answer]
- **Recipients:** [Internal roles, processors, third-party controllers]
- **International transfers:** [Destinations; transfer mechanism (adequacy decision, SCCs + transfer impact assessment, BCRs); or "none"]
- **Technology:** [Anything novel: AI/ML, biometrics, tracking. If AI is involved, also run applicability against the [EU AI Act](../context/regulations/eu-ai-act.md) and consider [../skills/ai-governance/SKILL.md](../skills/ai-governance/SKILL.md)]

## 3. Consultation record

*Art. 35(9): seek the views of data subjects or their representatives where appropriate. Record who was consulted (data subjects, works council, user research, DPO, security, the processor), when, what they said, and — if data subjects were not consulted — why not.*

| Party | Date | Method | Views expressed / rationale for not consulting |
|---|---|---|---|
| | | | |

## 4. Necessity and proportionality

*Art. 35(7)(b): assess necessity and proportionality relative to the purposes.*

- **Necessity:** [Could the purpose be achieved with less data, shorter retention, or without the intrusive element? If yes, why was that not chosen?]
- **Proportionality:** [Is the intrusion proportionate to the benefit? Consider data minimization, purpose limitation, transparency to subjects, and how each data subject right (access, erasure, objection, portability, rights related to automated decisions) will be honored in practice.]

## 5. Measures already envisaged

*Security and data protection measures designed into the processing (Art. 32 measures, pseudonymization, access control, encryption, DPAs with processors). These feed the "mitigations" column below.*

## 6. Risks to individuals

*Art. 35(7)(c). Assess risk **to the data subjects**, not to the organization. Likelihood and severity: use a defined scale (e.g., remote/possible/probable × minimal/significant/severe) — see [../context/risk-scoring.md](../context/risk-scoring.md) for scale discipline.*

| # | Risk to individuals | Likelihood | Severity | Mitigations (existing + planned) | Residual risk | Accepted? |
|---|---|---|---|---|---|---|
| 1 | Re-identification of pseudonymized wellness-survey responses by HR analysts, exposing health-related information to employer decision-makers | Possible | Severe | Aggregation threshold of n≥10 before results are visible; pseudonymization keys held by external processor only; HR access limited to aggregate dashboard; access logged and reviewed quarterly | Low | Y — DPO concurs |
| 2 | [Risk] | | | | | |

*Worked example above shows the standard: a concrete harm to identifiable people, mitigations that address that specific harm, and an explicit residual call.*

## 7. Sign-off and outcomes

| Item | Record |
|---|---|
| DPO advice (Art. 35(2)) | [Verbatim summary of the DPO's advice, date] |
| DPO advice followed? | [Y/N — if not, document the reasons] |
| Residual high risk remaining? | [Y/N] |
| **Prior consultation determination** | [If residual high risk remains unmitigated, prior consultation with the supervisory authority is required under Art. 36 **before** processing starts. Record the determination, and if triggered: authority, submission date, response.] |
| Approved by | [Role, date] |
| Review trigger | [Date or change condition — reassess when the processing changes materially] |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
