# CSA Cloud Controls Matrix (CCM) v4

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | Cloud Security Alliance (CSA) — nonprofit, community/working-group developed |
| Current version | v4 (initial release 2021, with subsequent v4.0.x errata/mapping updates — verify the current minor release before citing) |
| Structure | 17 domains → ~197 control specifications (v4.0 baseline; count can shift slightly across v4.0.x updates — verify) |
| Companion artifact | CAIQ — Consensus Assessments Initiative Questionnaire (yes/no/NA self-assessment questions derived from the CCM controls) |
| Certifiable? | Not directly, but it anchors the CSA STAR program: Level 1 self-assessment registry, Level 2 third-party certification/attestation (CCM combined with ISO 27001 or SOC 2) |
| Typical use | Cloud service provider (CSP) security programs, customer due diligence on CSPs, cloud-specific gap assessments, STAR submissions, RFP security requirements |
| Cost | Free download from CSA (registration required) |
| Distinctive feature | Every control carries a shared-responsibility allocation — CSP-owned, customer-owned, or shared — which generic frameworks lack |

## The 17 domains

Domain names below reflect the v4 publication; verify exact wording against the current CSA release before quoting in deliverables.

| ID | Domain |
|---|---|
| A&A | Audit & Assurance |
| AIS | Application & Interface Security |
| BCR | Business Continuity Management & Operational Resilience |
| CCC | Change Control & Configuration Management |
| CEK | Cryptography, Encryption & Key Management |
| DCS | Datacenter Security |
| DSP | Data Security & Privacy Lifecycle Management |
| GRC | Governance, Risk & Compliance |
| HRS | Human Resources |
| IAM | Identity & Access Management |
| IPY | Interoperability & Portability |
| IVS | Infrastructure & Virtualization Security |
| LOG | Logging & Monitoring |
| SEF | Security Incident Management, E-Discovery & Cloud Forensics |
| STA | Supply Chain Management, Transparency & Accountability |
| TVM | Threat & Vulnerability Management |
| UEM | Universal Endpoint Management |

Controls are numbered `DOMAIN-nn` (e.g., IAM-01, LOG-05). Compared to v3.0.1, v4 restructured domains (e.g., splitting cryptography/key management into CEK, adding UEM and expanding data security into DSP) and roughly doubled the mapping coverage — treat v3-era assessments as non-comparable without the CSA-published v3→v4 transition mapping.

## What a control specification contains

Each of the ~197 control specifications includes:

- **Control ID and title** plus the control specification text itself (outcome-oriented, one to a few sentences)
- **Shared Security Responsibility Model (SSRM) guidance** — whether the control is typically CSP-owned, cloud service customer (CSC)-owned, or shared, and how that allocation varies by service model (IaaS/PaaS/SaaS)
- **Implementation guidelines** and **auditing guidelines** (published as companion documents to the matrix — verify availability for the specific v4.0.x release)
- **Mappings** to other frameworks (see below)
- Corresponding **CAIQ question(s)**

The SSRM treatment is the CCM's core value: for any given control you can state which party must implement it and which party must verify it. No mainstream generic framework (ISO 27001, NIST CSF, CIS) does this natively.

## CAIQ — the questionnaire layer

The Consensus Assessments Initiative Questionnaire converts each CCM control into one or more closed-ended questions a CSP answers (yes/no/NA, with SSRM ownership per answer in the v4 format). In v4 the CAIQ was consolidated with the CCM into a single artifact rather than maintained as a separate question bank — verify the exact question count for the release you use rather than quoting one.

Practical roles:

- **For CSPs:** the standard "fill this in once, reuse for every prospect" security questionnaire; a completed CAIQ published to the STAR Registry is STAR Level 1.
- **For customers:** a free, cloud-specific due-diligence questionnaire that is materially better for assessing a CSP than a generic ISO-derived question set — see [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).

## STAR program

The CSA Security, Trust, Assurance and Risk (STAR) Registry is a public repository of CSP assurance submissions:

| Level | Mechanism | Assurance |
|---|---|---|
| Level 1 | Self-assessment: CSP publishes its completed CAIQ (and/or CCM self-evaluation) to the public STAR Registry | Self-attested; useful for transparency and scoping, not independent assurance |
| Level 2 | Third-party assessment: **STAR Certification** (CCM assessed on top of an ISO/IEC 27001 certification audit) or **STAR Attestation** (CCM incorporated into a SOC 2 examination) | Independent; combines a recognized base standard with cloud-specific CCM coverage |

CSA has also described a continuous/automated assurance level above these; treat its status and naming as evolving — verify against current CSA program documentation before citing it.

For assessors: a STAR Level 2 entry tells you the CSP holds ISO 27001 or a SOC 2 report *and* had CCM controls examined — ask for the underlying certificate/report anyway; the registry entry is a pointer, not the evidence. See [audit-preparation](../../skills/audit-preparation/SKILL.md).

## Mapping ecosystem

CSA publishes official mappings/gap analyses from CCM v4 to, among others:

- ISO/IEC 27001/27002 (including cloud extensions 27017 and privacy 27018) — see [iso-27001-2022.md](iso-27001-2022.md)
- NIST SP 800-53 — see [nist-800-53.md](nist-800-53.md)
- NIST CSF — see [nist-csf-2.md](nist-csf-2.md)
- CIS Controls — see [cis-controls-v8.md](cis-controls-v8.md)
- PCI DSS — see [pci-dss-4.md](pci-dss-4.md)
- AICPA Trust Services Criteria (the basis for STAR Attestation) — see [soc2-tsc.md](soc2-tsc.md)
- Various national/sectoral schemes (e.g., European cloud schemes) — check the CSA mapping catalog for the current list

The usual mapping caveats apply — directional, lossy, coverage not equivalence. CCM controls tend to be more granular than ISO 27002 controls and more cloud-specific than 800-53 baselines. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## When to use CCM vs a generic framework

Use CCM when:

- **You are a cloud-native provider.** A SaaS/PaaS/IaaS company gets a control catalog whose scope matches its actual estate — virtualization, tenant isolation, interoperability/portability, cloud forensics — instead of retro-fitting datacenter-era controls.
- **You assess CSPs.** SSRM allocation per control forces the "who does what" conversation that generic questionnaires blur; a vendor's CAIQ answers slot directly into your third-party review.
- **You need to demonstrate cloud assurance publicly.** STAR Level 1 is a low-cost transparency signal; Level 2 upgrades an existing ISO 27001 or SOC 2 investment with cloud-specific coverage rather than requiring a separate program.
- **Regulators or customers ask "how does your ISO cert cover cloud?"** CCM (or ISO 27017) is the standard answer.

Prefer a generic framework when the organization is not primarily a cloud provider or heavy cloud consumer, when the audience expects ISO/SOC 2/NIST vocabulary, or when certification itself (rather than cloud-specific depth) is the goal — then layer CCM on top for the cloud estate rather than replacing the base framework.

## Using this in assessments

- **Always capture SSRM allocation in the findings.** A "gap" against a CSP-owned control at a SaaS customer is not the customer's gap — it is a vendor-assurance question. Splitting the gap register by responsible party is the single highest-value CCM-specific habit. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
- **Service-model matters.** The same control's allocation differs across IaaS/PaaS/SaaS; assess per service, not per vendor, when a provider offers multiple models.
- **CAIQ answers are self-attested.** Treat "yes" answers as claims to be sampled and evidenced, not conclusions — especially for Level 1 registry entries with no third-party assessment behind them. See [control-testing](../../skills/control-testing/SKILL.md).
- **Scoping vendor reviews:** for a critical CSP, request the CAIQ plus the underlying ISO 27001 certificate or SOC 2 report; for lower-tier cloud vendors, a current CAIQ alone is a proportionate ask.
- **Version hygiene:** confirm whether artifacts you receive are CCM v3.0.1 or v4 — the domain structure differs enough that cross-version comparison without the official transition mapping produces false gaps.
- **Regulatory overlays:** CCM is a control catalog, not a legal instrument; for EU cloud customers pair it with the applicable regulation (e.g., [DORA](../regulations/dora.md) for financial entities, [NIS2](../regulations/nis2.md) for in-scope sectors).

Related skills: [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md), [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md), [control-mapping](../../skills/control-mapping/SKILL.md), [soc2-readiness](../../skills/soc2-readiness/SKILL.md).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
