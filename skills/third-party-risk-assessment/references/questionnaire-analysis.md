# Evaluating Vendor Questionnaire Responses

A completed questionnaire is a set of claims, mostly written by a sales engineer or a GRC analyst optimizing for deal velocity. Your job is to separate operational fact from aspiration and marketing. Score every answer; never average a questionnaire into a single "vendor score" that hides a critical inadequate answer under thirty adequate ones.

## Scoring scale

| Score | Meaning | Example (Q: "Describe your access-revocation process for terminated employees") |
|-------|---------|--------------------------------------------------------------------------------|
| Adequate | Specific, operational, verifiable; names mechanisms, owners, timeframes | "HR termination in Workday triggers automated deprovisioning via SCIM within 1 hour for SSO-federated apps; non-federated apps are revoked by IT within 24h from a system-generated ticket; quarterly access recertification catches residuals. Last SOC 2 tested this control (1 exception, remediated)." |
| Partial | Real answer but missing a dimension (timeframe, coverage, evidence) | "Access is removed by IT when HR notifies them of a termination." (How fast? All systems? What ensures HR notifies?) |
| Inadequate | Reveals a gap or an immature control | "Managers are responsible for requesting access removal for their reports." |
| Non-answer | Does not answer the question asked | See patterns below |

## Non-answer patterns

1. **Policy-quoting.** "Per our Access Control Policy, access is granted on least privilege and revoked timely." A policy excerpt answers "do you have a policy", not "what happens operationally". Follow-up: "Describe the mechanism and measured timeframe, and how you verify it."
2. **Answering an adjacent question.** Q: "Is customer data encrypted at rest?" A: "All data is encrypted in transit using TLS 1.2+." The at-rest question was dodged — often deliberately. Re-ask the exact question and flag the dodge.
3. **Capability vs. practice.** "Our platform supports SSO, MFA, and role-based access." Supports ≠ enforced, and this describes the *product's* features when you asked about the *vendor's own* internal controls. Distinguish "security of the product" questions from "security of the company" questions and make the vendor answer both.
4. **"N/A" without justification.** N/A is a claim requiring a reason ("N/A — we do not process cardholder data; payments are fully outsourced to <processor>, we hold tokens only" is fine). Bare N/A on a plainly applicable question = non-answer.
5. **Deferral loops.** "Available upon request under NDA" — when an NDA is already in place, or when the item is the questionnaire answer itself. Call the loop out and set a deadline.
6. **Future tense.** "We are implementing / plan to / are in the process of achieving ISO 27001." Score on today's state; capture the roadmap item as a contractual milestone if it matters.
7. **Confidence without object.** "We take security extremely seriously and employ industry-best-practice, military-grade security." Content-free. One instance is noise; a questionnaire full of it is a maturity signal in itself.
8. **Scope-shrinking.** Answers silently qualified to one environment: "Production systems are patched within 14 days" (and staging, and the corporate laptops with your data synced?). Watch for unprompted qualifiers: "critical systems", "where applicable", "generally".
9. **Third-party hand-waving.** "Our cloud provider is ISO 27001 certified and handles security." Inherited infrastructure controls do not answer questions about the vendor's own application security, access management, or personnel controls. Shared-responsibility confusion here is a genuine maturity flag.
10. **Copy-paste drift.** Answers referencing another customer's name, the wrong product, or questions from a different questionnaire. Signals nobody with actual knowledge reviewed the responses.

## Boilerplate detection heuristics

- **Specificity test**: does the answer contain at least one of — a number (SLA hours, retention days, test frequency), a named mechanism (tool category, protocol, standard), or a named accountable role? Zero of three across a paragraph → boilerplate.
- **Swap test**: could this exact paragraph be pasted into any other vendor's questionnaire unchanged? If yes, it carries no information about *this* vendor.
- **Verification hook test**: does the answer offer anything checkable (report, cert, metric, contractual commitment)? Strong answers volunteer evidence.

## Internal-consistency checks

Cross-check within the questionnaire and against other evidence:

- Encryption claims vs. the SOC 2 system description and the DPA's technical measures annex.
- "24/7 security operations" vs. stated security team headcount of 2.
- "Annual third-party penetration test" vs. inability to produce an attestation letter.
- Subprocessor list in the questionnaire vs. the public subprocessor page vs. the DPA annex — mismatches are common and material.
- Claimed certifications vs. the certificate registry of the issuing body (ISO certs are verifiable with the certification body; ask for certificate number and scope statement).

## Follow-up technique

- Batch follow-ups into **one** round; vendors reasonably resent drip-feed interrogation. Prioritize: only chase Partial/Non-answer scores on questions that matter for the tier.
- Ask for *mechanism and evidence*, not reassurance: "What is the measured p95 time from termination to full revocation over the last quarter, and how is it measured?" beats "Please confirm access is revoked promptly."
- For Tier 1 vendors, prefer a 60-minute call with the vendor's security team over a third written round — evasion is much harder live, and you learn more from who shows up (security engineer vs. sales) than from the answers.
- Record refusals verbatim. "Vendor declined to answer Q14 and Q22" is itself assessment evidence and belongs in the findings.

## Turning scores into findings

- Every **Inadequate** on a tier-relevant question → a finding with severity rated in engagement context (see `../../../context/risk-scoring.md`).
- Clusters of **Partial/Non-answer** in one domain (e.g., all vulnerability-management questions dodged) → a domain-level finding: "Vendor could not evidence a functioning vulnerability management process."
- Pervasive boilerplate with no evidence hooks → a program-maturity finding, and grounds to require independent attestation (SOC 2 / pen test) as a contract condition rather than accepting self-attestation.
- Refusal to complete a tier-appropriate questionnaire at all → escalate; for Tier 1-2 this alone can justify "approve with conditions" (attestation required by a dated milestone) or rejection.

## Anti-patterns on your side

- **Sending 300 questions to everyone.** Trim to tier; extract answers from the SOC 2 first and ask only the residual (see the questionnaire template: `../../../templates/vendor-security-questionnaire.md`).
- **Yes/no-only formats.** They invite "yes" and produce zero evidence. Every important question should ask "describe how" or "provide evidence".
- **Accepting a standardized-questionnaire PDF answered for someone else** (e.g., a generic shared-assessment document) without mapping it to your questions. Usable as input, but map coverage explicitly and chase your unanswered items.
- **Scoring completion instead of content.** "Vendor returned the questionnaire" is not an assessment result.
