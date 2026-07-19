# Vendor Tiering Rubric

Tiering exists to ration assessment effort. A program that assesses every vendor identically either drowns in Tier 1-depth reviews or dilutes everything to Tier 4-depth checkbox work. Tier on two axes, take the higher result, document the driver.

## Axis 1 — Data sensitivity and access

Score the *worst-case* data the vendor can touch under the contracted service, not the intended happy path. "Views via screen share during support calls" still counts as access.

| Score | Data/access profile | Examples |
|-------|--------------------|----------|
| 4 (Critical) | Stores or processes regulated data at scale: PHI, cardholder data (in-scope for PCI), government-classified, authentication secrets for your production estate; or holds privileged/admin access to production systems or your identity provider | Payment processor, EHR platform, managed detection and response provider with EDR admin, cloud identity provider, payroll processor |
| 3 (High) | Stores or processes customer PII, employee PII beyond directory data, material non-public financials, source code, or trade-secret IP; or has persistent network/API connectivity into internal systems | CRM, HR information system, code hosting, data warehouse ETL tool, customer support platform with ticket contents |
| 2 (Moderate) | Business contact data, internal documents of low sensitivity, aggregated or pseudonymized analytics; access limited to a narrow SaaS tenant with your data segregated | Webinar platform holding registrant names/emails, project management tool used for non-sensitive projects, survey tool |
| 1 (Low) | No organizational data beyond procurement/billing details; no connectivity | Office supplies vendor, facilities landscaping, stock photo subscription |

Modifiers:
- **Volume matters at the margin.** 50 customer email addresses in a survey tool is not the same exposure as 5 million in a marketing platform. Bump a score-3 down to 2 if records are trivially few and non-sensitive; bump a 2 up to 3 if volume is very large.
- **Credentials and keys are data.** A vendor holding API keys scoped to read production data inherits the score of that data.
- **Aggregation risk.** Several low-sensitivity feeds into one vendor can aggregate to a higher score (e.g., a business intelligence tool ingesting five "moderate" sources).

## Axis 2 — Operational criticality

Score by tolerable outage duration and substitutability.

| Score | Criticality profile | Test question |
|-------|--------------------|---------------|
| 4 (Critical) | Outage halts revenue, safety, or legal obligations within hours; no practical short-term substitute | "If this vendor is down for 4 hours, do we stop serving customers or breach an SLA/legal duty?" |
| 3 (High) | Outage degrades a core process; workarounds exist but are costly; recovery within days required | "Can we limp for 2-3 days with manual workarounds?" |
| 2 (Moderate) | Outage is an inconvenience; tolerable for a week+; substitutes available within a procurement cycle | "Would anyone outside the owning team notice within a week?" |
| 1 (Low) | No operational dependency | "Could we drop this vendor tomorrow with no process impact?" |

Modifiers:
- **Concentration.** If the vendor underpins multiple critical processes, or is one of very few viable providers in the market, raise the score by one. (This is the concern behind DORA's critical ICT third-party provider concept — see `../../../context/regulations/dora.md`.)
- **Fourth-party dependency.** If your critical vendor and your fallback both run on the same subservice provider, note it; it does not change the tier but belongs in the findings.

## Combining axes

**Tier = max(data score, criticality score)**, expressed as Tier 1 (score 4) down to Tier 4 (score 1). Record both scores; the gap tells you what to worry about:

- Data 4 / Criticality 1 → Tier 1 driven by confidentiality: focus on encryption, access control, breach notification, data deletion.
- Data 1 / Criticality 4 → Tier 1 driven by availability: focus on BCP/DR evidence, RTO/RPO commitments, SLA credits, exit plan, and the Availability TSC in their SOC 2 scope.

## Worked examples

| Vendor | Data score | Criticality score | Tier | Notes |
|--------|-----------|-------------------|------|-------|
| Payroll SaaS, 2,000 employees | 4 (PII incl. bank details, tax IDs) | 3 (payroll can slip days, not weeks) | 1 | Confidentiality-driven; require SOC 2 Type II, DPA, breach SLA |
| Cloud IaaS hosting production | 4 | 4 | 1 | Both axes maxed; also appears as carve-out in other vendors' SOC 2 reports |
| Marketing email platform, 3M customer emails | 3 (large-volume PII, low sensitivity per record) | 2 | 2 | Volume keeps it at 3 despite simple data |
| Code hosting (private repos) | 3 (source code, CI secrets) | 4 (dev and deploy halt) | 1 | Often under-tiered; CI secrets make it credential-critical |
| Ticketing tool, internal IT only, no customer data | 2 | 3 (IT support degrades) | 2 | |
| Contract e-signature, ~200 contracts/yr | 3 (contracts contain sensitive terms) | 2 | 2 | |
| Survey tool, anonymous product feedback | 2 | 1 | 3 | Short-form questionnaire or cert check only |
| Office coffee supplier | 1 | 1 | 4 | Registration only; resist the urge to assess |
| MDR/SOC provider with EDR admin agents fleet-wide | 4 (privileged endpoint access) | 4 (detection capability) | 1 | Deepest assessment in the portfolio; audit rights essential |
| Analytics SDK embedded in your product | 3 (end-user behavioral data, runs in your product) | 3 (removal requires release cycle) | 2 | Also a supply-chain code risk; ask about SDK signing and update process |

## Tier-to-depth mapping (summary)

| Tier | Evidence required | Questionnaire | Reassessment | Contract |
|------|-------------------|---------------|--------------|----------|
| 1 | SOC 2 Type II (or ISO cert + SoA + bridge evidence) AND pen test attestation; architecture/data-flow review | Full, minus items answered by reports | Annual + triggers | Full security schedule, mandatory |
| 2 | SOC 2 Type II or ISO cert + SoA | Targeted (gaps only) | 12-18 months + triggers | Core clauses (breach SLA, audit right, subprocessor, deletion) |
| 3 | Any one: current cert, SOC 2 (either type), or short-form questionnaire | Short-form (~20 questions) | 24 months, evidence refresh | Standard terms + breach notification |
| 4 | None proactive | None | Trigger-based only | Standard terms |

## Common tiering failures

- **Tiering by contract value.** A $3k/year OAuth-connected tool with mailbox read scope outranks a $500k facilities contract. Spend is not risk.
- **Tiering once, forever.** Scope creep (the "pilot" that now holds production data) is the norm. Reassess tier on any material scope change and at renewal.
- **Letting the business self-tier.** Owners under-tier to skip assessment. Security assigns tier; the owner supplies facts.
- **Ignoring free/shadow tools.** Anything integrated via OAuth into corporate identity or data stores gets tiered, paid or not.
