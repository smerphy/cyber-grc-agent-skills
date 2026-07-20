# US Sectoral Privacy Laws Beyond HIPAA and GLBA

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | United States, federal (plus a pointer to state sectoral laws) |
| Instruments | COPPA (children's online data), FERPA (education records), FTC Health Breach Notification Rule (non-HIPAA health data), VPPA (video viewing data), DPPA (driver records), TCPA (calls/texts) |
| Regulators | FTC (COPPA, HBNR, VPPA context), Dept. of Education (FERPA), FCC (TCPA), state AGs, plus private plaintiffs where a private right of action exists (VPPA, TCPA, DPPA) |
| Who's covered | Determined by **data type and audience**, not company size or sector registration — a single consumer app can trigger three of these at once |
| Max penalties | Vary: COPPA civil penalties per violation (five figures each, inflation-adjusted annually); FERPA — loss of federal education funding; HBNR — FTC penalties per violation; VPPA/TCPA/DPPA — statutory damages per person/call, which is where class actions get expensive |

US privacy law is sectoral: instead of one omnibus statute, obligations attach to specific data types. GRC teams usually know [hipaa.md](hipaa.md) and [glba-ftc-safeguards.md](glba-ftc-safeguards.md); this note covers the rest of the federal family plus the state sectoral wave, ending with a scoping method.

## COPPA — Children's Online Privacy Protection Act

**What it covers.** Personal information collected online from children **under 13**, by operators of websites/online services **directed to children** or with **actual knowledge** they are collecting from under-13 users. Enforced by the FTC under the COPPA Rule (16 CFR Part 312); state AGs can also enforce.

**Core obligations:**

- **Verifiable parental consent (VPC)** before collecting, using, or disclosing children's personal information, via approved methods (payment card verification, signed forms, knowledge-based questions, facial-comparison methods approved over time).
- Direct notice to parents and a compliant privacy policy; parental rights to review and delete; no conditioning participation on excess data collection; reasonable security; retention only as long as necessary.
- "Personal information" is broad: includes persistent identifiers (cookies, device IDs), geolocation, photos, voice — a persistent identifier used for behavioral advertising is enough to trigger COPPA on a child-directed service.
- **Mixed-audience** services can age-gate and apply COPPA only to under-13 users; purely child-directed services cannot age-gate their way out.

**2025 amendments.** The FTC finalized significant COPPA Rule amendments in 2025. Reported changes include: opt-in parental consent specifically for disclosures to third parties/targeted advertising (separate from consent to collect), biometric identifiers added to personal information, written data-retention policies with limits, strengthened security-program requirements, and safe-harbor program transparency. Compliance dates phased into 2025-2026. **Hedge:** verify the final amendment text and its compliance dates before designing controls to it.

**Penalties:** civil penalties assessed per violation (per child, in practice), inflation-adjusted annually — currently on the order of $50,000+ per violation. Landmark settlements: Google/YouTube ($170M), Epic Games ($275M COPPA component), Musical.ly/TikTok.

## FERPA — Family Educational Rights and Privacy Act

**What it covers.** "Education records" — records directly related to a student, maintained by an educational agency/institution **receiving federal education funds** (nearly all schools and universities). Regulated by the Department of Education (Student Privacy Policy Office), 34 CFR Part 99. No private right of action (Gonzaga v. Doe); the enforcement lever is loss of federal funding, which has never been fully imposed — but state student-privacy laws and contractual pressure do the practical enforcing.

**Mechanics that matter to vendors:**

- Schools need written parental consent (or eligible-student consent at 18+) to disclose education records, **except** under enumerated exceptions.
- The **school official exception** is how edtech works: a vendor can receive education records as a "school official" if it performs an institutional service, is under the school's **direct control** regarding the records, uses them only for the authorized purpose, and does not re-disclose. Your contract must actually establish these conditions.
- "Directory information" (name, dates of attendance, etc.) can be disclosed if the school designates it and offers opt-out — but vendors should not assume data received is directory information.
- **Edtech implications:** no product-improvement or advertising use of student records beyond what the school authorizes; delete/return on contract end; expect state student-privacy statutes (California SOPIPA and dozens of analogues) to layer stricter, directly enforceable rules on top of FERPA.

## FTC Health Breach Notification Rule (HBNR)

**What it covers.** The gap HIPAA leaves: vendors of **personal health records (PHRs)** and PHR-related entities **not covered by HIPAA** — in practice, health apps, fitness/wearable platforms, fertility and mental-health apps, and connected-device services that draw identifiable health data from multiple sources. 16 CFR Part 318, enforced by the FTC.

**2024 final rule expansion.** The FTC's 2024 amendments (effective mid-2024) codified its 2021 policy statement: definitions now clearly sweep in health apps and similar technologies ("health care provider" includes app and internet services; "PHR identifiable health information" broadened), and — critically — **"breach of security" includes unauthorized disclosures**, not just external intrusions. Sharing health data with an ad-tech pixel without authorization is a reportable "breach." The amendments also modernized notice methods (electronic notice) and expanded required notice content. Verify details against the final rule text.

**Timelines (verify):** notify affected individuals and the FTC **without unreasonable delay and no later than 60 calendar days** after discovery; if **500 or more** individuals are affected, notify the FTC within **10 business days**; under 500, an annual log to the FTC within 60 days of calendar-year end. Media notice for 500+ residents of a state/jurisdiction. Third-party service providers to PHR vendors must notify the vendor.

**Enforcement:** GoodRx (2023, first HBNR action — ad-pixel sharing of health data) and Easy Healthcare/Premom set the pattern: unauthorized ad-tech disclosure treated as a breach, paired with FTC Act Section 5 counts. If you run a consumer health product with any analytics/advertising SDKs, assume the HBNR applies and audit the data flows.

## VPPA — Video Privacy Protection Act (brief)

1988 statute (18 U.S.C. § 2710) prohibiting "video tape service providers" — read by courts to include streaming and many video-bearing websites/apps — from knowingly disclosing personally identifiable information tying a person to specific videos requested/watched, without particularized consent. Carries a **private right of action with $2,500 statutory damages per person**, which fueled a major litigation wave over analytics/advertising pixels (notably the Meta Pixel) on pages with video content. Case outcomes on who counts as a "consumer" and what disclosure is "knowing" are split by circuit and still evolving — treat any pixel on video pages as a legal review item, and prefer consent-gated loading of third-party trackers on video content.

## DPPA and TCPA (very brief)

- **DPPA** (Driver's Privacy Protection Act, 1994): restricts obtaining/disclosing personal information from **state motor vehicle records** to enumerated permissible uses; private right of action with statutory damages. Relevant if your product ingests DMV data (insurance, mobility, background screening).
- **TCPA** (Telephone Consumer Protection Act, 1991): consent rules for calls and **texts** using autodialers/prerecorded voice, plus do-not-call rules; FCC regulations; **$500-$1,500 per call/text private right of action**, making it a top class-action generator. Any product sending SMS needs a TCPA consent and revocation workflow. FCC one-to-one consent rulemaking for lead generators saw litigation and reversals — verify current state.

## State sectoral laws — the consumer health data wave

The omnibus state privacy laws are covered in [us-state-privacy.md](us-state-privacy.md); on top of them sits a growing sectoral layer:

- **Washington My Health My Data Act (2023)** — the landmark: broad "consumer health data" definition (including inferences and data that *identifies health-seeking behavior*), opt-in **consent for collection** and separate consent for sharing, near-prohibition on selling health data without signed authorization, geofencing ban around health facilities, and — the sting — a **private right of action** via Washington's Consumer Protection Act. It reaches non-residents' data processed in Washington and companies far outside healthcare (wellness apps, retailers inferring health status).
- **Nevada SB 370** (2023) — similar consumer-health-data regime, no private right of action.
- **Connecticut** added consumer health data provisions into its omnibus law; other states have followed the pattern. Illinois **BIPA** (biometrics, private right of action, per-scan damages tempered by 2024 amendments) belongs on the same watchlist.
- State student-privacy laws (SOPIPA and analogues) supplement FERPA as noted above.

## Practical scoping — which of these applies to your product?

Ask these questions in order; each "yes" adds a regime:

1. **Could users be under 13, or is any content child-directed?** Child-directed content, child-appeal design, or actual knowledge of under-13 users → COPPA (and check the 2025 amendments). Teens under 18 increasingly trigger state teen-privacy and design codes — separate analysis.
2. **Does data come from or relate to K-12/higher-ed institutions?** Serving schools → FERPA school-official exception requirements + state student-privacy laws in every state you sell into.
3. **Does the product touch health data and sit outside HIPAA?** Any health, fitness, reproductive, or mental-health signal without a covered-entity/BA relationship → FTC HBNR + Washington MHMD-style state laws. If you *are* a covered entity or BA → [hipaa.md](hipaa.md) instead (and both, for mixed businesses).
4. **Is there video content plus third-party trackers?** → VPPA exposure; consent-gate the pixels.
5. **Do you send texts or make automated calls?** → TCPA consent workflow.
6. **Do you ingest DMV data?** → DPPA permissible-use analysis.
7. **Everything else personal-data-shaped** → the omnibus state laws ([us-state-privacy.md](us-state-privacy.md)) and FTC Act Section 5 unfairness/deception as the backstop — the FTC's data-security and dark-patterns cases apply to everyone.

## Key obligations for security/GRC teams

1. Maintain a data-map layer that tags **data types with regulatory significance** (child data, student records, health signals, video-viewing data, phone numbers for texting, DMV-sourced data) — sectoral scoping is impossible without it.
2. Audit third-party SDKs/pixels quarterly against the map: ad-tech data flows are the common thread in COPPA, HBNR, VPPA, and MHMD enforcement.
3. Build consent infrastructure that distinguishes regimes: VPC for COPPA, signed authorization for health-data sale under MHMD, particularized VPPA consent, TCPA opt-in/opt-out — one generic cookie banner satisfies none of them.
4. Put the HBNR's 60-day/10-business-day clocks into the incident-reporting matrix alongside HIPAA and state breach laws — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
5. For edtech: template the school-official-exception contract terms (direct control, purpose limitation, no re-disclosure, deletion) and honor them operationally.
6. Track litigation-driven regimes (VPPA, TCPA, BIPA, MHMD) in legal-risk reviews — statutory damages times a user base is the loss model, and it dwarfs regulator fines.

## Interplay

- [hipaa.md](hipaa.md) and [glba-ftc-safeguards.md](glba-ftc-safeguards.md) — the two big sectoral regimes this note deliberately excludes; scoping question 3 above routes between HIPAA and the HBNR.
- [us-state-privacy.md](us-state-privacy.md) — omnibus state laws layer on top of every sectoral hit; sensitive-data categories there (health, biometrics, children) overlap these regimes.
- [sec-cyber-disclosure.md](sec-cyber-disclosure.md) — a sectoral-law enforcement action or class action can itself be a material development for public companies.
- Privacy program structure and DSR handling: see [gdpr.md](gdpr.md) patterns and [../frameworks/iso-27701.md](../frameworks/iso-27701.md) for the management-system scaffolding these laws can hang on.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
