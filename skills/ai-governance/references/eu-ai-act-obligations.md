# EU AI Act: Classification Practice and Obligation Selection

Working reference for classifying AI systems under Regulation (EU) 2024/1689 and selecting the right obligation set. Use with Step 2–3 of the AI governance skill.

**Statutory content lives in [../../../context/regulations/eu-ai-act.md](../../../context/regulations/eu-ai-act.md) — the Art. 5 prohibited-practices list, the Annex III high-risk use cases, provider requirements (Arts. 8–17, 43, 48–49, 72–73), Art. 50 transparency duties, GPAI/Chapter V duties, the applicability timeline, and penalties.** This file deliberately does not restate that material; consult the context file (and the official text) for the lists and figures, and use this file for how to apply them.

## Role determination in practice

Role drives the obligation set, and misassigned roles are the most common classification error:

- **Provider**: develops an AI system (or has it developed) and places it on the market or puts it into service **under its own name or trademark**. Building an internal tool and putting it into service for your own use makes you a provider of that system.
- **Deployer**: uses an AI system under its own authority in a professional context (personal non-professional use is out of scope).
- **Role conversion (Art. 25)**: a deployer, importer, or distributor becomes a provider of a high-risk system if it puts its name/trademark on it, substantially modifies it, or modifies its intended purpose in a way that makes it high-risk. White-labeling a vendor's AI product makes you the provider. Wire re-classification into change management and procurement gates, not just the annual review.
- **Downstream GPAI builders**: an organization fine-tuning or integrating a general-purpose AI model into an application is generally a provider or deployer of an AI *system* (classified by the risk tiers), not a GPAI provider — unless the modification is significant enough to make it a new model provider. Document the reasoning per case.
- Classify **per system, not per organization**: most enterprises are deployers of their internal and purchased tools and providers of anything customer-facing under their own brand.

Extraterritoriality check: the Act reaches providers placing AI on the EU market wherever established, deployers in the EU, and third-country providers/deployers **where the system's output is used in the EU**. Out-of-scope categories worth recording explicitly when claimed: exclusively military/defense purposes; pure scientific research and development; free and open-source AI outside the prohibited, high-risk, Art. 50, and GPAI cases.

## Classification quick-reference

For each inventoried system, answer in order and record the rationale:

1. EU nexus (provider placing on EU market / deployer in EU / output used in EU)? No → no AI Act duty; keep the tier as an internal severity proxy.
2. Does the use match any Art. 5 prohibition (list in the context file)? Yes → **stop and escalate immediately** — a prohibited practice is not a remediation ticket; the only options are cease or redesign.
3. Annex I product/safety component, or Annex III use case (lists in the context file)? If Annex III: does the Art. 6(3) filter apply (narrow procedural task, improving a completed human activity, pattern detection without replacing human assessment, preparatory task) — and is there **profiling of natural persons, which always defeats the filter**? A provider invoking Art. 6(3) must document the assessment and still register the system.
4. Does Art. 50 transparency apply (chatbot interaction, synthetic content, deepfakes, AI-generated public-interest text, emotion recognition / biometric categorisation)? Stackable with other tiers.
5. Are we provider or deployer for this system (check Art. 25 conversion)? → select the obligation set from the context file.
6. Any GPAI-provider exposure (Chapter V, including the systemic-risk compute presumption)? → separate obligation track.
7. Which obligations are in force today vs upcoming (timeline table in the context file)? → live compliance gap vs roadmap item.

As of mid-2026, prohibitions, AI literacy, and GPAI obligations are already in force, and the general high-risk regime applies from 2 Aug 2026 — treat unmet obligations for in-scope systems as live compliance gaps. Monitor for implementation-timing adjustments via the digital-omnibus process; verify the current state before relying on any date.

## Mapping obligations to program controls

- **High-risk provider stack** (Arts. 8–17, 43, 48–49, 72–73 — substance in the context file): map each duty to a control in [ai-control-set.md](ai-control-set.md) and record the article each control evidences; an obligation without a named control and owner is a gap, not a plan.
- **High-risk deployer duties** (Arts. 26–27): operationalize as assigned, trained human oversight; incorporation of the provider's instructions for use into SOPs; input-data controls where the deployer controls inputs; monitoring with a suspend-and-notify path; log retention of at least six months; worker and affected-person notification.
- **Fundamental rights impact assessment (Art. 27)**: required before first use for deployers that are public bodies or provide public services, and for deployers of Annex III credit-scoring and life/health-insurance systems. A DPIA under GDPR Art. 35 can be leveraged — run [../../dpia-privacy-assessment/SKILL.md](../../dpia-privacy-assessment/SKILL.md) and cross-reference rather than duplicating.
- **Minimal-risk systems** still carry the Art. 4 AI-literacy duty and should get internal controls proportionate to business risk — minimal risk under the Act is not "no governance."
- **Penalty exposure** (figures in the context file) scales by tier — use it to prioritize remediation, with prohibited-practice exposure always first.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
