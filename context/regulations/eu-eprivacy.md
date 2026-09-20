# EU ePrivacy Directive (Directive 2002/58/EC) and national cookie / electronic-communications rules

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Directive 2002/58/EC "concerning the processing of personal data and the protection of privacy in the electronic communications sector" (OJ L 201, 31.7.2002), as amended by Directive 2006/24/EC (data retention — later invalidated) and Directive 2009/136/EC (the "Citizens' Rights Directive", OJ L 337, 18.12.2009). A directive: it binds only through national transposing laws, which vary |
| Implementing measure | Commission Regulation (EU) No 611/2013 — directly applicable rules on provider breach notification under Art. 4 (24-hour clock, content, encryption safe harbour); in force 25 August 2013 |
| Regulator | Set nationally (Art. 15a): data protection authority, telecoms regulator, or both, depending on the Member State. The GDPR one-stop-shop does **not** apply to ePrivacy matters — each national authority acts alone for its territory (EDPB Opinion 5/2019; CNIL enforcement practice) |
| Status (Sept 2026) | In force and unreformed since 2009. The 2017 ePrivacy Regulation proposal (COM(2017) 10) was withdrawn — notice published OJ C/2025/5423 of 6 October 2025. The Commission's Digital Omnibus proposal (COM(2025) 837, 19 November 2025) would move personal-data cookie rules into the GDPR and delete Art. 4; still in first reading |
| Who is covered | Art. 4, 6, 9, 15: providers of publicly available electronic communications services / public networks. Art. 5(3) (terminal equipment) and Art. 13 (unsolicited marketing): **anyone** storing/reading information on a user's device or sending direct marketing — i.e. every website, app and marketer, not just telcos |
| Headline rules | Confidentiality of communications (Art. 5(1)); prior consent for cookies and similar storage/access (Art. 5(3)); security and breach notification for providers (Art. 4); traffic and location data limits (Arts. 6, 9); opt-in for electronic direct marketing with a "soft opt-in" (Art. 13) |
| Breach clock (providers) | Notify the competent national authority **no later than 24 hours after detection** where feasible; second notification within **3 days** of the initial one (Reg. 611/2013 Art. 2). UK PECR reg. 5A now says **72 hours** (since 20 August 2025) |
| Penalties | National (Art. 15a): "effective, proportionate and dissuasive". No EU-wide ceiling. France: CNIL fined Google EUR 325m and SHEIN EUR 150m on 1 September 2025 for cookie breaches. UK: up to GBP 17.5m or 4% of worldwide turnover for the core PECR duties since 5 February 2026 |
| Relationship to GDPR | Lex specialis: GDPR Art. 95 prevents double obligations; where ePrivacy requires consent (Arts. 5(3), 6(3), 9, 13), the full menu of GDPR Art. 6 lawful bases is unavailable (EDPB Opinion 5/2019; CJEU C-654/23) |
| UK equivalent | Privacy and Electronic Communications (EC Directive) Regulations 2003 (SI 2003/2426, "PECR"), substantially amended by the Data (Use and Access) Act 2025 |

## What it is

The ePrivacy Directive "particularises and complements" general data protection law for the electronic communications sector (Art. 1(2)). It began as a telecoms-sector instrument (replacing Directive 97/66/EC) protecting the confidentiality of communications, traffic and location data, itemised billing, calling-line identification and directories. Two provisions have since outgrown that origin and now shape every online business: Art. 5(3), which since the 2009 amendment requires **prior consent** for storing or accessing information on terminal equipment (the "cookie rule"), and Art. 13, which governs electronic direct marketing. Recital 24 of the 2002 text frames the rationale: terminal equipment and the information on it are part of the user's private sphere, and "spyware, web bugs, hidden identifiers and other similar devices" may enter it only for legitimate purposes with the user's knowledge.

The 2009 amendment also added the provider security baseline (Art. 4(1a)), the first EU sector-specific personal-data-breach notification duty (Art. 4(3)–(4), detailed by Regulation 611/2013), and the enforcement article (Art. 15a). The Directive's cross-references to Directive 95/46/EC are read as references to the GDPR (GDPR Art. 94(2)), and its definitions borrow from the EU electronic-communications framework — originally the 2002 Framework Directive, since 21 December 2020 the European Electronic Communications Code (EECC, Directive (EU) 2018/1972), whose "electronic communications service" definition covers number-independent interpersonal communications services such as messaging apps. Whether and how a given OTT service is caught depends on the national transposition — confirm per Member State.

A replacement ePrivacy Regulation was proposed in January 2017 and negotiated for eight years without agreement; it was formally withdrawn in October 2025. The Directive therefore remains the governing text, implemented 27 different ways.

## Who it covers / Scope

| Provision | Who is caught | Notes |
|---|---|---|
| Art. 3 (services concerned) | Processing of personal data in connection with publicly available electronic communications services in public networks in the EU, "including public communications networks supporting data collection and identification devices" | Sets the scope for the provider duties (Arts. 4, 6, 8–12, 15(1b)) |
| Art. 5(3) (terminal equipment) | Any natural or legal person that stores information in, or gains access to information already stored in, the terminal equipment of a subscriber or user | No establishment or sector test; applies to websites, apps, SDKs, connected devices, email pixels. National transpositions (e.g. France Art. 82 Loi Informatique et Libertés; UK PECR reg. 6) apply to devices of users in their territory |
| Art. 13 (unsolicited communications) | Anyone using automated calling systems, fax or electronic mail (defined in Art. 2(h) to include text, voice, sound or image messages — so SMS and in-app messages) for direct marketing | The Art. 13(1) opt-in and the Art. 13(3) national choice apply to subscribers who are natural persons (Art. 13(5)); for legal-person subscribers Member States must ensure legitimate interests are "sufficiently protected", and national rules differ |
| Art. 1(3) exclusions | Activities outside EU law: public security, defence, State security, criminal law | Art. 15(1) lets Member States restrict Arts. 5, 6, 8, 9 for these purposes, including data retention |
| "Information" | Both personal and non-personal data (EDPB Guidelines 2/2023; CJEU Planet49) | Art. 5(3) protection does not depend on personal data being involved |

Because it is a directive, applicability is ultimately a question of **which national law** applies: the ePrivacy Directive has no equivalent of GDPR Art. 3 or the one-stop-shop, and a website used from several Member States faces several authorities.

## Core obligations

### Terminal-equipment rule — Art. 5(3)

| Element | Requirement | Source |
|---|---|---|
| Default | Storing information, or gaining access to information already stored, in terminal equipment is allowed only with the subscriber's or user's **consent**, given after "clear and comprehensive information" including the purposes | Art. 5(3) as amended 2009 |
| Consent standard | GDPR-standard consent (Art. 2(f) ePD → GDPR Art. 4(11)/7): a pre-ticked checkbox the user must deselect is not valid consent; the standard does not change according to whether the stored information is personal data; the information given must include the duration of the cookies and whether third parties may have access | CJEU C-673/17 *Planet49*, 1 October 2019 |
| Exemptions (only two) | (a) technical storage/access for the sole purpose of carrying out the transmission of a communication; (b) storage/access **strictly necessary** for an information-society service **explicitly requested** by the user | Art. 5(3), second sentence; WP29 Opinion 04/2012 (WP 194) lists typical exempt cookies: user-input, authentication (session), user-centric security, multimedia player session, load-balancing session, UI customisation, some social plug-in cookies for logged-in members |
| Analytics | Not exempt under the Directive text. Some national regulators tolerate first-party audience-measurement under strict conditions; this is national practice, not EU law | EDPB-EDPS Joint Opinion 2/2026 notes the Directive contains no audience-measurement or security exception |
| Technical scope | Applies beyond cookies: tracking pixels and tracking URLs (caching = storage; the identifier callback = access), JavaScript/SDK collection of device data, unique/persistent identifiers hashed on-device, IoT devices reporting to servers, and access to IP addresses where they originate from the terminal equipment (e.g. static IPv4, IPv6). Three cumulative criteria: "information", "terminal equipment of a subscriber or user" connected to a public network, and "gaining access" or "storage" | EDPB Guidelines 2/2023 on the technical scope of Art. 5(3), v2.0 adopted 7 October 2024 |
| Browser settings | Recital 66 of Directive 2009/136/EC allows consent via browser or application settings "where technically possible and effective"; regulators have generally not accepted default browser settings as consent | Directive 2009/136/EC recital 66 |
| Banner design | EDPB Cookie Banner Taskforce report (adopted 17 January 2023): vast majority of authorities treat absence of a reject option on the first layer as an infringement; pre-ticked boxes on the second layer invalid; deceptive button colours and contrast, "reject" as a link buried in text rather than a button, legitimate interest claimed alongside the purpose list, cookies inaccurately classified as "essential", and no means of withdrawing consent are all flagged | EDPB report, 17 January 2023 |

### Confidentiality, traffic and location data — Arts. 5(1), 6, 9, 15

| Article | Obligation |
|---|---|
| 5(1) | Member States must prohibit listening, tapping, storage or other interception/surveillance of communications and related traffic data by anyone other than the users, without their consent, except where legally authorised under Art. 15(1). Technical storage necessary for conveyance is permitted; 5(2) preserves lawful business recording (evidence of transactions) |
| 6 | Traffic data must be erased or anonymised when no longer needed for transmission; may be kept for billing/interconnection until the bill can no longer be challenged; marketing or value-added-service use only with prior consent (withdrawable at any time); processing restricted to staff handling billing, traffic management, customer enquiries, fraud detection, marketing or value-added services |
| 9 | Location data other than traffic data: only anonymised or with consent, for the duration necessary for a value-added service; users must be told data types, purposes, duration and third-party transmission before consenting; must be able to temporarily refuse per connection, free of charge |
| 15(1) | Member States may restrict Arts. 5, 6, 8(1)–(4) and 9 by legislative measure that is necessary, appropriate and proportionate for national security, defence, public security or crime, including limited-period data retention. The 2006 Data Retention Directive (2006/24/EC) that hung off this article was declared invalid by the CJEU on 8 April 2014 (C-293/12 and C-594/12 *Digital Rights Ireland*) |
| 15(1b) | Providers must keep internal procedures for law-enforcement access requests and report request numbers and legal bases to the authority on demand |

### Security and breach notification — Art. 4 and Regulation (EU) 611/2013 (providers only)

| Requirement | Detail |
|---|---|
| Security measures (Art. 4(1)–(1a)) | Appropriate technical and organisational measures proportionate to risk; must at least restrict personal-data access to authorised personnel, protect stored/transmitted data against destruction, loss, alteration and unauthorised access or disclosure, and implement a security policy. Authorities may audit and issue best-practice recommendations |
| Risk warnings (Art. 4(2)) | Where a particular risk of a network security breach exists, inform subscribers of the risk and, if outside the provider's control, of remedies and likely costs |
| Authority notification (Art. 4(3); Reg. 611/2013 Art. 2) | **All** personal data breaches; no risk threshold. Notify no later than **24 hours after detection** where feasible; if Annex I information is incomplete, an initial notification within 24 hours (Section 1 content) followed by a second within **3 days** of the initial; further delay requires a reasoned justification. "Detection" = sufficient awareness that a security incident has compromised personal data to make a meaningful notification |
| Individual notification (Art. 4(3); Reg. 611/2013 Art. 3) | Where the breach is likely to adversely affect personal data or privacy, notify subscribers/individuals without undue delay, independently of the authority notification; Annex II content in clear language, dedicated message, no marketing; media advertisements permitted where individuals cannot be identified in time; delay possible with authority agreement if investigation at risk |
| Encryption safe harbour (Reg. 611/2013 Art. 4) | Individual notification not required if the provider demonstrates to the authority that the data was rendered unintelligible — securely encrypted with a standardised algorithm, or replaced by a keyed cryptographic hash, with uncompromised keys |
| Sub-providers (Reg. 611/2013 Art. 5) | A contracted provider without a direct subscriber relationship must **immediately** inform the contracting provider of a breach |
| Breach inventory (Art. 4(4)) | Providers must maintain an inventory of breaches (facts, effects, remedial action) sufficient for the authority to verify compliance |

### Unsolicited communications — Art. 13

| Rule | Detail |
|---|---|
| Opt-in (13(1)) | Automated calling and communication systems without human intervention, fax and electronic mail for direct marketing only with the prior consent of subscribers or users |
| Inbox advertising | Advertising messages displayed among private emails in an inbox, in a form resembling a real email, are "electronic mail" used for direct marketing and need Art. 13(1) consent (CJEU C-102/20 *StWL*, 25 November 2021) — the basis of the CNIL's 2025 Gmail decision |
| Soft opt-in (13(2)) | Where electronic contact details were obtained from a customer "in the context of the sale of a product or a service", the same entity may market its own similar products or services, provided the customer is given a clear, free and easy opportunity to object at collection and in every message. CJEU C-654/23 *Inteligo Media* (13 November 2025): a **free** account that gives access to a limited number of articles and a newsletter is a "sale" (remuneration may be indirect); a newsletter linking to paid content is direct marketing of similar services; and, read with GDPR Art. 95, GDPR Art. 6(1) does **not** additionally apply to the sending |
| Other channels (13(3)) | Member States choose opt-in or opt-out for other direct marketing (e.g. live calls); both must be free for the user |
| Sender identity (13(4)) | Marketing email that disguises the sender, lacks a valid opt-out address, or links to sites breaching e-Commerce Directive Art. 6 is prohibited outright |
| Remedies (13(6)) | Any person adversely affected — including a service provider protecting its business interests — may bring legal proceedings; Member States may penalise providers whose negligence contributes to breaches |

### Other provider duties

Arts. 7–8 and 10–12: right to non-itemised bills; free per-call and per-line blocking of calling-line identification, with override procedures for malicious-call tracing and emergency services; free stopping of automatic call forwarding; free opt-out from public directories with prior information.

## Enforcement and penalties

- **Art. 15a** (added 2009) requires Member States to lay down effective, proportionate and dissuasive penalties, "including criminal sanctions where appropriate", applicable even for periods of breach later rectified; competent authorities must have powers to order cessation and to investigate. No EU-level fine ceiling exists — the Directive predates the GDPR's Art. 83 model.
- **Competence is national and un-coordinated**: the GDPR cooperation and consistency mechanism (one-stop-shop) does not extend to ePrivacy-only breaches (EDPB Opinion 5/2019, adopted 12 March 2019). The CNIL states explicitly that it acts alone for cookies placed on devices in France because those operations fall under the ePrivacy transposition (Art. 82 Loi Informatique et Libertés; Art. L. 34-5 CPCE for e-marketing), not the GDPR.
- **Recent EU enforcement (official sources)**: CNIL, 1 September 2025 — EUR 325m against Google LLC and Google Ireland (EUR 200m + EUR 125m) for ads inserted between Gmail emails without consent and cookies set during account creation; EUR 150m against SHEIN's Irish subsidiary for advertising cookies set on arrival, incomplete consent interfaces and missing third-party information. Earlier, the CNIL issued orders to comply to nearly 90 organisations during 2021 for banners where refusing cookies was harder than accepting them.
- **Where GDPR also applies** (personal data processed after the cookie is read), the DPA can additionally apply GDPR Art. 83 fines to the downstream processing — the two regimes stack rather than substitute.
- **UK (PECR)**: since 5 February 2026 the ICO enforces PECR through DPA 2018 Parts 5–7 as modified by DUAA Schedule 13. The "higher maximum amount" (GBP 17.5m, or 4% of total annual worldwide turnover for an undertaking, whichever is higher) applies to breaches of regs. 5, 6, 7, 8, 14, 19–24 and 32B(4)–(5) (security, cookies, marketing calls and emails); the standard maximum (GBP 8.7m or 2%) applies otherwise. The pre-2026 ceiling was the GBP 500,000 monetary penalty under the old Schedule 1 route. Failure to notify a breach under reg. 5A is excluded from penalty notices and instead attracts a **fixed GBP 1,000** penalty (reg. 5C).

## Timeline and status

| Date | Event |
|---|---|
| 12 July 2002 | Directive 2002/58/EC adopted; transposition deadline 31 October 2003 (Art. 17); repeals Directive 97/66/EC |
| 15 March 2006 | Directive 2006/24/EC inserts Art. 15(1a) (data retention); invalidated by CJEU 8 April 2014 |
| 25 November 2009 | Directive 2009/136/EC: prior-consent cookie rule, Art. 4 security/breach duties, Art. 13 tightening, Art. 15a; transposition by 25 May 2011 |
| 25 August 2013 | Regulation (EU) 611/2013 (breach notification measures) enters into force |
| 25 May 2018 | GDPR applies; Art. 95 fixes the lex specialis relationship; EDPB Opinion 5/2019 (12 March 2019) explains it |
| 1 October 2019 | CJEU *Planet49* (C-673/17) |
| 21 December 2020 | EECC replaces the 2002 Framework Directive from which ePrivacy takes its definitions |
| 17 January 2023 | EDPB Cookie Banner Taskforce report adopted |
| 7 October 2024 | EDPB Guidelines 2/2023 on technical scope of Art. 5(3), v2.0 (v1.0 for consultation 14 November 2023) |
| 18 October 2024 | NIS2 deletes EECC Arts. 40–41 (telecom security/incident rules) — telecoms security supervision now sits in NIS2; ePrivacy Art. 4 personal-data-breach duties remain separate |
| 20 August 2025 | UK: DUAA 2025 s. 111 commences (SI 2025/904) — PECR reg. 5A breach notification becomes "without undue delay and, where feasible, not later than 72 hours", with reasons required for any later notification |
| 6 October 2025 | Withdrawal of the ePrivacy Regulation proposal COM(2017) 10 final published (OJ C/2025/5423) |
| 13 November 2025 | CJEU *Inteligo Media* (C-654/23) on the soft opt-in |
| 19 November 2025 | Commission Digital Omnibus proposal (COM(2025) 837, procedure 2025/0360(COD)): would **delete ePrivacy Art. 4** (provider security and breach notification) and disapply Art. 5(3) where the subscriber or user is a natural person and the information stored or accessed is or leads to personal data, moving those rules into a new GDPR Art. 88a (consent, plus exceptions for transmission, a service explicitly requested, controller-only audience measurement and service/device security; single-click refusal; no re-prompting for at least six months after a refusal) with machine-readable consent signals in a proposed Art. 88b — oversight would pass to the GDPR supervisory authorities and the one-stop-shop |
| 5 February 2026 | UK: DUAA ss. 112–116 with Schedules 12 and 13 commence (SI 2026/82) — substituted reg. 6 with the Schedule A1 exceptions, charity soft opt-in (reg. 22(3A)), and PECR enforcement through DPA 2018 Parts 5–7 at GDPR-level maxima |
| 10 February 2026 | EDPB-EDPS Joint Opinion 2/2026 on the Digital Omnibus: asks that the new audience-measurement and security exceptions be delimited to what is strictly necessary, noting no such exceptions exist under Art. 5(3) today |
| 29 April 2026 | UK ICO finalises its guidance on storage and access technologies after two consultations (December 2024 draft; July 2025 consultation on the DUAA changes) |
| 30 September 2026 (pending) | UK: the ICO is to become the Information Commission (DUAA ss. 117–119); consequential wording changes to PECR regs. 5A, 5C and 31 in SI 2026/386 (made 26 March 2026) take effect when that transfer is fully in force |
| Status, September 2026 | Digital Omnibus still in first reading: committee referral 19 January 2026; joint ITRE/LIBE rapporteurs appointed 25 February 2026 (Salla, Kaljurand); committee draft report 22 June 2026; amendments tabled 27 July 2026; the Parliament's procedure file records no committee vote, Council general approach or plenary position. **No agreed text — current obligations are unchanged** |

**UK PECR specifics (as amended).** Reg. 6(1) prohibits storing or accessing information on terminal equipment "subject to Schedule A1"; the definition expressly includes instigating storage/access and collecting information automatically emitted by the device. Schedule A1 exceptions: consent (para. 2, including via browser settings); transmission (3); strictly necessary for a requested service (4 — with examples: protecting information, device security, fraud and fault detection, authentication, remembering selections); **first-party statistical analytics** to improve the service, not shared except with helpers, with information and a free, simple means of objecting (5); **appearance/functionality** preferences on the same terms (6); emergency assistance geolocation (7). Reg. 22 keeps the opt-in for marketing email to individual subscribers, the commercial soft opt-in (22(3)), and adds a charity soft opt-in (22(3A)).

## Key obligations for security/GRC teams

1. **Map every Art. 5(3) touchpoint, not just cookies** — pixels, SDKs, fingerprinting, on-device hashing, IoT telemetry, IP-based tracking. Inventory by purpose and by first/third party; classify each as exempt (transmission / strictly necessary) or consent-required using the EDPB three-criteria test. Feed the result into [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
2. **Engineer consent to the CJEU standard**: no pre-ticked boxes, reject as easy as accept on the first layer, purposes and cookie duration disclosed, third-party access disclosed, withdrawal as easy as giving. Test that a "reject" actually suppresses the tags (regulators run technical checks). Record consent proofs.
3. **Determine the national law per market** — there is no one-stop-shop. For the UK, apply Schedule A1 (analytics and appearance exceptions exist there but not in the EU Directive). See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
4. **Providers of electronic communications services: run the 24-hour breach clock** from "detection" as defined in Reg. 611/2013, with the Annex I two-stage content ready, plus the separate individual-notification test and the encryption safe-harbour evidence. This is a distinct clock from GDPR Art. 33 (72 hours) and from NIS2 (24-hour early warning, 72-hour notification); keep them in the [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md). See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
5. **Maintain the Art. 4(4) breach inventory** (facts, effects, remediation) as a standing record — it is the audit artefact the authority will ask for, and it parallels the GDPR Art. 33(5) register.
6. **Control electronic direct marketing**: consent or a documented soft-opt-in basis per contact, similar-products test, objection link in every message, sender identity clear; do not relabel marketing as "service messages". Treat SMS and in-app pushes as "electronic mail".
7. **Third-party tags and SDKs are your compliance exposure**: contractually require vendors to fire only after consent, disclose their purposes, and support withdrawal signals. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
8. **Track the Digital Omnibus** through [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md): if adopted in anything like the proposed form, personal-data cookie rules move into the GDPR (with its one-stop-shop and Art. 83 fines) and browser-level signals become binding — a consent-management re-architecture, not a banner tweak.

## Interplay

- **GDPR** ([gdpr.md](gdpr.md)): ePrivacy governs the act of storing/accessing on the device and the sending of the message; GDPR governs the subsequent processing of any personal data (profiling, ad serving, analytics). Where ePrivacy demands consent, legitimate interest cannot substitute for that step (EDPB Opinion 5/2019 paras 40–41); where ePrivacy contains a specific rule, Art. 95 prevents duplicative GDPR obligations for providers. Consent quality, withdrawal and the information duties are all measured against GDPR Arts. 4(11), 7, 12–13.
- **NIS2** ([nis2.md](nis2.md)): providers of public electronic communications networks/services are NIS2 entities; NIS2 Art. 43 deleted EECC Arts. 40–41 from 18 October 2024, so their **security and significant-incident** reporting now runs under NIS2 (24h/72h/1 month), while **personal data breach** notification for the same providers still runs under ePrivacy Art. 4 / Reg. 611/2013 (24h) and GDPR Art. 33 (72h). Three regimes, three clocks, potentially two or three authorities.
- **DORA** ([dora.md](dora.md)): no direct overlap; financial entities' customer-facing websites and marketing are ePrivacy matters regardless of DORA.
- **EU AI Act** ([eu-ai-act.md](eu-ai-act.md)): on-device data collection feeding AI systems (profiling, ad models) needs an Art. 5(3) basis before AI Act obligations are reached.
- **UK** ([other-jurisdictions.md](other-jurisdictions.md)): PECR mirrors the Directive's structure (regs. 5–5C security/breach, 6 + Schedule A1 devices, 19–24 marketing) but has diverged materially since 2025–2026: 72-hour breach clock, analytics and appearance exceptions, charity soft opt-in, GDPR-level fines, ICO codes of conduct (reg. 32A). EU and UK cookie configurations should be managed as separate profiles.
- **US state privacy laws** ([us-state-privacy.md](us-state-privacy.md)): opt-out model (universal opt-out signals such as GPC) versus the EU opt-in model; a single consent platform must handle both.
- **Frameworks**: ePrivacy has no security control catalogue; Art. 4(1a) maps to access control, data protection and policy controls in [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md). Use [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) to evidence Art. 4 through existing controls.

## Primary sources

- Directive 2002/58/EC (ePrivacy Directive), original text with recitals: https://eur-lex.europa.eu/eli/dir/2002/58/oj — legal text
- Directive 2002/58/EC, consolidated version as at 19 December 2009: https://eur-lex.europa.eu/eli/dir/2002/58/2009-12-19 — the operative text used throughout this pack
- Directive 2009/136/EC (amending directive; recital 66 on browser settings): https://eur-lex.europa.eu/eli/dir/2009/136/oj — legal text
- Commission Regulation (EU) No 611/2013 of 24 June 2013 (breach-notification measures): https://eur-lex.europa.eu/eli/reg/2013/611/oj — legal text
- Regulation (EU) 2016/679 (GDPR) Arts. 33, 94(2) and 95: https://eur-lex.europa.eu/eli/reg/2016/679/oj — legal text
- Directive (EU) 2022/2555 (NIS2) Arts. 23 and 43: https://eur-lex.europa.eu/eli/dir/2022/2555/oj — legal text
- Directive (EU) 2018/1972 (EECC) Arts. 2, 124 and 125: https://eur-lex.europa.eu/eli/dir/2018/1972/oj — legal text
- Withdrawal of Commission proposals, OJ C/2025/5423 of 6 October 2025 (includes COM(2017) 10 final, 2017/0003(COD)): https://eur-lex.europa.eu/eli/C/2025/5423/oj — official notice
- Proposal COM(2017) 10 final (withdrawn ePrivacy Regulation), 10 January 2017: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52017PC0010 — legislative proposal
- Proposal COM(2025) 837 final (Digital Omnibus), 19 November 2025, incl. proposed GDPR Arts. 88a–88b and the amendments to Directive 2002/58/EC: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0837 — legislative proposal
- European Parliament procedure file 2025/0360(COD) (status, rapporteurs, committee dates): https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD) — official legislative observatory
- CJEU C-673/17 *Planet49*, 1 October 2019: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62017CJ0673 — judgment
- CJEU C-102/20 *StWL Städtische Werke Lauf a.d. Pegnitz*, 25 November 2021 (inbox advertising): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62020CJ0102 — judgment
- CJEU C-654/23 *Inteligo Media*, 13 November 2025 (soft opt-in; Art. 95 GDPR): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0654 — judgment
- CJEU Joined Cases C-293/12 and C-594/12 *Digital Rights Ireland*, 8 April 2014: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62012CJ0293 — judgment
- EDPB Opinion 5/2019 on the interplay between the ePrivacy Directive and the GDPR, 12 March 2019: https://www.edpb.europa.eu/sites/default/files/files/file1/201905_edpb_opinion_eprivacydir_gdpr_interplay_en_0.pdf — regulator opinion
- EDPB Guidelines 2/2023 on the technical scope of Art. 5(3), v2.0, 7 October 2024: https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf — regulator guidance
- EDPB Report of the Cookie Banner Taskforce, 17 January 2023: https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf — regulator report
- EDPB-EDPS Joint Opinion 2/2026 on the Digital Omnibus, adopted 10 February 2026: https://www.edpb.europa.eu/our-work-tools/our-documents/edpbedps-joint-opinion/edpb-edps-joint-opinion-22026-proposal_en — regulator opinion
- Article 29 Working Party Opinion 04/2012 on cookie consent exemption (WP 194), 7 June 2012: https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2012/wp194_en.pdf — regulator guidance
- CNIL, Google fined EUR 325m, 1 September 2025 (deliberation SAN-2025-004): https://www.cnil.fr/en/cookies-and-advertisements-inserted-between-emails-google-fined-325-million-euros-cnil — regulator press release
- CNIL, SHEIN (Infinite Styles Services Co. Ltd) fined EUR 150m, 1 September 2025 (deliberation SAN-2025-005): https://www.cnil.fr/en/cookies-placed-without-consent-shein-fined-150-million-euros-cnil — regulator press release
- CNIL, orders to nearly 90 organisations on cookie refusal, 14 December 2021: https://www.cnil.fr/en/refusing-cookies-should-be-easy-accepting-them-cnil-continues-its-action-and-issues-new-orders — regulator press release
- UK PECR (SI 2003/2426), including regs. 5A, 5C, 6, 22, 31 and Schedule A1 as amended: https://www.legislation.gov.uk/uksi/2003/2426/contents — legal text
- Data (Use and Access) Act 2025 (c. 18): https://www.legislation.gov.uk/ukpga/2025/18/contents — legal text
- DUAA commencement: SI 2025/904 (No. 1) https://www.legislation.gov.uk/uksi/2025/904/contents/made and SI 2026/82 (No. 6) https://www.legislation.gov.uk/uksi/2026/82/contents/made; consequential amendments SI 2026/386 https://www.legislation.gov.uk/uksi/2026/386/contents/made — legal texts
- Data Protection Act 2018 s. 157 (higher and standard maximum penalty amounts): https://www.legislation.gov.uk/ukpga/2018/12/section/157 — legal text
- ICO, Guidance on the use of storage and access technologies (finalised 29 April 2026): https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/ — regulator guidance
- ICO, governance changes confirmed for 30 September 2026: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/09/ico-to-become-information-commission-on-30-september-2026/ — regulator announcement

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
