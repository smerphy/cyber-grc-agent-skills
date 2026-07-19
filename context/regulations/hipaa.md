# HIPAA (Health Insurance Portability and Accountability Act)

US federal law governing protected health information (PHI). The operative rules are the Privacy Rule, Security Rule, and Breach Notification Rule at 45 CFR Parts 160 and 164, as amended by the HITECH Act (2009) and the 2013 Omnibus Rule. HIPAA is sectoral: it covers specific entity types, not health data generally — a fitness app with no covered-entity relationship is outside HIPAA (but may be inside FTC Health Breach Notification Rule or state health-privacy laws like Washington's My Health My Data).

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | United States (federal); preempts less-protective state law, floor not ceiling — stricter state laws survive |
| In force since | HIPAA enacted 1996; Privacy Rule compliance 2003; Security Rule compliance 2005; Breach Notification Rule 2009; Omnibus Rule 2013 |
| Regulator | HHS Office for Civil Rights (OCR); state AGs also empowered under HITECH; DOJ for criminal violations (42 U.S.C. §1320d-6) |
| Max penalties | Civil money penalties in four culpability tiers, inflation-adjusted, with annual caps per violation type (top tier historically up to ~$1.5M–$2M per year per provision — verify current adjusted figures); criminal penalties up to $250,000 and 10 years imprisonment for offenses with intent to sell/harm |
| Who's covered | Covered entities (health plans, healthcare clearinghouses, healthcare providers that transmit standard electronic transactions) and their business associates and subcontractors |
| Private right of action | None under HIPAA itself; state negligence suits often cite HIPAA as the standard of care |

## Covered entities and business associates

**Covered entities (CEs):**
- **Health plans** — insurers, HMOs, employer group health plans (the plan, not the employer as such), Medicare/Medicaid.
- **Healthcare clearinghouses** — entities converting nonstandard health transactions to standard formats.
- **Healthcare providers** — but only those that transmit health information electronically in connection with a HIPAA standard transaction (claims, eligibility, etc.). In practice, nearly all providers that bill insurance.

**Business associates (BAs) — the test:** a person or entity that, on behalf of a CE (or another BA), **creates, receives, maintains, or transmits PHI** to perform a function or service. Includes claims processing, billing, analytics, cloud hosting, IT services, and legal/accounting services involving PHI. Post-Omnibus, BAs are **directly liable** under the Security Rule, the Breach Notification Rule, and applicable Privacy Rule provisions — "we're just the vendor" is not a defense. Subcontractors of BAs are themselves BAs, all the way down the chain.

Key edge cases:
- **Conduit exception** — narrow: entities with only transient, random access (couriers, ISPs). Persistent storage of PHI (cloud providers) is BA status even if data is encrypted and the provider lacks keys, per OCR cloud guidance.
- **Hybrid entities** — organizations with covered and non-covered functions may designate healthcare components to fence HIPAA scope.
- **Workforce vs. BA** — employees and volunteers are workforce (trained and sanctioned internally), not BAs.

**Business associate agreements (BAAs):** required before any PHI disclosure to a BA (45 CFR §164.504(e)). Must establish permitted uses/disclosures, prohibit use beyond the contract or as required by law, require safeguards, require breach/security-incident reporting to the CE, flow obligations to subcontractors via downstream BAAs, provide for access/amendment/accounting support, allow HHS audit, and require return/destruction of PHI at termination (or extended protections if infeasible). Operating without a BAA is itself a violation and is regularly the lead finding in OCR settlements. Fold BAA verification into vendor onboarding — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

## Privacy Rule essentials

Governs all PHI in any form (oral, paper, electronic). **PHI** = individually identifiable health information held or transmitted by a CE or BA, relating to health condition, treatment, or payment. Excludes employment records held by an employer as employer, and de-identified data.

- **Use/disclosure baseline** — PHI may be used or disclosed without authorization for **treatment, payment, and healthcare operations (TPO)**, and for specified public-interest purposes (public health, law enforcement under conditions, judicial proceedings, etc.). Everything else requires a valid **written authorization** — notably marketing, sale of PHI, and most psychotherapy-notes uses.
- **Minimum necessary** — for uses/disclosures other than treatment, limit PHI to the minimum necessary for the purpose. Applies to internal role-based access — the bridge between the Privacy Rule and access-control engineering.
- **Notice of Privacy Practices (NPP)** — required from most CEs.
- **Individual rights** — access to PHI in a designated record set (30 days, one 30-day extension; the access right is an OCR enforcement-initiative focus with a long run of penalties for slow or denied access); amendment; accounting of disclosures; restriction requests (must honor the restriction on disclosures to a health plan when the individual paid in full out of pocket); confidential communications.
- **De-identification (§164.514)** — two methods: **Safe Harbor** (removal of 18 specified identifiers plus no actual knowledge of re-identifiability) or **Expert Determination** (documented statistical/scientific justification of very small re-identification risk). De-identified data is outside HIPAA.
- **Limited data set** — dates and some geography retained; usable for research, public health, and operations under a data use agreement.
- **Reproductive health privacy** — a 2024 Privacy Rule amendment restricted certain uses/disclosures of reproductive health information and added an attestation requirement; a 2025 federal district court decision vacated the amendment in substantial part nationwide, leaving only limited provisions standing — verify current enforceability before relying on it.

## Security Rule structure

Applies to **ePHI** only (electronic PHI). Deliberately technology-neutral and scalable: measures must be reasonable and appropriate given size, complexity, capabilities, cost, and risk (§164.306(b) flexibility factors).

Three safeguard categories, each composed of **standards** with **implementation specifications** that are either **Required (R)** or **Addressable (A)**:

- **Addressable does NOT mean optional.** For each addressable specification, assess whether it is reasonable and appropriate; implement it, or document why not and implement an equivalent alternative measure. The assessment and decision must be documented either way.

### Administrative safeguards (§164.308)

- **Security management process** — including the **risk analysis (R)** (§164.308(a)(1)(ii)(A)): an accurate, thorough, enterprise-wide assessment of risks to all ePHI. The most-cited failure in OCR enforcement — a scoped-down or stale risk analysis is treated as no risk analysis. Also risk management (R), sanction policy (R), information system activity review (R).
- **Assigned security responsibility** — a named security official (R).
- **Workforce security** — authorization/supervision, clearance, termination procedures (A).
- **Information access management** — access authorization and establishment/modification (R/A mix).
- **Security awareness and training** — reminders, malware protection, log-in monitoring, password management (A).
- **Security incident procedures** — identify, respond, mitigate, document (R).
- **Contingency plan** — data backup plan (R), disaster recovery plan (R), emergency mode operation plan (R), testing and criticality analysis (A).
- **Evaluation** — periodic technical and nontechnical evaluation (R).
- **BA contracts** (R).

### Physical safeguards (§164.310)

- **Facility access controls** — contingency operations, security plan, access control/validation, maintenance records (A).
- **Workstation use** and **workstation security** (R).
- **Device and media controls** — disposal (R), media re-use (R), accountability (A), data backup before movement (A). Improper disposal (drives, copiers, paper) is a recurring settlement fact pattern.

### Technical safeguards (§164.312)

- **Access control** — unique user identification (R), emergency access procedure (R), automatic logoff (A), **encryption and decryption (A)**.
- **Audit controls** — record and examine activity in systems containing ePHI (R).
- **Integrity** — mechanisms to authenticate ePHI (A).
- **Person or entity authentication** (R).
- **Transmission security** — integrity controls (A), **encryption (A)**.

Encryption being addressable is the classic trap: it is nearly always "reasonable and appropriate," and unencrypted lost laptops/media are among the most-penalized scenarios — plus encryption per NIST parameters is the safe harbor that avoids breach notification entirely. Also required: documentation and policy retention for **6 years** from creation or last effective date (§164.316), review and periodic update of documentation.

Map Security Rule safeguards to your control framework once (they align naturally with [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md); NIST SP 800-66 Rev. 2 is the implementation guide) — see [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

## Breach Notification Rule (§§164.400–414)

**Breach** = acquisition, access, use, or disclosure of unsecured PHI in violation of the Privacy Rule, which is **presumed reportable** unless the CE/BA demonstrates a **low probability of compromise** via a documented risk assessment covering at minimum four factors (§164.402):

1. Nature and extent of the PHI involved (identifiers, likelihood of re-identification);
2. The unauthorized person who used/received the PHI;
3. Whether the PHI was actually acquired or viewed;
4. The extent to which the risk has been mitigated.

Three regulatory exceptions: good-faith unintentional workforce access, inadvertent internal disclosures between authorized persons, and disclosures where the recipient could not reasonably retain the information. **Unsecured PHI** means not rendered unusable/unreadable/indecipherable per HHS guidance (encryption to NIST standards; destruction) — the encryption safe harbor removes the notification duty.

Notification obligations (clock runs from **discovery** — first day the breach is known or would have been known with reasonable diligence, imputed from any workforce member or agent):

- **Individuals** — written notice by first-class mail (or email if agreed) **without unreasonable delay and in no case later than 60 calendar days** after discovery. Substitute notice (website posting 90 days + media, or alternative) when contact information is insufficient for 10+ individuals. Content requirements: what happened, PHI involved, steps individuals should take, what the entity is doing, contact procedures.
- **HHS (OCR)** — breaches affecting **500 or more individuals**: notify HHS **contemporaneously with individual notice** (same 60-day outer bound). Breaches affecting **fewer than 500**: log and submit annually via the HHS portal **within 60 days after the end of the calendar year**.
- **Media** — breaches affecting **more than 500 residents of a single state or jurisdiction**: notify prominent media outlets serving that state, same timing as individual notice.
- **BA to CE** — BAs must notify the CE without unreasonable delay and no later than 60 days after discovery; the CE owns individual/HHS/media notice unless delegated. Contractually shorten the BA window (commonly 5–15 days, sometimes 72 hours) in the BAA — 60 days leaves the CE no runway.

Law-enforcement delay is available on official request. The 500+ list is published on the public HHS breach portal ("wall of shame") and routinely triggers an OCR investigation. State breach laws apply in parallel and may be stricter — see [us-state-privacy.md](us-state-privacy.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md); coordinate via [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Enforcement

- **OCR** investigates complaints, breach reports, and conducts compliance reviews/audits; resolves via technical assistance, resolution agreements with corrective action plans (CAPs, typically 2–3 years of monitoring), or civil money penalties.
- **Penalty tiers** (culpability-based, per HITECH, inflation-adjusted annually — verify current figures): (1) did not know and would not have known with reasonable diligence; (2) reasonable cause; (3) willful neglect, corrected within 30 days; (4) willful neglect, not corrected. Per-violation minimums/maximums rise by tier, with annual caps per identical provision; "per violation" can be counted per record or per day of noncompliance.
- **Recurring enforcement themes:** absent or inadequate risk analysis, no BAA, unencrypted devices, right-of-access delays, insufficient audit controls, and ransomware response failures (OCR treats ransomware encryption of ePHI as a presumptive breach requiring the four-factor analysis).
- **State AGs** may bring civil actions under HITECH; DOJ handles criminal cases (knowing misuse, false pretenses, intent to sell — up to 10 years).

## Security Rule NPRM (proposed update)

In late 2024/early 2025, HHS issued a **Notice of Proposed Rulemaking to strengthen the Security Rule** — the first major revision since 2003. Proposed directions included: removing the required/addressable distinction (making specifications uniformly required with limited exceptions), mandatory encryption of ePHI at rest and in transit, mandatory MFA, a written asset inventory and network map, defined vulnerability scanning and penetration testing cadences, network segmentation, tighter incident response and contingency testing requirements (including restoration time objectives), and annual compliance audits and verification of BA safeguards.

**Status: proposed, not final at last review.** Do not treat NPRM elements as current legal requirements; do treat them as the direction of travel worth building toward. Verify whether a final rule has been issued and its compliance dates before advising — track via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Maintain a current, enterprise-wide risk analysis** — covering every system, application, and location touching ePHI, refreshed on schedule and after material change, with a tracked risk-management plan. This is OCR's first document request. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
2. **Inventory ePHI and the BA chain** — you cannot scope the risk analysis, BAAs, or breach response without knowing where ePHI lives and which vendors touch it.
3. **Close the BAA loop** — BAA before PHI flows, subcontractor flow-down verified, breach-reporting windows shortened contractually, termination/return provisions tested.
4. **Encrypt to the safe harbor** — full-disk encryption on endpoints and media, TLS in transit, documented key management; this converts most lost-device incidents into non-events.
5. **Document addressable decisions** — for every addressable specification, a written reasonable-and-appropriate analysis; silence reads as noncompliance.
6. **Operate audit controls and review them** — logging on ePHI systems plus documented periodic review (information system activity review is Required); insider snooping cases turn on this.
7. **Test contingency plans** — backup, DR, and emergency-mode procedures exercised against the ransomware scenario, with evidence retained.
8. **Run the breach clock correctly** — discovery-based, imputed knowledge, four-factor assessments documented for every incident including those deemed non-reportable (burden of proof is on you), pre-built notice templates for individual/HHS/media tracks.
9. **Meet the right of access** — 30-day SLA with tracking; a top OCR enforcement priority.
10. **Retain documentation 6 years** and train workforce with sanctions applied and recorded. Periodic evaluation (§164.308(a)(8)) maps cleanly to control testing — see [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) and [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
