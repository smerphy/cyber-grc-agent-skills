# Data Subject Rights by Regime

Working map of the main rights, deadlines, and procedural rules across the regimes a multi-jurisdiction DSAR program most often meets. This is an orientation layer, not legal text: article and section numbers are given so you can go read them, and every operational decision should be checked against the official text and current regulator guidance. Regime background packs: `../../../context/regulations/gdpr.md`, `../../../context/regulations/us-state-privacy.md`, `../../../context/regulations/uk-data-protection.md`, `../../../context/regulations/other-jurisdictions.md`.

## Rights map

| Right | GDPR | CCPA/CPRA (California) | UK GDPR | Common analogues elsewhere |
|-------|------|------------------------|---------|----------------------------|
| Access / copy ("right to know") | Art. 15 — copy of the data plus purposes, categories, recipients, retention, source, rights, transfer safeguards, automated decision-making info | Right to know categories and specific pieces collected, sources, purposes, third parties disclosed to | Art. 15 (as retained) — mirrors EU GDPR | Brazil LGPD Art. 18; India DPDP §11; most US state laws; Canada PIPEDA access right |
| Rectification / correction | Art. 16 | Right to correct inaccurate PI (added by CPRA) | Art. 16 | Widely present (LGPD, US state laws, PIPEDA challenge-accuracy) |
| Erasure / deletion | Art. 17 — on enumerated grounds, with exceptions (legal obligation, legal claims, freedom of expression, etc.) | Right to delete PI collected from the consumer, subject to enumerated exceptions | Art. 17 | LGPD Art. 18; most US state laws; scope and exceptions vary substantially |
| Restriction of processing | Art. 18 | No direct equivalent (nearest: limit sensitive-PI use) | Art. 18 | Rare outside GDPR-derived laws |
| Portability | Art. 20 — data provided by the subject, automated processing, consent/contract basis | Included within access delivery (portable, readily usable format) | Art. 20 | Present in several newer laws; scope varies |
| Objection | Art. 21 — absolute for direct marketing; balancing test otherwise | No direct equivalent (nearest: opt-outs) | Art. 21 | Varies |
| Opt-out of sale/sharing | No direct equivalent (objection + consent rules cover similar ground) | Core CCPA/CPRA right; includes sharing for cross-context behavioral advertising; must honor opt-out preference signals (e.g., GPC) | — | Most US state laws have targeted-advertising/sale opt-outs |
| Limit sensitive-PI use | Special-category rules (Art. 9) rather than a request right | CPRA right to limit use/disclosure of sensitive PI | Art. 9 equivalent | US state laws mostly use consent for sensitive data instead |
| Automated decision-making | Art. 22 — right not to be subject to solely automated decisions with legal/similar effect, with exceptions | ADMT regulations (access/opt-out rights) — check current status of the finalized regulations | Art. 22 | Emerging area in several regimes |
| Notification of rectification/erasure to recipients | Art. 19 | Deletion must be passed to service providers/contractors and, in cases, third parties | Art. 19 | Varies |

Rights are conditional, not absolute — each has grounds, scope limits, and exceptions in the official text. Classify the request, then read the specific article/section before promising anything.

## Deadlines and extensions

| Regime | Baseline deadline | Extension | Notes |
|--------|-------------------|-----------|-------|
| GDPR | One month from receipt (Art. 12(3)) | Up to two further months for complex or numerous requests; requester must be informed with reasons within the first month | Clock runs from receipt; regulator guidance treats identity-verification interplay with the clock carefully — verify current EDPB guidance |
| UK GDPR | One month | Two further months, same conditions | ICO guidance permits pausing the clock while awaiting requested clarification in defined cases — verify current ICO position |
| CCPA/CPRA | 45 calendar days from receipt for know/delete/correct | One additional 45-day extension with notice within the first 45 days | Confirm receipt within 10 business days; opt-out of sale/sharing must be actioned within 15 business days; access lookback is 12 months by default, longer on request for data collected after CPRA's operative date unless impossible or disproportionate — verify details |
| Other US state laws (VA, CO, CT, TX, etc.) | Commonly 45 days | Commonly one 45-day extension | Many mandate an internal **appeal** process with its own response window (often 45-60 days) and a requirement to give the AG complaint route on appeal denial — check the specific statute |
| Brazil (LGPD) | Simplified response immediately; full declaration within 15 days for access (Art. 19) | — | Other rights lack a uniform statutory clock; ANPD guidance evolving — verify |
| Canada (PIPEDA) | 30 days | Extendable in defined circumstances with notice | Provincial laws (e.g., Quebec Law 25) differ — verify per province |
| India (DPDP Act) | Timelines set by rules rather than the Act | — | Check the current DPDP Rules for prescribed periods |

Universal practice regardless of regime: compute the deadline on day of receipt, diary the extension-notice date, and treat the shortest applicable deadline as controlling when regimes overlap.

## Verification standards

- **GDPR/UK**: Art. 12(6) — request additional information only where the controller has *reasonable doubts* about identity; proportionality is the test. Excessive ID demands are themselves criticized by regulators.
- **CCPA/CPRA**: regulations define verification tiers — matching data points on file for category-level disclosures, a higher bar ("reasonable degree" / "reasonably high degree" of certainty) for specific pieces and deletion. Opt-out requests must generally **not** be subject to verification (fraud-prevention denial is separately allowed). Password-protected account verification is acceptable; forcing account creation is not.
- **Agents**: CCPA permits authorized agents with written permission (and consumer identity verification); GDPR-side, third parties act under mandate/power of attorney — verify authority documents in both cases.
- Verification information collected for a request must be used only for verification and not retained beyond need.

## Fee rules

- **GDPR/UK**: free in the normal case (Art. 12(5)). A "reasonable fee" or refusal only for manifestly unfounded or excessive (especially repetitive) requests — controller bears the burden of demonstrating that character. Additional copies beyond the first may carry a reasonable administrative fee (Art. 15(3)).
- **CCPA/CPRA**: free; up to twice in a 12-month period for verifiable consumer requests to know. Manifestly unfounded/excessive requests may be charged or refused with justification.
- **Other regimes**: many permit a prescribed or reasonable fee in defined cases (e.g., PIPEDA minimal cost with advance notice). Check before charging anything — an unlawful fee converts a routine request into a complaint.

## Using this table

1. Identify every regime that attaches to the requester (residence, your establishment, targeting).
2. Take the **shortest deadline** and the **most protective standard** for each element where regimes overlap.
3. Read the actual article/section for the specific right invoked before acting — the table above deliberately omits the conditions and exceptions that decide hard cases.
4. Where this file and the official text or current regulator guidance disagree, the official text wins; flag the discrepancy for this file's next review.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
