# Mapping Method: Decomposition, Rating Rubric, Worked Example

Detailed method behind the control-mapping skill. Three parts: (1) normalization and decomposition technique, (2) the coverage rating rubric with rulings, (3) a worked example mapping ISO/IEC 27001:2022 Annex A control A.8.16 to NIST CSF 2.0 subcategories and CIS Controls v8 Safeguards.

---

## 1. Normalization and decomposition

### Normalization grammar

Restate every control statement as one or more atomic assertions of the form:

```
[scope/population] — [action verb] — [object] — [qualifiers]
```

Rules:

- One obligation per assertion. If a sentence forces two verbs or two objects, split it.
- Preserve every qualifier: frequency ("at least quarterly"), population ("all in-scope system components"), state demands ("documented", "approved", "communicated"), and outcome demands ("tested", "reviewed", "retained for N"). Qualifiers decide Full vs Partial more often than the main verb does.
- Strip only true boilerplate: "the organization shall", "the entity", introductory purpose prose. Do not strip words you merely find redundant — "and take appropriate action" is an obligation, not filler.
- Where the framework publishes control text plus implementation guidance (ISO 27002, CIS safeguard descriptions, 800-53 control + enhancements), normalize the *requirement* text. Guidance informs interpretation but is not itself the obligation — except 800-53 control enhancements, which are discrete selectable requirements and must be treated as separate elements when in baseline.

### Decomposition triggers

Split a control into numbered elements (`<ref>-e1`, `-e2`, …) when the statement contains any of:

- Coordinating conjunctions joining verbs or objects ("monitored **and** reviewed"; "networks, systems **and** applications" split only if the target set treats those objects under different controls).
- Enumerated lists or semicolons.
- Embedded lifecycle stages (establish / operate / review / update — these often map to different targets: policy-type targets vs operational targets).
- Mixed control natures in one sentence: preventive + detective, or technical + governance ("implement MFA and review its configuration annually").

Stop decomposing when further splitting produces assertions no target framework would ever distinguish. Two to five elements per compound control is typical; more than eight suggests over-splitting.

### Rollup rule

A control-level rating derives from its elements by **weakest link**:

- All in-scope elements Full → control Full.
- Any element Partial (none None) → control Partial.
- Any in-scope element None/uncovered → control Partial at best, and the uncovered element must appear in the residue list; if the uncovered element is the control's core obligation, rate the control uncovered.

Never average, never majority-vote.

---

## 2. Coverage rating rubric

Rate each source-element → target-element pair:

| Rating | Test (all conditions must hold) |
|---|---|
| **Full** | Source obligation(s) entail the target obligation: same or broader scope/population; same or stricter qualifiers; intent aligned (the *why* matches, not just the mechanism) |
| **Partial** | Genuine overlap in obligation, but at least one stateable delta in scope, qualifier, intent, or mechanism. The delta must be written into the rationale |
| **None** | Overlap is superficial (shared keywords, shared tool category) with no shared obligation |

Standard rulings:

1. **Scope narrower on source side → Partial at best.** A PCI requirement scoped to the cardholder data environment cannot fully cover an enterprise-wide ISO or CSF obligation, no matter how well-worded. The reverse (enterprise-wide source covering CDE-scoped target) can be Full if qualifiers hold.
2. **Missing frequency/cadence → Partial.** "Review access rights" does not fully cover "review access rights at least quarterly".
3. **Missing documentation/approval demand → Partial.** Doing the activity does not entail documenting it; many ISO and SOC 2 criteria carry explicit documentation expectations.
4. **Same mechanism, different intent → Partial at most.** Log collection for troubleshooting is not log collection for security detection; encryption for integrity is not encryption for confidentiality. Check the control's stated objective, not its tooling.
5. **Many-to-one Full is legitimate.** Several source elements may jointly entail one target element; record all contributors on the row and rate the combination. One-to-many likewise: a broad source control may Fully cover several narrow targets.
6. **Governance vs operation.** A policy-type source control ("a policy on X shall be defined") never fully covers an operational target ("X is performed") and vice versa. This is the single most common false-Full in vendor crosswalks.
7. **Tie goes to the lower rating** whenever the mapping's purpose is a coverage claim. Record the argument for the higher rating in the rationale so a reviewer can overrule deliberately.
8. **Rationale discipline:** a Full rationale states why entailment holds; a Partial rationale states the delta; a rejected candidate needs no rationale but keep a rejection log for high-stakes mappings so reviewers can see what was considered.

---

## 3. Worked example: ISO/IEC 27001:2022 A.8.16 → CSF 2.0 and CIS v8

### Step 1 — Source text

A.8.16 *Monitoring activities* (Technological theme): networks, systems and applications shall be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.

### Step 2 — Normalize and decompose

Two verbs ("monitored", "actions taken to evaluate") → two elements:

- **A.8.16-e1:** [networks, systems, applications] — [monitor] — [for anomalous behaviour] — [continuous/ongoing implied]
- **A.8.16-e2:** [organization] — [take action to evaluate] — [detected anomalies as potential security incidents] — [appropriate/timely implied]

Note what is *not* in the control text: no centralization requirement, no retention requirement, no log-generation requirement (that is A.8.15 Logging), no defined review cadence.

### Step 3 — Candidate generation

Domain-level crosswalk points to CSF 2.0 Detect function (DE.CM, DE.AE categories) and CIS Controls 8 (Audit Log Management) and 13 (Network Monitoring and Defense).

### Step 4 — Rate against CSF 2.0

| Source | Target | Rating | Rationale |
|---|---|---|---|
| A.8.16-e1 | DE.CM-01 (networks and network services monitored to find potentially adverse events) | Full | "Networks" monitored for anomalies entails monitoring networks for potentially adverse events; intent (detection) aligned; no qualifier delta |
| A.8.16-e1 | DE.CM-09 (computing hardware and software, runtime environments, and their data monitored) | Full | "Systems and applications" covers hosts and software environments; same detection intent |
| A.8.16-e2 | DE.AE-02 (potentially adverse events analyzed to better understand associated activities) | Full | "Take action to evaluate potential incidents" entails analysis of detected anomalies |
| A.8.16-e2 | DE.AE-03 (information correlated from multiple sources) | Partial | Evaluation is required by source, but multi-source correlation is a stricter mechanism than A.8.16 mandates — delta: correlation across sources |
| A.8.16-e1 | DE.CM-03 (personnel activity and technology usage monitored) | Partial | Systems monitoring may surface user activity anomalies, but personnel-activity monitoring as an objective is broader (policy violations, insider risk) — delta: monitoring objective |

Rollup toward CSF: A.8.16 contributes Full coverage of DE.CM-01, DE.CM-09, DE.AE-02; Partial toward DE.AE-03 and DE.CM-03. Reverse-direction note for the residue sweep: DE.CM-02 (physical environment) and DE.CM-06 (external service provider activity) receive nothing from A.8.16 — if the mapping's purpose is "ISO Annex A covers CSF Detect", those must find coverage elsewhere (A.7.4 physical monitoring; A.5.22 supplier service monitoring) or land on the coverage-gap list.

### Step 5 — Rate against CIS v8

| Source | Target | Rating | Rationale |
|---|---|---|---|
| A.8.16-e1 | CIS 13.1 (centralize security event alerting) | Partial | Shared detection intent, but 13.1 mandates centralization of alerting, which A.8.16 does not require — delta: centralization |
| A.8.16-e1 | CIS 13.3 (deploy a network intrusion detection solution) | Partial | 13.3 mandates a specific mechanism class (network IDS); A.8.16 requires the outcome (network anomaly monitoring) without mandating the mechanism — mechanism-level delta; an org could satisfy A.8.16 by other means |
| A.8.16-e2 | CIS 8.11 (conduct audit log reviews) | Partial | Both require examining collected data for anomalies; 8.11 is scoped to audit logs with a review-cadence expectation, A.8.16-e2 is anomaly evaluation broadly — deltas both directions |
| A.8.16-e1 | CIS 8.2 (collect audit logs) | None | Collection is a prerequisite for monitoring but not entailed by it; A.8.15 (Logging) is the right ISO source for 8.2. Rejecting this candidate prevents a classic keyword-trap mapping |

Rollup toward CIS: A.8.16 provides Partial support to safeguards in Controls 13 and 8 but Fully covers none — a realistic, and typical, result. An organization mapping ISO → CIS for a coverage claim must pull in A.8.15 (logging), A.5.25 (event assessment/decision), and operational evidence to approach Full on these safeguards.

### Step 6 — What the example teaches

- One well-regarded control (A.8.16) fans out to **five CSF subcategories and four CIS safeguards** with mixed ratings. Any crosswalk showing A.8.16 as a single 1:1 row is discarding information.
- The Full ratings cluster where frameworks state *outcomes*; the Partials cluster where a framework mandates *mechanisms* (IDS, centralization) or *stricter qualifiers* (correlation, cadence). This pattern generalizes: outcome-framed frameworks (CSF, ISO) map Partial onto prescriptive ones (CIS, PCI, 800-53) far more often than Full.
- The rejected 8.2 candidate shows why keyword matching ("logs", "monitoring") without obligation analysis corrupts mappings.

---

## 4. Internal-to-framework specifics

When the source is an internal control library:

- Normalize from the control statement as written and operated, not the aspirational policy sentence above it. If the internal statement is vague ("appropriate access controls are in place"), send it to [../../policy-review/SKILL.md](../../policy-review/SKILL.md) territory: flag it as unmappable-as-written and propose a rewrite before mapping.
- Capture the internal control's actual scope (which systems, which populations) as a qualifier — internal controls are often narrower than their wording implies, and ratings must reflect operated scope.
- Tag each internal control with its evidence type while mapping; this makes the mapping directly reusable by [../../audit-preparation/SKILL.md](../../audit-preparation/SKILL.md) for test-once/attest-many evidence planning.
- Internal residue (controls mapping to nothing external) is not automatically waste: classify each as `unique-obligation` (keep — often contractual or risk-driven), `duplicate` (merge candidate), or `over-spec` (candidate for simplification with risk sign-off).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
