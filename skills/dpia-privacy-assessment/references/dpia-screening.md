# DPIA Screening Criteria in Depth

Determines whether a Data Protection Impact Assessment is legally required under GDPR Art. 35, and documents the decision either way. Also covers analogous triggers under other regimes. Use during Step 1 of the DPIA skill procedure.

## Legal structure of the requirement

- **Art. 35(1)** — general rule: a DPIA is required where processing, "in particular using new technologies," is **likely to result in a high risk** to the rights and freedoms of natural persons, taking into account the nature, scope, context and purposes of the processing. One DPIA may cover a set of similar processing operations presenting similar high risks.
- **Art. 35(3)** — three cases where a DPIA is always required:
  - **(a)** systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions are based that produce **legal effects** or **similarly significantly affect** the person;
  - **(b)** **large-scale** processing of special categories of data (Art. 9(1)) or of personal data relating to criminal convictions and offences (Art. 10);
  - **(c)** systematic monitoring of a **publicly accessible area** on a large scale.
- **Art. 35(4)/(5)** — each supervisory authority publishes a list of processing operations **requiring** a DPIA (mandatory to consult for the relevant member state) and may publish a list of operations **exempt** from the requirement. Check the lists of every authority whose jurisdiction the processing touches; national lists commonly add items such as employee monitoring, genetic/biometric data, and data matching.
- **Art. 35(10)** — a DPIA is not required where processing under Art. 6(1)(c) or (e) has a legal basis in EU or member-state law, that law regulates the specific operation, and a DPIA was already carried out as part of adopting that legal basis (unless the member state says otherwise).
- **Art. 35(11)** — review the DPIA when there is a change in the risk represented by the processing.

A DPIA is also not required where the processing is not "likely to result in a high risk," where a materially identical processing operation has already been assessed, or (for pre-2018 processing) where nothing has changed since — though re-assessment on change is still mandatory.

## The nine WP248 criteria

WP248 rev.01 (Article 29 Working Party guidelines on DPIA, endorsed by the EDPB) provides nine criteria for judging "likely high risk." **Rule of thumb: processing meeting two or more criteria requires a DPIA. One criterion can be enough where it clearly creates high risk. Meeting none, a documented decision not to conduct a DPIA is defensible.**

### 1. Evaluation or scoring
Profiling and predicting, especially concerning work performance, economic situation, health, personal preferences or interests, reliability or behavior, location or movements.

- **Triggers:** credit scoring; insurance risk pricing from behavioral data; marketing propensity models building behavioral profiles; fraud-risk scoring of customers; an AI resume-screening tool ranking candidates.
- **Does not trigger by itself:** a static customer list segmented only by product purchased, with no prediction or inference about the person.

### 2. Automated decision-making with legal or similarly significant effect
Processing aimed at making decisions about people that produce legal effects or similarly significantly affect them (overlaps Art. 22).

- **Triggers:** automated loan approval/decline; automated benefit-eligibility decisions; algorithmic shift allocation materially affecting income; automated account termination.
- **Does not trigger:** automation that only queues items for a genuinely empowered human decision-maker (but watch for rubber-stamping — a human who approves 99.9% of machine recommendations is not meaningful review, and the criterion is met in substance).

### 3. Systematic monitoring
Observation, monitoring or control of data subjects, including data collected through networks or systematic monitoring of publicly accessible areas — situations where people may not know who collects their data or how it is used, and cannot avoid the processing.

- **Triggers:** CCTV of a public-facing space with analytics; employee monitoring (keystroke, screen, productivity, email scanning); telematics tracking of drivers; cross-site behavioral tracking.
- **Does not trigger:** a single access-controlled server-room camera; ordinary web-server logs retained briefly for security.

### 4. Sensitive data or data of a highly personal nature
Art. 9 special categories and Art. 10 criminal-offence data, but also data that is highly personal without being "special": location data, financial data, electronic communications content, official identifiers, and generally data whose breach would obviously harm daily life.

- **Triggers:** health records; biometric templates used for identification; precise geolocation history; bank transaction data; private message content.
- **Does not trigger by itself:** business contact details; name and email for a newsletter.

### 5. Data processed on a large scale
GDPR does not define "large scale." WP248 factors: (a) number or proportion of data subjects relative to the relevant population; (b) volume and range of data items; (c) duration or permanence of processing; (d) geographical extent. Recital 91 excludes processing of patient/client data by an **individual** physician or lawyer from "large scale."

- **Triggers:** a hospital chain's patient data; a national retailer's loyalty program; a SaaS platform processing data of millions of end users.
- **Does not trigger:** a single practitioner's client files; a 40-person company's own HR records (though other criteria — e.g., monitoring or vulnerable subjects — may still apply to employee data).

### 6. Matching or combining datasets
Combining data from two or more operations performed for different purposes and/or by different controllers, in a way exceeding the data subject's reasonable expectations.

- **Triggers:** enriching CRM records with purchased third-party data; joining loyalty-card purchases with location data; identity resolution across acquired companies' customer bases.
- **Does not trigger:** joining two tables inside one system serving the single purpose the data was collected for.

### 7. Data concerning vulnerable data subjects
Power imbalance means subjects may be unable to easily consent to or oppose the processing. Includes children, employees (vis-à-vis their employer), patients, the elderly, asylum seekers, people with mental illness, and any case of clear controller/subject imbalance.

- **Triggers:** an ed-tech product for schoolchildren; any non-trivial employee monitoring; a care-home resident management system.
- **Does not trigger by itself:** B2B contact data of professionals acting in a business capacity.

### 8. Innovative use or applying new technological or organisational solutions
Novel tech means the personal and social consequences are not yet well understood. Explicitly flagged in Art. 35(1) ("in particular using new technologies") and Recitals 89/91.

- **Triggers:** deploying an LLM over customer data; combined fingerprint-and-face access control; IoT sensors inferring behavior; emotion-inference features. AI systems almost always meet this criterion — run this skill alongside the AI governance skill.
- **Does not trigger:** mature, well-understood tech used conventionally (a standard relational CRM).

### 9. Processing that prevents data subjects from exercising a right or using a service or contract
Processing that conditions access to a service or contract, or screens people in/out.

- **Triggers:** credit-reference checks before granting a loan or tenancy; background screening before hiring; fraud blocklists that deny service.
- **Does not trigger:** optional personalization a user can decline without losing the service.

## Screening worked examples

| Scenario | Criteria met | DPIA? |
|---|---|---|
| Hospital deploys new EHR system | 4 (health), 5 (large scale), 7 (patients) | Yes — also Art. 35(3)(b) |
| Employer rolls out productivity-monitoring agent on laptops | 3 (monitoring), 7 (employees), often 1 (scoring) | Yes |
| Retailer adds AI chatbot answering questions using customer order history | 8 (new tech), possibly 1, possibly 6 | Yes (two criteria; likely on borderline — do it) |
| City installs ANPR cameras on public roads | 3 + Art. 35(3)(c) | Yes |
| Fintech launches automated creditworthiness scoring | 1, 2, 9 + Art. 35(3)(a) | Yes |
| 30-person company migrates its own payroll to a mainstream cloud provider | Possibly 7 (employees) only; no monitoring, no scoring, small scale, mature tech | Generally no — document the negative screening |
| B2B newsletter to opted-in professional contacts | None | No — document it |
| Solo physiotherapist's patient booking system | 4, 7 — but Recital 91 excludes individual practitioners from "large scale" | Generally no, but borderline; check the national Art. 35(4) list |

## Non-GDPR screening triggers (adapt Step 1)

- **UK GDPR:** same Art. 35 structure; the ICO publishes its own mandatory-DPIA list (includes, e.g., innovative technology, denial-of-service decisions, large-scale profiling, biometrics, genetic data, invisible processing, tracking, targeting children).
- **US state laws:** several states require "data protection assessments" for processing presenting a heightened risk of harm — typically targeted advertising, sale of personal data, profiling with legal/significant effects, and processing of sensitive data. California (CPRA) provides for risk assessments via regulation. Details and per-state variation: [../../../context/regulations/us-state-privacy.md](../../../context/regulations/us-state-privacy.md). A GDPR-grade DPIA generally satisfies these with a mapping cover sheet; some states allow a single assessment to cover comparable processing.
- **Other regimes** (LGPD RIPD, PIPL personal information protection impact assessment, etc.): see [../../../context/regulations/other-jurisdictions.md](../../../context/regulations/other-jurisdictions.md).

## Screening record — minimum content

Even a "no DPIA required" outcome must be written down. Record:

1. Processing name, owner, date, screener
2. One-paragraph description of the processing
3. Art. 35(3) checks: (a)/(b)/(c) — met / not met, with one line of evidence each
4. Nine-criteria table: criterion | met? | evidence
5. National mandatory/exempt list check (which lists, result)
6. Decision: DPIA required / not required / voluntary DPIA anyway — and rationale
7. Review trigger: what change would reopen this screening

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
