# NYDFS Cybersecurity Regulation (23 NYCRR Part 500)

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | New York State (with practical reach to any firm holding a NY financial-services license) |
| Instrument | State regulation: 23 NYCRR Part 500, issued by the NY Department of Financial Services (DFS) |
| Effective | Original rule March 1, 2017; **Second Amendment adopted November 1, 2023**, with phased compliance dates running from December 2023 through November 2025 |
| Regulator | NY DFS — the Superintendent of Financial Services |
| Applies to | "Covered entities": anyone operating under (or required to operate under) a license, registration, charter, certificate, permit, or similar authorization under the NY Banking Law, Insurance Law, or Financial Services Law — banks and foreign bank branches, insurers, insurance producers/agents, money transmitters, mortgage lenders/servicers, virtual currency (BitLicense) firms |
| Penalties | No single fixed cap in Part 500 itself; DFS assesses penalties under the Banking, Insurance, and Financial Services Laws, computed per violation (and in some cases per day). Consent orders have run from roughly $1M to tens of millions |
| Key deadlines | 72-hour notice of cybersecurity events; 24-hour extortion-payment notice + 30-day written explanation; annual compliance submission by **April 15** |

## Why this regulation punches above its weight

Part 500 was the first prescriptive US cybersecurity regulation for financial services and remains the template others copy (the FTC Safeguards Rule amendments and NAIC Insurance Data Security Model Law borrow heavily from it — see [glba-ftc-safeguards.md](glba-ftc-safeguards.md)). Two features make it unavoidable:

1. **Licensing reach.** Coverage follows the license, not the headquarters. An insurer domiciled in Ohio, a money transmitter based in California, or a London bank's New York branch is covered if it holds a NY authorization. Many national firms treat Part 500 as their de facto baseline because their NY license is the strictest thing they hold.
2. **Named-officer accountability.** The rule requires a designated CISO, senior-executive certification of compliance, and (post-amendment) explicit governing-body oversight duties — making it one of the few US regimes where individual executives sign their names to the state of the security program every year.

## Covered entities, class A companies, and exemptions

**Covered entity:** any person operating under or required to operate under a DFS authorization. "Person" includes non-NY entities; agents and employees covered by another covered entity's program can rely on that program (Section 500.19 exemption, still requires filing).

**Class A companies** (added by the Second Amendment, Section 500.1 definitions): larger covered entities — those with at least $20M in gross annual revenue from NY operations (in each of the last two fiscal years) **and** either over 2,000 employees or over $1B in gross annual revenue, counting affiliates per the rule's definitions. Verify the exact thresholds against the current text before classifying. Class A companies carry extra obligations:

- **Independent audit** of the cybersecurity program, conducted at least annually (internal or external auditors free of conflicts).
- **Privileged access management solution** plus an automated method of blocking commonly used passwords (Section 500.7), unless the CISO approves a reasonably equivalent alternative in writing.
- **Endpoint detection and response** and a **centralized logging and security-event alerting solution** (Section 500.14), again with a CISO-approved-alternative escape valve.

**Limited exemptions** (Section 500.19): smaller entities are exempt from a subset of requirements (not from the rule entirely — notification and certification duties remain). The Second Amendment raised the thresholds; they are now on the order of fewer than 20 employees, under $7.5M in gross annual revenue from NY operations over three years, or under $15M in year-end total assets — verify current figures. Exempt entities must file a notice of exemption through the DFS portal.

## Core requirements by section

Section numbers below reflect the amended rule; confirm against the current text before citing in formal documents.

| Section | Requirement |
|---|---|
| 500.2 | Maintain a cybersecurity program based on the risk assessment, covering the core functions (identify, protect, detect, respond, recover) |
| 500.3 | Written cybersecurity policies covering an enumerated topic list, approved at least annually by the **senior governing body** (board or equivalent) |
| 500.4 | Designate a **CISO** (in-house, affiliate, or third-party service provider with a designated internal senior overseer). CISO reports in writing at least annually to the senior governing body and must **timely report material cybersecurity issues** to it. The amendment adds governing-body duties: exercise oversight, require management to implement the program, and have sufficient understanding of cyber matters (or access to advisers who do) |
| 500.5 | Vulnerability management: **annual penetration testing** by a qualified party, automated vulnerability scans (plus manual review of systems scanning misses), timely risk-based remediation, and monitoring for new vulnerabilities |
| 500.6 | Audit trails sufficient to reconstruct material financial transactions (retain ~5 years) and detect/respond to cybersecurity events (retain ~3 years) |
| 500.7 | Access privileges: limit to need, limit privileged accounts and their use, **review all user access privileges at least annually**, disable/remove unnecessary accounts, promptly terminate departed-user access, and maintain a written password policy where passwords are used |
| 500.8 | Secure development practices for in-house applications and evaluation of third-party application security |
| 500.9 | Periodic **risk assessment**, updated at least annually and whenever material changes occur — this is the keystone: most other requirements are calibrated to it |
| 500.10 | Qualified cybersecurity personnel (in-house or vendor) with ongoing training |
| 500.11 | **Third-party service provider security policy**: risk-based due diligence, minimum contractual protections (MFA, encryption, notification), and periodic reassessment |
| 500.12 | **MFA** — post-amendment, MFA is required for remote access to the entity's systems, remote access to third-party applications from which nonpublic information is accessible, and all privileged accounts; the CISO may approve reasonably equivalent compensating controls in writing, reviewed annually. (This broadened MFA mandate was among the last amendment provisions to take effect, in late 2025) |
| 500.13 | Asset management and data retention: written policies for a complete, maintained **asset inventory** (owner, location, classification, support expiration, recovery objectives) and secure disposal of nonpublic information no longer necessary |
| 500.14 | Monitoring and training: risk-based monitoring of user activity, web/email filtering to block malicious content, and **annual security awareness training that includes social engineering** exercises; plus the class A EDR/logging requirements noted above |
| 500.15 | **Encryption** of nonpublic information in transit over external networks and at rest. Compensating controls in lieu of at-rest encryption are permitted only with written CISO approval reviewed at least annually; the amendment removed the compensating-control option for data in transit — verify the current text on this point |
| 500.16 | **Incident response and BCDR**: written IR plan (now explicitly including recovery from backups and root-cause processes) and business continuity/disaster recovery plans, both tested at least annually with relevant staff trained; maintain backups adequately protected from unauthorized alteration or destruction |
| 500.17 | Notices to the superintendent (below) |
| 500.19 | Exemptions (above) |
| 500.20 | Enforcement: the amendment states that a single act prohibited by the rule, or a single failure to secure nonpublic information due to noncompliance, constitutes a violation, and lists mitigating/aggravating factors DFS weighs |

## Notification and certification duties (Section 500.17)

**72-hour cybersecurity event notice.** Notify the superintendent (via the DFS portal) as promptly as possible but no later than **72 hours** after determining that a cybersecurity event has occurred that is any of:

1. An event requiring notice to any other government body, self-regulatory agency, or supervisory authority;
2. An event with a **reasonable likelihood of materially harming any material part of normal operations**; or
3. An event in which **ransomware was deployed** within a material part of the entity's information systems.

The amendment extended this to qualifying events occurring at a **third-party service provider** that affect the covered entity. Covered entities must also provide requested follow-up information and update DFS as material new information becomes available.

**Extortion payments.** If an extortion payment is made in connection with a cybersecurity event: notify the superintendent within **24 hours** of the payment, and within **30 days** provide a written description of why payment was necessary, alternatives considered, diligence performed to find alternatives, and diligence performed to ensure the payment complied with applicable law — including OFAC sanctions rules. Build the sanctions-screening step into the ransomware playbook; the 30-day letter assumes you did it before paying.

**Annual submission by April 15.** Each year, covered entities submit either:

- A **certification of material compliance** for the prior calendar year — signed by the **highest-ranking executive and the CISO** — based on data and documentation sufficient to demonstrate compliance; or
- A **written acknowledgment of noncompliance** identifying the sections not materially complied with and providing a remediation timeline.

The dual-signature design is deliberate: it forces an annual, documented conversation between the CISO and the CEO about gaps. Certifying falsely is itself an enforcement hook — DFS has charged false certification in past actions.

## Enforcement pattern

DFS enforcement has followed a consistent arc worth studying before it studies you:

- Actions typically follow a reported cybersecurity event, then examine the whole program: DFS charges the underlying control failures (commonly MFA gaps, missed risk assessments, weak access controls, unencrypted nonpublic information) *plus* false annual certifications where the entity certified compliance despite known gaps.
- Consent orders have involved insurers, title companies, banking organizations, and crypto firms, with penalties from roughly $1M to $30M+ (larger figures usually bundle BSA/AML findings). Orders routinely require remediation plans, independent consultants, and progress reporting.
- Recurring themes in orders: MFA exceptions that swallowed the rule, incidents known but not reported within 72 hours, and certifications signed without supporting evidence.

## Key obligations for security/GRC teams

1. Confirm scope: inventory every NY license across the corporate family; each licensed entity needs coverage (own program, or documented reliance on an affiliate's program that fully covers it).
2. Determine class A status annually and track the extra obligations (independent audit, PAM, password blocking, EDR, centralized logging).
3. Keep the risk assessment current and demonstrably linked to control decisions — DFS examiners ask for the thread from assessment to control.
4. Operate the calendar: annual pen test, access reviews, policy approval by the governing body, CISO board report, IR and BCDR tests, training with social engineering, April 15 filing.
5. Wire the 72-hour and 24-hour clocks into the IR plan, including the third-party-event trigger and the "reportable elsewhere = reportable to DFS" rule; pre-draft the extortion 30-day letter skeleton with the OFAC diligence checklist.
6. Treat the annual certification as an evidence exercise: assemble the compliance file before anyone signs, and use the acknowledgment-of-noncompliance path honestly when gaps exist — it is far cheaper than a false-certification charge.
7. Push Part 500 minimums (MFA, encryption, notification SLAs) into third-party contracts per Section 500.11.

## Interplay

- An event "requiring notice to any government body" makes Part 500's 72-hour clock parasitic on every other regime you are subject to — map them in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and run them concurrently via [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
- Public-company covered entities run the SEC materiality analysis in parallel — see [sec-cyber-disclosure.md](sec-cyber-disclosure.md); a DFS-reportable event is not automatically SEC-material, and vice versa.
- The FTC Safeguards Rule and state insurance-data-security laws overlap heavily; a Part 500-conformant program usually satisfies most of them — see [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- New York's SHIELD Act and other state breach laws govern consumer notification separately from DFS regulator notice — see [us-state-privacy.md](us-state-privacy.md).
- Part 500's control set maps cleanly onto [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) functions; many firms evidence compliance through a CSF-organized program.

## Primary sources

- [NYDFS cybersecurity resource center (23 NYCRR 500 text, FAQs, filing portal)](https://www.dfs.ny.gov/industry_guidance/cybersecurity)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
