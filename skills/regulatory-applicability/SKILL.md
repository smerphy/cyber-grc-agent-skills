---
name: regulatory-applicability
description: >-
  Determines which cybersecurity and privacy regulations, contractual regimes, and voluntary
  frameworks apply to an organization based on its sectors, jurisdictions, data, and status
  (listed, financial, government contractor). Produces an applicability register with rationale
  and confidence per determination. Use when a user asks "which regulations apply to us,"
  "are we in scope for NIS2/GDPR/DORA/HIPAA," or needs a compliance obligations inventory.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Build a defensible inventory of the cyber and privacy obligations an organization is subject to — the applicability register that every other GRC activity (gap assessments, policy scoping, incident reporting) depends on. The method is a structured profile of the organization followed by regime-by-regime trigger tests, distinguishing what is legally binding from what is contractually required from what is merely voluntary, with an explicit confidence level and counsel-review flag per determination.

## When to use

- The user asks which laws, regulations, or frameworks apply to their organization, or whether a specific regime (NIS2, DORA, GDPR, HIPAA, CCPA, SOX, EU AI Act...) applies.
- A new market entry, product launch, customer segment, acquisition, or listing changes the organization's footprint and the obligations inventory needs re-derivation.
- A compliance program is being scoped from scratch and needs its obligations baseline.
- An incident response needs a fast answer to "which reporting regimes could this touch" and no register exists yet.

**Do not use for:**
- Deciding what to notify after an incident under regimes already known to apply — use [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md).
- Assessing how well the organization meets a framework it has adopted — use [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md).
- Tracking upcoming/changing regulation — use [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md); this skill assesses law as it stands.
- Deep privacy analysis of a specific processing activity — use [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md).

## Inputs to gather

Collect the organization profile before testing any regime. Missing answers become explicit assumptions in the output, never silent defaults.

1. **Legal structure and establishments:** entities, countries of incorporation, branches/offices, group structure (parent/subsidiaries — obligations can attach at entity or group level).
2. **Sectors and activities:** what the organization actually does, mapped to regulated sector definitions (energy, transport, banking, financial market infrastructure, health, drinking water, digital infrastructure, ICT service management, public administration, space, postal, waste, chemicals, food, manufacturing of critical products, digital providers, research — the NIS2 Annex I/II vocabulary; plus healthcare/HIPAA, financial/GLBA-DORA, telecom).
3. **Jurisdictions of customers and data subjects** — distinct from establishment. Where are goods/services offered? Whose behavior is monitored? Where do end users sit?
4. **Data categories processed:** personal data (and special categories), health data/PHI, payment card data, financial account data, children's data, biometric data, government/classified or CUI data, AI training data.
5. **Size and financials:** headcount, annual turnover/revenue, balance sheet total (NIS2 size-cap and state privacy thresholds are numeric), records/consumer counts processed per jurisdiction.
6. **Status flags:** publicly listed (which exchange; domestic issuer vs foreign private issuer), regulated financial entity (which licenses), government contracts (US federal — FAR/DFARS/CUI; other governments), defense supply chain, critical infrastructure designations already received, data broker activities.
7. **Contractual context:** does the org store/process/transmit cardholder data or affect its security (PCI DSS)? Do customer contracts demand SOC 2, ISO 27001, or specific frameworks?
8. **Existing register:** any prior applicability analysis to update rather than rebuild.

## Procedure

1. **Build the organization profile** from the inputs above as a structured fact sheet. Every subsequent determination cites facts from this sheet — if a determination needs a fact the sheet lacks, go back and get it (or record the assumption).

2. **Walk the jurisdictional axis.** For each jurisdiction where the org is established **or** has customers/data subjects, test the general-application data protection and cyber laws using the trigger questions in [references/applicability-decision-trees.md](references/applicability-decision-trees.md):
   - **EU/EEA:** GDPR (Art. 3 territorial scope — establishment, targeting, monitoring), NIS2 (sector + size-cap + special categories), DORA (financial entity types), EU AI Act (provider/deployer/importer roles, output used in the EU).
   - **US:** federal sectoral laws (HIPAA, GLBA, COPPA, FERPA as relevant), SEC/SOX for issuers, state comprehensive privacy laws (threshold tests per state), state breach laws (apply wherever residents' data is held — effectively unavoidable), sector regulators (NYDFS, banking agencies), federal contracting regimes (FISMA-adjacent, DFARS 252.204-7012 / NIST SP 800-171 / CMMC — see [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md)).
   - **UK:** UK GDPR + DPA 2018, NIS Regulations, FCA/PRA operational resilience for financial firms.
   - **Other:** run PIPEDA, LGPD, PDPA, APPI, PIPL, DPDP, Australian Privacy Act/APRA CPS 234 tests per [../../context/regulations/other-jurisdictions.md](../../context/regulations/other-jurisdictions.md) for each remaining jurisdiction with establishments or data subjects.

3. **Walk the sectoral axis.** Regardless of jurisdiction results, test sector-specific regimes: HIPAA covered entity **and** business associate tests (BA status is where non-healthcare companies get caught), GLBA "financial institution" test (broader than banks — significantly engaged in financial activities), DORA financial entity list, NIS2 Annex I vs Annex II classification (essential vs important — different supervision, same security/reporting duties), telecom/eIDAS/trust services, energy and transport sector rules where relevant. A single organization commonly lands in several.

4. **Test the status flags.** Listed status → SOX 302/404 (404(b) auditor attestation depends on filer status) and SEC cyber disclosure (8-K Item 1.05, 10-K Item 106 — foreign private issuers use 6-K/20-F equivalents); see [../../context/regulations/sox-itgc.md](../../context/regulations/sox-itgc.md) and [../../context/regulations/sec-cyber-disclosure.md](../../context/regulations/sec-cyber-disclosure.md). Government contracts → contract-clause-driven regimes (treat as legally enforceable via contract). Data broker registration duties in several US states.

5. **Classify each obligation by bindingness.** Three buckets, kept visually distinct in the register:
   - **Legally binding:** statutes and regulations that apply by operation of law (GDPR, NIS2, HIPAA, state privacy laws...).
   - **Contractually binding:** obligations that bind only via contract but are practically mandatory — PCI DSS (card brand rules flowing through acquirer/merchant agreements), SOC 2 (customer-demanded), DFARS/CMMC clauses, customer-imposed ISO 27001 certification, cyber insurance conditions.
   - **Voluntary/adopted:** frameworks chosen as internal baselines — NIST CSF 2.0, CIS Controls v8, ISO 27001 absent contractual demand. See [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md), [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md), [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md), [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md), [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md).
   Misclassifying PCI DSS or SOC 2 as "law" (or NIS2 as "optional") is a classic register defect — the bucket determines who can grant exceptions and what non-compliance costs.

6. **Assign a determination, rationale, and confidence per regime.** Determination values: **Applies / Does not apply / Likely applies / Likely not / Needs counsel review**. Rationale must cite the trigger test outcome and the profile facts used ("NIS2: important entity — Annex II digital provider (online marketplace), 120 employees > medium-size threshold"). Confidence: **High** (clear statutory test, clear facts), **Medium** (test clear, facts incomplete — state which), **Low** (genuine legal ambiguity — always pair with counsel flag). Never present a Low-confidence determination as settled.

7. **Flag counsel-review items.** Mandatory flags: any "Likely" determination that drives material spend or risk; GDPR Art. 3(2) targeting analysis for orgs without EU establishment; NIS2 member-state scoping questions (national transpositions diverge on registration and scope details); DORA classification for mixed-activity groups; HIPAA hybrid-entity and BA-chain questions; anything turning on pending litigation or regulatory guidance. This skill produces analysis, not legal advice — the register must say which rows a lawyer has to confirm.

8. **Derive downstream actions.** For each "Applies," list the headline obligation categories (e.g., NIS2 → Art. 21 measures + registration + 24h/72h/1-month incident reporting + management accountability) and link the relevant context file rather than restating detail. Hand the register to [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) for compliance posture and to [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) as the incident-time regime sweep input. Set a review trigger: register re-derivation on new market/product/M&A/listing events and at least annually (pair with [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md)).

## Output format

**Applicability register** — one table plus per-row detail notes. Worked example rows (fictional: German-headquartered SaaS analytics company, 180 employees, EUR 25M turnover, EU + US customers, processes customer employee personal data, no card data storage, not listed, has US federal civilian agency pilot contract):

| # | Regime | Type | Determination | Rationale (trigger test + facts) | Confidence | Counsel review | Key obligations (link) |
|---|---|---|---|---|---|---|---|
| 1 | EU GDPR | Legal | Applies | Art. 3(1): establishment in Germany processing personal data | High | No | [gdpr.md](../../context/regulations/gdpr.md) |
| 2 | NIS2 | Legal | Likely applies | Annex II digital provider test hinges on whether the platform is a "cloud computing service" under national transposition; size (180 empl., EUR 25M) exceeds medium threshold | Medium | **Yes** | [nis2.md](../../context/regulations/nis2.md) |
| 3 | CCPA/CPRA | Legal | Likely not | B2B SaaS; revenue below threshold; CA consumer/household count est. < 100k — count unverified | Medium | No — verify count | [us-state-privacy.md](../../context/regulations/us-state-privacy.md) |
| 4 | US state breach laws | Legal | Applies | Holds personal information of residents of multiple states; breach laws have no size threshold | High | No | [us-state-privacy.md](../../context/regulations/us-state-privacy.md) |
| 5 | HIPAA | Legal | Does not apply | Fails CE test (no plan/clearinghouse/provider activity); no BA relationship in current contracts — re-test on new healthcare customers | High | No | [hipaa.md](../../context/regulations/hipaa.md) |
| 6 | DORA | Legal | Does not apply directly | Not a financial entity; **but** exposure as ICT third-party provider to two EU bank customers — contractual DORA flow-down expected | High | No | [dora.md](../../context/regulations/dora.md) |
| 7 | NIST SP 800-171 (DFARS-equivalent clause) | Contractual | Applies | Federal pilot contract includes CUI safeguarding clause | High | No | [nist-800-53.md](../../context/frameworks/nist-800-53.md) |
| 8 | SOC 2 | Contractual | Applies | 6 enterprise customers require Type II report | High | No | [soc2-tsc.md](../../context/frameworks/soc2-tsc.md) |
| 9 | PCI DSS | Contractual | Does not apply | No storage/processing/transmission of cardholder data; payments fully outsourced to PSP with hosted fields — validate SAQ A eligibility with acquirer | High | No | [pci-dss-4.md](../../context/frameworks/pci-dss-4.md) |
| 10 | SOX / SEC disclosure | Legal | Does not apply | Not an SEC registrant | High | No | [sox-itgc.md](../../context/regulations/sox-itgc.md) |
| 11 | EU AI Act | Legal | Needs counsel review | Product includes ML-based scoring of employees for customers — possible high-risk (employment) system; provider-role analysis required | Low | **Yes** | [eu-ai-act.md](../../context/regulations/eu-ai-act.md) |

Follow the table with:
- **Assumptions and open facts** (numbered; each mapped to the rows it affects).
- **Counsel review list** (rows flagged, question to be answered, urgency).
- **Change triggers** (events that invalidate specific rows — "first healthcare customer → re-test row 5," "US listing → rows 10").
- **Register metadata:** date, author, profile fact sheet version, next review date.

## Quality checklist

- [ ] Both axes walked: every establishment/customer jurisdiction AND every sector test — no regime dismissed without a stated test outcome.
- [ ] Customer/data-subject jurisdictions tested separately from establishment jurisdictions (GDPR Art. 3(2)-type extraterritoriality checked for every major regime).
- [ ] Every row has: determination, rationale citing profile facts, confidence, counsel flag, and an obligations link — no bare Yes/No rows.
- [ ] Legal vs contractual vs voluntary classification present and correct (PCI DSS and SOC 2 not listed as law; no legally binding regime listed as optional).
- [ ] Numeric thresholds (NIS2 size-cap, state privacy law consumer/revenue counts) tested against actual figures, or the missing figure is a named open fact.
- [ ] Second-order exposures caught: business associate status, ICT third-party/DORA flow-down, processor obligations, government contract clauses, data broker registration.
- [ ] "Does not apply" rows carry re-test triggers where the answer is fact-fragile.
- [ ] Low-confidence and "Likely" determinations all carry counsel flags or a named verification step; nothing ambiguous presented as settled.
- [ ] Group structure handled: register states which legal entity each determination attaches to.
- [ ] Review cadence and change triggers defined.

## References

- [references/applicability-decision-trees.md](references/applicability-decision-trees.md) — structured trigger questions per major regime.
- [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md) · [../../context/regulations/nis2.md](../../context/regulations/nis2.md) · [../../context/regulations/dora.md](../../context/regulations/dora.md) · [../../context/regulations/eu-ai-act.md](../../context/regulations/eu-ai-act.md) · [../../context/regulations/hipaa.md](../../context/regulations/hipaa.md) · [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md) · [../../context/regulations/glba-ftc-safeguards.md](../../context/regulations/glba-ftc-safeguards.md) · [../../context/regulations/sox-itgc.md](../../context/regulations/sox-itgc.md) · [../../context/regulations/sec-cyber-disclosure.md](../../context/regulations/sec-cyber-disclosure.md) · [../../context/regulations/other-jurisdictions.md](../../context/regulations/other-jurisdictions.md)
- [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md) · [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) · [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md) · [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md) · [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) · [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md)
- [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) — consumes this register at incident time.
- [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) — assess posture against regimes found applicable.
- [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md) — keep the register current as law changes.
- [../../context/internal/organization-profile.md](../../context/internal/organization-profile.md) — the organization's entities, footprint, sectors, and regulators, if filled in (respect the status marker); record applicability conclusions back into it.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
