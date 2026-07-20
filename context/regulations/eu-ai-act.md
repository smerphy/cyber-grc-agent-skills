# EU AI Act (Regulation (EU) 2024/1689)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2024/1689 — directly applicable across the EU |
| Entered into force | 1 August 2024 |
| Applicability | Staged: prohibitions + AI literacy 2 Feb 2025; GPAI obligations 2 Aug 2025; most high-risk and transparency obligations 2 Aug 2026; Annex I embedded high-risk 2 Aug 2027 |
| Model | Risk-based tiers: prohibited, high-risk, transparency-risk, minimal risk; separate regime for general-purpose AI (GPAI) models |
| Key roles | Provider, deployer, importer, distributor, authorised representative — obligations differ sharply by role |
| Extraterritorial reach | Applies to providers placing AI on the EU market wherever established, and where the AI system's **output is used in the EU** |
| Penalties | Up to €35M or 7% of worldwide annual turnover (prohibited practices); €15M / 3% (most other violations); €7.5M / 1% (misleading information); SMEs: lower of the amounts |
| Governance | EU AI Office (GPAI + coordination), European AI Board, national market surveillance authorities and notifying authorities |

## Risk tiers

### Prohibited practices (Art. 5) — applicable since 2 Feb 2025

AI practices banned outright, including:

- Subliminal, manipulative, or deceptive techniques that materially distort behaviour and cause significant harm
- Exploiting vulnerabilities of persons due to age, disability, or social/economic situation
- Social scoring by public or private actors leading to detrimental treatment that is unjustified or disproportionate/decontextualised
- Predicting criminal-offence risk based solely on profiling or personality traits
- Untargeted scraping of facial images from the internet or CCTV to build facial-recognition databases
- Emotion inference in workplaces and education institutions (narrow medical/safety exceptions)
- Biometric categorisation inferring race, political opinions, trade-union membership, religious/philosophical beliefs, sex life, or sexual orientation (law-enforcement carve-outs)
- Real-time remote biometric identification in publicly accessible spaces for law enforcement, subject to narrow, authorised exceptions

Screen for these first in any AI inventory — no controls remediate a prohibited practice; the only options are cease or redesign.

### High-risk AI systems (Art. 6 + Annexes I and III)

Two routes into high-risk classification:

1. **Annex I (product route):** the AI system is a safety component of, or is itself, a product covered by listed EU harmonisation legislation requiring third-party conformity assessment — machinery, toys, lifts, radio equipment, medical devices and IVDs, civil aviation, motor vehicles, marine equipment, rail, and others. Obligations apply from **2 Aug 2027**.
2. **Annex III (use-case route):** listed use cases, including — biometric identification/categorisation and emotion recognition (where not prohibited); safety components in management of critical infrastructure (digital infrastructure, road traffic, water, gas, heating, electricity); education and vocational training (admission, evaluation, exam monitoring); **employment and worker management** (recruitment, screening, promotion/termination decisions, task allocation, monitoring); access to essential private and public services (public-benefit eligibility, **creditworthiness/credit scoring**, **life and health insurance risk assessment and pricing**, emergency-call triage); law enforcement; migration, asylum and border control; administration of justice and democratic processes.

**Art. 6(3) filter:** an Annex III system is not high-risk if it performs only narrow procedural tasks, improves the result of a previously completed human activity, detects decision patterns without replacing human assessment, or does purely preparatory work — but the provider must document that assessment and the system must still be registered. Profiling of natural persons always stays high-risk.

### Transparency-risk (Art. 50) — from 2 Aug 2026

Regardless of other tiers:

- Inform people they are interacting with an AI system (chatbots) unless obvious
- Mark synthetic audio/image/video/text content as artificially generated or manipulated, in machine-readable form where feasible (providers)
- Disclose deepfakes and AI-generated text published to inform the public on matters of public interest (deployers, with editorial-control exceptions)
- Inform people exposed to emotion recognition or biometric categorisation systems

### Minimal risk

Everything else — no new obligations, though voluntary codes of conduct are encouraged, and the AI-literacy duty (Art. 4: providers and deployers ensure adequate AI literacy of staff operating AI, applicable since 2 Feb 2025) applies to everyone.

## Applicability timeline

| Date | What applies |
|---|---|
| 1 Aug 2024 | Entry into force |
| 2 Feb 2025 | Prohibited practices (Art. 5); AI literacy (Art. 4) |
| 2 Aug 2025 | GPAI model obligations; governance structures (AI Office, Board); notified-body provisions; penalties provisions |
| 2 Aug 2026 | General applicability: Annex III high-risk obligations, Art. 50 transparency, most remaining provisions |
| 2 Aug 2027 | Annex I (product-embedded) high-risk obligations; compliance deadline for GPAI models placed on the market before 2 Aug 2025 |

Legacy note: high-risk systems already on the market before the relevant date are generally caught only on significant design change (public-authority systems have a longer, specific catch-up path).

## Roles and the obligation split

| Role | Definition | Core obligations |
|---|---|---|
| **Provider** | Develops (or has developed) an AI system/GPAI model and places it on the market or into service under its own name/trademark | Full high-risk compliance stack: Arts. 8–15 requirements, QMS, conformity assessment, CE marking, registration, post-market monitoring, serious-incident reporting, corrective actions |
| **Deployer** | Uses an AI system under its authority in a professional context | Use per instructions; assign competent human oversight; ensure input-data relevance where it controls inputs; monitor operation; retain automatically generated logs under its control (minimum six months, subject to other law); inform workers/representatives before workplace use; certain deployers: FRIA (Art. 27) |
| **Importer / Distributor** | Brings a third-country system to the EU market / makes it available | Verify conformity assessment, documentation, CE marking; withhold non-conforming systems; cooperate with authorities |
| **Authorised representative** | EU-mandated representative of a non-EU provider | Holds documentation, cooperates with authorities |

**Role migration trap:** a deployer, importer, or distributor becomes a *provider* (with the full provider stack) if it puts its name/trademark on a high-risk system, substantially modifies one, or repurposes a non-high-risk system into a high-risk use. This is the single most common misclassification in enterprise AI governance — organizations fine-tuning or white-labelling vendor models often assume deployer-only status incorrectly.

Most enterprises are primarily **deployers**; a company building customer-facing AI products is a **provider** for those products and a deployer of its internal tools. Classify per system, not per organization.

## High-risk requirements (providers, Arts. 8–17 and related)

1. **Risk management system** (Art. 9) — continuous, iterative, across the lifecycle: identify/evaluate foreseeable risks to health, safety, fundamental rights; targeted mitigations; testing including against misuse that is reasonably foreseeable.
2. **Data and data governance** (Art. 10) — training/validation/test data relevant, sufficiently representative, and to the best extent possible error-free and complete for the intended purpose; examination for biases; documented provenance and preparation.
3. **Technical documentation** (Art. 11 + Annex IV) — pre-market, kept current; demonstrates compliance.
4. **Record-keeping/logging** (Art. 12) — automatic event logging enabling traceability appropriate to the system's purpose.
5. **Transparency to deployers** (Art. 13) — instructions for use: capabilities, limitations, accuracy metrics, foreseeable misuse, oversight measures, expected lifetime and maintenance.
6. **Human oversight** (Art. 14) — designed for effective oversight; overseers can understand, monitor, interpret, decide not to use, intervene, or stop; heightened rules for remote biometric identification.
7. **Accuracy, robustness, cybersecurity** (Art. 15) — declared accuracy levels; resilience to errors and to attacks including data poisoning, model poisoning, adversarial examples/model evasion, and confidentiality attacks; feedback-loop mitigation for continuously learning systems.
8. **Quality management system** (Art. 17) — documented policies/procedures covering design, testing, data management, post-market monitoring, incident reporting, communication with authorities.
9. **Conformity assessment** (Art. 43) — mostly internal control against harmonised standards; notified-body involvement for certain biometric systems and where standards are not applied; new assessment on substantial modification.
10. **Registration** (Art. 49) — providers register high-risk systems in the EU database before market placement; public-authority deployers register their use.
11. **Post-market monitoring and serious-incident reporting** (Arts. 72–73) — monitoring plan; report serious incidents to market surveillance authorities on short statutory clocks (tiered by severity — verify exact day-counts in Art. 73 when building the playbook).

## GPAI models (Chapter V)

- **All GPAI providers** (Art. 53): maintain technical documentation; provide information/documentation to downstream providers integrating the model; implement a copyright-compliance policy (including TDM opt-out respect); publish a sufficiently detailed summary of training content. Free open-source models get partial exemptions unless systemic-risk class.
- **Systemic-risk GPAI** (Arts. 51–52, 55): presumed when cumulative training compute exceeds **10^25 FLOPs**, or on Commission designation. Additional duties: state-of-the-art model evaluations including adversarial testing, assessment and mitigation of systemic risks at Union level, serious-incident tracking and reporting to the AI Office, and adequate cybersecurity protection of the model and infrastructure.
- The **GPAI Code of Practice** provides a presumption-of-conformity route pending harmonised standards; supervision sits with the **AI Office**, not national authorities.

## Penalties (Arts. 99, 101)

| Violation | Ceiling |
|---|---|
| Prohibited practices (Art. 5) | €35,000,000 or 7% of total worldwide annual turnover, whichever is higher |
| Non-compliance with most other obligations (provider, deployer, importer, distributor, notified-body duties) | €15,000,000 or 3% |
| Supplying incorrect, incomplete, or misleading information to authorities | €7,500,000 or 1% |
| GPAI provider violations (Commission-imposed) | €15,000,000 or 3% |

For SMEs and startups, each ceiling is the **lower** of the percentage or fixed amount. EU institutions face separate (lower) fines via the EDPS.

## Key obligations for security/GRC teams

1. **Build and maintain an AI system inventory** with per-system classification: prohibited screen, high-risk route (Annex I vs III, Art. 6(3) filter), transparency duties, GPAI dependencies, and role determination (provider vs deployer). See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
2. **Watch the role-migration trap** on fine-tuning, white-labelling, and repurposing — trigger re-classification in change management and procurement gates.
3. **Deployer baseline for high-risk systems**: assigned trained human oversight, log retention (≥6 months), input-data controls, operational monitoring, worker notification, vendor instructions incorporated into SOPs.
4. **FRIA where required** (Art. 27): public-law bodies and private deployers of Annex III credit-scoring and life/health-insurance-pricing systems complete a fundamental rights impact assessment before first use and notify the market surveillance authority. Reuse DPIA machinery — see below and [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
5. **Fold Art. 15 into security architecture**: adversarial-ML threats (poisoning, evasion, extraction) belong in threat models, pen-test scope, and vendor security questionnaires — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **AI literacy program** with role-based depth and attendance evidence — already in force.
7. **Track harmonised standards, codes of practice, and AI Office guidance** — conformity presumptions and interpretation are still solidifying; see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
8. Where building an AI management system, ISO/IEC 42001 provides a certifiable structure that can host AI Act obligations alongside an ISO 27001 ISMS ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md)).

## Interplay

- **GDPR:** the AI Act applies *without prejudice* to GDPR — a lawful basis, purpose limitation, and data-subject rights still govern any personal data in training or operation. Where a high-risk AI system involves personal data, a **DPIA (GDPR Art. 35)** is typically required *and* certain deployers also owe a **FRIA (AI Act Art. 27)**; the FRIA may build on and complement the DPIA rather than duplicate it — run them as one assessment with two outputs. AI Act Art. 10(5) permits processing special-category data strictly for bias detection/correction under safeguards. Automated-decision rights under GDPR Art. 22 operate alongside AI Act human-oversight duties. See [gdpr.md](gdpr.md).
- **NIS2:** an in-scope NIS2 entity deploying AI must cover those systems under its Art. 21 measures (supply-chain, secure development, incident handling); AI Act cybersecurity requirements (Art. 15) are system-level and complement NIS2's org-level program. See [nis2.md](nis2.md).
- **DORA:** financial entities using AI for credit scoring or insurance pricing face Annex III high-risk duties on top of DORA ICT-risk and third-party controls; GPAI vendors may appear in the DORA register of information and, if designated, CTPP oversight. See [dora.md](dora.md).
- **Product law:** for Annex I products, AI Act conformity assessment integrates into the existing sectoral CE process (one assessment, extended scope), which is why those obligations start in 2027.

## Primary sources

- [Regulation (EU) 2024/1689 (AI Act) — official text on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
