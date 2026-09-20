# MITRE ATT&CK, D3FEND and Threat-Informed Defence (ATT&CK v19.2 / D3FEND 1.6.0 / ATLAS 2026.09)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | The MITRE Corporation. ATT&CK, D3FEND, ATLAS and CAPEC are separate MITRE knowledge bases; the MITRE Center for Threat-Informed Defense (CTID) is a separate non-profit R&D consortium operated by MITRE that builds on ATT&CK |
| Current versions | ATT&CK **v19** (released 28 April 2026), patched to **v19.2** (6 August 2026); D3FEND ontology **1.6.0** (31 August 2026); ATLAS **2026.09** (data modified 15 September 2026); CAPEC **3.9** |
| Release cadence | ATT&CK is updated twice per year (spring/autumn). v19.2 was ATT&CK's **first "Agile release"** — a narrower off-cycle model that publishes targeted updates to Groups, Software and Campaigns between scheduled releases; v19.2 itself updated Enterprise Groups and Software |
| What ATT&CK is | Descriptive catalogue of observed adversary behaviour: tactics (the "why"), techniques/sub-techniques (the "how"), plus Groups, Software, Campaigns, Mitigations, Detection Strategies, Analytics and Data Components |
| What D3FEND is | A semantically rigorous **knowledge graph of countermeasures** (7 defensive tactics), funded by the NSA Cybersecurity Directorate and managed by MITRE; inferentially links defensive techniques to offensive techniques via digital artifacts |
| Certifiable? | **No.** None of these are certifiable or auditable standards. They are taxonomies and knowledge bases, published under royalty-free licences subject to each project's terms of use |
| Assessment model | Self-assessment of coverage (Navigator heatmaps, detection-coverage scoring, adversary emulation, purple teaming); CTID publishes INFORM, a program-level threat-informed-maturity self-assessment |
| GRC role | Supplies the **threat half** of risk statements and the validation half of control testing. Control frameworks say what to build; ATT&CK says what it must withstand and whether it demonstrably does |
| Regulatory hooks | Not named anywhere in the DORA level-1 text, but the TTP vocabulary underpins intelligence-led red teaming: DORA Art. 26 TLPT, ECB TIBER-EU, Bank of England CBEST |

## What it is

**ATT&CK** is an empirically grounded catalogue of how real intrusions actually proceed, organised as a matrix of tactics (adversary goals) crossed with techniques and sub-techniques (the means). It is descriptive, not prescriptive: it contains no control requirements, maturity levels or scores. Its value in GRC is that it is the common vocabulary linking threat intelligence, detection engineering, red teaming and control assessment, so that "we have EDR" can be replaced by "we detect these 40 techniques, at this quality, and here is the evidence".

**D3FEND** is the complementary countermeasure side. Rather than a control list, it is an ontology: defensive techniques are typed, defined against the cybersecurity literature (its source material included a targeted sample of over 500 US countermeasure patents from 2001–2018), and related to offensive techniques through the **digital artifacts** they operate on. That artifact-mediated linkage is why D3FEND supports inference ("this countermeasure works against that technique, and here is the engineering reason") rather than opinion-based mapping.

Around these sit **ATLAS** (adversary behaviours against AI-enabled systems), **CAPEC** (attack patterns tied to CWE weaknesses, with Explore/Experiment/Exploit execution flows), and the **Center for Threat-Informed Defense**, which publishes the control-to-ATT&CK mappings most GRC teams actually consume.

## Who it covers / Scope

| Knowledge base | Domains covered | Use it when |
|---|---|---|
| ATT&CK Enterprise | Enterprise IT, cloud and container estates | Default matrix for GRC control-coverage and scenario work |
| ATT&CK Mobile | Mobile platforms | BYOD and mobile-fleet risk scenarios |
| ATT&CK ICS | Operational technology; includes 18 ICS **Assets** | OT/plant risk assessment — pair with [IEC 62443](iec-62443-ot-security.md) |
| MITRE ATLAS | AI/ML-enabled systems; 73 published case studies | AI system threat modelling — pair with [NIST AI RMF](nist-ai-rmf.md) and [ISO/IEC 42001](iso-42001-ai-management.md) |
| MITRE D3FEND | Countermeasures mapped across ATT&CK Enterprise/Mobile/ICS, ATLAS and SPARTA (space) | Countermeasure design, control-rationale documentation |
| CAPEC | 559 attack patterns, weakness-centric | Application and product security; secure-design reviews |

Nothing here has an "in scope entity" test — adoption is voluntary. The practical scoping question is *which matrix and which subset*: a full Enterprise matrix is too large to assess against meaningfully, so scope by threat relevance (groups and campaigns credibly targeting your sector, geography and technology stack) before any coverage exercise.

## Structure and requirements

### ATT&CK v19 object model and counts

| Domain | Tactics | Techniques | Sub-techniques | Mitigations | Detection Strategies | Analytics | Data Components |
|---|---|---|---|---|---|---|---|
| Enterprise | 15 | 222 | 475 | 44 | 697 | 1,758 | 106 |
| Mobile | 12 | 77 | 47 | 13 | 124 | 211 | 29 |
| ICS | 12 | 79 | 18 | 52 | 97 | 96 | 36 |

Across all domains v19.0 carried 178 Groups, 949 pieces of Software and 59 Campaigns; after the v19.2 agile release the published totals stand at 180 Groups, 953 Software and 59 Campaigns.

### Enterprise tactics (v19)

`TA0043` Reconnaissance · `TA0042` Resource Development · `TA0001` Initial Access · `TA0002` Execution · `TA0003` Persistence · `TA0004` Privilege Escalation · `TA0005` **Stealth** · `TA0112` **Defense Impairment** · `TA0006` Credential Access · `TA0007` Discovery · `TA0008` Lateral Movement · `TA0009` Collection · `TA0011` Command and Control · `TA0010` Exfiltration · `TA0040` Impact

Two structural changes matter for anyone holding stored mappings or heatmaps:

- **v19 (April 2026)** split the former Defense Evasion tactic into **Stealth** (TA0005, hiding and blending in) and **Defense Impairment** (TA0112, breaking security mechanisms, pipelines and tooling), taking Enterprise from 14 to 15 tactics; it also added sub-techniques to ICS for the first time and began Detection Strategies in Mobile.
- **v18 (October 2025)** replaced per-technique "Detections" with first-class **Detection Strategies** and **Analytics**, overhauled Data Components and **deprecated Data Sources**.

Any control-to-ATT&CK mapping produced before October 2025 therefore references object types that no longer exist. Treat the ATT&CK version as a controlled attribute of every mapping artefact.

### D3FEND tactics (7)

**Model · Harden · Detect · Isolate · Deceive · Evict · Restore.** D3FEND publishes its own mappings — ATT&CK Mitigations to D3FEND techniques, NIST SP 800-53 Rev. 5 to D3FEND techniques, and DISA CCI to D3FEND techniques — plus a CSV of all techniques and definitions, a public API, and the D3FEND CAD graph tool. Ontology 1.5.0 (31 July 2026) aligned D3FEND to ATT&CK v19.0 and ATLAS v2026.06.

### ATLAS

16 tactics, 120 techniques with 88 sub-techniques, 40 mitigations and 73 case studies as of release 2026.09. Tactics reuse ATT&CK Enterprise semantics where they align (ATLAS Reconnaissance cross-references `TA0043`) and add AI-specific stages such as AI Attack Staging.

### The mapping layer (CTID Mappings Explorer)

| Mapped framework / platform | Notes |
|---|---|
| NIST SP 800-53 | Rev. 5 and Rev. 4, Enterprise domain; published against ATT&CK versions 16.1, 14.1, 12.1, 10.1, 9.0 and 8.2 |
| CSA Cloud Controls Matrix | Published against ATT&CK v17.1 |
| AWS, Azure, GCP, M365, Intel vPro | Native security-capability mappings; the ATT&CK version differs by platform (GCP 19.1; AWS, Azure and M365 16.1; Intel vPro 15.1) |
| CRI Profile, VERIS, CISA KEV | Financial-sector profile (ATT&CK 16.1), incident taxonomy (19.1), known-exploited-vulnerability linkage (16.1) |

Artefacts download as JSON, YAML, CSV, Excel, STIX bundles and Navigator layers. Note the lag: the newest published NIST 800-53 mapping targets ATT&CK 16.1 while ATT&CK is at v19 — CTID's **ATT&CK Sync** project exists precisely to manage that drift.

## Assessment, certification and evidence

- **Tools:** ATT&CK Navigator (annotating and colouring matrices — the source of "heatmaps"), ATT&CK Workbench (local extensions of the knowledge base), Python utilities, and STIX 2.0/2.1 data feeds. D3FEND adds CAD, technique extractors and an API.
- **Coverage heatmaps are the most abused artefact in this space.** A green cell asserts that a detection or control exists, not that it works, is tuned, or is monitored. Require an evidence reference per claimed technique (rule ID, test result, log sample) before a heatmap goes near a board pack or a regulator.
- **Detection quality, not count.** CTID's *Summiting the Pyramid* (latest release September 2026) exists to measure the robustness of detections — whether they key on ephemeral indicators or on invariant adversary behaviour. *Ambiguous Techniques* (February 2026) addresses techniques whose benign and malicious use are hard to separate.
- **Attack Flow** (latest release July 2026) captures sequences of techniques rather than isolated cells, which is what makes an ATT&CK-derived risk scenario narratable to executives.
- **INFORM** (January 2026) is a publicly available program-level self-assessment of how threat-informed a security programme is, usable as a maturity input alongside control assessments.
- **Purple teaming and adversary emulation** produce the strongest evidence: an executed technique with a recorded detection or prevention outcome is a test result, not an assertion. Feed those into [control-testing](../../skills/control-testing/SKILL.md) workpapers.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 20 Dec 2024 | D3FEND ontology 1.0.0 released (first stable release) |
| 28 Oct 2025 | ATT&CK **v18** — Detection Strategies and Analytics introduced; Data Sources deprecated |
| 16 Dec 2025 / 31 Mar 2026 | D3FEND 1.3.0 / 1.4.0 |
| Jan–May 2026 | CTID releases: cloud mappings and INFORM (January), Ambiguous Techniques (February), Fight Financial Fraud (April), Secure AI with ATLAS (May) |
| 28 Apr 2026 | ATT&CK **v19** — Defense Evasion split into Stealth and Defense Impairment; ICS sub-techniques added |
| 31 Jul 2026 | D3FEND 1.5.0 — aligned to ATT&CK v19.0 and ATLAS v2026.06 |
| 6 Aug 2026 | ATT&CK **v19.2**, the first Agile release (Enterprise Groups and Software) |
| 31 Aug 2026 | D3FEND ontology 1.6.0 (SPARTA v4.0 update, space-domain refinements) |
| 15 Sep 2026 | ATLAS data release 2026.09 |

ATT&CK's stated twice-yearly cadence implies a further scheduled release in the autumn 2026 window; none had been published as of 19 September 2026. Further off-cycle Agile releases should also be expected — plan mapping refresh cycles accordingly.

## Key obligations for security/GRC teams

1. **Version-pin every mapping.** Record the ATT&CK version (and domain) on every heatmap, SoA rationale and control-mapping artefact. The v18 and v19 structural changes silently invalidate older tagging.
2. **Scope by threat relevance first.** Select the groups, campaigns and techniques credible for your sector and stack before assessing coverage; a whole-matrix assessment yields noise. See [risk-assessment](../../skills/risk-assessment/SKILL.md) and its [scenario library](../../skills/risk-assessment/references/scenario-library.md).
3. **Write risk scenarios in TTP terms.** "Initial access via valid cloud accounts, leading to exfiltration over a C2 channel" is testable and traceable; "cyber attack" is not. Score consistently using [risk-scoring](../risk-scoring.md).
4. **Use published mappings for coverage analysis, never for equivalence.** A technique mapped to an 800-53 control does not mean the control defeats the technique; CTID scores each mapping's control effectiveness as Minimal, Partial or Significant for exactly this reason. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
5. **Convert heatmaps into gap findings with owners and dates,** not standalone artwork — route them through [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
6. **Pair each significant gap with a D3FEND countermeasure** so the remediation proposal states the engineering mechanism, not just a product category.
7. **Use ATT&CK/ATLAS to shape testing obligations,** including DORA Art. 26 TLPT scoping, TIBER-EU and CBEST engagements, and vendor penetration-test scopes — see [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
8. **Report technique coverage with an evidence column** and trend it over time; raw percentage coverage is a vanity metric. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
9. **Extend to AI systems via ATLAS** when scoping AI risk assessments and model-deployment reviews — see [ai-governance](../../skills/ai-governance/SKILL.md).
10. **Track releases as a horizon-scanning item** (twice-yearly plus Agile releases) rather than discovering the change during an audit — see [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **Control frameworks.** ATT&CK is orthogonal to [NIST SP 800-53](nist-800-53.md), [NIST CSF 2.0](nist-csf-2.md), [ISO/IEC 27001:2022](iso-27001-2022.md), [CIS Controls v8](cis-controls-v8.md), [CSA CCM](csa-ccm-star.md) and [PCI DSS v4](pci-dss-4.md): those enumerate controls, ATT&CK enumerates behaviours. Published mappings (CTID for 800-53, CCM and the cloud platforms; D3FEND for 800-53 Rev. 5 and DISA CCI; the CIS mapping noted in the CIS pack) bridge them, lossily.
- **DORA.** Art. 26 requires identified financial entities — excluding microenterprises and entities on the simplified framework — to carry out TLPT **at least every 3 years**, on live production systems covering several or all critical or important functions, with scope validated by the competent authority; internal testers may be used but external testers must be engaged **every three tests**, and significant credit institutions must use external testers. DORA Art. 3 defines TLPT as mimicking the **tactics, techniques and procedures** of real-life threat actors — the ATT&CK vocabulary in all but name. See [dora.md](../regulations/dora.md) and [eu-dora-technical-standards.md](../regulations/eu-dora-technical-standards.md).
- **TIBER-EU / CBEST.** TIBER-EU was published by the ECB and the national central banks in May 2018 and **updated in 2024** to align fully with the DORA TLPT RTS; the ECB states that adopting TIBER-EU can help fulfil the DORA TLPT requirements. It has been adopted in 20 jurisdictions plus the ECB, is explicitly not pass/fail, and applies beyond financial services. The UK equivalent, CBEST, has been part of the Bank of England/PRA/FCA supervisory toolkit since 2014 — see [uk-financial-operational-resilience.md](../regulations/uk-financial-operational-resilience.md).
- **Incident response.** ATT&CK technique IDs are the natural tagging scheme for incident records and post-incident reviews; see [nist-800-61-incident-handling.md](nist-800-61-incident-handling.md).
- **AI governance.** ATLAS complements — and does not replace — [EU AI Act](../regulations/eu-ai-act.md) obligations and AI management-system requirements; it supplies the threat scenarios those regimes assume you have considered.
- **Terminology.** ATT&CK-specific terms used above (tactic, technique, sub-technique, campaign, purple teaming) are defined in the [glossary](../glossary.md).

## Primary sources

- MITRE ATT&CK — Updates (August 2026 / v19.2): https://attack.mitre.org/resources/updates/ *(fetched)*
- MITRE ATT&CK — April 2026 release notes (v19, object counts): https://attack.mitre.org/resources/updates/updates-april-2026/ *(fetched)*
- MITRE ATT&CK — October 2025 release notes (v18, Detection Strategies): https://attack.mitre.org/resources/updates/updates-october-2025/ *(fetched)*
- MITRE ATT&CK — Version history (release dates for v18, v19 and v19.2): https://attack.mitre.org/resources/versions/ *(fetched)*
- MITRE ATT&CK — Enterprise tactics: https://attack.mitre.org/tactics/enterprise/ *(fetched)*
- MITRE ATT&CK — Groups, Software and Campaigns indexes (current cross-domain totals): https://attack.mitre.org/groups/, https://attack.mitre.org/software/, https://attack.mitre.org/campaigns/ *(fetched)*
- MITRE ATT&CK — Terms of use (royalty-free licence): https://attack.mitre.org/resources/legal-and-branding/terms-of-use/ *(fetched)*
- MITRE ATT&CK — Data & Tools (Navigator, Workbench, STIX): https://attack.mitre.org/resources/attack-data-and-tools/ *(fetched)*
- MITRE D3FEND — matrix and version: https://d3fend.mitre.org/ *(fetched)*
- MITRE D3FEND — resources, mappings and ontology changelog: https://d3fend.mitre.org/resources/ *(fetched)*
- MITRE D3FEND — about (funding, method): https://d3fend.mitre.org/about/ *(fetched)*
- MITRE ATLAS data release 2026.09: https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/v6/ATLAS-2026.09.yaml *(fetched; publisher-maintained data repository)*
- CAPEC — list version 3.9 and total attack patterns: https://capec.mitre.org/data/index.html *(fetched)*
- CAPEC — New to CAPEC (execution-flow phases, CWE linkage): https://capec.mitre.org/about/new_to_capec.html *(fetched)*
- Center for Threat-Informed Defense — project portfolio and dates: https://ctid.mitre.org/projects/ *(fetched)*
- CTID — ATT&CK Sync and INFORM project pages: https://ctid.mitre.org/projects/attack-sync/ and https://ctid.mitre.org/inform/ *(fetched)*
- CTID Mappings Explorer — NIST 800-53 mappings (revisions and ATT&CK versions): https://center-for-threat-informed-defense.github.io/mappings-explorer/external/nist/ *(fetched)*
- CTID Mappings Explorer — all mapping frameworks and their ATT&CK versions: https://center-for-threat-informed-defense.github.io/mappings-explorer/ *(fetched)*
- CTID Mappings Explorer — mapping methodology (Minimal / Partial / Significant scoring): https://center-for-threat-informed-defense.github.io/mappings-explorer/about/methodology/ *(fetched)*
- Regulation (EU) 2022/2554 (DORA), Arts. 3 and 26 (TLPT definition, frequency, tester rules): https://eur-lex.europa.eu/eli/reg/2022/2554/oj *(official text fetched from the Publications Office, CELEX 32022R2554)*
- ECB — What is TIBER-EU?: https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html *(fetched)*
- Bank of England — CBEST Implementation Guide: https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide *(fetched)*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
