# Workflow: Penetration Test Management

```yaml
name: penetration-test-management
description: >-
  Running a penetration test end to end: scoping and rules of engagement,
  qualification of the testing firm as a third party, written authorization and
  legal sign-off, execution oversight, findings triage into risk-rated register
  entries, remediation with owners and dates, formal risk acceptance for what
  will not be fixed, retest verification, and reporting into the metrics
  program.
skills_used:
  - third-party-risk-assessment
  - risk-assessment
  - exception-management
  - grc-metrics-reporting
typical_duration: 6-10 weeks from scoping to retest; remediation tail can run a quarter
roles:
  - grc-analyst
  - risk-manager
  - greybeard
```

## Trigger

- The annual or contractually required test cycle comes due (customer commitments, certification scopes, PCI DSS periodic testing requirements — see [PCI DSS](../context/frameworks/pci-dss-4.md); verify the current requirement text for cadence and scope specifics).
- A material change ships that invalidates prior results: new internet-facing system, re-architecture, major authentication change.
- Post-incident validation that an exploited path is actually closed.

## Prerequisites

- A defined test objective. "Get a pentest" is not one; "can an external attacker reach customer data from the internet" is. The objective drives scope, methodology, and what a pass means.
- Budget and a realistic window — testing squeezed into the last week of a compliance deadline buys a report, not a test.
- An asset inventory accurate enough to scope against, and named owners for the systems in scope.
- Incident response aware that a test window exists (without necessarily knowing dates, if detection is being evaluated).

## Steps

### 1. Scoping and rules of engagement — grc-analyst drafts; greybeard reviews

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (context: what are we worried about)
- **Inputs:** test objective; asset inventory; prior test reports.
- **Actions:** define scope from the threat model, not from convenience: in-scope systems and IP ranges, test type (external, internal, web app, cloud tenant, social engineering), black/grey/white-box, and explicit exclusions with rationale. The greybeard challenges sculpted scope — excluding the legacy system everyone fears is how organizations buy clean reports about their safest assets. Write rules of engagement: test window, allowed techniques, data-handling rules for anything exfiltrated as proof, halt conditions, and the emergency contact path both directions.
- **Outputs:** scope and rules-of-engagement document, signed by system owners.

### 2. Tester selection and qualification — grc-analyst

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md)
- **Inputs:** candidate firms; scope document.
- **Actions:** the testing firm will hold your vulnerabilities, credentials, and possibly your data — tier it accordingly (Tier 2 minimum) and assess it: tester qualifications and named-consultant CVs against the scope's technology, the firm's own security posture and report/data handling practices, insurance, and independence (a firm retesting its own remediation advice, or the MSP testing the environment it operates, is conflicted). Contract terms: confidentiality, data destruction after report acceptance, breach notification, and ownership of findings.
- **Outputs:** qualified firm under contract; vendor record opened per [vendor-onboarding](vendor-onboarding.md).

### 3. Authorization and legal sign-off — risk-manager, with counsel

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (contract step)
- **Inputs:** scope and RoE; contract.
- **Actions:** obtain written authorization signed by someone with actual authority over every in-scope system — unauthorized testing is a criminal-law problem in most jurisdictions, not a paperwork gap. Verify third-party dependencies: hosting and cloud providers' testing policies (most permit customer testing of customer workloads without prior approval, but policies differ by provider and service — verify the current policy), SaaS platforms generally require their own consent, and shared infrastructure needs the owner's sign-off. Confirm the authorization letter the testers carry matches the final scope.
- **Outputs:** signed authorization package; provider policy checks recorded.
- **Decision gate:** no signed authorization covering the full scope, no testing. Any in-scope system whose owner will not sign comes out of scope, visibly.

### 4. Execution oversight — grc-analyst

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (engagement monitoring)
- **Inputs:** test schedule; RoE.
- **Actions:** run a check-in cadence with the testers; track scope adherence; ensure critical findings are communicated **immediately, not in the report** — a remotely exploitable path to production data waits for no draft. If testers stumble on evidence of an actual prior compromise, the test pauses and incident response takes over — including the regulatory track ([incident-regulatory-response](incident-regulatory-response.md)) if thresholds could be engaged. Log any emergency scope changes with who approved them.
- **Outputs:** oversight log; any critical findings escalated in-flight.

### 5. Findings triage and risk rating — greybeard leads triage; grc-analyst records

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md)
- **Inputs:** draft report; environment context.
- **Actions:** challenge the report before accepting it — reproduce or evidence-check material findings, kill false positives with documented rationale, and re-rate everything in *your* context: a scanner-severity score is not a risk rating ([risk scoring](../context/risk-scoring.md) covers the CVSS caveats). Chain findings the way an attacker would — three mediums that compose into domain compromise are a critical. Look past instances to classes: five instances of the same missing-authorization bug is one engineering problem, not five tickets. Convert material findings into event-based risk statements for the register.
- **Outputs:** accepted final report; contextual ratings; register entries for material risks.

### 6. Remediation with owners and dates — grc-analyst tracks; system owners fix

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (treatment step)
- **Inputs:** rated findings.
- **Actions:** every finding gets a disposition: fix (named owner — a role, not "IT" — and a date scaled to severity), or risk-acceptance candidate for step 7. Track root-cause fixes separately from point fixes — patching the instance while the vulnerable pattern ships weekly is remediation theater. Report aging against dates weekly; overdue criticals escalate to the risk-manager, not into silence.
- **Outputs:** remediation tracker with owners, dates, and root-cause tags.

### 7. Risk acceptance for what will not be fixed — risk-manager approves; system owner sponsors

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** acceptance candidates with risk scores.
- **Actions:** formal, time-bound acceptance per the [exception request](../templates/exception-request.md): business justification, compensating controls with evidence, expiry with re-review — "won't fix" without an expiry is a permanent vulnerability with a signature on it. No self-approval by the owning team; authority follows the risk level. Findings against externally mandated requirements (e.g., in a certified or cardholder-data scope) get flagged to the relevant compliance owner — an internal acceptance does not satisfy an external assessor.
- **Outputs:** signed exceptions in the register, linked to the findings.
- **Decision gate:** declined acceptance returns the finding to step 6 with a funded date. Declining is a recorded, legitimate outcome.

### 8. Retest verification and metrics reporting — grc-analyst

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** remediation tracker; retest results.
- **Actions:** retest every fixed critical and high — by the original testers where practical — and verify the fix closes the finding, not just the proof-of-concept. Closure requires retest evidence, not a "done" ticket. Feed the metrics program: findings by severity, remediation SLA attainment, finding aging, repeat-finding rate across cycles (the honest indicator of whether root causes are being fixed), and accepted-risk count. Archive report, authorization package, and evidence for auditors and customer due diligence; confirm the testing firm's data destruction per contract.
- **Outputs:** retest evidence; closed findings; metrics into the reporting pack; archived engagement file.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Scope + rules of engagement | 1 | Engagement file |
| Qualified tester + contract | 2 | Vendor inventory |
| Authorization package | 3 | Engagement file (legal copy) |
| Oversight log | 4 | Engagement file |
| Final report + contextual ratings | 5 | Engagement file; risk register |
| Remediation tracker | 6 | Findings tracker |
| Signed exceptions | 7 | Exception register |
| Retest evidence + metrics | 8 | Engagement file; metrics pack |

## Failure modes

- **Sculpted scope.** The systems most likely to fail are excluded, and the clean report is waved at customers. The greybeard's step 1 challenge and documented exclusion rationale are the countermeasure.
- **Testing without authorization.** A missing signature, an unapproved SaaS target, or scope drift onto someone else's infrastructure turns a security exercise into a legal incident. Step 3's gate is absolute.
- **Report shelfware.** The PDF is filed, the deadline is met, nothing is fixed. If step 6 produces no tracker with owners and dates, the engagement bought paper.
- **CVSS worship.** Ratings imported unmodified from the report, so an unexploitable "critical" outranks the chained mediums that reach production data. Step 5 exists to re-rate in context.
- **Fix the instance, ship the class.** Point fixes without root-cause tags, and next year's report repeats this year's findings. Track the repeat-finding rate — it is the metric that embarrasses honestly.
- **Silent risk acceptance.** "We'll live with it" decided in a hallway, discovered in the next audit. Unfixed findings go through step 7 with a signature and an expiry, or back into remediation.
- **Retest skipped.** Fixes closed on the developer's word; the finding resurfaces next cycle as a repeat. Closure requires retest evidence — treat an unverified fix as an open finding.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
