# NIST AI Risk Management Framework (AI RMF 1.0, NIST AI 100-1) and the Generative AI Profile (NIST AI 600-1)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument / citation | NIST AI 100-1, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, January 2023 (DOI 10.6028/NIST.AI.100-1). Companion cross-sectoral profile: NIST AI 600-1, *Generative Artificial Intelligence Profile*, July 2024 (DOI 10.6028/NIST.AI.600-1) |
| Publisher | NIST Information Technology Laboratory (US Department of Commerce), developed with public and private sector input |
| Legal basis | Directed by the National Artificial Intelligence Initiative Act of 2020 (P.L. 116-283) to produce a **voluntary** resource — not a regulation, no rulemaking authority behind it |
| Status | AI RMF 1.0 released 26 January 2023 and still the current edition. NIST states it "is being revised as part of the White House AI Action Plan" (as of September 2026 no revised edition published) |
| Who it covers | Any organisation designing, developing, deploying, evaluating or acquiring AI systems. Intended to be voluntary, rights-preserving, non-sector-specific and use-case agnostic |
| Structure | 4 functions (Govern, Map, Measure, Manage) → 19 categories → 72 subcategories, plus 7 trustworthiness characteristics and a Profile mechanism |
| Enforcement | None directly. Bite comes indirectly: procurement terms, sector regulator expectations, US state AI statutes that credit recognised frameworks (verify per statute), and contractual commitments |
| Certifiable? | **No.** No certification scheme, no accredited assessor body, no conformity assessment. Self-assessment or contractual attestation only. ISO/IEC 42001 is the certifiable counterpart |
| Cost | Free. Framework, Playbook, crosswalks and profiles published at no charge via NIST and the Trustworthy & Responsible AI Resource Center (AIRC) |
| Relationship to neighbours | Sibling to NIST CSF 2.0 and the NIST Privacy Framework (same outcome-and-profile architecture); crosswalks to ISO/IEC 42001 and ISO/IEC 23894 are hosted on NIST's AI Resource Center, largely community-submitted and expressly not NIST endorsements; a common evidence base for EU AI Act risk-management-system duties without satisfying them |

## What it is

The AI RMF is an outcome-based risk management framework for AI, not a control catalogue and not a compliance standard. It describes *what good looks like* (subcategories phrased as achieved outcomes, e.g. "Mechanisms are in place to inventory AI systems") and leaves the *how* to a separate, continuously updated **AI RMF Playbook** hosted on the AIRC. NIST built it through a consensus-driven open process — a Request for Information, two public drafts, and multiple workshops — and published it on 26 January 2023.

Architecturally it is the AI-domain twin of the NIST Cybersecurity Framework: a Core of functions/categories/subcategories, plus Profiles that tailor those outcomes to a setting. A **use-case profile** applies the Core to a specific application; a **cross-sectoral profile** covers a technology or process used across sectors (generative AI, LLMs, cloud services, acquisition); **temporal profiles** are Current and Target states whose comparison yields the gap list and action plan. NIST deliberately prescribes no profile template.

The framework is a living document on a two-number version scheme (1.0, 1.1, …). NIST originally committed to a formal community review "no later than 2028"; that timetable has been overtaken by the July 2025 AI Action Plan directive to revise it (see Timeline and status). The Playbook is updated more often, with comments integrated semi-annually.

## Who it covers / Scope

- **Applicability is self-selected.** Nothing triggers the AI RMF by threshold, revenue, headcount or sector. It applies where an organisation adopts it, a customer requires it, or a regulator/statute treats it as a recognised framework.
- **AI actors, not just "AI companies."** The framework allocates outcomes across lifecycle roles — AI Design, AI Development, Deployment, Operation and Monitoring, TEVV (test, evaluation, verification and validation), and impacted-community/third-party actors. Deployers who buy AI rather than build it are squarely in scope, principally through Govern, Map and the third-party subcategories (MANAGE 3.1–3.2 cover third-party resources and pre-trained models).
- **No extraterritorial reach** of its own. Non-US organisations use it voluntarily, often to demonstrate maturity to US customers or as the risk-management substrate for an ISO/IEC 42001 management system.
- **Federal agencies** are governed instead by OMB M-25-21 (3 April 2025), which rescinds and replaces M-24-10, defines **High-Impact AI** (AI whose output is a principal basis for decisions with legal, material, binding or significant effect on civil rights/liberties/privacy; access to education, housing, insurance, credit or employment; access to critical government services; human health and safety; critical infrastructure or public safety; or strategic assets), and imposes minimum practices for it (Section 4(b)), Chief AI Officer designation within 60 days, and further 180-day duties. M-25-21 does not itself mandate the AI RMF by name.

## Structure and requirements

### The Core — 4 functions, 19 categories, 72 subcategories

| Function | Categories | Subcategories | What it demands |
|---|---|---|---|
| **GOVERN** | 6 (GOVERN 1–6) | 19 | Cross-cutting and infused through the other three. Legal/regulatory requirements understood (GV 1.1); trustworthiness characteristics embedded in policy (GV 1.2); risk tolerance set (GV 1.3); AI system **inventory** mechanisms (GV 1.6); decommissioning processes (GV 1.7); roles, training and executive accountability (GV 2.1–2.3); diverse teams informing risk decisions and defined roles for human-AI configuration and oversight (GV 3.1-3.2, under the GOVERN 3 workforce diversity/equity/inclusion/accessibility category); third-party/supply-chain policy (GV 6.1) and contingency for third-party failure (GV 6.2) |
| **MAP** | 5 (MAP 1–5) | 18 | Establish context before building or buying: intended purpose and context of use (MP 1.1), interdisciplinary teams (MP 1.2), risk tolerances (MP 1.5), system requirements (MP 1.6), knowledge limits and TEVV considerations (MP 2.2–2.3), benefits and non-monetary costs (MP 3.1–3.2), human-oversight processes (MP 3.5), legal risk mapping (MP 4.1), and impact characterisation with external engagement (MP 5.1–5.2) |
| **MEASURE** | 4 (MEASURE 1–4) | 22 | The largest function. Metrics selection and independent internal review (MS 1.1–1.3); the MS 2.x battery — test sets and tooling, human-subject evaluations, deployment-condition validity, **safety** (2.6), **security and resilience** (2.7), transparency/accountability (2.8), explainability (2.9), **privacy** (2.10), **fairness and bias** (2.11), environmental impact (2.12), and effectiveness of the TEVV metrics themselves (2.13); mechanisms to track identified, unanticipated and emergent risks over time, including where measurement techniques do not yet exist (MS 3.x); and feedback on the efficacy of measurement itself, validated with domain experts and relevant AI actors (MS 4.x) |
| **MANAGE** | 4 (MANAGE 1–4) | 13 | Go/no-go determination — does the system achieve its intended purposes and stated objectives, and should development or deployment proceed (MG 1.1); prioritisation and treatment (MG 1.2–1.3); explicit **residual risk** documentation (MG 1.4); resourcing against non-AI alternatives, sustaining deployed value, recovery from newly identified risk, and assigned mechanisms to supersede, disengage or deactivate a system (MG 2.1–2.4); third-party and pre-trained-model risk (MG 3.1–3.2); post-deployment monitoring plans, continual improvement, and **incident and error communication** to relevant actors (MG 4.1–4.3) |

### The 7 trustworthiness characteristics

Valid and Reliable (the base condition for all others) · Safe · Secure and Resilient · Accountable and Transparent (cross-cutting, applying to every other characteristic) · Explainable and Interpretable · Privacy-Enhanced · Fair – with Harmful Bias Managed. Trade-offs between them are expected and are to be documented, not resolved by default.

### Sequencing

Functions are not a waterfall. NIST's guidance: institute GOVERN outcomes first, then most users start at MAP and continue to MEASURE or MANAGE, iterating and cross-referencing. Organisations may adopt a subset of categories/subcategories.

### The Generative AI Profile (NIST AI 600-1, July 2024)

A **cross-sectoral profile** issued under section 4.1(a)(i)(A) of the now-revoked EO 14110. It defines 12 risks unique to or exacerbated by generative AI and maps suggested actions onto AI RMF subcategories.

| # | GAI risk | # | GAI risk |
|---|---|---|---|
| 1 | CBRN Information or Capabilities | 7 | Human-AI Configuration |
| 2 | Confabulation | 8 | Information Integrity |
| 3 | Dangerous, Violent, or Hateful Content | 9 | Information Security |
| 4 | Data Privacy | 10 | Intellectual Property |
| 5 | Environmental Impacts | 11 | Obscene, Degrading, and/or Abusive Content |
| 6 | Harmful Bias or Homogenization | 12 | Value Chain and Component Integration |

Section 3 carries **212 distinct suggested-action IDs** (GV-, MP-, MS-, MG- prefixed) spread across 49 AI RMF subcategories — 58 Govern, 39 Map, 72 Measure, 43 Manage — each tagged with the GAI risks and AI actor tasks it addresses. Scope was set by the four priorities of NIST's Generative AI Public Working Group: **Governance, Content Provenance, Pre-deployment Testing, and Incident Disclosure**; other GAI concerns are correspondingly thin. Each risk is also mapped to the trustworthiness characteristics it threatens.

### Adjacent NIST AI publications

| Publication | Date | Use |
|---|---|---|
| NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* | March 2025 | Shared vocabulary for AI attack classes; underpins MEASURE 2.7 evidence and red-team scoping |
| NIST SP 800-218A, *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models* (SSDF Community Profile) | July 2024 | SDLC controls for model builders and fine-tuners |
| SP 800-53 **Control Overlays for Securing AI Systems (COSAiS)** | Concept paper 14 Aug 2025; annotated outline for the predictive-AI use case 8 Jan 2026 (feedback due 13 Feb 2026) | Five planned overlays: adapting/using generative AI assistants, using and fine-tuning predictive AI, single-agent systems, multi-agent systems, and security controls for AI developers. Leverages SP 800-218A, draft NIST AI 800-1 and AI 100-2e2025. No draft overlay published as of September 2026 |
| NIST IR 8596, *Cybersecurity Framework Profile for Artificial Intelligence* (Cyber AI Profile) | Preliminary draft 16 Dec 2025; 45-day comment closed 30 Jan 2026; initial public draft still unpublished as of September 2026 | Applies CSF 2.0 to three focus areas: securing AI systems, conducting AI-enabled cyber defence, thwarting AI-enabled cyberattacks. The draft states the AI RMF mapping waits on the AI RMF revision |

## Assessment, certification and evidence

- **There is no certification.** Any vendor claiming to be "NIST AI RMF certified" is misdescribing a self-assessment. Accept AI RMF alignment as a maturity signal; require ISO/IEC 42001 certification or a SOC 2 examination scoped to AI processes where third-party assurance is genuinely needed.
- **The assessable unit is the subcategory outcome.** Score Current vs Target per subcategory (or per function for board reporting), evidence each with an artefact — model card, impact assessment, TEVV report, evaluation dataset documentation, incident log, decommissioning record — and keep the residual-risk statement (MANAGE 1.4) as the accountable sign-off. See [control-testing](../../skills/control-testing/SKILL.md) and [risk-scoring](../risk-scoring.md).
- **Two-layer scoping works best:** the 72 subcategories once at organisation level (Govern-heavy), then Map/Measure/Manage per AI system via an intake gate. See [ai-system-intake](../../workflows/ai-system-intake.md).
- **Crosswalks.** The AIRC hosts a crosswalk list made up of documents submitted by the AI RMF user community; NIST reviews submissions but states that listing implies no endorsement. The AI RMF → ISO/IEC FDIS 42001 file maps each subcategory to 42001 clauses and Annex B controls but is community-submitted, not NIST-authored. NIST's own ISO/IEC 23894 crosswalk (26 January 2023, against the FDIS text) is now marked superseded; the current revised 23894:2023 crosswalk (14 August 2025) is community-submitted and maps at function level only. Mappings are directional and lossy — use them for coverage analysis, not equivalence. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **Common evidence gaps in practice:** no AI system inventory (GV 1.6), no decommissioning path (GV 1.7), no documented risk tolerance (GV 1.3 / MP 1.5), no residual-risk acceptance (MG 1.4), and no route for reporting AI incidents and errors to affected actors (MG 4.3).

## Timeline and status

| Date | Event |
|---|---|
| 2020 | National Artificial Intelligence Initiative Act of 2020 (P.L. 116-283) directs NIST to develop a voluntary AI risk management framework |
| 26 Jan 2023 | AI RMF 1.0 (NIST AI 100-1) published, with the Playbook, Roadmap and initial crosswalks |
| 30 Mar 2023 | Trustworthy and Responsible AI Resource Center (AIRC) launched |
| 30 Oct 2023 | EO 14110 (Safe, Secure, and Trustworthy AI) directs the GenAI companion profile |
| Jul 2024 | SP 800-218A published (25 Jul 2024 editorial approval); NIST AI 600-1 GenAI Profile approved 25 Jul 2024 and released 26 Jul 2024 |
| 20 Jan 2025 | **EO 14148** (Initial Rescissions of Harmful Executive Orders and Actions) revokes EO 14110 at section 2(ggg) |
| 23 Jan 2025 | **EO 14179** (Removing Barriers to American Leadership in AI) orders an AI action plan within 180 days; agencies must review and, as appropriate, suspend, revise or rescind actions taken under the revoked EO 14110 |
| Mar 2025 | NIST AI 100-2e2025 adversarial ML taxonomy published |
| 3 Apr 2025 | OMB M-25-21 rescinds and replaces M-24-10 for federal agency AI use |
| 2025 | NIST's AI Safety Institute becomes the **Center for AI Standards and Innovation (CAISI)** — the agency's AI Safety Institute address now redirects to the CAISI page — serving as industry's primary US-government point of contact for AI testing and collaborative research; the July 2025 AI Action Plan assigns it frontier-model evaluation work. Exact renaming date not stated on the NIST page (verify) |
| 23 Jul 2025 | **America's AI Action Plan** directs Commerce/NIST to "revise the NIST AI Risk Management Framework to eliminate references to misinformation, Diversity, Equity, and Inclusion, and climate change" |
| 14 Aug 2025 | COSAiS concept paper opened for comment |
| 11 Dec 2025 | **EO 14365** (Ensuring a National Policy Framework for Artificial Intelligence) directs an effort to preempt conflicting state AI laws — relevant to any reliance on state safe-harbour provisions that credit recognised AI frameworks |
| 16 Dec 2025 | Cyber AI Profile (NIST IR 8596) preliminary draft; comments to 30 Jan 2026; workshop 14 Jan 2026 |
| 8 Jan 2026 | COSAiS annotated outline (predictive AI use case) released for discussion |
| 7 Apr 2026 | NIST releases a concept note for an **AI RMF Profile on Trustworthy AI in Critical Infrastructure** and opens a Community of Interest (project page updated 17 Jul 2026) |
| **As of Sept 2026** | AI RMF 1.0 remains the published edition; NIST states it is under revision per the AI Action Plan. No revised text, draft or comment period for the revision has been published on the NIST AI RMF page. Plan for content change — particularly in MEASURE 2.11/2.12 and Information Integrity material — and do not hard-code subcategory text into policies |

## Key obligations for security/GRC teams

1. **Stand up an AI system inventory before anything else** (GOVERN 1.6), covering built, bought, embedded and fine-tuned systems, with owner, purpose, data classes, model provenance and deployment status. Without it, Map/Measure/Manage cannot be scoped. See [ai-governance](../../skills/ai-governance/SKILL.md) and [ai-system-intake](../../workflows/ai-system-intake.md).
2. **Write a documented AI risk tolerance** (GOVERN 1.3, MAP 1.5) and the use classes you will not permit. Decisions without it become ad hoc and unauditable. See [policy-authoring](../../skills/policy-authoring/SKILL.md).
3. **Run intake as a MAP gate**: purpose, context of use, knowledge limits, benefits and non-monetary costs, human oversight design, legal risk. Record impacts before procurement is signed, not after. See [risk-assessment](../../skills/risk-assessment/SKILL.md).
4. **Treat MEASURE 2.7 as your existing security programme applied to AI** — access control, logging, secrets, supply chain — extended with adversarial-ML testing framed by AI 100-2e2025 (evasion, poisoning, extraction, prompt injection, abuse).
5. **Apply the 12 GenAI risks from AI 600-1 as the standing risk taxonomy** for any LLM or foundation-model use, and pull suggested actions by subcategory rather than trying to adopt all 212.
6. **Push third-party duties into contracts** (GOVERN 6.1–6.2, MANAGE 3.1–3.2): model and training-data provenance, evaluation results, change/retraining notification, incident notification, and a contingency plan for provider failure or model withdrawal. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
7. **Close MANAGE 4.3 explicitly** — define what counts as an AI incident, who is told, in what window, and how it joins the security incident process and any regulatory clock. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).
8. **Document residual risk and the named acceptor** for every deployed system (MANAGE 1.4), with re-review triggers on model change, data drift or new use. See [risk-register-guide](../../templates/risk-register-guide.md).
9. **Report by function, not by subcategory**, to executives: four Current/Target scores plus the top three gaps beats a 72-row heat map. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
10. **Track the pending revision and the adjacent drafts** (COSAiS overlays, IR 8596 Cyber AI Profile, the critical infrastructure profile) on your horizon-scanning calendar. See [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

| Neighbour | Relationship |
|---|---|
| [EU AI Act](../regulations/eu-ai-act.md) | The AI RMF is voluntary practice; the AI Act is binding law with penalties. AI RMF Map/Measure/Manage evidence substantially feeds the Act's risk-management-system, data-governance, logging and post-market-monitoring duties, but does not satisfy them — the Act's conformity assessment has no AI RMF equivalent |
| ISO/IEC 42001:2023 | The certifiable AI management system. AI RMF gives the risk-assessment substance, 42001 gives the auditable management wrapper (management-system clauses plus its annexes). A subcategory-level crosswalk to 42001 clauses and Annex B controls is hosted on the AIRC but was submitted by a third party, not authored by NIST. A common pattern: adopt the AI RMF first, certify to 42001 later. Full 42001 text is paywalled, so read the crosswalk rather than assuming clause coverage |
| ISO/IEC 23894:2023 | ISO's AI risk-management *guidance* (non-certifiable). NIST crosswalked the FDIS text to the AI RMF in January 2023; that file is now marked superseded and a revised function-level crosswalk (August 2025) is community-submitted |
| [NIST CSF 2.0](nist-csf-2.md) | Same outcome/profile architecture and a shared Govern function; the forthcoming Cyber AI Profile (IR 8596) is the intended bridge, applying CSF 2.0 to AI-related cyber risk; its December 2025 draft defers the AI RMF mapping until the AI RMF revision lands |
| [NIST SP 800-53](nist-800-53.md) | Provides the control depth the AI RMF deliberately lacks; COSAiS will publish AI-specific overlays tailoring 800-53 controls per AI use case |
| [ISO/IEC 27001:2022](iso-27001-2022.md) | Information security management for the systems AI runs on. Neither covers the other: an ISMS says nothing about bias, confabulation or model provenance |
| [US state AI legislation](../regulations/us-state-ai-laws.md) | Several state AI statutes reference recognised AI risk frameworks (including the AI RMF and its GenAI Profile) in affirmative-defence or safe-harbour provisions — check the specific statute's wording and version pinning before relying on it, and note that EO 14365 (December 2025) directs a federal effort to preempt conflicting state AI laws (verify) |
| Terminology | AI-specific terms used above (TEVV, confabulation, residual risk, AI actor) — see [glossary](../glossary.md) |

## Primary sources

- NIST AI 100-1, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, January 2023 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf (publisher document, fetched)
- NIST AI 600-1, *AI RMF: Generative Artificial Intelligence Profile*, July 2024 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (publisher document, fetched)
- NIST AI 100-2e2025, *Adversarial Machine Learning*, March 2025 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf (publisher document, fetched)
- NIST SP 800-218A, *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models*, July 2024 — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf (publisher document, fetched)
- NIST, AI Risk Management Framework programme page — https://www.nist.gov/itl/ai-risk-management-framework (publisher page, fetched)
- NIST, AI RMF FAQs — https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-faqs (publisher page, fetched)
- NIST, Crosswalks to the AI RMF — https://www.nist.gov/itl/ai-risk-management-framework/crosswalks-nist-artificial-intelligence-risk-management-framework (publisher page, fetched)
- NIST AIRC, AI RMF Playbook — https://airc.nist.gov/airmf-resources/playbook/ (publisher page, fetched)
- NIST AIRC, crosswalk document list (community submissions; NIST states listing implies no endorsement) — https://airc.nist.gov/airmf-resources/crosswalks/ (publisher page, fetched)
- AI RMF → ISO/IEC FDIS 42001 crosswalk hosted on the AIRC — https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf (community-submitted document, fetched)
- NIST, AI RMF 1.0 → ISO/IEC FDIS 23894 crosswalk, 26 January 2023 (superseded) — https://www.nist.gov/system/files/documents/2023/01/26/crosswalk_AI_RMF_1_0_ISO_IEC_23894.pdf (publisher document, link checked)
- Revised ISO/IEC 23894:2023 ↔ AI RMF crosswalk, 14 August 2025 — https://airc.nist.gov/documents/3/ai-2025-00109_revised_ISO_IEC_23894_Crosswalk_to_the_NIST_AI_RMF.pdf (community-submitted document, fetched)
- NIST CSRC, SP 800-53 Control Overlays for Securing AI Systems (COSAiS) project — https://csrc.nist.gov/projects/cosais (publisher page, fetched)
- NIST IR 8596 (Initial Preliminary Draft), *Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)*, 16 December 2025 — https://csrc.nist.gov/pubs/ir/8596/iprd (publisher page, fetched)
- NIST, *Draft NIST Guidelines Rethink Cybersecurity for the AI Era*, 16 December 2025 — https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era (publisher page, fetched)
- NIST, Concept Note: AI RMF Profile on Trustworthy AI in Critical Infrastructure — https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure (publisher page, fetched)
- NIST, Center for AI Standards and Innovation — https://www.nist.gov/caisi (publisher page, fetched)
- Executive Order 14148, *Initial Rescissions of Harmful Executive Orders and Actions*, 20 January 2025 (revokes EO 14110 at section 2(ggg)) — https://www.federalregister.gov/documents/2025/01/28/2025-01901/initial-rescissions-of-harmful-executive-orders-and-actions (legal text, fetched)
- Executive Order 14179, *Removing Barriers to American Leadership in Artificial Intelligence*, 23 January 2025 — https://www.federalregister.gov/documents/2025/01/31/2025-02172/removing-barriers-to-american-leadership-in-artificial-intelligence (legal text, fetched)
- Executive Order 14365, *Ensuring a National Policy Framework for Artificial Intelligence*, signed 11 December 2025 (90 FR 58499) — https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence (legal text; full text read at https://www.govinfo.gov/content/pkg/FR-2025-12-16/html/2025-23092.htm)
- *Winning the Race: America's AI Action Plan*, July 2025 — https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf (policy document, fetched)
- OMB M-25-21, *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust*, 3 April 2025 — https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf (regulator guidance, fetched)
- ISO/IEC 42001:2023 and ISO/IEC 23894:2023 themselves are **paywalled** and were not read; statements about them rest on the crosswalk documents above and on the standards' published titles.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
