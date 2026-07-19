# Cyber Risk Scenario Starter Library

Twenty scenarios covering the common body of cyber risk. Use as a completeness prompt during identification — walk the list, keep what is plausible for the assessed context, tailor drivers to observed conditions, and discard the rest. Do not paste scenarios into a register untailored: generic entries score poorly and never get owned.

Each entry: the event, typical drivers (candidate causes — verify which apply), and primary impact types (candidate consequence categories — pick what actually drives impact in context).

**Impact type key:** FIN (direct financial loss), OPS (operational disruption), REG (regulatory/legal exposure), REP (reputational harm), CONF (data confidentiality), SAFE (safety).

---

## 1. Ransomware with data encryption and extortion
- **Event:** Attacker encrypts production systems and backups; may exfiltrate data first for double extortion.
- **Typical drivers:** Phishing or exposed remote-access initial entry; flat network; online-only backups; slow patching of edge devices; excessive standing privileges.
- **Impacts:** OPS (primary), FIN (recovery, ransom pressure), REG (if data exfiltrated), REP.

## 2. Business email compromise / payment fraud
- **Event:** Fraudulent payment or payroll/vendor bank-detail change executed after mailbox compromise or convincing spoof.
- **Typical drivers:** No MFA on email; weak payment-change verification (no out-of-band callback); autonomy of single approvers; invoice-process visibility to attacker.
- **Impacts:** FIN (primary), REP, audit findings on payment controls.

## 3. Customer data breach via application exploitation
- **Event:** Internet-facing application exploited (injection, auth bypass, unpatched CVE); customer records exfiltrated.
- **Typical drivers:** Missed patching SLAs; no WAF or misconfigured WAF; secrets in code; insufficient pen-testing of releases.
- **Impacts:** CONF, REG (notification duties — see ../../../context/crosswalks/breach-notification-timelines.md), REP, FIN (response, litigation).

## 4. Credential stuffing / account takeover of customer accounts
- **Event:** Attackers replay breached credentials against customer login at scale; fraud through hijacked accounts.
- **Typical drivers:** No MFA option or low adoption; no bot/rate-limit defenses; password reuse by customers.
- **Impacts:** FIN (fraud reimbursement), REP, REG (depending on data accessed).

## 5. Insider data theft (departing or disgruntled employee)
- **Event:** Employee exfiltrates customer lists, source code, or trade secrets before departure.
- **Typical drivers:** Broad access to shared drives; no egress monitoring/DLP; delayed deprovisioning; no leaver-review process.
- **Impacts:** CONF, competitive/FIN, contractual breach, REP.

## 6. Privileged insider sabotage
- **Event:** Administrator with legitimate access deletes data, disables controls, or plants logic bombs.
- **Typical drivers:** Shared/unmonitored admin accounts; no separation of duties on destructive actions; poor termination coordination for privileged staff.
- **Impacts:** OPS, FIN, SAFE (in OT contexts).

## 7. Software supply chain compromise (upstream dependency or vendor update)
- **Event:** Malicious code enters via a compromised dependency, build pipeline, or signed vendor update.
- **Typical drivers:** No SBOM or dependency vetting; auto-update from vendor without staging; CI/CD pipeline with weak access control.
- **Impacts:** CONF, OPS, incident response FIN, REP (if own product ships the compromise downstream).

## 8. Critical third-party service provider outage
- **Event:** SaaS/cloud/managed-service provider suffers extended outage; dependent business processes stop.
- **Typical drivers:** Single-provider dependency without exit or continuity plan; no contractual RTO; unmapped process-to-provider dependencies.
- **Impacts:** OPS (primary), FIN, SLA breaches. (Assess the vendor itself via the third-party-risk-assessment skill.)

## 9. Third-party data processor breach
- **Event:** Vendor holding your customer or employee data is breached; your data exposed via their environment.
- **Typical drivers:** Weak vendor due diligence; data shared beyond need; no contractual breach-notification clause or audit rights.
- **Impacts:** REG (controller obligations persist), REP, FIN.

## 10. Cloud misconfiguration exposure
- **Event:** Storage bucket, database, or management interface left publicly accessible; data indexed or scraped.
- **Typical drivers:** No CSPM/config monitoring; broad IAM roles; infrastructure changes outside IaC review; multi-account sprawl.
- **Impacts:** CONF, REG, REP.

## 11. Cloud tenant/account compromise
- **Event:** Attacker obtains cloud console or API credentials; escalates to full tenant control (resource destruction, cryptomining, data theft).
- **Typical drivers:** Long-lived access keys; no MFA on cloud accounts; leaked keys in repos; weak conditional access.
- **Impacts:** OPS, FIN (resource abuse + recovery), CONF.

## 12. DDoS against customer-facing services
- **Event:** Volumetric or application-layer denial of service takes revenue-generating services offline, possibly with extortion demand.
- **Typical drivers:** No DDoS mitigation service; single ingress point; public visibility as attractive target.
- **Impacts:** OPS, FIN (revenue), REP.

## 13. Undetected long-dwell intrusion (espionage/APT)
- **Event:** Intrusion persists for weeks–months; attacker harvests credentials, mail, and IP before detection.
- **Typical drivers:** Logging gaps on critical systems; no 24/7 monitoring; alert fatigue; limited east-west visibility.
- **Impacts:** CONF (primary), REG (breach scope inflation), REP, higher IR FIN.

## 14. Loss/theft of unencrypted endpoint or removable media
- **Event:** Laptop or drive containing sensitive data lost or stolen without encryption.
- **Typical drivers:** Incomplete disk-encryption enforcement; unmanaged BYOD; permissive USB policy.
- **Impacts:** CONF, REG (often a per-device notification analysis), REP.

## 15. Legacy / end-of-life system compromise
- **Event:** Unsupported OS or application exploited via a vulnerability that will never be patched.
- **Typical drivers:** EOL systems tied to critical processes; no compensating isolation; vendor lock preventing upgrade.
- **Impacts:** OPS, SAFE (OT/healthcare), CONF.

## 16. OT / ICS disruption
- **Event:** Attack or malware crosses from IT into operational technology; production or physical processes halt or behave unsafely.
- **Typical drivers:** Weak IT/OT segmentation; remote vendor access into OT; flat plant networks; unpatchable controllers.
- **Impacts:** SAFE, OPS, FIN, REG (sector regulators).

## 17. Source code / secrets leakage
- **Event:** Proprietary code or embedded credentials exposed via public repo, misconfigured artifact store, or developer error; secrets reused to breach production.
- **Typical drivers:** No secret scanning; personal-repo use for work; tokens with broad scope and no rotation.
- **Impacts:** CONF, downstream compromise (feeds scenarios 3/11), competitive FIN.

## 18. Generative-AI data leakage and misuse
- **Event:** Employees paste confidential or personal data into public AI tools, or an internal AI feature exposes training/context data to the wrong users; alternatively, staff act on hallucinated output in a regulated process.
- **Typical drivers:** No AI acceptable-use policy; no enterprise-sanctioned alternative; AI features shipped without access-control review; no output-verification step for high-stakes use.
- **Impacts:** CONF, REG (privacy, sector rules; see ../../../context/regulations/eu-ai-act.md for AI-specific obligations), REP. (Systemic AI oversight belongs to the ai-governance skill.)

## 19. Deepfake-enabled social engineering
- **Event:** Voice or video impersonation of an executive drives a fraudulent payment, credential disclosure, or market-sensitive misinformation.
- **Typical drivers:** Publicly available executive audio/video; verification procedures that trust voice/video identity; time-pressure payment culture.
- **Impacts:** FIN, REP, market/REG (for listed companies).

## 20. Failed or corrupted backup discovered during recovery
- **Event:** During an outage or ransomware event, backups prove incomplete, corrupted, or also encrypted; recovery time balloons.
- **Typical drivers:** Untested restores; backup credentials reachable from production domain; scope drift (new systems never enrolled).
- **Impacts:** OPS (multiplier on every availability scenario), FIN. Register separately or as an explicit key assumption under scenario 1.

---

## Using the library

1. **Filter:** discard scenarios with no plausible pathway in the assessed environment; record why (shows completeness to reviewers).
2. **Tailor:** replace generic drivers with observed conditions from gap assessments, audits, and incidents. A scenario with verified drivers scores higher likelihood than the same scenario with none.
3. **Combine:** several scenarios often share drivers (flat network, weak MFA, untested backups). Note shared drivers — treating one may reduce multiple risks, which strengthens the treatment business case.
4. **Extend:** sector-specific scenarios (payment-card skimming, medical-device compromise, trading-system manipulation) belong in your own extension of this library, not forced into these 20.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
