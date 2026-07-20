# Brazil: Lei Geral de Proteção de Dados (LGPD)

Law No. 13,709/2018. Brazil's omnibus data protection law, closely modeled on GDPR but with meaningful local differences: a broader set of legal bases, a near-universal DPO expectation, Brazil-capped fines, and a regulator — the ANPD — that spent its first years building rules and guidance and is now enforcing them. If you already run a GDPR program, LGPD is an adaptation exercise, not a rebuild; the traps are in the deltas.

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | Brazil; extraterritorial — applies to processing carried out in Brazil, processing to offer goods/services to or process data of individuals located in Brazil, and processing of personal data collected in Brazil (Art. 3) |
| In force since | Law enacted 2018-08-14; main provisions effective 2020-09-18; administrative sanctions applicable from 2021-08-01 |
| Regulator | Autoridade Nacional de Proteção de Dados (ANPD) — an autonomous federal authority (autarquia) since 2022; sector overlays from the Central Bank (BCB cyber rules for financial institutions), SUSEP, ANS, and others |
| Max penalties | Simple fine up to **2% of the private group's revenue in Brazil** for the prior fiscal year (tax-excluded), **capped at R$50M per infraction**; plus daily fines, publicization of the infraction, blocking or deletion of the data involved, and partial or total suspension/prohibition of processing activities |
| Who's covered | Controllers and processors ("operadores"), public or private, regardless of headquarters location, subject to Art. 3 hooks; exemptions for purely personal, journalistic/artistic, academic (partially), and certain state-security/criminal-investigation uses |
| Private right of action | Yes — individual and collective actions for damages (Arts. 42–45); Brazilian consumer-protection bodies and public prosecutors (Ministério Público) actively litigate data cases, and courts have recognized non-material damages for breaches |

## Legal bases (Art. 7)

LGPD provides **ten** legal bases — GDPR's six plus four Brazil-specific ones. Any one suffices; document the choice before processing:

1. Consent — free, informed, unambiguous, for specified purposes; withdrawable.
2. Legal or regulatory obligation of the controller.
3. Execution of public policies by the public administration.
4. Studies by research bodies (anonymized where possible).
5. Contract performance or preliminary procedures at the data subject's request.
6. Exercise of rights in judicial, administrative, or arbitration proceedings.
7. Protection of life or physical safety.
8. Health protection, in procedures by health professionals/services/authorities.
9. Legitimate interests of the controller or third parties — requires a balancing test and, per ANPD guidance, a documented legitimate-interest assessment; the ANPD may demand the record.
10. Credit protection — a Brazil-specific basis reflecting the credit-scoring ecosystem.

**Sensitive personal data (Art. 11)** — racial/ethnic origin, religious conviction, political opinion, union or religious/philosophical/political organization membership, health, sex life, genetic or biometric data — has its own narrower basis list (no legitimate interests, no credit protection); the default is specific and highlighted consent. Children's data (Art. 14) requires processing in the child's best interest; the consent rules were refined by ANPD interpretation — verify current guidance for under-18 processing.

## Data subject rights (Art. 18)

Confirmation of processing, access, correction, anonymization/blocking/deletion of unnecessary or noncompliant data, portability, deletion of consent-based data, information on sharing and on consequences of refusing consent, consent revocation, and review of solely automated decisions (Art. 20 — note: the review need not be human, a divergence from GDPR Art. 22).

- Response clock: confirmation/access in simplified form **immediately**, or by complete declaration **within 15 days** (Art. 19); other rights "without delay" — ANPD regulation details procedures, verify current rules.
- No fee may be charged. Requests can be made by the data subject or a legally constituted representative.

## Governance, security, and the DPO

- **DPO ("encarregado," Art. 41).** Every controller must indicate an encarregado — identity and contact information published — to interface with data subjects and the ANPD. The ANPD's 2024 DPO regulation (CD/ANPD Resolution) allows the role to be an individual or legal entity, internal or outsourced, and waives the formal indication for small-scale agents while keeping the communication-channel duty — verify the current small-agent carve-outs. Unlike GDPR, the default posture is that a DPO is expected, not the exception.
- **Security measures (Arts. 46–49).** Processing agents must adopt security, technical, and administrative measures able to protect personal data from unauthorized access and from accidental or unlawful destruction, loss, alteration, communication, or diffusion — from the design phase through execution (Art. 46 §2 embeds privacy by design). Art. 49 requires systems to be structured to meet security requirements and good practice standards. The ANPD has published a minimum-security guide for small processing agents that doubles as a de facto baseline expectation.
- **Good practice and governance programs (Art. 50).** Controllers may (and, at enforcement time, are effectively expected to) implement a privacy governance program: demonstrable commitment, applicable to all personal data, adapted to structure/scale/volume and to risk, with policies, training, incident-response plans, and periodic review. Art. 50 program evidence functions like GDPR accountability evidence — it is a fine-mitigation factor under the ANPD's sanction-dosimetry regulation.
- **Records of processing (Art. 37).** Controllers and processors must keep records of their processing operations — the LGPD analogue to GDPR Art. 30, with less prescriptive content.
- **Data Protection Impact Report (RIPD, Art. 38).** The ANPD may require a controller to produce an impact report; ANPD guidance identifies high-risk processing (large scale, sensitive data, vulnerable subjects, new technologies) as the trigger zone. Maintain DPIA-style documentation for high-risk processing so an ANPD demand is a retrieval exercise, not a drafting one — see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).

## Security incident notification (Art. 48)

- **Trigger:** a security incident that may cause **relevant risk or damage** to data subjects. The controller notifies both the **ANPD** and the **affected data subjects**.
- **Deadline:** the statute says "within a reasonable time"; the ANPD's incident-reporting regulation (CD/ANPD Resolution No. 15/2024) fixed it at **3 business days** from the controller's knowledge that the incident affected personal data — verify the current text and counting rules before relying on it. Incomplete initial filings can be supplemented (the regulation contemplates a supplementation window), but late filings attract scrutiny.
- **Relevant risk:** the ANPD regulation defines when an incident is reportable — broadly, incidents involving sensitive data, children/adolescents, financial data, large scale, or capacity to cause material/moral damage. Non-reportable incidents must still be **recorded internally** with the assessment rationale; the ANPD can inspect the register.
- **Content:** description of the affected data, subjects involved, technical and security measures used (respecting trade secrets), risks, reasons for any delay, measures taken/planned. Processor ("operador") duty: inform the controller — pin a tight contractual clock, the regulation's deadline runs against the controller.
- Cross-regime note: Central Bank cyber rules (Resolution CMN 4,893 and successors) impose separate incident handling and reporting expectations on financial institutions. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## International transfers (Arts. 33–36)

- Permitted routes: adequacy (countries/organizations the ANPD deems to provide an adequate level of protection), safeguards (standard contractual clauses, specific contractual clauses, global corporate norms — the BCR analogue, seals/certificates/codes of conduct), plus derogations (consent with specific highlighted information, legal cooperation, life protection, public policy, ANPD authorization).
- The **ANPD's 2024 international transfer regulation (CD/ANPD Resolution No. 19/2024)** operationalized the chapter: it published Brazil's **standard contractual clauses**, set a transition window to incorporate them into existing contracts, defined the process for recognizing equivalent clauses (including a path for recognizing EU SCCs as equivalent — verify current status of any such recognition), and framed the future adequacy-decision process. No adequacy decisions were in place at the time the regulation issued — check the ANPD's current list before assuming any.
- Practical default for multinationals: execute the ANPD SCCs (or ANPD-recognized equivalent clauses) for Brazil-outbound flows, and inventory transfers now — the transition deadline for legacy contracts is a compliance date, not a suggestion.

## Sanctions and enforcement maturity (Arts. 52–54)

- Sanction menu: warning with correction deadline; simple fine (up to 2% of Brazil-sourced group revenue, capped at **R$50M per infraction**); daily fine (same cap); publicization of the infraction; blocking and deletion of the personal data involved; and, for repeat cases, partial suspension of the database, suspension of the processing activity, or partial/total prohibition of processing.
- The ANPD's sanction-dosimetry regulation (2023) sets calculation methodology: classification of infractions (light/medium/severe), base-fine ranges keyed to revenue, aggravators (recidivism, non-cooperation) and mitigators (good-practice programs per Art. 50, prompt remediation, self-report).
- **Enforcement pattern:** the ANPD's first fines (from mid-2023) were small and aimed at non-cooperation and basic failures (first against a small telemarketing firm; public-sector reprimands followed); activity has since scaled up — preventive orders, processing-suspension orders against high-profile AI training uses, and sectoral sweeps. Courts run a parallel track: Brazilian consumer bodies (Procons, Senacon) and the Ministério Público pursue data cases under LGPD and the Consumer Defense Code, and labor courts apply LGPD to employee data. Expect the litigation exposure, not just the ANPD fine, to drive risk.

## Key obligations for security/GRC teams

1. **Adapt, don't duplicate, the GDPR program:** re-point the record of processing to Art. 37, add the Brazil-specific bases (credit protection; health-professional basis) to the lawful-basis register, and re-derive the sensitive-data flows against Art. 11's narrower basis list.
2. **Appoint and publish the encarregado** — decide internal vs. outsourced, publish identity and contact channel on the privacy notice, and register the interface duties (data-subject channel + ANPD contact) in the RACI.
3. **Tune the breach process to 3 business days:** knowledge-to-assessment triage keyed to the ANPD's relevant-risk criteria, ANPD portal filing playbook (Portuguese-language), subject-notification templates, the non-notified incident register, and processor notification SLAs shorter than the regulatory clock.
4. **Stand up Art. 50 governance evidence** — it is the explicit fine mitigator: documented program, training records, incident-response plan tests, periodic reviews.
5. **Remediate transfers:** inventory Brazil-outbound flows, execute ANPD SCCs or recognized equivalents within the transition window, and track ANPD adequacy/equivalence decisions — see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
6. **Operate rights handling on the 15-day clock** with immediate simplified confirmation — faster than GDPR's one month for the full declaration; build the retrieval path accordingly.
7. **Prepare the RIPD on demand:** maintain impact assessments for high-risk processing so an ANPD demand under Art. 38 can be answered from the shelf.
8. **Watch the sector overlays:** BCB cyber and outsourcing rules for financial institutions, ANS for health plans — these carry their own control and reporting expectations on top of LGPD.

## Interplay

- **Versus [GDPR](./gdpr.md):** same skeleton — extraterritorial scope, principles, rights, DPO, breach notification, transfer mechanisms, accountability. Key deltas:
  - **Ten legal bases** vs. six, including credit protection; legitimate interests exists but sensitive data cannot use it.
  - **DPO broadly expected** for controllers generally, vs. GDPR's conditional triggers (with ANPD small-agent relief).
  - **Fines are Brazil-revenue-based and capped** (2% of Brazil revenue, R$50M per infraction) vs. GDPR's uncapped 4% of worldwide turnover — materially lower ceiling for multinationals, but per-infraction stacking and litigation exposure narrow the gap.
  - **Breach clock:** 3 business days (regulation-set) vs. GDPR's 72 calendar hours — similar magnitude, different counting; a Friday incident plays out differently under each.
  - **Automated-decision review (Art. 20)** does not guarantee human review, unlike GDPR Art. 22.
  - **Transfers:** ANPD-issued SCCs and a young adequacy framework vs. the mature EU apparatus; Brazil is itself not EU-adequate, so EU-to-Brazil flows need EU SCCs plus a TIA while Brazil-to-EU flows need an LGPD route.
- A single incident affecting EU and Brazil data subjects triggers both regimes with different clocks and content requirements — run them from one incident record ([../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md)).
- Regional context: Brazil anchors the Latin American privacy landscape; Argentina, Colombia, Chile, and Mexico run their own regimes (not covered by dedicated packs here — see [other-jurisdictions.md](other-jurisdictions.md)).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
