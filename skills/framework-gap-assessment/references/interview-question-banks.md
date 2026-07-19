# Interview Question Banks

Per-domain question banks for gap-assessment interviews. Usage pattern for every domain: open with the walkthrough question ("show me / walk me through"), follow with the specifics, close by requesting one artifact per material claim. Record interviewee name, role, and date against every answer — the gap register cites them.

General technique:

- Ask about the last real occurrence, not the theory: "When did you last actually restore from backup?" beats "Do you test restores?"
- Chase pronouns: "we monitor that" → who is "we", with what tool, reviewed by whom, how often?
- Quantify coverage on every "yes": how many of how many? Since when? What is excluded?
- When answers conflict with documents, note it verbatim; the conflict is a finding.

---

## Part A — NIST CSF 2.0 function banks

Use these when assessing against CSF 2.0 (6 functions, 22 categories). Detail on categories: [../../../context/frameworks/nist-csf-2.md](../../../context/frameworks/nist-csf-2.md). Questions are grouped by function; tag notes with the category they inform.

### Govern (GV)

Primary interviewees: CISO/security lead, executive sponsor, legal/compliance, risk owner.

1. Who is accountable for cybersecurity at executive level, and how is that documented? When did that person last brief the board or owners, and on what?
2. Show me the cybersecurity risk management strategy or equivalent. Who approved it and when was it last reviewed?
3. How does the organization decide how much cyber risk is acceptable? Is there a written risk appetite or tolerance statement anyone can quote?
4. Which laws, regulations, and contractual security obligations apply to you, and where is that list maintained? Who watches for changes? (Cross-check with [../../regulatory-applicability/SKILL.md](../../regulatory-applicability/SKILL.md).)
5. Walk me through the security budget process. Who proposes, who approves, what happened to last year's asks?
6. What security roles exist, and are responsibilities written into job descriptions or a RACI? What happens when the security lead is on leave?
7. How are policies created, approved, communicated, and enforced? Show me the most recently updated policy and its approval trail.
8. How do you oversee supplier/third-party cyber risk — before contract, during, at exit? Who owns that process? (Informs GV.SC; deep-dive via [../../third-party-risk-assessment/SKILL.md](../../third-party-risk-assessment/SKILL.md).)
9. What cyber metrics does leadership see, and can you show me the last pack sent to them?
10. Has an internal or external party ever assessed the security program? What happened to the findings?

### Identify (ID)

Primary interviewees: IT ops lead, asset/CMDB owner, risk owner, engineering lead.

1. Walk me through how you know what hardware, software, systems, and services you have. Show me the inventory; when was this entry last updated, and what populates it — discovery tooling or manual entry?
2. How do unmanaged or unknown devices get detected on your networks?
3. Where is your data inventory or data map? Which systems hold your most sensitive data (personal data, payment data, IP), and how do you know?
4. How are cloud resources and SaaS applications tracked? Who can create a new cloud account or subscribe to a SaaS product, and how would security find out?
5. Walk me through your last risk assessment: method, scope, who participated, where the register lives, and one risk that led to an actual decision. (Method detail: [../../risk-assessment/SKILL.md](../../risk-assessment/SKILL.md).)
6. How do vulnerabilities get identified — scanning coverage and cadence, pen tests, bug reports? Show me the latest scan summary and what happened to its critical findings.
7. How do you learn from incidents and near misses? Show me an improvement that came out of one. (Informs ID.IM.)
8. Which business processes would hurt most if their systems went down, and where is that dependency analysis written down?

### Protect (PR)

Primary interviewees: IT ops, identity admin, HR (awareness), platform/infra engineers.

1. Walk me through the identity lifecycle: a new hire's first day, a role change, and a termination on a Friday afternoon. How fast is access actually revoked, and who checks?
2. Where is MFA enforced, and — more importantly — where is it not? Admin accounts, remote access, email, break-glass accounts, service accounts?
3. How is privileged access granted, recorded, time-limited, and reviewed? Show me the last access review and what it caught.
4. How do you decide who can access what data? Are shared accounts in use anywhere?
5. What security training do people get at joining and periodically? Show completion figures. Do admins/developers get role-specific training? (Informs PR.AT.)
6. How is data protected at rest and in transit? Where does encryption not apply, and why? How are keys and secrets managed?
7. Walk me through patching: how a critical patch reaches all endpoints/servers, target timelines, actual current compliance numbers, and what is knowingly unpatchable.
8. How are systems hardened — is there a baseline/standard image, and how is drift detected?
9. Walk me through backups: what is backed up, where, how often, offline/immutable copies, and the date and result of the last actual restore test. (Informs PR.IR/PR.DS.)
10. How is the network segmented? Could a compromised workstation reach the crown-jewel systems directly?
11. How do changes to production get approved and rolled back? Show me the record for the most recent emergency change.

### Detect (DE)

Primary interviewees: security operations (or whoever fills that role), IT ops, MSSP liaison.

1. What security-relevant logs are collected, from what percentage of the estate, and where do they go? What is knowingly not logged?
2. Who or what looks at alerts, during which hours? What happens to an alert firing at 03:00 on a Sunday?
3. Walk me through the last true-positive alert end to end: detection, triage, escalation, closure. How long did each stage take?
4. How do you detect the classics: impossible-travel logins, mass file changes/encryption, data leaving in bulk, new local admin accounts?
5. How are detection rules created, tuned, and tested? When was a detection last verified to actually fire (purple-team, simulation)?
6. What monitoring covers cloud tenants and SaaS admin activity, not just on-prem?
7. If you use an MSSP/MDR: show me the contract's detection scope, the last monthly report, and an example escalation. Who validates their performance?

### Respond (RS)

Primary interviewees: incident response lead, IT ops, communications/legal.

1. Show me the incident response plan. Who declares an incident, and against what severity definitions?
2. When was the plan last exercised (tabletop or live), who attended, and what changed as a result? Show the after-action report.
3. Walk me through your most recent real incident: timeline, roles, decisions, evidence handling, root cause, lessons.
4. How would you contain a compromised laptop, a compromised cloud admin account, and a ransomware detonation — concretely, with which tools and authority?
5. Who decides on and executes external notifications — regulators, customers, insurers, law enforcement? Are notification deadlines for your regimes documented in the plan? (Deadlines and process: [../../incident-regulatory-reporting/SKILL.md](../../incident-regulatory-reporting/SKILL.md) and [../../../context/crosswalks/breach-notification-timelines.md](../../../context/crosswalks/breach-notification-timelines.md).)
6. Is there retained external help (IR firm, counsel, insurer hotline)? Are the engagement numbers reachable without corporate email or SSO?
7. How is forensic evidence preserved so it survives legal scrutiny?

### Recover (RC)

Primary interviewees: IT ops, business continuity owner, service owners.

1. What are the recovery time and recovery point objectives for the top business services, who set them, and has recovery ever been tested against them?
2. Walk me through the last recovery exercise or real recovery: what was restored, how long it took versus target, what failed.
3. In what order would systems be restored after a site- or estate-wide event, and where is that order written down?
4. How would you operate during a multi-day outage — manual workarounds, alternate comms if email/chat are down?
5. Who communicates recovery status to customers and internally, and against what pre-approved templates?
6. How is "recovered" verified — integrity checks before reconnecting restored systems to production?

---

## Part B — ISO/IEC 27001:2022 banks

Use for ISO 27001 assessments: clauses 4–10 (the ISMS) then Annex A by ISO/IEC 27002:2022 theme. Reference: [../../../context/frameworks/iso-27001-2022.md](../../../context/frameworks/iso-27001-2022.md). For certification mechanics (SoA, audit evidence), switch to [../../iso27001-readiness/SKILL.md](../../iso27001-readiness/SKILL.md).

### Clause 4 — Context of the organization

1. What internal and external issues affect your security objectives, and where are they documented?
2. Who are the interested parties (customers, regulators, insurers, staff) and what are their security-relevant requirements? Show the analysis.
3. Show me the ISMS scope statement. What is excluded and why? Does the scope match what your certificate (or intended certificate) will claim?

### Clause 5 — Leadership

1. How does top management demonstrate commitment beyond signing the policy — budget decisions, attendance, direction-setting? Give a concrete recent example.
2. Show me the information security policy: approval, communication, and how a new employee would encounter it.
3. Which ISMS roles are assigned, and does the assignee know? (Ask the assignee separately.)

### Clause 6 — Planning

1. Walk me through the risk assessment methodology: criteria, scales, ownership, and how results drive the risk treatment plan.
2. Show me the risk treatment plan and the Statement of Applicability. How were Annex A control exclusions justified?
3. What are the measurable information security objectives, and who tracks progress?
4. How are changes to the ISMS planned rather than improvised? (Clause 6.3.)

### Clause 7 — Support

1. How were resource needs for the ISMS determined and met?
2. How is competence for security-relevant roles determined and evidenced (training records, certs, evaluations)?
3. What does the awareness program cover, and how do you know it works?
4. What internal/external communications about the ISMS are planned — who, what, when, how?
5. Walk me through documented-information control: versioning, approval, access, protection against loss. Show a document's history.

### Clause 8 — Operation

1. How do you ensure operational processes run as planned — and how are outsourced processes controlled?
2. How often are risk assessments performed or refreshed, and what triggers an off-cycle one?
3. Show evidence that the risk treatment plan is being executed, not just written: closed treatments, updated residual risks.

### Clause 9 — Performance evaluation

1. What is monitored and measured, by whom, with what methods, and where are results recorded?
2. Show me the internal audit programme and the last internal audit report. Who performed it, and how was independence preserved?
3. Show me the last management review: inputs (per 9.3), decisions, and resulting actions with owners.

### Clause 10 — Improvement

1. Walk me through a recent nonconformity: correction, root-cause analysis, corrective action, effectiveness check.
2. Where do improvement opportunities get captured, and show one implemented in the last year.

### Annex A — Organizational controls theme

(37 controls; sample the highest-signal ones.)

1. How current is the control set against your SoA? Any controls marked implemented that no one currently operates?
2. How is information classified and labeled, and does handling actually differ by class?
3. Walk me through supplier security: requirements in contracts, assessment before onboarding, monitoring, and cloud-service-specific handling.
4. How are security requirements built into projects and new initiatives?
5. Threat intelligence: what sources feed you, and show one action taken from intel.
6. Evidence collection and incident management: covered under CSF RS/DE banks above — reuse them.

### Annex A — People controls theme

(8 controls.)

1. What screening happens before hire, proportionate to role? What about contractors?
2. Where do confidentiality/NDA and security responsibilities appear in employment terms — including post-employment?
3. Walk me through the disciplinary process for a security policy violation. Has it ever been used?
4. What happens security-wise at termination or role change — and who verifies completion?
5. How can staff report security events, and are reports acted on without blame? Show a recent one.
6. Remote-working rules: what is required of home/mobile work environments, and how is it checked?

### Annex A — Physical controls theme

(14 controls.)

1. Walk me through physical entry to areas holding sensitive systems: badges, visitors, tailgating countermeasures, logs. When were access lists last reviewed?
2. How is equipment protected — siting, environmental controls, cabling, maintenance records?
3. Clear desk / clear screen: policy and observed reality (walk the floor if on site).
4. How does equipment and media leave — reuse, repair, disposal? Show a destruction certificate.
5. If offices closed or shrank recently: what happened to the kit that was there?

### Annex A — Technological controls theme

(34 controls; heavy overlap with CSF PR/DE banks — reuse those, then add:)

1. Endpoint protection: what runs on every endpoint class, and what is the current coverage number?
2. How are utility programs and admin tools restricted?
3. Secure development: standards, code review, separation of dev/test/prod, test data handling, dependency and secrets scanning. Show a recent finding fixed pre-release.
4. Web filtering, DLP or equivalent data-leak measures: what exists, what does it actually block, monitored by whom?
5. Configuration management: baselines, drift detection, who may deviate and how it's recorded (link to [../../exception-management/SKILL.md](../../exception-management/SKILL.md)).
6. Logging/monitoring/clock sync: reuse DE bank; additionally, are logs protected from tampering and deletion, including by admins?
7. Cryptography: algorithm/key standards, certificate lifecycle, last expiry-related outage.

---

## Part C — Adapting banks for other frameworks

- **CIS v8:** the CSF banks cover the ground; anchor follow-ups to specific safeguards ("Control 5: show me the account inventory; Control 8: show retention settings"). Consult [../../../context/frameworks/cis-controls-v8.md](../../../context/frameworks/cis-controls-v8.md) and interview against the organization's Implementation Group.
- **SOC 2:** emphasize governance, change management, logical access, and monitoring evidence over a period, plus the additional TSC categories in scope. See [../../../context/frameworks/soc2-tsc.md](../../../context/frameworks/soc2-tsc.md) and [../../soc2-readiness/SKILL.md](../../soc2-readiness/SKILL.md).
- **NIST SP 800-53:** interview per family against the selected baseline; the CSF banks map naturally onto families (AC, AU, IR, CP, CM, etc.). See [../../../context/frameworks/nist-800-53.md](../../../context/frameworks/nist-800-53.md).
- **PCI DSS v4.x:** scope interviews around the CDE first — "where does card data enter, flow, rest, and leave?" — then walk the 12 requirements. See [../../../context/frameworks/pci-dss-4.md](../../../context/frameworks/pci-dss-4.md).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
