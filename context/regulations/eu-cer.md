# Critical Entities Resilience Directive (EU 2022/2557)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Directive (EU) 2022/2557 ("CER Directive") — requires national transposition; obligations bind via member-state law |
| Replaces | European Critical Infrastructure Directive 2008/114/EC |
| Entered into force | 16 January 2023 (adopted as a package with NIS2) |
| Transposition deadline | 17 October 2024 (same date as NIS2; several member states missed it — check local implementing law) |
| Designation timeline | Member states to adopt national strategies and risk assessments, then identify critical entities — identification was due by mid-2026 (verify exact national dates); obligations bite ~10 months after an entity is notified of its designation |
| Who is covered | Entities **designated as critical** by a member state in one of 11 sectors — designation-based, not self-assessed |
| Core obligations | Entity risk assessment, resilience measures, incident notification, employee background checks, cooperation with authorities |
| Maximum fines | Set by national law — the directive requires "effective, proportionate and dissuasive" penalties but sets no EU-wide floor or ceiling |
| Supervisors | National competent authorities per member state; Critical Entities Resilience Group at EU level |

## What it is

CER is the **physical-resilience sibling of NIS2**. The two directives were adopted the same day and share a design philosophy: NIS2 addresses cyber risks to network and information systems; CER addresses **all-hazards resilience** of the entities themselves — natural disasters, terrorism, insider threats, sabotage, public-health emergencies, and hybrid attacks, alongside the physical dimension of cyber-physical incidents.

The key structural difference from NIS2: CER is **designation-based**. An entity is not in scope because it matches a sector and size test; it is in scope because a member state has identified it as a critical entity and told it so. Expect designations to concentrate on genuinely infrastructure-critical operators — a much smaller population than NIS2's.

## Sectors (Annex)

Eleven sectors, closely mirroring NIS2 Annex I:

- Energy (electricity, district heating/cooling, oil, gas, hydrogen)
- Transport (air, rail, water, road)
- Banking
- Financial market infrastructure
- Health
- Drinking water
- Waste water
- Digital infrastructure
- Public administration
- Space
- Production, processing and distribution of food

## Designation of critical entities

Each member state must:

1. Adopt a **national resilience strategy** and carry out a **national risk assessment** covering the Annex sectors.
2. **Identify critical entities**: entities providing one or more essential services, operating and with critical infrastructure located on its territory, where an incident would have significant disruptive effects on the provision of essential services (significance judged on user numbers, interdependencies, substitutability, and cross-border impact, among other criteria).
3. **Notify** each designated entity, which then has (approximately) 10 months before the core obligations apply to it — verify the exact mechanics in national law.

Entities providing essential services to or in **six or more member states** can be recognised as "critical entities of particular European significance," attracting Commission/member-state advisory missions and additional oversight.

## Obligations of designated critical entities

- **Entity-level risk assessment** — within (approximately) nine months of notification and at least every four years thereafter, based on the national risk assessment plus entity-specific all-hazards analysis.
- **Resilience measures** — appropriate and proportionate technical, security, and organisational measures to: prevent incidents (including disaster-risk reduction and physical protection of premises and infrastructure); ensure adequate physical protection and access control; respond to, resist, and mitigate the consequences of incidents (alarm, crisis-management, and continuity procedures); recover from incidents (business continuity, alternative supply chains); manage employee security (see background checks below); and raise staff awareness. Documented in a resilience plan or equivalent.
- **Background checks** — critical entities may request, and member states must provide a mechanism for, background verification of personnel in sensitive roles (identity confirmation and criminal-record checks), within the limits of national and EU law.
- **Incident notification** — notify the competent authority of incidents that significantly disrupt or are capable of significantly disrupting the provision of essential services **without undue delay and in any event within 24 hours** of becoming aware, followed by a detailed report within one month where relevant (verify the exact staging against the official text and national implementation). Authorities inform the public where disclosure is in the public interest.
- **Cooperation and information provision** — respond to authority information requests, permit inspections and audits, and implement remediation orders.

## Supervision and enforcement

Competent authorities can conduct on-site inspections and off-site supervision, require information and evidence of resilience measures, and order remediation. Penalties are left to national law — unlike NIS2, there are no EU-mandated minimum fine ceilings, so exposure varies materially by member state. Management-liability mechanics also follow national implementation.

## Key obligations for security/GRC teams

1. **Track designation, don't self-assess into scope.** Monitor national identification processes in every member state where the organisation operates essential-service infrastructure; designation letters start the compliance clock. Feed this into horizon scanning — see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
2. **Assume NIS2 consequences immediately upon designation**: CER designation makes the entity an essential entity under NIS2 regardless of size, with NIS2's proactive supervision and fine regime attaching to the cyber side. See [./nis2.md](./nis2.md).
3. **Extend risk assessment beyond cyber** to all-hazards: physical intrusion, sabotage, natural disasters, dependencies on utilities and suppliers, and cross-border interdependencies. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
4. **Unify incident notification runbooks**: a cyber-physical incident at a designated entity can require a CER notification (≤24h), a NIS2 early warning (≤24h), and a GDPR notification (≤72h) to different recipients. Pre-map the national portals — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
5. **Build the personnel-security process**: define sensitive roles, establish the background-check workflow with the national mechanism, and reconcile it with employment and data-protection law.
6. **Consolidate physical and cyber governance.** CER effectively forces convergence of corporate/physical security and information security programs; a single resilience plan with shared risk register and board reporting is the efficient answer — see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIS2:** the defining interaction — entities identified as critical under CER are **automatically essential entities under NIS2**, in scope regardless of size. CER governs physical/all-hazards resilience; NIS2 governs cybersecurity of network and information systems. Authorities under the two regimes are required to cooperate and share incident information. See [./nis2.md](./nis2.md).
- **DORA:** for banking and financial market infrastructure, DORA occupies the ICT-resilience field; CER designation would layer physical-resilience duties on top. Member states may apply CER to these sectors in a limited way given the density of financial-sector regulation — verify national approach. See [./dora.md](./dora.md).
- **GDPR:** background checks and incident records involve personal data; process them with a documented lawful basis and retention limits. See [./gdpr.md](./gdpr.md).

## Primary sources

- [Directive (EU) 2022/2557 (CER) — official text on EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
