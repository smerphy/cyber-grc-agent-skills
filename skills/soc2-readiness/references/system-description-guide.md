# SOC 2 System Description Guide

The system description is Section 3 of a SOC 2 report — management's own account of the system, asserted by management and attested by the auditor against the AICPA description criteria (DC section 200 for SOC 2). It is the most-read part of the report after the opinion, and the part management alone controls. A vague or overbroad description invites scope disputes with the auditor and skeptical questions from customer reviewers.

## What "the system" means

The system is the set of components that deliver the in-scope service and meet the service commitments — not the whole company. Everything in the description must trace to a service commitment (what the org promises customers: SLAs, security exhibits, DPA terms, published trust commitments) or a system requirement (what the system needs to meet those commitments: laws, regulations, framework obligations, internal standards).

Start by writing the commitments inventory. Every later scoping argument ("is the marketing website in scope?") resolves against it: if no commitment depends on a component, it can stay out; if one does, it cannot.

## The five system components

Define the boundary by enumerating each component. Gaps here become gaps in the control matrix.

### 1. Infrastructure

Physical and virtual resources: cloud accounts/subscriptions, VPCs/networks, compute, storage, databases, CDNs, corporate network segments that touch production, and any physical facilities in scope. For cloud-native orgs, name the provider(s), regions, and account structure. Include the endpoint fleet if endpoints can reach production or hold in-scope data (they almost always can — excluding laptops rarely survives scrutiny).

### 2. Software

Application software delivering the service, plus supporting software: operating systems, databases, container orchestration, CI/CD tooling, monitoring/logging stack, identity provider, security tooling (EDR, scanners). Rule of thumb: any software whose compromise or failure would break a service commitment is in scope. The CI/CD pipeline and IdP are in scope in virtually every modern SaaS description — they gate production changes and production access.

### 3. People

Roles (not names) involved in operating and securing the system: engineering, SRE/ops, security, IT, support with production or customer-data access, and management/oversight functions. Include contractors performing these roles. State which roles have privileged access. Roles with no path to the system or its data (e.g., sales with no admin CRM access to in-scope data) can be excluded — say so deliberately, not silently.

### 4. Procedures

The automated and manual procedures by which the system is operated: provisioning/deprovisioning, change management, incident response, backup and recovery, vulnerability management, monitoring, vendor management. The description summarizes these at process level; the control matrix carries the detail.

### 5. Data

Data types the system processes and their flow: customer data (define it — content vs metadata), authentication data, logs, backups. State classification, where each type resides, and how it moves across the boundary. A data-flow diagram is not mandated but resolves more auditor and customer questions than any other single artifact.

## Structure of the description

A well-formed description covers, in order:

1. **Company and services overview** — one or two paragraphs; what the service does for whom.
2. **Principal service commitments and system requirements** — the commitments inventory, summarized. This anchors the auditor's evaluation: the opinion is on whether controls provide reasonable assurance that commitments and requirements are met.
3. **System boundary and components** — the five components above. State explicitly what is excluded and why (other product lines, corporate systems with no path to in-scope data).
4. **Relevant aspects of the control environment, risk assessment, information and communication, and monitoring** — brief; mirrors CC1-CC4.
5. **Control activities** — process-level narrative of the control areas (access, change, operations, incident response). Do not enumerate every control; the auditor's Section 4 test matrix does that.
6. **Complementary user entity controls (CUECs)** — see below.
7. **Subservice organizations** — see below, including complementary subservice organization controls (CSOCs) under the carve-out method.
8. **Significant changes during the period** (Type II) — re-architectures, acquisitions, major tooling changes affecting the system during the window.
9. **Incidents** — the description criteria require disclosure of incidents during the period that were the result of controls failing to meet commitments/requirements, if significant. Decide disclosure with the auditor early, not during draft review.

## Writing rules

- Present tense, factual, verifiable. Every sentence is an assertion management signs and the auditor attests. Delete marketing language ("bank-grade security") — it creates attestation risk with no benefit.
- Describe what is done, not what policy says should be done. "Access is reviewed quarterly" must be true for the whole window in a Type II.
- Match granularity to stability: name product categories ("an EDR agent") rather than vendors where tooling churns, unless the vendor is itself a subservice org.
- Keep the description synchronized with the control matrix — auditors reconcile them, and mismatches generate exceptions or description modifications late in fieldwork.

## Complementary user entity controls (CUECs)

CUECs are controls the customer must operate for the service's control environment to be complete. If the org's controls assume the customer does something, write it as a CUEC — otherwise the auditor may treat the assumption as a control gap.

Typical CUECs for a B2B SaaS:

- Customer manages provisioning, deprovisioning, and periodic review of its own user accounts in the service.
- Customer configures available security features appropriate to its needs (SSO enforcement, MFA, role assignments, IP allowlists).
- Customer protects credentials and API keys issued to it.
- Customer ensures data it submits is authorized and lawfully collected.
- Customer notifies the service organization of suspected security incidents or unauthorized access.

Keep the list short and real. Every CUEC is homework for every customer's vendor-review team; padded CUEC lists cause questionnaire friction. Conversely, a missing CUEC ("customer manages its own users") can make the org's CC6.2/CC6.3 controls look incomplete.

## Subservice organizations: inclusive vs carve-out

A subservice organization is a vendor whose own controls are necessary, in combination with the org's, to meet the service commitments — not every vendor. A billing tool the service does not depend on for its commitments is a vendor (handled under CC9.2), not a subservice org.

**Carve-out method (the norm):** the description identifies the subservice org and the types of controls it is expected to perform (CSOCs — complementary subservice organization controls), but those controls are excluded from the description and the auditor's testing. The org must still monitor the subservice org — typically by reviewing its SOC 2 report annually, mapping its CUECs back to the org's own controls, and assessing complementary coverage. Cloud IaaS (AWS, Azure, GCP) is almost always carved out: their physical security, environmental protections, and hypervisor controls are CSOCs.

**Inclusive method (rare):** the subservice org's controls appear in the description and the auditor tests them, which requires the subservice org's cooperation, its management's assertion, and access for testing. Used mainly when the subservice org is an affiliate or has no report of its own and customers demand coverage.

Decision rule: carve out any subservice org that has its own SOC 2 report. Consider inclusive only when (a) the subservice org has no report, (b) its controls are material to commitments, and (c) it will contractually cooperate — all three are rarely true.

For each carved-out subservice org, the readiness work is:

1. Obtain its current SOC 2 report (Type II preferred); verify the report period reasonably covers or abuts the org's own window — note any gap and obtain a bridge letter if material.
2. Read the opinion and exceptions; assess impact of any qualification on the org's commitments.
3. Map its CUECs to the org's controls — the subservice org's CUECs are obligations on this org. Unmapped CUECs are genuine gaps.
4. Record the review as evidence for CC9.2 (vendor risk) — see [third-party-risk-assessment](../../third-party-risk-assessment/SKILL.md).

## Common description defects

| Defect | Consequence |
|---|---|
| Boundary excludes CI/CD or IdP | Auditor rejects boundary; late re-scoping and evidence scramble |
| Commitments section generic ("we take security seriously") | Auditor cannot anchor the opinion; rework |
| Description asserts controls the matrix does not contain (or vice versa) | Reconciliation findings during fieldwork |
| Subservice orgs listed but no CSOCs/monitoring described | Description criteria deficiency; CC9.2 exception risk |
| No CUECs, but controls assume customer-side actions | Perceived control gaps; customer reviewer questions |
| Aspirational tense ("will implement in Q3") | Cannot be attested; strike or implement before the window |
| Significant in-window changes omitted (Type II) | Description modification late in the audit; credibility damage |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
