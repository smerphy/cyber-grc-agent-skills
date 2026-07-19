# Recommended Policy Catalog for a Security Program

A pragmatic policy set for a mid-size organization. Small organizations can merge several of these into fewer documents (a common consolidation pattern is noted at the end); large or heavily regulated organizations will split further. Each entry lists the document's scope, the standards/procedures that typically hang beneath it, and the primary framework domains it serves.

Numbering below is illustrative — adopt the organization's own scheme.

## Tier 0 — Charter

### 1. Information Security Policy (top-level / ISMS policy)
- **Scope:** Management intent and commitment; objectives of the security program; assignment of top-level accountability; authority of the security function; requirement that all workforce members comply with subordinate policies.
- **Children:** Everything below. This is the parent of the whole set.
- **Serves:** ISO 27001 clause 5.2 (policy) and leadership requirements; NIST CSF 2.0 Govern function; SOC 2 CC1 (control environment).
- **Note:** Keep to 2–3 pages. It is the document the board approves; volatile content does not belong here.

## Tier 1 — Core policies

### 2. Acceptable Use Policy (AUP)
- **Scope:** Rules for workforce use of organizational systems, data, and networks: personal use limits, prohibited activities, monitoring notice, email/messaging conduct, social media, personal devices touching corporate data (or pointer to BYOD standard), consequences.
- **Children:** BYOD standard; monitoring/logging notice (jurisdiction-dependent).
- **Serves:** ISO 27001 A.5.10 (acceptable use); CIS v8 relies on it for user-facing controls; HR enforcement anchor for most other policies.
- **Note:** The one policy every employee must read and attest to. Write it at a general-audience reading level.

### 3. Access Control Policy
- **Scope:** Identity lifecycle (joiner/mover/leaver), least privilege, role-based access, authentication requirements (pointer to authentication standard), privileged access, remote access, access reviews/certification, segregation of duties.
- **Children:** Authentication standard (password/MFA parameters); privileged access management standard; access review procedure; JML procedure.
- **Serves:** ISO 27001 A.5.15–A.5.18, A.8.2–A.8.5; CIS v8 controls 5 and 6; SOC 2 CC6; PCI DSS requirements 7 and 8.

### 4. Data Classification and Handling Policy
- **Scope:** Classification scheme (typically 3–4 levels), classification responsibility (data owners), labeling, handling rules per level (storage, transmission, sharing, printing, disposal), retention pointer.
- **Children:** Handling matrix standard (level x action grid); data retention schedule.
- **Serves:** ISO 27001 A.5.12–A.5.14; SOC 2 confidentiality criteria; prerequisite for DLP tooling and for privacy compliance.
- **Note:** Every other policy references these levels. Author this early; never let siblings redefine the levels.

### 5. Cryptography Policy
- **Scope:** When encryption is required (at rest, in transit, by classification level), key management responsibilities, prohibition of home-grown crypto, certificate management ownership.
- **Children:** Cryptographic standard (approved algorithms, minimum key lengths, TLS versions, key rotation intervals) — parameters live here, not in the policy.
- **Serves:** ISO 27001 A.8.24; PCI DSS requirements 3 and 4; GDPR Art. 32 security-of-processing expectations.

### 6. Incident Response Policy
- **Scope:** Definition of a security incident vs. event, obligation to report, IR team authority (including power to disconnect systems), severity classification, regulatory notification responsibility, post-incident review requirement.
- **Children:** IR plan (procedure); playbooks per scenario; regulatory notification procedure (see the incident-regulatory-reporting skill and ../../../context/crosswalks/breach-notification-timelines.md for deadline obligations across regimes).
- **Serves:** ISO 27001 A.5.24–A.5.28; CIS v8 control 17; SOC 2 CC7; breach-notification duties under GDPR Art. 33/34, HIPAA, NIS2, and state breach laws.

### 7. Business Continuity and Disaster Recovery Policy
- **Scope:** Requirement to identify critical processes (BIA), set RTO/RPO by criticality tier, maintain and test continuity/recovery plans, backup requirements (pointer to backup standard), test frequency.
- **Children:** BIA methodology; DR plans per system; backup standard; test schedule and exercise procedure.
- **Serves:** ISO 27001 A.5.29–A.5.30, A.8.13–A.8.14; SOC 2 availability criteria; operational resilience expectations under DORA for financial entities.

### 8. Third-Party / Vendor Security Policy
- **Scope:** Security requirements before engaging a vendor, risk tiering of vendors, contractual security clauses, right to audit, ongoing monitoring, offboarding/data return, subcontractor flow-down.
- **Children:** Vendor assessment procedure (see the third-party-risk-assessment skill); contract clause library; vendor tiering standard.
- **Serves:** ISO 27001 A.5.19–A.5.23; SOC 2 CC9; DORA ICT third-party provisions; GLBA/FTC Safeguards service-provider oversight.

### 9. Secure Development Policy
- **Scope:** Security requirements in the SDLC: threat modeling triggers, secure coding requirement, code review, dependency and secret management, security testing gates, separation of environments, production data in non-production.
- **Children:** Secure coding standard (language-specific); CI/CD security standard; open-source usage standard.
- **Serves:** ISO 27001 A.8.25–A.8.31; CIS v8 control 16; PCI DSS requirement 6.

### 10. Vulnerability and Patch Management Policy
- **Scope:** Obligation to scan (frequency by asset class), remediation SLAs by severity, patching responsibility, exception path for unpatchable systems, penetration testing requirement.
- **Children:** Remediation SLA standard (severity x asset criticality grid); scanning procedure; pen test scoping standard.
- **Serves:** ISO 27001 A.8.8; CIS v8 control 7; PCI DSS requirements 6 and 11.

### 11. Logging and Monitoring Policy
- **Scope:** What must be logged (authentication, privileged actions, security events), retention periods, clock synchronization, log protection, monitoring/alerting responsibility, workforce privacy boundaries on monitoring.
- **Children:** Logging standard (event types, retention by log class); alert triage procedure.
- **Serves:** ISO 27001 A.8.15–A.8.17; CIS v8 control 8; SOC 2 CC7.2; PCI DSS requirement 10.

### 12. Asset Management Policy
- **Scope:** Inventory requirement (hardware, software, data, cloud), asset ownership assignment, secure configuration requirement (pointer to hardening standards), media handling and disposal.
- **Children:** Hardening baselines per platform; disposal/sanitization standard; software allowlist standard.
- **Serves:** ISO 27001 A.5.9, A.8.1; CIS v8 controls 1, 2, 4; NIST CSF 2.0 Identify function.

### 13. Human Resources Security Policy
- **Scope:** Screening/background checks (jurisdiction-permitting), security terms in employment contracts, security awareness training requirement and frequency, disciplinary linkage, termination duties (return of assets, access revocation).
- **Children:** Awareness training standard (audience x frequency x content); screening standard.
- **Serves:** ISO 27001 A.6.1–A.6.8; CIS v8 control 14; SOC 2 CC1.
- **Note:** Co-own with HR. Security drafts the requirements; HR owns the employment-law mechanics.

### 14. Physical and Environmental Security Policy
- **Scope:** Facility access control, visitor management, secure areas, clear desk/clear screen, equipment siting and protection, environmental controls for processing facilities.
- **Children:** Badge/visitor procedure; data center access standard.
- **Serves:** ISO 27001 A.7.1–A.7.14 (physical controls theme); often partially outsourced to facilities or the colo/cloud provider — scope carefully around what the organization actually controls.

### 15. Risk Management Policy
- **Scope:** Requirement to perform risk assessments (methodology pointer), risk acceptance authority by level, risk register maintenance, treatment plan follow-up, reporting to governance bodies.
- **Children:** Risk assessment methodology (see the risk-assessment skill and ../../../context/risk-scoring.md); risk acceptance procedure.
- **Serves:** ISO 27001 clauses 6.1 and 8.2–8.3; NIST CSF 2.0 Govern/Identify; SOC 2 CC3.

### 16. Change Management Policy
- **Scope:** Definition of change classes (standard/normal/emergency), approval requirements per class, testing and rollback requirements, emergency change ratification, unauthorized-change handling.
- **Children:** CAB procedure; emergency change procedure.
- **Serves:** ISO 27001 A.8.32; SOC 2 CC8; SOX ITGC change-management expectations (see ../../../context/regulations/sox-itgc.md).

## Tier 1 — Conditional (adopt when the trigger applies)

### 17. Privacy / Data Protection Policy — *trigger: processing personal data (nearly universal)*
- **Scope:** Lawful processing commitments, data subject rights handling, DPIA triggers, records of processing, cross-border transfer rules, breach notification linkage.
- **Serves:** GDPR (see ../../../context/regulations/gdpr.md), US state privacy laws, HIPAA Privacy Rule for covered entities. Often owned by legal/privacy with security as contributor. Pair with the dpia-privacy-assessment skill.

### 18. Cloud Security Policy — *trigger: material cloud usage*
- **Scope:** Approved cloud service models, shared-responsibility assignment, cloud account provisioning governance, tenant baseline requirements, shadow-IT/SaaS intake.
- **Note:** Small organizations fold this into asset management + access control instead.

### 19. AI Acceptable Use / AI Governance Policy — *trigger: workforce use of AI tools or AI in products*
- **Scope:** Approved AI tools, data permitted in prompts by classification level, human-review requirements for AI output, AI system intake and risk assessment, transparency obligations.
- **Serves:** EU AI Act obligations where applicable (see ../../../context/regulations/eu-ai-act.md). Pair with the ai-governance skill.

### 20. Mobile Device / BYOD Policy — *trigger: personal devices accessing corporate data*
- **Scope:** Enrollment requirements, minimum device posture, containerization/wipe rights and their limits, lost-device reporting.
- **Note:** Frequently a standard beneath the AUP rather than a standalone policy.

## Consolidation pattern for small organizations (under ~100 staff)

Six documents can cover the set: (1) Information Security Policy incorporating risk management and HR security; (2) Acceptable Use incorporating BYOD and AI use; (3) Access Control incorporating cryptography-for-users; (4) Operations Security incorporating asset, vulnerability, logging, change, and cloud; (5) Incident Response and Continuity; (6) Third-Party and Data Protection. Keep the traceability table per statement regardless of packaging — auditors care about coverage, not document count.

## Coverage check

After selecting the set, verify the union of all policies covers every in-scope framework domain using ../../../context/crosswalks/framework-crosswalk.md. Common gaps in otherwise complete sets: threat intelligence (ISO 27001 A.5.7), security in project management (A.5.8), and configuration management as distinct from asset inventory (A.8.9, CIS v8 control 4).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
