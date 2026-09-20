# South Africa: Protection of Personal Information Act (POPIA, Act 4 of 2013) and the Cybercrimes Act (Act 19 of 2020)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **POPIA** — Protection of Personal Information Act 4 of 2013 (GG 37067, 26 Nov 2013) plus the Regulations relating to the Protection of Personal Information (GN R.1383, GG 42110, 14 Dec 2018). **Cybercrimes Act** 19 of 2020 (GG 44651, 1 Jun 2021). **Joint Standard 2 of 2024** — Cybersecurity and Cyber Resilience Requirements for financial institutions (FSCA/Prudential Authority under the Financial Sector Regulation Act 9 of 2017) |
| Regulators | **Information Regulator** (POPIA s.39; also enforces PAIA, the access-to-information statute); **SAPS** and the National Prosecuting Authority for cybercrimes; **FSCA and Prudential Authority** (jointly "the Authorities") for Joint Standards |
| Status | POPIA substantive sections in force 1 Jul 2020, one-year grace expired 30 Jun 2021 — fully enforceable since 1 Jul 2021. Cybercrimes Act partially commenced 1 Dec 2021; the s.54 72-hour reporting duty was excluded from that commencement. Joint Standard 2 of 2024 effective 1 Jun 2025; its incident-notification template (Joint Notice 2 of 2026) effective 1 Sep 2026 |
| Who is covered | POPIA: any **responsible party** (public or private body, or any person) domiciled in South Africa, or not domiciled but using automated or non-automated means in South Africa (s.3(1)(b)); protects natural **and juristic** persons; **operators** (processors) carry direct duties (ss.20–21). Joint Standard: licensed financial institutions (banks, insurers, CIS managers, market infrastructures, FSPs, pension funds, etc.) |
| Breach clock | POPIA s.22: notify the Regulator and affected data subjects **"as soon as reasonably possible"** after discovery of a security compromise; **no risk threshold** — the Regulator's position is that every compromise is notifiable; mandatory portal reporting since 1 Apr 2025. Joint Standard 2 of 2024 + Joint Notice 2 of 2026: initial notice **within 24 hours** of classifying a cyber or information-security incident as material; update within 14 calendar days |
| Penalties | POPIA administrative fine up to **R10 million** per infringement notice (s.109); criminal offences up to **10 years'** imprisonment and/or a fine (s.107); civil damages including aggravated damages (s.99). Cybercrimes Act: up to 5, 10 or 15 years' imprisonment depending on offence (s.19) |
| Accountability roles | POPIA: **Information Officer** (the head of the body by default) must be registered with the Regulator before taking up duties (s.55(2)); deputies may be designated (s.56). Joint Standard: the **governing body** is ultimately responsible (para 4.1) |
| Key structures | POPIA: 8 conditions for lawful processing (ss.8–25), special personal information and children (ss.26–35), prior authorisation (ss.57–59), codes of conduct (ss.60–68), direct marketing and automated decisions (ss.69–71), transfers (s.72), enforcement (ss.73–99), offences and fines (ss.100–109) |
| Certifiable? | No. Regulator-approved sector codes of conduct (e.g., banking, credit bureaux) displace prior-authorisation duties (s.57(3)) and set sector complaint handling |

## What it is

POPIA gives effect to the constitutional right to privacy (s.14 of the Constitution) by setting minimum conditions for processing personal information, creating an independent Information Regulator, and providing data-subject rights and remedies. Its design tracks the EU Data Protection Directive/GDPR lineage (conditions, special categories, transfer restrictions, a supervisory authority) but with South African particulars: it protects **juristic persons** as well as natural persons, contains a specific **account-number** offence, and hands the Regulator a dual mandate with the Promotion of Access to Information Act (PAIA). Enacted in 2013, it lay largely dormant until the President proclaimed the operative sections into force on 1 July 2020, with a one-year transition (s.114(1)) that ended on 30 June 2021.

The **Cybercrimes Act** is the criminal-law companion: it codifies cyber offences (unlawful access, interception, interference, cyber fraud/forgery/extortion, malicious communications), creates investigation and preservation powers, provides for a designated Point of Contact, and — in a section not yet commenced — imposes a 72-hour offence-reporting duty on electronic communications service providers and financial institutions.

For the financial sector, the FSCA and Prudential Authority have layered **Joint Standard 1 of 2023** (IT governance and risk management, effective 15 November 2024) and **Joint Standard 2 of 2024** (cybersecurity and cyber resilience, effective 1 June 2025) on top of POPIA — a DORA-like prudential regime with board accountability, testing cadences and a material-incident notification clock.

## Who it covers / Scope

| Test | POPIA position |
|---|---|
| Material scope (s.3(1)(a)) | Personal information entered in a record by automated means, or by non-automated means where it forms (or is intended to form) part of a filing system |
| Territorial scope (s.3(1)(b)) | Responsible party **domiciled** in the Republic; or not domiciled but **using means in the Republic** — unless those means are used only to forward information through the Republic |
| "Personal information" (s.1) | Information relating to an identifiable, living natural person and, where applicable, an identifiable, existing **juristic person** |
| Responsible party / operator (s.1) | Responsible party = determines purpose and means (controller). Operator = processes for a responsible party under contract or mandate without coming under its direct authority (processor) |
| Exclusions (ss.6–7) | Purely personal or household activity; information de-identified so it cannot be re-identified; certain national-security, law-enforcement and prosecution processing by public bodies where legislation provides adequate safeguards; Cabinet and provincial executive councils; judicial functions of courts; journalistic, literary or artistic expression (with a code-of-ethics carve-out) |
| Precedence (s.3(2)) | POPIA overrides materially inconsistent legislation, but more extensive processing conditions in other laws prevail |
| Exemptions (s.37) | Regulator may, by Gazette notice, exempt processing that would otherwise breach a condition where the s.37(1) circumstances are met; the s.37(1) exemption application form is published on the Regulator's forms page |

The Cybercrimes Act applies to any person; its s.54 duty is limited to **electronic communications service providers** (licensed or exempted under the Electronic Communications Act 2005, including operators of exempt private networks) and **financial institutions** as defined in the Financial Sector Regulation Act 2017. Joint Standard 2 of 2024 applies to "financial institutions" as defined in the standard, with group-wide coverage obligations for banks and insurers (paras 3.2–3.3) and proportionality by nature, size, complexity and risk profile (para 3.4).

## Core obligations

### The eight conditions (s.4) and the provisions behind them

| Condition | Sections | Substance |
|---|---|---|
| 1 Accountability | s.8 | Responsible party must ensure all conditions are met at the time purpose and means are determined and throughout processing |
| 2 Processing limitation | ss.9–12 | Lawful, minimal, with a justification (consent, contract, legal obligation, legitimate interest, public-law duty); objection rights (Form 1); collection directly from the data subject |
| 3 Purpose specification | ss.13–14 | Specific, explicitly defined purpose; **retention** no longer than necessary unless required by law, reasonably required for lawful purposes, required by contract, or consented to (s.14(1)); destroy/de-identify thereafter |
| 4 Further processing limitation | s.15 | Further processing must be compatible with the original purpose |
| 5 Information quality | s.16 | Complete, accurate, not misleading, updated where necessary |
| 6 Openness | ss.17–18 | Maintain documentation of all processing operations per PAIA ss.14/51 (the PAIA manual); notify data subjects of source, identity, purpose, voluntariness, consequences and recipients (s.18) |
| 7 Security safeguards | ss.19–22 | See below |
| 8 Data subject participation | ss.23–25 | Access (s.23); correction or deletion of information, or destruction of the record (s.24, Form 2); manner of access (s.25) |

### Security safeguards and breach notification (ss.19–22)

- **s.19(1)** — secure integrity and confidentiality with **appropriate, reasonable technical and organisational measures** against loss, damage, unauthorised destruction, and unlawful access or processing.
- **s.19(2)** — a four-step risk cycle: identify all reasonably foreseeable internal and external risks; establish and maintain safeguards; **regularly verify** they are effectively implemented; **continually update** them in response to new risks or deficiencies.
- **s.19(3)** — have due regard to generally accepted information security practices and any industry or professional rules. Enforcement notices have cited ISO/IEC 27001-family practice under this limb; see [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md).
- **s.20** — operators process only with the responsible party's knowledge or authorisation and keep information confidential. **s.21(1)** — a **written contract** must bind the operator to the s.19 measures; **s.21(2)** — the operator must notify the responsible party **immediately** on reasonable grounds to believe personal information has been accessed or acquired by an unauthorised person.
- **s.22** — where there are reasonable grounds to believe personal information has been accessed or acquired by an unauthorised person, notify **the Regulator and the data subject** (unless identity cannot be established) **as soon as reasonably possible** after discovery, allowing only for legitimate law-enforcement needs and measures needed to scope the compromise and restore system integrity (s.22(2)). Data-subject notification may be delayed only if a law-enforcement body or the Regulator determines it would impede a criminal investigation (s.22(3)). Notice must be in writing by post, e-mail, prominent website notice, news media, or as the Regulator directs (s.22(4)), and must include possible consequences, measures taken or intended, recommended data-subject mitigations, and, if known, the identity of the unauthorised person (s.22(5)). The Regulator can order publicity (s.22(6)).

Regulator practice on s.22:

| Point | Regulator position |
|---|---|
| Threshold | "POPIA does not have a threshold for reporting of security compromises. All security compromises must be reported irrespective of the deemed level of risk" (Regulator FAQ). A compromise includes intentional or accidental loss, sharing or destruction, and incidents at an operator, which the responsible party reports |
| Channel | Form SCN1 with published guidelines; from **1 April 2025** reporting through the eServices portal is **mandatory** (media statement, 7 April 2025) — the organisation and its Information Officer must already be registered on the portal |
| Content | Date of compromise, date reported, explanation for any delay, type, description, categories of personal information, number of data subjects, notification method to data subjects, consequences, remediation, recommendations, identity of the intruder if known |

See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md); log entries with [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).

### Governance: Information Officer and compliance framework

| Duty | Source |
|---|---|
| Encourage and ensure compliance; handle requests; work with the Regulator on investigations | s.55(1) |
| Register with the Regulator **before** taking up duties (portal registration; the Regulator states registration is a duty of the responsible party) | s.55(2); Guidance Note on Information Officers (1 April 2021) |
| Ensure a **compliance framework** is developed, implemented, monitored and maintained; a **personal information impact assessment (PIIA)** is done; a PAIA manual is maintained; internal request-handling measures exist; internal awareness sessions are held | Regulations 2018, reg 4(1) |
| Designate deputy information officers as needed | s.56 |

The PIIA is the South African analogue of a DPIA — see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md).

### Special personal information, children, prior authorisation, marketing, automated decisions, transfers

| Topic | Rule |
|---|---|
| Special personal information (ss.26–33) | Prohibited absent a s.27 ground (consent, legal claims, international public law, research with safeguards, etc.) or a specific authorisation: religious/philosophical beliefs, race or ethnic origin, trade-union membership, political persuasion, **health or sex life**, **biometric information**, criminal behaviour. Regulator authorisation may be sought under s.27(2) (application form published) |
| Children (ss.34–35) | Processing of a child's personal information is prohibited unless a s.35 ground applies (competent-person consent, etc.) or the Regulator authorises it |
| Prior authorisation (ss.57–59) | Required before: linking unique identifiers across responsible parties; processing criminal-behaviour or objectionable-conduct information for third parties; **credit reporting**; transferring special or children's information to a foreign country without adequate protection. Regulator must say within **four weeks** whether it will investigate further; investigation capped at **13 weeks**; processing must be suspended meanwhile (s.58(2); the Regulator first set 1 July 2021, then by amending notice of 25 June 2021 determined **1 February 2022** as the date from which s.58(2) applies to processing already under way, per s.114(3)); failure to notify is an offence (s.59). Not required where an approved code of conduct applies (s.57(3)) |
| Direct marketing by electronic means (s.69) | Prohibited unless the data subject consented or is an existing customer (own similar products, opt-out at collection and in every message); a non-customer may be approached **only once** for consent, in the prescribed form (**Form 4**, reg 6). Every message must identify the sender and give an opt-out address. The Regulator's Guidance Note on Direct Marketing (3 December 2024) requires the Form 4 content in any channel (recorded call if by telephone). The Regulator stated on 21 April 2026 that the Consumer Protection Act Amendment Regulations gazetted 15 April 2026 (opt-out registry against unsolicited marketing) do not displace s.69 consent |
| Automated decision-making (s.71) | No decision with legal or substantial effect based solely on automated profiling (work performance, creditworthiness, reliability, location, health, preferences, conduct) unless contract-related with protective measures or governed by law/code; data subject must be able to make representations and receive the underlying logic |
| Cross-border transfers (s.72) | Transfer to a third party in a foreign country only if: the recipient is bound by law, **binding corporate rules** or a **binding agreement** giving substantially similar protection including onward-transfer limits; or consent; or contractual necessity; or the data subject's benefit where consent is impracticable but likely. No adequacy list is published by the Regulator |
| Codes of conduct (ss.60–68) | Regulator-issued sector codes; Banking Association (BASA) and Credit Bureau Association (CBA) codes approved 16 September 2022, gazetted 7 October 2022 (GN 2601–2602), effective 4 November 2022, review due 4 November 2027; proposed codes for research (May 2023), direct marketing (DMASA, June 2023) and residential communities (RCC, September 2023); the Regulator's **own-initiative** code on processing at gated accesses was published for comment on 30 April 2026 (GN 7415, GG 54594), with the comment period extended in May 2026 |

## Enforcement and penalties

| Mechanism | Detail |
|---|---|
| Complaints and own-initiative assessments | Any person may complain (s.74, Form 5); Regulator may assess compliance on its own initiative (s.89) and issue information notices (s.90) |
| Enforcement notice (s.95) | Orders specified steps within a period, or a stop on processing; contains reasons and appeal rights; normally not enforceable until the appeal period expires, but urgent notices can require compliance after **3 days** (s.95(4)–(5)). Appeal to the High Court within **30 days** (s.97(1)) |
| Offences (ss.100–106) | Obstructing the Regulator; breach of confidentiality; obstructing a warrant; **failing to comply with an enforcement notice** (s.103(1)); false statements in response to an information notice; witness offences; unlawful obtaining, disclosure or sale of an **account number** (ss.105–106) |
| Criminal penalties (s.107) | Up to **10 years'** imprisonment and/or a fine for ss.100, 103(1), 104(2), 105(1), 106(1), (3), (4); up to **12 months** for ss.59, 101, 102, 103(2), 104(1). Magistrates' courts may impose any s.107 penalty (s.108) |
| Administrative fines (s.109) | Infringement notice for an alleged offence; fine **not exceeding R10 million** (Minister may CPI-adjust, s.109(10)); infringer has **30 days** to pay, arrange instalments or elect trial; factors include nature of information, duration, number of data subjects, public importance, likelihood of damage or distress, preventability, **failure to carry out a risk assessment or operate good policies**, and prior offences (s.109(3)); an unpaid fine can be filed as a civil judgment (s.109(5)) |
| Civil remedies (s.99) | Data subject (or the Regulator on request) may sue for damages **whether or not there is intent or negligence**; courts may award patrimonial and non-patrimonial loss, aggravated damages and interest; defences include vis major, plaintiff consent or fault, and compliance not reasonably practicable |

Enforcement record (Regulator publications):

| Date | Matter | Significance |
|---|---|---|
| 9 May 2023 / 3 Jul 2023 | Department of Justice and Constitutional Development — enforcement notice after the September 2021 ransomware attack, then an infringement notice with a **R5 million** administrative fine | Findings under s.19(1)–(3) and s.22(1): SIEM, intrusion-detection and anti-virus licences expired in 2020; no PIIA or compliance framework; 31-day remediation orders. The fine was the first published s.109 fine and was imposed for failing to comply with the enforcement notice |
| 5 Feb 2024 | Dis-Chem Pharmacies — enforcement notice (brute-force attack at operator Grapevine) | No written operator contract (s.21(1)), inadequate safeguards and verification (s.19), failure to notify data subjects (s.22(1)(b)) |
| 21 Feb 2024 | FT Rams Consulting — enforcement notice | The Regulator's **first enforcement notice arising from a direct-marketing complaint**: persistent unsolicited marketing e-mail to a data subject who had opted out, contrary to s.69(1)–(2) |
| Nov–Dec 2024 | Department of Basic Education — enforcement notice on newspaper publication of matric results; **R5 million** infringement notice (23 Dec 2024) | A full bench of the Pretoria High Court set both notices aside in December 2025; the Regulator applied for leave to appeal (31 Dec 2025) and the matter was before the Supreme Court of Appeal in August 2026 — treat the notices' status as contested |
| 16 Apr 2025 | WhatsApp — enforcement notice under s.95 (listed on the Regulator's enforcement-notices register) | A cross-border platform brought under the Act; the published notice is a scanned image whose text is not machine-readable, so its findings are not summarised here (verify) |
| Apr 2026 | Blouberg Local Municipality — s.109(5) court confirmation | Polokwane High Court confirmed an administrative fine but reduced it from R500,000 to **R250,000** (single data subject, corrective action taken, first offence) — the first published judicial calibration of a POPIA fine |
| 22 May 2026 | Central Johannesburg TVET College — enforcement notice | Unlawful sharing of special personal information (criminal records) and failure to notify a security compromise under s.22 |

The Regulator also enforces PAIA (s.77J notices, e.g., Sibanye Stillwater and Gauteng Department of Health, June 2026) — the same body assesses both privacy and access-to-information compliance.

### Cybercrimes Act offences and duties

| Provision | Content |
|---|---|
| ss.2–11 | Unlawful access; unlawful interception of data; unlawful acts in respect of software or hardware tools; unlawful interference with data or a computer program; unlawful interference with a storage medium or computer system; unlawful acquisition, possession, provision, receipt or use of passwords, access codes or similar data; cyber fraud; cyber forgery and uttering; cyber extortion; **aggravated offences** against a "restricted computer system" — one under the control of, or exclusively used by, a financial institution or an organ of state (including a court) and protected by security measures |
| ss.14–16 | Malicious communications: data messages inciting damage or violence, threatening damage or violence, or disclosing intimate images |
| s.19 | Penalties: up to **5 years** (ss.2(1)–(2), 3(3), 7(2)); up to **10 years** (ss.3(1)–(2), 4(1), 5(1), 6(1), 7(1)); up to **15 years** for aggravated offences (s.11(1)); commission by electronic means and extent of loss are aggravating factors |
| s.24 | Jurisdiction of South African courts over Part I and Part II offences with a South African nexus |
| s.52 | Designated Point of Contact within SAPS to give immediate assistance in cybercrime investigations (Chapter 6 — **not included** in the 1 December 2021 commencement) |
| **s.54** | ECSPs and financial institutions aware that their service or network is involved in prescribed Part I offences must report to SAPS **without undue delay and, where feasible, not later than 72 hours** after becoming aware, and preserve evidence; the categories of offences and the form of report are to be prescribed by the Minister of Police (s.54(2)). **Not yet in force** — excluded from the 1 December 2021 commencement, and the Act's official commencement record still lists only that proclamation as of September 2026 |

### Joint Standard 2 of 2024 (financial institutions)

| Paragraph | Requirement |
|---|---|
| 4–5 | Governing body ultimately responsible for compliance and cyber-risk oversight; security roles in third-party contracts/SLAs; dedicated, adequately resourced cyber and information-security function with access to the governing body; regulator may require an independent oversight function |
| 6 | Governing-body-approved cybersecurity **strategy** (reviewed at least annually) and **framework** aligned to enterprise risk management (reviewed at least annually) |
| 7 | Identify (7.1): information-asset inventory reviewed at least **biennially**; security risk assessments on critical operations. Protect (7.2): defence-in-depth controls, cryptographic-key backups, and a cybersecurity awareness programme with refresher training at least **annually**. Detect (7.3), response and recovery (7.4, including a backup strategy with encrypted media stored offline or offsite), incident response and management (7.5). Testing (7.7): regular vulnerability assessments (7.7.2); **penetration testing** of critical systems, and of internet-facing systems on major change or at least **annually** (7.7.3); **scenario-based simulation exercises** including adversarial attack-and-defence, designed from threat intelligence (7.7.4) |
| 8–9 | Cybersecurity hygiene practices (8.1–8.7: access management, privileged access, MFA, network perimeter defence, vulnerability and patch management, secure configurations, malware protection); notify the responsible authority, in the form and manner determined, after classifying a cyber incident or information-security compromise as **material** (9.1) |
| Joint Notice 2 of 2026 (31 Aug 2026, effective 1 Sep 2026) | Material incident = disruption with severe and widespread impact on operations, customers or the financial system. Template submission: immediate notification (contact details and incident details tabs) **within 24 hours** of classifying an incident as material — separately for Joint Standard 1 of 2023 IT incidents and Joint Standard 2 of 2024 cyber and information-security incidents; subsequent update (impact tab) **within 14 calendar days** of that notification; the full report — all tabs plus the final investigation report — on timelines agreed with the responsible authority. Banks, mutual banks and insurers file via the Prudential Authority's Umoja portal; CIS managers, market infrastructures, FSPs, pension funds and administrators, OTC derivative providers and credit rating agencies via the FSCA Joint Standards Submission Portal. The Prudential Authority intends to withdraw Directive 2 of 2019 (banks) |

## Timeline and status

| Date | Event |
|---|---|
| 26 Nov 2013 | POPIA assented to and gazetted |
| 11 Apr 2014 | s.1, Part A of Chapter 5 (ss.39–54, the Regulator) and ss.112–113 commenced (GG 37544) |
| 14 Dec 2018 | POPIA Regulations (GN R.1383, GG 42110) |
| 1 Jul 2020 | ss.2–38, 55–109, 111, 114(1)–(3) commenced (Proclamation R.21, GG 43461, 22 Jun 2020) |
| 30 Jun 2021 | ss.110 and 114(4) commenced; one-year transition ends |
| 1 Jul 2021 | Transition period over; the Act fully enforceable |
| 1 Dec 2021 | Cybercrimes Act partially commenced (Proclamation in GG 45562, 30 Nov 2021): Chapters 1, 3, 7; Chapter 2 excluding Part VI; Chapter 4 excluding ss.38(1)(d)–(f), 40(3)–(4), 41–44; Chapter 8 **excluding s.54**; Chapter 9 excluding certain Sexual Offences Act amendments |
| 1 Feb 2022 | s.58(2) (suspension pending prior-authorisation review) becomes applicable to processing already under way (GN 560, GG 44761, 25 Jun 2021, amending GN 297, GG 44383, 1 Apr 2021, which had set 1 Jul 2021) |
| 4 Nov 2022 | BASA and CBA codes of conduct take effect (approved 16 Sep 2022; GN 2601–2602, 7 Oct 2022) |
| 10 Nov 2023 | Joint Standard 1 of 2023 (IT governance and risk management) published |
| 17 May 2024 | Joint Standard 2 of 2024 published (Joint Communication 2 of 2024) |
| 15 Nov 2024 | Joint Standard 1 of 2023 (IT governance and risk management) effective |
| 3 Dec 2024 | Guidance Note on Direct Marketing |
| 1 Apr 2025 | eServices portal mandatory for security-compromise reports |
| 1 Jun 2025 | Joint Standard 2 of 2024 effective |
| 26 Sep 2025 | Draft Regulations on processing of health or sex-life information under s.112(2)(c) published for comment (GN 6673, GG 53426; comments closed 10 Oct 2025) — no final regulations on the Regulator's gazette register as of September 2026 |
| Dec 2025 – Aug 2026 | High Court sets aside DBE notices; Regulator appeals; SCA proceedings pending |
| 15 Apr 2026 | Consumer Protection Act Amendment Regulations (unsolicited-marketing opt-out) gazetted |
| 30 Apr 2026 | Regulator's own-initiative code of conduct on processing at gated accesses published for comment (GN 7415, GG 54594) |
| 31 Aug 2026 / 1 Sep 2026 | Joint Notice 2 of 2026 issued / takes effect |

No amendment to POPIA's text appears on the official commencement or gazette records as of September 2026. The Cybercrimes Act's commencement record still shows only the 1 December 2021 proclamation, so s.54, Chapter 5 (mutual assistance), Chapter 6 (designated Point of Contact) and ss.41–44 remain uncommenced. Pending as of September 2026: the DBE appeal before the Supreme Court of Appeal, the final s.112(2)(c) health/sex-life regulations, the gated-access code of conduct, and the Prudential Authority's stated intention to withdraw Directive 2 of 2019 for banks.

## Key obligations for security/GRC teams

1. **Scope the entity**: confirm responsible-party vs operator roles per processing activity, territorial reach (s.3), juristic-person data, and whether a sector code or Joint Standard applies. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Register the Information Officer** (and deputies) on the Regulator's portal before they act; keep the PAIA manual current — registration is a precondition for portal breach reporting.
3. **Run and document the s.19(2) cycle**: risk identification, safeguards, regular verification, continual update — enforcement notices treat lapsed licences and untested controls as s.19 breaches. Anchor to a recognised standard to satisfy s.19(3). See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
4. **Complete a PIIA and compliance framework** (reg 4) and maintain them as living documents; see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
5. **Paper every operator**: written contracts carrying s.19 measures and an immediate-notification clause (s.21); Dis-Chem shows that a missing contract is itself a finding. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **Build the s.22 playbook**: no materiality threshold, "as soon as reasonably possible", eServices portal, Form SCN1 content, data-subject notice channels, law-enforcement delay authority; for financial institutions add the 24-hour / 14-day Joint Standard template and the correct portal. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
7. **Control marketing, profiling and transfers**: Form 4 consent capture, once-only approach, opt-out in every message, records of consent; assess automated decisions against s.71; map foreign recipients and choose a s.72 mechanism (binding agreement or BCRs), with prior authorisation for special or children's data going to countries without adequate protection. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
8. **Board reporting for financial institutions**: governing-body approval of strategy and framework, annual reviews, penetration-test and simulation results, material-incident log. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
9. **Watch the horizon**: s.54 commencement, the final health/sex-life regulations, the DBE appeal (scope of Regulator powers), and the gated-access and other codes of conduct. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **GDPR** ([gdpr.md](gdpr.md)): POPIA is close enough in structure that a GDPR programme maps onto it, with deltas — juristic-person data, no fixed 72-hour clock but no materiality threshold either, Information Officer registration, prior authorisation for credit reporting and identifier linking, an account-number offence, and no adequacy list (rely on binding agreements/BCRs under s.72). South Africa is not the subject of an EU adequacy decision; EU-to-SA transfers still need GDPR Chapter V tools.
- **DORA / NIS2** ([dora.md](dora.md), [nis2.md](nis2.md)): Joint Standards 1 of 2023 and 2 of 2024 are the South African prudential counterpart to DORA — governing-body accountability, testing cadences, material-incident notification with a fixed template. Groups regulated in both jurisdictions should harmonise incident classification so one triage feeds both clocks.
- **Cybercrimes Act vs POPIA**: a single intrusion can trigger POPIA s.22 (Regulator and data subjects), Joint Standard notification (Authorities), a criminal complaint to SAPS, and — once s.54 commences — a mandatory 72-hour SAPS report for ECSPs and financial institutions. Preserve evidence for all four.
- **PAIA and the Consumer Protection Act**: the same Regulator enforces access-to-information duties, the PAIA manual is the POPIA s.17 documentation record and PAIA annual reports are a recurring filing; the 2026 CPA opt-out registry sits alongside, not instead of, s.69 consent. Other African and emerging-market regimes are summarised in [other-jurisdictions.md](other-jurisdictions.md); framework mapping via [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- POPIA, Act 4 of 2013 (legal text, GG 37067): https://www.gov.za/sites/default/files/gcis_document/201409/3706726-11act4of2013protectionofpersonalinforcorrect.pdf ; commencement record: https://www.gov.za/documents/protection-personal-information-act ; Proclamation R.21 of 2020 (GG 43461): https://www.gov.za/documents/protection-personal-information-act-commencement-certain-sections-22-jun-2020-0000 ; s.58(2) determination, GN 297, GG 44383, 1 Apr 2021: https://www.gov.za/documents/protection-personal-information-act-commencement-section-582-1-apr-2021-0000 ; amending notice GN 560, GG 44761, 25 Jun 2021 (1 February 2022): https://inforegulator.org.za/wp-content/uploads/2020/07/20210625-gg44761gon560-POPIA-S58-2.pdf
- Regulations relating to the Protection of Personal Information, 2018 (GN R.1383, GG 42110): https://inforegulator.org.za/wp-content/uploads/2020/07/20181214-gg42110-rg10897-gon1383-POPIA-Regulations-1.pdf
- Information Regulator indexes (regulator guidance): POPIA and FAQ https://inforegulator.org.za/popia/ ; forms https://inforegulator.org.za/popia-forms/ ; guidance notes https://inforegulator.org.za/guidance-notes/ ; codes of conduct https://inforegulator.org.za/codes-of-conduct/ ; gazette register https://inforegulator.org.za/government-gazettes/ ; enforcement notices https://inforegulator.org.za/enforcement-notices/ ; media statements https://inforegulator.org.za/media-statements/
- Guidelines on completing a s.22 security compromise notification: https://inforegulator.org.za/wp-content/uploads/2020/07/Guidelines-on-completing-a-Security-Compromise-Notification-ito-Section-22-POPIA.pdf ; eServices portal guide: https://eservices.inforegulator.org.za/compromises/docs/guide.pdf ; portal mandatory from 1 Apr 2025 (media statement, 7 Apr 2025): https://inforegulator.org.za/wp-content/uploads/2025/04/MEDIA-STATEMENT-INVITATION-TO-REPORT-SECURITY-COMPROMISES-THROUGH-THE-eSERVICES-PORTAL-.pdf
- Guidance notes: Information Officers (1 Apr 2021): https://inforegulator.org.za/wp-content/uploads/2025/07/Guidance_Note_on_Information_Officers_.pdf ; Guidance Note on Direct Marketing (3 Dec 2024): https://inforegulator.org.za/wp-content/uploads/2020/07/GUIDANCE-NOTE-ON-DIRECT-MARKETING-IN-TERMS-OF-THE-PROTECTION-OF-PERSONAL-INFORMATION-ACT-4-OF-2013-POPIA.pdf
- Enforcement record: DoJ&CD enforcement notice https://inforegulator.org.za/wp-content/uploads/2020/07/ENFORCEMENT-NOTICE-DOJCD-MATTER-090523.pdf and R5m infringement statement https://inforegulator.org.za/wp-content/uploads/2020/07/MEDIA-STATEMENT-INFRINGEMENT-NOTICE-ISSUED-TO-THE-DEPARTMENT-OF-JUSTICE-AND-CONSTITUTIONAL.pdf ; Dis-Chem https://inforegulator.org.za/wp-content/uploads/2020/07/DIS-CHEM-ENFORCEMENT-NOTICE.pdf ; FT Rams https://inforegulator.org.za/wp-content/uploads/2020/07/MEDIA-STATEMENT-ENFORCEMENT-NOTICE-ON-DIRECT-MARKETING-COMPLAINT.pdf ; DBE infringement https://inforegulator.org.za/wp-content/uploads/2025/01/Media-Statement-Infringement-Notice-DBE.pdf and appeal https://inforegulator.org.za/wp-content/uploads/2026/01/MEDIA-STATEMENT-THE-REGULATOR-APPEALS-THE-JUDGEMENT-ON-PUBLICATION-OF-MATRIC-RESULTS-31-DEC-2025.pdf ; Blouberg https://inforegulator.org.za/wp-content/uploads/2026/04/INFORMATION-REGULATOR-TURNS-TO-THE-COURTS-TO-FINE-BLOUBERG-LOCAL-MUNICIPALITY-FOR-CONTRAVENTION-OF-POPIA_.pdf ; CJC and Sibanye https://inforegulator.org.za/wp-content/uploads/2026/06/MEDIA-STATEMENT-INFORMATION-REGULATOR-ISSUES-ENFORCEMENT-NOTICES-FOR-THE-CONTRAVENTIONS-OF-POPIA-AND-PAIA-BY-PUBLIC-AND-PRIVATE-BODIES.pdf . The WhatsApp enforcement notice of 16 Apr 2025 (https://inforegulator.org.za/wp-content/uploads/2025/04/WHATS-APP-ENFORCEMENT-NOTICE.pdf) is a scanned image and its text could not be read.
- Draft s.112(2)(c) health/sex-life regulations (GN 6673, GG 53426, 26 Sep 2025): https://inforegulator.org.za/wp-content/uploads/2025/10/SECTION-112_2_C_-HEALTH-REGULATIONS-FINAL-1.pdf ; gated-access code notice (GN 7415, GG 54594, 30 Apr 2026): https://inforegulator.org.za/wp-content/uploads/2026/04/GG-NOTICE-CODE-OF-CONDUCT-ON-GATED-ACCESSES-WITH-COMMENTS-20.3.2026.pdf ; Consumer Protection Act regulations statement (21 Apr 2026): https://inforegulator.org.za/wp-content/uploads/2026/04/MEDIA-STATEMENT-REGULATOR-NOTES-PUBLISHED-GAZETTE-OF-THE-CONSUMER-PROTECT-ACT-AMENDMENT-REGULATIONS-2026.pdf
- Cybercrimes Act 19 of 2020 (legal text, GG 44651): https://www.gov.za/sites/default/files/gcis_document/202106/44651gon324.pdf ; commencement record (Proclamation in GG 45562, 30 Nov 2021): https://www.gov.za/documents/cybercrimes-act-19-2020-1-jun-2021-0000
- Joint Standard 2 of 2024 with Joint Communication 2 of 2024, Statement of Need and Consultation Report (publisher documents, FSCA document store): https://www.fsca.co.za/_api/cr3ad_noticedocumentses(ce8f1c99-399f-f111-b8dc-7c1e52fc9f22)/cr3ad_document/$value ; Joint Notice 2 of 2026 with Joint Communication 5 of 2026, the reporting template and Comments Report (publisher documents, FSCA): https://www.fsca.co.za/_api/cr3ad_noticedocumentses(bd4abdb6-dba6-f111-b8dd-7ced8d48cf36)/cr3ad_document/$value ; FSCA standards and notices landing page: https://www.fsca.co.za/Supervisory-Information

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
