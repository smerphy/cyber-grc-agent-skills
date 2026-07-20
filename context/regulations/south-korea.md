# South Korea: Personal Information Protection Act (PIPA)

## At a glance

| Attribute | Detail |
|---|---|
| Jurisdiction | Republic of Korea |
| Instrument | Personal Information Protection Act (PIPA) 2011, materially amended 2020 (regulator consolidation, Network Act merger) and March 2023 (in force from September 2023, some provisions phased) |
| Regulator | Personal Information Protection Commission (PIPC) — consolidated, independent |
| Who's covered | Personal information controllers (public and private); extraterritorial application to foreign operators processing Koreans' data in connection with the Korean market; local-representative requirement for large foreign providers |
| Breach notification | Notify affected individuals and report to the PIPC within **72 hours** of becoming aware, for breaches meeting thresholds (scale or category based — verify current Enforcement Decree thresholds) |
| Max penalties | Administrative fines up to **3% of turnover** — the 2023 amendment moved the base from violation-related revenue toward total revenue with deductions for demonstrably unrelated revenue (burden on the company); criminal penalties for defined violations |
| Reputation | One of the strictest and most actively enforced regimes in APAC |

## Why Korea is treated as a strict regime

Three compounding factors: a **consent-centric statute** (historically requiring granular, itemized consent for collection, use, third-party provision, and cross-border transfer separately), an **active enforcement record** (the PIPC has imposed some of APAC's largest fines, including landmark penalties against global platforms over behavioral-advertising consent), and **prescriptive security rules** — the Enforcement Decree and PIPC notifications specify concrete technical measures (access-control logging and retention, encryption of resident registration numbers and passwords, network separation for large handlers of resident data — verify current specifics) rather than leaving "appropriate measures" open-ended. Audit against the letter of the PIPC standards, not a generic control baseline.

## The 2023 amendment

The March 2023 amendment (effective September 2023, phased) modernized the Act. Highlights (verify commencement of each):

- **Expanded lawful bases** beyond consent — notably processing necessary for contract performance and a narrow legitimate-interests-style ground where the controller's justifiable interest "clearly overrides" the data subject's rights — reducing consent fatigue but not eliminating Korea's consent-first culture.
- **Unified online/offline rules:** the special online-provider provisions inherited from the Network Act merger were consolidated so one framework applies to all controllers.
- **Data portability** (phased) and rights regarding **automated decisions** — the right to an explanation and to refuse fully automated decisions with significant effects (commencement phased; verify).
- **Cross-border transfer routes broadened:** beyond consent — contract-necessity disclosures, certification, and transfers to jurisdictions/entities recognized as providing equivalent protection; the PIPC also gained a **transfer suspension order** power.
- **Penalty restructure** to the turnover-based model noted above, plus reduced criminal emphasis in favor of administrative fines.

## Breach notification

Notify **without delay — within 72 hours** of awareness, both to affected data subjects and (for breaches above thresholds, e.g., 1,000+ data subjects, or involving sensitive data or unauthorized external access — verify current decree thresholds) to the PIPC. Required content follows the familiar pattern: what happened, categories affected, countermeasures, contact point, mitigation guidance for individuals. Where full facts are unavailable, report what is known and supplement — the clock is not tolled by an incomplete investigation. Track alongside other regimes in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md); drive with [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Governance requirements

- **Privacy officer (CPO):** every controller must designate one; 2023-era reforms added qualification/independence expectations for large controllers (domestic-resident requirements — verify).
- **CISO designation:** under the Network Act framework, information/communications service providers above size thresholds must designate a CISO and report the designation to the Ministry of Science and ICT; larger firms face exclusive-duty CISO requirements — verify thresholds. Distinct from the CPO; both may be required.
- **ISMS-P certification:** Korea operates a national certification (ISMS and ISMS-P for personal information) mandatory for large ICT service providers by revenue/user thresholds — a real audit with a defined control set, not a self-attestation. Foreign SaaS with large Korean user bases should scope this early.
- **Local representative:** foreign operators above user/revenue thresholds must appoint a Korea-based representative for PIPC matters and user complaints.

## Sensitive and resident registration data

- **Sensitive information** (ideology, health, sexual life, biometrics for identification, criminal records, etc.) requires separate consent or specific legal authority.
- **Resident registration numbers (RRNs)** are quasi-prohibited: processing only where a statute specifically authorizes it, with mandatory encryption and alternative sign-up methods. Systems built for global markets routinely fail this — RRN handling needs Korea-specific engineering.

## Key obligations for security/GRC teams

1. **Consent architecture:** itemized, separately bundled consents (collection/use, third-party provision, cross-border, marketing, sensitive data) with records; leverage the new non-consent bases only after documented analysis.
2. **Implement the prescriptive security notifications** — access logs with defined retention, encryption mandates, network measures for large resident-data handlers — as a compliance checklist mapped into the control set ([../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md)).
3. **72-hour breach runbook** with the dual notification (subjects + PIPC) and threshold triage.
4. **Governance roles staffed:** CPO (and CISO where in scope), local representative if foreign, ISMS-P scoping decision documented.
5. **Cross-border transfer register** with the route per flow, plus outbound-transfer disclosures in privacy notices.
6. **Vendor (consignment) controls:** consignment contracts with required clauses, public disclosure of consignees, and supervision evidence — Korea audits the paper trail.

## Interplay

- **GDPR** ([./gdpr.md](./gdpr.md)): PIPA is comparably strict but differently shaped — consent-first rather than lawful-basis-first, prescriptive security rather than risk-based, and 72h notification to *individuals* as well as the regulator. An EU program is a strong starting chassis; the deltas (RRN, ISMS-P, itemized consent, CISO) are structural, not cosmetic.
- **EU adequacy:** the EU granted Korea adequacy in December 2021, easing EU→Korea flows (covers most PIPA-regulated processing — verify scope).
- **Sector overlays:** credit information (Credit Information Act), financial cloud rules (FSC/FSS), and location information (Location Information Act) carry their own consent and security regimes.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
