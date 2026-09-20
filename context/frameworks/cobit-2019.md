# COBIT 2019 — Control Objectives for Information and Related Technologies (ISACA)

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | ISACA (Schaumburg, IL, USA). "COBIT" is an ISACA trademark |
| Current edition | COBIT 2019 — launched November 2018; ISACA describes it as the first update in nearly seven years (COBIT 5 was 2012) |
| Subject matter | Enterprise governance of information and technology (EGIT) — not a security control catalogue |
| Structure | 5 domains → 40 governance and management objectives → practices → activities; each objective supported by 7 component types |
| Tailoring mechanism | 11 design factors plus the goals cascade (13 enterprise goals → 13 alignment goals → 40 objectives), applied through the Design Guide workflow |
| Performance model | COBIT Performance Management (CPM): capability and maturity levels 0–5, aligned to and extending CMMI Development V2.0 (COBIT 5 used ISO/IEC 33000 SPICE) |
| Certifiable? | No enterprise certification scheme. ISACA's credentialing catalogue lists individual certificates only: COBIT Foundation, COBIT Design & Implementation and the legacy COBIT 5 certificates |
| Positioning | Deliberately an "umbrella" framework: it references and integrates other standards rather than replacing them |
| Successor in flight | COBIT 7 — the COBIT 2019 Foundations Certificate is replaced by the COBIT 7 Foundations Certificate on 27 October 2026; COBIT 2019 Foundations sunsets 26 April 2027 |

## What it is

COBIT is ISACA's framework for the governance and management of enterprise information and technology. It was first released in 1996 as *Control Objectives for Information and Related Technology*, shipped on diskette, consolidating and harmonising standards from 18 global sources for an audience of IT auditors. It grew in phases: COBIT 2 (1998) added IT control guidance, COBIT 3 (2000) made it a management framework, COBIT 4 (2005) a full IT governance framework, and COBIT 5 (2012) a comprehensive practices-and-models framework. COBIT turned 30 in 2026, with more than one million publication downloads to date.

COBIT 2019 answers a narrower and more useful question than most security frameworks: **who decides, who is accountable, and how would we prove it**. It separates *governance* (the board evaluates options, directs management, and monitors performance and compliance) from *management* (plan, build, run, monitor within the direction the governing body set) and gives each its own objectives. That governance/management split is what makes COBIT the usual reference when an auditor or regulator asks who owns an IT decision rather than whether a control fired.

Its second distinguishing feature is that it is explicitly generic and expected to be cut down. An enterprise starts from the COBIT core model and tailors it using design factors; ISACA is clear that few organisations will implement COBIT in its entirety. Content is published across several publications rather than in a single book — the two framework volumes (*Introduction and Methodology*, *Governance and Management Objectives*) plus the *Design Guide* and *Implementation Guide*, with focus-area publications layered on top.

## Who it covers / Scope

COBIT is voluntary. No statute mandates it and it carries no penalties; adoption is driven by boards, internal audit functions, and external expectations.

- **Any enterprise, any size, any sector.** ISACA publishes *COBIT 2019 for Small and Medium Enterprises* for smaller adopters.
- **Scope is the whole enterprise, not the IT department.** The end-to-end principle covers all enterprise functions and all technology and information used to achieve enterprise goals, not only the IT function.
- **Practical scoping is done by design factors** (below), which produce a prioritised subset of the 40 objectives and target capability levels for each — that subset, not the full core model, is the assessable scope.
- **Common institutional drivers:** IT audit programmes (COBIT's original audience), SOX ITGC design work, board-level IT governance reporting, and integration of multiple overlapping frameworks under one structure.

## Structure and requirements

### Principles

COBIT 2019 states **six principles for a governance system** (COBIT 5 had five): a governance system must satisfy stakeholder needs and generate value from I&T; it is built from several components of different types working holistically; it must be dynamic, reconsidered whenever a design factor changes; governance activities and structures are distinct from management ones; it is tailored to the enterprise's needs using design factors; and it is end-to-end, covering all enterprise functions.

COBIT 2019 adds **three governance framework principles** (absent in COBIT 5), addressed to the framework itself rather than the enterprise: it should be based on a conceptual model identifying key components and their relationships; it should be open and flexible, allowing new content and new issues to be added without losing integrity and consistency; and it should be aligned to major relevant standards, frameworks and regulations.

### The core model — five domains, 40 objectives

| Domain | Type | Objectives | Focus |
|---|---|---|---|
| **EDM** — Evaluate, Direct and Monitor | Governance | EDM01 Ensured Governance Framework Setting and Maintenance · EDM02 Ensured Benefits Delivery · EDM03 Ensured Risk Optimization · EDM04 Ensured Resource Optimization · EDM05 Ensured Stakeholder Engagement | Governing-body activity: set direction, evaluate options, monitor delivery |
| **APO** — Align, Plan and Organize | Management | APO01 Managed I&T Management Framework · APO02 Strategy · APO03 Enterprise Architecture · APO04 Innovation · APO05 Portfolio · APO06 Budget and Costs · APO07 Human Resources · APO08 Relationships · APO09 Service Agreements · APO10 Vendors · APO11 Quality · APO12 Risk · APO13 Security · APO14 Data | Organisation, strategy, policy, risk and resource planning |
| **BAI** — Build, Acquire and Implement | Management | BAI01 Managed Programs · BAI02 Requirements Definition · BAI03 Solutions Identification and Build · BAI04 Availability and Capacity · BAI05 Organizational Change · BAI06 IT Changes · BAI07 IT Change Acceptance and Transitioning · BAI08 Knowledge · BAI09 Assets · BAI10 Configuration · BAI11 Projects | Definition, acquisition, implementation and integration of solutions |
| **DSS** — Deliver, Service and Support | Management | DSS01 Managed Operations · DSS02 Service Requests and Incidents · DSS03 Problems · DSS04 Continuity · DSS05 Security Services · DSS06 Business Process Controls | Operational delivery and support, including security operations |
| **MEA** — Monitor, Evaluate and Assess | Management | MEA01 Managed Performance and Conformance Monitoring · MEA02 System of Internal Control · MEA03 Compliance With External Requirements · MEA04 Assurance | Performance monitoring, internal control, external compliance, assurance |

Objectives use "Ensured" verbs for governance (EDM) and "Managed" verbs for management, replacing COBIT 5's "Ensure"/"Manage". Three objectives are new relative to COBIT 5's 37 processes: **APO14 Managed Data**, **BAI11 Managed Projects**, **MEA04 Managed Assurance**; APO10 changed from "supplier" to "vendor".

### The seven components

Every objective is supported by seven interacting component types: **Processes; Organizational Structures; Information; People, Skills and Competencies; Principles, Policies and Procedures; Culture, Ethics and Behavior; Services, Infrastructure and Applications.** COBIT 5's "enablers" were renamed components. Practically, each objective in *Governance and Management Objectives* ships with: a set of governance/management practices, each with activities and a target capability level per activity; example metrics at practice level; a responsibility/accountability matrix across organisational roles; information inputs and outputs; relevant policies; culture expectations; and related guidance pointers (for example SFIA for skills).

### Goals cascade and design factors

The goals cascade runs **stakeholder drivers and needs → 13 generic enterprise goals → 13 alignment goals → the 40 objectives**, and exists to prioritise, not to enumerate. It is embedded in the **11 design factors**, categorised as contextual (outside enterprise control), strategic (enterprise decisions) and tactical (implementation choices):

| Used to set | Design factors |
|---|---|
| Initial scope | Enterprise strategy · Enterprise goals · Risk profile · I&T-related issues |
| Refined scope | Threat landscape · Compliance requirements · Role of IT · Sourcing model for IT · IT implementation methods · Technology adoption strategy |
| Also a design factor | Enterprise size — ISACA's Design Guide names it in the refine-scope step, although the toolkit's refined-scope weighting chart lists only the six factors above |

For every factor except risk profile the weighting is by importance; for risk profile it is by risk rating. The *Design Guide* workflow has four stages — understand the context and strategy; determine the initial scope; refine the scope; resolve conflicts and conclude the design — and ISACA ships an Excel **Design Guide Tool Kit** that computes the weighted objective priorities. Output of the design phase: prioritised objectives, target capability levels per process, and any component flagged for special attention.

### Focus areas

Focus areas extend the core model for a specific topic, adding topic-specific practices, activities and metrics without creating a parallel framework. Published focus areas and topic guidance include **Information Security** (July 2020, the first focus area under the COBIT 2019 umbrella), **Information and Technology Risk**, **DevOps** (with a companion audit program), *COBIT 2019 for Small and Medium Enterprises*, and *Implementing the NIST Cybersecurity Framework Using COBIT 2019* (written against CSF v1.1).

## Assessment, certification and evidence

- **COBIT Performance Management (CPM)** replaces COBIT 5's ISO/IEC 33000-based scale. Capability and maturity levels run **0–5**, aligned to and extending CMMI Development V2.0. ISACA renders levels 1–5 with the CMMI V2.0 descriptors Initial, Managed, Defined, Quantitatively Managed, Optimizing.
- **Capability applies to processes; maturity applies to focus areas.** A focus area reaches a maturity level only when all the capability levels it requires have been achieved — so maturity claims are derived, never asserted directly.
- **Rating scale per activity/capability level:** Fully (achieved >85%), Largely (50–85%), Partially (15–50%), Not (<15%). Ratings must be traceable to validated evidence, direct (a document or outcome) or indirect (plans to produce an outcome), typically gathered by interview and confirmed against work products.
- **Assessment sequence in practice:** stakeholder awareness → design the tailored governance system and set target capability levels → brief process owners and prepare templates → collect and validate evidence → rate activities → report strengths, weaknesses and improvement opportunities. See [control-testing](../../skills/control-testing/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
- **Individual credentials.** COBIT Foundation: 75 multiple-choice questions, 2-hour remotely proctored exam, 65% to pass, US$175 for members and non-members; domains include governance system and components, objectives, principles, implementation, designing a tailored governance system, performance management and the business case. COBIT Design & Implementation: 60 multiple-choice questions, 3-hour exam, US$275. ISACA positions the Foundation certificate as preparation for the CGEIT certification exam.
- **No organisational certificate exists**, so COBIT evidence is used internally (board reporting, audit committee packs, IT audit universe design) or as a structuring layer beneath certifications granted elsewhere, e.g. ISO/IEC 27001.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 1996 | COBIT 1 released, harmonising 18 source standards; audience: IT auditors |
| 1998 / 2000 / 2005 | COBIT 2 (IT control guidance) / COBIT 3 (management framework) / COBIT 4 (IT governance framework) |
| 2012 | COBIT 5 — 5 principles, 37 processes, enablers, ISO/IEC 33000 capability scale |
| November 2018 | COBIT 2019 launched: *Framework: Introduction and Methodology* and *Framework: Governance and Management Objectives* |
| 11 December 2018 | *Design Guide* and *Implementation Guide* published, introducing the design-factor workflow |
| 2019 | COBIT 2019 training and certificate programmes released |
| July 2020 | *COBIT Focus Area: Information Security* — first focus area under COBIT 2019 |
| June 2021 | Joint Axelos/ISACA white paper mapping ITIL 4 practices to COBIT 2019 objectives |
| June 2024 | ISACA releases the *Cybersecurity Audit Program: Based on the NIST Cybersecurity Framework 2.0* — an audit program, not a COBIT implementation guide |
| January 2025 | ISACA white paper *Leveraging COBIT for Effective AI System Governance* |
| April 2026 | COBIT 30th anniversary; ISACA states a COBIT update is planned for later in 2026, largely digital, adding a flexible, customisable assessment module |
| 27 October 2026 | COBIT 7 Foundations Certificate replaces the COBIT 2019 Foundations Certificate (last day to buy the COBIT 2019 exam or prep: 26 October 2026) |
| 2027 / 26 April 2027 | COBIT 7 Design & Implementation Certificate replaces the COBIT 2019 version / both COBIT 2019 certificates sunset |

**Planning note:** as of 19 September 2026 no COBIT 7 framework publication appears in ISACA's COBIT resource hub, its 2026 press releases or its site index; the COBIT 7 *framework* publication schedule and its content changes have not been published in the detail the certificate transition has. Treat COBIT 2019 as the current citable edition, but do not commission a multi-year COBIT 2019 maturity roadmap in late 2026 without a re-baselining checkpoint. See [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Run the design-factor exercise before anything else.** Assessing all 40 objectives at a mid-sized company produces an unusable gap list. Use the Design Guide workflow and toolkit to fix a prioritised objective set and target capability levels, and keep the resulting design as the scoping evidence. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
2. **Use COBIT for decision rights, not control detail.** Where the finding is "nobody owns this", the fix lives in EDM01 and the organisational-structures component, not in another technical control.
3. **Map, don't migrate.** Keep the operating control set in ISO 27001, CSF or CIS and use COBIT's 40 objectives as the integrating layer above them. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
4. **Anchor ITGC scoping for SOX.** The objectives that line up with the standard ITGC domains are BAI06/BAI07 (IT changes, change acceptance and transitioning), BAI10 (configuration), DSS01 (operations), DSS05 (security services) and MEA02 (system of internal control), under APO01 and APO13. ISACA has published *IT Control Objectives for Sarbanes-Oxley* as ICFR-specific guidance, but no current edition of it could be found in ISACA's online catalogue in September 2026 (verify) — treat this objective list as a starting point, not an authoritative mapping. See [sox-itgc.md](../regulations/sox-itgc.md).
5. **Assess with the published rating scale and hold the line on evidence.** Fully/Largely/Partially/Not against traceable artefacts; refuse capability claims resting on interviews alone.
6. **Report maturity honestly.** Maturity belongs to focus areas and is earned only when all required capability levels are met; a "Level 3 organisation" claim built from a handful of Level 3 processes will not survive audit. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md) and [grc-board-report.md](../../templates/grc-board-report.md).
7. **Treat AI as a governance problem, not a new programme.** ISACA's 2025 white paper places AI in the Services, Infrastructure and Applications component and maps trustworthy-AI elements to existing objectives — EDM01 (accountability and ethics), EDM02 (benefits and societal impact), APO01 (ethical standards in the I&T framework), APO11 (quality and safety documentation), APO14 (data and privacy), BAI03 (training-data quality), BAI06 (model and algorithm changes), BAI09 and DSS05 (asset and security controls). See [ai-governance](../../skills/ai-governance/SKILL.md).
8. **Re-run the design when a design factor moves.** The dynamic-governance principle makes a strategy shift, a new regulation, a sourcing change or a threat-landscape change a trigger to revisit scope — not an annual-cycle item.
9. **Feed the IT audit universe.** The 40 objectives, with design-factor priorities and target capability levels, make a defensible risk-ranked audit universe; see the [internal auditor](../../agents/internal-auditor.md) perspective.

## Interplay

- **ISO/IEC 27001:2022** — complementary, not competing. ISO certifies an ISMS against Annex A controls; COBIT structures the enterprise decision rights, goals cascade and capability targets above them. Most organisations running both use ISO for certification and COBIT for governance reporting. See [iso-27001-2022.md](iso-27001-2022.md).
- **NIST CSF 2.0** — ISACA published *Implementing the NIST Cybersecurity Framework Using COBIT 2019* against **CSF v1.1**; CSF 2.0 (2024) added the Govern function, which overlaps COBIT's EDM domain directly. ISACA's CSF 2.0 output since June 2024 has been an audit program covering the six CSF 2.0 functions, not a COBIT implementation guide, and no COBIT-branded CSF 2.0 guide was located as of September 2026 — build the mapping yourself rather than citing a stale one. See [nist-csf-2.md](nist-csf-2.md).
- **NIST SP 800-53 / CIS Controls** — control catalogues that sit under COBIT objectives as the implementation layer; COBIT supplies no control text at that depth. See [nist-800-53.md](nist-800-53.md) and [cis-controls-v8.md](cis-controls-v8.md).
- **ITIL 4** — a free Axelos/ISACA white paper, *Using ITIL 4 and COBIT 2019 to Create an Integrated I&T Framework Environment* (June 2021), maps ITIL 4 practices to COBIT 2019 objectives and aligns ITIL's dimensions with COBIT's components. ISACA's position is that the two are complementary, not a choice: COBIT for governance, ITIL for service-management execution. Take the practice-level mapping from that paper rather than improvising one.
- **SOX / ICFR** — COBIT objectives supply the common vocabulary behind ITGC scoping; ISACA's older *IT Control Objectives for Sarbanes-Oxley* guidance is no longer listed in its online catalogue (verify before citing it). See [sox-itgc.md](../regulations/sox-itgc.md).
- **DORA, NIS2 and other governance-heavy regimes** — these impose management-body accountability, documented frameworks and evidence of oversight. COBIT's EDM and MEA objectives are a workable structure for demonstrating that, but COBIT is not a compliance mapping: none of these regimes recognises COBIT as a conformity route. See [dora.md](../regulations/dora.md) and [nis2.md](../regulations/nis2.md).
- **EU AI Act** — COBIT can carry AI accountability and lifecycle governance internally, but the Act's obligations are legal and specific; use the regulation's own requirements as the control set. See [eu-ai-act.md](../regulations/eu-ai-act.md).
- **COSO** — ISACA's mapping white paper *Relating the COSO Internal Control—Integrated Framework & COBIT* takes COSO ICIF as the base structure and relates **COBIT 5** content to it; there is no COBIT 2019 equivalent, so re-derive the mapping against the 40 objectives. See [coso-internal-control-erm.md](coso-internal-control-erm.md).
- **COBIT 5 artefacts** — still circulating in older audit programmes. COBIT 5 process IDs mostly map to COBIT 2019 objectives, but the capability scale changed (ISO/IEC 33000 → CMMI-based), so historical capability scores are not directly comparable to CPM results.

## Primary sources

- ISACA, COBIT resource hub — publication catalogue, focus areas, certification (publisher page): https://www.isaca.org/resources/cobit — fetched
- ISACA press release, *New COBIT 2019 Resources Help Organizations Design and Implement Tailored Governance Systems*, 11 December 2018 (publisher announcement; launch date, publications, Design Guide four steps): https://www.isaca.org/about-us/newsroom/press-releases/2018/new-cobit-2019-resources-help-organizations-design-and-implement-tailored-governance-systems — fetched
- ISACA, *Leveraging COBIT for Effective AI System Governance*, white paper, 2025 (publisher document; reproduces the COBIT core model, the seven components, the goals cascade and the 11 design factors): https://www.isaca.org/-/media/files/isacadp/project/isaca/resources/white-papers/leveraging_cobit_for_effective_ai_system_governance_and_management__0125.pdf — fetched
- ISACA, *COBIT 2019 and COBIT 5 Comparison*, 27 April 2020 (publisher article; principles, 37→40 processes, design factors, CMMI scale): https://www.isaca.org/resources/news-and-trends/industry-news/2020/cobit-2019-and-cobit-5-comparison — fetched
- ISACA, *Employing COBIT 2019 for Enterprise Governance Strategy*, 28 October 2019 (publisher article; five domains, 13 enterprise and 13 alignment goals): https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy — fetched
- ISACA, *Using COBIT 2019 Performance Management Model to Assess Governance and Management Objectives*, 16 September 2019 (publisher article; CPM assessment steps and the Fully/Largely/Partially/Not rating bands): https://www.isaca.org/resources/news-and-trends/industry-news/2019/using-cobit-2019-performance-management-model-to-assess-governance-and-management-objectives — fetched
- ISACA, *Effective Capability and Maturity Assessment Using COBIT 2019*, 27 July 2020 (publisher article; capability vs. maturity, CMMI level descriptors): https://www.isaca.org/resources/news-and-trends/industry-news/2020/effective-capability-and-maturity-assessment-using-cobit-2019 — fetched
- ISACA, *A Systematic Approach to Implementing a Governance System Using COBIT 2019*, 26 May 2021 (publisher article; component-by-component worked example): https://www.isaca.org/resources/news-and-trends/industry-news/2021/a-systematic-approach-to-implementing-a-governance-system-using-cobit-2019 — fetched
- ISACA, *COBIT Design Factors*, 4 February 2019 (publisher article; contextual/strategic/tactical categories, 11 design factors, toolkit): https://www.isaca.org/resources/news-and-trends/industry-news/2019/cobit-design-factors — fetched
- ISACA, *COBIT 2019 and the IIA 2019 Guiding Principles of Corporate Governance*, 13 July 2020 (publisher article; the six governance system principles in full): https://www.isaca.org/resources/news-and-trends/industry-news/2020/cobit-2019-and-the-iia-2019-guiding-principles-of-corporate-governance — fetched
- ISACA, *Celebrating Three Decades of COBIT*, @ISACA newsletter, 20 April 2026 (publisher article; version history and the 2026 update plan): https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2026/volume-8/celebrating-three-decades-of-cobit — fetched
- ISACA, COBIT Foundation Certificate and COBIT Design & Implementation Certificate pages (publisher pages; COBIT 7 transition dates, exam format, fees): https://www.isaca.org/credentialing/cobit-foundation and https://www.isaca.org/credentialing/cobit-design-and-implementation — both fetched
- ISACA press release, *New COBIT Resource from ISACA Offers Guidance for Governance and Management of Information Security*, 14 July 2020 (publisher announcement; first COBIT 2019 focus area): https://www.isaca.org/about-us/newsroom/press-releases/2020/new-cobit-resource-from-isaca-offers-guidance-for-governance-and-management-of-information-security — fetched
- ISACA, *New Resource Illustrates Synergies Between ITIL 4 and COBIT 2019*, 16 June 2021 (publisher article; Axelos/ISACA mapping white paper): https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2021/volume-17/new-resource-illustrates-synergies-between-itil-4-and-cobit-2019 — fetched. White paper landing page: https://www.isaca.org/resources/white-papers/using-itil-4-and-cobit-2019-to-create-an-integrated-i-and-t-framework-environment
- ISACA press release, *Audit and Assurance Guidance for the NIST Cybersecurity Framework 2.0 and Artificial Intelligence*, 6 June 2024 (publisher announcement; CSF 2.0 audit program scope and pricing): https://www.isaca.org/about-us/newsroom/press-releases/2024/audit-and-assurance-guidance-for-the-nist-cybersecurity-framework-2-0-and-artificial-intelligence — fetched
- ISACA, *Relating the COSO Internal Control—Integrated Framework & COBIT* (publisher white-paper page; abstract confirms the mapping is COBIT 5-based): https://www.isaca.org/resources/white-papers/relating-the-coso-internal-control-integrated-framework-and-cobit — fetched
- ISACA newsroom, press releases 2026 (publisher listing; checked through 10 September 2026 for any COBIT 7 framework announcement — none): https://www.isaca.org/about-us/newsroom/press-releases/2026 — fetched
- Access note: the COBIT 2019 framework text is distributed as ISACA publications rather than as an open web document. ISACA's 14 July 2020 announcement (above) states that *COBIT 2019 Framework: Introduction and Methodology* and *Framework: Governance and Management Objectives* are free downloads for ISACA members, while focus-area and other titles are priced. Figures reproduced in the sources above are cited to those two volumes (ISACA, 2018). Catalogue: https://www.isaca.org/resources/cobit

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
