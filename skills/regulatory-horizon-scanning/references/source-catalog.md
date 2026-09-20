# Authoritative Monitoring Sources by Jurisdiction

Primary sources are the only citable authority for a development's status, text, and dates.
Secondary sources may surface signal earlier but must always be traced back to a primary source
before an item enters the horizon register. For each source you adopt, record: what it
publishes, how often you check it, and who owns the check.

How to read the tables. Within each region, sources run in the order you should trust them:
official journal or legislature first, then the cross-sector regulator, then sector regulators.
The **Check** column is a realistic default cadence for a team with a normal workload — raise it
to weekly for any source carrying a file you have an open register entry against, and lower it
to annual for jurisdictions where you have no establishment and no customers. Each regional
section ends with the context packs covering that region; load the pack for the facts, use this
catalog only to decide what to watch.

## European Union

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Official Journal of the EU (via EUR-Lex) | The authoritative text of every regulation, directive, delegated act, and implementing act. Entry-into-force and application dates are computed from OJ publication. The final word on what the law says. | Weekly |
| EUR-Lex | Consolidated texts, corrigenda, national transposition measures for directives (useful for tracking NIS2-style transposition state by member state), and legislative procedure records. | Weekly |
| European Parliament Legislative Observatory (OEIL) | Stage-by-stage status of pending legislative files: committee reports, trilogue outcomes, vote dates. The earliest reliable signal on what a proposal will become. | Weekly while a file is live |
| Council of the EU document register (data.consilium.europa.eu) | Presidency progress reports, general approaches, and negotiating mandates — the other half of the trilogue picture that OEIL alone does not give you. | Monthly |
| European Commission | Legislative proposals, calls for evidence, public consultations, draft delegated/implementing acts, Q&A documents. Delegated acts often carry the operational detail (thresholds, templates) that determines real effort. | Weekly |
| Commission thematic portals: digital-strategy, single-market-economy, health, home-affairs | Where the operational guidance for a specific file actually lands — Cyber Resilience Act and product guidance on the single-market and digital-strategy pages, EHDS on the health pages, CER Directive on home-affairs. Guidance appears here before it appears anywhere else. | Monthly, per file you own |
| Commission NIS2 transposition tracker and infringement press releases | Per-country transposition state and referrals to the CJEU for non-transposition. The practical answer to "is there a law binding me in that member state yet". | Quarterly |
| EDPB (European Data Protection Board) | Guidelines, opinions, binding decisions, and coordinated enforcement priorities under GDPR. Guidelines shift interpretation without changing the regulation's text — treat as horizon events. | Monthly |
| EDPS | Opinions on EU legislative proposals touching personal data; early signal on privacy issues in pending files. | Quarterly |
| ENISA | Implementing guidance and technical mappings for NIS2 and the Cybersecurity Act, certification schemes (EUCC and successors, via the ENISA certification pages), threat landscape reports. | Monthly |
| European Supervisory Authorities: EBA, ESMA, EIOPA | For financial entities: DORA regulatory technical standards (RTS) and implementing technical standards (ITS), consultations, and supervisory statements. The RTS layer is where DORA obligations become concrete. | Monthly |
| EU AI Office (within the Commission) | GPAI codes of practice, guidance on AI Act interpretation, template documents. Central to AI Act readiness tracking. | Monthly |
| CEN/CENELEC | Harmonized standards development supporting the AI Act, Cyber Resilience Act, Radio Equipment Directive and the Machinery Regulation. Harmonized standards create presumption-of-conformity paths — their publication dates are horizon events for product compliance strategy. | Quarterly |
| National transposition and DPAs | For directives, the member-state implementing law is what binds; monitor the national official journal of each state of establishment. National DPAs (CNIL, BfDI/state DPAs, Garante, AEPD, DPC Ireland, etc.) publish guidance and enforcement that shape practical obligations. | Monthly for states of establishment |
| National cyber authorities and NIS2 competent authorities | Registration portals, sector scoping decisions and national technical baselines: BSI and gesetze-im-internet.de (Germany), ANSSI (France), ACN (Italy), NCSC-NL (Netherlands), NCSC Ireland, CCB (Belgium). Registration duties and deadlines are set nationally, not by the Directive. | Monthly for states of establishment |
| Sector and single-file national authorities | Where a Regulation names a national competent authority: for the Data Act, Germany's Bundesnetzagentur became competent authority, dispute-body certifier and cloud-switching supervisor when the national implementing act took effect. Expect one such authority per member state per file. | Quarterly |

Packs: [gdpr](../../../context/regulations/gdpr.md) · [eu-eprivacy](../../../context/regulations/eu-eprivacy.md) · [eu-gdpr-international-transfers](../../../context/regulations/eu-gdpr-international-transfers.md) · [nis2](../../../context/regulations/nis2.md) · [eu-nis2-implementing-and-transposition](../../../context/regulations/eu-nis2-implementing-and-transposition.md) · [eu-cer-directive](../../../context/regulations/eu-cer-directive.md) · [dora](../../../context/regulations/dora.md) · [eu-dora-technical-standards](../../../context/regulations/eu-dora-technical-standards.md) · [eu-ai-act](../../../context/regulations/eu-ai-act.md) · [eu-cyber-resilience-act](../../../context/regulations/eu-cyber-resilience-act.md) · [eu-cybersecurity-act](../../../context/regulations/eu-cybersecurity-act.md) · [eu-data-act](../../../context/regulations/eu-data-act.md) · [eu-digital-services-act](../../../context/regulations/eu-digital-services-act.md) · [eu-ehds](../../../context/regulations/eu-ehds.md) · [eu-eidas2](../../../context/regulations/eu-eidas2.md) · [eu-product-security-red-machinery](../../../context/regulations/eu-product-security-red-machinery.md)

## United States — federal

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Federal Register | Every proposed rule, final rule, and notice from all federal agencies, with comment deadlines and effective dates. The backbone of US federal monitoring; regulations.gov carries the dockets and comments. | Weekly |
| eCFR and govinfo / uscode.house.gov | The codified text as it currently stands (eCFR) and the authenticated statutory text. Use these to confirm what a rule became after the Federal Register notice, not the preamble. | On use |
| Reginfo.gov (Unified Agenda, OIRA review) | Each agency's planned rulemakings with target dates and RIN, plus rules sitting at OMB review. The earliest official signal that a rule is coming and roughly when — CIRCIA and the TSA cyber rule are both tracked this way. | Each Agenda edition (twice a year), plus quarterly for RINs you own |
| SEC | Rulemaking (proposed and final rules), guidance, C&DIs, and enforcement actions relevant to cyber disclosure (Form 8-K Item 1.05, Regulation S-K Item 106), Regulation S-P and Regulation SCI, and internal controls. Enforcement actions signal interpretation. | Monthly |
| FINRA | Notices and rule filings that carry SEC requirements down to broker-dealers — the operational layer above Reg S-P for member firms. | Quarterly |
| FTC | Safeguards Rule amendments and breach reporting requirements under GLBA, Section 5 enforcement (unfair/deceptive practices covering security and privacy claims, dark patterns, AI claims), Health Breach Notification Rule, COPPA Rule amendments and consent orders. Consent orders function as de facto rules. | Monthly |
| NIST (CSRC, nvlpubs, project pages) | CSF and its profiles and companion resources, SP 800-series drafts and finals, SSDF, zero trust, C-SCRM, digital identity, AI RMF and companion resources, post-quantum cryptography migration guidance. Voluntary, but contractual and regulatory references make revisions horizon events; drafts carry comment deadlines. | Quarterly, plus each comment deadline you intend to meet |
| CISA | Binding Operational Directives and Emergency Directives (binding on federal agencies, signal for everyone), CIRCIA rulemaking status (critical-infrastructure incident reporting), KEV catalog policy, Cross-Sector Cybersecurity Performance Goals and sector-specific goals, secure-by-design guidance. | Monthly |
| HHS Office for Civil Rights (OCR) | HIPAA rulemaking (including Security Rule updates), enforcement resolutions, breach portal trends. | Monthly |
| FDA | Premarket cybersecurity guidance for medical devices and the device-specific statutory requirements; guidance documents, not rules, carry most of the obligation detail. | Quarterly |
| Federal banking agencies (OCC, Federal Reserve, FDIC, NCUA) and FFIEC | Interagency guidance, the 36-hour computer-security incident notification rule for banking organizations, third-party risk guidance, examination handbook updates. | Monthly |
| CFPB | Rules and circulars touching consumer financial data (including data-rights rulemaking) and service-provider oversight. | Quarterly |
| DoD / CMMC program (via the DoD CIO, acquisition.gov and the Federal Register) | CMMC rule status and phase-in for defense contractors; DFARS clause changes; the SP 800-171 assessment regime behind them. | Monthly |
| FedRAMP (fedramp.gov) and OMB | Authorization process changes, baselines and key security indicators; OMB memoranda set the policy the program implements. | Monthly |
| DOJ National Security Division | The bulk sensitive data rule — restricted and prohibited transactions, covered data thresholds, security requirements developed with CISA, and compliance FAQ updates. | Quarterly |
| FBI CJIS (le.fbi.gov file repository) | CJIS Security Policy versions and the Requirements Companion Document for anyone touching criminal justice information. Policy is versioned and republished as a PDF, not as a rule. | Twice a year |
| IRS | Publication 1075 and its safeguard requirements for federal tax information held by agencies and their contractors. | Twice a year |
| TSA | Security directives and the pipeline/rail cyber risk management rulemaking; directives renew and change on their own clock rather than through notice-and-comment. | Quarterly, plus on each directive renewal |
| Department of Education (studentprivacy.ed.gov) | FERPA guidance and technical assistance for education records and edtech vendors. | Twice a year |
| NERC (and FERC via the Federal Register) | CIP standards development, approved and pending standards, and enforcement — NERC files, FERC approves, and the Federal Register notice is the binding event. | Quarterly |

Packs: [sec-cyber-disclosure](../../../context/regulations/sec-cyber-disclosure.md) · [us-sec-reg-sp-reg-sci](../../../context/regulations/us-sec-reg-sp-reg-sci.md) · [glba-ftc-safeguards](../../../context/regulations/glba-ftc-safeguards.md) · [us-ftc-act-health-breach-rule](../../../context/regulations/us-ftc-act-health-breach-rule.md) · [us-coppa](../../../context/regulations/us-coppa.md) · [hipaa](../../../context/regulations/hipaa.md) · [us-fda-medical-device-cybersecurity](../../../context/regulations/us-fda-medical-device-cybersecurity.md) · [sox-itgc](../../../context/regulations/sox-itgc.md) · [us-circia](../../../context/regulations/us-circia.md) · [us-banking-incident-notification-third-party](../../../context/regulations/us-banking-incident-notification-third-party.md) · [us-fisma-federal-cyber](../../../context/regulations/us-fisma-federal-cyber.md) · [us-doj-bulk-data-rule](../../../context/regulations/us-doj-bulk-data-rule.md) · [us-cjis-security-policy](../../../context/regulations/us-cjis-security-policy.md) · [us-irs-pub-1075](../../../context/regulations/us-irs-pub-1075.md) · [us-tsa-transportation-cyber](../../../context/regulations/us-tsa-transportation-cyber.md) · [us-ferpa-education-privacy](../../../context/regulations/us-ferpa-education-privacy.md) · [nerc-cip](../../../context/regulations/nerc-cip.md)

## United States — state

| Source | What it publishes / why monitor | Check |
|---|---|---|
| State attorneys general | Breach notification enforcement, privacy enforcement (many state privacy laws are AG-enforced), rulemaking in some states, published guidance and breach portals. Monitor the AGs of states where you have significant customer bases. | Quarterly; monthly for your top states |
| California Privacy Protection Agency (CPPA) | CCPA/CPRA regulations, rulemaking on automated decision-making, risk assessments, and audits; enforcement. The most active state privacy regulator. | Monthly |
| NY Department of Financial Services (DFS) | 23 NYCRR Part 500 cybersecurity regulation amendments, guidance letters, enforcement — binding for covered financial services entities. DFS's own site is the reliable copy; the official NYCRR compilation is not scriptable. | Monthly |
| State legislatures (official bill and statute sites) | New comprehensive privacy laws, AI laws, biometric laws, breach-law amendments. Impractical to monitor 50 legislatures directly — use a secondary tracker (below) and confirm against the enrolled bill text or codified section on the state legislature's own site. | Weekly during session for tracked bills; quarterly otherwise |
| NAIC (content.naic.org) | The Insurance Data Security Model Law text and the state-adoption page — the model is only law where a state enacts it, so the adoption table is the thing to watch, not the model. | Twice a year |
| State cloud authorization programs (e.g. the Texas DIR program, GovRAMP) | Authorization requirements for vendors selling to state agencies; they inherit from FedRAMP but diverge on timing. | Twice a year |

Packs: [us-state-privacy](../../../context/regulations/us-state-privacy.md) · [us-state-breach-notification-laws](../../../context/regulations/us-state-breach-notification-laws.md) · [us-state-ai-laws](../../../context/regulations/us-state-ai-laws.md) · [us-biometric-privacy-laws](../../../context/regulations/us-biometric-privacy-laws.md) · [us-nydfs-part-500](../../../context/regulations/us-nydfs-part-500.md) · [us-naic-insurance-data-security](../../../context/regulations/us-naic-insurance-data-security.md) · [fedramp](../../../context/frameworks/fedramp.md)

## United Kingdom

| Source | What it publishes / why monitor | Check |
|---|---|---|
| legislation.gov.uk | Authoritative text of acts and statutory instruments, including data protection, product security and cybersecurity legislation and amendments. | Monthly |
| Parliament bill pages and the Bills API (bills.parliament.uk, bills-api.parliament.uk) | Stage-by-stage progress of pending bills — the cyber security and resilience legislation is tracked here until it becomes an Act. The API is the scriptable route where the HTML pages are not. | Weekly while a bill you track is live |
| ICO (Information Commissioner's Office) | UK GDPR/DPA guidance, codes of practice, enforcement, consultation responses; international transfer mechanisms (IDTA, UK addendum). | Monthly |
| NCSC | Cyber Assessment Framework versions and changelog, Cyber Essentials requirements and scheme changes, guidance referenced by UK regulators. | Quarterly |
| IASME | Cyber Essentials delivery: question set changes, scheme updates and certification-body notices — the operational detail behind an NCSC scheme change. | Quarterly |
| FCA and PRA (handbook and Bank of England pages) | Operational resilience rules, outsourcing/third-party requirements, critical-third-party regime development for financial services. | Monthly |
| DSIT, gov.uk guidance and the Government Security function | Policy papers, PSTI product-security guidance, procurement policy notes that make a scheme contractual, and consultation outcomes. | Monthly |
| Devolved and sector bodies (Northern Ireland Assembly, NHS DSP Toolkit) | Where a regime is devolved or delivered through a sector toolkit, the deadline that binds you is published there, not centrally. | Quarterly |

Packs: [uk-data-protection](../../../context/regulations/uk-data-protection.md) · [uk-nis-cyber-security-resilience](../../../context/regulations/uk-nis-cyber-security-resilience.md) · [uk-financial-operational-resilience](../../../context/regulations/uk-financial-operational-resilience.md) · [uk-psti-product-security](../../../context/regulations/uk-psti-product-security.md) · [uk-cyber-essentials-ncsc-caf](../../../context/frameworks/uk-cyber-essentials-ncsc-caf.md)

## Europe outside the EU

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Switzerland — Fedlex (fedlex.admin.ch) | Consolidated federal law including the FADP and the Information Security Act; the German, French and Italian texts are the official ones. | Quarterly |
| Switzerland — FDPIC (edoeb.admin.ch), BACS and FINMA | Data protection guidance and enforcement; the federal cyber security office for incident reporting duties; FINMA for financial-sector operational and cyber requirements. | Quarterly |

Packs: [switzerland-fadp-isa](../../../context/regulations/switzerland-fadp-isa.md) · [germany-bsi-it-grundschutz-c5](../../../context/frameworks/germany-bsi-it-grundschutz-c5.md)

## Canada and Latin America

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Canada — Justice Laws (laws-lois.justice.gc.ca) and Parliament (parl.ca) | Consolidated federal statutes including PIPEDA, and the status of reform bills. | Quarterly |
| Canada — OPC (priv.gc.ca), provincial regulators and provincial statute sites | PIPEDA guidance and reform status; Quebec (Law 25) via LégisQuébec and the provincial regulator, plus Alberta and British Columbia statutes. | Quarterly |
| Canada — OSFI | Technology and cyber risk and third-party guidelines for federally regulated financial institutions. | Quarterly |
| Brazil — Planalto and the Diário Oficial da União (in.gov.br) | The LGPD text and every implementing act; the DOU is where ANPD resolutions become binding. | Monthly |
| Brazil — ANPD (gov.br/anpd) | LGPD regulations, security-incident reporting rules, international transfer rules, enforcement. | Monthly |
| Mexico — Cámara de Diputados | Consolidated LFPDPPP and LGPDPPSO texts and their reforms. | Quarterly |
| Argentina — InfoLEG and the AAIP | Ley 25.326 text and AAIP resolutions and guidance. | Quarterly |
| Chile — Biblioteca del Congreso Nacional (leychile.cl) | Ley 21.719 and the amended Ley 19.628 versions with their effective dates. | Quarterly |
| Colombia — Senado (secretariasenado.gov.co) and the SIC | Ley 1581/2012, its decrees and the SIC's external circulars. | Quarterly |
| Peru — MINJUSDH and the ANPD (gob.pe) | Ley 29733, its reglamento and the regulator's normative index and directoral resolutions. | Quarterly |
| Uruguay — IMPO and the URCDP | Consolidated legal texts and the regulator's guidance; relevant to EU adequacy status. | Quarterly |
| Ecuador — Gobierno del Ecuador regulations repository and the Superintendencia de Protección de Datos Personales | The consolidated LOPDP text and the regulator's build-out. | Quarterly |
| Costa Rica — official normative copies | Ley 8968; the regulator's own pages are unreliable to fetch, so keep a second official copy (see the hard-to-monitor section). | Twice a year |
| European Commission adequacy pages | Which of these regimes currently holds an adequacy decision, and the periodic review reports on them — an adequacy change is a transfer-mechanism event. | Quarterly |

Packs: [canada-pipeda-law-25](../../../context/regulations/canada-pipeda-law-25.md) · [brazil-lgpd](../../../context/regulations/brazil-lgpd.md) · [latin-america-privacy-regimes](../../../context/regulations/latin-america-privacy-regimes.md)

## Asia-Pacific

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Australia — Federal Register of Legislation (legislation.gov.au) and APH | Acts and instruments including the privacy and critical-infrastructure legislation, and parliamentary status of pending bills. | Monthly |
| Australia — OAIC | Privacy Act reform implementation, Notifiable Data Breaches scheme guidance and reports. | Monthly |
| Australia — APRA | Prudential standards for regulated financial entities — CPS 234 (information security), CPS 230 (operational risk), practice guides, and consultation papers. | Monthly |
| Australia — Home Affairs and the Cyber and Infrastructure Security Centre (cisc.gov.au) | SOCI Act rules, designations and the cyber security legislation package; the CISC publishes the operational guidance and forms. | Monthly |
| Australia — ACSC (cyber.gov.au) | Information Security Manual and Essential Eight maturity guidance. | Quarterly, on the ISM release months |
| New Zealand — legislation.govt.nz, the NZ Gazette, OPC (privacy.org.nz) and NCSC | Privacy Act text and amendments, gazette notices, regulator guidance, and the national cyber authority's reporting expectations. | Quarterly |
| Singapore — Singapore Statutes Online (sso.agc.gov.sg) | Consolidated PDPA and Cybersecurity Act text plus the subsidiary regulations, which is where breach and CII duties actually sit. | Quarterly |
| Singapore — PDPC, CSA and MAS | PDPA advisory guidelines and enforcement decisions; CSA codes of practice, licensing and the Cyber Essentials/Cyber Trust marks; MAS notices, guidelines and incident-reporting circulars for financial institutions. | Monthly |
| Hong Kong — e-Legislation (elegislation.gov.hk) and LegCo | Ordinance text and bill papers, including the critical-infrastructure computer-system regime. | Quarterly |
| Hong Kong — PCPD, OCCICS, the Communications Authority, HKMA and SFC | PDPO guidance and breach-handling expectations; the critical-infrastructure commissioner's codes of practice and sectoral codes; sector regulators' circulars and supervisory manuals. | Monthly |
| Japan — e-Gov law database (laws.e-gov.go.jp) and Japanese Law Translation | Current Japanese statutory text and the official — but lagging — English translations. | Quarterly |
| Japan — PPC, the National Cybersecurity Office (cyber.go.jp), METI and FSA | APPI guidelines and the amendment cycle, breach-reporting pages and forms; the active-cyberdefence legislation and its cabinet orders; METI management guidelines; FSA financial-sector cyber guidelines. | Monthly |
| South Korea — National Law Information Center (law.go.kr) and KLRI translations | Current Korean text of PIPA and its Enforcement Decree, with the research institute's English translations as a reading aid. | Quarterly |
| South Korea — PIPC | Enforcement decisions, ISMS-P certification criteria, and announcements including adequacy-related developments. | Monthly |
| China — CAC (cac.gov.cn) and the State Council (gov.cn) | Implementing measures and decrees under PIPL/DSL/CSL, cross-border transfer rules and exemptions, incident-reporting measures, compliance-audit measures, draft rules open for comment, and enforcement campaigns. Official texts are Chinese. | Monthly |
| China — national standards platform (openstd.samr.gov.cn) | Catalogue entries for the GB/T standards that regulators reference; full text is often not public. | Quarterly |
| India — MeitY and the Gazette of India | The DPDP Act and the DPDP Rules as notified; obligations turn on notified rules, so rule notifications are the horizon events. | Monthly |
| India — CERT-In, RBI, SEBI and IRDAI | The s.70B directions, FAQs and technical guidelines (including the SBOM family); sector cyber frameworks, circulars and extensions — SEBI's CSCRF in particular moves through dated circulars. | Monthly |
| Malaysia — PDP Department (pdp.gov.my) | Amendment Act commencement orders, commissioner's circulars (breach notification, DPO appointment), and the cross-border, DPIA and by-design guidelines. Circulars are often issued in Malay first. | Quarterly |
| Other Southeast Asia — national gazettes and regulators (Indonesia, Thailand, Vietnam, Philippines) | Law and implementing-regulation text, and the regulator build-out. Official online publication is patchy for this group; see the hard-to-monitor section. | Quarterly |

Packs: [australia-privacy-act](../../../context/regulations/australia-privacy-act.md) · [australia-apra-cps-234-230](../../../context/regulations/australia-apra-cps-234-230.md) · [australia-soci-cyber-security-act](../../../context/regulations/australia-soci-cyber-security-act.md) · [australia-essential-eight-ism](../../../context/frameworks/australia-essential-eight-ism.md) · [new-zealand-privacy-act](../../../context/regulations/new-zealand-privacy-act.md) · [singapore-pdpa-cybersecurity](../../../context/regulations/singapore-pdpa-cybersecurity.md) · [hong-kong-pdpo-critical-infrastructure](../../../context/regulations/hong-kong-pdpo-critical-infrastructure.md) · [japan-appi-cyber](../../../context/regulations/japan-appi-cyber.md) · [south-korea-pipa](../../../context/regulations/south-korea-pipa.md) · [china-pipl-dsl-csl](../../../context/regulations/china-pipl-dsl-csl.md) · [india-dpdp-cert-in](../../../context/regulations/india-dpdp-cert-in.md) · [southeast-asia-privacy-regimes](../../../context/regulations/southeast-asia-privacy-regimes.md)

## Middle East and Africa

| Source | What it publishes / why monitor | Check |
|---|---|---|
| Saudi Arabia — SDAIA | The PDPL and its implementing regulation, the transfer regulation and standard contractual clauses, DPO and national-register rules, accreditation rules and the breach procedural guide, all indexed on the laws-and-regulations page. | Monthly |
| Saudi Arabia — NCA, SAMA and CST | The essential and sector cybersecurity controls documents and the NCA regulatory-documents list; SAMA's rulebook for financial institutions; CST's regulatory framework for the communications sector. Some NCA controls are published in Arabic only. | Quarterly |
| UAE — federal legislation portal (uaelegislation.gov.ae) and the government portal (u.ae) | The federal decree-laws including data protection and cybercrime, in Arabic, with the government portal summaries in English. | Quarterly |
| UAE — DIFC and ADGM | Free-zone data protection laws, amendment laws and rulebooks that bind entities inside the zone regardless of the federal position. | Quarterly |
| UAE — CBUAE and the Dubai Electronic Security Center | Operational risk and technology regulations for licensed financial institutions; DESC standards and policies for Dubai government-linked entities. | Quarterly |
| Israel — Privacy Protection Authority (gov.il) and the Knesset legal databases | The consolidated Privacy Protection Law including its amendments, the data security regulations, transfer regulations and administrative-enforcement regulations, plus PPA opinions. Official texts are Hebrew. | Quarterly |
| South Africa — Government Gazette (gov.za) and the Information Regulator | POPIA and its regulations, guidance notes, codes of conduct, enforcement notices, and the eServices portal for security-compromise notifications; the Cybercrimes Act and its commencement proclamations. | Monthly |
| South Africa — FSCA and Prudential Authority | The joint standards on cybersecurity and IT risk for financial institutions. | Quarterly |
| Nigeria — NDPC | The NDP Act implementation directive, FAQs, registration duties and their annual deadline, and penalty guidance. | Quarterly |
| Kenya — ODPC | The Data Protection Act, the registration regulations and the regulator's framework index. | Quarterly |
| Rwanda, Uganda, Tanzania, Ghana, Morocco, Egypt — national regulators and gazettes | Data protection acts, registration regimes and their regulations; coverage quality varies sharply by country and several sites are unreliable (see below). | Twice a year |
| African Union | The Malabo Convention text and its ratification status — the signature and ratification list is the practical thing to watch. | Annual |

Packs: [saudi-arabia-pdpl-nca](../../../context/regulations/saudi-arabia-pdpl-nca.md) · [uae-data-protection-cyber](../../../context/regulations/uae-data-protection-cyber.md) · [israel-privacy-protection-law](../../../context/regulations/israel-privacy-protection-law.md) · [south-africa-popia](../../../context/regulations/south-africa-popia.md) · [africa-privacy-regimes](../../../context/regulations/africa-privacy-regimes.md) · [other-jurisdictions](../../../context/regulations/other-jurisdictions.md)

Anywhere else: the official gazette plus the national DPA or cyber agency form the minimum
primary pair. Add the sector regulator if you are supervised.

## Standards, frameworks and industry publishers

Revision cadence is stated below only where the pack for that framework states it. Where a
publisher has no stated cadence, watch the publisher's release or advisory feed rather than
guessing a date — "no announced revision" is a finding you can record, not a gap.

| Publisher / source | What it publishes / why monitor | Revision cadence | Check |
|---|---|---|---|
| ISO/IEC JTC 1/SC 27 (via the ISO catalogue and national member bodies) | Revisions of 27001/27002 and the 27xxx family, including the cloud and privacy extensions. Certification transition windows after a revision are hard deadlines for certified orgs. Amendments can land between editions — the 2024 climate-change amendment changed clause 4 inputs without a new edition. | Not stated; revision projects are visible as CD/DIS/FDIS stage entries before publication | Quarterly |
| ISO/IEC JTC 1/SC 42 | AI standards, including the AI management system standard, increasingly referenced by regulators and customers. | Not stated | Quarterly |
| ISO/TC 262 and ISO/TC 292 | Risk management and business continuity standards; the ISO 22301 third-edition project is live at committee stage. | Not stated; watch the project stage codes | Quarterly |
| IEC (webstore) and the ISA/IEC 62443 committees | The 62443 parts for OT and industrial automation security, per-part and paywalled, with public front-matter previews. | Per part, not synchronized | Twice a year |
| UNECE WP.29 | UN Regulations R155/R156 and the status document listing which Contracting Parties apply each regulation and which version is in force — the authoritative answer for market access. | Not stated; the status document is the version of record | Twice a year, plus before any new market entry |
| NIST (CSRC project pages) | CSF profiles and companion resources, the SP 800-series, AI and privacy frameworks. Drafts carry comment deadlines and initial public drafts can sit unfinalized for years — draft status matters for defensibility. | Not stated; track the draft pipeline | Quarterly |
| PCI Security Standards Council | PCI DSS versions, future-dated requirement activations, SAQ changes, FAQs and guidance, plus the other standards in the family (P2PE, Secure Software, PTS POI, HSM). Version sunset dates are compliance deadlines for anyone handling cardholder data. Releases are announced on the council's blog. | Not stated; per-standard releases announced individually | Quarterly |
| AICPA | Trust Services Criteria and SOC reporting guidance revisions — affects SOC 2 scope and auditor expectations; also the SOC 1 / attestation guidance layer. | Not stated | Twice a year |
| IAASB and PCAOB | ISAE 3402 and the auditing standards that sit behind service-organization and ICFR reporting. | Not stated | Annual |
| CIS | Controls version updates and benchmark revisions (free, registration required for download). | Not stated | Quarterly |
| Cloud Security Alliance | CCM revisions and STAR registry program rules relevant if used in customer assurance. STAR Level 1 self-assessments are expected to be refreshed annually. | Not stated for CCM; Level 1 listings updated annually | Quarterly |
| MITRE (ATT&CK, D3FEND, CAPEC, Center for Threat-Informed Defense) | Technique and mitigation content that detection coverage, purple teaming and threat-led testing programs are pinned to. | Twice-yearly stated cadence, plus off-cycle releases | Twice a year, on the release windows |
| OWASP | Top 10 lists (including the LLM list), ASVS, SAMM, WSTG, SCVS and CycloneDX. Release semantics matter contractually: a major version implies re-assessment. Publication dates are sometimes absent from the project pages. | Not stated; per-project and irregular | Quarterly |
| HITRUST | CSF versions and assessment-handbook changes, each announced as a numbered advisory; new authoritative sources are added with each release, which changes what a certification demonstrates. | Multiple releases per year, each with an advisory | Quarterly |
| ISACA | COBIT and its focus areas, plus audit programs. COBIT 2019 remains the current framework publication. | Not stated | Twice a year |
| COSO | Internal control and ERM guidance and supplements — the dated release list on the news index is the reliable signal. | Not stated | Twice a year |
| Institute of Internal Auditors | The Global Internal Audit Standards and Topical Requirements, which set what an external quality assessment will test. | Not stated; the 2024 edition remains current with Topical Requirements issued separately | Twice a year |
| The Open Group and the FAIR Institute | The risk taxonomy and analysis standards behind quantitative cyber risk work, and the certification program. | Not stated | Annual |
| Swift | The Customer Security Controls Framework and the Independent Assessment Framework, published through the Swift document centre and Knowledge Centre. | A new CSCF version each July for the following year; attestation window 1 July – 31 December | Each July, plus mid-year change announcements |
| ENX Association (TISAX / VDA ISA) | The ISA catalogue and TISAX assessment rules for the automotive supply chain. | Annual release cycle with year-based versioning from ISA2027 | Annual, before ordering an assessment |
| Germany — BSI | IT-Grundschutz and the C5 cloud criteria, plus the NIS2 national guidance and registration expectations. | Not stated | Quarterly |
| Australia — ACSC | The Information Security Manual and its OSCAL catalog. | Quarterly content releases (March, June, September, December) | Quarterly, on the release months |
| UK — NCSC and IASME | The Cyber Assessment Framework (with a published changelog) and the Cyber Essentials requirements and question set. | Not stated as a cycle; CAF versions have landed roughly annually to biennially since v3.0 | Quarterly |
| CISA (as a framework publisher) | The Cross-Sector Cybersecurity Performance Goals and the sector-specific goals released with sector risk management agencies. | Not stated; v2.0 superseded v1.0.1 | Twice a year |
| FedRAMP PMO | Baselines, authorization process changes and the continuous-monitoring rhythm, which sets quarterly reporting obligations for authorized providers. | Not stated | Monthly |

Packs: [nist-csf-2](../../../context/frameworks/nist-csf-2.md) · [nist-csf-profiles-and-companion-resources](../../../context/frameworks/nist-csf-profiles-and-companion-resources.md) · [nist-800-53](../../../context/frameworks/nist-800-53.md) · [nist-rmf-800-37-800-30](../../../context/frameworks/nist-rmf-800-37-800-30.md) · [nist-800-171-cmmc](../../../context/frameworks/nist-800-171-cmmc.md) · [nist-800-161-cscrm](../../../context/frameworks/nist-800-161-cscrm.md) · [nist-800-207-zero-trust](../../../context/frameworks/nist-800-207-zero-trust.md) · [nist-800-61-incident-handling](../../../context/frameworks/nist-800-61-incident-handling.md) · [nist-800-63-digital-identity](../../../context/frameworks/nist-800-63-digital-identity.md) · [nist-ssdf-800-218](../../../context/frameworks/nist-ssdf-800-218.md) · [nist-ai-rmf](../../../context/frameworks/nist-ai-rmf.md) · [nist-privacy-framework](../../../context/frameworks/nist-privacy-framework.md) · [iso-27001-2022](../../../context/frameworks/iso-27001-2022.md) · [iso-27017-27018-cloud](../../../context/frameworks/iso-27017-27018-cloud.md) · [iso-27701-privacy-management](../../../context/frameworks/iso-27701-privacy-management.md) · [iso-31000-27005-risk-management](../../../context/frameworks/iso-31000-27005-risk-management.md) · [iso-22301-business-continuity](../../../context/frameworks/iso-22301-business-continuity.md) · [iso-42001-ai-management](../../../context/frameworks/iso-42001-ai-management.md) · [iec-62443-ot-security](../../../context/frameworks/iec-62443-ot-security.md) · [automotive-un-r155-iso-21434](../../../context/regulations/automotive-un-r155-iso-21434.md) · [pci-dss-4](../../../context/frameworks/pci-dss-4.md) · [pci-other-standards](../../../context/frameworks/pci-other-standards.md) · [soc2-tsc](../../../context/frameworks/soc2-tsc.md) · [soc1-isae3402-soc-reports](../../../context/frameworks/soc1-isae3402-soc-reports.md) · [cis-controls-v8](../../../context/frameworks/cis-controls-v8.md) · [csa-ccm-star](../../../context/frameworks/csa-ccm-star.md) · [mitre-attack-threat-informed-defense](../../../context/frameworks/mitre-attack-threat-informed-defense.md) · [owasp-application-security](../../../context/frameworks/owasp-application-security.md) · [hitrust-csf](../../../context/frameworks/hitrust-csf.md) · [cobit-2019](../../../context/frameworks/cobit-2019.md) · [coso-internal-control-erm](../../../context/frameworks/coso-internal-control-erm.md) · [iia-global-internal-audit-standards](../../../context/frameworks/iia-global-internal-audit-standards.md) · [fair-cyber-risk-quantification](../../../context/frameworks/fair-cyber-risk-quantification.md) · [swift-customer-security-programme](../../../context/frameworks/swift-customer-security-programme.md) · [tisax-vda-isa](../../../context/frameworks/tisax-vda-isa.md) · [ffiec-it-examination-handbook](../../../context/frameworks/ffiec-it-examination-handbook.md) · [cisa-cpg-secure-by-design](../../../context/frameworks/cisa-cpg-secure-by-design.md)

## Sources that resist automated monitoring

A monitoring program that silently drops the sources a scraper cannot reach is worse than one
that names them. Every category below is one the context packs hit while being drafted; each
needs a named human owner and a calendar entry instead of a feed.

**Paywalled standards.** ISO, IEC and CEN/CENELEC texts are sold, not published: the 62443
parts are priced per part, the EN product-security standards are sold through national member
bodies, and the vulnerability-disclosure standards referenced by product regulations are behind
the same wall. What to do: monitor the free catalogue entry rather than the text — publication
date, edition, stage code and withdrawal status are all public, and a stage code moving toward
publication is the horizon event. Read the publisher's front-matter preview for scope and
contents. Buy the text before a certification cycle or a conformity-assessment decision, not
after. Never quote clause wording you have not licensed, and never let a summary of a paid
standard stand in for the standard in an audit file.

**Sites that block or defeat scripted access.** Some official sites return challenge pages,
403s, or require JavaScript: examples met while drafting the packs include the US federal
examination handbook site, the Belgian cyber centre, one US state legislature's public-acts
viewer, the EUR-Lex and European Parliament full-text search interfaces, the Chinese
legislature's pages, and the official state compilation of the New York codes. What to do:
(1) prefer the stable document URL over the search interface — the EU document identifier, the
parliamentary bills API, the regulator's own PDF file repository; (2) subscribe to the email
alert or RSS feed where the site offers one; (3) otherwise assign a quarterly manual check to a
named owner and log the check even when nothing changed. Record a fetch failure as a fetch
failure: absence of a search hit is not evidence that a document does not exist.

**Credential-walled and member-only material.** Some binding material is only available behind
a login: the defense cloud computing requirements library needs government credentials, and the
Swift controls framework reaches users through the member knowledge centre before the public
document centre catches up. What to do: make sure at least one named person holds the account,
put the release month in the compliance calendar, and treat the public page as a lagging
confirmation rather than the source.

**Non-English-only official texts.** For several regimes the only authoritative text is in the
local language: Chinese for the PIPL/DSL/CSL implementing measures, Japanese for the APPI
guidelines, Korean for PIPA and its enforcement decree, Hebrew for the Israeli privacy law and
its regulations, Arabic for the UAE federal data protection law and some Saudi national
controls, German/French/Italian for Swiss federal law, Malay for some Malaysian commissioner
circulars, and Thai or Vietnamese for parts of Southeast Asia. What to do: monitor the
official-language page for change (a date or version change is detectable without reading the
language), use the official English translation where one exists while noting that it lags the
amended text, and have local counsel confirm any operative wording before it drives a decision.
Record in the register which language version a fact came from — a fact taken from an
unofficial translation is a verified fact about a translation, not about the law.

**Scanned and image-only documents.** Some official PDFs are page images with no text layer —
a regional convention text and at least one national act met this way. What to do: cite the
regulator's own derivative documents (implementation directives, FAQs, guidance notes) for the
operative detail, and flag the underlying text as unverified until someone has read the image.

**Sites that intermittently fail to resolve.** Several national regulator sites did not resolve
or refused connections during pack drafting. What to do: record the failure and its date in the
register entry, schedule a re-check rather than deleting the source, and fall back to a clearly
labelled secondary source in the meantime — never silently upgrade that secondary to primary.

## Secondary sources and aggregators — use with rules

Useful for breadth, never citable as authority:

- **Professional associations** (e.g., privacy and audit professional bodies) — legislative
  trackers and news digests; good early warning for state-level and international activity.
- **Law firm and Big Four client alerts** — fast analysis of major developments; watch for
  marketing framing that inflates urgency. For jurisdictions with thin official publication,
  country surveys are sometimes the only readable account — mark them as secondary in the
  register and say which specific facts rest on them.
- **Regulator newsletters and RSS/alert subscriptions** — many primary sources above offer
  alerts; prefer these over third-party summaries where available.
- **Vendor blogs** — treat as leads only; commercial incentive to overstate impact.

Rules: (1) every secondary-sourced item must be confirmed against a primary source before
register entry; (2) record the primary citation, not the alert; (3) if primary confirmation
cannot be found, the item does not exist for register purposes — except where the primary
source is one of the hard-to-monitor categories above, in which case the register entry names
the secondary source, the access barrier, and the date of the next attempt.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
