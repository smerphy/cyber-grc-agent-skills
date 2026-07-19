# GLBA and the FTC Safeguards Rule for Security Teams

## At a glance

| Item | Detail |
|---|---|
| Law | Gramm-Leach-Bliley Act (1999), Title V — privacy and safeguarding of nonpublic personal information (NPI) |
| FTC rule | Safeguards Rule, 16 CFR Part 314, substantially amended 2021 (main elements effective June 2023) |
| FTC scope | Non-bank "financial institutions": auto dealers, mortgage brokers/lenders, payday lenders, tax preparers, accountants, collection agencies, finders, wire transferors, check cashers, investment advisers not SEC-registered, higher-ed institutions handling federal financial aid |
| Banking regulators | OCC/Fed/FDIC (and NCUA for credit unions) apply the Interagency Guidelines Establishing Information Security Standards instead |
| FTC breach notification | 2023 amendment: notify the FTC within **30 days** of discovering a notification event involving unencrypted customer information of **500+ consumers** (effective May 2024) |
| Banking-org incident notification | Computer-Security Incident Notification Rule: notify primary federal regulator within **36 hours** of determining a notification incident occurred (effective 2022) |
| Small-business carve-out | Institutions maintaining information on **fewer than 5,000 consumers** are exempt from some elements (written risk assessment, continuous monitoring/pen-testing cadence, IR plan, annual board report) |
| SEC/CFTC-regulated firms | Covered by Regulation S-P (SEC) / analogous rules, not the FTC Safeguards Rule |

## Who is covered — the FTC's broad reach

GLBA defines "financial institution" by activity, not charter: any business significantly engaged in financial activities. Under FTC jurisdiction this sweeps in organizations that rarely think of themselves as financial institutions:

- **Auto dealers** that arrange or extend financing or leasing.
- **Mortgage brokers, non-bank lenders, payday lenders.**
- **Tax preparation firms and accountants.**
- **Higher-education institutions** administering federal student aid (Title IV) — the Department of Education enforces Safeguards Rule compliance through the FSA program participation agreement, and audits check it.
- **Debt collectors, credit counselors, financial advisors, real estate settlement services, check-cashing businesses, wire transfer services.**
- **"Finders"** — businesses that connect buyers and sellers of financial products.

The rule protects **customer information**: any record containing NPI about a customer of a financial institution, handled by you or your affiliates — including information you hold about customers of *other* financial institutions.

## FTC Safeguards Rule — required elements of the information security program

The program must be **written**, and appropriate to the institution's size, complexity, and the sensitivity of information. Required elements (16 CFR 314.4):

1. **Qualified Individual.** Designate one qualified individual responsible for overseeing, implementing, and enforcing the program. May be an employee, affiliate, or service provider (a "vCISO" is permissible) — but if outsourced, a senior employee must supervise and the institution retains responsibility.
2. **Written risk assessment.** Identify reasonably foreseeable internal and external risks to customer information; must be written, must state criteria for evaluating risks and the adequacy of safeguards, and must be **periodically reassessed**. (See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).)
3. **Safeguards to control the assessed risks**, specifically including:
   - **Access controls:** authenticate users and limit access to customer information to those with a business need; periodic review of access.
   - **Data and system inventory:** know where customer information is collected, stored, and transmitted, and on which systems.
   - **Encryption** of customer information **at rest and in transit** over external networks. If encryption is infeasible, the Qualified Individual must approve in writing an effective compensating control.
   - **Secure development practices** for in-house applications handling customer information, and procedures to evaluate the security of externally developed applications.
   - **Multi-factor authentication** for any individual accessing any information system holding customer information, unless the Qualified Individual approves in writing a reasonably equivalent control.
   - **Secure disposal** of customer information no later than two years after last use for a business purpose (unless retention is required or disposal infeasible), plus periodic review of retention.
   - **Change management** procedures.
   - **Logging and monitoring** of authorized user activity, and detection of unauthorized access or use.
4. **Regular testing and monitoring.** Either **continuous monitoring** of systems, or, absent that: **annual penetration testing** plus **vulnerability assessments at least every six months** (and after material changes). This cadence is explicit in the rule — build it into the security calendar.
5. **Training and personnel.** Security awareness training for staff; qualified security personnel (own or provider); keep them current on threats.
6. **Service provider oversight.** Select providers capable of maintaining appropriate safeguards, **require safeguards by contract**, and **periodically assess** providers based on risk. (See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).)
7. **Program evaluation and adjustment** based on testing results, operational changes, and risk assessment updates.
8. **Written incident response plan** covering goals, internal processes, roles and decision authority, communications, remediation of systems and weaknesses, documentation of incidents, and post-incident revision.
9. **Annual written report to the board** (or equivalent governing body / senior officer) by the Qualified Individual: overall program status, compliance with the rule, and material matters — risk assessment results, testing results, security events and responses, and recommendations for change.

The 2021 amendment made the rule unusually prescriptive for FTC regulation — MFA, encryption, and the testing cadence are checkable line items in enforcement, not aspirations.

## FTC breach notification (2023 amendment)

- Trigger: a **notification event** — acquisition of **unencrypted** customer information without authorization (information is treated as unencrypted if the encryption key was also compromised; unauthorized acquisition is presumed on unauthorized access unless reliable evidence shows otherwise).
- Threshold: event involves the information of **at least 500 consumers**.
- Deadline: report to the FTC **as soon as possible and no later than 30 days after discovery**, via the FTC's online portal.
- Content: institution name and contact, description of types of information involved, date/date-range if determinable, number of consumers affected, general description of the event; whether a law-enforcement official has requested a public-disclosure delay.
- **Reports are published** on the FTC website — assume public exposure.
- This is regulator notification only; **consumer notification** obligations still come from state breach laws (see [us-state-privacy.md](us-state-privacy.md)) and, for higher-ed and other sectors, additional regimes.

## The banking-regulator side

Depository institutions answer to their prudential regulators, not the FTC:

- **Interagency Guidelines Establishing Information Security Standards** (issued under GLBA s501(b)): board-approved written program, risk assessment, access controls, encryption consideration, testing, service provider oversight, board reporting — conceptually parallel to the Safeguards Rule but principles-based, examined during safety-and-soundness exams. Supplemental guidance requires customer notice programs for unauthorized access to sensitive customer information.
- **Computer-Security Incident Notification Rule** (OCC/Fed/FDIC, effective 2022): a **banking organization** must notify its primary federal regulator **as soon as possible and no later than 36 hours** after determining that a **notification incident** occurred — an incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, operations, lines of business, or operations whose failure would threaten US financial stability. Notification is a simple alert (email/phone acceptable), not a detailed report.
- The same rule requires **bank service providers** to notify each affected banking-organization customer **as soon as possible** after determining an incident has caused or is reasonably likely to cause material service disruption for four or more hours — if you sell services to banks, this clause lands in your contracts and IR plan.
- Credit unions: NCUA requires reporting of reportable cyber incidents within **72 hours**.

## Interaction with other regimes

- SEC-registered broker-dealers, investment companies, and advisers: **Regulation S-P** (amended 2024 to add incident response and customer notification requirements) — out of FTC scope but the same GLBA root.
- State insurance regulators: NYDFS Part 500 and NAIC Insurance Data Security Model Law analogues run in parallel for insurers.
- Map all applicable notification clocks side by side: [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## Key obligations for security/GRC teams

1. Confirm scope honestly — activity-based analysis of whether the organization (or a business line) is a GLBA financial institution, and which regulator applies (see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md)).
2. Name the Qualified Individual in writing; if outsourced, document the supervising senior employee.
3. Maintain the written risk assessment with stated evaluation criteria; refresh on a defined cycle.
4. Evidence the prescriptive controls: MFA coverage for all systems holding customer information, encryption at rest/in transit, data inventory, disposal within the two-year rule, change management, activity logging.
5. Run the testing cadence — continuous monitoring, or annual pen test + semiannual vulnerability assessments — and retain reports.
6. Contractually obligate and periodically reassess service providers handling customer information.
7. Keep the incident response plan current and rehearsed; pre-build the FTC 30-day report template and (for banking organizations) the 36-hour regulator alert path.
8. Deliver the annual written board report; keep board minutes reflecting it (see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md)).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
