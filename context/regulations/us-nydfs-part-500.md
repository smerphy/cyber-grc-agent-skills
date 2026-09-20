# NYDFS Cybersecurity Regulation (23 NYCRR Part 500, as amended)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | 23 NYCRR Part 500, "Cybersecurity Requirements for Financial Services Companies" — a New York State regulation promulgated under the Financial Services Law, Banking Law and Insurance Law |
| Regulator | New York State Department of Financial Services (DFS / NYDFS), headed since 2026 by Acting Superintendent Kaitlin Asrow; the Superintendent enforces via examination, investigation and consent orders |
| Key dates | Original Part effective 1 March 2017; Second Amendment effective 1 November 2023 with phased compliance through 1 November 2025 (all phases now in force) |
| Who is covered | Any person operating under (or required to operate under) a DFS license, registration, charter, certificate, permit or similar authorization under the Banking, Insurance or Financial Services Law — banks, insurers, producers/agents, money transmitters, virtual-currency licensees, mortgage lenders, etc. (§500.1(e)) |
| Tiering | Three tiers: **Class A companies** (largest, extra controls), standard covered entities, and **limited-exemption** entities under §500.19(a) (small entities relieved of some sections) |
| Structure | §§500.0–500.24: program, policy, governance, vulnerability management, audit trail, access, appsec, risk assessment, personnel, third parties, MFA, asset/data management, monitoring/training, encryption, IR/BCDR, notices, exemptions, enforcement |
| Incident clocks | 72 hours to notify DFS of a cybersecurity incident; 24 hours to notify an extortion payment, plus a written explanation within 30 days (§500.17) |
| Annual filing | By **15 April** each year: certification of material compliance *or* acknowledgment of non-compliance, signed by the highest-ranking executive and the CISO (§500.17(b)) |
| Penalties | No fixed ceiling in Part 500; civil penalties assessed under the Banking, Insurance and Financial Services Laws using the §500.20(c) factors. DFS reported consent orders with 27 entities and over $144 million in cybersecurity fines as of October 2025; individual settlements have run from $250,000 to $30 million (the largest bundled with anti-money-laundering and other violations) |
| Certifiable? | No third-party certification. Self-certification to DFS plus DFS examinations; Class A companies must run independent audits (§500.2(c)) |

## What it is

Part 500 is New York's prescriptive cybersecurity regulation for DFS-licensed financial services companies. It requires every DFS-licensed entity to run a risk-based cybersecurity program with named minimum controls, a designated CISO, board-level oversight, regulator notification of incidents, and an annual executive-signed compliance filing. The original rule took effect on 1 March 2017, with the first annual certification due 15 February 2018 (§500.21(a)); a First Amendment later moved the annual filing date to 15 April — the Second Amendment redline shows the pre-2023 text of §500.17(b) already reading “April 15th”, but DFS no longer posts that adoption, so its date is not restated here (verify).

The **Second Amendment**, signed 16 October 2023 and effective 1 November 2023, is the substantive re-write practitioners must work from. It created the Class A tier, made MFA near-universal, turned "penetration testing and vulnerability assessments" into a full vulnerability-management duty, added asset inventory, IR/BCDR and backup-testing requirements, sharpened board oversight, added extortion-payment reporting, replaced the flat certification with a certification-or-acknowledgment choice, and codified enforcement factors. DFS states its factors include whether policies are "consistent with nationally recognized cybersecurity frameworks, such as NIST" (§500.20(c)(15)), so mapping to NIST CSF or ISO 27001 is both a control strategy and a mitigation strategy.

## Who it covers / Scope

| Test | Detail (section) |
|---|---|
| Covered entity | Any person licensed, registered, chartered, certified, permitted or accredited (or required to be) under the Banking Law, Insurance Law or Financial Services Law, "regardless of whether the covered entity is also regulated by other government agencies" (§500.1(e)). Individuals (e.g., insurance producers) are covered entities in their own right |
| Class A company | ≥ $20m gross annual revenue in each of the last two fiscal years (entity worldwide plus affiliates' NY operations) **and** either > 2,000 employees averaged over two years (entity plus all affiliates, wherever located) **or** > $1bn gross annual revenue in each of the last two years (entity plus all affiliates). Only affiliates that share information systems, cybersecurity resources or any part of the cybersecurity program are counted (§500.1(d)) |
| Limited exemption §500.19(a) | Any one of: fewer than 20 employees and independent contractors (entity plus affiliates); < $7.5m gross annual revenue in each of the last three fiscal years (entity worldwide plus affiliates' NY operations); < $15m year-end total assets under GAAP including all affiliates. Exempt from §§500.4, 500.5, 500.6, 500.8, 500.10, 500.14(a)(1)–(2) and (b), 500.15, 500.16 — but **not** from risk assessment (§500.9), access privileges (§500.7), third-party policy (§500.11), reduced-scope MFA (§500.12(a)), asset inventory/data disposal (§500.13), training (§500.14(a)(3)), or notices (§500.17) |
| Other exemptions | §500.19(b): employee/agent/wholly owned subsidiary covered by another covered entity's program (full); (c): entity with no information systems and no NPI (limited); (d): captive insurers holding only parent/affiliate NPI (limited); (e): inactive individual brokers meeting (c) (full); (g): listed persons such as accredited/certified reinsurers and inactive agents (full) |
| Exemption mechanics | File a Notice of Exemption on the DFS portal within 30 days of determining eligibility (§500.19(f)); it remains valid while the entity qualifies. Once an entity ceases to qualify it has 180 days to comply fully (§500.19(h)). Fully exempt entities under (b), (e) or (g) need not file the annual notification; limited-exemption entities under (a), (c) or (d) must (DFS FAQ) |
| Affiliate programs | A covered entity may satisfy Part 500 by adopting the applicable provisions of an affiliate's program, and the affiliate's board may act as the senior governing body (§§500.2(d), 500.1(q)); all program documentation must be produced to DFS on request (§500.2(e)) |
| Territorial reach | Attaches to the DFS authorization, not to New York data or New York residents: an entity licensed by DFS is in scope wherever it is headquartered, and the revenue/employee tests count the entity's worldwide operations |

## Core obligations

### Program, policy and governance

| Section | Requirement |
|---|---|
| §500.2 | Risk-assessment-based program covering six core functions: identify/assess risk, protect, detect, respond, recover, and fulfil regulatory reporting obligations. Class A companies must design and conduct **independent audits** of the program based on the risk assessment |
| §500.3 | Written cybersecurity policy approved at least annually by a senior officer or the senior governing body, covering 15 named areas (information security; data governance, classification and retention; asset inventory, device and end-of-life management; access controls incl. remote access and identity; BCDR; systems operations; network security and monitoring; awareness and training; application security and SDLC; physical security; customer data privacy; vendor/third-party management; risk assessment; incident response and notification; vulnerability management) |
| §500.4 | Designate a **CISO** (may sit at an affiliate or third-party provider — the entity retains responsibility and must designate a senior internal overseer). CISO reports in writing at least annually to the senior governing body on the program, policies, material risks, effectiveness, material events and remediation plans, and reports material issues "timely". The **senior governing body** must have sufficient cyber understanding (advisors permitted), require management to run the program, regularly review management reports, and confirm sufficient resources |
| §500.9 | Periodic **risk assessment** "sufficient to inform the design of the cybersecurity program", reviewed and updated at least annually and whenever business or technology change materially alters cyber risk; must consider NPI held, systems used and control effectiveness. DFS's 10 September 2026 guidance sets expectations for scope (all assets, NPI locations, third parties, cloud), methodology (inherent vs residual risk), evolving/interconnected risks, governance and risk treatment, and demonstrating how the assessment drove controls and risk-acceptance decisions |
| §500.10 | Qualified cybersecurity personnel (in-house, affiliate or provider) with current training and threat knowledge |
| §500.17(b) | Annual notice by 15 April: either a **certification of material compliance** for the prior calendar year, based on sufficient supporting data, or a **written acknowledgment of non-compliance** identifying each section not materially complied with, the nature and extent, and a remediation timeline. Signed by the highest-ranking executive and the CISO (or senior cyber officer if no CISO); individual licensees sign alone. Supporting records retained **5 years** for DFS inspection |

### Technical and operational controls

| Section | Requirement | Class A add-on |
|---|---|---|
| §500.5 Vulnerability management | Written policies/procedures; **penetration testing** from inside and outside the boundary by a qualified internal or external party at least **annually**; automated scans plus manual review of uncovered systems at a risk-assessment-set frequency and after material changes; a process to be promptly informed of new vulnerabilities; risk-prioritized timely remediation | — |
| §500.6 Audit trail | Systems able to reconstruct material financial transactions (records kept ≥ 5 years) and audit trails to detect and respond to materially harmful events (≥ 3 years) | — |
| §500.7 Access privileges | Least privilege for NPI access; limit number, functions and use of privileged accounts; annual review and removal of unneeded access; disable or securely configure remote-control protocols; prompt termination on departure; industry-standard password policy | Monitor privileged access; deploy a **privileged access management** solution; automated blocking of commonly used passwords (CISO may approve compensating controls annually if infeasible) |
| §500.8 Application security | Secure development practices for in-house apps and testing procedures for externally developed apps; CISO (or designee) reviews at least annually | — |
| §500.11 Third-party service providers | Written policies covering provider identification and risk assessment, minimum cybersecurity practices, due diligence, and periodic reassessment; guidelines/contract terms on provider MFA, encryption, notice of cybersecurity events affecting the entity's systems or NPI, and representations and warranties | — |
| §500.12 MFA | **MFA for any individual accessing any information system** of the covered entity. Limited-exemption entities need MFA only for remote access, remote access to third-party (incl. cloud) apps holding NPI, and all privileged accounts other than non-interactive service accounts. A CISO may approve in writing reasonably equivalent or more secure compensating controls, reviewed at least annually | — |
| §500.13 Asset management and data retention | Written policies producing a complete, accurate, documented **asset inventory** tracking owner, location, classification/sensitivity, support expiration date and RTO, with a defined update/validation frequency; periodic secure disposal of NPI no longer needed | — |
| §500.14 Monitoring and training | Risk-based monitoring of authorized-user activity; controls against malicious code incl. web and email filtering; at least annual awareness training covering social engineering, updated to the risk assessment | **EDR** to monitor anomalous activity incl. lateral movement, and centralized logging and security-event alerting (CISO-approved compensating controls permitted) |
| §500.15 Encryption | Written policy requiring industry-standard encryption of NPI in transit over external networks and at rest; at-rest infeasibility only with CISO-approved written compensating controls reviewed annually | — |
| §500.16 IR and BCDR | Written incident response plans (goals, processes, roles and decision authority, communications, remediation, documentation, backup recovery, **root-cause analysis**, plan updates) covering event types incl. ransomware; BCDR plans identifying essential assets/people/third parties, responsible personnel, communications and recovery procedures, offsite backups. Distribute plans, train responders, **test IR and BCDR plans and backup restoration at least annually**; keep backups protected from alteration or destruction | — |

### Notices to the Superintendent (§500.17)

| Trigger | Clock | Content / notes |
|---|---|---|
| **Cybersecurity incident** — a cybersecurity event at the entity, an affiliate or a third-party service provider that (1) requires notice to any government, self-regulatory or supervisory body, (2) has a reasonable likelihood of materially harming a material part of normal operations, or (3) deploys ransomware in a material part of the entity's systems (§500.1(g)) | "As promptly as possible but in no event later than **72 hours** after determining" the incident occurred | Electronic filing on the DFS portal; continuing duty to supply requested information and update DFS with material changes or newly available information |
| **Extortion payment** in connection with a cybersecurity event | Notice within **24 hours** of payment; written explanation within **30 days** | Explanation must cover why payment was necessary, alternatives considered, diligence on alternatives, and diligence on sanctions compliance including OFAC |
| Annual compliance notice | **15 April** for the prior calendar year | Certification or acknowledgment (see above) |
| Notice of exemption | Within 30 days of determining eligibility | Amend or terminate on the portal when circumstances change |

Note that limb (1) of the incident definition makes any other regulator's breach threshold (e.g., New York's SHIELD Act, HIPAA, SEC Form 8-K) a DFS trigger too. Enforcement actions repeatedly cite late notice: Healthplex (notice more than four months after a late-2021 phishing compromise) and Delta Dental (2023 MOVEit exploitation; DFS cited failure to report timely). See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

### DFS guidance layer (no new legal obligations, but examination expectations)

| Date | Guidance | Substance |
|---|---|---|
| 16 Oct 2024 | Industry letter: Cybersecurity Risks Arising from Artificial Intelligence | Names four AI risks (AI-enabled social engineering, AI-enhanced attacks, exposure/theft of large NPI stores, supply-chain/vendor AI) and maps mitigations to §§500.9, 500.11, 500.7/500.12 (MFA that avoids SMS/voice; digital certificates or liveness checks), 500.14 (deepfake-aware training, monitoring), 500.13 (data minimization, AI assets in the inventory). States it "does not impose any new requirements" |
| 21 Oct 2025 | Guidance on Managing Risks Related to Third-Party Service Providers | Examination-driven expectations under §500.11: risk-tiered classification of providers by access, data sensitivity, location and criticality; due-diligence factors including the provider's own Part 500-equivalent controls, unique traceable accounts and §500.6 audit trails, and geopolitical/jurisdictional risk; contractual protections, ongoing monitoring and termination planning. States it “does not impose new requirements” |
| 21 May 2026 | Advisory to CISOs: Heightened Cybersecurity Risks Associated with Frontier AI Models; companion letter on measures for a heightened cybersecurity threat environment | Frontier models amplify "the potency, scale, and speed of identifying vulnerabilities and exploits"; expects expedited vulnerability remediation, dependency mapping with critical third parties, human oversight of AI-generated code, stronger monitoring/logging/alerting, and resilience testing. No new requirements |
| 11 Aug 2026 | Cyber threat alert: N-central vulnerability affecting some managed service providers | Example of DFS's regular product-specific vulnerability alerts; §500.5(b)–(c) require entities to be promptly informed of new vulnerabilities and to remediate them on a risk-prioritized basis, and DFS has cited failure to act on an earlier alert (MOVEit, June 2023) in enforcement |
| 10 Sep 2026 | Guidance on How to Conduct and Use Risk Assessments | Five deficiency categories seen in examinations (asset scope, methodology, evolving/interconnected risk, governance/risk treatment, failure to inform the program); expects entities to demonstrate how the assessment drove control selection, compensating controls and risk acceptance |

## Enforcement and penalties

- **Violation definition (§500.20(b)):** a single prohibited act or failure to act is a violation, including failure to prevent unauthorized access to NPI due to non-compliance, or "the material failure to comply for any 24-hour period with any section" — i.e., each day of non-compliance can count separately.
- **Penalty factors (§500.20(c)):** cooperation, good faith, intent/recklessness, failure to remedy prior examination findings, history and pattern of violations, false or misleading information, consumer harm, timeliness of consumer disclosures, gravity, number and duration, senior governing body participation, other regulators' sanctions, financial resources, consistency with NIST-type frameworks, and the public interest. Part 500 sets no penalty ceiling; the Superintendent draws on the underlying Banking, Insurance and Financial Services Law powers.
- **Personal accountability:** the annual certification is signed by the highest-ranking executive and CISO on the basis of "data and documentation sufficient to accurately determine and demonstrate" material compliance; false certifications have featured in enforcement (Robinhood Crypto).
- **Scale:** DFS stated in October 2025 that it had entered consent orders with 27 entities for cybersecurity-regulation violations, yielding over $144 million in fines.
- **Representative consent orders (DFS press releases):**

| Date | Entity | Penalty | Findings cited by DFS |
|---|---|---|---|
| 2 Aug 2022 | Robinhood Crypto | $30m (combined AML, transaction monitoring, virtual-currency and Part 500 violations; examination-driven) | Inadequate cybersecurity program, false compliance certifications; independent consultant required |
| 25 May 2023 | OneMain Financial Group | $4.25m | Third-party risk and vendor due diligence, shared admin accounts and default passwords, no formal secure-SDLC methodology |
| 23 Jan 2025 | PayPal | $2m | Unqualified personnel for key cybersecurity functions (§500.10) and inadequate training (§500.14(a)(3)); missing access-control/identity/customer-data policies; no customer MFA, CAPTCHA or rate limiting — exposed Form 1099-K data including SSNs |
| 14 Aug 2025 | Healthplex | $2m | No MFA on cloud email, no email retention limits, notice to DFS more than four months after discovery; independent MFA audit required |
| 14 Oct 2025 | Eight auto insurers (Farmers, Hagerty, Hartford Fire, Infinity, Liberty Mutual, Metromile, Midvale, State Auto) | > $19m aggregate ($1.85m–$3m each) | Exposure of driver's license numbers and dates of birth via public-facing quoting applications and agent portals; two firms also failed to report timely |
| 30 Apr 2026 | Delta Dental Insurance Co. / Delta Dental of New York | $2.25m | MOVEit exploitation; inadequate IR policies and procedures, missing retention settings and controls, failure to report timely |
| 5 Aug 2026 | Order Express (money transmitter, limited-exemption entity) | $250,000 | Inadequate patching/system-update policies and risk assessments — shows small exempt entities are examined against the sections that still apply to them |

## Timeline and status

| Date | Event |
|---|---|
| 1 Mar 2017 | Part 500 effective (§500.21(a)); first annual certifications due 15 February 2018 |
| Before 2023 | First Amendment — annual filing date moved from 15 February to 15 April; date of adoption not evidenced in current DFS postings (verify) |
| 9 Nov 2022 / 28 Jun 2023 | Proposed Second Amendment published in the State Register (comments to 9 Jan 2023); revised proposal published (comments to 14 Aug 2023) |
| 16 Oct 2023 / 1 Nov 2023 | Second Amendment signed / effective; §§500.19(e)–(h), 500.20, 500.21, 500.22, 500.24 effective immediately (§500.22(e)) |
| 1 Dec 2023 | 30-day phase: amended §500.17 notices (72-hour incident notice under the new definition; 24-hour/30-day extortion reporting) |
| 29 Apr 2024 | 180-day default phase: everything not listed elsewhere — e.g., §500.2(c) Class A independent audits, §500.3 policy areas, §500.9 annual risk-assessment cadence, §500.10, §500.11, §500.13(b) disposal, §500.14(a)(1) user monitoring and (a)(3) training |
| 1 Nov 2024 | One-year phase: §500.4 governance (CISO reporting content, senior governing body duties), §500.15 encryption, §500.16 IR/BCDR and annual testing, §500.19(a) new exemption thresholds |
| 1 May 2025 | 18-month phase: §500.5(a)(2) scanning, §500.7 access-privilege management incl. §500.7(c) Class A PAM and password blocking, §500.14(a)(2) malicious-code controls and §500.14(b) Class A EDR/centralized logging |
| 1 Nov 2025 | Two-year phase: §500.12 universal MFA and §500.13(a) asset inventory — last transitional period expired |
| 15 Apr 2026 | Annual notice covering calendar year 2025 — the first to span the expiry of the last transitional periods (§§500.12, 500.13(a)). Calendar year 2026, certified by 15 April 2027, is the first full year with every amended requirement in force throughout |
| Status, Sep 2026 | No Third Amendment proposed, pre-proposed or adopted: as of September 2026 the DFS financial services regulatory-activity page lists no Part 500 item under pre-proposed or proposed rulemaking, and the last Part 500 final adoption remains the Second Amendment. DFS activity in 2025–26 has been guidance (Oct 2025, May 2026, Sep 2026), threat alerts and enforcement. Watch the DFS Cybersecurity Resource Center and the State Register |

## Key obligations for security/GRC teams

1. **Classify the entity and every affiliate**: covered entity → Class A / standard / limited-exemption, counting affiliates exactly as §500.1(d) and §500.19(a) prescribe (worldwide revenue for the entity, NY-only revenue for affiliates, shared-infrastructure affiliates only for Class A). Re-test annually before the 15 April filing. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Run the §500.9 risk assessment as the documented root of every control decision** and keep an audit trail showing how it drove control selection, compensating controls and risk acceptance — the September 2026 guidance makes this an examination question. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
3. **Wire the §500.1(g) incident definition into severity triage** with a pre-approved 72-hour DFS filing, a 24-hour extortion-payment notice and the 30-day OFAC-diligence memo, plus provider-incident intake under §500.11(b)(3). See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
4. **Treat the annual notice as an attestation exercise**: build a section-by-section evidence file supporting material compliance (or an honest acknowledgment with remediation timelines), retain it five years, and get the CEO and CISO signatures on evidence, not assurances. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
5. **Close the universal MFA and asset-inventory gaps** (in force since 1 November 2025) and track any CISO-approved compensating controls as formal, annually reviewed exceptions. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
6. **Evidence the annual cycle**: penetration test (internal and external, qualified tester), IR/BCDR tabletop with critical staff, backup restoration test, access review, policy approval, training, CISO report to the board. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
7. **Board readiness**: the senior governing body must demonstrate cyber understanding and resource oversight — minute the CISO's written report and the board's challenge. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
8. **Third-party program** aligned to §500.11 and the October 2025 DFS guidance: provider inventory and risk tiering by access/sensitivity/criticality, minimum practices, MFA/encryption/notice contract clauses, periodic reassessment and termination planning; extend to AI vendors per the October 2024 letter. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
9. **Policy set** covering all 15 §500.3 areas, approved annually. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
10. **AI governance hook**: fold AI-enabled social engineering, AI data-exposure and frontier-model exploit acceleration into the risk assessment and training. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).

## Interplay

- **GLBA / FTC Safeguards Rule and federal banking regulators:** Part 500 applies "regardless of whether the covered entity is also regulated by other government agencies"; state-licensed lenders and insurers face both. Part 500's named controls (MFA, encryption, pen test, asset inventory, CISO, board reporting) are more prescriptive than the Safeguards Rule's; a Part 500 program generally satisfies the Safeguards Rule element list but not vice versa. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- **NAIC Insurance Data Security Model Law:** DFS states in its enforcement releases that Part 500 has served as a model for the FTC, multiple states, the NAIC and the CSBS Nonbank Model Data Security Law. Insurers licensed in multiple states should treat Part 500 as the superset and map state variants (notice clocks, exemption thresholds) against it. See [us-naic-insurance-data-security.md](us-naic-insurance-data-security.md).
- **SEC cybersecurity disclosure:** a DFS "cybersecurity incident" and an SEC "material cybersecurity incident" are different tests with different clocks (72 hours after determination vs four business days after materiality determination); an 8-K filing is itself a limb-(1) DFS trigger. See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **HIPAA:** health insurers and dental/health plan administrators licensed by DFS (Healthplex, Delta Dental) face parallel OCR breach rules; several recent DFS actions have involved health-sector licensees. See [hipaa.md](hipaa.md).
- **State breach laws / New York SHIELD Act:** consumer-notice statutes drive limb (1) of the DFS incident definition and the §500.20(c)(9) penalty factor on timely consumer disclosure. See [us-state-breach-notification-laws.md](us-state-breach-notification-laws.md) and [us-state-privacy.md](us-state-privacy.md).
- **DORA / EU and UK operational resilience:** Part 500's IR/BCDR, backup-testing and third-party provisions overlap with DORA pillars 1, 2 and 4 for groups with EU financial entities; DFS's 24-hour extortion-payment notice is a distinct clock to add to any shared incident playbook. See [dora.md](dora.md) and [uk-financial-operational-resilience.md](uk-financial-operational-resilience.md).
- **Frameworks:** §500.20(c)(15) rewards alignment with "nationally recognized cybersecurity frameworks, such as NIST"; §500.2(b)'s six functions map directly to NIST CSF 2.0 Identify/Protect/Detect/Respond/Recover, and the control set maps cleanly to ISO 27001:2022 Annex A and CIS Controls v8. See [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- https://www.dfs.ny.gov/industry_guidance/regulations/final_adoptions_fs/rf_fs_2amend23nycrr500_text_20231101 — adopted Second Amendment text (legal text, bracketed/underscored, signed 16 October 2023)
- https://www.dfs.ny.gov/system/files/documents/2023/12/rf23_nycrr_part_500_amend02_20231101.pdf — DFS consolidated Part 500 text as amended (legal text; DFS labels it an unofficial consolidation)
- https://www.dfs.ny.gov/system/files/documents/2026/07/NYCRR-part-500-Cybersecurity-Regulation.pdf — same consolidated amended text, July 2026 posting (legal text)
- https://www.dfs.ny.gov/industry_guidance/cybersecurity — DFS Cybersecurity Resource Center (regulator guidance; index of letters, FAQs, portal)
- https://www.dfs.ny.gov/cybersecurity/faqs — DFS FAQs (regulator guidance)
- https://www.dfs.ny.gov/cybersecurity/exemptions and https://www.dfs.ny.gov/cybersecurity/submissions — exemption and filing guidance (regulator guidance)
- https://www.dfs.ny.gov/industry_guidance/regulatory_activity/financial_services — DFS financial services regulatory activity (pre-proposed, proposed and final adoptions; evidences that the Second Amendment remains the latest Part 500 adoption)
- https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks — AI cybersecurity risk letter, 16 October 2024
- https://www.dfs.ny.gov/industry-guidance/industry-letters/il20251021-guidance-managing-risks-third-party — third-party service provider risk guidance, 21 October 2025
- https://www.dfs.ny.gov/industry-guidance/industry-letters/20260521-heightened-cybersecurity-risks-assoc-with-frontier-ai-models — Frontier AI advisory, 21 May 2026
- https://www.dfs.ny.gov/industry_guidance/industry_letters/il20260910-cyber-risk-assessment — risk assessment guidance, 10 September 2026
- DFS press releases: pr202208021 (Robinhood Crypto), pr202305251 (OneMain), pr20250123 (PayPal), pr20250814 (Healthplex), pr20251014 (auto insurers), pr20260430 (Delta Dental), pr20260805 (Order Express) under https://www.dfs.ny.gov/reports_and_publications/press_releases/
- Not fetched: the official NYCRR compilation at govt.westlaw.com/nycrr (JS-gated), and any DFS posting of the First Amendment, which is no longer listed on the final-adoptions page — hence the hedged treatment of its date above.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
