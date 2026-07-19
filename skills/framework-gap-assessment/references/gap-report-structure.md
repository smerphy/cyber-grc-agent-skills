# Gap Report Structure

Full skeleton for the gap assessment deliverable, with example rows. Sections 1–6 form the report body; 7–9 are appendices. Keep the body under ~15 pages for a single-framework assessment; move bulk to appendices.

---

## 1. Executive summary (1 page hard limit)

Contents, in order:

1. **One-sentence verdict.** Overall posture relative to target, in plain language.
2. **Maturity distribution, numerically.** "Of 22 CSF 2.0 categories assessed: 3 at Level 1, 11 at Level 2, 7 at Level 3, 1 at Level 4."
3. **Top three gaps** with business consequence, not framework citation, leading each.
4. **Headline of the roadmap:** what Wave 1 (0–90 days) buys, in risk terms.
5. **Confidence statement:** evidence basis (n interviews, n documents, n artifacts) and any scope limitations.

Example verdict: "The organization runs capable day-to-day IT security but lacks the governance layer and detection coverage its customer commitments assume; three gaps require action this quarter."

## 2. Scope and method

- Framework and exact version; scoring granularity chosen.
- Organizational and system boundary; exclusions with justification.
- Assessment window and evidence cutoff date.
- Evidence channels used (interviews with roles, documents reviewed, artifacts sampled) — counts here, full lists in appendices.
- Maturity scale summary (one table; full anchors by reference to the scale document).
- Target level(s) and who set them.
- Limitations: refused/unavailable evidence, roles not interviewed, sites not visited. State the effect on confidence, not blame.

## 3. Scorecard

One row per scored domain. Sort in framework order, not by score.

| Domain | Current | Target | Gap | Confidence | One-line basis |
|---|---|---|---|---|---|
| GV – Govern | 2 | 3 | Y | Medium | Risk appetite undocumented; policy suite approved but metrics absent |
| ID – Identify | 2 | 3 | Y | High | Asset inventory 60% coverage per discovery-scan diff, 2026-06-28 |
| PR – Protect | 3 | 3 | N | High | MFA, patching, backup practices defined and artifact-verified |
| DE – Detect | 1 | 3 | Y | High | No log aggregation; alerts unmonitored outside business hours |
| RS – Respond | 2 | 3 | Y | Medium | IR plan exists, never exercised; roles unstaffed on paper |
| RC – Recover | 2 | 3 | Y | Medium | Backups tested ad hoc; no RTO/RPO agreed with the business |

Include a function/theme-level rollup chart description if the report will be rendered visually (bar per domain, current vs target). Never present an averaged single "maturity number" for the whole organization without the distribution beside it.

## 4. Gap register

The heart of the report. One row per gap; IDs stable for tracking into remediation. Sort by severity, then framework order.

Columns and rules:

| Column | Rule |
|---|---|
| ID | `GAP-nn`, never reused after deletion |
| Framework ref | Precise citation (e.g., "CSF 2.0 DE.CM-01", "ISO 27001 cl. 9.2", "CIS 8.2", "PCI DSS Req. 10") — one primary ref; secondary refs allowed |
| Finding | Factual statement of the deficiency; no recommendations mixed in |
| Evidence | Interviewee+date, document+version, or artifact — enough for a reader to re-verify |
| Current → Target | Levels, e.g., "1 → 3" |
| Severity | Critical / High / Medium / Low per the two-axis rule (exposure × obligation) |
| Recommendation | Specific, testable action; name the class of solution, not a vendor |
| Owner | Role, agreed in the review meeting — "TBD" only with a date to resolve |
| Effort | S (< 2 person-weeks), M (2–8), L (> 8) — order-of-magnitude only |
| Dependencies | Other GAP IDs or prerequisites |

Example rows:

| ID | Framework ref | Finding | Evidence | Current → Target | Severity | Recommendation | Owner | Effort | Dependencies |
|---|---|---|---|---|---|---|---|---|---|
| GAP-03 | CSF 2.0 DE.CM-01; CIS 8.2 | Server and firewall logs are retained locally on each device with no aggregation; no alerting exists outside the EDR console | Interview: Infra Lead 2026-07-01; absence confirmed in tooling inventory v1.4 | 1 → 3 | Critical | Deploy centralized log collection for the 41 in-scope servers and perimeter devices; define minimum alert set for authentication and admin-activity anomalies | Head of IT | M | — |
| GAP-07 | CSF 2.0 PR.AA-02; CIS 6.5 | MFA enforced for VPN and email but not for three break-glass domain admin accounts | Entra ID CA policy export 2026-07-02; Interview: IT Ops Lead | 2 → 3 | Critical | Enroll break-glass accounts in phishing-resistant MFA; document monitored exclusion procedure | Head of IT | S | — |
| GAP-11 | ISO 27001 cl. 9.2 | No internal ISMS audit has been performed; programme not defined | Absence of audit records; confirmed by CISO 2026-07-03 | 1 → 3 | High | Define internal audit programme; execute first audit before certification stage 1 | CISO | M | GAP-02 (SoA completion) |
| GAP-15 | CSF 2.0 RS.MA; ISO A theme: Organizational | IR plan (v0.9, 2024) never exercised; on-call contact list contains two departed employees | IR plan v0.9; Interview: Ops Manager 2026-07-02 | 2 → 3 | High | Update plan, assign roles to current staff, run tabletop within 90 days | CISO | S | — |
| GAP-22 | CIS 7.3 | Vulnerability scans run monthly but only against externally facing assets; internal ranges unscanned | Scan config export 2026-06-30 | 2 → 3 | Medium | Extend authenticated scanning to internal server and workstation ranges; define remediation SLAs | Security Engineer | S | GAP-01 (asset inventory) |

Accepted-rather-than-remediated gaps: move to a short "Risk acceptances proposed" table and route through the exception process — do not leave them in the register marked "accept" without an owner and expiry.

## 5. Remediation roadmap

Structure by wave; within a wave, list items in execution order.

| Wave | Horizon | Theme | Items (GAP IDs) | Effort total | Exit criterion |
|---|---|---|---|---|---|
| 1 | 0–90 days | Stop the bleeding + quick wins | GAP-03, GAP-07, GAP-15 | 1×M + 2×S | All Critical gaps closed or formally accepted |
| 2 | 90–180 days | Foundations | GAP-01, GAP-11, GAP-22 | 2×M + 1×S | Asset inventory ≥ 95% coverage; first internal audit complete |
| 3 | 180–365 days | Maturity uplift | GAP-05, GAP-09, GAP-18 | 1×L + 2×M | Target levels met in all domains named in the driver |

Roadmap rules:

- Every register gap appears in exactly one wave, in the acceptances table, or in an explicit "deferred beyond 12 months" list with rationale.
- Dependencies sequence waves: inventory and logging before detection; detection before response-metric targets.
- If the driver has a hard date (certification audit, customer deadline, regulatory milestone), show it on the roadmap and verify Wave exit criteria land before it.

## 6. Reassessment recommendation

One short section: when to reassess (typically 6–12 months or post-Wave-2), what evidence to keep collecting in the meantime, and which metrics from the roadmap should flow into ongoing reporting (hand off to the metrics program).

## 7. Appendix A — Evidence inventory

Table: `Evidence ID | Type (doc/interview/artifact) | Name/description | Version/date | Source | Domains it supports`. Every citation in sections 3–4 must resolve to a row here.

## 8. Appendix B — Interview log

Table: `Date | Interviewee role | Duration | Domains covered`. Names may be replaced by roles in externally shared versions.

## 9. Appendix C — Maturity scale definitions

Reproduce the level anchors so the report is self-contained when forwarded.

---

## Formatting rules

- Framework citations always carry the identifier the framework itself uses (subcategory ID, clause number, control/safeguard number, requirement number).
- Findings are past/present factual statements; recommendations are imperatives. Never blend them in one cell.
- Severity words are reserved: do not use "critical" loosely in prose if it is not a Critical-rated gap.
- If the report will feed audit preparation, keep evidence IDs stable — the audit workstream will reuse them.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
