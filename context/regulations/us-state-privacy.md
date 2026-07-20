# US State Privacy Laws (CCPA/CPRA and the Comprehensive-Law Landscape)

The US has no comprehensive federal privacy law. Privacy regulation is a patchwork: sectoral federal laws ([HIPAA](hipaa.md), [GLBA](glba-ftc-safeguards.md), COPPA, FCRA), FTC Section 5 enforcement against unfair or deceptive practices, state comprehensive privacy laws (roughly 20 states as of mid-2026), and breach notification statutes in all 50 states plus DC and territories.

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | US states individually; laws apply based on doing business in / targeting residents of the state, subject to revenue and volume thresholds |
| In force since | CCPA effective 2020-01-01; CPRA amendments operative 2023-01-01; Virginia (VCDPA) 2023-01-01; Colorado (CPA) and Connecticut (CTDPA) 2023-07-01; Utah (UCPA) 2023-12-31; others rolling through 2024–2026 |
| Regulators | California: California Privacy Protection Agency (CPPA) + California AG; all other states: state Attorney General (Colorado also empowers district attorneys) |
| Max penalties | CCPA: up to $2,500 per violation / $7,500 per intentional violation or violations involving minors' data (per consumer, per violation — aggregates fast); other states typically similar per-violation civil penalty ranges under AG enforcement or state UDAP statutes |
| Who's covered | Businesses meeting state thresholds (revenue and/or number of residents' data processed); most laws exempt nonprofits (with exceptions), HIPAA/GLBA-regulated data, and employment data (except California) |
| Private right of action | Only CCPA, and only for certain data breaches (Cal. Civ. Code §1798.150): statutory damages $100–$750 per consumer per incident. No general private right of action in any state comprehensive law |

## California: CCPA as amended by CPRA

The California Consumer Privacy Act (2018), substantially amended by the California Privacy Rights Act (Prop 24, 2020), is the strictest and most-enforced state regime and the de facto US design baseline.

### Applicability thresholds

A for-profit entity doing business in California that collects California residents' personal information and meets **any one** of:

1. Annual gross revenue above **$25 million** (adjusted periodically for inflation — verify the current figure);
2. Annually buys, sells, or shares the personal information of **100,000 or more** California consumers or households;
3. Derives **50% or more of annual revenue** from selling or sharing consumers' personal information.

Since 2023, CCPA covers **employee and B2B contact data** — California is the only state whose comprehensive law reaches HR data. Entity-level exemptions are narrow; data-level exemptions cover PHI under HIPAA, GLBA-regulated data, FCRA data, and similar.

### Key concepts

- **Personal information (PI)** — information that identifies, relates to, or could reasonably be linked with a consumer or household. Household linkage is broader than GDPR's individual focus.
- **Sensitive personal information (SPI)** — includes SSN and other government identifiers, financial account credentials, precise geolocation, racial/ethnic origin, religious beliefs, union membership, contents of mail/email/texts not directed to the business, genetic data, biometric data for identification, health data, and sex life/sexual orientation data. Consumers may **limit use and disclosure** of SPI to specified necessary purposes.
- **Sell / share** — "sell" is broad (disclosure for monetary *or other valuable* consideration); "share" specifically means disclosure for **cross-context behavioral advertising**, with or without consideration. Most third-party ad-tech data flows are sales or sharing.
- **Service provider / contractor / third party** — a recipient is a service provider only under a written contract restricting processing to specified business purposes, prohibiting sale/share, prohibiting combination with other data (limited exceptions), and requiring compliance assistance. Without conforming contract terms, the disclosure defaults to a sale.

### Consumer rights

- **Know/access** — categories and specific pieces of PI collected, sources, purposes, and categories of third-party recipients.
- **Delete** — with exceptions (transaction completion, security and fraud prevention, legal compliance, internal uses compatible with expectations); must flow down to service providers.
- **Correct** — inaccurate PI.
- **Opt out of sale/sharing** — must honor a "Do Not Sell or Share My Personal Information" link and the **Global Privacy Control (GPC)** opt-out preference signal (enforced — see the Sephora settlement).
- **Limit use/disclosure of SPI.**
- **Non-discrimination / non-retaliation** for exercising rights; financial incentives allowed with disclosures.
- **Opt-in for minors** — no sale/sharing of PI of consumers under 16 without opt-in (13–15 self-consent; under 13 parental consent).

Respond to requests within **45 days**, extendable once by a further 45 days with notice.

### Enforcement and security expectations

- **CPPA** — first US dedicated privacy regulator; rulemaking (including regulations on cybersecurity audits, risk assessments, and automated decision-making technology — check current status and compliance dates) and administrative enforcement. The 30-day cure period was removed by CPRA; cure is now discretionary.
- **California AG** — parallel civil enforcement.
- **Reasonable security** — the §1798.150 private right of action attaches to breaches of unencrypted, unredacted PI resulting from failure to maintain **reasonable security procedures and practices**. California guidance has historically pointed to the CIS Controls as a benchmark for reasonableness — see [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md). Statutory damages without proof of actual harm make this the primary class-action driver in US breach litigation.
- **Risk assessments and cybersecurity audits** — CPPA regulations require risk assessments for higher-risk processing and annual independent cybersecurity audits for businesses whose processing presents significant risk; phased compliance dates apply — verify current requirements and deadlines.

## The broader state landscape

### The common model

Virginia's CDPA (2023) set the template most states copied; Colorado and Connecticut strengthened it; Utah weakened it (no correction right, narrower assessments); Texas notably applies without a revenue threshold to businesses that are not small businesses. Oregon and Montana are among the stronger recent adopters. Roughly **20 states** have passed comprehensive laws as of mid-2026, with effective dates rolling through 2026 — maintain a current tracker rather than relying on a static list; see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

Shared architecture (verify specifics per state before relying on them):

- **Controller/processor model** — GDPR-style terminology (unlike CCPA's business/service provider), with mandatory processor contracts covering confidentiality, subcontractor flow-down, deletion/return, and compliance demonstration.
- **Applicability thresholds** — typically processing personal data of ~100,000 residents, or ~25,000 residents plus a revenue share from data sales; thresholds and exact figures vary by state.
- **Consumer rights** — access, deletion, correction (most states), portability, and appeal of rights-request denials (a feature CCPA lacks).
- **Opt-outs** — sale of personal data, **targeted advertising**, and **profiling** in furtherance of decisions producing legal or similarly significant effects. Several states (including Colorado, Connecticut, Texas, Oregon, Montana) require honoring **universal opt-out mechanisms** such as GPC.
- **Sensitive data** — most states require **opt-in consent** before processing sensitive data (California's limit-use model is the outlier). Categories broadly track: racial/ethnic origin, religion, health, sexual orientation, immigration/citizenship status, genetic/biometric data, children's data, precise geolocation.
- **Data protection assessments** — required for targeted advertising, sale, sensitive data processing, and profiling presenting heightened risk. Producible to the AG on demand. One well-built assessment process can serve all states plus GDPR DPIAs — see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
- **Reasonable security** — all comprehensive laws require security appropriate to the volume and nature of the data; none prescribes specific controls.
- **Enforcement** — AG-only, civil penalties per violation; several states had sunsetting cure periods. **No private right of action** in any state comprehensive law except California's breach provision.
- **Common exemptions** — GLBA and HIPAA entity- or data-level exemptions, FCRA data, employment and B2B data (except California), nonprofits (with state-by-state exceptions), and small businesses below thresholds.

Beyond comprehensive laws, watch adjacent state statutes: Illinois BIPA (biometrics, private right of action, heavy class-action exposure), Washington My Health My Data (broad consumer health data, private right of action), and state minors'/age-appropriate design and AI acts.

## State breach notification laws

**All 50 states**, DC, and the US territories have breach notification statutes — a separate, older layer that applies regardless of comprehensive-law coverage. There is no federal general breach notification law (sectoral rules exist: HIPAA, GLBA, SEC — see [sec-cyber-disclosure.md](sec-cyber-disclosure.md)).

Common structure (each element varies by state — a multi-state incident requires per-state analysis):

- **Covered PI definition** — typically name plus SSN, driver's license/state ID number, or financial account number with access credentials. Many states have expanded to include medical information, health insurance IDs, biometric data, and username/email plus password or security answers.
- **Trigger** — unauthorized acquisition (some states: access) of unencrypted computerized PI. **Encryption safe harbor** in most states — no notice if data was encrypted and the key was not compromised.
- **Risk-of-harm analysis** — many states allow no notification where investigation concludes no reasonable likelihood of harm; some require documenting that determination in writing and/or notifying the AG of it.
- **Timing** — most commonly "in the most expedient time possible and without unreasonable delay"; a substantial minority impose outer bounds, **typically 30–60 days** (e.g., 30 days in some states, 45 or 60 in others — verify per state). Law-enforcement delay provisions are universal.
- **Regulator notice** — many states require notifying the AG (and sometimes state police or consumer agencies), often above a resident-count threshold (commonly 500 or 1,000 residents; a few states require AG notice for any notified breach).
- **Consumer reporting agencies** — notice to CRAs typically required above ~1,000 affected residents.
- **Substitute notice** — email/website/media notice permitted where cost or affected population exceeds thresholds or contact information is insufficient.
- **Third-party/vendor duty** — entities *maintaining* data for another must notify the data owner, who owes the consumer notice; contractually pin vendor notification to a fixed short window.

Several states also impose standalone **data security** and **disposal** duties (e.g., Massachusetts 201 CMR 17.00 requires a written information security program (WISP) for holders of Massachusetts residents' PI; New York's SHIELD Act imposes reasonable-safeguards requirements tied to its breach law). New York DFS 23 NYCRR 500 applies to licensed financial services companies — a sectoral regime with its own 72-hour event notification.

For the incident playbook and deadline matrix across all regimes, see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Key obligations for security/GRC teams

1. **Run applicability analysis annually and on business change** — thresholds are volume- and revenue-based, so growth, M&A, or a new marketing tactic can pull you into new states mid-year. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Build once for the strictest applicable state** — in practice: California + the strongest opt-in-consent state you face. A single program honoring GPC, opt-in for sensitive data, correction, and appeals satisfies nearly all states.
3. **Maintain a data inventory with sale/share and sensitive-data flags** — you cannot honor opt-outs or scope assessments without knowing which flows are "sales," "sharing," or targeted advertising. Ad-tech pixels and SDKs are the most common blind spot and the top enforcement theme.
4. **Honor opt-out preference signals technically** — GPC handling must actually suppress downstream sharing, not just set a cookie. Test it; regulators do.
5. **Paper the vendor chain** — service-provider/processor contract terms per statute; without them, routine disclosures become "sales." Fold into [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **Operate data protection assessments** — one template covering targeted ads, sale, sensitive data, and profiling; retain for AG production; track CPPA risk-assessment and cybersecurity-audit rules for California-specific submission/certification duties.
7. **Evidence "reasonable security"** — map your control set to CIS Controls v8 or NIST CSF 2.0 ([../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)); this is both the CCPA §1798.150 defense and the AG-enforcement defense.
8. **Encrypt PI at rest and in transit** — the encryption safe harbor is the single highest-leverage control against 50-state breach notice and California statutory damages.
9. **Pre-build the 50-state breach decision matrix** — per-state PI definitions, deadlines, AG thresholds, and letter templates, refreshed periodically; deadline research during an incident is too late.
10. **Track rights-request SLAs** — 45 days (California and most states), with appeal workflows where required; log volume and timeliness as program metrics ([../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md)).

Related context: [gdpr.md](gdpr.md) for the EU model most state laws borrow from; [hipaa.md](hipaa.md) and [glba-ftc-safeguards.md](glba-ftc-safeguards.md) for the sectoral exemptions these laws carve around.

## Primary sources

- [California AG — CCPA (statute, regulations, enforcement)](https://oag.ca.gov/privacy/ccpa)
- [California Privacy Protection Agency (CPRA regulations)](https://cppa.ca.gov)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
