# [Policy Name] Policy

**How to use:** Replace bracketed placeholders, delete guidance in *italics*, and delete this paragraph. Keep policy statements numbered, testable, and mapped to controls — the worked examples in Section 4 show the quality bar. For the authoring method (audience, tone, policy vs. standard vs. procedure layering), use [../skills/policy-authoring/SKILL.md](../skills/policy-authoring/SKILL.md); for reviewing an existing policy, [../skills/policy-review/SKILL.md](../skills/policy-review/SKILL.md).

## Document control

| Attribute | Value |
|---|---|
| Document ID | [POL-XXX] |
| Owner | [Role, not name — e.g., CISO] |
| Version | [e.g., 2.1] |
| Status | [Draft / In review / Approved / Retired] |
| Approved by | [Approving body/role — e.g., Information Security Steering Committee] |
| Approval date | [YYYY-MM-DD] |
| Effective date | [YYYY-MM-DD] |
| Next review date | [YYYY-MM-DD — at most 12 months out, or on material change] |
| Classification | [e.g., Internal] |
| Supersedes | [Prior version or "None"] |

## 1. Purpose

*One short paragraph: why this policy exists, tied to a business or compliance driver (risk addressed; framework, regulatory, or contractual obligations satisfied). No boilerplate about "the importance of security".*

## 2. Scope

*Who and what this policy binds. Name populations (employees, contractors, third parties with system access), systems/data (all information systems? production only? a defined environment?), and geographies. State exclusions explicitly with rationale — an unstated exclusion is a future audit finding.*

## 3. Definitions

*Define only terms used in this policy with a specific meaning. Link the rest to your organizational glossary (see [../context/glossary.md](../context/glossary.md) for a starting vocabulary).*

| Term | Definition |
|---|---|
| [Term] | [Definition] |

## 4. Policy statements

*The rules. Each statement must be: numbered with a stable ID (do not renumber on revision), testable (an auditor can determine pass/fail), and assigned (clear who must comply). Use **must** / **must not** for mandatory requirements, **should** / **should not** for expected practice overridable with documented justification, **may** for discretion. Avoid "will", "strives to", "as appropriate". One requirement per statement; put tunable parameters (key lengths, review frequencies per tier) in a subordinate standard. Map each statement to the framework(s) you assert compliance against — see [../context/crosswalks/framework-crosswalk.md](../context/crosswalks/framework-crosswalk.md).*

**Worked example (from an access control policy):**

| # | Statement | Control mapping |
|---|---|---|
| AC-01 | Access to information systems **must** be granted on the basis of least privilege and documented business need, via the access request workflow. Standing access **must not** be granted by verbal or chat approval. | ISO 27001 A.5.15; CIS v8 Control 6; NIST CSF 2.0 PR.AA; SOC 2 CC6.1 |
| AC-02 | User access to in-scope systems **must** be reviewed by the system owner at least quarterly; access not reaffirmed within 14 days of review issuance **must** be revoked. | ISO 27001 A.5.18; CIS v8 6.8; SOC 2 CC6.2-CC6.3 |
| AC-03 | Multi-factor authentication **must** be enforced for all remote access and all administrative access. Phishing-resistant factors **should** be used for administrative access. | ISO 27001 A.8.5; CIS v8 6.3-6.5; NIST SP 800-53 IA-2 |
| AC-04 | Accounts of leavers **must** be disabled within 24 hours of employment end; contractor accounts **must** carry an expiry date at creation. | ISO 27001 A.5.16; SOC 2 CC6.2 |

*What makes these testable: each has a population (all remote access; leavers), a measurable condition (quarterly; 14 days; 24 hours), and a binary outcome. "Access should be reviewed regularly" fails all three.*

## 5. Roles and responsibilities

| Role | Responsibility |
|---|---|
| [Policy owner] | Maintains the policy, triggers reviews, tracks exceptions |
| [Approving body] | Approves the policy and material changes |
| [System owners] | Implement statements applicable to their systems; execute reviews |
| [All personnel in scope] | Comply; report suspected violations |
| [Internal audit / control testing] | Independently tests compliance — see [../skills/control-testing/SKILL.md](../skills/control-testing/SKILL.md) |

## 6. Compliance and enforcement

*How compliance is measured (control testing, metrics, audits) and consequences of violation — up to and including termination of employment or contract, per HR and contractual processes. Name the escalation path for identified violations.*

## 7. Exceptions

Deviations from this policy require an approved, time-bound exception via the exception management process — see [exception-request.md](exception-request.md) and [../skills/exception-management/SKILL.md](../skills/exception-management/SKILL.md). Exceptions **must not** exceed [12] months without re-approval. No retroactive exceptions: non-compliance without an approved exception is a policy violation.

## 8. Related documents

*Parent documents (e.g., overall information security policy), subordinate standards and procedures that implement this policy, sibling policies referenced, and applicable regulatory obligations. Keep policy (what/why) separate from standard (specific parameters) and procedure (how).*

## 9. Revision history

| Version | Date | Author | Approver | Summary of change |
|---|---|---|---|---|
| [2.1] | [YYYY-MM-DD] | [Role] | [Role/body] | [e.g., Added AC-04 leaver deadline; annual review] |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
