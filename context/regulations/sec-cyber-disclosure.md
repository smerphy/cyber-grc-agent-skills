# SEC Cybersecurity Disclosure Rules (2023): 8-K Item 1.05 and Regulation S-K Item 106

## At a glance

| Item | Detail |
|---|---|
| Rule | SEC final rule "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure," adopted July 2023 |
| Applies to | SEC registrants: domestic issuers (Forms 8-K, 10-K) and foreign private issuers (Forms 6-K, 20-F) |
| Incident disclosure | Form 8-K Item 1.05 — within **4 business days of the materiality determination**, not of detection |
| Materiality timing | Determination must be made "without unreasonable delay" after discovery |
| Delay mechanism | Only via written US Attorney General determination that disclosure poses substantial risk to national security or public safety (initial 30 days, extendable) |
| Annual disclosure | Regulation S-K Item 106 in Form 10-K: risk management/strategy processes, board oversight, management's role |
| Materiality standard | Traditional securities-law standard: substantial likelihood a reasonable investor would consider it important (quantitative + qualitative) |
| Third-party incidents | Incidents on third-party systems can be material to the registrant and trigger Item 1.05 |

## The common misreading — fix it first

Item 1.05 does **not** require disclosure within four business days of detecting an incident. The clock starts when the registrant **determines the incident is material**. Two separate obligations govern:

1. Make the materiality determination **without unreasonable delay** after discovering the incident. You cannot slow-walk the analysis to defer disclosure — an intentionally delayed determination is itself a violation.
2. File the 8-K within **four business days** after that determination.

Practical consequence: a well-documented materiality assessment process, with dated records of when facts became known and when the determination was made, is your defense on both prongs. "We were still investigating" is legitimate only while facts genuinely necessary to the materiality call remain unknown.

## Form 8-K Item 1.05 — material incident disclosure

Required content, to the extent known at filing:

- The material aspects of the **nature, scope, and timing** of the incident.
- The **material impact or reasonably likely material impact** on the registrant, including financial condition and results of operations.
- Explicitly **not required**: technical details about the intrusion, vulnerabilities, or response that would impede remediation — the SEC does not demand a roadmap for attackers.
- If required information is not determined or unavailable at filing, state that, and **amend the 8-K** (Item 1.05 amendment) within four business days of the information becoming available.

Related mechanics:

- **"Cybersecurity incident"** is defined broadly: an unauthorized occurrence (or series of related occurrences) on or conducted through information systems that jeopardizes confidentiality, integrity, or availability of information systems or the information on them. A **series of related smaller incidents** can be material in the aggregate.
- **Voluntary disclosure:** SEC staff guidance (2024) directs that incidents disclosed before or without a materiality determination should go under **Item 8.01**, reserving Item 1.05 for incidents determined material — keep the two clean.
- **Foreign private issuers** furnish comparable incident information on Form 6-K if disclosed elsewhere.
- Untimely Item 1.05 filing does not, by itself, forfeit Form S-3 eligibility — a deliberate design choice to reduce over-caution — but late filing remains an enforcement exposure.

## National security / public safety delay

The **only** sanctioned delay path: the **US Attorney General** determines in writing that disclosure would pose a substantial risk to national security or public safety and notifies the SEC.

- Initial delay: up to **30 days**; extendable by an additional **30 days**; in extraordinary circumstances involving national security, up to a further **60 days**; beyond that only via SEC exemptive order.
- In practice, requests route through the **FBI** (with CISA and other agencies) under DOJ-published procedures — engage the FBI **early and pre-incident** (know your field office contacts), because the AG determination must exist before the four-day deadline lapses.
- Law-enforcement investigation interest alone is **not** a delay basis. Neither are contractual NDAs, insurer preferences, or a desire to finish remediation.

## Regulation S-K Item 106 — annual disclosures (Form 10-K)

**Item 106(b) — Risk management and strategy.** Describe processes, if any, for assessing, identifying, and managing material risks from cybersecurity threats, including:

- Whether and how those processes are integrated into overall risk management.
- Use of assessors, consultants, auditors, or other third parties.
- Processes to oversee and identify material risks from threats associated with **third-party service providers**.
- Whether risks from cybersecurity threats, including prior incidents, have materially affected or are reasonably likely to materially affect the registrant, its strategy, results, or financial condition.

**Item 106(c) — Governance.**

- **Board oversight:** which board committee or subcommittee oversees cybersecurity risk, and how the board is informed.
- **Management's role:** which positions or committees assess and manage the risk, their relevant **expertise**, how they are informed of and monitor incidents, and whether/how they report to the board.

Note: the adopted rule does **not** require disclosure of board-member cyber expertise (that proposal was dropped). Foreign private issuers make comparable disclosures on Form 20-F.

Item 106 is describable-as-is: there is no mandated program standard. But the disclosure must be accurate — describing processes you do not actually operate creates independent liability (misrepresentation cases have been brought over inflated security claims). Align the described program with reality, and reality with a framework (see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)).

## Materiality analysis — considerations

The standard is the classic securities-law test (substantial likelihood that a reasonable investor would consider the information important / that it significantly alters the total mix of information). There is no bright-line threshold. Weigh:

**Quantitative**

- Direct costs: response, recovery, legal, notification, ransom considerations.
- Revenue impact: operational downtime, lost sales, contract penalties or terminations.
- Balance-sheet effects: asset impairment, contingent liabilities, insurance recoveries.
- Compare against earnings, revenue, and prior benchmarks the company uses for materiality in financial reporting — but do not stop there.

**Qualitative** (can make a quantitatively small incident material)

- Nature of data or systems: crown-jewel IP, large volumes of customer PII, safety-critical OT.
- Harm to reputation, customer relationships, or competitive position.
- Regulatory and litigation exposure triggered by the incident (GDPR, state AGs, class actions).
- Ongoing attacker access vs. contained event; whether the incident reveals a systemic control weakness.
- Prior related incidents (aggregation) and prior risk-factor statements ("if X occurred, it could…" reads badly once X has occurred and goes undisclosed).

Document the analysis, the participants, the facts available at each decision point, and the conclusion — whether the answer is "material" or "not material."

## Practical incident-to-disclosure workflow

1. **Pre-incident:** define materiality criteria and a **disclosure committee escalation trigger** inside the incident response plan; identify the deciders (typically CFO, GC, CISO, disclosure committee); establish FBI contacts; brief the board committee on the process.
2. **Detection/escalation:** IR severity scheme flags candidate-material incidents to legal and the disclosure committee at a defined threshold — early, on preliminary facts.
3. **Assessment loop:** disclosure committee assesses materiality iteratively as facts develop, minuting each meeting: facts known, open questions, conclusion (material / not material / not yet determinable and why).
4. **Determination:** on a "material" conclusion, the 4-business-day clock starts. Draft the 8-K (nature/scope/timing + impact; omit exploitable technical detail), coordinate with law enforcement if a delay request is in play, file.
5. **Amend** as previously unknown required information becomes available.
6. **Parallel obligations:** run other notification clocks concurrently — they are independent and mostly faster (see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md)).
7. **Post-incident:** update Item 106 narrative, risk factors, and — if the incident affected financial reporting systems — the ICFR/disclosure-controls assessment (see [sox-itgc.md](sox-itgc.md)).

## Third-party incidents

An incident on a vendor's, cloud provider's, or supply-chain partner's systems can be material **to you** — the rule's incident definition covers occurrences "on or conducted through" your information systems, and SEC commentary makes clear registrants cannot ignore incidents at third parties holding their data or supporting their operations. Implications:

- Contractual incident-notification clauses with providers feed your materiality clock: assess without unreasonable delay once you learn of the incident, based on information reasonably available.
- You are not expected to disclose faster than the third party gives you facts, but you cannot avoid inquiry.
- Fold this into vendor tiering and contract requirements (see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)).

## Key obligations for security/GRC teams

1. Embed the materiality escalation path in the IR plan; exercise it in tabletops, including a mock disclosure-committee determination.
2. Keep a dated evidence trail: incident discovery, escalation, each materiality deliberation, determination, filing.
3. Maintain the Item 106 disclosure inputs annually: current process descriptions, third-party oversight processes, management roles and expertise, board reporting cadence.
4. Verify described practices exist — reconcile the 10-K narrative against actual program documentation before filing.
5. Pre-establish FBI/CISA contacts and internal criteria for seeking an AG delay.
6. Require and test vendor incident-notification SLAs for materially relied-upon providers.
7. Track amendments owed on open 8-K Item 1.05 filings.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
