---
name: control-testing
description: >-
  Designs and executes tests of control design and operating effectiveness for
  internal audit, SOC 2/ISO readiness, SOX ITGC, or continuous assurance. Covers
  test method selection (inquiry/observation/inspection/reperformance), sample
  sizing by control frequency and automation, population completeness, workpaper
  documentation, and exception classification. Use when a user says "test this
  control", "operating effectiveness", "sample size", "TOD/TOE", or "workpaper".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Produce defensible conclusions about whether a control is well designed and operated effectively over a period, documented in a workpaper a reviewer or external auditor can re-perform. The skill enforces the discipline that separates real testing from box-checking: design before operation, evidence hierarchy, population-first sampling, and honest exception classification.

## When to use

- Internal audit or SOX ITGC testing cycles; management testing under s404.
- Readiness testing before an external audit (invoked from step 4 of [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md)).
- Validating a remediated control before closing a finding or exception.
- Periodic control assurance for a risk or compliance program.
- **Do NOT use** for:
  - Assessing whether the right controls *exist* against a framework — use [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md).
  - Preparing evidence for someone else's audit — use [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md).
  - Mapping one control to multiple frameworks — use [../control-mapping/SKILL.md](../control-mapping/SKILL.md).
  - Tracking failed controls after testing — hand off to [../exception-management/SKILL.md](../exception-management/SKILL.md).

## Inputs to gather

1. **Control description** — the documented control: what happens, who performs it, what triggers it, what artifact it produces. If no documented description exists, write one with the owner first; you cannot test an undefined control.
2. **Control attributes** — frequency (continuous, daily, weekly, monthly, quarterly, annual, ad hoc/per-occurrence), automation (fully automated / manual / IT-dependent manual), preventive vs. detective, and the risk it mitigates.
3. **Test period** — the window the conclusion will cover.
4. **Test purpose** — readiness (reduced rigor acceptable, say so in the workpaper), SOX/management testing, internal audit, or remediation validation (sample from post-remediation period only).
5. **Population source** — which system holds the records of the control operating, and who can extract it.
6. **Prior results** — last test's conclusion and exceptions; prior failures argue for larger samples or earlier testing.

## Procedure

1. **Understand the control.** Restate it as a testable assertion: *who* does *what*, *when/how often*, using *what input*, producing *what evidence*, with *what precision* (what size/type of error would it catch?). Classify it:
   - **Fully automated** — executes in software with no human judgment (e.g., pipeline blocks unapproved merges). Test the configuration plus one instance; rely on IT general controls (change management) for consistency through the period.
   - **Manual** — human performs and evidences it (e.g., quarterly access review).
   - **IT-dependent manual (ITDM)** — human judgment applied to system-produced data (e.g., manager reviews a system-generated exception report). Test *both* the human review *and* the accuracy/completeness of the system-generated report it depends on — a diligent review of a broken report is a broken control.

2. **Test design effectiveness first.** Before any sampling, answer: if this control operated exactly as described, would it actually mitigate the stated risk? Check precision (would it catch an error of the size that matters?), timeliness (does it fire soon enough?), the performer's competence and independence, and coverage (all in-scope systems/populations?). Decision point: **if design is ineffective, stop — conclude "design deficiency" and do not test operating effectiveness.** Operating a badly designed control consistently is not effectiveness. Walkthrough one instance end-to-end with the owner to confirm your understanding of the design.

3. **Choose the test method.** Use the evidence hierarchy — each level supersedes the ones below; combine inquiry with at least one stronger method, always:
   - **Reperformance** (strongest) — independently redo the control and compare results (re-run the access review yourself; recalculate the report).
   - **Inspection** — examine artifacts the control produced (signed reviews, tickets, configs, logs).
   - **Observation** — watch the control performed; evidences that moment only.
   - **Inquiry** (weakest) — ask the owner. Never sufficient alone for operating effectiveness.
   Default: inspection for most manual/ITDM controls, reperformance for high-risk or key controls, inspection of configuration plus one reperformed instance for automated controls.

4. **Determine the sample size** by frequency and automation. Standard baseline (industry-conventional for controls testing; adjust up for high risk or prior failures — see [references/sampling-guide.md](references/sampling-guide.md)):

   | Control frequency | Baseline sample size |
   |---|---|
   | Multiple times per day / per-occurrence, large population | 25 |
   | Daily | 25 |
   | Weekly | 5 |
   | Monthly | 2 |
   | Quarterly | 2 |
   | Annual | 1 |
   | Fully automated | 1 instance + configuration inspection (per configuration, per system) |
   | ITDM | Sample the manual review per its frequency **+** test the underlying report's logic once per configuration |

   Samples must be selected randomly or haphazardly-without-bias from the full population, spread across the period (include period start/end and any personnel-change windows). Never let the control owner choose the items.

5. **Pull the population with a completeness check.** Obtain the population directly from the source system (or observe the extraction), with query parameters, extraction date, and record count. Validate completeness before sampling: reconcile the count to an independent source (e.g., change tickets vs. deployment log; terminations vs. HRIS report), check period boundary records exist, and confirm no filters silently excluded records. Document the check in the workpaper. **A perfect test of an incomplete population concludes nothing.** Techniques in [references/sampling-guide.md](references/sampling-guide.md).

6. **Execute and document in a workpaper.** For each sampled item, test the defined attributes (e.g., for change approval: approval exists, approver ≠ developer, approval date ≤ deploy date, evidence of testing). Record per item: identifier, attributes tested, result per attribute, evidence reference. Use [../../templates/control-test-workpaper.md](../../templates/control-test-workpaper.md). The re-performance standard: an uninvolved reviewer must be able to reach the same conclusion from the workpaper and referenced evidence alone. Worked procedures for ~12 common controls are in [references/test-procedures-library.md](references/test-procedures-library.md).

7. **Classify exceptions.** For every failed attribute, decide the path:
   - **Deviation, isolated** — a one-off failure with identifiable non-systemic cause. You may not simply excuse it: expand the sample (typically add the same number again) and re-evaluate; a second failure of the same attribute means it is not isolated. See the expansion rules in [references/sampling-guide.md](references/sampling-guide.md).
   - **Control deficiency** — the control did not operate consistently (multiple failures, or failure with systemic cause). Assess severity by likelihood and magnitude of the risk left unmitigated, considering compensating controls.
   - **Significant deficiency / material weakness path** — for SOX/ICFR contexts, escalate severity assessment per [../../context/regulations/sox-itgc.md](../../context/regulations/sox-itgc.md); this determination belongs to management and auditors, so document facts (nature, cause, magnitude, duration, compensating controls) that enable it rather than asserting the label unilaterally.
   Route every deficiency into [../exception-management/SKILL.md](../exception-management/SKILL.md) with owner and remediation date.

8. **Conclude.** One of: **Design effective + operating effectively** / **Design effective, operating ineffectively** (with deficiency detail) / **Design deficiency** (operation not tested). State the conclusion, the period it covers, and any scope limitations (population caveats, reduced readiness-level sampling). Never conclude "effective with exceptions" — either the exceptions were resolved as isolated deviations after expansion, or the control has a deficiency.

## Output format

Deliverable: a completed workpaper per [../../templates/control-test-workpaper.md](../../templates/control-test-workpaper.md). Skeleton with worked example values:

```
WP ref: ITGC-CM-01 | Tester: <name> | Date tested: 2026-07-10 | Reviewer: <name>
Control: CM-01 — All production changes require pre-deployment approval by a
  non-author reviewer, evidenced in the change ticket. Frequency: per-occurrence.
  Type: manual (approval) over automated gate (pipeline).  Owner: Eng Lead.
Period: 2025-07-01 – 2026-06-30 | Purpose: SOC 2 readiness
Design assessment: Effective — walkthrough of CHG-4102 on 2026-07-08; gate blocks
  merge without approval field; approver population restricted to leads group.
Population: 412 production changes; source: deploy log query (attached, run
  2026-07-09); completeness: reconciled 412 deploys to 412 pipeline runs; period
  boundary changes verified (first 2025-07-02, last 2026-06-29).
Method: Inspection. Sample: 25, random, spread across 12 months.
Attributes: A1 approval exists; A2 approver ≠ author; A3 approval ts ≤ deploy ts.
Results: 25/25 pass A1, A2. A3: 1 exception — CHG-4677 approved 14 min post-deploy
  (emergency change, retro-approval per policy §4.2, emergency path evidenced).
Exception evaluation: A3 item followed the documented emergency-change path —
  not a deviation from design. No expansion required. Zero unexplained failures.
Conclusion: Design effective and operating effectively for the period.
```

## Quality checklist

- [ ] Control restated as a testable assertion with frequency, performer, precision, and expected evidence; automation class (automated/manual/ITDM) recorded.
- [ ] Design effectiveness concluded before operating tests; a design deficiency stopped further testing.
- [ ] Test method stronger than inquiry alone; method choice justified in the workpaper.
- [ ] Sample size meets or exceeds the frequency baseline; deviations from baseline justified in writing.
- [ ] For ITDM controls, the underlying report's completeness/accuracy was tested, not just the human review.
- [ ] Population obtained system-generated with query, date, and count; completeness check documented; sample selected without owner involvement and spread across the period.
- [ ] Every sampled item has per-attribute results with evidence references; a reviewer could re-perform from the workpaper alone.
- [ ] Every exception classified (isolated deviation with expanded sample, or deficiency) — none waved through; deficiencies logged to exception management with owners.
- [ ] Conclusion states one of the three permitted outcomes, the period covered, and scope limitations.

## References

- [references/sampling-guide.md](references/sampling-guide.md) — sample-size rationale, population completeness techniques, exception handling and sample expansion.
- [references/test-procedures-library.md](references/test-procedures-library.md) — worked test procedures for 12 common controls.
- [../../templates/control-test-workpaper.md](../../templates/control-test-workpaper.md) — workpaper template.
- [../../context/regulations/sox-itgc.md](../../context/regulations/sox-itgc.md) — SOX s302/404, ITGC, deficiency severity in ICFR.
- [../../context/frameworks/coso-internal-control-erm.md](../../context/frameworks/coso-internal-control-erm.md) — the internal-control components and principles a deficiency is evaluated against.
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) — Type II operating-effectiveness context.
- [../../context/frameworks/soc1-isae3402-soc-reports.md](../../context/frameworks/soc1-isae3402-soc-reports.md) — SOC 1 / ISAE 3402 Type 2 testing of ICFR-relevant controls, including the description of tests and results.
- [../../context/frameworks/iia-global-internal-audit-standards.md](../../context/frameworks/iia-global-internal-audit-standards.md) — the standards the internal audit function performing the testing must itself conform to.
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — ISMS internal audit and the Annex A controls under test.
- Control sets that publish their own assessment procedures or scoring rubric: [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md), [../../context/frameworks/nist-800-171-cmmc.md](../../context/frameworks/nist-800-171-cmmc.md), [../../context/frameworks/nist-rmf-800-37-800-30.md](../../context/frameworks/nist-rmf-800-37-800-30.md), [../../context/frameworks/fedramp.md](../../context/frameworks/fedramp.md), [../../context/frameworks/hitrust-csf.md](../../context/frameworks/hitrust-csf.md), [../../context/frameworks/cobit-2019.md](../../context/frameworks/cobit-2019.md)
- Scheme-specific testing and independent-assessment regimes: [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md), [../../context/frameworks/pci-other-standards.md](../../context/frameworks/pci-other-standards.md), [../../context/frameworks/csa-ccm-star.md](../../context/frameworks/csa-ccm-star.md), [../../context/frameworks/swift-customer-security-programme.md](../../context/frameworks/swift-customer-security-programme.md), [../../context/frameworks/tisax-vda-isa.md](../../context/frameworks/tisax-vda-isa.md), [../../context/frameworks/germany-bsi-it-grundschutz-c5.md](../../context/frameworks/germany-bsi-it-grundschutz-c5.md), [../../context/frameworks/uk-cyber-essentials-ncsc-caf.md](../../context/frameworks/uk-cyber-essentials-ncsc-caf.md), [../../context/frameworks/iec-62443-ot-security.md](../../context/frameworks/iec-62443-ot-security.md)
- Technical control sets that shape test design and evidence choice: [../../context/frameworks/nist-800-63-digital-identity.md](../../context/frameworks/nist-800-63-digital-identity.md), [../../context/frameworks/nist-800-207-zero-trust.md](../../context/frameworks/nist-800-207-zero-trust.md), [../../context/frameworks/nist-ssdf-800-218.md](../../context/frameworks/nist-ssdf-800-218.md), [../../context/frameworks/owasp-application-security.md](../../context/frameworks/owasp-application-security.md), [../../context/frameworks/nist-800-61-incident-handling.md](../../context/frameworks/nist-800-61-incident-handling.md), [../../context/frameworks/mitre-attack-threat-informed-defense.md](../../context/frameworks/mitre-attack-threat-informed-defense.md), [../../context/frameworks/cisa-cpg-secure-by-design.md](../../context/frameworks/cisa-cpg-secure-by-design.md)
- [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md) — readiness testing before external audits.
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — tracking deficiencies to remediation.
- [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md) — reporting test results as program metrics.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
