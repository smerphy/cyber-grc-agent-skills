# Workflow: Customer Security Assurance Response

```yaml
name: customer-assurance-response
description: >-
  End-to-end handling of inbound customer and prospect security diligence:
  triage by request type and deal proportionality, truthful questionnaire
  responses from the answer library, controlled evidence sharing under NDA,
  customer audit management, contract security schedule review with formal
  risk decisions on commitments beyond current practice, and library
  maintenance so the next request costs less.
skills_used:
  - security-questionnaire-response
  - soc2-readiness
  - risk-assessment
  - exception-management
typical_duration: 2-10 business days per request; contract schedule reviews track the deal timeline
roles:
  - grc-analyst
  - compliance-officer
  - risk-manager
```

## Trigger

- A prospect or customer (or their TPRM platform) sends a security questionnaire, evidence request, or audit notice — at any deal stage, including renewal reassessments.
- Sales forwards "a few security questions from the customer" — which is this workflow whether or not anyone calls it that.
- A contract redline arrives containing a security schedule, DPA security annex, or audit-rights clause.

## Prerequisites

- A canonical answer library with owners and review dates — or the commitment to seed one during the first pass (see [security-questionnaire-response](../skills/security-questionnaire-response/SKILL.md)); without it every questionnaire is answered from scratch and answers drift.
- The current evidence set inventoried: latest SOC 2 report (type, period, TSC scope), ISO 27001 certificate and scope, pen test attestation, trust page, subprocessor list — and honesty about their expiry dates.
- A standard NDA path with a known turnaround, and a named deal owner for every request.
- An agreed internal position on what is never shared (raw pen test reports, network diagrams, unredacted policies) versus shared under NDA versus public.

## Steps

### 1. Request triage — grc-analyst with the deal owner

- **Skill:** [security-questionnaire-response](../skills/security-questionnaire-response/SKILL.md) (triage step)
- **Inputs:** the request; deal context (stage, size, strategic weight); deadline; NDA status.
- **Actions:** classify the request: standard questionnaire (SIG, CAIQ, custom), evidence-package request, audit/assessment right being exercised, onsite/meeting request, or contract security schedule — each takes a different path below. Apply proportionality: offer the standard package (trust page, whitepaper, SOC 2 under NDA) first; many customers accept it in lieu of a 300-question spreadsheet. For small deals with outsized asks, escalate effort-vs-value to the deal owner before committing. Set the internal deadline backed off from the customer's, and name the security and legal reviewers now.
- **Outputs:** triaged request with path, owner, and dates in the request log.
- **Decision gate:** no NDA and the request needs NDA-gated material — the NDA goes out first, and someone chases it; do not let the request idle in a deferral loop.

### 2. Questionnaire response — grc-analyst drafts; subject-matter owners confirm

- **Skill:** [security-questionnaire-response](../skills/security-questionnaire-response/SKILL.md)
- **Inputs:** questionnaire; answer library; current evidence set; product/scope boundaries; prior answers to this customer.
- **Actions:** map questions to library entries; draft unmatched ones with the responsible subject-matter owner. Enforce the truthfulness rules without exception: true today (not the roadmap), scoped precisely (which product, which environment — corporate vs. product scope), consistent with the record (the SOC 2 report, DPA, and trust page are cross-checked by good assessors), and evidence-anchored. Handle "no" answers honestly with compensating context; a discovered creative "yes" costs more than any gap. Flag every exposure answer — SLA commitments, audit rights, insurance, residency, anything asked to be certified — for the security and legal review named in step 1, because questionnaire answers get incorporated into contracts by reference.
- **Outputs:** reviewed, approved response; question-to-library mapping; list of gaps discovered while answering (routed to the risk register or [exception-management](../skills/exception-management/SKILL.md), never into an answer).

### 3. Evidence sharing under NDA — grc-analyst; compliance-officer owns the boundary

- **Skill:** [soc2-readiness](../skills/soc2-readiness/SKILL.md) (for knowing exactly what the report covers before handing it over)
- **Inputs:** executed NDA; evidence set; the never-share/NDA/public position from prerequisites.
- **Actions:** share deliberately, not reflexively. Know your own SOC 2 before the customer reads it: TSC categories in scope, system boundary, period, exceptions and management responses, and the CUECs the customer must operate — be ready to speak to each exception rather than be ambushed by it (see [SOC 2 TSC](../context/frameworks/soc2-tsc.md)). Send pen test *summaries or attestations*, not raw reports full of reproduction steps. Watermark where feasible, use expiring links or the trust portal, and log what was shared with whom and when — that log is your answer when a shared document surfaces somewhere it should not.
- **Outputs:** evidence package delivered; sharing log entry.
- **Decision gate:** requests for material on the never-share list get the standing alternative (summary, attestation, live walkthrough under NDA) — deviations require the compliance-officer, not an accommodating account executive.

### 4. Customer audit or assessment meeting — compliance-officer leads; grc-analyst prepares

- **Skill:** [security-questionnaire-response](../skills/security-questionnaire-response/SKILL.md) (consistency discipline applies verbatim); [soc2-readiness](../skills/soc2-readiness/SKILL.md) for scope questions
- **Inputs:** the customer's audit scope or agenda; contractual audit clause defining what they are entitled to; prior answers given to this customer.
- **Actions:** confirm the audit stays within the contractual clause — scope, frequency, notice, and cost allocation; a contractual "audit right" is rarely a right to roam. Pre-brief participants: answer what is asked, consistently with the written record, and take questions away rather than improvising. Offer the SOC 2 report as the substitute for control-by-control re-testing where the clause allows. Track every commitment made in the meeting — verbal commitments become expectations, and expectations become escalations.
- **Outputs:** audit/meeting record; follow-up commitments logged with owners and dates.

### 5. Contract security schedule review — grc-analyst screens; risk-manager decides; legal drafts

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) for commitments beyond current practice; [exception-management](../skills/exception-management/SKILL.md) where the gap is accepted
- **Inputs:** proposed security schedule or redlines; current control reality (not the policy aspiration); existing customer-commitment inventory.
- **Actions:** compare every proposed clause against what is actually operated. Three buckets: (a) already true — accept; (b) not true and should not be promised — redline to what is true, with the standard alternative clause; (c) not true but the business wants the deal — this is a risk decision, not a drafting problem. For bucket (c), score the commitment gap (likelihood of being caught out × contractual and regulatory consequence) so the risk-manager decides on stated risk; if accepted, record a time-bound exception with a remediation plan that makes the clause true before it is tested. **Never sign up to controls you do not run** on the theory that nobody checks — breach litigation and post-incident audits check.
- **Outputs:** redline rationale to legal; risk-scored gap list; time-bound exceptions with remediation plans for accepted commitments; new commitments added to the commitment inventory.
- **Decision gate:** a commitment gap the risk-manager declines to accept blocks that clause — the deal team renegotiates or the deal proceeds without it. Declining is a recorded, legitimate outcome.

### 6. Answer library and commitment maintenance — grc-analyst

- **Skill:** [security-questionnaire-response](../skills/security-questionnaire-response/SKILL.md) (library maintenance step)
- **Inputs:** this request's mappings, new answers, exposure flags, and contract commitments.
- **Actions:** fold new and improved answers into the library with owner and review date; retire answers invalidated by environment changes. Record what this customer was told and promised — the next renewal questionnaire will be checked against it. Feed systemic signals back: questions repeatedly answered "no" are a control-roadmap input; commitments repeatedly requested (breach SLAs, residency options) are product/legal standardization candidates. Diary evidence expiries (SOC 2 period end, certificate renewals) so step 3 never ships stale artifacts.
- **Outputs:** updated answer library; updated commitment inventory; expiry diary entries.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Triaged request + reviewers | 1 | Request log |
| Approved questionnaire response | 2 | Request log; customer file |
| Evidence package + sharing log | 3 | Sharing log / trust portal |
| Audit record + commitments | 4 | Customer file; commitment inventory |
| Redlines, risk decisions, exceptions | 5 | Contract file; risk + exception registers |
| Updated answer library | 6 | Answer library |

## Failure modes

- **Sales answers the questionnaire.** Optimistic answers written outside this workflow, discovered at renewal or post-incident. Route all requests through the request log; make the answer library easier to use than improvising.
- **The creative yes.** "Yes" because the roadmap says next quarter, or because a narrow reading permits it. Assessors cross-check against your SOC 2 and trust page; one discovered contradiction taints every other answer.
- **Evidence spray.** Raw pen test reports and architecture diagrams emailed to any prospect who asks. Step 3's boundary exists because shared documents outlive deals and NDAs are remedies, not walls.
- **Contract commitments nobody operates.** Security schedules signed unread, then surfacing in breach litigation as a list of promises not kept. Step 5 is the only step here that can create multi-year liability in an afternoon.
- **Commitment amnesia.** No inventory of what each customer was promised, so obligations are discovered by being breached. The commitment inventory in steps 5-6 is as important as the answer library.
- **Library rot.** An answer library nobody maintains drifts from reality until it is a liability engine. Owners and review dates per entry, refreshed by every request that touches them.
- **Audit scope surrender.** Letting a customer audit expand past its contractual clause because saying no feels commercially awkward. The clause was negotiated for a reason; the compliance-officer holds the line, not the account team.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
