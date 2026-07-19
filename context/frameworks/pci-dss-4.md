# PCI DSS v4.x — Payment Card Industry Data Security Standard

## At a glance

| Attribute | Detail |
|---|---|
| Owner | PCI Security Standards Council (PCI SSC), founded by the card brands |
| Current version | v4.0 (March 2022); v4.0.1 (June 2024) — a limited revision correcting/clarifying v4.0, no new requirements |
| Prior version | v3.2.1 retired March 31, 2024 |
| Future-dated requirements | ~50 requirements that were best practice under v4.0 became **mandatory March 31, 2025** |
| Structure | 12 principal requirements grouped under 6 goals; hundreds of sub-requirements |
| Applies to | Any entity that stores, processes, or transmits cardholder data or can impact its security (merchants and service providers) |
| Validation artifacts | ROC (Report on Compliance), SAQ (Self-Assessment Questionnaire), AOC (Attestation of Compliance), ASV scan reports |
| Assessors | QSA (Qualified Security Assessor), ISA (Internal Security Assessor), ASV (Approved Scanning Vendor) |
| Enforcement | Contractual — via card brands and acquiring banks, not statute; fines/fee increases flow through the acquirer |
| New in v4.x | Customized approach, targeted risk analyses, expanded MFA, stronger e-commerce/anti-skimming controls (6.4.3, 11.6.1), authenticated internal scanning |

## Key data definitions

- **Cardholder data (CHD):** primary account number (PAN), plus cardholder name, expiration date, service code when stored with the PAN.
- **Sensitive authentication data (SAD):** full track data, CAV2/CVC2/CVV2/CID, PINs/PIN blocks. Storage after authorization is prohibited even encrypted (limited issuer exceptions).
- **Account data** = CHD + SAD.
- **Cardholder data environment (CDE):** the people, processes, and technologies that store, process, or transmit CHD/SAD, **plus** any system components on the same network segment or that can connect to/impact the CDE.

## Scoping and segmentation

Scope determines cost and effort more than any other decision. Principles:

1. Everything is in scope until verified otherwise; the entity must confirm scope **at least annually** (service providers: every six months under v4.x, per requirement 12.5.2.1).
2. In-scope categories: CDE systems; systems that connect to or can impact the CDE (jump hosts, AD/identity, monitoring, patch servers, backup); systems providing security services to the CDE.
3. **Segmentation** (network or logical isolation) removes systems from scope only if it is verified effective — segmentation penetration testing is required at least annually (every six months for service providers, per 11.4.5/11.4.6 context).
4. Scope-reduction levers, in rough order of impact: outsource card handling entirely (redirect/iframe to a compliant PSP), P2PE-validated terminals, tokenization, network segmentation, eliminating PAN storage.
5. Third parties that handle card data on your behalf are part of your compliance story: track their AOCs and responsibility matrices — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

## The 12 requirements by goal

**Build and Maintain a Secure Network and Systems**
1. Install and Maintain Network Security Controls
2. Apply Secure Configurations to All System Components

**Protect Account Data**
3. Protect Stored Account Data
4. Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks

**Maintain a Vulnerability Management Program**
5. Protect All Systems and Networks from Malicious Software
6. Develop and Maintain Secure Systems and Software

**Implement Strong Access Control Measures**
7. Restrict Access to System Components and Cardholder Data by Business Need to Know
8. Identify Users and Authenticate Access to System Components
9. Restrict Physical Access to Cardholder Data

**Regularly Monitor and Test Networks**
10. Log and Monitor All Access to System Components and Cardholder Data
11. Test Security of Systems and Networks Regularly

**Maintain an Information Security Policy**
12. Support Information Security with Organizational Policies and Programs

High-friction v4.x items practitioners should flag early (all mandatory since March 31, 2025):

- **3.5.1.x** — disk/partition-level encryption alone no longer suffices for PAN on non-removable media; keyed cryptographic hashes required where hashing is used (3.5.1.1).
- **6.4.3 / 11.6.1** — inventory, authorization, and integrity/change detection for payment-page scripts and HTTP headers (anti-Magecart). Affects even many SAQ A merchants.
- **8.3.6** — passwords minimum 12 characters (where passwords are used).
- **8.4.2** — MFA for **all** access into the CDE, not just remote and admin access.
- **10.7.x** — detection and prompt response to failures of critical security control systems.
- **11.3.1.2** — authenticated internal vulnerability scanning.
- **12.3.1** — targeted risk analyses for every requirement that allows frequency/scope flexibility.

## Defined approach vs customized approach

| | Defined approach | Customized approach |
|---|---|---|
| What it is | Implement the requirement as literally written; test against the standard's testing procedures | Meet the requirement's stated **Customized Approach Objective** by different means |
| Evidence | Standard testing procedures | Controls matrix + **targeted risk analysis per 12.3.2** + assessor-designed testing procedures |
| Who can use it | Anyone | Entities assessed by a QSA/ISA producing a **ROC only — not available for SAQ** validation |
| Compensating controls | Still exist in v4.x for constraint-driven shortfalls (Appendix B), requiring a documented business/technical constraint | Not a "compensating control" — it is a first-class alternative for mature entities, no constraint needed |

Practitioner guidance: the customized approach is expensive to document and defend; use it selectively for individual requirements where the defined approach genuinely conflicts with the architecture, not as a general posture.

## Targeted risk analysis (TRA)

v4.x embeds risk analysis in two places:

- **12.3.1** — a documented TRA for each requirement that lets the entity choose a frequency or scope (e.g., how often to review certain logs, POI device inspections, non-CDE malware scans). Must identify assets, threats, factors, and justify the chosen frequency; reviewed at least annually.
- **12.3.2** — a TRA supporting **each** customized-approach control.

These are requirement-scoped analyses, not a substitute for the enterprise risk assessment — see [../risk-scoring.md](../risk-scoring.md) and [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).

## Merchant levels and validation

Merchant levels are defined **by each card brand and enforced by the acquirer** — always confirm with the acquirer. Typical (Visa-style) tiers:

| Level | Typical threshold (annual transactions) | Typical validation |
|---|---|---|
| 1 | Over 6 million (any channel), or brand-designated (e.g., post-breach) | Annual QSA/ISA assessment → ROC + AOC; quarterly ASV scans |
| 2 | 1–6 million | Annual SAQ (some brands require ISA/QSA involvement) + quarterly ASV scans |
| 3 | 20,000–1 million e-commerce | Annual SAQ + quarterly ASV scans |
| 4 | All others | Annual SAQ + quarterly ASV scans (acquirer discretion) |

Service providers have their own two-level scheme (Level 1 typically >300,000 transactions → annual ROC; listed on brand registries).

## SAQ types (practitioner level)

| SAQ | Who it fits | Size/burden |
|---|---|---|
| A | Card-not-present merchants fully outsourcing card handling to PCI-compliant third parties (e.g., hosted payment page/redirect or compliant iframe); no electronic storage/processing/transmission of account data on merchant systems | Smallest, but v4.x added e-commerce script/page controls affecting eligibility and content |
| A-EP | E-commerce merchants whose website doesn't receive account data but **affects the security of the payment transaction** (e.g., merchant site serves the page or JavaScript that frames/redirects payment) | Much larger than A — close to full standard for the web estate |
| B | Merchants with imprint machines or standalone dial-out terminals; no electronic account data storage | Small |
| B-IP | Standalone PTS-approved terminals over IP; no electronic storage | Moderate |
| C | Merchants with payment application systems connected to the internet; no electronic storage | Moderate–large |
| C-VT | Merchants keying transactions one at a time into a third party's virtual terminal on an isolated workstation; no electronic storage | Small–moderate |
| P2PE | Merchants using a PCI-listed P2PE solution; no electronic storage | Small |
| D (Merchant) | Everyone who fits no other SAQ — including anyone storing account data electronically | Full standard |
| D (Service Provider) | Service providers eligible to self-assess | Full standard + service-provider-only requirements |

Misclassification is the most common self-assessment failure — eligibility criteria are printed at the front of each SAQ; verify every criterion, and confirm the acquirer accepts the chosen SAQ.

## Artifacts: ROC vs SAQ vs AOC

- **ROC** — full assessor-written report of an on-site QSA/ISA assessment against all applicable requirements. Confidential; shared with acquirer/brands.
- **SAQ** — self-assessment questionnaire, brand-published per eligibility profile above.
- **AOC** — the signed attestation summarizing the ROC or SAQ result. This is the document exchanged in vendor due diligence: check assessment date, assessed entity legal name, covered services/locations, SAQ type or ROC, and whether any requirements were "not in place" or validated via customized approach. An AOC without a matching service scope is weak evidence.
- **ASV scans** — quarterly external vulnerability scans by an Approved Scanning Vendor with passing results (11.3.2).

## Using this in assessments

- **Start with scope, not requirements.** Produce a data-flow diagram and system inventory of everywhere account data is stored/processed/transmitted, then argue systems *out* of scope with evidence. Requirements 12.5.1/12.5.2 make this documentation mandatory anyway.
- **Gap assessments:** run against v4.0.1 including all formerly future-dated requirements (mandatory since March 31, 2025). Structure per [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
- **Mapping:** PCI DSS is prescriptive and control-dense; it maps down from ISO 27001/NIST comfortably but not up — a PCI-compliant CDE says little about the rest of the enterprise. See [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Breach context:** a card-data breach triggers card-brand/acquirer obligations (PFI forensic investigation, potential re-validation as Level 1) *in addition to* statutory breach notification — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
- **Common pitfalls:** assuming an iframe integration guarantees SAQ A eligibility without checking 6.4.3/11.6.1 applicability; treating "quarterly" as calendar-quarter-optional (scans must be passing every ~3 months with no gaps); scoping out the virtualization/identity layer that administers CDE systems; accepting a vendor's AOC that doesn't cover the service actually consumed; leaving 12.3.1 TRAs unwritten while relying on "periodic" frequencies.

## References

- Related frameworks: [iso-27001-2022.md](iso-27001-2022.md), [cis-controls-v8.md](cis-controls-v8.md), [nist-800-53.md](nist-800-53.md)
- Crosswalks: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md), [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md), [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
