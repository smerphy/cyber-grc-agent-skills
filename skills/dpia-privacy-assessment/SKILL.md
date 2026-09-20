---
name: dpia-privacy-assessment
description: >-
  Conducts Data Protection Impact Assessments under GDPR Art. 35 and general
  privacy impact assessments (PIAs). Screens whether a DPIA is required,
  documents the processing, assesses necessity/proportionality and risks to
  data subjects, and produces a decision-ready DPIA report. Use when a user
  says "DPIA", "PIA", "privacy impact assessment", "do we need a DPIA",
  "assess this new processing/system/feature for privacy risk", or before
  launching processing involving profiling, monitoring, or sensitive data.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Run a defensible DPIA end-to-end: determine whether one is legally required, describe the processing systematically, evaluate necessity and proportionality, assess risks **to data subjects** (not to the organization), select mitigations, and conclude — including whether prior consultation with the supervisory authority under GDPR Art. 36 is triggered. The same procedure covers non-GDPR privacy impact assessments (US state "data protection assessments", internal PIAs) with the screening step swapped for the applicable trigger list.

## When to use

- A new system, product feature, vendor tool, or processing activity involves personal data and someone must decide whether a DPIA/PIA is needed — or must actually write one.
- Existing processing changes materially (new purpose, new data categories, new technology such as AI/ML, new recipients or transfers) — GDPR Art. 35(11) requires review when risk changes.
- A US state privacy law data protection assessment is required (targeted advertising, sale of personal data, profiling with significant effects, sensitive data — see [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md)), or a US sectoral rule is in play for children's, health, education or biometric data ([us-coppa.md](../../context/regulations/us-coppa.md), [us-ftc-act-health-breach-rule.md](../../context/regulations/us-ftc-act-health-breach-rule.md), [us-ferpa-education-privacy.md](../../context/regulations/us-ferpa-education-privacy.md), [us-biometric-privacy-laws.md](../../context/regulations/us-biometric-privacy-laws.md)).
- Another jurisdiction imposes its own impact-assessment duty — among others [UK GDPR as amended by the DUAA](../../context/regulations/uk-data-protection.md), [India's significant data fiduciary DPIA](../../context/regulations/india-dpdp-cert-in.md), [Quebec's Law 25 PIA](../../context/regulations/canada-pipeda-law-25.md), [South Africa's PIIA](../../context/regulations/south-africa-popia.md), [Korea's public-institution PIA](../../context/regulations/south-korea-pipa.md), [China's PIPL impact assessment](../../context/regulations/china-pipl-dsl-csl.md) and [Brazil's LGPD impact report (RIPD)](../../context/regulations/brazil-lgpd.md). Run the same procedure with that regime's screening triggers in place of Art. 35(3).
- **Not for:** general (non-privacy) risk assessment of a system — use [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md). AI-specific governance and EU AI Act classification — use [../ai-governance/SKILL.md](../ai-governance/SKILL.md) (an AI system will often need both; the DPIA and AI assessment cross-reference each other). Deciding which privacy laws apply at all — use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) first.

## Inputs to gather

Ask for these before starting; do not guess:

1. **Processing description**: what data, about whom, collected how, for what purposes, using what systems/vendors. A data-flow diagram or written flow if available.
2. **Data categories**: specifically whether any GDPR Art. 9 special categories (health, biometrics for identification, sex life/orientation, racial/ethnic origin, political/religious/philosophical beliefs, trade-union membership, genetic data) or Art. 10 criminal-offence data are involved.
3. **Data subjects**: who they are, approximate number, and whether any are vulnerable (children, employees, patients, asylum seekers, elderly).
4. **Lawful basis** claimed for each purpose, and retention periods (or admission that none are defined — record that as a finding, not a blocker).
5. **Recipients and transfers**: processors, sub-processors, group companies, third countries and the transfer mechanism relied on.
6. **Technology characteristics**: automated decision-making, profiling, AI/ML, tracking, monitoring, matching of datasets, novel tech.
7. **Existing controls**: security measures, access model, pseudonymization/encryption, DPO involvement to date.
8. **Jurisdiction and role**: controller or processor; which regimes apply (GDPR, UK GDPR, US state laws, others).

## Procedure

1. **Screen: is a DPIA required?**
   - Check GDPR Art. 35(3) mandatory triggers: (a) systematic and extensive automated evaluation/profiling producing legal or similarly significant effects; (b) large-scale processing of special categories (Art. 9) or criminal-offence data (Art. 10); (c) systematic monitoring of a publicly accessible area on a large scale.
   - Score the processing against the nine WP248 rev.01 criteria (endorsed by the EDPB): evaluation/scoring; automated decision-making with legal or similar significant effect; systematic monitoring; sensitive or highly personal data; large scale; matching/combining datasets; vulnerable data subjects; innovative use or new technology; processing that prevents subjects from exercising a right or accessing a service/contract. **Rule of thumb: two or more criteria met → DPIA required; one criterion can suffice where the risk is clearly high.**
   - Check the relevant supervisory authority's Art. 35(4) mandatory-DPIA list and any Art. 35(5) exemption list for the member state(s) concerned.
   - Detailed criteria, borderline calls, and worked examples: [references/dpia-screening.md](references/dpia-screening.md).
   - **Decision point:** DPIA required → continue. Not required → still record the screening decision and rationale (regulators expect a documented negative screening). Borderline → do the DPIA; the cost of an unnecessary DPIA is lower than the cost of a missing one.
2. **Describe the processing systematically** (Art. 35(7)(a)). Document: nature (operations performed, data flow source → storage → use → disclosure → deletion), scope (data categories, volume, subjects, geography, retention), context (relationship with subjects, their reasonable expectations, prior incidents, public concern), and purposes (including the legitimate interest where that basis is claimed). One row per purpose in the processing table — a single system frequently serves multiple purposes with different lawful bases.
3. **Assess necessity and proportionality** (Art. 35(7)(b)). For each purpose answer: Is the processing necessary to achieve it, or would a less intrusive means work? Is each data element needed (data minimization)? Is retention justified per element? Is the lawful basis valid and correctly matched (consent must be freely given — problematic for employees; legitimate interests requires the three-part test)? Are Arts. 13/14 transparency, data-subject rights handling, processor contracts (Art. 28), and transfer mechanisms ([eu-gdpr-international-transfers.md](../../context/regulations/eu-gdpr-international-transfers.md)) in place? Record gaps as compliance findings distinct from risk findings.
4. **Assess risks to data subjects** (Art. 35(7)(c)). **Common error — call it out explicitly if the draft does it: a DPIA assesses risk to the rights and freedoms of individuals, not risk to the organization.** "Regulatory fine" and "reputational damage to the company" do not belong in this section. For each risk: identify the threat event (illegitimate access, unwanted modification, data disappearance, but also *intended* processing that harms — e.g., discriminatory profiling working exactly as designed), the harm to individuals (discrimination, financial loss, identity theft, reputational damage, physical harm, chilling effects on speech/behavior, loss of control over data), then rate severity and likelihood using the anchors in [references/risk-to-individuals.md](references/risk-to-individuals.md). Assess inherent risk first, then residual risk after existing controls.
5. **Identify measures to address the risks** (Art. 35(7)(d)). For each risk above tolerance: mitigations mapped to the risk (minimization, pseudonymization, encryption, access restriction, retention shortening, human review of automated decisions, transparency improvements, opt-outs, DPO oversight). Record owner and deadline per measure. Re-rate residual risk after planned measures.
6. **Document consultation.** DPO advice is mandatory where a DPO is appointed (Art. 35(2)) — record it verbatim or summarized, with the DPO's name and date, and whether it was followed. Seek the views of data subjects or their representatives "where appropriate" (Art. 35(9)) — surveys, works councils, user research; if not sought, document why (e.g., disproportionate effort, confidentiality) rather than staying silent. Processors must assist (Art. 28(3)(f)) — record their input on security measures.
7. **Conclude and route the outcome.**
   - **Decision point:** If residual risk remains **high** after all feasible mitigations, the controller must consult the supervisory authority **before** processing starts (Art. 36 prior consultation; the authority has 8 weeks to respond, extendable by a further 6 weeks). Do not launch while consultation is pending. In practice, most organizations treat unresolved high residual risk as a signal to redesign the processing rather than consult.
   - Otherwise: obtain sign-off from the accountability owner (not the DPO — the DPO advises, the controller decides), set a review date and review triggers (Art. 35(11): change in risk, new purposes, incidents, regulatory change), and file the DPIA where it is retrievable for accountability (Art. 5(2)).
   - Feed accepted residual risks into the enterprise register via [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md); route any deliberately accepted non-conformity through [../exception-management/SKILL.md](../exception-management/SKILL.md).

## Output format

Deliver the DPIA using [../../templates/dpia-template.md](../../templates/dpia-template.md). Required sections, in order:

1. Screening decision and rationale (criteria met, with evidence)
2. Systematic description of processing (incl. data-flow narrative or diagram, processing table: purpose | data categories | subjects | lawful basis | retention | recipients | transfers)
3. Necessity and proportionality assessment
4. Risks to data subjects (risk table: ID | threat event | harm to individuals | severity | likelihood | inherent rating | existing controls | residual rating)
5. Measures to address risks (measure | risk IDs addressed | owner | deadline | post-measure residual)
6. Consultation record (DPO, data subjects, processors)
7. Conclusion: sign-off, Art. 36 determination, review date and triggers

Worked example (risk table rows — note the harms are to individuals):

| ID | Threat event | Harm to individuals | Sev | Lik | Inherent | Residual |
|----|---|---|---|---|---|---|
| R1 | Wellness-app health data disclosed to employer via analytics integration | Employment discrimination; distress; chilling effect on app use | Significant | Possible | High | Medium (integration disabled; contract amended) |
| R2 | Credit-scoring model produces systematically worse scores for a protected group | Financial exclusion; discrimination | Significant | Likely | High | Medium (bias testing pre-release + quarterly; human review of declines) |

## Quality checklist

- [ ] Screening decision documented with named criteria and rationale — including when the answer is "no DPIA needed"
- [ ] Every purpose has a stated lawful basis and retention period, or an explicit finding that one is missing
- [ ] Risk section contains **zero** organization-centric risks (no fines, no company reputation); every harm names an effect on individuals
- [ ] Both security failures **and** harms from the processing working as intended are considered
- [ ] Severity/likelihood ratings use the anchors in references/risk-to-individuals.md, not gut feel
- [ ] Every above-tolerance risk has at least one mitigation with an owner and deadline
- [ ] DPO advice recorded (or absence of DPO noted); data-subject consultation done or its omission justified
- [ ] Art. 36 prior-consultation determination stated explicitly (triggered / not triggered, and why)
- [ ] Sign-off by the controller's accountable owner; review date and triggers set
- [ ] If the system includes AI/ML, cross-reference to the AI governance assessment exists

## References

- [references/dpia-screening.md](references/dpia-screening.md) — screening criteria in depth, with examples that do and do not trigger a DPIA
- [references/risk-to-individuals.md](references/risk-to-individuals.md) — harm taxonomy and severity/likelihood anchors for risks to data subjects
- [../../templates/dpia-template.md](../../templates/dpia-template.md) — DPIA report template
- **EU/EEA and UK privacy law:** [gdpr.md](../../context/regulations/gdpr.md) · [eu-gdpr-international-transfers.md](../../context/regulations/eu-gdpr-international-transfers.md) · [eu-eprivacy.md](../../context/regulations/eu-eprivacy.md) · [eu-ehds.md](../../context/regulations/eu-ehds.md) · [eu-ai-act.md](../../context/regulations/eu-ai-act.md) · [uk-data-protection.md](../../context/regulations/uk-data-protection.md) · [switzerland-fadp-isa.md](../../context/regulations/switzerland-fadp-isa.md)
- **US privacy law:** [us-state-privacy.md](../../context/regulations/us-state-privacy.md) · [us-biometric-privacy-laws.md](../../context/regulations/us-biometric-privacy-laws.md) · [us-coppa.md](../../context/regulations/us-coppa.md) · [us-ferpa-education-privacy.md](../../context/regulations/us-ferpa-education-privacy.md) · [us-ftc-act-health-breach-rule.md](../../context/regulations/us-ftc-act-health-breach-rule.md) · [hipaa.md](../../context/regulations/hipaa.md) · [glba-ftc-safeguards.md](../../context/regulations/glba-ftc-safeguards.md) · [us-state-ai-laws.md](../../context/regulations/us-state-ai-laws.md) · [us-doj-bulk-data-rule.md](../../context/regulations/us-doj-bulk-data-rule.md)
- **Asia-Pacific privacy law:** [china-pipl-dsl-csl.md](../../context/regulations/china-pipl-dsl-csl.md) · [japan-appi-cyber.md](../../context/regulations/japan-appi-cyber.md) · [south-korea-pipa.md](../../context/regulations/south-korea-pipa.md) · [india-dpdp-cert-in.md](../../context/regulations/india-dpdp-cert-in.md) · [singapore-pdpa-cybersecurity.md](../../context/regulations/singapore-pdpa-cybersecurity.md) · [southeast-asia-privacy-regimes.md](../../context/regulations/southeast-asia-privacy-regimes.md) · [hong-kong-pdpo-critical-infrastructure.md](../../context/regulations/hong-kong-pdpo-critical-infrastructure.md) · [australia-privacy-act.md](../../context/regulations/australia-privacy-act.md) · [new-zealand-privacy-act.md](../../context/regulations/new-zealand-privacy-act.md)
- **Americas, Middle East, Africa privacy law:** [canada-pipeda-law-25.md](../../context/regulations/canada-pipeda-law-25.md) · [brazil-lgpd.md](../../context/regulations/brazil-lgpd.md) · [latin-america-privacy-regimes.md](../../context/regulations/latin-america-privacy-regimes.md) · [israel-privacy-protection-law.md](../../context/regulations/israel-privacy-protection-law.md) · [saudi-arabia-pdpl-nca.md](../../context/regulations/saudi-arabia-pdpl-nca.md) · [uae-data-protection-cyber.md](../../context/regulations/uae-data-protection-cyber.md) · [south-africa-popia.md](../../context/regulations/south-africa-popia.md) · [africa-privacy-regimes.md](../../context/regulations/africa-privacy-regimes.md) · [other-jurisdictions.md](../../context/regulations/other-jurisdictions.md)
- **Privacy management frameworks:** [iso-27701-privacy-management.md](../../context/frameworks/iso-27701-privacy-management.md) · [nist-privacy-framework.md](../../context/frameworks/nist-privacy-framework.md) · [iso-27017-27018-cloud.md](../../context/frameworks/iso-27017-27018-cloud.md)
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — qualitative matrices and aggregation pitfalls
- [../ai-governance/SKILL.md](../ai-governance/SKILL.md) — AI system classification and controls (run alongside a DPIA for AI systems)
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — enterprise risk register intake for residual risks
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — determining which privacy regimes apply
- [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) — breach notification duties for the processing assessed here

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
