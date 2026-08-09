# System Inventory

**Status: TEMPLATE — not filled in.**

*The key systems agents need to reason about scope, criticality, and blast radius — consumed by [risk-assessment](../../skills/risk-assessment/SKILL.md), [bcdr-readiness](../../skills/bcdr-readiness/SKILL.md) (BIA input), [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) (what data was where), and [dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md). This is the decision-support view, not a CMDB replacement: keep it to systems that matter and record where the authoritative inventory lives. Agents: while the status is TEMPLATE, the rows below are illustrative, not your systems.*

## Conventions

| Field | Value |
|---|---|
| Criticality tiers | [example: Tier 1 = revenue/safety critical, RTO ≤ 4h · Tier 2 = important, RTO ≤ 24h · Tier 3 = deferrable] |
| Data classification scheme | [example: Public / Internal / Confidential / Restricted; personal data flagged separately] |
| Authoritative inventory | [example: CMDB in ITSM tool; this file is the curated Tier 1–2 extract] |
| Personal-data detail | [example: full processing detail lives in the RoPA — see skills/ropa-data-mapping] |

## Inventory

| System | Tier | What it does | Data classes | Personal data | Hosting | Internet-facing | Owner |
|---|---|---|---|---|---|---|---|
| [example: Payment platform] | [example: 1] | [example: core transaction processing] | [example: Restricted] | [example: yes — customer financial] | [example: cloud, EU regions] | [example: yes] | [example: Head of Platform] |
| [example: Customer portal] | [example: 1] | [example: customer self-service] | [example: Confidential] | [example: yes — contact, account] | [example: cloud, EU] | [example: yes] | [example: Head of Product Eng] |
| [example: HR system (SaaS)] | [example: 2] | [example: HR records, payroll feed] | [example: Restricted] | [example: yes — employee] | [example: vendor SaaS] | [example: yes] | [example: Head of People] |
| [example: Data warehouse] | [example: 2] | [example: analytics/reporting] | [example: Confidential] | [example: yes — pseudonymized] | [example: cloud, EU] | [example: no] | [example: Head of Data] |

## Known blind spots

*An inventory that admits its gaps is worth more than one that claims completeness — unmanaged-asset rate is a KRI for a reason.*

| Blind spot | Risk | Plan |
|---|---|---|
| [example: SaaS tools procured outside IT] | [example: unassessed personal-data processing] | [example: SSO+expense sweep quarterly; TPRM intake enforcement] |

**Document owner:** [name/team] · **Review cycle:** [example: quarterly extract refresh; tier definitions annually]
