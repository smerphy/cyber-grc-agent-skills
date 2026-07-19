# TISAX — Trusted Information Security Assessment Exchange (Automotive)

## At a glance

| Attribute | Detail |
|---|---|
| Operator | **ENX Association** (on behalf of the VDA, the German Association of the Automotive Industry) — runs registration, audit-provider accreditation, and the results-exchange platform |
| Catalogue | **VDA ISA** (Information Security Assessment) — control questionnaire maintained by the VDA; ISO/IEC 27001-derived heritage. Current major version **6** (published late 2023, mandatory for new assessments from 2024) — **verify the current minor release** before an engagement |
| Structure | Modular catalogue: information security (core), prototype protection, and data protection modules; controls scored on a **maturity model (levels 0–5)** with target maturity 3 for most requirements |
| Assessment levels | AL1 (self-assessment, no label), AL2 (plausibility check, usually remote), AL3 (comprehensive on-site assessment) — driven by protection need: normal / high / very high |
| Outcome | **TISAX labels** recorded on the ENX portal and shared with chosen partners — there is **no public certificate** |
| Validity | **3 years**, then full re-assessment (no annual surveillance audits, unlike ISO 27001) |
| Assessors | ENX-accredited audit providers only (a defined list of firms); the participant contracts one directly |
| Who needs it | Suppliers and service providers handling protected information of German/European OEMs and their tier-1s — routinely a **contractual precondition** for awards involving confidential data, prototypes, or connected services |
| Typical use | Automotive supply-chain trust mechanism replacing per-OEM security audits with one mutually recognized assessment |

## Key terms

| Term | Meaning |
|---|---|
| Participant | An organization registered with ENX that undergoes assessments and/or consumes others' results |
| Assessment scope | The defined locations/processes assessed; the "standard scope" wording is strongly preferred — custom scopes reduce acceptance by partners |
| Assessment objective | What you are assessed *for* (e.g., handling data with high protection needs, prototype protection); determines module, level, and label |
| TISAX label | The shareable proof that an objective was achieved for a scope; visible to permitted partners on the ENX portal |
| Assessment level (AL) | Rigor of the audit (AL1/AL2/AL3), driven by protection need |
| Audit provider | ENX-accredited firm that performs AL2/AL3 assessments |
| Exchange | The controlled sharing of assessment results between participants via the ENX portal |

## How the scheme works

1. **Register as a participant** with ENX (fee applies); define one or more **assessment scopes** — normally the "standard scope" covering the locations that collect, store, or process protected information for the relevant business.
2. **Select assessment objectives** — these determine the required module(s) and assessment level, and map to the labels you will earn.
3. **Self-assess** against the VDA ISA catalogue, remediate obvious gaps.
4. **Contract an ENX-accredited audit provider** for the required assessment level.
5. **Assessment** → findings → corrective-action plans. Minor nonconformities can yield **temporary labels** while corrective actions complete (follow-up within a defined window, historically up to nine months — verify current rules); major gaps block labels.
6. **Labels published to the ENX portal**; the participant controls which partners can view results and at what detail level.

## Assessment levels and protection needs

| Protection need | Assessment level | Method |
|---|---|---|
| Normal | AL1 | Self-assessment; result has essentially no exchange value — no labels |
| High | AL2 | Audit provider performs a plausibility check of the self-assessment and evidence, typically via remote interviews/document review |
| Very high | AL3 | Full assessment including on-site verification, interviews, and effectiveness checking |

The OEM/customer dictates the protection need (and therefore the level and objectives) in the contract or supplier requirements — confirm in writing before scoping, since AL2→AL3 is a materially larger exercise.

## Assessment objectives and labels

Objectives fall into three families; earning an objective yields the corresponding label(s) on the portal:

- **Information security** — confidentiality- and availability-oriented objectives for handling partner information with high or very high protection needs. VDA ISA 6 restructured these (splitting confidentiality and availability aspects into distinct labels, replacing the older "Info High"/"Info Very High" naming) — **verify current label names** on the ENX site before writing them into contracts or reports.
- **Prototype protection** — physical and organizational security for prototype parts, vehicles, and test operations (based on the VDA prototype-protection requirements); relevant to proving grounds, camouflage, presentation/filming, and test-vehicle logistics.
- **Data protection** — processing personal data on behalf of partners (GDPR Art. 28 processor context), with a heightened variant for special categories of data.

An assessment can bundle multiple objectives in one audit; labels are earned per objective for the defined scope.

## Maturity-based scoring

Unlike ISO 27001's conform/nonconform model, VDA ISA scores each requirement on maturity levels **0 (incomplete) through 5 (optimizing)**, with 3 ("established" — defined, implemented, evidenced) as the general target. The overall result is computed from per-control scores, and scores above target are **cut back** so that over-performance on some controls cannot offset gaps elsewhere. Practical consequences:

- "We do it but haven't documented it" caps maturity below target — documentation and demonstrable operation matter as much as the technical control.
- The result is a numeric maturity profile plus findings, which is more granular than a certificate and is visible (at the permitted detail level) to sharing partners.

## Exchange mechanism — how results are consumed

- Results live on the **ENX portal**; the assessed participant grants each partner access and chooses a **disclosure level** — from label-only up to detailed results including maturity scores and findings.
- OEM supplier-security requirements typically state the required labels, protection need, and assessment level; the supplier satisfies them by sharing the matching portal entry — no audit report changes hands by default.
- There is no public register to check a claimed label against; verification requires the supplier to grant portal access (or produce a portal excerpt). Build that request into onboarding workflows.
- Labels carry scope: a partner should confirm the label covers the **locations actually performing their work** and the right objective — the portal shows scope locations for exactly this purpose.
- Sub-suppliers handling in-scope information are commonly required to hold TISAX labels too — flow-down obligations appear in OEM terms; factor this into supply-chain assessments.

## TISAX vs ISO 27001 certification

| | ISO 27001 | TISAX |
|---|---|---|
| Requirement source | Your own risk-driven SoA against Annex A | Fixed VDA ISA catalogue — no scoping controls away by risk acceptance |
| Verdict | Certificate: conformity of the ISMS | Maturity scores + labels per objective |
| Publicity | Public certificate, freely shareable | Results shared only via ENX portal to approved partners |
| Cycle | 3-year cycle **with annual surveillance audits** | 3-year validity, no surveillance in between |
| Recognition | Cross-industry | Mutual recognition **within automotive** — OEMs accept each other's required labels instead of running their own audits |
| Extras | — | Prototype-protection and data-protection modules with no ISO equivalent |

An existing ISO 27001 ISMS is the best possible foundation — the VDA ISA catalogue is built on ISO 27001/27002 concepts and much evidence is reusable — but an ISO certificate **does not replace** a TISAX assessment, and TISAX labels do not constitute ISO certification. Organizations holding both should maintain one control set mapped to both catalogues (see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) and [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md)).

## Common findings in first-time assessments

- Information classification scheme exists on paper but is not applied to actual documents, repositories, and email handling.
- Supplier/sub-supplier security requirements not contractually flowed down or not monitored.
- Asset inventories incomplete for the assessed scope (test benches, engineering workstations, external development partners).
- Cryptography and key-management practices undocumented despite adequate tooling.
- Incident management defined but never exercised; no link to customer-notification obligations in OEM contracts.
- Business continuity / availability controls thin relative to the availability-oriented objectives introduced with ISA 6-era restructuring.
- Physical/prototype gaps: visitor management, camera policies, visual protection of prototypes in shared spaces.

## Preparation guidance

- **Scope precisely.** Scope is location- and business-process-based; every site handling in-scope information needs coverage (site groups/multi-site rules exist — confirm with the audit provider). Missing a satellite office that touches OEM data is a classic late finding.
- **Run the self-assessment early and honestly** against the current VDA ISA version; budget remediation time for the perennial gaps: information classification actually applied, supplier security management, secure development evidence, incident-management exercising, and business-continuity/availability controls (weight increased in ISA 6 era — verify).
- **Evidence at maturity 3 means:** documented requirement + assigned responsibility + implementation proof + records of operation. Assemble this per control before the audit window, per [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
- **Prototype module is physical-security-heavy** — perimeter, access control, visual protection, transport — involve facilities/site management early; IT-led teams underestimate it.
- Typical timeline from standing start to labels: several months to a year depending on ISMS maturity; the ENX registration and audit-provider scheduling add lead time — start registration before remediation finishes.

## Using this in assessments

- **Gap assessments:** run against the current VDA ISA catalogue at the contractually required objectives/level — structure per [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md); an ISO 27001 readiness effort ([../../skills/iso27001-readiness/SKILL.md](../../skills/iso27001-readiness/SKILL.md)) covers much of the core module but not maturity evidencing, prototypes, or the data-protection module.
- **Vendor due diligence:** for automotive suppliers, ask for portal-shared TISAX results, and check **scope locations, objectives/labels, assessment level, and expiry** — a label for the wrong site or objective is weak evidence (see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)). Remember results are not public: absence from public view proves nothing either way.
- **Data-protection module ≠ GDPR compliance program** — it evidences processor-side controls for partners; the legal regime lives in [../regulations/gdpr.md](../regulations/gdpr.md).
- **Common pitfalls:** assuming ISO 27001 certification will be accepted in lieu of TISAX; scoping only headquarters when engineering/test sites hold the actual OEM data; treating maturity 3 as "control exists" without operating evidence; missing the re-assessment lead time at year 3 (labels lapse — there is no grace surveillance visit to catch drift).

## References

- Related frameworks: [iso-27001-2022.md](iso-27001-2022.md), [nist-csf-2.md](nist-csf-2.md), [soc2-tsc.md](soc2-tsc.md)
- Regulations: [../regulations/gdpr.md](../regulations/gdpr.md), [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md)
- Crosswalks: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/iso27001-readiness/SKILL.md](../../skills/iso27001-readiness/SKILL.md), [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md), [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
