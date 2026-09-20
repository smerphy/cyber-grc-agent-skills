# Zero Trust Architecture — NIST SP 800-207, SP 800-207A, SP 1800-35 and CISA ZTMM 2.0

## At a glance

| Attribute | Detail |
|---|---|
| Core document | NIST SP 800-207, *Zero Trust Architecture* — published **August 2020**, 59 pages, DOI 10.6028/NIST.SP.800-207. Authored by NIST's Advanced Network Technologies Division with a CISA co-author |
| Publisher / status | NIST (Information Technology Laboratory). The CSRC document history carries a single entry — final, 11 August 2020. No revision and no draft revision existed as of September 2026 |
| Companions | SP 800-207A (September 2023) — ZTA access control for cloud-native apps in multi-location environments; SP 1800-35 (NCCoE practice guide, **final 10 June 2025**) — 19 example implementations built with 24 CRADA collaborators |
| Maturity model | CISA *Zero Trust Maturity Model* **v2.0, April 2023** (TLP:CLEAR) — 5 pillars, 3 cross-cutting capabilities, 4 maturity stages. Still the current version as of September 2026 |
| Federal mandate layer | EO 14028 (signed 12 May 2021, 86 FR 26633) → OMB M-22-09 (26 January 2022, FY2024 objectives) → EO 14144 (signed 16 January 2025, 90 FR 6755), amended by EO 14306 (signed 6 June 2025, 90 FR 24723). M-22-09 has not been rescinded and is still measured in the FY 2026–FY 2027 CIO FISMA metrics |
| Defense variant | DoD Zero Trust Strategy (21 October 2022): 7 pillars, 45 capabilities, "Target Level" no later than **FY2027**, Advanced Level activities through **FY2032** |
| Certifiable? | **No.** SP 800-207 is architectural guidance, not a control catalogue and not an auditable standard. There is no zero-trust certification; assurance comes from maturity assessment plus control-level evidence in CSF/800-53/ISO terms |
| Nature of obligation | Voluntary for private sector; binding-by-policy for US federal civilian agencies (via OMB memoranda) and DoD components |
| UK counterpart | NCSC *Zero trust architecture design principles* — version 1.1, reviewed 16 January 2026; seven numbered principles (the page summary line still says "eight", a legacy of v1.0). The surrounding NCSC collection now also carries Zero Trust Network Access (ZTNA) guidance |

## What it is

Zero trust is a design philosophy, not a product or a control set. SP 800-207 defines it as "a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised." A *zero trust architecture* (ZTA) is the enterprise's plan — component relationships, workflow planning and access policies — that applies those concepts; a *zero trust enterprise* is the resulting infrastructure and operating policy.

The central move is the removal of implicit trust based on network location or asset ownership. Authentication and authorization of both subject and device are discrete functions performed **before** a session to a resource is established, and re-evaluated during it. SP 800-207 is deliberately technology-agnostic and vendor-neutral: it describes logical components and abstract deployment models rather than products, which is exactly why it has become the reference definition that regulators, auditors and vendors all cite.

Two layers sit on top of it in practice. CISA's Zero Trust Maturity Model turns the concepts into an assessable gradient for US federal civilian agencies (and, explicitly, "all organizations" that find it useful). NCCoE's SP 1800-35 turns them into demonstrated builds. GRC teams almost always work with all three: SP 800-207 for definitions and architecture review, ZTMM for maturity scoring and roadmaps, SP 1800-35 for implementation evidence and standards mappings.

## Who it covers / Scope

- **No statutory scope.** SP 800-207 is NIST guidance issued under FISMA authority; it binds no one directly and is explicitly available for voluntary non-governmental use.
- **US federal civilian (FCEB) agencies** are driven by OMB M-22-09, which set a Federal ZTA strategy with objectives due by the end of FY2024 and required agencies to designate a zero-trust implementation lead within 30 days and to submit an FY22–FY24 implementation plan within 60 days. M-22-09 has not been rescinded: the FY 2026 & FY 2027 CIO FISMA Metrics (v1.0, 3 August 2026) still measure agencies against it, and OMB M-26-14 (22 May 2026) ties the new federal logging reference architecture to CISA's Zero Trust Maturity Model.
- **DoD components and, in practice, their Defense Industrial Base partners** work to the separate DoD Zero Trust Strategy and its capability roadmap rather than the CISA model.
- **Private sector** adoption is voluntary but increasingly contractual: cyber-insurance questionnaires, customer security addenda and government supply-chain terms now use SP 800-207 vocabulary (PEP, policy engine, per-session authorization) as shorthand.
- **Boundary caveat:** the tenets apply to work done inside an organization or with partner organizations — SP 800-207 states they are not intended for anonymous public or consumer-facing business processes, since an enterprise cannot impose internal policy on external actors.
- **Explicit ZTMM exclusions:** the maturity model does not cover incident response, logging/monitoring/alerting specifics, forensics, risk acceptance or recovery, and does not address operational technology, certain IoT classes, or how to incorporate machine learning and AI capabilities.

## Structure and requirements

### The seven tenets (SP 800-207 §2.1)

| # | Tenet | Practical test |
|---|---|---|
| 1 | All data sources and computing services are considered resources | Is there a resource inventory that includes SaaS, small-footprint devices and (where allowed) personally owned devices? |
| 2 | All communication is secured regardless of network location | Does traffic inside the corporate LAN meet the same authentication/encryption bar as traffic from the internet? |
| 3 | Access to individual enterprise resources is granted on a per-session basis | Does authorization to one resource automatically grant another? It must not. Least privilege per session |
| 4 | Access is determined by dynamic policy — client identity, application/service and requesting-asset state, plus behavioural and environmental attributes | Are policies attribute-based and sensitivity-scaled, or static group membership? |
| 5 | The enterprise monitors and measures the integrity and security posture of all owned and associated assets | Is there a CDM-style system feeding real device posture into access decisions? |
| 6 | All resource authentication and authorization are dynamic and strictly enforced before access is allowed | ICAM plus asset management in place; MFA for some or all resources; continual re-evaluation during the session |
| 7 | The enterprise collects as much information as possible about assets, network infrastructure and communications and uses it to improve posture | Is telemetry actually feeding policy refinement, or just retained? |

### Logical components (SP 800-207 §3)

| Component | Role |
|---|---|
| Policy engine (PE) | Makes and records the grant/deny/revoke decision for a subject–resource pair, using the trust algorithm |
| Policy administrator (PA) | Executes the decision: establishes or tears down the communication path, issues session credentials/tokens; with the PE forms the **policy decision point (PDP)** |
| Policy enforcement point (PEP) | Enables, monitors and terminates the connection. May be split client-side (agent) and resource-side (gateway), or be a single portal. Beyond the PEP lies the implicit trust zone |

Data sources feeding the PE: CDM system; industry compliance system; threat intelligence feeds; network and system activity logs; data access policies; enterprise PKI; ID management system; SIEM.

### Architecture approaches and deployment models

| Axis | Options (SP 800-207 §3.1–§3.2) |
|---|---|
| Approach (main policy driver) | Enhanced identity governance; micro-segmentation; network infrastructure and software-defined perimeters (SDP). A full solution contains elements of all three |
| Deployed variation | Device agent/gateway-based; enclave-based; resource portal-based; device application sandboxing |
| Trust algorithm | Criteria-based vs score-based; singular vs contextual. SP 800-207 states a ZTA trust algorithm should ideally be **contextual** — it detects an attacker operating inside a compromised account's normal role — while warning about usability cost |

SP 800-207 also works through five deployment scenarios (§4: satellite facilities; multi-cloud/cloud-to-cloud; contracted services and non-employee access; cross-enterprise collaboration; public/customer-facing services) and seven ZTA-specific threats (§5: subversion of the decision process; denial of service or network disruption; stolen credentials/insider threat; loss of network visibility; storage of system and network information; reliance on proprietary data formats; use of non-person entities in ZTA administration). Section 7.3 gives a seven-step migration path: identify actors → identify enterprise-owned assets → identify key processes and evaluate their risks → formulate ZTA candidate policies → identify candidate solutions → initial deployment and monitoring → expand the ZTA.

### CISA Zero Trust Maturity Model 2.0

Five pillars — **Identity, Devices, Networks, Applications and Workloads, Data** — each assessed across four stages, with three cross-cutting capabilities (**Visibility and Analytics, Automation and Orchestration, Governance**) evaluated within every pillar.

| Stage | Defining characteristics (ZTMM §5) |
|---|---|
| Traditional | Manual lifecycles and attribute assignment; static policies addressing one pillar at a time; least privilege set only at provisioning; siloed enforcement; manual response; limited log/telemetry correlation |
| Initial | Starting automation of attribute assignment and lifecycle configuration; initial cross-pillar solutions; some responsive change to least privilege after provisioning; aggregated visibility for internal systems |
| Advanced | Automated lifecycle and policy assignment with cross-pillar coordination; centralized visibility and identity control; pre-defined mitigation responses; least privilege changes driven by risk and posture assessment |
| Optimal | Fully automated just-in-time lifecycles; self-reporting assets; dynamic policy from observed triggers; dynamic least-privilege enterprise-wide; cross-pillar interoperability with continuous monitoring |

Pillar functions assessed (ZTMM tables 2–6): Identity — Authentication, Identity Stores, Risk Assessments, Access Management. Devices — Policy Enforcement and Compliance Monitoring, Asset and Supply Chain Risk Management, Resource Access, Device Threat Protection. Networks — Network Segmentation, Network Traffic Management, Traffic Encryption, Network Resilience. Applications and Workloads — Application Access, Application Threat Protections, Accessible Applications, Secure Application Development and Deployment Workflow, Application Security Testing. Data — Data Inventory Management, Data Categorization, Data Availability, Data Access, Data Encryption.

Pillars may progress at different rates, but cross-pillar coordination is what unlocks the Advanced and Optimal stages — a point worth making to leadership when one pillar's tooling budget is proposed in isolation.

### OMB M-22-09 — the concrete federal requirements

| Pillar | Selected required actions |
|---|---|
| Identity | Centralized enterprise identity systems; **phishing-resistant MFA required** for staff, contractors and partners and offered as an option to public users; MFA enforced at the application layer, not the network layer; password policies must **not** require special characters or periodic rotation; at least one device-level signal considered alongside user identity |
| Devices | Reliable asset inventories via CISA's CDM program; EDR meeting CISA technical requirements, widely deployed, with information sharing per M-22-01 |
| Networks | Encrypted DNS wherever technically supported; HTTPS enforced for all web and API traffic with .gov domains preloaded; a ZTA plan describing environmental isolation submitted to OMB |
| Applications and workloads | Dedicated application security testing programs; independent third-party appsec evaluation; a welcoming public vulnerability disclosure programme; make at least one internal FISMA Moderate application fully accessible over the public internet; work toward immutable workloads |
| Data | Joint Federal CDO/CISO effort on data categorization and protection; cloud security services to monitor access to sensitive data; enterprise-wide logging and information sharing |

## Assessment, certification and evidence

- **There is no zero-trust certification and no auditor opinion on "zero trust".** Anyone selling one is selling a proprietary scheme. Assurance is assembled from other frameworks' evidence.
- **The normal assessment artifact is a ZTMM scorecard**: current stage and target stage per pillar per function, with a dated evidence reference for each rating. Rate functions, not pillars — a pillar-level score hides the gap that matters.
- **SP 1800-35 is the evidence bridge.** It documents capabilities and their mappings to NIST CSF 1.1 and 2.0, SP 800-53 Rev. 5, and NIST's critical software security measures, so a ZTA capability claim can be tied back to an auditable control. Its builds were run in three phases — enhanced identity governance (EIG) "crawl", EIG "run", then SDP/microsegmentation/SASE — a useful sequencing precedent for a roadmap.
- **Evidence that actually stands up:** policy-engine decision logs showing per-session authorization and denials; device-posture signals demonstrably consumed in an access decision (screenshot of policy plus a denied-access log line); MFA enrolment coverage by population and authenticator strength; segmentation rule sets with change history; inventory reconciliation showing resource coverage of the PEP estate.
- **Common audit failure:** a "zero trust" claim backed only by an SSO deployment. SSO without device signal, per-session re-evaluation or resource-level PEPs satisfies none of tenets 3, 5 or 6.
- See [control-testing](../../skills/control-testing/SKILL.md) and [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).

## Timeline and status

| Date | Event |
|---|---|
| 11 August 2020 | NIST SP 800-207 published (final) |
| 12 May 2021 | EO 14028 *Improving the Nation's Cybersecurity* signed; published in the Federal Register 17 May 2021 (86 FR 26633); directs federal migration to ZTA |
| August 2021 | CISA ZTMM v1.0 initial release (per the v2.0 revision history) |
| 26 January 2022 | OMB M-22-09 sets the Federal ZTA strategy with objectives due by end of FY2024 |
| 21 October 2022 | DoD Zero Trust Strategy published; 7 pillars, 45 capabilities |
| April 2023 | CISA ZTMM **v2.0** published, aligned to M-22-09 |
| September 2023 | NIST SP 800-207A published — network-tier and identity-tier policies for service-mesh/microservices platforms across multi-cloud |
| 16 January 2025 | EO 14144 signed; published 17 January 2025 (90 FR 6755). Its section 7 directed OMB to revise Circular A-130 within three years to cover migration to zero trust architectures |
| 6 June 2025 | EO 14306 signed (published 11 June 2025, 90 FR 24723), amending EO 14144 and EO 13694. It struck and replaced EO 14144 section 7: the three-year deadline for OMB guidance revising Circular A-130 survives, but the express reference to zero-trust migration, EDR, encryption, segmentation and phishing-resistant MFA was removed. The EO text does not mention zero trust anywhere |
| **10 June 2025** | NIST SP 1800-35 finalized (24 collaborators, 19 example implementations) |
| 16 January 2026 | UK NCSC zero trust design principles reviewed at version 1.1 |
| 22 May 2026 | OMB M-26-14 rescinds M-21-31 and replaces the federal logging maturity model with continuous event monitoring (CEM) and threat-hunting/forensics (THIRF) objectives; CISA's logging reference architecture is to align with the ZTMM |
| 3 August 2026 | FY 2026 & FY 2027 CIO FISMA Metrics v1.0 published; still measure M-22-09 zero-trust requirements, including application-layer MFA and micro-segmentation |
| End of FY2027 | DoD "Target Level" zero trust deadline; Advanced Level activities run through FY2032 |
| As of September 2026 | SP 800-207 remains at its 2020 edition with no announced revision; ZTMM remains at v2.0; M-22-09 remains in force |

## Key obligations for security/GRC teams

1. **Fix the definition before the roadmap.** Adopt SP 800-207's vocabulary (resource, subject, PE/PA/PEP, implicit trust zone) in policy and architecture standards so "zero trust" stops meaning whatever the last vendor said. See [policy-authoring](../../skills/policy-authoring/SKILL.md) and [../glossary.md](../glossary.md).
2. **Baseline with the ZTMM at function level**, recording current and target stage per function per pillar with dated evidence — this is the assessment artifact regulators, boards and acquirers actually accept. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
3. **Build the resource inventory first** (tenet 1 and migration step 2). Every later decision — which PEP, which policy, which segment — depends on knowing the resources and the business processes that touch them.
4. **Make device posture a real input, not a slide.** Tenets 4–6 require asset state to change the access outcome; evidence this with a policy that denies on stale posture and the log to prove it.
5. **Treat phishing-resistant MFA as the identity floor**, and re-check password policy against M-22-09's prohibition on forced rotation and special-character rules — many internal policies still contradict it. See [policy-review](../../skills/policy-review/SKILL.md).
6. **Risk-assess the ZTA itself.** SP 800-207 §5 names seven architecture-specific risks; the PE/PA becomes a single point of both compromise and outage, and non-person entities administering the ZTA are an under-modelled threat. Record these in the register. See [risk-assessment](../../skills/risk-assessment/SKILL.md) and [../risk-scoring.md](../risk-scoring.md).
7. **Avoid proprietary lock-in as a control decision** (§5.6): a ZTA whose policy and telemetry live in one vendor's format is a concentration risk, not just a procurement preference. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
8. **Map ZTA capabilities to the control frameworks you are already audited against** before claiming coverage, using SP 1800-35's CSF/800-53 mappings as the starting point. See [control-mapping](../../skills/control-mapping/SKILL.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
9. **Report maturity movement, not tool counts.** Stage transitions per pillar, MFA coverage by authenticator strength, and share of resources behind a PEP are the metrics that survive board scrutiny. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
10. **Track exceptions explicitly** for legacy systems that cannot support per-session authorization — these are the residual implicit trust zones and belong in the exception register with compensating controls. See [exception-management](../../skills/exception-management/SKILL.md).

## Interplay

- **NIST CSF 2.0:** the natural mapping target is the **PR.AA** category (Identity Management, Authentication, and Access Control, subcategories PR.AA-01 to PR.AA-06), with ID.AM (Asset Management) for resource inventory and DE.CM (Continuous Monitoring) for posture telemetry. CSF gives the outcome language, SP 800-207 the architecture. See [nist-csf-2.md](nist-csf-2.md).
- **NIST SP 800-53 Rev. 5:** the actual control text an assessor tests — AC, IA, SC and SI families. SP 1800-35 publishes the capability-to-800-53r5 mapping. See [nist-800-53.md](nist-800-53.md).
- **ISO/IEC 27001:2022:** no zero-trust clause; Annex A controls on identity, authentication, privileged access, network security and segregation carry the load. A ZTMM score is not ISO evidence and vice versa. See [iso-27001-2022.md](iso-27001-2022.md).
- **CIS Controls v8/v8.1:** the pragmatic implementation layer — Controls 1, 2, 5, 6, 12 and 13 are where zero-trust intent becomes concrete safeguards. See [cis-controls-v8.md](cis-controls-v8.md).
- **PCI DSS v4.x:** network segmentation and scope reduction interact directly with micro-segmentation designs; a ZTA that dissolves flat networks can shrink CDE scope, but segmentation still has to be validated on PCI DSS's own terms. See [pci-dss-4.md](pci-dss-4.md).
- **DORA and NIS2:** neither mandates zero trust, but both demand risk-based access control, segmentation and continuous monitoring that ZTA satisfies well; a ZTMM roadmap is a defensible way to evidence "state of the art" measures. See [dora.md](../regulations/dora.md) and [nis2.md](../regulations/nis2.md).
- **SEC cyber disclosure and HIPAA:** zero-trust maturity is a governance narrative, not a disclosure control or a Security Rule safeguard — do not substitute one for the other. See [sec-cyber-disclosure.md](../regulations/sec-cyber-disclosure.md) and [hipaa.md](../regulations/hipaa.md).
- Related packs exist in this library for federal cyber (FISMA) and for SP 800-171/CMMC; check the frameworks and regulations directories for the current set.

## Primary sources

- NIST SP 800-207, *Zero Trust Architecture* (August 2020) — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf — core guidance (fetched); landing page https://csrc.nist.gov/pubs/sp/800/207/final (fetched)
- NIST SP 800-207A, *A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Location Environments* (September 2023) — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf (fetched)
- NIST SP 1800-35, *Implementing a Zero Trust Architecture* (final 10 June 2025) — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-35.pdf and https://csrc.nist.gov/pubs/sp/1800/35/final (both fetched)
- CISA, *Zero Trust Maturity Model* version 2.0 (April 2023) — https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf (document text obtained; the CISA web server blocks scripted downloads) and https://www.cisa.gov/zero-trust-maturity-model (page read; confirms v2.0 is the current release)
- OMB Memorandum M-22-09, *Moving the U.S. Government Toward Zero Trust Cybersecurity Principles* (26 January 2022) — https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf (fetched)
- NIST Cybersecurity Framework 2.0 (NIST CSWP 29) — https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (fetched, for the PR.AA category text)
- EO 14028, *Improving the Nation's Cybersecurity* (86 FR 26633) — https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity (fetched via the Federal Register API)
- EO 14144, *Strengthening and Promoting Innovation in the Nation's Cybersecurity* (90 FR 6755) — https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01470.htm (full text fetched)
- EO 14306, *Sustaining Select Efforts to Strengthen the Nation's Cybersecurity and Amending Executive Order 13694 and Executive Order 14144* (90 FR 24723) — https://www.govinfo.gov/content/pkg/FR-2025-06-11/html/2025-10804.htm (full text fetched; amendments to EO 14144 section 7 read directly)
- OMB Memorandum M-26-14, *Ensuring Effective and Efficient Agency Logging and Network Visibility to Defend Against Evolving Cyber Threats* (22 May 2026) — https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf (fetched)
- OMB/CISA, *FY 2026 & FY 2027 CIO FISMA Metrics*, version 1.0 (3 August 2026) — https://www.cisa.gov/sites/default/files/2026-08/FY2026-FISMA-cio-metrics.pdf (document text obtained; the CISA web server blocks scripted downloads)
- UK NCSC, *Zero trust architecture design principles* (version 1.1, reviewed 16 January 2026) — https://www.ncsc.gov.uk/collection/zero-trust-architecture (fetched)
- GSA Federal Acquisition Service, *Zero Trust Strategy Buyer's Guide — DoD Zero Trust Strategy*, v1.4 (May 2025) — https://buy.gsa.gov/api/system/files/documents/dod-zero-trust-strategy-buyer-s-guide-version-1.4-may-2025-508-reviewed_0.pdf (fetched; used for DoD pillar, capability and FY2027/FY2032 figures because the DoD Strategy PDF at dodcio.defense.gov returned access denied)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
