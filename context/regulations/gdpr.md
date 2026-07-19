# EU General Data Protection Regulation (GDPR)

Regulation (EU) 2016/679. The baseline data protection law for the EU/EEA and the reference model for most privacy statutes worldwide. Directly applicable in all member states — no national transposition required, though member states supplement it in defined areas (e.g., employment data, age of consent for information society services).

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | EU/EEA (all 27 EU member states + Iceland, Liechtenstein, Norway); extraterritorial reach under Art. 3 |
| In force since | Adopted 2016-04-27; applicable from 2018-05-25 |
| Regulators | Independent supervisory authority (SA) per member state (e.g., CNIL, Irish DPC, Spanish AEPD); coordinated by the European Data Protection Board (EDPB); one-stop-shop lead SA for cross-border processing |
| Max penalties | Two tiers: up to EUR 10M or 2% of worldwide annual turnover (whichever is higher) for Art. 83(4) infringements; up to EUR 20M or 4% for Art. 83(5) infringements. Plus corrective powers: processing bans, suspension of transfers |
| Who's covered | Controllers and processors established in the EU (regardless of where processing happens), and non-EU organizations targeting or monitoring people in the EU (Art. 3(2)) |
| Private right of action | Yes — Art. 79 judicial remedy and Art. 82 compensation for material and non-material damage; Art. 80 representative actions |

## Territorial scope (Art. 3)

Two independent hooks — either one triggers full applicability:

1. **Establishment (Art. 3(1)).** Processing in the context of the activities of an establishment of a controller or processor in the EU, whether or not the processing itself takes place in the EU. "Establishment" is broad: a stable arrangement (a single agent or sales office can suffice) whose activities are inextricably linked to the processing.
2. **Targeting (Art. 3(2)).** Processing of personal data of data subjects who are in the EU by a controller/processor not established in the EU, where the processing relates to:
   - **(a) Offering goods or services** to people in the EU (payment not required — intent matters: EU-language sites, euro pricing, EU shipping, EU marketing).
   - **(b) Monitoring behaviour** of people in the EU (tracking, profiling, behavioural advertising, some analytics).

Non-EU organizations caught by Art. 3(2) must designate an EU representative (Art. 27) unless the processing is occasional, low-risk, and excludes large-scale special-category data.

Practical screen: an organization with no EU establishment, no EU-directed offering, and no monitoring of EU individuals is generally out of scope even if EU residents incidentally use its services. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md) for a structured applicability analysis.

## Key definitions (Art. 4)

- **Personal data** — any information relating to an identified or identifiable natural person ("data subject"). Includes identifiers such as name, ID number, location data, online identifiers (IP addresses, cookie IDs, device IDs). Pseudonymized data remains personal data; only truly anonymized data (irreversibly, considering means reasonably likely to be used) is out of scope.
- **Processing** — practically any operation on personal data: collection, storage, use, disclosure, erasure. Merely holding data is processing.
- **Controller** — determines the purposes and means of processing. Joint controllers (Art. 26) jointly determine both and must allocate responsibilities transparently.
- **Processor** — processes on behalf of and on documented instructions from a controller. A processor that determines its own purposes becomes a controller for that processing.
- **Special categories (Art. 9)** — data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership; genetic data; biometric data for the purpose of uniquely identifying a person; health data; data concerning sex life or sexual orientation. Processing is prohibited unless an Art. 9(2) condition applies (e.g., explicit consent, employment/social-security law, vital interests, substantial public interest, health care, public health, research). Criminal conviction and offence data is separately restricted (Art. 10).

## Principles (Art. 5)

1. **Lawfulness, fairness, transparency** (Art. 5(1)(a))
2. **Purpose limitation** — collected for specified, explicit, legitimate purposes; no incompatible further processing (Art. 5(1)(b))
3. **Data minimisation** — adequate, relevant, limited to what is necessary (Art. 5(1)(c))
4. **Accuracy** (Art. 5(1)(d))
5. **Storage limitation** — kept in identifiable form no longer than necessary (Art. 5(1)(e))
6. **Integrity and confidentiality** — appropriate security, including protection against unauthorised or unlawful processing and accidental loss, destruction, or damage (Art. 5(1)(f))
7. **Accountability** (Art. 5(2)) — the controller must be able to *demonstrate* compliance with all of the above. This is what drives records of processing (Art. 30), DPIAs, policies, and evidence retention.

## Lawful bases (Art. 6)

Every processing operation needs exactly one identified basis, documented before processing starts:

| Basis | Art. | Typical use | Watch-outs |
|---|---|---|---|
| Consent | 6(1)(a) | Marketing, cookies (with ePrivacy), optional features | Must be freely given, specific, informed, unambiguous; withdrawable as easily as given (Art. 7); explicit consent required for Art. 9 data and some transfers |
| Contract | 6(1)(b) | Delivering the service the person signed up for | Only what is objectively necessary for the contract — not everything mentioned in the T&Cs |
| Legal obligation | 6(1)(c) | Tax records, AML/KYC | Must be an EU or member-state law obligation |
| Vital interests | 6(1)(d) | Life-or-death emergencies | Narrow; last resort |
| Public task | 6(1)(e) | Public authorities | Rarely available to private companies |
| Legitimate interests | 6(1)(f) | Fraud prevention, network/information security (Recital 49), intra-group admin, some analytics | Requires a documented three-part balancing test (purpose, necessity, balancing); not available to public authorities in performance of their tasks; data subject can object (Art. 21) |

Security teams: Recital 49 recognizes network and information security as a legitimate interest — a common basis for logging, monitoring, and threat detection, still subject to necessity and proportionality.

## Data subject rights (Arts. 12–22)

Respond within **one month** of receipt, extendable by two further months for complex or numerous requests (Art. 12(3)), with the extension notified within the first month. Free of charge unless manifestly unfounded or excessive. Verify identity proportionately.

- **Transparency / information** (Arts. 13–14) — privacy notices at collection (or within one month if obtained indirectly).
- **Access** (Art. 15) — confirmation, a copy of the data, and prescribed metadata (purposes, recipients, retention, source, safeguards for transfers).
- **Rectification** (Art. 16).
- **Erasure / "right to be forgotten"** (Art. 17) — conditional, not absolute; exceptions include legal obligations, legal claims, freedom of expression.
- **Restriction of processing** (Art. 18).
- **Notification duty to recipients** of rectification/erasure/restriction (Art. 19).
- **Data portability** (Art. 20) — structured, commonly used, machine-readable format; applies only to data the person provided, processed by consent or contract, by automated means.
- **Objection** (Art. 21) — absolute for direct marketing; otherwise the controller must demonstrate compelling legitimate grounds.
- **Automated individual decision-making including profiling** (Art. 22) — right not to be subject to solely automated decisions with legal or similarly significant effects, subject to exceptions (contract necessity, law, explicit consent) with safeguards including human intervention. Interacts with AI system governance — see [eu-ai-act.md](eu-ai-act.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).

## Security of processing (Art. 32)

Controllers *and* processors must implement technical and organisational measures appropriate to the risk, considering state of the art, implementation cost, and the nature/scope/context/purposes of processing. Art. 32(1) explicitly names:

- **(a)** pseudonymisation and encryption of personal data;
- **(b)** ability to ensure ongoing confidentiality, integrity, availability, and **resilience** of processing systems and services;
- **(c)** ability to **restore availability and access** in a timely manner after an incident (backup/DR);
- **(d)** a process for **regularly testing, assessing and evaluating** the effectiveness of the measures.

GDPR does not mandate specific controls or certifications. In practice, alignment to ISO/IEC 27001, NIST CSF, or CIS Controls is how organizations evidence Art. 32 appropriateness — see [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md), [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md). Art. 32(2) ties "appropriate" to the risks of accidental or unlawful destruction, loss, alteration, unauthorised disclosure or access — i.e., a documented risk assessment is the anchor ([../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md)).

## Personal data breach notification (Arts. 33–34)

A **personal data breach** (Art. 4(12)) is a breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data. Availability incidents (ransomware, data loss without exfiltration) qualify.

- **Art. 33 — to the supervisory authority.** Without undue delay and, where feasible, **within 72 hours of becoming aware**, *unless* the breach is unlikely to result in a risk to individuals' rights and freedoms. If notification is later than 72 hours, it must be accompanied by reasons for the delay. Phased notification is permitted (Art. 33(4)) — notify with what you know, supplement later. Required content (Art. 33(3)): nature of the breach, categories and approximate numbers of data subjects and records, DPO contact, likely consequences, measures taken or proposed.
- **Processor duty (Art. 33(2)).** Processors must notify the controller without undue delay after becoming aware — no risk threshold. Contractually pin this to a specific hour count (commonly 24–48h) in the Art. 28 DPA.
- **Art. 34 — to data subjects.** Without undue delay when the breach is likely to result in a **high risk** to rights and freedoms. Exceptions (Art. 34(3)): data rendered unintelligible (e.g., strong encryption with keys not compromised), subsequent measures eliminating the high risk, or disproportionate effort (public communication instead). SAs can compel subject notification.
- **Art. 33(5) — documentation duty.** Document *every* personal data breach — facts, effects, remediation — even those not notified. This internal breach register is what SAs inspect to verify the "unlikely to result in a risk" judgments.

"Awareness" starts when the controller has a reasonable degree of certainty a breach occurred — a short investigation window is acceptable, but the clock is not paused by ongoing forensics. For multi-regime incidents, see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## DPIA and prior consultation (Arts. 35–36)

A **Data Protection Impact Assessment** is mandatory where processing is *likely to result in a high risk*, in particular (Art. 35(3)):

- systematic and extensive automated evaluation/profiling with legal or similarly significant effects;
- large-scale processing of Art. 9 special categories or Art. 10 criminal data;
- systematic large-scale monitoring of publicly accessible areas.

Each SA publishes a mandatory-DPIA list (Art. 35(4)); EDPB criteria (e.g., new technologies, matching datasets, vulnerable subjects) mean two or more risk factors usually indicate a DPIA. Required content (Art. 35(7)): systematic description, necessity/proportionality assessment, risk assessment, and mitigating measures. Seek the DPO's advice (Art. 35(2)).

**Prior consultation (Art. 36):** if the DPIA shows high residual risk that cannot be mitigated, consult the SA *before* processing. The SA has 8 weeks (extendable by 6) to respond.

DPIA methodology and templates: [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).

## Data Protection Officer (Arts. 37–39)

Mandatory designation when: (a) processing by a public authority; (b) core activities involve regular and systematic monitoring of data subjects on a large scale; or (c) core activities involve large-scale processing of Art. 9/10 data. The DPO must be involved in all data protection issues, adequately resourced, independent (no instructions on task performance, no dismissal for performing tasks, no conflict of interest — the CISO role can conflict where the CISO decides processing means), and reports to the highest management level. Tasks (Art. 39): inform/advise, monitor compliance, advise on DPIAs, cooperate with and act as contact point for the SA. Publish and communicate the DPO's contact details to the SA.

## International transfers (Chapter V, Arts. 44–49)

Transfers of personal data outside the EU/EEA require a transfer mechanism:

1. **Adequacy decisions (Art. 45)** — Commission-designated jurisdictions with essentially equivalent protection (includes UK, Japan, South Korea, Switzerland, Canada (commercial/PIPEDA), and the EU–US Data Privacy Framework for certified US organizations). Verify current status — adequacy decisions can be challenged or lapse.
2. **Appropriate safeguards (Art. 46)** — most commonly **Standard Contractual Clauses (SCCs)** (the 2021 modular set: C2C, C2P, P2C, P2P) and **Binding Corporate Rules (BCRs)** (Art. 47) for intra-group transfers; also approved codes of conduct and certifications.
3. **Derogations (Art. 49)** — explicit consent, contract necessity, important public interest, legal claims, vital interests — narrow, for occasional transfers, not a systematic mechanism.

**Post-Schrems II (CJEU C-311/18, 2020):** SCCs alone are not sufficient where the destination country's law undermines them. Exporters must perform a **Transfer Impact Assessment (TIA)** — evaluate destination surveillance/access laws against the specific transfer, and apply supplementary measures (technical: encryption with EU-held keys, pseudonymisation; contractual; organisational) where needed. Document TIAs; SAs request them. Onward transfers and remote access from third countries (e.g., support teams) count as transfers.

## Processor contracts (Art. 28)

Engaging a processor requires a binding written contract (the "DPA") containing, at minimum:

- processing only on **documented instructions** (including for transfers);
- personnel confidentiality commitments;
- Art. 32 security measures;
- **sub-processor** conditions — prior specific or general written authorisation, with objection rights and flow-down of obligations;
- **assistance** with data subject rights (Arts. 12–23) and with Arts. 32–36 obligations (security, breach notification, DPIAs);
- **deletion or return** of data at end of engagement;
- **audit and inspection** rights, including making available all information necessary to demonstrate compliance.

Also specify: subject matter, duration, nature and purpose, data types, categories of data subjects. The DPA review is a core third-party diligence step — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md). Processors acting outside instructions become controllers (Art. 28(10)) with full controller liability.

## Fines and enforcement (Art. 83)

Two tiers, each "whichever is higher":

- **Tier 1 — up to EUR 10M or 2% of total worldwide annual turnover** (Art. 83(4)): infringements of controller/processor obligations including Arts. 8, 11, 25–39 (privacy by design, records, security, breach notification, DPIA, DPO), 42, 43.
- **Tier 2 — up to EUR 20M or 4% of total worldwide annual turnover** (Art. 83(5)): infringements of the principles (Art. 5), lawful basis (Arts. 6, 7, 9), data subject rights (Arts. 12–22), transfer rules (Arts. 44–49), and non-compliance with SA orders.

Note the asymmetry: a security failure (Art. 32) is Tier 1, but the same incident often also evidences an Art. 5(1)(f) principle breach — Tier 2. Fine factors (Art. 83(2)) include nature/gravity/duration, intent or negligence, mitigation, prior infringements, cooperation, and how the SA learned of it (self-report vs. discovery). Corrective powers (Art. 58) can bite harder than fines: processing bans and transfer suspensions.

## Key obligations for security/GRC teams

1. **Maintain a record of processing activities (Art. 30)** — the data inventory that everything else (DPIAs, breach scoping, DSARs, transfer mapping) depends on. Required for organizations with 250+ employees, and below that for non-occasional, risky, or special-category processing.
2. **Evidence Art. 32 appropriateness** — a documented, risk-based control set mapped to a recognized framework, with proof of regular testing (Art. 32(1)(d)): pen tests, control testing, DR exercises. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
3. **Operate a breach process tuned to 72 hours** — detection-to-awareness triage, risk assessment template for the notify/don't-notify call, SA notification playbooks per lead authority, processor notification SLAs, and the Art. 33(5) register including non-notified breaches.
4. **Embed data protection by design and by default (Art. 25)** — minimisation, default-off sharing, retention enforcement — into SDLC and change gates.
5. **Run the DPIA pipeline** — screening criteria in project intake, DPO consultation, Art. 36 escalation path for unmitigable high residual risk.
6. **Govern processors and transfers** — Art. 28 DPA terms in all vendor contracts, sub-processor change monitoring, current SCC modules, documented TIAs for third-country transfers, annual adequacy-status review.
7. **Support data subject rights operations** — identity verification, one-month clock tracking, search/retrieval across systems, erasure propagation to backups per documented policy, Art. 19 recipient notification.
8. **Retention schedule enforcement** — storage limitation (Art. 5(1)(e)) is among the most-enforced principles; automate deletion where feasible and document exceptions via [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
9. **Know your lead SA** — for cross-border processing, identify the main establishment and lead authority (Art. 56) before an incident forces the question.

Related context: [nis2.md](nis2.md) and [dora.md](dora.md) impose parallel EU incident-reporting duties that can apply to the same event; [us-state-privacy.md](us-state-privacy.md) for the US analogue landscape.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
