# Extended GRC Metric Catalog

Twenty-eight metrics across nine domains. Each entry: formula, data source, cadence, target guidance, and gaming risk with counter-measure. Targets are common starting points for a mid-maturity program, not standards — calibrate to your risk appetite and baseline, and set targets you can miss (a target you always hit is a decoration).

Selection guidance: pick 8-12 for the executive view. Cover at least: vulnerability/patching, identity, third-party, risk register hygiene, human layer, and control assurance. Do not deploy all 28 — a catalog is a menu, not a dashboard.

## Vulnerability and patch management

**1. Critical vulnerability SLA attainment**
- Formula: critical-severity vulns remediated within SLA / critical vulns due for remediation in period. Population: in-scope production and internet-facing assets. Clock starts at first detection by scanner, not ticket creation.
- Source: vulnerability scanner + ticketing reconciliation. Cadence: monthly.
- Target: ≥90%, rising. Severity per your scoring standard — note CVSS base scores overstate/understate contextually; see `../../../context/risk-scoring.md`.
- Gaming: reclassifying criticals to high; rescanning after SLA lapse to reset the clock; shrinking "in-scope". Counter: track severity-downgrade volume and scope population size alongside.

**2. Internet-facing exposure window**
- Formula: median and p95 days from disclosure of an exploited-in-the-wild vulnerability affecting your internet-facing estate to remediation.
- Source: scanner + external attack surface tool + threat intel feed. Cadence: monthly.
- Target: median <7 days; p95 <15. This is the metric attackers experience; SLA attainment is the metric auditors experience.
- Gaming: incomplete external asset inventory makes the number look great. Counter: pair with metric 21 (unmanaged asset rate).

**3. Vulnerability debt trend**
- Formula: total open vuln instances weighted by severity, on in-scope assets, trended. (One of the few acceptable "counts" — it works because it is trended and weighted, and answers "is the backlog growing?")
- Source: scanner. Cadence: monthly.
- Target: flat or declining across 6+ months; spikes annotated (new scan coverage vs. real regression).
- Gaming: excluding asset groups. Counter: report the denominator (assets scanned) with the trend.

**4. Patch currency of endpoint fleet**
- Formula: endpoints on OS/browser patch level ≤30 days old / endpoints under management.
- Source: endpoint management platform. Cadence: monthly.
- Target: ≥95%.
- Gaming: "under management" shrinks. Counter: metric 21.

## Identity and access

**5. Mean/p95 time to revoke access on termination**
- Formula: mean and p95 hours from termination effective timestamp (HR) to completed revocation across all in-scope systems. Exclude conversions with no employment gap.
- Source: IdP audit log joined to HR feed. Cadence: monthly.
- Target: mean <24h; p95 <72h; any case >7 days individually escalated.
- Gaming: revoking SSO only while local/service accounts persist. Counter: recertification residual-access find rate (metric 7).

**6. MFA / phishing-resistant authentication coverage**
- Formula: accounts with enforced strong auth / total active accounts; report three cuts: privileged, workforce, third-party accounts.
- Source: IdP. Cadence: monthly.
- Target: privileged 100% (any gap is red); workforce ≥99%; track phishing-resistant (FIDO2) share as the maturity successor once MFA saturates.
- Gaming: "coverage" of SSO-federated apps only, ignoring apps outside SSO. Counter: application inventory vs. SSO integration rate.

**7. Access recertification: residual find rate**
- Formula: access entitlements revoked as inappropriate during recertification / entitlements reviewed. A *find rate near zero with rubber-stamp review durations* is worse than a moderate find rate — it means reviewers approve blindly.
- Source: IGA/recert tooling. Cadence: per campaign (quarterly/semiannual).
- Target: no fixed number; watch trend and review-duration distribution. Flag campaigns where median per-item review time is under a few seconds.
- Gaming: this metric *is* the counter-metric for 5 and rubber-stamping; its own gaming (pre-cleaning before campaign) is acceptable — that is the point.

**8. Privileged account inventory accuracy**
- Formula: privileged accounts in PAM/vault and attributable to an owner / privileged accounts discovered by scan.
- Source: PAM + periodic discovery scan. Cadence: quarterly.
- Target: ≥98%; orphaned privileged accounts individually reported.

## Security operations and incidents

**9. Median time to detect (MTTD) and contain (MTTC)**
- Formula: median hours from incident start (best-evidence) to detection, and detection to containment, for confirmed incidents at severity ≥ defined bar. Use median, not mean — one long incident destroys a mean; always show n.
- Source: incident records. Cadence: quarterly (monthly n is usually too small).
- Target: trending down; be honest that small n makes quarter-to-quarter movement noise.
- Gaming: severity-classifying borderline incidents downward to exclude them. Counter: report total incident count by severity alongside.

**10. Incident recurrence rate**
- Formula: incidents in period whose root cause matches a previously closed incident's root cause / total incidents.
- Source: incident post-mortems (requires disciplined root-cause taxonomy). Cadence: semiannual.
- Target: declining; recurrence >20% indicates corrective actions are theater.

**11. Detection coverage vs. threat model**
- Formula: adversary techniques in your prioritized threat model with at least one validated (tested, not just deployed) detection / techniques prioritized.
- Source: detection engineering backlog + purple team results. Cadence: quarterly.
- Target: rising; pair with metric 12 to keep "validated" honest.

**12. Detection validation freshness**
- Formula: detections exercised (test or real fire) in last 12 months / total production detections.
- Source: detection platform + test records. Cadence: quarterly.

## Third-party risk

**13. Vendors assessed on schedule**
- Formula: Tier 1-2 vendors with a current-cycle completed assessment / all Tier 1-2 vendors. (Tiering per `../../third-party-risk-assessment/SKILL.md`.)
- Source: TPRM records. Cadence: quarterly.
- Target: ≥95%; every overdue Tier 1 named individually.
- Gaming: down-tiering vendors to shrink the denominator. Counter: report tier distribution changes and require security sign-off on tier changes.

**14. Vendor findings past remediation date**
- Formula: open vendor assessment findings (high+) past agreed date, count and oldest age.
- Source: TPRM records. Cadence: quarterly. Target: 0 high past due.

**15. Attestation currency of critical vendors**
- Formula: Tier 1 vendors with current SOC 2 Type II / ISO cert on file (period/validity covering the last 12 months, bridge letters counted with flag) / Tier 1 vendors.
- Source: TPRM evidence repository. Cadence: quarterly. Target: 100%.

**16. Unsanctioned SaaS discovery rate**
- Formula: newly discovered unsanctioned SaaS with corporate data or OAuth grants, per quarter, and median days to disposition (sanction/block).
- Source: CASB/SSO logs/expense mining. Cadence: quarterly.

## Risk register and governance

**17. Open high/critical risks past treatment due date**
- Formula: count, plus oldest age in days, of high+ register risks past their treatment milestone.
- Source: risk register. Cadence: monthly to exec; each one named to the board.
- Target: 0. This is a premier board KRI — it measures whether the organization does what it decided.
- Gaming: re-baselining due dates. Counter: report count of due-date extensions granted in period.

**18. Risk review currency**
- Formula: register risks reviewed within their mandated cycle / total risks.
- Source: risk register. Cadence: quarterly. Target: ≥95%.

**19. Exception load and currency**
- Formula: open security exceptions (count, trend), % past scheduled review, and count of expired-but-still-operating exceptions.
- Source: exception register (`../../exception-management/SKILL.md`). Cadence: quarterly.
- Target: zero past review; total trend flat/down. Rising exception load with flat risk register = risk leaking around the register.

**20. Risk acceptance concentration**
- Formula: accepted risks by owner/business unit, weighted by rating.
- Source: risk register. Cadence: semiannual. Purpose: surfaces the executive who accepts everything; a governance conversation, not a dashboard tile.

## Asset and configuration

**21. Unmanaged asset rate**
- Formula: assets observed (network discovery, EDR gap analysis, cloud inventory) not present in CMDB with required management agents / total observed.
- Source: discovery tooling vs. CMDB. Cadence: monthly.
- Target: <2% and declining. This metric underwrites the honesty of nearly every other metric's denominator; report it adjacent to metrics 1, 4, 6.

**22. Configuration baseline compliance**
- Formula: systems passing hardening baseline checks / systems assessed, by platform.
- Source: configuration compliance tooling. Cadence: monthly. Target: ≥90% with failing checks aged.

**23. Backup restoration test success**
- Formula: restoration tests meeting RTO/RPO / tests executed; and % of critical systems with a test in last 12 months.
- Source: backup platform + test records. Cadence: quarterly. Target: 100% of critical systems tested annually, ≥95% success.
- Gaming: testing only easy systems. Counter: coverage cut by criticality tier.

## Human layer

**24. Phishing simulation failure and report rates**
- Formula: per campaign: clicked / delivered, and reported / delivered. Trend ≥4 campaigns; note difficulty tier of each lure — a falling click rate on easier lures is not improvement.
- Source: phishing platform. Cadence: per campaign (monthly/quarterly).
- Target: click declining at constant difficulty; report rate rising (report rate is the better security signal).
- Gaming: easier lures; excluding high-risk departments. Counter: publish lure difficulty and population alongside.

**25. Policy attestation rate**
- Formula: in-scope staff completing attestation / in-scope staff, measured 30 days after launch; laggards by department.
- Source: LMS/policy platform. Cadence: per campaign.
- Target: ≥97% at 30 days. Attestation is a weak proxy for understanding — treat as hygiene, don't celebrate it.

**26. Training completion within onboarding window**
- Formula: new joiners completing security training within 30 days of start / new joiners.
- Source: LMS + HR feed. Cadence: quarterly. Target: ≥95%.

## Control assurance and audit

**27. Control test pass rate and repeat-failure rate**
- Formula: controls passing / controls tested in period (by domain); and controls failing that also failed their previous test / controls failing.
- Source: control testing program (`../../control-testing/SKILL.md`). Cadence: quarterly.
- Target: ≥95% pass; repeat-failure rate is the sharper signal — repeat fails mean remediation isn't real.
- Gaming: testing only strong controls. Counter: publish test selection method and coverage % of control population.

**28. Audit finding aging**
- Formula: open internal/external audit findings by severity and age bucket (<30 / 30-90 / >90 days past due); trend of total weighted backlog.
- Source: findings tracker (`../../audit-preparation/SKILL.md`). Cadence: monthly.
- Target: 0 high findings >90 days past due; total backlog declining.
- Gaming: due-date renegotiation. Counter: extensions-granted count, as with metric 17.

## Cadence summary

| Cadence | Metrics |
|---------|---------|
| Monthly (ops/exec) | 1, 2, 3, 4, 5, 6, 17, 21, 22, 28 |
| Quarterly (exec/board) | 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 23, 26, 27 |
| Semiannual (governance review) | 10, 20 |
| Per campaign | 24, 25 |

## General gaming principles

1. Every ratio invites denominator management. Publish the denominator and its source next to the ratio.
2. Every SLA invites clock management. Pin the clock start to a system timestamp outside the operating team's control.
3. Every severity-scoped metric invites reclassification. Track classification-change volume as a standing counter-metric.
4. Every target invites Goodhart's law. Rotate spot-check audits of the underlying data; when a metric sits green for four consecutive periods, either raise the target or retire it to spot-check status.
