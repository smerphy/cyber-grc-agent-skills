---
name: risk-assessment
description: >-
  Runs a structured cyber risk assessment and produces risk register entries: establishes
  context and risk appetite, identifies risks via threat-, asset-, and scenario-based
  techniques, scores likelihood and impact, documents inherent vs residual risk, and
  proposes treatments. Use when asked to "assess risk", "build/update the risk register",
  "score this risk", "identify cyber risks for X", or "what are our top risks".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

# Cyber Risk Assessment

## Purpose

Produce a defensible cyber risk assessment: a set of well-formed, scored, treatment-assigned risk register entries tied to a defined scope and risk appetite. The output is decision-ready material for a risk committee, not a vulnerability list. This skill covers enterprise, project, and system-level assessments using qualitative or semi-quantitative scoring.

## When to use

- Building or refreshing a risk register (enterprise, business unit, project, or system scope).
- Assessing risk for a new system, initiative, major change, or identified threat.
- Converting audit findings, pen-test results, or incident lessons into register-ready risks.
- Re-scoring existing risks after control changes or environment shifts.

**When NOT to use:**

- Assessing a vendor or supplier — use [third-party-risk-assessment](../third-party-risk-assessment/SKILL.md).
- Assessing privacy risk to data subjects from a processing activity — use [dpia-privacy-assessment](../dpia-privacy-assessment/SKILL.md).
- Evaluating a request to deviate from a control (the risk is accepted, not treated) — use [exception-management](../exception-management/SKILL.md).
- Measuring compliance posture against a framework — use [framework-gap-assessment](../framework-gap-assessment/SKILL.md). Gaps found there can feed this skill as risk inputs.

## Inputs to gather

Ask for these before starting; state assumptions explicitly for anything unavailable:

1. **Scope and objective** — enterprise-wide, a business unit, a system, a project, or a single scenario? What decision will the assessment inform?
2. **Methodology constraints** — existing risk matrix (scale dimensions, definitions), scoring method mandate (qualitative, semi-quantitative, FAIR), and any framework alignment required (e.g., ISO 27005, NIST SP 800-30). See [risk scoring methodology](../../context/risk-scoring.md) before choosing — do not invent a scale if one exists.
3. **Risk appetite / tolerance** — appetite statements, tolerance thresholds per impact category, or at minimum "what risk level requires executive attention?"
4. **Asset and context information** — critical assets/services in scope, data classifications, crown jewels, architecture summary, dependencies (cloud providers, key vendors, single points of failure).
5. **Threat landscape inputs** — recent incidents (own and sector), threat intel relevant to the industry, known adversary interest.
6. **Current controls** — control framework in use, recent gap assessment or audit results, known deficiencies, open findings.
7. **Existing register** — current risk register (to avoid duplicates and reuse IDs/taxonomy) and the register schema if one is mandated.

## Procedure

### 1. Establish context

1. Confirm scope boundary in writing: what systems, processes, locations, and data are in/out.
2. Fix the scoring scale before identifying anything. Default to a 5x5 likelihood x impact matrix unless the organization has its own. Define each level with concrete anchors (e.g., Likelihood 4 = "once in 1–3 years / has occurred in sector peers recently"; Impact 4 = "financial loss $5M–$25M, or enforcement action or material fines, or critical service down >3 days" — the example likelihood and impact tables in [../../context/risk-scoring.md](../../context/risk-scoring.md) provide a full anchor set). Ordinal scales without anchors produce noise — see [risk scoring pitfalls](../../context/risk-scoring.md).
3. Record risk appetite as a line on the matrix: which cells are acceptable, which require treatment, which require escalation.
4. List in-scope assets/services with a criticality rating. If no asset inventory exists, build a minimal one (top 10–20 assets by business criticality) rather than proceeding assetless.

### 2. Identify risks (use all three lenses, then deduplicate)

- **Threat-based:** walk relevant threat categories (external attacker, insider, third party, environmental/technical failure) against the asset list. Use the [scenario library](references/scenario-library.md) as a completeness prompt, not a copy source — keep only scenarios plausible for this context, and tailor drivers.
- **Asset-based:** for each critical asset, ask what loss of confidentiality, integrity, and availability would mean, and what could cause each.
- **Scenario-based:** develop 3–8 narrative scenarios for the highest-stakes combinations (e.g., "ransomware encrypts the ERP and backups during quarter close"). Scenarios force impact realism that category-walking misses.

**Decision point:** stop identifying when new candidates are variants of existing entries. A focused register of 15–40 well-formed risks beats 200 control gaps relabeled as risks.

Write every candidate as an event-based risk statement: **"Risk that [event] due to [cause/driver] resulting in [consequence]."** Never register a control gap ("we lack MFA") as a risk — the gap is a driver inside a risk statement, not the risk. See [risk statement patterns](references/risk-statement-patterns.md) for good/bad examples and rewrites. Test each statement: does it name an event that could happen on a date? If not, rewrite.

### 3. Analyze — inherent and residual

For each risk:

1. **Inherent (or "current-controls-absent") score:** rate likelihood and impact assuming key controls fail or are absent. If the organization's methodology uses "current risk" instead of true inherent, follow their convention — but label which convention is used.
2. **Identify current controls** that actually operate against this risk (preventive, detective, corrective). Name specific controls, not aspirations ("EDR deployed on 92% of endpoints", not "we have endpoint security"). Pull control status from any recent [control testing](../control-testing/SKILL.md) or gap assessment output rather than assuming controls work.
3. **Residual score:** re-rate likelihood and impact with current controls operating at their observed (not designed) effectiveness.
4. Rate impact on the organization's defined categories (typically financial, operational, regulatory/legal, reputational; take the highest, or follow the org's aggregation rule). Note which category drives the score.
5. Record rationale for every score in one or two sentences. Unrationalized scores are unauditable and get re-litigated in committee.

**Decision point:** if a risk's residual score is highly sensitive to one uncertain assumption (e.g., "backups are restorable"), flag it as a key assumption and recommend validation rather than guessing.

### 4. Evaluate against appetite

Compare each residual score to the appetite line from step 1.3:

- **Within appetite** → candidate for Accept (document, monitor, set review date).
- **Above appetite** → requires treatment; priority order by residual score, then by velocity (how fast it could materialize) as a tiebreaker.
- **Far above appetite / intolerable** → escalate immediately; do not wait for the report cycle.

### 5. Propose treatments

For each risk above appetite, propose one primary treatment with rationale:

| Treatment | Use when | Register requirements |
|---|---|---|
| **Mitigate** | Controls can feasibly reduce likelihood or impact at proportionate cost | Named actions, owner, due date, expected residual after treatment |
| **Transfer** | Financial impact insurable or contractually shiftable (cyber insurance, vendor liability terms) | Note: transfer rarely moves regulatory/reputational impact — score what remains |
| **Avoid** | Activity's risk exceeds its value; org can stop or redesign it | Decision owner and deprecation path |
| **Accept** | Residual within appetite, or treatment cost disproportionate | Formal acceptance by the right authority and a review date — route via [exception-management](../exception-management/SKILL.md) if acceptance means deviating from a mandated control |

For mitigations, state the expected post-treatment residual score so leadership sees what they are buying. Do not propose "implement framework X" as a treatment — name the 1–3 specific controls that move this risk's score.

### 6. Write register entries

Emit entries in the fixed schema below (matches [templates/risk-register.csv](../../templates/risk-register.csv)). One row per risk. Assign IDs continuing the existing register's sequence if one exists.

### 7. Package and route

1. Summarize: scope, method, matrix used, count of risks by residual band, top 5 risks, risks escalated as above-appetite.
2. Name what the assessment did NOT cover (out-of-scope items, unvalidated assumptions).
3. Recommend register review cadence (quarterly for enterprise registers is typical; after material change for system-level).
4. Hand top-risk metrics to [grc-metrics-reporting](../grc-metrics-reporting/SKILL.md) if a reporting pack is needed.

## Output format

Deliverable = (a) assessment summary, (b) register entries.

**Register entry schema (fixed):**

| Field | Content |
|---|---|
| Risk ID | e.g., RSK-2026-014 (continue existing sequence) |
| Title | ≤10 words, event-focused |
| Risk statement | "Risk that [event] due to [cause] resulting in [consequence]" |
| Category | Org taxonomy (e.g., Cyber – Availability; Cyber – Data Breach; Third Party) |
| Assets/scope affected | Named systems, data, services |
| Inherent likelihood / impact / score | With one-line rationale |
| Current controls | Named controls with observed effectiveness |
| Residual likelihood / impact / score | With one-line rationale; note driving impact category |
| Appetite status | Within / Above / Intolerable |
| Treatment | Mitigate / Transfer / Avoid / Accept + specific actions |
| Treatment owner & due date | Named role (not "IT"), date |
| Expected post-treatment residual | Score |
| Risk owner | Accountable role |
| Review date | Explicit date |
| Status | New / Open / In treatment / Accepted / Closed |

**Worked example (abbreviated):**

> **RSK-2026-014 — Ransomware outage of order-management platform**
> Risk that a ransomware actor encrypts the order-management platform and connected file shares due to phishing-delivered initial access and flat internal network segmentation, resulting in multi-day fulfilment outage, recovery cost, and customer contractual penalties.
> Category: Cyber – Availability. Assets: OMS, WMS integration, EU order data.
> Inherent: L4 x I5 = 20 (sector peers hit twice in 18 months; no segmentation between user LAN and OMS).
> Current controls: EDR (96% coverage), offline weekly backups (restore untested >12 months), email filtering. Residual: L3 x I4 = 12 — above appetite (threshold 9).
> Treatment: Mitigate — (1) segment OMS VLAN from user network, owner: Head of Infrastructure, due 2026-10-31; (2) quarterly restore test of OMS backups, owner: IT Ops Manager, due 2026-08-31. Expected post-treatment residual: L2 x I4 = 8.
> Risk owner: COO. Review: 2026-11-15. Status: In treatment.

## Quality checklist

- [ ] Scoring scale has concrete anchors for every level; matrix and appetite line documented before identification began.
- [ ] Every risk statement is event-based ("risk that X due to Y resulting in Z") — zero control-gap statements registered as risks.
- [ ] All three identification lenses (threat, asset, scenario) applied; deduplication performed.
- [ ] Every likelihood and impact rating has a written rationale; driving impact category noted.
- [ ] Inherent and residual both recorded; convention (true inherent vs current risk) labeled.
- [ ] Current controls named specifically with observed effectiveness, not assumed design effectiveness.
- [ ] Every above-appetite risk has a treatment with named owner (role), due date, and expected post-treatment residual.
- [ ] Every accepted risk has a named accepting authority and review date.
- [ ] Key assumptions and out-of-scope items stated in the summary.
- [ ] Register entries match the fixed schema; IDs continue the existing sequence.

## References

- [references/risk-statement-patterns.md](references/risk-statement-patterns.md) — good vs bad risk statements with worked rewrites
- [references/scenario-library.md](references/scenario-library.md) — starter library of ~20 cyber risk scenarios with drivers and impact types
- [../../templates/risk-register.csv](../../templates/risk-register.csv) — register template matching the output schema
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — matrix design, FAIR overview, CVSS caveats, aggregation pitfalls
- [../../context/glossary.md](../../context/glossary.md) — term definitions (inherent, residual, appetite, tolerance)
- [../../context/internal/risk-appetite.md](../../context/internal/risk-appetite.md) and [../../context/internal/system-inventory.md](../../context/internal/system-inventory.md) — the organization's appetite statements, thresholds, and system criticality, if filled in (respect the status marker)
- Related skills: [exception-management](../exception-management/SKILL.md), [third-party-risk-assessment](../third-party-risk-assessment/SKILL.md), [framework-gap-assessment](../framework-gap-assessment/SKILL.md), [control-testing](../control-testing/SKILL.md), [grc-metrics-reporting](../grc-metrics-reporting/SKILL.md), [dpia-privacy-assessment](../dpia-privacy-assessment/SKILL.md)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
