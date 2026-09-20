# Workflow: Vendor Security Onboarding

```yaml
name: vendor-onboarding
description: >-
  Security and compliance onboarding for a new third party: structured intake,
  risk tiering, tier-proportionate assessment, findings translated into contract
  requirements, formal risk acceptance where gaps remain, and continuous
  monitoring setup before the vendor goes live.
skills_used:
  - third-party-risk-assessment
  - risk-assessment
  - exception-management
typical_duration: 3-10 business days for low tiers; 3-6 weeks for critical vendors
roles:
  - grc-analyst
  - risk-manager
  - privacy-officer
```

## Trigger

- Procurement or a business owner requests a new vendor, SaaS tool, or service provider.
- An existing vendor's use materially expands (new data categories, new integration, new business criticality) — re-run from step 2.
- Shadow-IT discovery surfaces a vendor already in use without assessment — run the workflow retroactively and treat the in-use period as a finding.

## Prerequisites

- A tiering scheme with defined criteria (data sensitivity, access level, business criticality, substitutability). If none exists, define one first — see [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md).
- A named business owner for the vendor relationship; no owner, no onboarding.
- Standard contract security schedule / DPA templates available from legal.
- A vendor inventory system of record (a spreadsheet qualifies).

## Steps

### 1. Intake — grc-analyst, with the requesting business owner

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (intake questionnaire)
- **Inputs:** business owner's description of the use case.
- **Actions:** capture the facts that drive tiering: what service, what data categories and volumes the vendor will store/process/access, integration and network access model, user population, business process supported, and whether the vendor uses subprocessors. Verify answers against the actual solution design, not the sales deck. If personal data is involved, flag for the privacy-officer (DPA, transfer mechanism — see [EU international transfers](../context/regulations/eu-gdpr-international-transfers.md), and the [US DOJ data security program](../context/regulations/us-doj-bulk-data-rule.md) where the arrangement could give a country of concern access to bulk US sensitive personal data — and possible [DPIA screening](../skills/dpia-privacy-assessment/SKILL.md)).
- **Outputs:** completed intake record in the vendor inventory.

### 2. Tiering — grc-analyst, tier confirmed by risk-manager

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (tiering step)
- **Inputs:** intake record; tiering criteria.
- **Actions:** apply the tiering rubric mechanically; document the driving factor. Typical result: Tier 1 (critical) / Tier 2 (high) / Tier 3 (medium) / Tier 4 (low). Regulated contexts may force a floor — e.g., an ICT provider supporting a critical function under [DORA](../context/regulations/dora.md) (register-of-information and contractual content requirements sit in its [technical standards](../context/regulations/eu-dora-technical-standards.md)), a service provider in scope of the [US banking third-party and notification rules](../context/regulations/us-banking-incident-notification-third-party.md), or a subprocessor of regulated data, cannot tier below Tier 2 (high).
- **Outputs:** assigned tier with rationale.
- **Decision gate:** Tier 4 (low) vendors with no sensitive data and no access skip to step 6 with a lightweight terms check. Everything else proceeds to step 3.

### 3. Assessment by tier — grc-analyst

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md)
- **Inputs:** tier; vendor-provided evidence (questionnaire responses, SOC 2 report, ISO 27001 certificate, penetration test summary, security whitepaper).
- **Actions:** scale depth to tier. Tier 3 (medium): questionnaire plus certificate validation. Tier 2 (high): full questionnaire, SOC 2 Type II report review (read the exceptions, the CUECs, and the scope — a certificate logo is not assurance; see [SOC 2 TSC](../context/frameworks/soc2-tsc.md)), subprocessor list review. Tier 1 (critical): all of the above plus architecture review, resilience/exit analysis, and a call with the vendor's security team. Check the assessed scope actually covers the service being bought. Read each attestation against what it is actually an opinion on: [SOC 1 / ISAE 3402](../context/frameworks/soc1-isae3402-soc-reports.md) where the service touches financial reporting rather than security, [ISO 27017/27018](../context/frameworks/iso-27017-27018-cloud.md) and [CSA CCM, CAIQ and STAR](../context/frameworks/csa-ccm-star.md) for cloud-specific coverage and shared-responsibility boundaries, and the scheme's own pack where the vendor claims [FedRAMP](../context/frameworks/fedramp.md), [HITRUST](../context/frameworks/hitrust-csf.md), [TISAX](../context/frameworks/tisax-vda-isa.md), [BSI C5](../context/frameworks/germany-bsi-it-grundschutz-c5.md) or [Cyber Essentials](../context/frameworks/uk-cyber-essentials-ncsc-caf.md) — the packs state what each one certifies, attests or merely self-declares.
- **Outputs:** assessment report with findings rated by severity, and complementary user entity controls we must operate.

### 4. Findings disposition and contract requirements — grc-analyst with legal, risk-manager on severity calls

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md); [risk-assessment](../skills/risk-assessment/SKILL.md) for scoring material findings
- **Inputs:** assessment report; standard contract security schedule.
- **Actions:** disposition each finding: (a) vendor remediates pre-contract, (b) contractual control (security schedule clause, audit rights, breach notification SLA, subprocessor approval rights, termination/exit assistance), (c) compensating control on our side, or (d) risk acceptance candidate. Score material residual findings so the acceptance decision in step 5 is made on stated risk, not adjectives. Ensure breach-notification clauses are compatible with our own regulatory clocks (see [breach notification timelines](../context/crosswalks/breach-notification-timelines.md)) — a vendor SLA of "30 days" is useless against a 72-hour obligation.
- **Outputs:** findings disposition table; contract requirements list handed to legal/procurement.

### 5. Risk acceptance (conditional) — risk-manager approves; business owner sponsors

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** unresolved findings from step 4 with risk scores.
- **Actions:** only reached when material findings remain after negotiation. The business owner sponsors the acceptance; approval authority follows the risk level per the appetite statement — the grc-analyst never self-approves. Acceptance is time-bound, linked to the vendor record and the risk register, and carries review conditions (e.g., re-assess at renewal or when the vendor remediates).
- **Outputs:** signed, time-bound risk acceptance; register entry.
- **Decision gate:** if the required approver declines, the vendor is rejected or the deal is renegotiated. Declined acceptance is a valid and recorded outcome.

### 6. Monitoring setup and go-live — grc-analyst

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (ongoing monitoring step)
- **Inputs:** tier; contract terms; findings disposition.
- **Actions:** before go-live, record in the vendor inventory: tier, reassessment cadence (Tier 1 annual; Tier 2 every 12-18 months; Tier 3 every 24 months; Tier 4 trigger-based), evidence expiry dates (SOC 2 period end, certificate expiry), contractual review triggers, and the operational monitoring hooks (breach notification contact path, subprocessor change notifications, service/security bulletin subscriptions). Confirm our side of the complementary user entity controls is actually implemented.
- **Outputs:** vendor live in inventory with monitoring schedule; onboarding record closed.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Intake record | 1 | Vendor inventory |
| Tier + rationale | 2 | Vendor inventory |
| Assessment report | 3 | Vendor file (audit evidence) |
| Findings disposition + contract requirements | 4 | Vendor file; contract |
| Risk acceptance (if any) | 5 | Exception register + risk register |
| Monitoring schedule | 6 | Vendor inventory |

## Failure modes

- **Assessment after signature.** Procurement signs, then asks security. All leverage for contract requirements (step 4) is gone. Wire the workflow into procurement so no PO issues without a closed step 4.
- **Certificate worship.** Accepting an ISO 27001 certificate or SOC 2 logo without reading scope, period, and exceptions. The service you buy may be entirely outside the assessed scope.
- **Questionnaire theater.** 300-question questionnaires nobody reads, answered by vendor sales. Fewer questions, evidence-backed, scaled by tier.
- **Tier inflation avoidance.** Business owners minimizing intake answers to land a lower tier. Spot-check intake facts against the solution design; make re-tiering on discovery automatic.
- **Orphan acceptances.** Risk acceptances with no expiry or review trigger that outlive the people who signed them. Step 5 requires time-bounding; step 6's reassessment cadence enforces revisits.
- **Onboarding-only program.** Vendors assessed once and never again while their subprocessors, breaches, and scope drift accumulate. Step 6 is the whole point — a vendor program without monitoring is a point-in-time photo album.
- **Fourth-party blindness.** Never asking about subprocessors, then being surprised when the vendor's vendor causes the breach. [NIST SP 800-161 C-SCRM](../context/frameworks/nist-800-161-cscrm.md) is the reference for extending the program past the first tier.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
