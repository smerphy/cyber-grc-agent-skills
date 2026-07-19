# Risks to Individuals: Harm Taxonomy and Rating Anchors

The risk section of a DPIA rates risk **to data subjects' rights and freedoms** — not to the organization. This file provides the harm taxonomy, threat-event catalog, and severity/likelihood anchors to make those ratings consistent and defensible. Use during Step 4 of the DPIA skill procedure.

## The framing error to avoid

The single most common DPIA defect is importing enterprise-risk language: "risk of regulatory fine," "reputational damage to the company," "loss of customer trust." These are consequences **for the controller** and belong in the enterprise risk register, not the DPIA. GDPR Recital 75 frames the target correctly: risks of varying likelihood and severity to the rights and freedoms of natural persons, arising from processing that could lead to physical, material or non-material damage.

Test every risk statement: *"Who is harmed?"* If the answer is the organization, move it out. If the answer names no one, rewrite it until it does.

A second, subtler error: assessing only security failures. Harm also arises from processing **working exactly as intended** — a discriminatory scoring model, excessive surveillance, a dark-pattern consent flow. Assess both.

## Harm taxonomy

### Physical harm
- Bodily injury or death enabled by data exposure: location data of a domestic-abuse survivor reaching an abuser; home address of a protected witness leaked; health data errors causing wrong treatment.
- Deterioration of health from stress caused by an incident or by oppressive monitoring.

### Material / financial harm
- Direct financial loss: fraud, drained accounts, ransom demands against individuals.
- Identity theft and its long tail: fraudulent credit, criminal records in the victim's name, years of remediation effort.
- Loss of employment or income: dismissal following disclosed data; algorithmic shift/pay decisions.
- Denial or worsening of services: credit declined, insurance loaded, tenancy refused, benefits stopped — whether by breach or by the intended operation of a scoring system.
- Costs imposed on the individual: time, legal fees, credit monitoring.

### Discrimination
- Unlawful discrimination on protected characteristics inferred or revealed by the data (health, ethnicity, religion, sexual orientation, trade-union membership).
- Statistical discrimination by proxy: a model using postcode or purchasing behavior that correlates with protected characteristics. This is a harm even when no protected attribute is explicitly processed.
- Exclusion or disadvantage of already-vulnerable groups (children, migrants, people in financial distress).

### Reputational and social harm
- Public embarrassment, humiliation, social exclusion from disclosed private facts (health conditions, sexuality, financial trouble, browsing or purchase history).
- Damage to family life or relationships; harassment and doxxing following disclosure.
- Being falsely represented (wrong records, deepfakes, conflated identities).

### Loss of autonomy and control
- Loss of control over personal data: inability to know who holds it, correct it, or delete it; onward sharing beyond expectations; irreversible disclosure.
- Manipulation: exploiting profiles to steer decisions (dark patterns, exploitative targeting of gambling or credit products at vulnerable people).
- Deprivation of rights: inability to exercise access, rectification, objection; automated decisions with no route to human review; being locked out of a service.

### Chilling effects
- Self-censorship of lawful speech, association, movement, research, or religious practice because people know or suspect they are monitored. This is a rights harm even if no data is ever misused — pervasive workplace monitoring or public-space surveillance harms by existing.
- Deterrence from seeking help: avoiding medical care, counselling, or legal advice for fear the data will surface elsewhere.

### Psychological harm
- Anxiety and distress from a breach, from surveillance, or from intrusive profiling ("they know this about me").

## Threat-event catalog

Rate each relevant combination of threat event × harm. Sources of risk:

**Security-failure events** (confidentiality/integrity/availability of personal data):
1. Illegitimate access — external breach, insider snooping, misdirected disclosure, over-broad internal access, vendor/sub-processor compromise, government access in third countries.
2. Unwanted modification — corruption or manipulation of records leading to wrong decisions about the person.
3. Disappearance of data — loss of records the individual depends on (medical history, entitlement evidence).

**By-design events** (the processing itself):
4. Excessive collection or retention beyond need.
5. Function creep — reuse for new incompatible purposes.
6. Profiling/inference revealing more than the subject disclosed (pregnancy from purchases, health from typing patterns).
7. Automated decisions that are wrong, biased, or unexplainable.
8. Surveillance pressure — monitoring intensity itself.
9. Transparency failure — the subject cannot understand or foresee the processing.
10. Rights obstruction — practical inability to exercise data-subject rights.

## Severity anchors

Rate the impact **on the individuals affected**, taking into account how identifiable the data is, how sensitive, how many people, whether the effects are reversible, and whether vulnerable subjects are involved. Four levels (aligned with the widely used CNIL PIA methodology):

| Level | Anchor | Examples |
|---|---|---|
| **1 — Negligible** | Individuals not affected or face minor inconveniences they overcome without difficulty | Re-entering data; receiving irrelevant marketing; annoyance |
| **2 — Limited** | Significant inconveniences, overcome despite some difficulty | Extra costs; stress; having to dispute a record; denial of a convenience service; minor reputational embarrassment in a small circle |
| **3 — Significant** | Serious consequences, overcome only with real difficulty | Financial loss requiring recovery effort; identity theft; loss of employment; denial of credit/insurance/housing; targeted harassment; worsening of health; discrimination in a material decision |
| **4 — Maximum** | Irreversible consequences the individual may not overcome | Physical danger or death; long-term psychological harm; irreversible public exposure of intimate data; loss of legal status or liberty; financial ruin |

Modifiers that push severity up a level: special-category data; vulnerable subjects; large numbers affected; data or effects that cannot be recalled (public disclosure, biometric templates); decisions with legal effect.

## Likelihood anchors

Rate how plausibly the threat event occurs **and** leads to the harm, given the context and existing controls:

| Level | Anchor |
|---|---|
| **1 — Remote** | No realistic path with current controls; would require capable, motivated attacker plus multiple control failures; no history of this event in comparable processing |
| **2 — Possible** | A plausible path exists; comparable organizations have experienced it; depends on a single control holding, or on sustained good behavior by many insiders |
| **3 — Likely** | Known weaknesses make the event more probable than not over the processing's lifetime; high-value target; broad access; or the "event" is inherent to the design (e.g., profiling inference happens by default) |
| **4 — Nearly certain** | The event is occurring or will occur in normal operation; by-design harms with no mitigating control score here |

Note: for by-design events, likelihood of the *event* is often 4 — the assessment work is in severity and in how mitigations reduce the harm.

## Combining into a rating

Use a 4×4 matrix (severity × likelihood). Suggested banding: **High** = severity 3-4 with likelihood 3-4, or severity 4 with likelihood 2; **Medium** = mixed mid ratings; **Low** = severity 1-2 with likelihood 1-2. Calibrate to the organization's matrix conventions — see [../../../context/risk-scoring.md](../../../context/risk-scoring.md) for matrix design and aggregation pitfalls (in particular: do not average away one severe risk with many trivial ones; each risk stands alone).

**Residual high risk** after all feasible mitigations triggers the Art. 36 prior-consultation duty — flag it in the DPIA conclusion, do not bury it.

## Worked micro-examples

1. **Employee monitoring dashboard.** Event 8 (surveillance pressure) → chilling effect + psychological harm. Severity 2-3 (vulnerable subjects: employees; sustained exposure), likelihood 4 (by design). Inherent High. Mitigations: aggregate-only reporting, no keystroke capture, works-council agreement, access limited to HR. Residual Medium.
2. **Marketing enrichment with purchased data.** Event 6 (inference) + event 5 (function creep) → loss of control, possible discrimination by proxy. Severity 2, likelihood 3. Medium. Mitigations: drop inferred sensitive segments, honor objections globally, transparency notice update. Residual Low.
3. **Health-app data breach path.** Event 1 (illegitimate access to health data) → reputational harm, discrimination, distress. Severity 3 (special category, irreversible disclosure), likelihood 2 (strong encryption, tested controls). High inherent, Medium residual. Document why not lower: large scale keeps severity at 3.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
