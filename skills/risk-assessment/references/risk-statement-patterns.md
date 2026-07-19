# Risk Statement Patterns: Good vs Bad

A risk statement describes an uncertain **event** and its consequences — something that could happen on a specific date. It is not a missing control, not a worry, not a category, and not a fact. Weak statements produce unscoreabe registers: nobody can rate the likelihood of "lack of MFA", and the impact of "cloud" is undefined.

## The pattern

> **Risk that [EVENT] due to [CAUSE / DRIVER(S)] resulting in [CONSEQUENCE(S)].**

- **Event** — the thing that happens: an incident, failure, or loss. Must be observable ("attacker exfiltrates the customer database", not "data security is weak").
- **Cause / driver** — the condition, threat, or control weakness that makes the event plausible. Control gaps live here. Multiple drivers are fine.
- **Consequence** — the business harm: financial loss, outage, regulatory action, contractual breach, safety, reputation. Name the categories that will drive the impact score.

Tests before registering a statement:

1. **Date test** — could this event happen on a Tuesday? "Insufficient logging" cannot happen on a Tuesday; "an intrusion goes undetected for 60 days" can.
2. **Likelihood test** — can two informed people debate how likely the event is? If the statement is a fact ("we have no DR site"), it has likelihood 100% and is a driver, not a risk.
3. **So-what test** — does the consequence name a harm the business recognizes? "Resulting in non-compliance" is usually a half-step; name what non-compliance costs (fines, lost certification, lost contracts).
4. **Single-event test** — one event per statement. "Risk of breach, outage, and fraud" is three risks.

## Anti-patterns

| Anti-pattern | Example | Why it fails |
|---|---|---|
| Control-gap-as-risk | "Lack of MFA on VPN" | A fact, not an event. Likelihood is meaningless. |
| Category-as-risk | "Cloud security risk" | Unscoreabe; no event, cause, or consequence. |
| Consequence-only | "Risk of reputational damage" | No event to prevent or detect; every risk ends here. |
| Cause-only | "Risk of phishing" | Phishing is a vector; the risk is what phishing enables. |
| Compound risk | "Risk of ransomware, insider theft, and vendor failure" | Cannot be scored or owned as one item. |
| Aspiration inversion | "Risk that we fail to implement Zero Trust" | Registers a project miss, not a business harm. Score the harm the project prevents. |
| Audit finding verbatim | "Patch SLAs not met for 34% of critical vulns" | An observation. Convert: it is a driver of an exploitation event. |

## Worked examples (bad → good)

### 1. Identity / access
- **Bad:** "Lack of MFA on remote access."
- **Good:** "Risk that an attacker gains VPN access using stolen employee credentials due to absence of MFA on remote access, resulting in unauthorized access to internal systems, data theft, and incident response cost."

### 2. Ransomware
- **Bad:** "Ransomware risk."
- **Good:** "Risk that ransomware encrypts production servers and reachable backups due to phishing-delivered initial access and flat network segmentation, resulting in multi-day outage of core services, recovery costs, and contractual penalties."

### 3. Patching
- **Bad:** "Critical patches are applied late."
- **Good:** "Risk that an internet-facing application is compromised via exploitation of a known vulnerability due to patch deployment routinely exceeding the 14-day SLA, resulting in data breach, regulatory notification obligations, and remediation cost."

### 4. Third party / supply chain
- **Bad:** "Vendor risk."
- **Good:** "Risk that customer personal data is exposed through a breach at the outsourced billing provider due to limited assurance over the provider's security controls, resulting in notification obligations, regulatory scrutiny, and customer churn."

### 5. Cloud misconfiguration
- **Bad:** "S3 buckets may be public."
- **Good:** "Risk that sensitive data in cloud object storage is exposed publicly due to misconfigured access policies and absence of automated configuration monitoring, resulting in data breach disclosure, regulatory penalties, and loss of enterprise customers."

### 6. Insider
- **Bad:** "Insider threat."
- **Good:** "Risk that a departing employee exfiltrates customer lists and pricing data due to broad file-share access and no DLP monitoring on egress channels, resulting in competitive harm and breach of customer confidentiality commitments."

### 7. Business email compromise
- **Bad:** "Phishing risk to finance team."
- **Good:** "Risk that a fraudulent payment is executed following compromise or spoofing of an executive mailbox due to weak payment-change verification procedures, resulting in direct financial loss and audit findings over payment controls."

### 8. Availability / resilience
- **Bad:** "No tested DR plan."
- **Good:** "Risk that a data-center or cloud-region failure causes an extended outage of customer-facing services due to untested failover and single-region architecture, resulting in SLA breaches, revenue loss, and customer attrition."

### 9. Data governance
- **Bad:** "Data retention policy not enforced."
- **Good:** "Risk that personal data held beyond its lawful retention period is exposed in a breach or regulator inquiry due to absent automated deletion, resulting in enlarged breach scope, higher penalties, and remediation effort disproportionate to the data's value."

### 10. Shadow IT / SaaS sprawl
- **Bad:** "Users adopt unapproved SaaS."
- **Good:** "Risk that corporate data is stored in unmanaged SaaS applications outside security monitoring and contractual protection due to absent SaaS discovery and procurement bypass, resulting in unrecoverable data exposure and inability to meet deletion or disclosure obligations."

### 11. Privileged access
- **Bad:** "Too many domain admins."
- **Good:** "Risk that an attacker escalates a single workstation compromise to full domain control due to excessive standing privileged accounts and shared admin credentials, resulting in enterprise-wide compromise and full rebuild cost."

### 12. AI / emerging technology
- **Bad:** "AI risk."
- **Good:** "Risk that confidential data is disclosed through employee use of public generative-AI tools due to absent usage policy and controls, resulting in loss of trade-secret protection and breach of customer confidentiality obligations." (For AI system governance itself, see the ai-governance skill.)

### 13. Logging / detection
- **Bad:** "Insufficient logging coverage."
- **Good:** "Risk that an intrusion persists undetected for weeks due to log coverage gaps on critical servers and no alerting on anomalous authentication, resulting in escalated breach scope, higher recovery cost, and regulator criticism of detection capability."

### 14. Legacy technology
- **Bad:** "Windows Server 2012 still in use."
- **Good:** "Risk that unsupported servers hosting the manufacturing execution system are compromised via unpatched vulnerabilities due to end-of-life operating systems with no vendor patches, resulting in production stoppage and safety-system exposure."

### 15. Regulatory / compliance-driven
- **Bad:** "Risk of GDPR non-compliance."
- **Good:** "Risk that a personal-data breach is notified late or incompletely to the supervisory authority due to unclear breach-assessment ownership and untested reporting procedures, resulting in aggravated regulatory penalties and enforcement action beyond the breach itself." (Timelines: see ../../../context/crosswalks/breach-notification-timelines.md.)

## Converting findings into risks

Audit findings, pen-test results, and gap-assessment outputs arrive as facts. Convert each with three questions:

1. **What event does this fact make more likely or more severe?** (fact → driver)
2. **Which asset/process would that event hit?** (scope)
3. **What would the business lose?** (consequence)

Multiple findings often collapse into one risk: "no MFA", "flat network", and "stale admin accounts" are three drivers of one "enterprise compromise via credential attack" risk. Register the risk once; list all drivers; map each treatment action to the driver it removes.

## Style rules

- One sentence if possible; two maximum. Cut adjectives ("significant", "potential" — every risk is potential).
- Present tense, active voice. Name systems and data classes, not "certain assets".
- Never embed the score or the treatment in the statement — those live in their own register fields.
- Title ≤10 words, led by the event: "Ransomware outage of order-management platform", not "Cybersecurity".

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
