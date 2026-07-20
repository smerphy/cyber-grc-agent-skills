# FISMA and the US Federal Compliance Stack

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | United States, federal government |
| Instrument | Statutes: FISMA 2002 (E-Government Act, Title III) as superseded/updated by the Federal Information Security Modernization Act of 2014 (44 U.S.C. § 3551 et seq.), plus the surrounding stack of OMB circulars/memoranda, NIST standards, and CISA directives |
| Effective | FISMA 2002 since 2002; FISMA 2014 since December 2014 |
| Regulator/overseers | OMB (policy and oversight), DHS/CISA (operational security for federal civilian agencies, binding directives), NIST (standards and guidelines), agency Inspectors General (annual independent evaluations), GAO and Congress (reporting) |
| Applies to | Federal agencies and the information systems they own **or that are operated on their behalf** — which is how contractors and cloud providers get pulled in |
| Penalties | No fines. Consequences are budgetary/oversight (OMB scorecards, IG findings, congressional scrutiny) for agencies; **lost or unwinnable contracts** for vendors that cannot meet the flowed-down requirements |

## The stack in one view

Federal information security is not one rule but a layered system. Reading order for a newcomer:

| Layer | Instrument | What it does |
|---|---|---|
| Statute | FISMA (44 U.S.C. § 3551 et seq.) | Requires every agency to run a risk-based, agency-wide information security program; assigns roles to OMB, DHS, NIST, IGs |
| Policy | OMB Circular A-130, OMB memoranda (M-series) | Translates the statute into binding management policy: authorization of systems, continuous monitoring, annual FISMA reporting metrics, incident/breach handling |
| Standards | FIPS 199, FIPS 200 | Mandatory standards: categorize systems (low/moderate/high impact) and set minimum security requirements |
| Guidelines | NIST SP 800-53, SP 800-37 (RMF), SP 800-60, and the wider 800-series | The control catalog and the process for selecting, implementing, assessing, and authorizing controls |
| Operations | CISA Binding Operational Directives (BODs) and Emergency Directives (EDs) | Compulsory actions for federal civilian executive branch (FCEB) agencies on specific threats and practices |
| Cloud | FedRAMP | Standardized authorization for cloud services used by agencies — see [../frameworks/fedramp.md](../frameworks/fedramp.md) |
| Contractors | FAR/DFARS clauses, SP 800-171, CMMC | Protection of federal information on **nonfederal** systems — see [../frameworks/nist-800-171-cmmc.md](../frameworks/nist-800-171-cmmc.md) |

## FISMA itself: what the statute requires

**Agency obligations.** Each agency head is accountable for information security commensurate with risk; in practice the CIO (and below them a senior agency information security officer — the agency CISO) runs a program that must include: periodic risk assessments; policies and procedures; security and awareness training; periodic testing and evaluation of controls (at least annually); a remediation process (**POA&M** — plan of action and milestones); incident detection, reporting, and response procedures; and continuity plans.

**FISMA 2014 changes** (vs. 2002): codified DHS's operational role for civilian agencies (the authority under which CISA issues BODs), moved reporting toward automated/continuous data feeds instead of paper checklists, and set breach-notification expectations to Congress and affected individuals via OMB policy.

**Annual reporting and IG evaluations.** Agencies report annually to OMB/DHS/Congress against CIO FISMA metrics; each agency's **Inspector General independently evaluates** the program every year using a maturity model (the IG FISMA metrics, historically organized around the NIST CSF functions — see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)). IG ratings and OMB scorecards are public accountability instruments; "effective/not effective" findings drive agency behavior more than any fine could.

**Authorization to Operate (ATO).** Under A-130 and the RMF, a federal system must be authorized by an agency official who formally accepts the residual risk before operation, and continuously monitored thereafter. For vendors, "getting an ATO" is the practical translation of "FISMA compliance."

## NIST's role

NIST writes the standards FISMA makes mandatory for federal systems:

- **FIPS 199** — categorize each system as low, moderate, or high impact for confidentiality, integrity, and availability (high-water mark governs). Categorization drives everything downstream, so fight the scoping battle here.
- **FIPS 200** — minimum security requirements; operationally, it points you into SP 800-53.
- **SP 800-53** — the control catalog (with 800-53B baselines by impact level and 800-53A assessment procedures). See [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md).
- **SP 800-37, the Risk Management Framework (RMF)** — the seven-step lifecycle: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. This is the process wrapper that produces the ATO.
- Supporting guides: SP 800-60 (mapping information types to impact levels), SP 800-137 (continuous monitoring), SP 800-61 (incident handling), and many others.

## OMB policy layer

- **Circular A-130** ("Managing Information as a Strategic Resource") is the umbrella policy: it mandates RMF use, system authorization, continuous monitoring, PIAs, and role assignments. When someone asks "where does it say agencies must do the RMF," the answer is A-130.
- **Annual FISMA guidance memoranda** — OMB issues yearly memos setting that cycle's reporting metrics and deadlines (identifiers change every year; look up the current one).
- **M-21-31** (2021) — event-logging maturity requirements for agencies (EL0-EL3 tiers), driving major log retention and centralization work. Verify tier details before citing.
- **M-22-09** (January 2022) — the **federal zero trust strategy**, requiring agencies to hit zero-trust architecture goals (phishing-resistant MFA, encrypted DNS/HTTP traffic, application-level access, and related pillars) originally targeted through FY2024, aligned to CISA's Zero Trust Maturity Model. Hedge on specific milestone status — targets and dates have been updated by later guidance; check the current OMB posture.
- Breach response policy (M-17-12 and successors) governs federal breach notification. Memo numbers get superseded — always confirm the operative memo.

## Executive Order 14028 and its aftermath

EO 14028, "Improving the Nation's Cybersecurity" (May 2021), is the hinge event of the modern stack. It drove: the zero-trust push (M-22-09), software supply chain security requirements (NIST Secure Software Development Framework SP 800-218, self-attestations for software sold to agencies — see the CISA secure software attestation process), SBOM momentum, EDR deployment across agencies, cyber incident reporting expectations for contractors via FAR updates, and the creation of the Cyber Safety Review Board. Follow-on executive orders and FAR rulemakings (including proposed FAR CUI and incident-reporting clauses) have continued to evolve — verify current status before relying on any specific FAR clause.

## CISA operational directives

CISA issues **Binding Operational Directives (BODs)** — compulsory for FCEB agencies (not for contractors directly, and not for national security systems) — and **Emergency Directives** for acute threats. Notable BODs (verify identifiers and current requirements against CISA's directives page):

- **BOD 22-01** — "Reducing the Significant Risk of Known Exploited Vulnerabilities": agencies must remediate vulnerabilities listed in CISA's **KEV catalog** within set timeframes. The KEV catalog has become a de facto prioritization standard far beyond government.
- **BOD 23-01** — asset visibility and vulnerability detection: regular automated asset discovery and vulnerability enumeration, with results fed to CISA (CDM program).
- **BOD 18-01** — email and web security (DMARC, HTTPS/HSTS); **BOD 19-02** — remediation timelines for internet-facing critical/high vulnerabilities; **BOD 23-02** — removing exposed management interfaces; **BOD 25-01** — secure configuration of cloud services (SCuBA baselines, beginning with Microsoft 365) — verify the exact scope.

Even outside government, BODs are a useful free signal: they tell you what CISA considers exploitable-now hygiene.

## What this means for contractors and vendors

FISMA does not directly regulate private companies, but its reach arrives through three doors:

1. **Systems operated on behalf of an agency:** if you run a system for the government (hosting, processing, or a mission application), that system sits inside FISMA scope — expect FIPS categorization, an 800-53 baseline, an ATO in the agency's name, continuous monitoring, and incident reporting to the agency and US-CERT/CISA per federal timelines (federal incident reporting runs on aggressive clocks — historically 1 hour to CISA for many incident types under the federal incident notification guidelines; verify current requirements).
2. **Cloud services:** agencies may only use cloud offerings with **FedRAMP** authorization; FedRAMP is essentially FISMA's RMF industrialized for multi-tenant cloud. See [../frameworks/fedramp.md](../frameworks/fedramp.md), including its statutory codification in the FY2023 NDAA (FedRAMP Authorization Act).
3. **Federal information on your own systems:** CUI on nonfederal systems triggers **SP 800-171** via DFARS (defense) and, progressively, FAR clauses (civilian), with **CMMC** as DoD's assessment regime. See [../frameworks/nist-800-171-cmmc.md](../frameworks/nist-800-171-cmmc.md). FAR 52.204-21's fifteen basic safeguarding requirements are the floor for any contractor handling federal contract information.

Rule of thumb: "FISMA compliance" in an RFP usually means "you will support our ATO with an 800-53 control implementation at the FIPS 199 level we specify" — price the assessment and documentation burden accordingly.

## FISMA reform

FISMA modernization bills have been introduced repeatedly (2021 through the mid-2020s) proposing codified CISA/OMB/national-cyber-director roles, shifting from compliance reporting toward risk-based metrics, and updating breach notification to Congress. As of this writing none is confirmed enacted — treat any claim that "FISMA was updated in 20XX" with suspicion and verify against the US Code. The practical modernization has instead arrived through OMB memoranda, EO 14028 follow-through, and CISA directives.

## Key obligations for security/GRC teams

1. If you sell to or operate for federal agencies: identify which door you enter through (system on behalf of agency, cloud service, or CUI on your systems) — the control regime, assessor, and artifact set differ for each.
2. Run FIPS 199 categorization deliberately; over-categorization is the single most expensive avoidable mistake in federal work.
3. Build and maintain the RMF artifact set (SSP, control implementation statements, assessment results, POA&M, continuous monitoring plan) as living documents — ATOs are increasingly conditioned on ongoing evidence, not snapshots.
4. Track CISA KEV remediation timelines as an internal SLA even if BODs do not bind you; agencies will push them into contracts.
5. Watch the FAR/DFARS clause churn (incident reporting, SBOM/attestation, CUI) each contracting cycle; flow requirements down to your own subcontractors.
6. For incident response, know the federal reporting chain (agency + CISA) and clocks in advance; they are faster than commercial regimes — see [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Interplay

- [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md) — the control catalog underneath everything here; [../frameworks/fedramp.md](../frameworks/fedramp.md) — the cloud pathway; [../frameworks/nist-800-171-cmmc.md](../frameworks/nist-800-171-cmmc.md) — the contractor/CUI pathway.
- [circia.md](circia.md) — critical infrastructure incident reporting sits beside (not inside) the federal stack; a contractor can owe both federal incident reports and CIRCIA reports.
- [sec-cyber-disclosure.md](sec-cyber-disclosure.md) — publicly traded federal contractors run SEC materiality analysis in parallel with agency reporting.
- [sox-itgc.md](sox-itgc.md) — 800-53's control families overlap heavily with ITGC domains; reuse evidence where you can.
- [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) — mappings from 800-53 to ISO 27001, CSF, and SOC 2.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
