# Example: Vendor SOC 2 Report Review

**Persona:** grc-analyst · **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) · **Reference used:** [soc2-report-review](../skills/third-party-risk-assessment/references/soc2-report-review.md)

All entities are fictional.

---

## User input

> Prospective vendor: Corvid Metrics (product analytics; will receive our end-user event data incl. pseudonymous IDs and IP addresses). They sent their SOC 2 report. Tier 2 per our tiering (significant data access, moderate operational dependency). Report facts:
> - SOC 2 **Type II**, Security + Availability, period **1 Feb 2025 – 31 Jul 2025**, unqualified opinion, issued by a mid-size CPA firm
> - Uses AWS as subservice organization, **carve-out** method
> - 4 exceptions noted; 9 CUECs listed
> - Today is 2026-07-20. They say a new report is "in progress."

## Agent output (deliverable)

### Verdict: CONDITIONAL PASS — three conditions before signature

Suitable for Tier 2 use *if* the coverage gap, one exception, and two CUECs are addressed as below.

### Report analysis

**1. Opinion and scope — acceptable.** Unqualified Type II over Security + Availability matches a Tier 2 analytics use case. Confidentiality category absent: acceptable given pseudonymized event data, but note it in the file — if the data shared ever includes direct identifiers, revisit.

**2. Coverage gap — the real issue.** The period ended **31 Jul 2025, nearly 12 months ago**. A report is not a subscription: there is currently **no third-party assurance covering Aug 2025 → today**. "In progress" is not evidence.
→ **Condition A:** obtain either the new Type II (expected period ~Aug 2025–2026) before go-live, or a signed **bridge letter** from Corvid management covering the gap, plus a contractual commitment to annual Type II delivery within 90 days of period end.

**3. Exceptions — one matters for this use case.**

| Exception (as reported) | Auditor note | Assessment for our use |
|---|---|---|
| 2 of 25 sampled terminations: access removed in 6–9 business days vs. 5-day policy | No compensating control cited | **Material to us** — orphaned vendor-side accounts with access to our event pipeline. → Condition B: ask for current-period termination metrics and whether the new report re-tests it clean |
| 1 of 8 sampled changes missing peer-review evidence | Change deployed via CI with tests | Accept — low relevance to data protection |
| Quarterly access review for one internal tool completed 18 days late | Review completed, no anomalies found | Accept with note |
| Backup restore test for one non-production system not performed in period | Production restore tested clean | Accept — availability impact only, non-production |

**4. Carve-out means AWS is our problem too.** The report gives no assurance over AWS controls. Standard resolution: AWS's own SOC 2 covers the carve-out; confirm Corvid's *use* of AWS matches the CUEC-style assumptions in AWS's report (region redundancy, KMS usage). No action beyond noting — this is the normal pattern.

**5. CUECs — two are live obligations on us.** Of 9 complementary user entity controls, 7 are generic (manage your own users, secure your credentials). Two require action:

| CUEC | Our owning control | Status |
|---|---|---|
| "Customer configures IP filtering / data-ingest restrictions appropriate to its data" | Data-eng ingest allowlist | **Not currently configured** → Condition C: configure before production data flows; add to control inventory with an owner |
| "Customer defines retention period for event data" | None — we'd inherit their 25-month default | Decision needed from privacy team (align with our retention schedule) |

CUECs are the most-skipped part of SOC 2 review; both entries go into our control register with owners, not into a note nobody reads.

### Contract asks (from [contract-clauses](../skills/third-party-risk-assessment/references/contract-clauses.md))

1. Annual SOC 2 Type II (Security + Availability) delivery ≤90 days after period end; bridge letter on request.
2. Security incident notice: 48 hours, security contact named.
3. Subprocessor change notification with objection right (AWS region changes included).
4. Data deletion within 30 days of termination, with written confirmation.

### Register entry

`VEN-2026-041 · Corvid Metrics · Tier 2 · Assessment: SOC 2 Type II reviewed (period ended 2025-07-31, stale — bridge pending) · Residual risk: Medium until Conditions A–C close · Review: at new report receipt or 2027-01, whichever first · Owner: vendor-mgmt`
