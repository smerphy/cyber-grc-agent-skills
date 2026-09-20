# NIST CSF 2.0 companion resources — Quick-Start Guides, Organizational and Community Profiles, Informative References

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | US National Institute of Standards and Technology (NIST), Applied Cybersecurity Division / NCCoE |
| Anchor document | The CSF 2.0 framework itself (NIST CSWP 29, 26 February 2024) — see [nist-csf-2.md](nist-csf-2.md). This pack covers everything *around* it |
| Quick-Start Guide series | SP 1299, 1300, 1301, 1302, 1303, 1305, 1308, 1347 final; SP 1353 in initial public draft; CSWP 32 (Community Profiles) still an initial public draft |
| Profile types | **Organizational Profile** (one organization's Current/Target state, SP 1301) and **Community Profile** (a published baseline for a sector, technology or threat, CSWP 32 ipd) |
| Mapping layer | Informative References, reached through CPRT, the CSF 2.0 Reference Tool, or the OLIR catalog (IR 8278 Rev. 1, Feb 2024; submission conformance per IR 8278A Rev. 1) |
| ERM bridge | NIST IR 8286 series — 8286 Rev. 1 and 8286A Rev. 1 (Dec 2025), 8286B-upd1 and 8286D-upd1 (Feb 2025), 8286C Rev. 1 (Dec 2025) |
| Certifiable? | No. Every item here is free, voluntary guidance; none creates a certification, audit opinion or conformity assessment |
| Cost / licensing | Free; NIST publications are US Government works. CSF 2.0 is published in 12 languages (Arabic, French, German, Greek, Japanese, Korean, Mandarin, Norwegian, Polish, Portuguese, Spanish, Thai) |
| Status as of Sept 2026 | Active portfolio; SP 1347 finalised August 2026, SP 1353 (AI-assisted CSF analysis) open for comment to 15 October 2026 |

## What it is

CSF 2.0 itself is deliberately thin: a Core of Function/Category/Subcategory outcome statements, with no method, no scoring scale and no control text. Everything that makes the framework usable — how to build a Profile, how to pick a Tier, how to reach the control mappings, how to hand cyber risk to an enterprise risk function — lives in a separate and steadily growing body of NIST companion material. Practitioners who read only the framework document conclude CSF is vague; the companion resources are where the method actually is.

The portfolio has three strands. **Quick-Start Guides (QSGs)** are short, audience-specific how-tos numbered in the NIST SP 1299–1353 range. **Profiles** are the framework's tailoring mechanism: Organizational Profiles for a single organization, Community Profiles as published sector/technology baselines that an organization can adopt as a starting Target Profile. **Informative References** are machine-readable mappings from CSF outcomes to other standards, deliberately kept outside the framework document so they can be revised without republishing CSF.

NIST also uses the CSF as an authoring format for substantive guidance: SP 800-61 Rev. 3 (April 2025), which supersedes the 2012 Rev. 2, is titled and structured as a CSF 2.0 Community Profile for incident response rather than as a conventional handbook. Expect more NIST guidance to arrive in this shape.

## Who it covers / Scope

| Resource | Intended audience | Practical use |
|---|---|---|
| SP 1299 — Resource and Overview Guide (Feb 2024) | Anyone new to CSF 2.0 | Map of the resource set; hand to stakeholders before a kick-off |
| SP 1300 — Small Business QSG (Feb 2024) | SMBs, non-profits, schools, small government bodies with modest or no cybersecurity plan | Explicitly a supplement to, not a replacement for, the CSF |
| SP 1301 — Organizational Profiles QSG (26 Feb 2024) | Program owners running a current-vs-target assessment | The five-step Profile method plus the template's column semantics |
| SP 1302 — Using the CSF Tiers QSG (Oct 2024) | Assessors applying Tiers | Applies Tiers *to Profiles* to characterise governance/management rigour |
| SP 1303 — Enterprise Risk Management QSG (Oct 2024) | ERM practitioners | Using CSF outcomes inside an existing ERM process |
| SP 1305 — C-SCRM QSG (Oct 2024) | Procurement, vendor risk, supplier-side teams | Being a smarter acquirer *and* supplier of technology |
| SP 1308 — Cybersecurity, ERM and Workforce Management QSG (Mar 2026) | HR, workforce planning, CISO staffing | Joins the NICE Workforce Framework to CSF outcomes |
| SP 1347 — Informative References QSG (Aug 2026) | Control mappers, GRC tooling owners | How to find, filter and apply references; two worked use cases |
| SP 1353 ipd — AI for CSF Analysis and Reporting (19 Aug 2026) | Early adopters | Draft only; comments close 15 October 2026 — do not cite as settled guidance |
| CSWP 32 ipd — Guide to Creating Community Profiles (26 Feb 2024) | Sector bodies, ISACs, consortia | Still an initial public draft more than two years after issue |

## Structure and requirements

### Organizational Profiles (SP 1301)

Five steps: **1 Scope the Profile** → **2 Gather needed information** → **3 Create the Profile** → **4 Analyze gaps and create an action plan** → **5 Implement the action plan and update the Profile**.

- **Scope is a design decision, not a formality.** SP 1301 expects an organization to run *several* Profiles with distinct scopes — by technology category (IT, OT), data type (PII, PHI, PCI), or user population (employees, third parties) — because scope determines whether a given CSF outcome applies at all. Scoping questions include which divisions, data and technology assets, products, services and suppliers are in, which threat types are in, and who is accountable for developing, reviewing and operationalising the Profile.
- **Template column semantics** (the NIST Organizational Profile template is an XLSX on the CSF 2.0 Profiles page): the CSF outcome (Identifier, Description, extensible with your own outcomes); Current Profile columns for **Practices** (policies, processes, procedures and evidence artifacts), **Status** (whether the outcome is achieved and to what degree) and **Rating** (an evaluation of current practice on a scale you choose — high/medium/low, 1–5, 0–100%, RAG); Target Profile columns for **Goals** and **Priority** (relative importance, again on a scale you choose).
- **NIST prescribes no scale.** Both Rating and Priority are explicitly "scales such as…" — the scale is yours to define and anchor, which is exactly where cross-year and cross-assessor comparability is won or lost. See [risk-scoring.md](../risk-scoring.md).
- **Prioritisation is the defining feature of a Target Profile** — SP 1301 frames priorities as driven by strategic objectives, laws, regulations and risk responses, and points at SP 800-37 Rev. 2 (Prepare step) and IR 8286B for the underlying method.
- Step 5 wires the Profile into operations: action plans fulfilled through management, programmatic and technical controls; implementation tracked in the Profile; KPIs and KRIs for monitoring; POA&Ms for long-remediation gaps; risk assessments per SP 800-30 Rev. 1 for risks beyond tolerance.

### Community Profiles (CSWP 32 ipd)

A Community Profile is a published baseline of CSF outcomes addressing shared interests across many organizations — a sector, subsector, technology or threat type. Per CSWP 32, one **should** contain, per included Subcategory: a **priority level** (e.g. 1/2/3 or Low/Moderate/High), a **rationale** explaining the community-specific threat or challenge that justifies the priority, and applicable **Informative References/Mappings**. It **may** add *Considerations* and *Implementation Examples*. There is no mandated format.

Lifecycle: **Plan** (audience, scope, participants, references, content) → **Develop** (prioritize, align to CSF outcomes, document, gather feedback, inform the community) → **Use** (collaborate/coordinate, assess current state) → **Maintain** (measure impact, monitor and feed back changes).

An organization consumes a Community Profile by copying it into an Organizational Profile as the basis of its Target Profile, then adapting — adjusting priorities, adding organization-specific Subcategories, references or implementation guidance.

### Published Community Profiles (NIST CSF 2.0 Profiles page, updated 17 September 2026)

| Profile | Identifier / publisher | Status |
|---|---|---|
| Incident Response | NIST SP 800-61 Rev. 3 | Final, April 2025 (supersedes SP 800-61 Rev. 2, 2012) |
| Ransomware Risk Management | NIST IR 8374 Rev. 1 | Final, June 2026 — CSF 2.0 rewrite superseding IR 8374 (Feb 2022, CSF 1.1) |
| Manufacturing | NIST IR 8183 Rev. 2 | Initial public draft, 29 Sept 2025 (comments closed 17 Nov 2025); Rev. 1 (Oct 2020) is CSF 1.1-based |
| Genomic Data | NIST IR 8467 | Second public draft, 16 Dec 2024 (comments closed 30 Jan 2025) |
| Federal agency O-RAN deployment | NIST IR 8623 | Initial public draft, 17 Sept 2026; comments due 2 Nov 2026 |
| Cyber AI; Transit; Foundational PNT; Semiconductor manufacturing | NIST / NCCoE projects | Listed on the NIST Profiles page; check the project page for current draft state |
| Financial Sector CSF Profile; Financial Sector Cloud Services Profile | Cyber Risk Institute (CRI) | CRI Profile v2.2 — CSF 2.0-aligned, 318 diagnostic statements, ~40 regulatory/standards mappings, impact tiers (Tier 1–Tier 4) set by a nine-question impact assessment |
| Cloud Security | Cloud Security Alliance, based on CCM v4 | Third-party published |
| Internet Routing | CableLabs | Third-party published |
| Telecommunications Sector, v1.0 and v2.0 | Seemless Transition / Trusted Cyber Annex | Third-party published, sold commercially |

No US healthcare/public-health (HPH) Community Profile is listed on the NIST page as of September 2026 (verify separately whether HHS 405(d) HICP or the HPH performance goals are being restated as a CSF Community Profile).

### Informative References, CPRT and OLIR

SP 1347 names three access routes, in increasing order of granularity: **CPRT** (the Cybersecurity and Privacy Reference Tool — browse, search and export NIST reference data as XLSX/JSON rather than PDF), the **CSF 2.0 Reference Tool** (filter the CSF Core and attach selected references), and the **OLIR** Informative Reference Catalog (individual reference documents, Derived Relationship Mappings, and a cross-reference comparison report between two references).

References published against CSF 2.0 include ISO/IEC 27001:2022, PCI DSS 4.0.1, CIS Controls 8.1, NIST SP 800-53 Rev. 5, SP 800-171 Rev. 3, SP 800-81r3, NICE Framework v2.0.0, OWASP LLM Top 10 v2.0, CRI Profile v2.0, CSA Cloud Controls Matrix v4.0, the Secure Controls Framework, the UK Cyber Governance Code of Practice, and a growing set of vendor submissions.

**Governance caveats, stated by NIST and worth quoting to stakeholders:** references are produced by NIST *and non-NIST* entities; NIST performs only limited conformance testing against IR 8278A Rev. 1; NIST performs **no correctness testing** on non-NIST submissions; a catalog listing does **not** imply NIST endorsement; each submission runs a 30-day public comment period before being published as final. Section 2.3.1 of IR 8278 Rev. 1 covers unilateral mappings and NIST's role.

SP 1347 also addresses tool-assisted mapping directly: exports are structured, so automated analysis is possible, but automated mappings must be evaluated continuously and outputs must retain identifiers, source context, provenance and review status so unsupported mappings are not consumed without review. Treat that as the standard of care for any automated crosswalk. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

### ERM integration (IR 8286 series)

The IR 8286 series is the bridge between CSF outcomes and an enterprise risk register, and it was substantially refreshed in 2025: IR 8286 Rev. 1 (Dec 2025, superseding the Oct 2020 original), IR 8286A Rev. 1 (Dec 2025, risk identification and analysis), IR 8286B-upd1 (Feb 2025, prioritisation and risk response selection), IR 8286C Rev. 1 (Dec 2025, cybersecurity risk registers rolled up into the enterprise risk portfolio), IR 8286D-upd1 (Feb 2025, business impact analysis informing prioritisation). SP 1303 is the two-page entry point. See [risk-assessment](../../skills/risk-assessment/SKILL.md) and [risk-register-guide.md](../../templates/risk-register-guide.md).

## Assessment, certification and evidence

- **Nothing here is certifiable or auditable in its own right.** A Profile is a self-assessment artifact; a Community Profile is a published baseline; an Informative Reference is a mapping. "Aligned to the NIST CSF" remains a self-attestation — see [nist-csf-2.md](nist-csf-2.md).
- **What auditors and customers will accept as evidence:** a scoped Profile with a dated Current assessment, named evidence artifacts in the Practices column, a Target with rationales and priorities, and a tracked action plan. A spreadsheet of RAG dots with no Practices column is not evidence.
- **Draft status matters for defensibility.** CSWP 32 and SP 1353 are initial public drafts; IR 8183 Rev. 2 and IR 8467 are drafts. Citing a draft as a control requirement in a policy or contract invites a finding. Cite the final where one exists.
- **Version pinning.** Informative References carry their own version strings (e.g. CIS Controls 8.1, PCI DSS 4.0.1). Record the reference identifier and its version in any crosswalk deliverable; the catalog changes under you.
- **Community Profile adoption is not conformance.** Adopting a sector Community Profile as a Target does not make the organization "compliant" with it — there is no attestation mechanism behind it.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| Feb 2024 | CSF 2.0 published; SP 1299, SP 1300, SP 1301 and CSWP 32 ipd issued the same day; IR 8278 Rev. 1 published |
| Feb–May 2024 | CSWP 32 ipd public comment period (closed 3 May 2024); no final issued since |
| Oct 2024 | SP 1302 (Tiers), SP 1303 (ERM), SP 1305 (C-SCRM) finalised |
| Apr 2025 | SP 800-61 Rev. 3 published as a CSF 2.0 Community Profile for incident response |
| Feb / Dec 2025 | IR 8286B-upd1 and 8286D-upd1 (Feb); IR 8286 Rev. 1, 8286A Rev. 1, 8286C Rev. 1 (Dec) |
| Sept 2025 | IR 8183 Rev. 2 (CSF 2.0 Manufacturing Profile) initial public draft |
| Feb 2026 | Two-year anniversary of CSF 2.0 |
| Mar 2026 | SP 1308 (Cybersecurity, ERM and Workforce Management) finalised |
| Aug 2026 | SP 1347 (Informative References QSG) finalised; SP 1353 ipd released 19 August |
| Sept–Nov 2026 | IR 8623 (O-RAN) draft open 17 Sept–2 Nov; SP 1353 comments close 15 Oct |

## Key obligations for security/GRC teams

1. **Decide your Profile portfolio before assessing.** One enterprise-wide Profile is rarely right; scope separate Profiles by IT/OT, data type or user population as SP 1301 expects, and record each scope in writing. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
2. **Adopt a Community Profile as the Target where one exists for your sector** (ransomware, incident response, manufacturing, financial services) rather than authoring priorities from scratch — then document every deviation and its rationale.
3. **Define and publish your Rating and Priority scales.** NIST supplies none; an undefined scale makes year-over-year trending and board reporting meaningless. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
4. **Pull mappings from CPRT/OLIR rather than hand-building them**, record the reference name and version, and re-pull on a schedule. Never present a mapping as equivalence — coverage analysis only. See [control-mapping](../../skills/control-mapping/SKILL.md).
5. **Apply SP 1347's provenance rule to every automated crosswalk**: identifiers, source context, provenance and review status retained, with human review before use.
6. **Wire CSF outputs into ERM using the refreshed IR 8286 series** — cybersecurity risk registers rolling into the enterprise risk portfolio (8286C Rev. 1), BIA-informed prioritisation (8286D-upd1).
7. **Use SP 1300 for small vendors and small business units.** A full-Core assessment against a 40-person supplier produces noise; the Small Business QSG is the proportionate ask. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
8. **Track the draft pipeline quarterly** — CSWP 32, SP 1353, IR 8183 Rev. 2, IR 8467, IR 8623. See [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).
9. **Assess Tiers separately from outcomes** using SP 1302; Tiers characterise governance and management rigour applied to a Profile, not per-Subcategory achievement.

## Interplay

- **CSF 2.0 core** — this pack is the companion layer; Functions, Categories, Tiers and the 1.1→2.0 changes are in [nist-csf-2.md](nist-csf-2.md).
- **Control frameworks reached through Informative References** — [ISO/IEC 27001:2022](iso-27001-2022.md), [NIST SP 800-53](nist-800-53.md), [CIS Controls v8/v8.1](cis-controls-v8.md), [PCI DSS 4.x](pci-dss-4.md), the CSA Cloud Controls Matrix, NIST SP 800-171. CSF is the practical hub taxonomy: map once to CSF, reach the rest.
- **Incident response** — SP 800-61 Rev. 3 is simultaneously the IR handbook and a CSF Community Profile; it is the successor to the long-standing NIST incident-handling guide. It informs, but does not satisfy, regulatory notification clocks ([breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md)).
- **Supply chain** — SP 1305 is the two-page entry point above NIST SP 800-161 Rev. 1, the detailed C-SCRM guidance.
- **AI** — SP 1353 (draft) covers using AI *to run* CSF analysis; governing AI systems themselves belongs to the NIST AI RMF and ISO/IEC 42001. The NIST Cyber AI Profile is listed as a Community Profile in development.
- **Financial services** — the CRI Profile is the sector's CSF-derived assessment vehicle and maps to regulatory expectations including EU requirements; see [dora.md](../regulations/dora.md).
- **Risk quantification** — the IR 8286 series is a register-and-roll-up model, not a quantification method; pair it with a quantification method such as FAIR where monetary figures are required.

## Primary sources

- NIST Cybersecurity Framework resource centre — https://www.nist.gov/cyberframework — publisher page
- CSF 2.0 Quick-Start Guides index — https://www.nist.gov/cyberframework/quick-start-guides — publisher page
- CSF 2.0 Profiles, incl. the Community Profile catalogue — https://www.nist.gov/cyberframework/profiles — publisher page
- CSF 2.0 Informative References — https://www.nist.gov/cyberframework/informative-references — publisher page
- CSF 2.0 translations — https://www.nist.gov/cyberframework/translations — publisher page
- NIST SP 1301, Organizational Profiles QSG — https://doi.org/10.6028/NIST.SP.1301 — publisher document
- NIST SP 1347, Informative References QSG — https://doi.org/10.6028/NIST.SP.1347 — publisher document
- NIST CSWP 32 ipd, A Guide to Creating Community Profiles — https://doi.org/10.6028/NIST.CSWP.32.ipd — publisher document (initial public draft)
- CSRC publication records for SP 1299/1300/1301/1302/1303/1305/1308/1347/1353, IR 8183 Rev. 2, IR 8278 Rev. 1, IR 8286 and 8286A–D, IR 8374 and Rev. 1, IR 8467, IR 8623, SP 800-61 Rev. 3 — https://csrc.nist.gov/pubs/ — publisher publication records
- NIST OLIR program — https://csrc.nist.gov/projects/olir — publisher page
- NIST CPRT — https://csrc.nist.gov/Projects/cprt — publisher page
- Cyber Risk Institute, CRI Profile — https://cyberriskinstitute.org/the-profile/ and /cri-profile-overview/ — publisher pages
- NCCoE Community Profile project pages (Cyber AI, Transit, PNT, Semiconductor, Ransomware) — https://www.nccoe.nist.gov/ — **could not be fetched** (access blocked); status above is taken from the NIST Profiles page instead

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
