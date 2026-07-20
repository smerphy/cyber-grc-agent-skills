# Example: NIST CSF 2.0 Gap Assessment (Excerpt)

**Persona:** grc-analyst · **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md) · **Context loaded:** [nist-csf-2](../context/frameworks/nist-csf-2.md), maturity anchors from [maturity-scale](../skills/framework-gap-assessment/references/maturity-scale.md)

All entities are fictional. This excerpt shows the scope statement, two scored functions, and the top of the remediation roadmap; a full report covers all six functions.

---

## User input

> Assess us against NIST CSF 2.0. We're Halvard Payments — 340 employees, payment orchestration SaaS, AWS multi-region, ~90 engineers. No dedicated GRC team until I was hired last month. I've uploaded our policy set (11 docs), last pen test report, and you interviewed our CTO, platform lead, and IT manager yesterday.

## Agent output (deliverable, excerpt)

### Scope statement (frozen 2026-07-08)

Assessment of Halvard Payments B.V. against **NIST CSF 2.0, scored at category level** (22 categories, 6 functions) on the library's 5-level maturity scale (1 Not Performed → 5 Optimized). Boundary: production SaaS platform and corporate IT; excludes the acquired Voss Ledger entity (integration pending, assessed separately in Q4). Evidence cutoff 2026-07-05: 11 policy documents, 2026-03 penetration test report, AWS config exports, 3 structured interviews. Target profile agreed with CTO: **level 3 across all categories by Q2 2027**, level 4 for PR.AA and DE.CM.

### GOVERN (GV) — function score: 1.8 · target 3 · gap: HIGH

| Category | Score | Evidence basis | Key finding |
|---|---|---|---|
| GV.OC Organizational context | 2 | Interview (CTO); no documented mission/stakeholder analysis for security | Security objectives exist in heads, not documents; no linkage to business objectives |
| GV.RM Risk management strategy | 1 | No risk register, no risk appetite statement produced on request | **No risk management process exists.** Decisions are ad hoc; nothing to audit |
| GV.RR Roles & responsibilities | 2 | Org chart; interviews conflicted on incident ownership | CTO and platform lead each believe the other owns vendor security |
| GV.PO Policy | 2 | 11 policies reviewed; 7 past review date; AUP references a firewall product retired in 2024 | Policies exist but are stale and unowned — governance theater risk |
| GV.OV Oversight | 1 | No management review cadence, no metrics reach leadership | Board has never received a security report |
| GV.SC Supply chain risk mgmt | 1 | No vendor inventory; contracts sampled (n=3) lack security clauses | Unmanaged — see roadmap item 2 |

*Interview vs. document conflict noted per procedure: platform lead described a "quarterly risk review" no artifact supports — scored on observed practice (GV.RM = 1), conflict logged as its own finding.*

### PROTECT (PR) — function score: 2.6 · target 3 (PR.AA: 4) · gap: MEDIUM

| Category | Score | Evidence basis | Key finding |
|---|---|---|---|
| PR.AA Identity & access | 3 | Okta SSO + MFA enforced (config export); quarterly access review ran twice, evidenced once | Strong tooling; review evidence inconsistent — one of two quarters has no artifact |
| PR.AT Awareness & training | 2 | Onboarding training only; 61% completion on last phishing module | No role-based training for engineers with production access |
| PR.DS Data security | 3 | KMS encryption at rest verified in config; TLS everywhere per pen test | Key rotation manual; no data classification to drive handling rules |
| PR.PS Platform security | 3 | IaC + drift detection on prod accounts; hardening baseline for EKS | Laptops unmanaged for 40% of fleet (no MDM on contractor devices) |
| PR.IR Technology infrastructure resilience | 2 | Multi-AZ verified; last restore test 14 months ago, single database only | Declared RPO 1h is aspiration, not demonstrated — see roadmap item 3 |

### Remediation roadmap (top 3 of 12)

| # | Gap | Action | Effort | Priority rationale |
|---|---|---|---|---|
| 1 | GV.RM = 1 | Stand up risk management: appetite statement, register seeded via [risk-assessment](../skills/risk-assessment/SKILL.md), monthly review | M | Every other gap's prioritization depends on it; auditors and enterprise customers ask for it first |
| 2 | GV.SC = 1 | Vendor inventory + tiering + security clauses in renewals via [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) | M | Payment-flow vendors unassessed; concentration risk unknown |
| 3 | PR.IR = 2 | Scheduled restore tests across all data stores; measure against declared RPO/RTO | S | Cheapest way to remove the largest silent assumption; a ransomware event would test it for you |

### Quality checklist result

Scores traceable to named evidence: ✔ (every cell cites artifact or interview) · Conflicts resolved to observed practice: ✔ (2 logged) · No category scored without evidence: ✔ — GV.OV and GV.SC scored 1 on documented absence, which is itself evidence · Target profile agreed before scoring: ✔
