# Truthfulness Rules for Questionnaire Answers

A questionnaire answer is a written representation to a counterparty in a commercial relationship. It will be read by an assessor trained to detect evasion, filed by the customer, and compared — against your SOC 2 report, your trust page, your DPA, and the answers you gave the same customer last year. The rules below exist because the failure mode is never "we looked slightly less mature"; it is "the customer found a contradiction and now re-reads every answer as adversarial".

## The rules

1. **True today.** Answer the current, operating state. Roadmap items are stated as roadmap, dated, and marked non-contractual.
2. **Scoped precisely.** Say what the answer covers: which product, which environment, which population. "Yes" with an unstated scope is how true statements become false ones.
3. **Corporate vs. product scope.** Decide, per question, whether it asks about the company's internal controls or the product the customer buys — and answer the one asked, labeling the scope. Assessors treat conflation as either confusion or evasion.
4. **Consistent with the record.** Never claim more than the SOC 2 report, cert scope, DPA, or public docs support. If the SOC 2 report carries an exception on the control, the answer acknowledges the control accurately — the customer has the report.
5. **Evidence over reassurance.** Prefer a checkable fact (report, cert, metric, named mechanism) to an adjective. "Military-grade" and "industry-best-practice" are assessor bingo squares.
6. **No is an acceptable answer.** Delivered with compensating controls, a no costs a finding at worst. A discovered false yes costs the relationship.

## The "aspirational yes" antipattern

The most common dangerous answer: "yes" because the capability is planned, partially deployed, supported-but-not-enforced, or true of one environment. Each of these is a *different true answer* that got rounded up.

Rounding up feels safe because any single answer rarely gets verified. But answers are verified in aggregate — by the SOC 2 cross-check, by the follow-up call, by the incident that triggers an audit-rights clause. And a yes given this year silently commits next year's response, because the renewal diff surfaces "you told us yes in 2026".

Test for it: could you demonstrate the "yes" live, today, to this customer's auditor? If not, write the version you could demonstrate.

## Before/after rewrites

**Enforcement rounded up.**
- *Dangerous:* "Yes, MFA is enforced for all users."
- *Honest:* "MFA is enforced at the IdP for all workforce SSO access. Two legacy internal applications are not yet SSO-federated; both are scheduled for migration by Q4 2026 and are restricted to the corporate network in the interim."

**Capability presented as practice.**
- *Dangerous:* "Yes, we support SIEM integration and log monitoring."
- *Honest:* "Production and security logs are centralized and monitored with alerting; alerts route to the on-call security rotation. (If the question asks whether *customers* can export logs: audit-log export is available on the Enterprise tier via API.)" — "supports" answered a product-feature question that wasn't asked, and dodged the operational one that was.

**Roadmap rounded up.**
- *Dangerous:* "Yes, we are SOC 2 compliant." (when the Type II period ends next month)
- *Honest:* "We hold a SOC 2 Type I (issued <date>); our first Type II observation period ends <date> and the report is expected <date>. The Type I report is available under NDA."

**Scope silently shrunk.**
- *Dangerous:* "All data is encrypted at rest."
- *Honest:* "Customer data in the production platform is encrypted at rest (AES-256). Corporate laptops are full-disk encrypted. Data in the analytics warehouse is encrypted at rest; field-level encryption is not applied." Unprompted qualifiers you write ("critical systems", "where applicable") read exactly as evasively as when a vendor writes them to you.

**SLA volunteered.**
- *Dangerous:* "Yes, we notify customers of breaches within 24 hours."
- *Honest:* "We notify affected customers of confirmed incidents involving their data without undue delay, in accordance with our DPA and the agreement between the parties." A number in a questionnaire is a number the customer's lawyers will incorporate. If the customer needs a specific SLA, that is a contract negotiation — route it there.

**The heroic certification claim.**
- *Dangerous:* "We are ISO 27001, SOC 2, GDPR, HIPAA, and PCI compliant."
- *Honest:* Name only certifications you hold, with scope: "ISO/IEC 27001:2022 certified (certificate <n>, scope: <scope statement>); SOC 2 Type II (Security, Availability). We support customers' GDPR obligations as a processor under our DPA; we do not process cardholder data." "GDPR-compliant" is not a certification, and claiming HIPAA without a BAA program is discoverable in one follow-up.

## N/A vs. No

They answer different questions and are scored differently:

- **No** = the question applies and the control is absent. Pair with compensating controls and (if real) dated roadmap.
- **N/A** = the question does not apply, *for a stated reason*: "N/A — we do not process cardholder data; payments are fully outsourced to <processor>." Bare N/A on an applicable question is scored as a non-answer, and wrongly claiming N/A ("N/A — cloud provider handles this" on an appsec question) is scored as shared-responsibility confusion — a maturity flag.
- When unsure whether it applies, answer the applicable interpretation and state the assumption: "Assuming this refers to <X>: ..."

## Consistency traps

Contradictions get discovered. Check each before every submission:

1. **Questionnaire vs. SOC 2 report.** The report's system description, tested controls, and exceptions are in the customer's hands. Claiming a control the report scoped out, or describing as flawless a control the report excepted, is the single most common discovered contradiction.
2. **Questionnaire vs. public trust page.** Trust pages age. If the page says "SOC 2 Type I" and you answer "Type II", one of them is wrong in public. Fix the page or the answer — same-day.
3. **Questionnaire vs. subprocessor list.** The list in your answer, the public page, and the DPA annex must match. Assessors diff these routinely because mismatches are so common.
4. **Questionnaire vs. DPA.** Retention, deletion timelines, notification language, transfer mechanisms — the DPA is contractual; the questionnaire must not promise beyond it.
5. **This questionnaire vs. your last one to the same customer.** Renewals get diffed. Any answer that moved from yes to no (scope corrected, control retired) needs a proactive explanation, not silence.
6. **This customer vs. other customers.** One canonical library prevents the worst version: two customers comparing notes at a conference, holding different answers to the same question.
7. **Sales deck vs. security answers.** If marketing claims "zero-knowledge encryption" and your questionnaire answer describes provider-managed keys, the questionnaire is right and the deck needs fixing — flag it up rather than harmonizing downward.

## Review discipline

- Every answer that states a number (SLA, retention, RTO/RPO, insurance), grants a right (audit, pen test), or uses "certify/warrant/commit" gets legal review — no exceptions for deadline pressure.
- The security reviewer reads for rule 4 (consistency with the record); they should have the current SOC 2 report open while reviewing.
- Record what was flagged and how it was resolved. When the same flag recurs three times, the resolution belongs in the answer library so it stops recurring.
