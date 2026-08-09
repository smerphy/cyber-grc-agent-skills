# Internal Control Catalog

**Status: TEMPLATE — not filled in.**

*Your organization's control set — the anchor for [control-mapping](../../skills/control-mapping/SKILL.md) (map internal controls to frameworks once, reuse everywhere), [control-testing](../../skills/control-testing/SKILL.md) (what to test, who owns it), and [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) (assess against your controls, not abstract ones). If the real catalog lives in a GRC tool, keep this file as the schema + export convention rather than duplicating it — but record the ID scheme and mappings policy here either way. Agents: while the status is TEMPLATE, the rows below are illustrative, not your controls.*

## Catalog conventions

| Field | Value |
|---|---|
| ID scheme | [example: CTL-<domain>-NN, e.g. CTL-IAM-03] |
| Domains | [example: IAM, VULN, NET, DATA, IR, BCM, TPRM, HR, PHY, GOV] |
| System of record | [example: GRC tool; this file regenerated from monthly export] |
| Mapping policy | [example: mappings maintained internal→framework, with coverage rating full/partial per control-mapping skill conventions] |

## Catalog

| ID | Control | Domain | Type | Frequency | Owner | Framework mappings | Evidence source |
|---|---|---|---|---|---|---|---|
| [example: CTL-IAM-01] | [example: Joiner/mover/leaver access provisioning tied to HR events] | [example: IAM] | [example: preventive, automated] | [example: continuous] | [example: Head of IAM] | [example: ISO 27001 A.5.16/A.5.18 (full); SOC 2 CC6.2 (full); CSF PR.AA (partial)] | [example: IdP + HR feed logs] |
| [example: CTL-IAM-03] | [example: Quarterly privileged access review] | [example: IAM] | [example: detective, manual] | [example: quarterly] | [example: Head of IAM] | [example: ISO 27001 A.5.18 (partial); SOC 2 CC6.3 (full)] | [example: review sign-offs in ticketing] |
| [example: CTL-VULN-02] | [example: Critical vulnerability remediation within 15-day SLA (internet-facing)] | [example: VULN] | [example: corrective] | [example: continuous] | [example: Head of Platform] | [example: CIS 7.x (full); ISO 27001 A.8.8 (full)] | [example: scanner + ticketing extract] |

## Retired and superseded controls

*Keep the trail — auditors and trend lines both need it.*

| ID | Control | Retired | Superseded by | Reason |
|---|---|---|---|---|
| [example: CTL-IAM-09] | [example: Annual all-staff access recertification] | [example: 2026-01] | [example: CTL-IAM-03 quarterly scoped reviews] | [example: annual big-bang reviews produced rubber-stamping] |

**Document owner:** [name/team] · **Review cycle:** [example: monthly export refresh; conventions annually]
