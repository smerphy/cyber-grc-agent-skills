---
name: control-mapping
description: >-
  Maps controls between security frameworks (ISO 27001, NIST CSF 2.0, CIS v8,
  SOC 2, NIST 800-53, PCI DSS) or from an internal control set to a framework,
  producing a many-to-many mapping table with full/partial/none coverage ratings,
  rationales, and unmapped-residue lists in both directions. Use when asked to
  "map controls", "crosswalk frameworks", "translate our controls to X", "show
  coverage of X by Y", or to validate an existing crosswalk.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

# Control Mapping

## Purpose

Produce a defensible mapping between two control sets — framework-to-framework or internal-to-framework — that records the strength of each relationship (full/partial/none), the rationale, and everything left unmapped on both sides. The method is many-to-many and partial-coverage aware by design, because real control sets never align 1:1 and pretending they do creates silent compliance gaps.

## When to use

- The organization holds one framework's controls and needs to demonstrate coverage of another ("we're ISO 27001 certified; how much of SOC 2 CC do we already meet?").
- An internal control library needs to be mapped to one or more external frameworks for a unified controls approach ("test once, attest many").
- An inherited or vendor-provided crosswalk needs validation before being relied on.
- A framework version change requires remapping (e.g., ISO/IEC 27001:2013 → 2022, CSF 1.1 → 2.0).

**Do NOT use this skill when:**
- The question is "how mature are we against framework X?" — that is a gap assessment: [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md). Mapping tells you where requirements correspond; it says nothing about whether controls are implemented or effective.
- The question is whether a control operates effectively — use [../control-testing/SKILL.md](../control-testing/SKILL.md).
- The user needs only a rough domain-level orientation — point them at [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) instead of building a control-level mapping.

## Inputs to gather

1. **Source and target control sets, with exact versions.** Version drift is the top cause of bad mappings. "CIS" without v8/v8.1, or "ISO 27001" without 2013/2022, is not an answer.
2. **Direction and purpose.** Coverage claim ("does source satisfy target?"), rationalization (build a common control set), or audit-evidence reuse? Purpose sets the strictness bar: coverage claims need conservative ratings.
3. **Granularity available.** Full control text for both sides, or only titles/IDs? Titles alone produce unreliable mappings — say so and get the text. For internal controls, get the actual control statements as written, not the policy they summarize.
4. **Scoping decisions already made.** Statement of Applicability exclusions, SOC 2 categories in scope, PCI SAQ type, 800-53 baseline. Mapping out-of-scope controls wastes effort and misleads readers.
5. **Existing crosswalks in hand** (vendor matrices, OLIR-style mappings, the previous year's spreadsheet). Treat them as candidate input to validate, never as ground truth — see stale-crosswalk warnings below.
6. **Who consumes the output** — auditors, a GRC tool import, engineers? This drives output format (table columns, machine-readable export).

## Procedure

Full method with worked example: [references/mapping-method.md](references/mapping-method.md). Failure modes: [references/common-pitfalls.md](references/common-pitfalls.md).

1. **Fix the frame.** Record source set, target set, versions, direction, purpose, and scoping exclusions in a mapping header block. Every later judgment is relative to this frame; a mapping without its frame is unusable.

2. **Normalize control statements.** For each control on both sides, restate the requirement as one or more atomic assertions in a common grammar: *actor/scope — action — object — condition/qualifier*. Strip framework boilerplate ("the organization shall…"), keep every qualifier (frequency, population, "documented", "approved", "tested"). Qualifiers are where partial coverage hides.

3. **Decompose compound controls.** Any control whose statement contains multiple obligations (look for "and", lists, semicolons, embedded frequencies) becomes numbered elements: `A.8.16-e1`, `A.8.16-e2`. Map at element level; roll up to control level afterwards. Never rate a compound control "full" because its most visible element matched.

4. **Generate candidate matches.** For each source element, search the target set by: shared domain (use [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) to narrow the field), keyword/synonym match on normalized assertions, and any existing crosswalk suggestions. Cast wide — false candidates are cheap to reject; missed candidates become silent gaps.

5. **Rate each candidate pair.** Compare atomic assertions and assign:
   - **Full** — target element's obligations are entirely satisfied by the source element(s), including qualifiers (scope, frequency, documentation/approval demands). Rare between real frameworks.
   - **Partial** — meaningful overlap with a stateable delta. The rationale MUST name the delta ("source requires logging but not the review cadence target demands").
   - **None** — reject the candidate; superficial keyword overlap only.
   **Decision points:** intent vs mechanism mismatches (same tool, different objective) rate at most Partial. When multiple source elements together satisfy one target element, record a many-to-one Full with all contributors listed. When rating is arguable, take the lower rating for coverage-claim purposes and note the argument.

6. **Sweep for unmapped residue — both directions.** List every target element with no Full coverage (the "coverage gap" list — this is what the user usually actually needs) AND every source element that mapped to nothing (candidate duplicates, over-engineering, or unique obligations worth keeping). A mapping deliverable without both residue lists is incomplete.

7. **Roll up and quality-sample.** Aggregate element ratings to control level using the weakest-link rule: a control is Full only if all its in-scope elements are Full. Compute coverage statistics (% of target controls Full / Partial / uncovered). Then re-derive 10% of mappings (minimum 10) blind — without looking at the recorded rating — and compare. Mismatch above ~1 in 10 sampled means the rubric was applied inconsistently: recalibrate and re-review.

8. **Deliver with maintenance triggers.** State in the deliverable which events invalidate the mapping: version change of either set, internal control wording changes, scope changes. A mapping is a snapshot, not an asset that survives framework revisions — see stale-reuse pitfalls in [references/common-pitfalls.md](references/common-pitfalls.md).

## Output format

**Mapping header** — source/target + versions, direction, purpose, scope exclusions, date, method note ("element-level, weakest-link rollup").

**Mapping table** — one row per source-element → target-element pair rated Full or Partial:

| Source ref | Source element | Target ref | Target element | Coverage | Rationale / delta |
|---|---|---|---|---|---|
| ISO A.8.16-e1 | Monitor networks, systems, applications for anomalous behaviour | CSF 2.0 DE.CM-01 | Networks and network services are monitored to find potentially adverse events | Partial | Source covers monitoring of networks; DE.CM-01's "network services" breadth met, but source element alone does not evidence the analysis expectation carried by DE.AE — pair with A.8.16-e2 |
| ISO A.8.16-e2 | Take action to evaluate potential information security incidents | CSF 2.0 DE.AE-02 | Potentially adverse events are analyzed to better understand associated activities | Full | Evaluation-of-anomalies obligation aligns in intent and object; no qualifier delta identified |
| ISO A.8.16-e1 | Monitor networks, systems, applications for anomalous behaviour | CIS 13.1 | Centralize security event alerting | Partial | Monitoring intent shared; CIS 13.1 additionally requires centralization, which A.8.16 does not mandate |

**Residue lists** — (a) target elements with no Full coverage, each with severity note if the purpose is a coverage claim; (b) source elements mapping to nothing, each tagged `unique-obligation | duplicate | over-spec`.

**Coverage summary** — counts and percentages at control level, weakest-link rolled: e.g., "Of 106 CSF 2.0 subcategories in scope: 31 Full, 52 Partial, 23 uncovered."

**Maintenance triggers** — bullet list of invalidating events with the version identifiers this mapping is pinned to.

## Quality checklist

- [ ] Header states both versions exactly; no bare framework names.
- [ ] Every compound control decomposed before rating; no control with "and"-joined obligations rated as a single unit.
- [ ] Every Partial rating's rationale names the specific delta — "partially overlaps" alone fails.
- [ ] No Full rating between differently-scoped requirements (e.g., PCI's CDE-scoped requirement claimed as Full coverage of an enterprise-wide target).
- [ ] Both residue lists present, even if empty ("none identified" stated explicitly).
- [ ] Rollup uses weakest-link, not majority or average.
- [ ] Blind re-derivation sample performed and mismatch rate recorded.
- [ ] Existing/vendor crosswalks used only as candidate generators; every adopted suggestion independently rated.
- [ ] Deliverable states maintenance triggers and mapping date.
- [ ] The mapping makes no implementation claims — wording avoids "we meet", using "requirement corresponds" language, unless the user explicitly layered implementation status on top.

## References

- [references/mapping-method.md](references/mapping-method.md) — decomposition technique, coverage rubric, worked example (ISO A.8.16 → CSF 2.0 and CIS v8)
- [references/common-pitfalls.md](references/common-pitfalls.md) — naive 1:1 mapping, stale crosswalk reuse, keyword traps, scope mismatches
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) — domain-level orientation crosswalk
- Most common source and target sets: [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md), [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md), [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md), [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md), [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md), [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md)
- Published mappings to validate as candidate input, never to adopt wholesale: [../../context/frameworks/nist-csf-profiles-and-companion-resources.md](../../context/frameworks/nist-csf-profiles-and-companion-resources.md) (CSF Informative References and the OLIR catalog), [../../context/frameworks/csa-ccm-star.md](../../context/frameworks/csa-ccm-star.md) (CCM mappings and CAIQ), [../../context/frameworks/hitrust-csf.md](../../context/frameworks/hitrust-csf.md) (authoritative-source harmonization)
- ISO management-system standards mapped onto or alongside 27001: [../../context/frameworks/iso-27017-27018-cloud.md](../../context/frameworks/iso-27017-27018-cloud.md), [../../context/frameworks/iso-27701-privacy-management.md](../../context/frameworks/iso-27701-privacy-management.md), [../../context/frameworks/iso-22301-business-continuity.md](../../context/frameworks/iso-22301-business-continuity.md), [../../context/frameworks/iso-42001-ai-management.md](../../context/frameworks/iso-42001-ai-management.md), [../../context/frameworks/iso-31000-27005-risk-management.md](../../context/frameworks/iso-31000-27005-risk-management.md)
- Governance and internal-control frameworks: [../../context/frameworks/cobit-2019.md](../../context/frameworks/cobit-2019.md), [../../context/frameworks/coso-internal-control-erm.md](../../context/frameworks/coso-internal-control-erm.md), [../../context/frameworks/iia-global-internal-audit-standards.md](../../context/frameworks/iia-global-internal-audit-standards.md)
- US federal, defense and technical sets: [../../context/frameworks/nist-800-171-cmmc.md](../../context/frameworks/nist-800-171-cmmc.md), [../../context/frameworks/nist-rmf-800-37-800-30.md](../../context/frameworks/nist-rmf-800-37-800-30.md), [../../context/frameworks/fedramp.md](../../context/frameworks/fedramp.md), [../../context/frameworks/nist-ssdf-800-218.md](../../context/frameworks/nist-ssdf-800-218.md), [../../context/frameworks/nist-800-161-cscrm.md](../../context/frameworks/nist-800-161-cscrm.md), [../../context/frameworks/nist-800-207-zero-trust.md](../../context/frameworks/nist-800-207-zero-trust.md), [../../context/frameworks/nist-800-63-digital-identity.md](../../context/frameworks/nist-800-63-digital-identity.md), [../../context/frameworks/nist-800-61-incident-handling.md](../../context/frameworks/nist-800-61-incident-handling.md)
- Sector and scheme-specific sets: [../../context/frameworks/iec-62443-ot-security.md](../../context/frameworks/iec-62443-ot-security.md), [../../context/frameworks/swift-customer-security-programme.md](../../context/frameworks/swift-customer-security-programme.md), [../../context/frameworks/tisax-vda-isa.md](../../context/frameworks/tisax-vda-isa.md), [../../context/frameworks/pci-other-standards.md](../../context/frameworks/pci-other-standards.md), [../../context/frameworks/soc1-isae3402-soc-reports.md](../../context/frameworks/soc1-isae3402-soc-reports.md), [../../context/frameworks/ffiec-it-examination-handbook.md](../../context/frameworks/ffiec-it-examination-handbook.md), [../../context/frameworks/owasp-application-security.md](../../context/frameworks/owasp-application-security.md), [../../context/frameworks/mitre-attack-threat-informed-defense.md](../../context/frameworks/mitre-attack-threat-informed-defense.md), [../../context/frameworks/cisa-cpg-secure-by-design.md](../../context/frameworks/cisa-cpg-secure-by-design.md)
- National baselines: [../../context/frameworks/australia-essential-eight-ism.md](../../context/frameworks/australia-essential-eight-ism.md), [../../context/frameworks/uk-cyber-essentials-ncsc-caf.md](../../context/frameworks/uk-cyber-essentials-ncsc-caf.md), [../../context/frameworks/germany-bsi-it-grundschutz-c5.md](../../context/frameworks/germany-bsi-it-grundschutz-c5.md)
- Related skills: [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md), [../control-testing/SKILL.md](../control-testing/SKILL.md), [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md), [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md), [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
