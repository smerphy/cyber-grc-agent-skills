# Risk Scoring & Analysis Methods

How to analyze and score cyber risk without fooling yourself. Covers qualitative matrices, semi-quantitative scoring, quantitative analysis (FAIR), vulnerability-score contextualization, aggregation pitfalls, and how to pick a method for the decision at hand. Terminology: [glossary.md](glossary.md). Applied procedure: [../skills/risk-assessment/SKILL.md](../skills/risk-assessment/SKILL.md).

Governing principle: **a score exists to support a decision.** If a rating cannot change what someone does — treatment choice, budget, priority order, acceptance — it is theater. Choose the cheapest method that reliably supports the decision.

## Qualitative 5x5 matrices

The default for enterprise risk registers. Valid only when every scale point has a written, calibrated anchor. Unanchored "High/Medium/Low" scoring produces ratings that measure the assessor's mood.

### Example likelihood scale (frequency-anchored)

Anchor likelihood as an expected frequency of the *loss event* (not the attack attempt), over a defined horizon:

| Level | Label | Anchor (per year) |
|---|---|---|
| 1 | Rare | Less than once in 25 years (<4%/yr) |
| 2 | Unlikely | Once in 10–25 years (4–10%/yr) |
| 3 | Possible | Once in 3–10 years (10–33%/yr) |
| 4 | Likely | Once in 1–3 years (33–100%/yr) |
| 5 | Almost certain | One or more times per year |

### Example impact scale (multi-dimension anchors)

Calibrate the financial band to the organization — the example below suits an organization with roughly $100M–$1B revenue; scale bands proportionally. Rate a scenario at the **highest** applicable dimension, and record which dimension drove it.

| Level | Financial | Operational | Legal / regulatory | Reputational |
|---|---|---|---|---|
| 1 Minimal | <$50k | Negligible disruption; no customer impact | None expected | Not externally visible |
| 2 Minor | $50k–$500k | Single team/process degraded <1 day | Reportable to no one; contractual notice possible | Isolated customer complaints |
| 3 Moderate | $500k–$5M | Business unit disrupted 1–3 days; SLA breaches | Regulator notification; findings likely | Local/trade press; some customer attrition |
| 4 Major | $5M–$25M | Critical service down >3 days or multi-unit outage | Enforcement action, material fines, or litigation | National press; measurable churn; executive scrutiny |
| 5 Severe | >$25M | Enterprise-wide or safety-impacting outage | Loss of license/authorization; criminal exposure; class actions | Sustained international coverage; lasting brand damage |

### Rules for using the matrix

1. **Score scenarios, not categories.** "Ransomware encrypts the ERP via a compromised admin workstation" is scoreable; "malware risk" is not.
2. Score **inherent and residual** separately, naming the controls that account for the difference.
3. Define rating bands on the grid explicitly (e.g., product 1–4 Low, 5–9 Moderate, 10–14 High, 15–25 Critical) and treat the product as a **bucket label, not a number** — see the ordinal-arithmetic warning below.
4. Record rationale and key assumptions per score; unexplainable scores cannot be re-reviewed or challenged.
5. Calibrate as a group: have multiple assessors score a shared set of reference scenarios and reconcile systematic bias before scoring the register.

## Semi-quantitative scoring and its pitfalls

Semi-quantitative methods assign numbers to ordinal levels and compute with them (weighted factor models, vendor-risk scorecards, most GRC-tool "risk scores").

**The ordinal arithmetic warning.** Scale labels 1–5 are ranks, not quantities. The distance between "4 Likely" and "5 Almost certain" is not the distance between 1 and 2, and a frequency anchor spanning <4%/yr to >100%/yr is wildly non-linear. Consequences:

- **Multiplication is not meaningful.** L4×I2 = 8 vs. L2×I4 = 8 look identical but can differ by orders of magnitude in expected loss. Products can also *reverse* true rankings (a 1-in-25-year, $30M scenario scores 1×5=5 "Moderate"; a weekly $10k nuisance scores 5×1=5 the same).
- **Averaging ordinals is undefined.** The mean of a "2" and a "4" control gap is not a "3" anything. Weighted averages of questionnaire answers inherit the same flaw plus arbitrary weights.
- **Range compression.** Real cyber losses span 5+ orders of magnitude; a 1–5 scale compresses that into five buckets, so the top bucket hides everything from "bad quarter" to "existential."
- **False precision.** A composite score of 3.72 carries decimal places that no input justifies. Report the bucket, not the decimals.

Legitimate uses: forced-rank prioritization within a homogeneous set (e.g., triaging 40 vendor assessments), where only ordering matters and no one treats the score as magnitude. Never use semi-quantitative outputs to justify spend ("this control reduces score by 6 points") — that claim needs quantitative form.

## Quantitative analysis — FAIR overview

FAIR (Factor Analysis of Information Risk; Open Group standard) expresses risk as a distribution of probable loss in currency, decomposing:

**Risk = Loss Event Frequency (LEF) x Loss Magnitude (LM)**

- **LEF** decomposes into Threat Event Frequency (how often the threat acts against the asset) x Vulnerability (the probability a threat event becomes a loss event, i.e., the attack overcomes resistance).
- **LM** splits into **primary loss** (borne directly: response, replacement, productivity) and **secondary loss** (from stakeholder reactions: fines and judgments, customer churn, credit monitoring, reputation) with its own frequency and magnitude.

Method, honestly summarized:

1. **Scope a precise loss scenario** (asset, threat, effect) — same discipline as qualitative scoping.
2. **Estimate each factor as a calibrated range** (minimum / most likely / maximum, typically at a 90% confidence interval), not a point value. Calibration training (reference-class questions, equivalent-bet tests) demonstrably improves estimators; uncalibrated experts are systematically overconfident.
3. **Run a Monte Carlo simulation**: sample each factor's distribution (commonly PERT/beta-PERT) thousands of times, multiply through the model, and aggregate.
4. **Read results as distributions**: report the annualized loss range (e.g., 10th/50th/90th percentiles) and a loss exceedance curve ("10% chance of exceeding $8M/yr"), never a single expected value — the tail is usually what matters for decisions.

Strengths: outputs in money support cost-benefit and insurance decisions; assumptions are explicit and challengeable; ranges honestly carry uncertainty. Limits and failure modes: garbage-in still applies (calibration is the real work); analysis cost is high, so reserve it for top scenarios; a Monte Carlo over invented point estimates is qualitative guessing wearing a lab coat. Do not report "$4.7M expected annual loss" from inputs with order-of-magnitude uncertainty — fake precision destroys the method's credibility.

## CVSS is severity, not risk

A CVSS base score measures the **technical severity characteristics of a vulnerability in the abstract** — exploitability metrics and impact on the vulnerable component. It says nothing about *your* probability of experiencing a loss or its size. "CVSS 9.8 therefore critical risk" is the single most common scoring error in vulnerability management.

To turn severity into a prioritization signal, contextualize with:

- **Exploitation likelihood:** EPSS (Exploit Prediction Scoring System) estimates the probability a vulnerability will be exploited in the wild in the next 30 days; CISA's KEV catalog lists vulnerabilities with confirmed active exploitation. A KEV-listed CVSS 7.5 on an internet-facing system outranks a CVSS 9.8 with negligible EPSS on an isolated host.
- **Asset context:** criticality of the affected asset (BIA tier, data classification), exposure (internet-facing vs. segmented), and privileges attainable.
- **Compensating controls:** WAF rules, segmentation, EDR coverage, exploit mitigations that reduce practical exploitability — the intent of CVSS environmental/threat metrics, which almost no one populates.
- **Decision-tree alternatives:** SSVC (Stakeholder-Specific Vulnerability Categorization) replaces scores with explicit decisions (exploitation status, exposure, mission impact → act/track/defer) and is often a better operational fit than score thresholds.

A practical priority rule: (KEV or high EPSS) AND exposed AND critical asset → fix now; escalating SLAs for the descending combinations. Encode the rule; don't re-litigate per ticket. See [../skills/risk-assessment/SKILL.md](../skills/risk-assessment/SKILL.md) and, for treatment deadlines, [../skills/exception-management/SKILL.md](../skills/exception-management/SKILL.md).

## Risk aggregation pitfalls

Roll-ups to board level are where good scenario-level analysis goes to die. Watch for:

1. **Averaging across risks.** The mean of the register hides the tail — one existential risk averaged against forty trivia looks "moderate." Report top-N scenarios and the tail, not the mean.
2. **Summing ordinal scores.** "Total risk score 372, down from 401" is numerology; the sum of ranks has no unit. Track count-by-band movements and specific top-risk changes instead.
3. **Max-only heatmap roll-ups.** Reporting only the worst cell ignores accumulation of many moderate risks that share a common cause or budget.
4. **Ignoring correlation and common cause.** Portfolio views that treat risks as independent understate aggregate exposure: one cloud region failure, one identity provider compromise, or one shared third party can fire many register entries simultaneously. Aggregate quantitatively only with explicit correlation assumptions — or at least tag common-cause clusters (see concentration risk in [../skills/third-party-risk-assessment/SKILL.md](../skills/third-party-risk-assessment/SKILL.md)).
5. **Double counting.** The same underlying scenario entered by three business units inflates aggregate exposure; deduplicate by scenario, not by reporter.
6. **Mixing inherent and residual** in one view, or comparing this quarter's residual against last quarter's inherent.
7. **Appetite mismatch.** Appetite statements set at portfolio level cannot be tested against single-scenario ratings without an aggregation method; conversely, per-scenario tolerances don't sum to portfolio appetite.

## Choosing a methodology by decision type

| Decision to support | Method | Why |
|---|---|---|
| Maintain enterprise risk register; board-level relative visibility | Qualitative 5x5 with calibrated anchors | Cheap, comparable across domains; ranking is the goal |
| Prioritize a large homogeneous queue (vulns, vendors, findings) | Rule-based triage (KEV/EPSS/exposure/criticality) or forced ranking | Ordering decision; scores need only be consistent, not true |
| Justify a specific control investment or compare treatment options | FAIR / quantitative on the relevant scenarios | Cost-benefit requires magnitude in money |
| Set cyber insurance limits and retentions | Quantitative with loss exceedance curve | The decision is literally about the tail of a loss distribution |
| Accept a specific residual risk | Scenario analysis at the depth matching exposure: qualitative for low bands, quantified range for large exposures | Acceptance authority should see the honest size of what they sign |
| Regulatory or framework-mandated risk assessment (ISO 27001, DPIA) | Method-agnostic but documented, repeatable, criteria-driven | Regulators/auditors test process quality and consistency, not the arithmetic |
| Aggregate/portfolio exposure reporting | Quantitative with correlation assumptions, or qualitative top-N + common-cause clusters | Ordinal roll-ups mislead; see pitfalls above |

Hybrid is the norm in practice: a qualitative register for breadth, quantitative deep-dives on the top 5–10 scenarios, and rule-based triage in operational queues. Document which method governs which decision so numbers from different methods are never compared to each other.

## Related

- [glossary.md](glossary.md) — inherent/residual risk, appetite vs. tolerance, KRI definitions
- [../skills/risk-assessment/SKILL.md](../skills/risk-assessment/SKILL.md) — end-to-end assessment procedure using these methods
- [../skills/grc-metrics-reporting/SKILL.md](../skills/grc-metrics-reporting/SKILL.md) — reporting risk without aggregation traps
- [../skills/dpia-privacy-assessment/SKILL.md](../skills/dpia-privacy-assessment/SKILL.md) — risk-to-individuals analysis, a different lens than enterprise risk

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
