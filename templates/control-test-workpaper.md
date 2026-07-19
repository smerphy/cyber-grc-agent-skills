# Control Test Workpaper

**How to use:** One workpaper per control test. Complete every section — a workpaper that skips population completeness or design assessment does not support a conclusion. The worked example below (in the right-hand column of each table and the example blocks) shows a completed quarterly access review test; replace with your own content. Method, sampling guidance, and attribute design: [../skills/control-testing/SKILL.md](../skills/control-testing/SKILL.md). Evidence sourcing: [audit-evidence-request-list.md](audit-evidence-request-list.md).

## 1. Header

| Field | Entry | Worked example |
|---|---|---|
| Workpaper ref | | WP-AC-03 |
| Control ID and description | | AC-02: User access to in-scope systems is reviewed by the system owner at least quarterly; access not reaffirmed within 14 days of review issuance is revoked. |
| Control type / frequency | [Preventive/detective; automated/manual/IT-dependent manual] | Detective, manual with system-generated input; quarterly |
| Control owner | | ERP system owner (Finance Systems Manager) |
| Test period | | 2025-07-01 to 2026-06-30 |
| Tester / date | | J. Rivera, GRC Analyst / 2026-08-14 |
| Framework mapping | | ISO 27001 A.5.18; SOC 2 CC6.2-CC6.3; SOX ITGC (access to ICFR-relevant system — see [../context/regulations/sox-itgc.md](../context/regulations/sox-itgc.md)) |

## 2. Test objective

*One sentence: what assertion this test supports.*

> **Example:** Determine whether quarterly ERP access reviews operated throughout the period: reviews performed on schedule by the accountable owner, all active accounts covered, and non-reaffirmed access revoked within 14 days.

## 3. Design assessment

*Before testing operation, assess design: if the control as designed cannot achieve the objective, operating-effectiveness testing is pointless. Walk through one instance end-to-end and record it.*

| Question | Assessment |
|---|---|
| Does the control, as designed, address the risk? | [E.g., Yes — quarterly certification with forced revocation addresses accumulation of inappropriate access; input listing is system-generated from the ERP, not self-reported] |
| Walkthrough performed | [Instance walked through, with whom, date; note the input source, the performer's judgment steps, and the output evidence] |
| Design conclusion | [Effective / Deficient — if deficient, stop and report; do not test operation of a badly designed control] |

## 4. Population and completeness

*Define the population of control occurrences, state where it came from, and evidence its completeness. An untested population makes every subsequent step unreliable.*

> **Example:** Population = 4 quarterly reviews due in the period (Q3'25, Q4'25, Q1'26, Q2'26) for the ERP. Completeness: review schedule per policy cross-checked against the review tool's campaign list; account listings used in each review were system-generated exports from ERP admin, compared for record counts against an independently run current-user query (variance 0). All 4 occurrences tested — no sampling at the review level. Within Q2'26, revocation actions sampled.

## 5. Sample selection

| Field | Entry | Worked example |
|---|---|---|
| Sampling approach | [Full population / random / risk-based; justify] | All 4 reviews tested. Within reviews: all 23 non-reaffirmed access items across the period tested for timely revocation (full population, small N). |
| Sample size and selection method | | 4 reviews + 23 revocation items; N/A random selection (full population) |

## 6. Attributes tested

*Each attribute is a binary pass/fail question applied to every sampled item.*

| # | Attribute | Pass criterion |
|---|---|---|
| A | Review performed in the quarter it was due | Campaign completion date within the quarter |
| B | Performed by the accountable system owner (or documented delegate) | Sign-off identity matches owner/delegate register |
| C | Review covered the complete account population | Reviewed listing reconciles to system-generated account export at campaign start |
| D | Non-reaffirmed access revoked within 14 days | Revocation ticket/IdM log date ≤ certification date + 14 days |

## 7. Results

| Item | Attribute A | Attribute B | Attribute C | Attribute D | Notes |
|---|---|---|---|---|---|
| Q3 2025 review | Pass | Pass | Pass | Pass (6/6 items) | |
| Q4 2025 review | **Fail** — completed 2026-01-19 | Pass | Pass | Pass (4/4 items) | 19 days late; year-end freeze cited |
| Q1 2026 review | Pass | Pass | Pass | **Fail** — 1 of 8 items revoked day 22 | Contractor account, ticket sat unassigned |
| Q2 2026 review | Pass | Pass | Pass | Pass (5/5 items) | |

**Exceptions: 2** (1 late review; 1 late revocation of 23 revocation items).

## 8. Exceptions and evaluation

*For each exception: root cause, whether it is systematic or isolated, actual exposure during the gap, and whether it changes the conclusion. An exception is not automatically a deficiency — but explaining it away without evidence is worse than reporting it.*

> **Example:** (1) Q4'25 review 19 days late — root cause: no calendar trigger during year-end freeze; isolated to one quarter; no access changes occurred in the gap window per ERP admin log. Management action: automated campaign scheduling enabled 2026-02. (2) One revocation at 22 days vs. 14-day requirement — contractor account, no login activity after certification date (verified in auth logs), so no actual exposure. Isolated (1 of 23). Combined evaluation: control operated with minor deviations; deviations were detected and corrected by management; no evidence of unauthorized access resulting.

## 9. Conclusion

| Field | Entry | Worked example |
|---|---|---|
| Conclusion | [Operating effectively / Operating effectively with noted deviations / Deficiency — with severity] | Operating effectively with noted deviations. Deviations reported as a low-severity finding with management actions already implemented; re-test of automated scheduling at next cycle. |
| Findings raised | [Refs into findings log] | F-2026-11 |
| Impact on reliance | [Can the assessed framework requirement be asserted? Any knock-on to other tests?] | No change to SOC 2 CC6.3 reliance; SOX evaluation: deficiency assessed as not significant (isolated, compensated, no misstatement exposure) |

## 10. Review and sign-off

| Role | Name | Date | Notes |
|---|---|---|---|
| Preparer | | | |
| Reviewer (independent of preparer) | | | [Reviewer checks: population completeness evidenced; attributes match the control's requirement; exceptions evaluated with evidence, not assertion; conclusion follows from results] |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
