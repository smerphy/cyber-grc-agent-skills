# Authoritative Monitoring Sources by Jurisdiction

Primary sources are the only citable authority for a development's status, text, and dates.
Secondary sources may surface signal earlier but must always be traced back to a primary source
before an item enters the horizon register. For each source you adopt, record: what it
publishes, how often you check it, and who owns the check.

## European Union

| Source | What it publishes / why monitor |
|---|---|
| Official Journal of the EU (via EUR-Lex) | The authoritative text of every regulation, directive, delegated act, and implementing act. Entry-into-force and application dates are computed from OJ publication. The final word on what the law says. |
| EUR-Lex | Consolidated texts, corrigenda, national transposition measures for directives (useful for tracking NIS2-style transposition state by member state), and legislative procedure records. |
| European Parliament Legislative Observatory (OEIL) | Stage-by-stage status of pending legislative files: committee reports, trilogue outcomes, vote dates. The earliest reliable signal on what a proposal will become. |
| European Commission | Legislative proposals, calls for evidence, public consultations, draft delegated/implementing acts, Q&A documents. Delegated acts often carry the operational detail (thresholds, templates) that determines real effort. |
| EDPB (European Data Protection Board) | Guidelines, opinions, binding decisions, and coordinated enforcement priorities under GDPR. Guidelines shift interpretation without changing the regulation's text — treat as horizon events. |
| EDPS | Opinions on EU legislative proposals touching personal data; early signal on privacy issues in pending files. |
| ENISA | Implementing guidance and technical mappings for NIS2 and the Cybersecurity Act, certification schemes (EUCC and successors), threat landscape reports. |
| European Supervisory Authorities: EBA, ESMA, EIOPA | For financial entities: DORA regulatory technical standards (RTS) and implementing technical standards (ITS), consultations, and supervisory statements. The RTS layer is where DORA obligations become concrete. |
| EU AI Office (within the Commission) | GPAI codes of practice, guidance on AI Act interpretation, template documents. Central to AI Act readiness tracking. |
| CEN/CENELEC | Harmonized standards development supporting the AI Act, Cyber Resilience Act, and Radio Equipment Directive. Harmonized standards create presumption-of-conformity paths — their publication dates are horizon events for product compliance strategy. |
| National transposition and DPAs | For directives, the member-state implementing law is what binds; monitor the national official journal of each state of establishment. National DPAs (CNIL, BfDI/state DPAs, Garante, AEPD, DPC Ireland, etc.) publish guidance and enforcement that shape practical obligations. |

## United States — federal

| Source | What it publishes / why monitor |
|---|---|
| Federal Register | Every proposed rule, final rule, and notice from all federal agencies, with comment deadlines and effective dates. The backbone of US federal monitoring; regulations.gov carries the dockets and comments. |
| SEC | Rulemaking (proposed and final rules), guidance, C&DIs, and enforcement actions relevant to cyber disclosure (Form 8-K Item 1.05, Regulation S-K Item 106) and internal controls. Enforcement actions signal interpretation. |
| FTC | Safeguards Rule amendments and breach reporting requirements under GLBA, Section 5 enforcement (unfair/deceptive practices covering security and privacy claims, dark patterns, AI claims), Health Breach Notification Rule. Consent orders function as de facto rules. |
| NIST (CSRC) | CSF, SP 800-series drafts and finals, AI RMF and companion resources, post-quantum cryptography migration guidance. Voluntary, but contractual and regulatory references make revisions horizon events. |
| CISA | Binding Operational Directives and Emergency Directives (binding on federal agencies, signal for everyone), CIRCIA rulemaking status (critical-infrastructure incident reporting), KEV catalog policy, secure-by-design guidance. |
| HHS Office for Civil Rights (OCR) | HIPAA rulemaking (including Security Rule updates), enforcement resolutions, breach portal trends. |
| Federal banking agencies (OCC, Federal Reserve, FDIC) and FFIEC | Interagency guidance, the 36-hour computer-security incident notification rule for banking organizations, examination handbook updates. |
| CFPB | Rules and circulars touching consumer financial data (including data-rights rulemaking) and service-provider oversight. |
| DoD / CMMC program (via the DoD CIO and Federal Register) | CMMC rule status and phase-in for defense contractors; DFARS clause changes. |

## United States — state

| Source | What it publishes / why monitor |
|---|---|
| State attorneys general | Breach notification enforcement, privacy enforcement (many state privacy laws are AG-enforced), rulemaking in some states, published guidance. Monitor the AGs of states where you have significant customer bases. |
| California Privacy Protection Agency (CPPA) | CCPA/CPRA regulations, rulemaking on automated decision-making, risk assessments, and audits; enforcement. The most active state privacy regulator. |
| NY Department of Financial Services (DFS) | 23 NYCRR Part 500 cybersecurity regulation amendments, guidance letters, enforcement — binding for covered financial services entities. |
| State legislatures | New comprehensive privacy laws, AI laws, breach-law amendments. Impractical to monitor 50 legislatures directly — use a secondary tracker (below) and confirm against the enrolled bill text on the state legislature's site. |

## United Kingdom

| Source | What it publishes / why monitor |
|---|---|
| legislation.gov.uk | Authoritative text of acts and statutory instruments, including data protection and cybersecurity legislation and amendments. |
| ICO (Information Commissioner's Office) | UK GDPR/DPA guidance, codes of practice, enforcement, consultation responses; international transfer mechanisms (IDTA, UK addendum). |
| NCSC | Cyber Assessment Framework updates, guidance referenced by UK regulators. |
| FCA and PRA | Operational resilience rules, outsourcing/third-party requirements, critical-third-party regime development for financial services. |
| DSIT and parliamentary bill trackers | Pending cyber and data legislation status (bills.parliament.uk for stage tracking). |

## Other key jurisdictions

| Source | What it publishes / why monitor |
|---|---|
| APRA (Australia) | Prudential standards for regulated financial entities — CPS 234 (information security), CPS 230 (operational risk), practice guides, and consultation papers. |
| OAIC (Australia) | Privacy Act reform implementation, Notifiable Data Breaches scheme guidance and reports. |
| OPC Canada + provincial regulators | PIPEDA guidance and reform status; Quebec (Law 25) and other provincial regimes via provincial regulators and gazettes. |
| PDPC (Singapore) | PDPA advisory guidelines, enforcement decisions, model AI governance frameworks. |
| ANPD (Brazil) | LGPD regulations, security-incident reporting rules, international transfer rules, enforcement. |
| CAC (China) | PIPL/DSL/CSL implementing measures, cross-border data transfer rules and exemptions, algorithm and AI regulations. Official texts in Chinese; verify translations. |
| PPC (Japan) | APPI guidelines and the triennial review cycle of the Act. |
| MeitY / Data Protection Board (India) | DPDP Act rules and enforcement machinery as they are notified; effective obligations depend on notified rules, so rule notifications are the horizon events. |
| National official gazettes | For any other jurisdiction of establishment, the official gazette plus the national DPA/cyber agency form the minimum primary pair. |

## Standards and industry bodies

| Source | What it publishes / why monitor |
|---|---|
| ISO/IEC JTC 1/SC 27 | Revisions of 27001/27002 and the 27xxx family. Certification transition windows after a revision are hard deadlines for certified orgs. |
| ISO/IEC JTC 1/SC 42 | AI standards (including AI management systems) increasingly referenced by regulators and customers. |
| PCI Security Standards Council | PCI DSS versions, future-dated requirement activations, SAQ changes, FAQs and guidance. Version sunset dates are compliance deadlines for anyone handling cardholder data. |
| AICPA | Trust Services Criteria and SOC reporting guidance revisions — affects SOC 2 scope and auditor expectations. |
| CIS | Controls version updates and benchmark revisions. |
| Cloud Security Alliance | CCM revisions relevant if used in customer assurance or STAR. |

## Secondary sources and aggregators — use with rules

Useful for breadth, never citable as authority:

- **Professional associations** (e.g., privacy and audit professional bodies) — legislative
  trackers and news digests; good early warning for state-level and international activity.
- **Law firm and Big Four client alerts** — fast analysis of major developments; watch for
  marketing framing that inflates urgency.
- **Regulator newsletters and RSS/alert subscriptions** — many primary sources above offer
  alerts; prefer these over third-party summaries where available.
- **Vendor blogs** — treat as leads only; commercial incentive to overstate impact.

Rules: (1) every secondary-sourced item must be confirmed against a primary source before
register entry; (2) record the primary citation, not the alert; (3) if primary confirmation
cannot be found, the item does not exist for register purposes.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
