# UK data protection — UK GDPR, Data Protection Act 2018, Data (Use and Access) Act 2025 and PECR

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **UK GDPR** — Regulation (EU) 2016/679 as retained in UK law and amended (legislation.gov.uk/eur/2016/679); **Data Protection Act 2018** (2018 c. 12, "DPA 2018"); **Data (Use and Access) Act 2025** (2025 c. 18, "DUAA") — an amending Act that changes, but does not replace, UK GDPR, DPA 2018 and PECR; **Privacy and Electronic Communications (EC Directive) Regulations 2003** (SI 2003/2426, "PECR") |
| Regulator | Information Commissioner's Office (ICO). On **30 September 2026** the office of Information Commissioner is abolished and its functions transfer to the **Information Commission**, a body corporate (DPA 2018 s. 114A; DUAA ss. 117–119; SI 2026/1015). The regulator keeps using the name "ICO" |
| Status and key dates | DPA 2018 Royal Assent 23 May 2018; UK GDPR is the EU text as it stood at IP completion day (31 December 2020, 11 pm), kept up to date with UK amendments (initially via SI 2019/419); DUAA Royal Assent 19 June 2025, data-protection provisions commenced in tranches from 19 June 2025 to 19 June 2026 (main tranche **5 February 2026**) |
| Who is covered | Controllers and processors established in the UK (UK GDPR Art. 3(1)); non-UK organisations offering goods or services to, or monitoring the behaviour of, people in the UK (Art. 3(2)), which must appoint a UK representative (Art. 27); PECR covers electronic direct marketing, storage of/access to information on terminal equipment (cookies etc.) and public electronic communications service providers |
| Structure | UK GDPR = general processing; DPA 2018 Part 2 supplements it (exemptions, special-category conditions), Part 3 = law enforcement processing, Part 4 = intelligence services, Parts 5–7 = Commissioner, enforcement, supplementary; PECR is enforced through DPA 2018 Parts 5–7 as modified by PECR Sch. 1 |
| Breach clocks | 72 hours to the ICO (UK GDPR Art. 33(1)); processor to controller without undue delay (Art. 33(2)); high-risk breaches to individuals without undue delay (Art. 34); PECR service-provider breaches also 72 hours since 20 August 2025 (was 24 hours) |
| Penalties | **Higher maximum** £17,500,000 or 4% of total worldwide annual turnover, whichever is higher; **standard maximum** £8,700,000 or 2% (UK GDPR Art. 83(4)–(6); DPA 2018 s. 157). PECR infringements on or after 5 February 2026 attract the same two tiers (previously capped at £500,000 — verify) |
| Certifiable? | No mandatory certification. ICO compliance is evidenced by accountability records, audits/assessment notices and codes of practice; UK GDPR codes of conduct and certification schemes are voluntary |
| Relationship to neighbours | Structurally almost identical to EU GDPR (see [gdpr.md](gdpr.md)); DUAA introduces targeted divergences. EU adequacy decisions for the UK renewed 19 December 2025, expiring 27 December 2031. Cyber-resilience duties sit in the NIS Regulations 2018 (SI 2018/506), which the pending Cyber Security and Resilience Bill will reform |

## What it is

The UK regime is EU GDPR frozen at Brexit and then edited domestically. The DPA 2018 was enacted to sit alongside EU GDPR; at IP completion day the EU text was converted into "UK GDPR" and the DPA 2018 was re-pointed at it. The result is one merged framework: UK GDPR carries the principles, lawful bases, rights and controller/processor duties, while the DPA 2018 supplies the exemptions, special-category conditions, the law-enforcement and intelligence-services regimes, the regulator and the enforcement machinery.

The **Data (Use and Access) Act 2025** is the first substantive post-Brexit reform. It is an amending Act: it inserts new articles into UK GDPR (recognised legitimate interests, a statutory "applicable time period" for rights requests, Articles 22A–22D on automated decision-making, Articles 45A–45B on transfers), adds a complaints duty and new investigatory powers to the DPA 2018, rewrites PECR's cookie rule and enforcement regime, and restructures the regulator into the Information Commission. The ICO's own framing is that most changes are permissive ("an opportunity to do things differently") with two genuinely new duties for organisations: a data-protection complaints process and explicit consideration of children's needs when designing online services.

PECR is the UK implementation of the ePrivacy Directive. It is narrower than UK GDPR (marketing calls/emails/texts, cookies and similar technologies, communications-provider security and breach reporting) but, after DUAA, carries UK-GDPR-level fines.

## Who it covers / Scope

| Test | Rule | Practical notes |
|---|---|---|
| UK establishment | UK GDPR Art. 3(1): processing in the context of the activities of a UK establishment of a controller or processor, wherever the processing takes place | A UK branch or subsidiary brings the processing it directs into scope even if servers sit abroad |
| Targeting the UK | Art. 3(2): non-UK controllers/processors offering goods or services (paid or free) to data subjects in the UK, or monitoring behaviour that takes place in the UK | Must designate a UK representative in writing (Art. 27), subject to the Art. 27(2) exemptions |
| DPA 2018 territorial rule | s. 207: for processing outside Part 2, applies where carried out in the context of a UK establishment | Governs Parts 3–4 and the enforcement provisions |
| Public authorities | May not rely on legitimate interests or recognised legitimate interests when performing their tasks (Art. 6(1), final subparagraph) | Public-task basis (Art. 6(1)(e)) instead |
| Law enforcement / intelligence | DPA 2018 Part 3 (competent authorities, based on the EU Law Enforcement Directive) and Part 4 (intelligence services) | Separate principles, rights and transfer rules; not covered further here |
| PECR | Applies to anyone sending electronic direct marketing to UK subscribers, anyone storing or accessing information on a user's terminal equipment (reg. 6), and providers of public electronic communications services (regs. 5–5C) | Reg. 6 is technology-neutral: any storage of, or access to, information on terminal equipment, including instigating it, not only cookies |

The transfer and core processing rules apply to organisations of every size, including sole traders and self-employed individuals (ICO).

## Core obligations

### Where UK GDPR now diverges from EU GDPR (DUAA changes, in force unless stated)

| Topic | Provision | UK rule |
|---|---|---|
| Recognised legitimate interests | UK GDPR Art. 6(1)(ea), Art. 6(5)–(9), Annex 1 (DUAA s. 70, Sch. 4) — from 5 Feb 2026 | New lawful basis with **no balancing test** where processing is necessary for an Annex 1 condition: disclosures to a person who states it needs the data for a public-interest/official-authority task; national security, public security and defence; emergencies (Civil Contingencies Act 2004 meaning); detecting, investigating or preventing crime, or apprehending or prosecuting offenders; safeguarding vulnerable individuals. Secretary of State may add cases by regulations. Not available to public authorities performing their tasks |
| Legitimate-interest examples | Art. 6 (DUAA s. 70) | Statutory examples of processing that may be a legitimate interest: direct marketing; intra-group transmission for internal administrative purposes; ensuring the security of network and information systems (NIS Regulations 2018 meaning). Balancing test still required |
| Purpose limitation | Art. 5(1)(b) and Sch. 5 (DUAA s. 71) | Listed re-uses are deemed compatible with the original purpose (including disclosure for archiving in the public interest) without a compatibility test |
| Research | DUAA ss. 67–68, 77, 86 | Statutory definition of research and statistical purposes covering commercial research; "broad consent" to an area of scientific research; privacy notice may be replaced by a published notice where individual notice is a disproportionate effort |
| Rights-request clock | Art. 12(3)–(4) and new Art. 12A (DUAA s. 76) — for requests received on/after 5 Feb 2026 | "Applicable time period" = one month from the latest of receipt of the request, receipt of information requested under Art. 12(6), or payment of any Art. 12(5) fee; extendable by two further months for complexity or number of requests, by notice given within the first month stating reasons. **Stop-the-clock**: time spent waiting for further information the controller reasonably requires to identify the information or processing (e.g. where it holds a large amount of data on the person) does not count |
| DSAR search effort | Art. 15(1A) (DUAA s. 78, in force from Royal Assent) | The data subject is entitled only to what the controller can provide after a **reasonable and proportionate search** |
| Automated decision-making | Arts. 22A–22D replace Art. 22 (DUAA s. 80, Sch. 6) — decisions taken on/after 5 Feb 2026 | See table below |
| Children online | Art. 25(1A)–(1B) (DUAA s. 81) | Providers of information society services likely to be accessed by children must take "children's higher protection matters" into account when deciding technical and organisational measures; the ICO states conformance with its Age Appropriate Design Code (DPA 2018 s. 123) satisfies this |
| International transfers | Arts. 44A, 45A, 45B and Sch. 7 (DUAA s. 85) | Secretary of State approves destinations by regulations if the **data protection test** is met — protection "not materially lower" than UK GDPR and DPA 2018 Part 2 taken as a whole, considering rule of law and human rights, an enforcement authority, redress, onward-transfer rules, international obligations and the country's constitution, traditions and culture. Regulations may be sectoral or transfer-specific (negative procedure) |
| Complaints | DPA 2018 s. 164A (DUAA s. 103) — complaints received on/after 19 June 2026 | Controller must facilitate complaints (e.g. an electronic complaint form), **acknowledge within 30 days**, and respond without undue delay, making enquiries as appropriate and informing the complainant of progress and outcome. Art. 12(4) refusals must now signpost this route as well as the ICO (s. 165). Infringement carries the standard maximum (s. 157(4A)); s. 164B lets regulations require controllers to report complaint volumes to the Commissioner |
| Legal professional privilege / national security | DUAA ss. 79, 88 (in force 5 Sept 2025) | LPP exemption to rights requests under Part 3; revised national security exemption certificates |

### Automated decision-making (UK GDPR Arts. 22A–22D)

| Element | Rule |
|---|---|
| Definitions (Art. 22A) | "Solely automated" = no **meaningful human involvement** (the degree of profiling is relevant); "significant decision" = legal effect or similarly significant effect on the data subject |
| General position | Solely automated significant decisions are permitted on any lawful basis (including legitimate interests) provided the Art. 22C safeguards are in place — a reversal of the EU Art. 22 prohibition-with-exceptions model |
| Restrictions (Art. 22B) | Where the decision is based entirely or partly on special-category data, it may be solely automated only with explicit consent, or where necessary for a contract or under Art. 9(2)(g) substantial public interest. A solely automated significant decision may **not** rely on the recognised-legitimate-interest basis (Art. 6(1)(ea)) |
| Safeguards (Art. 22C) | Measures that inform the individual of such decisions, enable representations, enable human intervention, and enable the decision to be contested |
| Secondary rules (Art. 22D) | Secretary of State may define what counts as meaningful human involvement or a similarly significant effect, and add safeguards (affirmative procedure). ICO began work on a statutory code of practice on AI and automated decision-making in 2026 |

### Breach and incident clocks

| Trigger | Deadline | Source |
|---|---|---|
| Personal data breach likely to result in a risk to individuals | Notify ICO without undue delay and where feasible within **72 hours** of awareness; reasons required if late; information may be provided in phases without undue further delay | UK GDPR Art. 33(1), (4) |
| Processor becomes aware of a breach | Notify the controller without undue delay | Art. 33(2) |
| Breach likely to result in a **high** risk | Inform affected individuals without undue delay | Art. 34 |
| Any breach, reportable or not | Document facts, effects and remedial action | Art. 33(5); ICO expects a breach log |
| Public electronic communications service provider breach | Notify ICO without undue delay and where feasible within 72 hours (reasons if later); notify affected subscribers/users where the breach is likely to adversely affect them; maintain a breach inventory; £1,000 fixed penalty for failing to notify | PECR regs. 5A, 5C (as amended by DUAA s. 111, from 20 Aug 2025) |
| Failure to notify a UK GDPR breach | Fine up to the standard maximum (£8.7m / 2%) plus Art. 58 corrective powers | ICO breach guidance |

Cross-regime timing is tracked in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

### International transfers

| Mechanism | Detail |
|---|---|
| Restricted transfer test | UK GDPR applies to the processing; the UK organisation initiates the transfer; the recipient is a separate legal entity outside the UK (ICO three-step test) |
| UK adequacy regulations (full) | EEA states and EU/EEA institutions; Andorra, Argentina, Faroe Islands, Gibraltar, Guernsey, Isle of Man, Israel, Jersey, New Zealand, Switzerland, Uruguay; Republic of Korea |
| UK adequacy regulations (partial) | Canada (PIPEDA-covered private-sector recipients); Japan (APPI-covered business operators); **United States** — only recipients on the Data Privacy Framework List participating in the **UK Extension to the EU-US DPF** (SI 2023/1028, in force 12 October 2023). Check the certification is active and covers HR/non-HR data; flag special-category and criminal-offence data as "sensitive"; the ICO treats the UK regulations as independent of the EU's own US adequacy finding |
| Appropriate safeguards | ICO International Data Transfer Agreement (IDTA), the UK Addendum to the EU SCCs, UK Binding Corporate Rules — each with a **transfer risk assessment** (TRA) confirming protection is not materially lower after transfer |
| Exceptions | Art. 49 derogations, to be shown necessary and proportionate |
| Inbound from the EEA | Commission adequacy decisions for the UK (GDPR and Law Enforcement Directive) renewed 19 December 2025, valid to 27 December 2031; EDPB opinions adopted 20 October 2025 flagged the new "not materially lower" test and UK onward-transfer rules for monitoring |

### PECR: marketing, cookies and terminal equipment

| Area | Rule (post-DUAA) |
|---|---|
| Electronic mail marketing to individuals (reg. 22) | Prior consent, or the "soft opt-in" (details obtained in a sale/negotiation, similar products/services, refusal offered at collection and in every message). **Charities** may use a soft opt-in for supporters who expressed interest in their purposes (reg. 22(3A), from 5 Feb 2026) |
| Storage/access on terminal equipment (reg. 6, Sch. A1) | Prohibited unless informed consent given (browser settings may signify consent), or an exemption applies: transmission of a communication; **strictly necessary** for a requested service (security, fraud and fault prevention/detection, authentication); **statistical/analytics** collection solely to improve the service, not shared except to assist with that, with information and a free, simple objection route; **website appearance/functionality** preferences with information and an objection route; emergency-assistance geolocation. Secretary of State may add or vary exemptions (reg. 6A) |
| Communications providers (regs. 5–5C) | Security measures, 72-hour breach notification, breach inventory |
| Enforcement (reg. 31, Sch. 1, as substituted by DUAA Sch. 13) | DPA 2018 Parts 5–7 apply: the **higher maximum** for infringements of regs. 5, 6, 7, 8, 14, 19–24 and 32B(4)–(5); standard maximum otherwise. Conduct before 5 Feb 2026 stays under the old regime (SI 2026/82 reg. 11) |

## Enforcement and penalties

| Power | Provision | Notes |
|---|---|---|
| Information notice | DPA 2018 s. 142 | Compels information; non-compliance attracts the higher maximum (s. 157(4)) |
| Assessment notice / audit | s. 146 | Now may require the organisation to commission a **report by an approved person** at its own cost (DUAA s. 98) |
| Interview notice | s. 148A (DUAA s. 100) | Compels current or former staff and managers to attend and answer questions where a failure or offence is suspected |
| Enforcement notice | s. 149 | Orders to do or stop doing something |
| Penalty notice | s. 155, Sch. 16 | Notice of intent first, with at least 21 days for written representations; for notices of intent given on/after 5 Feb 2026 the ICO must issue the penalty notice (or a decision not to) within 6 months or as soon as reasonably practicable after (DUAA s. 101) |
| Fine ceilings | UK GDPR Art. 83(4)–(6); DPA 2018 s. 157 | Higher maximum £17.5m / 4% for principles and consent (Arts. 5–7, 9), rights (Arts. 12–21), ADM restrictions and safeguards (Arts. 22B–22C), transfers (Arts. 44A–49), Sch. 2 Parts 5–6 duties and Commissioner orders; standard maximum £8.7m / 2% for controller/processor obligations under Arts. 8, 11, 25–39, 42–43 (including security, breach notification, records, DPO and processor terms) and the s. 164A complaints duty |
| Fine calculation | ICO Data Protection Fining Guidance (March 2024) | Five steps: seriousness (starting point 20–100% of the statutory maximum for high seriousness, 10–20% medium, 0–10% lower), turnover (percentage figure used once worldwide turnover exceeds £435m / £437.5m), starting point, aggravating/mitigating factors, effectiveness/proportionality check. A separate PECR higher-fines guidance was in development as of June 2026 |
| Civil remedies | ss. 165–168 | Complaints to the ICO (s. 165); orders to progress complaints (s. 166); court compliance orders (s. 167); compensation (s. 168) |
| Criminal offences | ss. 170, 173 | Knowingly or recklessly obtaining, disclosing, procuring, retaining or selling personal data without consent; altering data to prevent disclosure under a rights request |
| Annual reporting | DUAA s. 102 | ICO must publish an annual report on regulatory action; draft enforcement procedural guidance published 2026, final pending |

## Timeline and status

| Date | Event |
|---|---|
| 23 May 2018 | DPA 2018 Royal Assent |
| 31 Dec 2020 | IP completion day — EU GDPR becomes UK GDPR, amended by SI 2019/419 |
| 21 Mar 2022 | IDTA and UK Addendum in force (verify) |
| 12 Oct 2023 | UK–US data bridge: SI 2023/1028 in force |
| Mar 2024 | ICO Data Protection Fining Guidance published |
| 19 Jun 2025 | DUAA Royal Assent; s. 78 (reasonable and proportionate DSAR searches) and s. 66 in force immediately; ss. 69, 82, 96, 97 two months later |
| 20 Aug 2025 | Commencement No. 1 (SI 2025/904): PECR breach clock 72 h (s. 111), special-category provisions (s. 74), ICO duties and codes (ss. 91–93), annual regulatory-action report (s. 102), s. 106 |
| 5 Sep / 17 Nov 2025 | Commencement No. 3 (SI 2025/996): LPP and national-security exemptions (ss. 79, 88); joint intelligence/law-enforcement processing (ss. 89–90) |
| 20 Oct 2025 | EDPB opinions on draft renewed UK adequacy decisions |
| 19 Dec 2025 | Commission adopts renewed UK adequacy decisions (GDPR and LED) to 27 Dec 2031, after a six-month technical extension adopted in June 2025 (verify) |
| 5 Feb 2026 | Commencement No. 6 (SI 2026/82): main tranche — recognised legitimate interests, purpose limitation, research, Art. 12A time limits, ADM (Arts. 22A–22D), children's higher protection, transfers (Arts. 45A–45B), interview notices, approved-person reports, penalty-notice timing, PECR cookie exemptions, charity soft opt-in, PECR enforcement alignment, Information Commission property transfer |
| 19 Jun 2026 | s. 103 complaints duty (DPA 2018 s. 164A) in force; ICO marks all data-protection provisions as commenced |
| 30 Sep 2026 | Commencement No. 9 (SI 2026/1015, made 10 Sept 2026): Information Commissioner abolished; functions transfer to the Information Commission; SI 2026/386 consequential renaming takes effect |
| Pending (Sept 2026) | Cyber Security and Resilience (Network and Information Systems) Bill — introduced 12 November 2025, reported to be in House of Lords committee stage from September 2026 with Royal Assent expected late 2026 or 2027 (verify); ICO guidance pipeline continues (PECR fines guidance, final enforcement procedural guidance, AI/ADM code of practice) |

## Key obligations for security/GRC teams

1. **Confirm which regime applies** — UK GDPR Art. 3 establishment or targeting test, Art. 27 representative for non-UK entities, PECR for marketing and cookies, and DPA Part 3 for any law-enforcement function. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Run UK and EU GDPR as one programme with a divergence register** — lawful-basis inventory (flag any use of recognised legitimate interests, which is UK-only), ADM inventory against Arts. 22A–22D, and transfer records that cite UK adequacy regulations, IDTA/Addendum and TRAs separately from EU SCCs.
3. **Wire the 72-hour clock into incident response** with awareness-time logging, phased-reporting templates and the PECR breach form for communications providers. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
4. **Stand up the s. 164A complaints channel** — electronic form, 30-day acknowledgement, case tracking to evidence "without undue delay", and reporting metrics ready for any s. 164B regulations. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
5. **Re-baseline DSAR handling** to the Art. 12A clock: record the "relevant time", identity/clarification requests that stop the clock, extension notices within month one, and a documented search-scope rationale under Art. 15(1A).
6. **Re-audit cookies and tracking** against Sch. A1: classify each technology as consent-required, strictly necessary, analytics-exempt (with objection route and no onward sharing) or appearance/functionality-exempt, and keep the evidence — PECR now carries £17.5m / 4% exposure.
7. **Treat ADM and AI systems as a governed inventory** — safeguards under Art. 22C, special-category restrictions, DPIA where high risk, and readiness for the ICO's AI/ADM code. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
8. **Prepare for the new investigatory powers** — interview-notice protocols for current and former staff, budget and scoping playbook for approved-person reports, and legal-hold procedures aligned to the 6-month penalty-notice window.
9. **Refresh processor and vendor terms** for breach-notification timing, UK transfer mechanisms and DPF certification checks. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
10. **Track the horizon** — Information Commission transition, secondary regulations under Arts. 6(6), 22D, 45A and PECR reg. 6A, and the Cyber Security and Resilience Bill. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).

## Interplay

- **EU GDPR** ([gdpr.md](gdpr.md)): same skeleton, different edits. Organisations in both markets must not import UK-only bases (recognised legitimate interests), the UK ADM model or the Art. 12A stop-the-clock into EU processing. EU–UK adequacy in both directions means intra-group flows need no safeguards, but EU adequacy is monitored and sunsets on 27 December 2031.
- **NIS Regulations 2018 / Cyber Security and Resilience Bill**: cyber-resilience and incident-reporting duties for operators of essential services and digital service providers sit outside UK GDPR; a single incident can trigger both a NIS report and an Art. 33 notification with different regulators and clocks. See [other-jurisdictions.md](other-jurisdictions.md) and, for the EU analogue, [nis2.md](nis2.md).
- **EU NIS2 / DORA**: UK entities serving EU financial or essential-service clients may face those regimes contractually or through EU subsidiaries; see [dora.md](dora.md).
- **EU AI Act** ([eu-ai-act.md](eu-ai-act.md)): UK ADM governance is delivered through Arts. 22A–22D, DPIAs and the forthcoming ICO code rather than a horizontal AI statute (verify current status) — a lighter but still enforceable layer for UK-only deployments.
- **ISO/IEC 27001 and NIST CSF 2.0** ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)): UK GDPR's security-of-processing duty still turns on appropriate technical and organisational measures; the ICO's fining guidance weighs whether an infringement was intentional or negligent and the categories of data affected, so certified controls remain the primary mitigation evidence.
- **Freedom of Information Act 2000**: the Information Commission also regulates FOI; SI 2026/386 amends the FOI Acts to reflect the new body.

## Primary sources

- UK GDPR (legislation.gov.uk, revised) — contents, Arts. 3, 6, 12, 15, 22A–22D, 27, 33, 45A, 45B, 83, Annex 1: https://www.legislation.gov.uk/eur/2016/679/contents (legal text)
- Data Protection Act 2018 — contents, introduction, ss. 3, 155, 157, 164A, 170, 207, 212, Sch. 16: https://www.legislation.gov.uk/ukpga/2018/12/contents (legal text)
- Data (Use and Access) Act 2025 — full text and contents: https://www.legislation.gov.uk/ukpga/2025/18/contents (legal text)
- PECR 2003 (SI 2003/2426) — regs. 5, 5A, 5C, 6, 22, 31, Sch. A1, Sch. 1: https://www.legislation.gov.uk/uksi/2003/2426/contents (legal text)
- DUAA commencement regulations: SI 2025/904 (No. 1), SI 2025/996 (No. 3), SI 2026/82 (No. 6), SI 2026/126 (No. 7), SI 2026/317 (No. 8), SI 2026/1015 (No. 9); SI 2026/386 (consequential amendments) — all on legislation.gov.uk (legal text)
- SI 2019/419 (EU Exit amendments) and SI 2023/1028 (US adequacy regulations): legislation.gov.uk (legal text)
- NIS Regulations 2018 (SI 2018/506) contents; GOV.UK Cyber Security and Resilience Bill collection page (introduction date only) (legal text / government page)
- ICO: Personal data breaches — a guide; A brief guide to international transfers; Adequacy regulations and country list; UK Extension to the EU-US DPF; Receiving personal information from the EEA (all ico.org.uk, regulator guidance)
- ICO: DUAA summary of changes; DUAA — what does it mean for organisations; statement on DUAA commencement (5 Feb 2026); "One year on" blog (23 June 2026); ICO governance changes confirmed for 30 September 2026 (regulator guidance / statements)
- Information Commissioner Data Protection Fining Guidance, March 2024 (PDF via GOV.UK) (regulator guidance)
- EDPB news, 20 October 2025: opinions on draft UK adequacy decisions (EU regulator page)
- Not fetched: European Commission press release IP/25/3059 on the renewed UK adequacy decisions (page unreachable); UK Parliament bill pages for the Cyber Security and Resilience Bill (blocked) — status taken from search snippets and marked "(verify)"

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
