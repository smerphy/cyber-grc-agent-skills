# Exception Criteria: Approval Matrix, Evidence, Escalation

Default criteria for organizations without their own exception standard. Where an organizational authority matrix exists, it wins; use this file to sanity-check it (an org matrix that lets a team lead approve High-risk exceptions is a finding, not a convention).

## Approval authority matrix (default)

Residual risk level refers to the score **with** proposed compensating controls operating, on the organization's matrix. Where band names differ, map by position (e.g., a 5x5 matrix: Low ≈ 1–4, Medium/Moderate ≈ 5–9, High ≈ 10–14, Critical ≈ 15–25, per the example banding in [../../../context/risk-scoring.md](../../../context/risk-scoring.md) — adjust to the org's actual banding).

| Residual risk | Approvers (all required) | Max initial term | Max renewals before mandatory escalation | Review lead time | Register visibility |
|---|---|---|---|---|---|
| **Low** | Security/GRC manager + business asset owner | 12 months | 2 (then Medium-level approval) | 30 days before expiry | Exception register |
| **Medium** | CISO or formally named delegate + business unit leader | 12 months | 1 (then High-level approval) | 30 days | Exception register + risk register cross-ref |
| **High** | CISO (no delegation) + executive risk owner (CIO/COO/CFO per asset) | 6 months | 1 (then Critical-level approval) | 60 days | Risk committee agenda item |
| **Critical / above appetite** | Executive risk committee (quorum decision); CEO or board risk committee where org policy requires | 3 months, only with funded remediation in flight | 0 — renewal is a new committee decision | 60 days | Standing risk committee item until closed |

Rules that override the matrix:

- **Self-approval prohibition:** no approver may be the requester, sit in the requester's reporting line below the required level, or own the exception's exit plan delivery. If the CISO's own team requests the exception, business-side approval must come from outside the CISO chain and one level higher than the matrix requires.
- **Escalation triggers (+1 authority level regardless of score):** regulated data in scope (cardholder, health, personal data at scale); crown-jewel assets; scope inside an externally certified/attested boundary (ISO 27001, SOC 2, PCI DSS); third consecutive renewal of any exception; aggregation with existing exceptions producing a combined higher band.
- **Automatic rejection (do not route for approval):** deviation from a legal or regulatory obligation; no expiry proposed; residual Medium+ with no compensating controls; requester unable to name the requirement deviated from.

## Compensating control standard

A compensating control is acceptable only if it meets all four tests (aligned with the intent of PCI DSS's compensating-control criteria, applied generally):

1. **Same threat:** addresses the threat the original requirement addresses, not a neighboring one. (Extra logging does not compensate for missing encryption; it changes detection, not exposure.)
2. **Comparable rigor:** provides risk reduction commensurate with the original control, alone or in combination.
3. **Beyond baseline:** is not something already required elsewhere — an existing mandatory control cannot be double-counted as compensation.
4. **Evidenced:** is demonstrably operating (config export, monitoring output, test result) before the exception activates, or has a hard activation date that gates the exception's effective date.

## Required evidence by risk level

| Evidence item | Low | Medium | High | Critical |
|---|---|---|---|---|
| Completed intake form (scope, justification, duration, exit plan) | Required | Required | Required | Required |
| Named requirement/control ID deviated from | Required | Required | Required | Required |
| Risk assessment (event-based statement, inherent + residual scores, rationale) | Short form | Required | Required + independent GRC review | Required + independent review + scenario analysis |
| Compensating controls with operating evidence | If proposed | Required | Required, tested within last 90 days | Required, tested within last 30 days |
| Exit plan with funded owner and milestone dates | Statement | Required | Required + project reference | Required + committee-tracked milestones |
| Prior exception history for asset/requirement | — | Required | Required | Required |
| Aggregation analysis (combined exposure with existing exceptions) | — | If same asset/control | Required | Required |
| Legal/compliance sign-off that no regulatory obligation is breached | — | If regulated data | Required | Required |
| Business impact statement of denying the exception | — | — | Required | Required |

## Escalation paths

- **Disputed risk score** (requester vs GRC): decided at the next authority level up; the higher score's authority level applies while disputed.
- **Approver unavailable:** formally named delegate only; delegation of Critical-level approval is not permitted — the decision waits or goes to the committee chair.
- **Urgent operational need** (outage-driven, cannot wait for committee): time-boxed emergency exception ≤14 days may be granted by CISO + one executive, with mandatory ratification or termination at the next committee session. Emergency exceptions cannot be renewed as emergencies.
- **Expired without action:** day 1 after expiry → status "Expired-violation", control owner notified, reported in the next compliance report. Day 30 → escalate to the authority level above the original approver. Serial expiry (twice for the same exception) → risk committee item.
- **Discovered undocumented deviation:** log immediately with discovery date, assess as a new request at +1 evidence rigor, and record the unmanaged period in the register; route root cause (why was it undetected?) to control-owner remediation.

## Duration guidance

- Default to the shortest term the exit plan supports; the matrix maxima are ceilings, not defaults.
- Tie expiry to a milestone with a hard backstop date ("upon migration completion, no later than YYYY-MM-DD").
- Renewal = full re-approval: fresh risk score, fresh compensating-control evidence, demonstrated exit-plan progress. An exception renewed without exit-plan progress twice is de facto permanent risk acceptance and must be either escalated for explicit long-horizon acceptance at the higher authority level (with annual re-certification) or converted into a remediation mandate.

## Example completed exception record

---

**Exception ID:** EXC-2026-018
**Status:** Active
**Requirement deviated from:** Endpoint Security Standard §3.1 — "EDR agent required on all servers processing Confidential data."
**Scope:** SRV-LAB-04 and SRV-LAB-05, two Windows Server hosts running vendor-locked laboratory instrument software (Confidential research data, isolated lab VLAN, no internet egress). No other assets.
**Requester:** R. Okafor, Lab IT Lead — submitted 2026-05-28.
**Business justification:** Instrument vendor certifies the control software only on a fixed OS image; EDR agent installation voids support and has crashed acquisition runs in testing. Vendor's EDR-compatible release is scheduled for 2027-Q1. Instruments support active research contracts worth $2.3M/yr.
**Risk statement:** Risk that malware on the lab servers persists undetected due to absent EDR telemetry, resulting in research data theft or corruption and lateral movement attempts toward the corporate network.
**Inherent risk:** Likelihood 3 x Impact 4 = 12 (High) — no endpoint detection, Confidential data, Windows targets.
**Compensating controls:**
1. Lab VLAN isolated; firewall permits only instrument-to-storage flows, deny-all otherwise (ruleset export reviewed 2026-06-05).
2. No internet egress from either host; USB ports disabled via GPO (config attestation 2026-06-05).
3. Network IDS sensor on the lab VLAN with alerting to SOC (alert test 2026-06-06).
4. Weekly offline snapshot of research data to immutable storage (restore test 2026-06-10).
**Residual risk:** Likelihood 2 x Impact 3 = 6 (Medium) — initial-access and lateral-movement paths materially constrained; data recoverable. Independent GRC review: concur (T. Nguyen, 2026-06-11).
**Aggregation check:** no other exceptions on these assets or against §3.1. No combined-exposure change.
**Legal/compliance check:** no regulatory obligation mandates EDR specifically; research data contractual clauses reviewed — isolation satisfies "industry-standard safeguards" language (Counsel, 2026-06-12).
**Approval routing:** Residual Medium, escalated one level per the Confidential-data trigger → CISO (no delegation) J. Ortiz + BU Director Research S. Adeyemi. Approved 2026-06-16. Condition: any IDS critical alert on the lab VLAN suspends the exception pending review.
**Effective:** 2026-06-16. **Review date:** 2026-11-16. **Expiry:** upon vendor EDR-compatible release deployment, no later than 2027-03-31.
**Exit plan:** Deploy vendor 2027-Q1 release with EDR agent; owner R. Okafor; milestone: vendor beta validation 2026-12-15.
**Risk register cross-reference:** RSK-2026-041 (accepted, Medium).
**Re-certification history:** none yet; first review scheduled with fresh IDS alert-test evidence required.

---

Use this record as the completeness bar: every field populated, every control evidenced with a date, approval names and conditions verbatim, and expiry double-bounded (milestone + hard date).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
