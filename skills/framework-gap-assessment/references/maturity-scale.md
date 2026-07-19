# Maturity Scale: Scoring Anchors

Five-level scale used by the framework gap assessment skill. Semantics follow CMMI-style progression (initial → repeatable/defined → quantitatively managed → optimizing) collapsed into five practitioner-friendly levels. Score at the domain granularity chosen in the assessment workbook (CSF category, ISO clause/theme, CIS control, SOC 2 CC-series, 800-53 family, PCI requirement).

## The scale

| Level | Name | Core question it answers |
|---|---|---|
| 1 | Not Performed | Does the activity exist at all? — No |
| 2 | Ad Hoc | Does it happen? — Sometimes, depending on who and when |
| 3 | Defined | Is it documented, approved, and done as written? — Yes |
| 4 | Managed | Is it measured, and are deviations corrected? — Yes |
| 5 | Optimized | Does measurement drive continuous improvement? — Yes |

## Level 1 — Not Performed

**Semantic:** The activity does not occur. There may be no awareness that it should, or awareness with no action.

Anchors (all typically true):
- No policy, standard, or procedure references the activity.
- Interviewees cannot describe anyone performing it, even informally.
- No tooling, tickets, or artifacts exist.
- If the activity is legally or contractually required, the organization is exposed with no compensating practice.

Edge rulings:
- "We bought a tool but never deployed it" → Level 1. Shelfware is not performance.
- "The MSP probably does that" with no contract clause or report to show → Level 1, plus a third-party oversight finding (see [../../third-party-risk-assessment/SKILL.md](../../third-party-risk-assessment/SKILL.md)).

## Level 2 — Ad Hoc

**Semantic:** The activity happens, but inconsistently. Success depends on specific individuals. There is no approved documentation, or documentation exists but is ignored.

Anchors (any combination):
- Performed reactively (after incidents, before audits) rather than routinely.
- One person holds the knowledge; their departure would stop the activity.
- Practices differ across teams/sites with no rationalized reason.
- A policy exists but interviewees have not read it, or observed practice contradicts it.
- Evidence is anecdotal; artifacts exist for some instances but coverage is unknown.

Edge rulings:
- Strong practice, zero documentation → Level 2, never 3. Documentation is a hard gate for Level 3.
- Excellent policy, no evidence of execution → Level 2 ("paper program"). Flag explicitly: paper programs are the most common inflation error in self-assessments.
- Practice documented in a wiki page nobody approved → Level 2. Approval and ownership are part of "defined".

## Level 3 — Defined

**Semantic:** Documented, approved by an accountable owner, communicated to those who perform it, and consistently performed as written. This is the default target level for most organizations and the default gap threshold in this skill.

Anchors (all required):
- Current, approved document (policy/standard/procedure) with named owner and review date inside its stated cycle.
- Interviewees across teams describe the practice consistently and consistently with the document.
- Roles and responsibilities assigned (not necessarily full-time staff).
- Artifacts demonstrate routine execution (recurring tickets, reports, meeting minutes), not just one-off instances.
- Exceptions to the practice are recognized as exceptions (even if the exception process itself is immature).

Edge rulings:
- Documented and executed, but coverage is knowingly partial (e.g., patching process covers servers, not network devices) → Level 3 only if the exclusion is documented and accepted; otherwise Level 2 and a coverage gap.
- Automation is NOT required for Level 3. Manual-but-consistent qualifies.

## Level 4 — Managed

**Semantic:** The defined practice is measured with defined metrics; performance against thresholds is reviewed by management; deviations are detected and corrected through a feedback loop.

Anchors (all required):
- Metrics defined with thresholds/targets (e.g., critical patch SLA compliance %, phishing failure rate, mean time to detect) — see [../../grc-metrics-reporting/SKILL.md](../../grc-metrics-reporting/SKILL.md) for metric design.
- Metrics are reviewed on a cadence by someone with authority to act, and there is evidence of action taken on a missed threshold.
- Coverage of the practice is known quantitatively (not "most systems" but "94% of the 412 in-scope servers").
- Internal checks (self-testing, internal audit, control testing per [../../control-testing/SKILL.md](../../control-testing/SKILL.md)) verify the practice periodically.

Edge rulings:
- Dashboards exist but nobody can show a decision or correction driven by them → Level 3. Measurement without management is decoration.
- Metrics reviewed only when an auditor asks → Level 3.

## Level 5 — Optimized

**Semantic:** The practice is continuously improved. Metric trends and incident/exercise lessons feed changes to the practice itself; investment decisions cite the metrics; automation is applied where it reduces error or toil.

Anchors (most required):
- Documented improvement history: the practice measurably changed based on data (trend analysis, root-cause analysis, benchmarking).
- Leading indicators tracked, not only lagging ones.
- Automation of repetitive steps where sensible, with humans on exceptions.
- Practice performance influences budgeting or resourcing decisions with traceable rationale.
- The organization contributes lessons outward (peer sharing, ISAC participation) — supporting, not required.

Edge rulings:
- Level 5 should be rare. In a typical first assessment, expect zero to a few Level 5 domains. An assessment returning many Level 5 scores is more likely an anchoring failure than an elite program — re-check evidence.

## Cross-cutting scoring rules

1. **Weakest credible evidence governs.** Score what the evidence supports across the whole domain, not the best example within it.
2. **No half-levels.** When torn, take the lower level and record the reason; the delta becomes a near-term roadmap item.
3. **Confidence tag per score:** High = artifact-backed; Medium = corroborated interviews; Low = single source or documents only. Report the confidence distribution in the executive summary.
4. **Documentation gates Level 3; measurement gates Level 4; improvement evidence gates Level 5.** These are hard gates — one missing gate element caps the level regardless of other strengths.
5. **N/A requires written justification** traceable to the scope statement, and must be excluded from averages, not counted as any level.
6. **Do not average subdomain scores into a domain score.** Report the modal level with the range (e.g., "Level 2, with PR.AA at 3 and PR.IR at 1"). Averaging hides the weakest link, which is usually what an attacker finds. See aggregation pitfalls in [../../../context/risk-scoring.md](../../../context/risk-scoring.md).

## Relationship to framework-native tiers

- **NIST CSF 2.0 Tiers (Partial / Risk Informed / Repeatable / Adaptive)** characterize cybersecurity risk governance and management overall, not per-category maturity. Do not relabel this skill's per-domain levels as CSF Tiers; if the user wants Tiers, assess them separately at the whole-program level per [../../../context/frameworks/nist-csf-2.md](../../../context/frameworks/nist-csf-2.md).
- **PCI DSS** is binary per requirement (in place / not in place / N/A, with compensating controls or the customized approach as defined paths). Maturity levels are diagnostic overlay only.
- **ISO/IEC 27001** certification requires conformity, not a maturity number; use levels to show distance from a certifiable state (roughly Level 3 across clauses 4–10 plus applicable Annex A controls, with clause 9 monitoring/audit pushing toward Level 4 behaviors).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
