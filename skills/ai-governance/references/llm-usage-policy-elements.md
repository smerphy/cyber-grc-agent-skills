# Internal LLM / Generative AI Acceptable-Use Standard: Required Elements

Content specification for an internal standard governing employee and contractor use of LLMs and generative AI tools. Use this as the requirements list when drafting via the policy-authoring skill; it is not itself the policy. Target document length when drafted: 3–6 pages. A standard nobody reads protects nobody — every element below must resolve to a rule a non-lawyer can follow.

## 1. Purpose and scope

- State the goal: enable productive AI use while protecting confidential data, customers, and legal position — not to ban AI. A pure ban drives usage underground and forfeits visibility.
- Scope: all workforce members (employees, contractors, temps); all generative AI touchpoints — standalone chatbots, AI features embedded in approved SaaS, coding assistants, browser extensions, API usage, AI agents, meeting transcription/notetaker bots.
- Explicitly cover use on any device where company data is involved, including personal accounts on personal devices handling work content.

## 2. Approved tools and the approval path

- Maintain a living **approved-tools list** (link, not embed — the list changes faster than the policy): tool, approved plan/tier (enterprise vs consumer accounts differ materially in data-use terms), permitted data classes, notes.
- State the default: **tools not on the list are not approved for company data.** Public/consumer tiers of otherwise-approved tools count as separate, unapproved tools unless listed.
- Define the request path for new tools (routes into third-party risk assessment — [../../third-party-risk-assessment/SKILL.md](../../third-party-risk-assessment/SKILL.md)) with a realistic SLA; and the exception path for time-bound deviations ([../../exception-management/SKILL.md](../../exception-management/SKILL.md)).
- Address embedded AI: vendors enabling AI features inside already-approved tools does not auto-approve those features; owners of vendor relationships must notify the AI governance function of new AI features.

## 3. Data input rules

The core of the standard. Tie rules to the existing data classification scheme — one table, no prose ambiguity:

| Data class | Consumer AI tools | Approved enterprise AI tools |
|---|---|---|
| Public | Allowed | Allowed |
| Internal | Prohibited | Allowed |
| Confidential (incl. customer data, source code where classified) | Prohibited | Allowed only where the tool's listing permits it |
| Restricted (regulated personal data, secrets/credentials, material non-public information, trade secrets under NDA) | Prohibited | Prohibited unless explicitly listed with contractual and technical safeguards |

- Call out the non-obvious prohibited inputs by name: credentials and API keys; personal data of customers or colleagues; health or financial records; M&A and other MNPI; third-party data under NDA; unpublished IP where AI-provider training or retention terms are unresolved.
- State that prompts and uploaded files **are disclosures to the provider** — the same rules as sending data to any vendor apply.
- Note technical enforcement where present (gateway/proxy, DLP, egress blocking) and that enforcement gaps do not create permission.

## 4. Output handling rules

- **Verification duty**: generative output can be wrong with high confidence (hallucination). The human using the output owns its accuracy. Require verification proportionate to use: spot-check for internal drafts; full review for anything customer-facing, published, legal, financial, or safety-relevant.
- **Consequential decisions**: LLM output must not be the sole basis for decisions materially affecting people (hiring, discipline, credit, medical, legal positions); a competent human must make the decision and be able to justify it without "the AI said so."
- **Code**: AI-generated code follows the same review, testing, and security-scanning gates as human code; no direct-to-production paths.
- **IP and attribution**: do not represent AI output as the work of a named person where that misleads; respect third-party IP (do not prompt for imitation of identifiable protected works); follow any client contract terms restricting AI use in deliverables.
- **Disclosure**: where law or policy requires disclosure of AI-generated content (e.g., EU AI Act Art. 50 for synthetic media and certain public-interest text), mark it.

## 5. Prohibited uses

Enumerate explicitly; do not rely on "common sense":

- Entering data in violation of Section 3.
- Uses on the organization's prohibited list (mirror EU AI Act Art. 5 where relevant: no emotion inference on employees, no social scoring, no covert manipulation).
- Generating content that is unlawful, harassing, or discriminatory; deepfakes of real people without documented authorization and legal review.
- Circumventing security controls, or using AI to do so (e.g., asking a tool to deobfuscate credentials, bypassing the approved gateway).
- Autonomous/agentic AI executing actions on production systems, finances, or external communications without a human approval step, unless the specific agent deployment is approved with defined guardrails.
- Meeting recording/transcription bots in meetings without required consent of participants (jurisdiction-dependent — route to legal).

## 6. Roles and responsibilities

- **All users**: follow the standard, complete training, report incidents and suspected misuse.
- **Managers**: ensure team tool usage is on the approved list; no procuring AI tools on expense cards outside the approval path.
- **AI governance function / CISO delegate**: own the approved list, run approvals with security/legal/privacy input, monitor compliance, maintain the standard.
- **Legal/privacy**: assess data-protection and IP implications; own DPIA triggers for AI uses involving personal data ([../../dpia-privacy-assessment/SKILL.md](../../dpia-privacy-assessment/SKILL.md)).
- **Engineering owners of internal LLM apps**: comply with the AI control set (see [ai-control-set.md](ai-control-set.md)) — this standard governs *use* of AI tools; building AI products carries additional obligations.

## 7. Incident reporting

- Define reportable events: confidential/restricted data entered into an unapproved tool or beyond permitted class; suspected prompt-injection or manipulation of an internal AI app; harmful or defamatory output published; AI account compromise; vendor notice of an AI-related breach.
- Route into the existing incident process — data-leakage-via-prompt is a data incident and may carry regulatory notification duties; assess via [../../incident-regulatory-reporting/SKILL.md](../../incident-regulatory-reporting/SKILL.md).
- State the no-blame reporting norm: self-reporting an accidental paste is treated as a control improvement input, not a disciplinary event (deliberate or repeated violations are handled under Section 9).

## 8. Training and awareness

- Mandatory at onboarding and periodically thereafter (annual is the common bar; the EU AI Act Art. 4 AI-literacy duty applies from 2 Feb 2025 for organizations in scope). Role-based depth: general users vs developers vs oversight roles.
- Content minimum: the data-input table, hallucination risk, approved list location, how to request a tool, how to report.

## 9. Enforcement, monitoring, and review

- State what is monitored (network egress to AI services, gateway logs, DLP events) — transparency about monitoring is both a legal expectation and a deterrent; coordinate with works councils/employee-representation where applicable.
- Consequences for violations per the existing disciplinary/sanctions framework; contractual consequences for contractors.
- Review cycle: at least annually and on trigger events (new regulation, major incident, significant new tool class). Owner named. Version history kept.

## Common drafting failures

1. **Ban-everything drafting** — creates shadow AI and destroys the inventory's accuracy. Approve a capable default toolset on enterprise terms first, then restrict.
2. **No data-class table** — "use good judgment with sensitive data" is not a rule. The table in Section 3 is the standard's load-bearing wall.
3. **Ignoring embedded AI** — the policy covers ChatGPT but not the AI features that appeared in the CRM last quarter.
4. **Static approved list inside the policy body** — the list must be separable and fast to update or it will be ignored.
5. **No exception path** — without a sanctioned route, deviations happen without visibility. See [../../exception-management/SKILL.md](../../exception-management/SKILL.md).
6. **Unowned output** — failing to state that the human user owns the accuracy and consequences of anything they do with AI output.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
