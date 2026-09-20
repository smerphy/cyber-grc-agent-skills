# IEC 62443 / ISA-62443 — Security for industrial automation and control systems (with NIST SP 800-82 Rev. 3)

## At a glance

| Attribute | Detail |
|---|---|
| Publishers | IEC TC 65/WG 10 and the ISA99 committee (established 2002), developed jointly and published in parallel as `ANSI/ISA-62443-x-y` and `IEC 62443-x-y`; the two are not always at the same revision — e.g. ANSI/ISA-62443-2-4-2018 corresponds to IEC 62443-2-4:2015+AMD1:2017, while IEC is at edition 2.0 (2023) |
| Scope object | Industrial automation and control systems (IACS) = the Automation Solution (hardware/software as installed and configured) plus the organizational measures for its design, deployment, operation and maintenance |
| Structure | A multi-part series organised in groups: 1-x general, 2-x policies and procedures, 3-x system, 4-x component, plus 6-x evaluation methodologies |
| Status | Not a single standard: parts carry their own editions and dates (2-1 ed. 2.0 2024-08-07; 3-2 2020-06-24; 3-3 2013-08-07; 4-1 2018-01-15; 4-2 2019-02-27; 2-4 ed. 2.0 2023-12-15) |
| Horizontal designation | IEC recognised the series as a horizontal standard in 2021 — proven to apply across industries, not just process manufacturing |
| Measurement model | Security levels SL 1–4 for technical capability; maturity levels ML 1–4 (CMMI-derived) for processes; SL-T (target), SL-C (capability), SL-A (achieved) |
| Certifiable? | Yes, through schemes rather than the standards themselves: ISASecure (CSA, ICSA, SSA, SDLA, ACSSA) with ISO/IEC 17065-accredited certification bodies; IECEE conformity assessment for 62443 |
| Cost | Paywalled per part (e.g. IEC 62443-3-3 listed at CHF 380); previews of front matter and contents are public |
| US counterpart guidance | NIST SP 800-82r3, *Guide to Operational Technology (OT) Security* (September 2023), free; Rev. 4 at pre-draft stage — call for comments closed 23 February 2026, no draft published as of September 2026 |
| Related but distinct | ISO/IEC 27019 (energy-sector 27002 extension) and IEC 62351 (power-system communications) are used alongside 62443, not in place of it |

## What it is

IEC 62443 is the international, consensus-developed standard series for securing industrial automation and control systems across their lifecycle. Its central premise is that IACS security is a **shared responsibility** across the stakeholder groups ISA names — asset owners (end users), product suppliers, integrators who build and maintain control system solutions, and service suppliers who support their operation — and that requirements must be allocated to whichever role can actually meet them. It is engineering-flavoured rather than management-system-flavoured: risk assessment produces zones, conduits and target security levels, and those targets are then met by product capability, system design, or compensating countermeasures.

The series was written for a world where the object being protected is a physical process. Consequences include loss of life or health, environmental damage and loss of product integrity, not only information disclosure; equipment lifespans can exceed twenty years; and legacy components often cannot support the technical requirement directly, so the standards explicitly admit compensating countermeasures and brownfield adaptation (IEC 62443-2-1:2024, Scope).

NIST SP 800-82r3 is the complementary US guidance: free, narrative, and broader in scope than ICS (it covers building automation, transportation, physical access control and measurement systems). It applies the NIST Risk Management Framework to OT, maps its risk-management tasks to both the Cybersecurity Framework and IEC 62443, and carries an OT overlay of SP 800-53 Rev. 5 in Appendix F. The two are used together: 62443 for requirements, role allocation and certification; 800-82 for programme narrative, architecture patterns and a federal-compatible control baseline.

## Who it covers / Scope

- **Roles, not entities.** Requirements are addressed to asset owners (2-1), service providers (2-4), and product suppliers (4-1 process, 4-2 product capability). A single organisation frequently holds more than one role.
- **Sectors.** Originally the process industries; ISA records use cases from more than 20 industries and states the series applies to all automation and control systems, not only industrial — the basis of the 2021 horizontal-standard designation. NIST SP 800-82r3 names industrial control systems, building automation, transportation, physical access control and physical environment monitoring/measurement systems as OT.
- **No legal force on its own.** 62443 is voluntary unless pulled in by contract, by a sector regulator, or by procurement. OT-relevant legal regimes sit in separate packs — see Interplay.
- **Applicability filtering is expected.** IEC 62443-2-1:2024 states that not all requirements apply to all IACS (e.g. wireless or remote-access requirements where those technologies are absent) and that the asset owner must identify which requirements apply to its environments.
- **NIST SP 800-82r3 scope:** all OT, defined as programmable systems and devices that interact with, or manage devices that interact with, the physical environment.

## Structure and requirements

### Parts of the series (IEC editions, with publication dates)

| Part | Title | Edition / date | Role addressed |
|---|---|---|---|
| IEC TS 62443-1-1 | Terminology, concepts and models | 2009 | All — defines IACS and the seven foundational requirements |
| IEC TS 62443-1-5 | Scheme for IEC 62443 security profiles | 2023-09-15 | Scheme owners; supports comparable conformity assessment |
| IEC PAS 62443-1-6 | Application of the series to the Industrial IoT (IIoT) | 2025-12-19 | Asset owners, service providers (PAS withdrawn automatically after 4 years) |
| IEC 62443-2-1 | Security program requirements for IACS asset owners | Ed. 2.0, 2024-08-07 | Asset owner |
| IEC PAS 62443-2-2 | IACS security protection scheme (SPS) | 2025-03-11 | Asset owner — technical, physical and process measures in operation |
| IEC TR 62443-2-3 | Patch management in the IACS environment | 2015-06-30 | Asset owner, product supplier |
| IEC 62443-2-4 | Security program requirements for IACS service providers | Ed. 2.0, 2023-12-15 | Integration and maintenance service providers; supports profiles |
| IEC TR 62443-3-1 | Security technologies for IACS | 2009-07-30 | All — survey of countermeasure technologies |
| IEC 62443-3-2 | Security risk assessment for system design | 2020-06-24 | Asset owner / integrator — zones, conduits, SL-T |
| IEC 62443-3-3 | System security requirements and security levels | 2013-08-07 (COR1:2014 incorporated) | System — SL-C(control system) |
| IEC 62443-4-1 | Secure product development lifecycle requirements | 2018-01-15 | Product supplier (developer and maintainer only) |
| IEC 62443-4-2 | Technical security requirements for IACS components | 2019-02-27 (Aug 2022 corrigendum incorporated) | Product supplier — SL-C(component) |
| IEC TS 62443-6-1 | Security evaluation methodology for IEC 62443-2-4 | 2024-03-12 | Evaluators, first/second/third party |
| IEC TS 62443-6-2 | Security evaluation methodology for IEC 62443-4-2 | 2025-01-21 | Evaluators (assumes a 4-1 lifecycle as prerequisite) |

### The seven foundational requirements (FRs)

Defined in IEC TS 62443-1-1 and used to organise the technical requirements in 3-3 (system requirements, SRs) and 4-2 (component requirements, CRs), each with requirement enhancements (REs) allocated to security levels.

| FR | Name | Abbrev. |
|---|---|---|
| FR 1 | Identification and authentication control | IAC |
| FR 2 | Use control | UC |
| FR 3 | System integrity | SI |
| FR 4 | Data confidentiality | DC |
| FR 5 | Restricted data flow | RDF |
| FR 6 | Timely response to events | TRE |
| FR 7 | Resource availability | RA |

FR 1 and FR 2 together are what IT calls access control; they were split to keep requirement counts manageable.

### Security levels

| SL | Definition (means / resources / skills / motivation) |
|---|---|
| SL 1 | Protection against casual or coincidental violation |
| SL 2 | Intentional violation using simple means, low resources, generic skills, low motivation |
| SL 3 | Intentional violation using sophisticated means, moderate resources, IACS-specific skills, moderate motivation |
| SL 4 | Intentional violation using sophisticated means, extended resources, IACS-specific skills, high motivation |

- Three *uses* of the scale: **SL-T** (target, an output of the 3-2 risk assessment, recorded in the cybersecurity requirements specification), **SL-C** (capability a system or component can provide when properly integrated and configured), **SL-A** (achieved, measured after commissioning).
- A zone or conduit is rated as a **seven-element SL vector**, one element per FR — e.g. SL = (3,3,3,1,2,1,3) — so confidentiality can be rated low where integrity and availability are rated high; an element may be set to none/0 where an FR is not a security objective.
- Requirements may be met directly or by **compensating countermeasures**, which is how brownfield plant reaches a target level with equipment that cannot support the native capability.
- Security measures must not adversely affect **essential functions** (safety instrumented function, control function, operator view/manipulate) of a high-availability IACS unless a risk assessment supports it.

### Maturity levels (processes)

Used in Parts 2-1, 2-2, 2-4 and 4-1 to measure how thoroughly process requirements are met. Based on CMMI, with Levels 4 and 5 combined.

| ML | Name | Meaning |
|---|---|---|
| 1 | Initial | Ad hoc, often undocumented; repeatability not assured |
| 2 | Managed | Managed by written policies; trained personnel; some defined processes not yet in practice |
| 3 | Defined (Practiced) | Repeatable across the organisation, in practice, with documented evidence |
| 4 | Improving | Process metrics used to control effectiveness and performance; continuous improvement |

### Asset-owner programme structure (IEC 62443-2-1:2024)

Edition 2.0 restructured requirements into eight **security program elements (SPEs)**, eliminated duplication with an ISMS, and defined a maturity model for evaluating requirements:

| SPE | Element | Requirement groups |
|---|---|---|
| 1 | Organizational security measures | ORG 1 security related organization and policies; ORG 2 security assessments and reviews; ORG 3 security of physical access |
| 2 | Configuration management | CM 1 inventory management of IACS hardware/software components (baseline, drawings, configuration settings, change control) |
| 3 | Network and communications security | NET 1 system segmentation; NET 2 secure wireless access; NET 3 secure remote access |
| 4 | Component security | COMP 1 components and portable media; COMP 2 malware protection; COMP 3 patch management |
| 5 | Protection of data | DATA 1 protection of data (classification, confidentiality, retention, cryptography) |
| 6 | User access control | USER 1 identification and authentication; USER 2 authorization and access control |
| 7 | Event and incident management | EVENT 1 event and incident management |
| 8 | System integrity and availability | AVAIL 1 system availability and intended functionality; AVAIL 2 backup/restore/archive |

### Risk assessment workflow (IEC 62443-3-2)

ZCR 1 identify the system under consideration → ZCR 2 initial cyber risk assessment → ZCR 3 partition into zones and conduits → ZCR 4 decision: does initial risk exceed tolerable risk? → ZCR 5 detailed risk assessment → document cybersecurity requirements, assumptions and constraints in the **cybersecurity requirements specification (CRS)** → ZCR 7 asset-owner approval. Outputs: zone/conduit diagrams, residual risk and SL-T per zone and conduit.

### NIST SP 800-82 Rev. 3 content map

| Chapter / annex | Content |
|---|---|
| Ch. 2 | OT overview: SCADA, DCS, PLC topologies, building automation, physical access control, safety systems, IIoT; OT vs IT security comparison |
| Ch. 3 | Building the OT cybersecurity programme: charter, business case, governance, OT-specific policies, training, incident response and recovery capability |
| Ch. 4 | Risk management for OT, including applying the RMF (Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor) with task-level mappings to CSF and IEC 62443 |
| Ch. 5 | Architecture: defence-in-depth layers (security management, physical, network, hardware, software), field I/O (Purdue Level 0) considerations, IIoT, DCS/PLC/SCADA reference models |
| Ch. 6 | Applying the Cybersecurity Framework to OT, organised by CSF 1.1 functions and categories (ID.AM, ID.GV, PR.AC, DE.CM, RS.RP, RC.RP …) |
| App. F | **OT overlay** — a partial tailoring of SP 800-53 Rev. 5 controls and Low/Moderate/High baselines (per FIPS 199) with OT-specific supplemental guidance |

800-82r3 states the priority ordering explicitly: IT information security programmes focus on confidentiality, integrity and availability *in that order*, whereas OT "instead prioritizes safety, followed by availability, integrity, and confidentiality".

## Assessment, certification and evidence

- **ISASecure** (founded 2007, a wholly owned subsidiary of ISA; the ISA Security Compliance Institute, ISCI, owns the conformance scheme) certifies to the series through ISO/IEC 17065-accredited certification bodies: **CSA** and **ICSA** (components / IIoT components, to 62443-4-2), **SSA** (systems, to 62443-3-3), **SDLA** (development organisations, to 62443-4-1), and **ACSSA** (deployed IACS and asset-owner programme, to 62443-2-1, 2-4, 3-2 and 3-3).
- **ACSSA 1.0.0** became effective **17 February 2026**. Two paths: *inspection* (letter plus formal report from an ISO/IEC 17020-accredited inspection body) and *certification* (three-year validity with periodic surveillance and recertification, from an ISO/IEC 17065-accredited certification body). Eligibility requires an IACS either in operation or near transition to operation, with submissions such as a system asset inventory under change control and a risk assessment performed in accordance with 62443-3-2 (criteria in specification ACSSA-300). Supplier and service-provider certificates (4-2, 3-3, 4-1, 2-4 at ML 3) feed evidence into an ACSSA evaluation but do not replace evidence of the asset owner's *use* of those capabilities.
- **In development.** On 20 August 2026 ISASecure announced a partnership with the US National Security Agency's Operational Technology Assurance Partnership (OTAP) to build a **High Criticality Component Security Assurance (HCSA)** scheme derived from CSA; once accepted it is intended as an approved certification mechanism for adding OT components to the NSS OT Product Compliant List. Not yet available as of September 2026.
- **IECEE** operates a conformity assessment programme yielding IECEE Certificates of Conformity against 62443 parts, including capability certification for 62443-2-4 and 4-1 and product certificates for 62443-3-3 and 4-2.
- **Evaluation methodologies** IEC TS 62443-6-1 (for 2-4) and 6-2 (for 4-2) exist to make evaluations repeatable and reproducible; 6-2 assumes a 62443-4-1 secure development lifecycle as a prerequisite and does not prescribe tools or a certification scheme.
- **Evidence practice.** Certification is per product, per system or per site — never organisation-wide. In vendor assessments, always ask for the certificate scope, the certified version, the SL and, for 2-4, the ML. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 2002 | ISA99 committee formed; series later developed jointly with IEC TC 65/WG 10 |
| 2013-08-07 | IEC 62443-3-3 published (corrigendum 2014 incorporated); still edition 1.0 |
| 2018 / 2019 | IEC 62443-4-1 (2018-01-15) and 4-2 (2019-02-27) published — the basis of most product certification |
| 2020-06-24 | IEC 62443-3-2 published (zones, conduits, SL-T) |
| 2021 | IEC recognises the series as a horizontal standard |
| 2023-09 | NIST SP 800-82 Rev. 3 published, superseding Rev. 2 (2015) |
| 2023-12-15 | IEC 62443-2-4 edition 2.0 (service providers) |
| 2024-03-12 | IEC TS 62443-6-1 evaluation methodology for 2-4 |
| 2024-08-07 | IEC 62443-2-1 edition 2.0 — SPE restructure, ISMS de-duplication, maturity model |
| 2025-01-21 / 2025-03-11 / 2025-12-19 | IEC TS 62443-6-2 (evaluation methodology for 4-2); IEC PAS 62443-2-2 (security protection scheme); IEC PAS 62443-1-6 (IIoT) |
| 2026-01-22 | NIST opens a pre-draft call for comments on **SP 800-82 Rev. 4**, to align with CSF 2.0, NIST IR 8286 Rev. 1 and SP 800-53 Rev. 5.2.0; comments closed 23 February 2026. No draft published as of September 2026 |
| 2026-02-17 | ISASecure ACSSA 1.0.0 scheme effective (certifies to 62443-2-1, 2-4, 3-2 and 3-3) |
| 2026-07-13 | A2LA extends accreditation to ISASecure ACSSA certification-body and inspection-body programmes |
| 2026-08-20 | ISASecure and NSA OTAP announce development of the HCSA scheme for high-criticality components |
| Pending | As of September 2026 the IEC webstore shows 3-2, 3-3 and 4-2 still at their original editions (stability date 2027) and 2-1 at a 2026 stability date, with **no** revision registered as under development for any of them. Registered under development: 62443-1-1 as a full International Standard (stage PCC, forecast 2027-12-31), 62443-6-1 (stage ACDV, forecast 2027-09-01, registered without the TS prefix), 62443-4-1 edition 2.0 (stage PCC, forecast 2028-04-21) and 62443-2-4 edition 3.0 (stage PCC, forecast 2028-05-31). Forecast dates move; treat any claim of a published "62443-4-2:2026" as unverified until the webstore entry changes. IEC PAS 62443-1-6:2025 exists because much of the series was written before IIoT was common; as a PAS it is automatically withdrawn after four years |

EU angle: the Commission's CRA standardisation request **M/606** covers 41 harmonised standards (horizontal and product-specific) to support the Cyber Resilience Act. Reports that the resulting component/system standards are built on 62443-3-3, 4-1 and 4-2 come from industry commentary rather than the Commission's own page — treat the specific standard numbers as **(verify)**.

## Key obligations for security/GRC teams

1. **Decide which roles you hold** (asset owner, service provider, product supplier) before selecting parts; the requirement sets and the evidence expected differ per role. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Run 62443-3-2 properly**: define the system under consideration, partition into zones and conduits, and set an SL-T vector per zone/conduit with documented rationale in a CRS. Without SL-Ts, every later control debate is unanchored. See [risk-assessment](../../skills/risk-assessment/SKILL.md).
3. **Build the asset-owner programme against 62443-2-1:2024 SPEs** and assess each requirement at a maturity level, not a binary pass/fail — ML 3 (practiced with documented evidence) is the realistic assurance target. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
4. **Track SL-C vs SL-T per zone** and record every gap closed by a compensating countermeasure as a documented, time-bound exception; legacy plant is where these accumulate. See [exception-management](../../skills/exception-management/SKILL.md).
5. **Put 62443 requirements into procurement**: 4-1 (development process) and 4-2 (component capability) for products, 2-4 with a maturity-level expectation for integrators and maintenance providers; ask for certificate scope, not marketing claims. See [vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
6. **Do not let IT controls break essential functions** — access control, malware protection and patching in OT must be justified against safety and availability, with the 800-82r3 defence-in-depth layers as the architecture reference.
7. **Map the OT control set to the enterprise framework once** (CSF 2.0, ISO 27001, 800-53 via the 800-82r3 Appendix F overlay) so OT reports into the same risk register rather than a parallel one. See [control-mapping](../../skills/control-mapping/SKILL.md) and [framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
8. **Wire OT into incident response and regulatory reporting**: OT incidents trigger sector clocks (see the regulation packs below), and 800-82r3 treats incident response and recovery capability as core programme content. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).
9. **Test the OT controls that matter** — segmentation between zones, remote-access paths, backup/restore of controller configurations — with methods that respect process availability. See [control-testing](../../skills/control-testing/SKILL.md).
10. **Report OT posture in board terms**: SL-T coverage by zone, ML by SPE, and certified-supplier share, rather than raw vulnerability counts. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **ISO/IEC 27001:** complementary, not overlapping. 62443-2-1:2024 was deliberately edited to remove duplication with an ISMS, so run the ISMS for management-system obligations and 62443 for IACS-specific requirements. See [iso-27001-2022.md](iso-27001-2022.md).
- **NIST CSF 2.0 and SP 800-53:** 800-82r3 currently applies CSF 1.1 structure and tailors 800-53 Rev. 5; Rev. 4 is intended to align with CSF 2.0. Until then, expect to re-map Govern-function content yourself. See [nist-csf-2.md](nist-csf-2.md) and [nist-800-53.md](nist-800-53.md).
- **Product-security regimes:** 62443-4-1/4-2 are the natural evidence base for manufacturer obligations under the EU Cyber Resilience Act and adjacent product rules — see [eu-cyber-resilience-act.md](../regulations/eu-cyber-resilience-act.md) and [eu-product-security-red-machinery.md](../regulations/eu-product-security-red-machinery.md); secure-development expectations also align with [nist-ssdf-800-218.md](nist-ssdf-800-218.md).
- **Sector regimes:** NIS2 for EU essential/important entities ([nis2.md](../regulations/nis2.md)), NERC CIP for the bulk electric system ([nerc-cip.md](../regulations/nerc-cip.md)), TSA directives for pipelines and rail ([us-tsa-transportation-cyber.md](../regulations/us-tsa-transportation-cyber.md)), FDA premarket cybersecurity for medical devices ([us-fda-medical-device-cybersecurity.md](../regulations/us-fda-medical-device-cybersecurity.md)), UN R155/ISO 21434 for vehicles ([automotive-un-r155-iso-21434.md](../regulations/automotive-un-r155-iso-21434.md)). None of these makes 62443 mandatory by itself; 62443 is the usual way to evidence "state of the art" OT controls under them.
- **Supply chain:** pair 62443-2-4 service-provider requirements with [nist-800-161-cscrm.md](nist-800-161-cscrm.md) for the procurement and continuous-monitoring layer.
- **Baseline hygiene:** where an OT site has no programme at all, CIS Controls IG1 is a faster starting point than a full 62443 gap assessment; migrate to 62443 once zones and conduits exist. See [cis-controls-v8.md](cis-controls-v8.md).
- **Adjacent standards:** ISO/IEC 27019 (energy-sector control systems) and IEC 62351 (power-system communications security) are used alongside 62443 in the energy domain.

## Primary sources

- IEC webstore publication pages (publisher, current editions and dates): [62443-2-1:2024](https://webstore.iec.ch/en/publication/62883), [PAS 62443-2-2:2025](https://webstore.iec.ch/en/publication/63886), [62443-2-4:2023](https://webstore.iec.ch/en/publication/67631), [62443-3-2:2020](https://webstore.iec.ch/en/publication/30727), [62443-3-3:2013](https://webstore.iec.ch/en/publication/7033), [62443-4-1:2018](https://webstore.iec.ch/en/publication/33615), [62443-4-2:2019](https://webstore.iec.ch/en/publication/34421), [TS 62443-6-1:2024](https://webstore.iec.ch/en/publication/67462), [TS 62443-6-2:2025](https://webstore.iec.ch/en/publication/67463), [TS 62443-1-5:2023](https://webstore.iec.ch/en/publication/67461), [PAS 62443-1-6:2025](https://webstore.iec.ch/en/publication/102885), [TS 62443-1-1:2009](https://webstore.iec.ch/en/publication/7029), [TR 62443-2-3:2015](https://webstore.iec.ch/en/publication/22811), [TR 62443-3-1:2009](https://webstore.iec.ch/en/publication/7031) — all fetched. These pages also carry each part's stability date and any registered under-development revision.
- IEC 62443-2-1 Edition 2.0 (2024-08) official preview (scope, contents, SPE structure): https://webstore.iec.ch/en/iec_catalog/product/preview/?id=L3B1Yi9wZGYvcHJldmlldy9pbmZvX2llYzYyNDQzLTItMXtlZDIuMH1iLnBkZg%3D%3D — fetched. Full text is paywalled.
- IEC official previews used for scope and title wording of IEC PAS 62443-1-6:2025 (IIoT rationale, PAS four-year withdrawal note): https://webstore.iec.ch/en/iec_catalog/product/preview/?id=L3B1Yi9wZGYvcHJldmlldy9pbmZvX2llY3BhczYyNDQzLTEtNntlZDEuMH1lbi5wZGY%3D — fetched. Previews for TS 62443-1-5, PAS 62443-2-2, 62443-4-1, TS 62443-6-1 and TS 62443-6-2 were fetched the same way from the same catalogue endpoint.
- ISA, *ISA/IEC 62443 Series of Standards* (publisher page; ISA editions, horizontal-standard designation, ISASecure schemes): https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards — fetched.
- IEC SyC Smart Energy, *IEC 62443* (IEC page; FRs, SL vector, IECEE conformity assessment): https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ — fetched.
- ISAGCA, *Quick Start Guide: An Overview of ISA/IEC 62443 Standards* (publisher guide; SL and ML definitions, SL-T/SL-C/SL-A, ZCR steps, essential functions): https://isasecure.org/hubfs/2023%20ISA%20Website%20Redesigns/ISAGCA/PDFs/ISAGCA%20Quick%20Start%20Guide%20FINAL.pdf — fetched.
- ISASecure certification schemes and ACSSA scheme description: https://www.isasecure.org/certification and https://isasecure.org/acssa-certification — fetched.
- ISASecure news and events (A2LA ACSSA accreditation, 13 July 2026; NSA OTAP / HCSA announcement, 20 August 2026): https://isasecure.org/news-events and https://isasecure.org/news-events/isasecure-to-develop-certification-scheme-for-commercial-components-procured-by-us-government — fetched.
- NIST SP 800-82r3, *Guide to Operational Technology (OT) Security* (September 2023): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf and its CSRC record (publication date, supersession of Rev. 2) https://csrc.nist.gov/pubs/sp/800/82/r3/final — both fetched.
- NIST CSRC, OT overlay entry in the control overlay repository (Appendix F tailoring of SP 800-53 Rev. 5): https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/overlay-repository/nist-developed-overlay-submissions/operational-technology — fetched.
- NIST CSRC, *SP 800-82 Rev. 4 Pre-Draft Call for Comments* (22 January 2026): https://csrc.nist.gov/pubs/sp/800/82/r4/iprd — fetched.
- European Commission, *Cyber Resilience Act — Standardisation* (M/606, 41 standards): https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation — fetched.
- Not fetched / blocked: iec.ch blog *Understanding IEC 62443* (challenge page), ISA Global Cybersecurity Alliance standards-status blog (403), cisa.gov industrial control systems topic page (403).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
