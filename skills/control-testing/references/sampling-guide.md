# Sampling Guide for Control Testing

Rationale behind the standard sample sizes, techniques for proving population completeness, and the rules for handling exceptions and expanded samples.

## Why these sample sizes

The conventional attribute-sampling baseline used across SOX ITGC, SOC 2, and internal audit practice:

| Control frequency | Approx. population/year | Baseline sample | Rationale |
|---|---|---|---|
| Per-occurrence / many per day | 250+ | 25 | Attribute-sampling convention: 25 with zero deviations supports roughly 90% confidence that the deviation rate is below ~10%. Beyond 25, marginal assurance per item drops sharply for a homogeneous manual control. |
| Daily | ~250 | 25 | Same statistical basis; population is large enough that 25 is the conventional cap. |
| Weekly | ~52 | 5 | ~10% of population; enough to span the period and different performers. |
| Monthly | 12 | 2 | Small populations are tested judgmental-not-statistical; 2 spread across the period detects sustained non-operation. |
| Quarterly | 4 | 2 | Half the population; covers different quarters/performers. |
| Annual | 1 | 1 | The population is 1. Test it thoroughly rather than sampling. |
| Fully automated | n/a | 1 + config | A deterministic control either works or doesn't; consistency comes from ITGC over change management, which must itself be tested. |
| ITDM | per review frequency | review sample + 1 report-logic test per config | Two failure modes, two tests: the human review (sample by frequency) and the system report feeding it (test logic/parameters once per configuration, re-test on change). |

These are **baselines for zero-expected-deviation testing at moderate risk**. They are conventions widely used in practice, not a statute; document the table you use and apply it consistently.

### When to increase the sample

Increase (typically 1.5–2x, or move to statistical sampling) when any of:

- The control is a **key control** over a high-impact risk (financial reporting materiality, safety, regulatory exposure).
- **Prior-period failures** or recent remediation — you are testing whether the fix stuck.
- **Multiple performers or locations** — sample must include each performer/location, which can push above baseline.
- **Population heterogeneity** — e.g., "changes" spanning standard, emergency, and vendor-applied changes: stratify and sample each stratum (emergency changes almost always deserve their own stratum; take all of them if fewer than 5).
- **Reliance by others** — external auditors intending to rely on management testing often expect the higher end.

### When a reduced sample is acceptable

- **Readiness/dry-run testing** — smaller judgmental samples are fine *if the workpaper says so* and the conclusion is labeled readiness-level, not assurance.
- **Interim + roll-forward** — test at interim with the baseline, then a small roll-forward sample (e.g., 5 for a daily control) covering interim-to-period-end. Standard SOX practice; document both windows.

### Automated controls: what "1 + config" really means

1. Inspect the configuration that implements the control (rule, policy object, pipeline gate) — capture value, system, timestamp.
2. Reperform or observe **one instance**, ideally including a negative test (attempt the action the control should block, in a safe environment).
3. Verify the configuration was **unchanged during the period**: change history for the setting, or reliance on tested change management ITGC.
4. Repeat per distinct configuration — the "same" control on three tenants with three configs is three tests.

If change management ITGC failed, the benchmark collapses: the automated control must be re-evaluated because you can no longer assume the config held all period.

## Population completeness

Sampling from an incomplete population is the most common fatal flaw in control testing. The test is only as good as the population.

### Techniques, strongest first

1. **Reconciliation to an independent source.** Count records in the population against a system that captures the same events independently:
   - Changes: deployment/release log vs. change tickets.
   - Terminations: HRIS termination report vs. access-removal tickets.
   - Incidents: alerting-tool export vs. incident tickets.
   - New hires: HRIS vs. account-creation logs.
   Investigate every reconciling difference — differences *are* often the findings (the unticketed change, the termination with no removal ticket).
2. **Boundary testing.** Confirm records exist at both edges of the period (first and last expected occurrence). A population starting six weeks into the period suggests a filtering error — or the control not operating.
3. **Query inspection.** Read the extraction query/filter yourself. Common silent excluders: status filters (`status=closed` drops open items), date field choice (created vs. closed date shifts records across the boundary), environment filters, record-type filters.
4. **Sequence/gap checks.** For serially numbered records (tickets, change IDs), check for gaps in the sequence and explain them.
5. **Expected-count reasonableness.** Sanity-check volume: 12 monthly reviews for 12 months; ~250 daily records for a year of weekdays. A quarterly control with 3 records for a 4-quarter period is a missing occurrence, not a small population.
6. **Observed extraction.** Watch (or perform) the extraction live from the source system. Eliminates curation risk entirely; use for high-risk tests and whenever the population arrives as a suspiciously tidy spreadsheet.

Document which technique was used and its result in the workpaper. "Population provided by control owner" with no check is a scope limitation and must be stated as one in the conclusion.

### Selecting from the population

- **Random** (random number generator against row numbers) — default; document seed/method.
- **Haphazard** — acceptable for judgmental testing if genuinely unbiased: no picking "clean-looking" items, no clustering in one month.
- **Stratified** — required for heterogeneous populations (see above); sample each stratum, conclude per stratum.
- **Never**: items chosen by the control owner; only the most recent items; excluding "known messy" periods. Include period boundaries and any window where the performer changed (leaver/joiner in the owning role) — that is where controls break.

## Handling exceptions

### First: is it actually an exception?

Before classifying, confirm the failure is real:

- **Misunderstood control** — the item followed a documented alternate path (emergency change procedure, delegated approver matrix). Verify the alternate path is documented, itself controlled, and was followed — then it is a pass under that path, and note it.
- **Evidence problem, not control problem** — the approval happened but was recorded elsewhere. Give the owner a bounded chance (e.g., 3 business days) to produce the evidence; if it exists and predates the action, it passes. If evidence "appears" with timestamps after your request, treat with skepticism and test the artifact's metadata.
- **Population error** — the item shouldn't have been in scope (test record, out-of-scope system). Remove it, *replace it with another sampled item*, and revisit the completeness check — population errors are themselves informative.

### Real exception: the expansion rule

For a confirmed deviation in a zero-expected-deviation plan:

1. **Root-cause the item.** Who, when, why. An exception without a cause analysis cannot be called isolated.
2. **Assess isolation honestly.** Grounds for "potentially isolated": unique cause unlikely to recur (a specific outage, a one-day process gap during a documented transition), no pattern with other items. NOT grounds: "the person was busy", "it was year-end" — those are systemic pressures, and they recur.
3. **Expand the sample** if potentially isolated: select an additional sample of the same size as the original (e.g., 25 → +25; monthly 2 → +2, which for small populations may mean testing the remainder) from the same population, excluding already-tested items.
4. **Evaluate the expanded results:**
   - Zero further deviations of that attribute → conclude isolated deviation; control operating effectively; document the deviation, cause, and expansion in the workpaper.
   - Any further deviation of the same attribute → **stop expanding. It is a deficiency.** Do not keep sampling in search of a clean run — sequential expansion hunting for a passing sample is testing malpractice.
5. **Small populations** (monthly/quarterly/annual): one failure is a large fraction of the population; expansion often means testing 100% of remaining items, and even one confirmed unexcused failure in an annual or quarterly control generally cannot be "isolated" — the control failed for that period. Classify as a deficiency for the affected period.

### Classifying the deficiency

Severity is a function of **likelihood** (could the failure recur/persist?) and **magnitude** (what's the worst outcome the unmitigated risk permits?), moderated by **compensating controls** that were themselves tested:

| Question | Pushes severity up | Pushes severity down |
|---|---|---|
| How long did the control not operate? | Full period | Narrow, bounded window |
| Was the failure exploited/did errors occur? | Actual errors found | None found in look-back |
| Compensating control? | None, or untested | Tested, effective, covers the risk |
| Systemic cause? | Process/design gap | Truly one-off event |

In SOX/ICFR contexts the labels are deficiency → significant deficiency → material weakness; the escalation criteria and who makes the call are covered in [../../../context/regulations/sox-itgc.md](../../../context/regulations/sox-itgc.md). In SOC 2 contexts, uncorrected operating failures surface as exceptions in the auditor's report and can qualify the opinion if pervasive. In all contexts: the tester's job is to document nature, cause, duration, magnitude, and compensating controls — precisely enough that the severity call is forced by the facts.

### Documentation minimums per exception

- Item identifier and failed attribute(s).
- Root cause, with the owner's explanation quoted or summarized (labeled as inquiry).
- Isolation assessment and expansion results (or why expansion was inapplicable).
- Look-back performed for actual impact, and result.
- Classification, and the exception-management record it was routed to.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
