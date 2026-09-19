# US State Data Breach Notification Laws (50-state patchwork: common structure and notable outliers)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | One statute per state, DC and territory — e.g. Cal. Civ. Code §1798.82; Tex. Bus. & Com. Code §521.053; N.Y. Gen. Bus. Law §899-aa; Fla. Stat. §501.171; RCW 19.255.010; C.R.S. 6-1-716; Md. Com. Law §14-3504; 73 P.S. §2301 et seq. (Pennsylvania BPINA); ORS 646A.604; Utah Code 13-44-202; P.R. Act 111-2005 |
| Regulators | State attorneys general (AG) almost everywhere; some states route to a consumer-protection department (Florida Department of Legal Affairs, Puerto Rico Department of Consumer Affairs), a financial regulator for licensees (Vermont DFR, New York DFS, Maine DPFR), or a cyber agency (Utah Cyber Center, Arizona Department of Homeland Security) |
| Status (Sept 2026) | Mature and continuously amended. 2024–2026 wave: New York fixed 30-day clock (Dec 2024); Utah AG/Cyber Center notice (May 2024); California SB 446 fixed 30-day consumer clock and 15-day AG clock (eff. 1 Jan 2026); Oklahoma SB 626 expanded definitions and added AG notice (eff. 1 Jan 2026) |
| Who is covered | Any person or business that "conducts business in" the state or owns/licenses/maintains computerized personal information of its residents — applicability follows the **residence of the individual**, not the location of the company or the data |
| Trigger | Unauthorized acquisition (Florida: unauthorized *access*) of unencrypted computerized personal information; most states add a risk-of-harm qualifier |
| Structure | Common skeleton: PI definition → breach definition and encryption safe harbor → investigation/risk-of-harm gate → notice to residents (timing, method, content) → notice to AG/regulator above a threshold → notice to consumer reporting agencies above a threshold → law-enforcement delay → enforcement |
| Deadlines | "Most expedient time possible and without unreasonable delay" everywhere; roughly half the states add an outer limit of 30, 45 or 60 days; Puerto Rico gives 10 days to the regulator |
| Penalties | Civil penalties under the state's unfair-trade-practices law or a dedicated schedule (e.g. Florida up to $500,000 per breach; Arizona up to $500,000 per breach or series; Virginia and Indiana up to $150,000 per breach/act; New York up to $250,000 for knowing or reckless failures). No private right of action in most breach statutes; California's private right sits in the CCPA (§1798.150), not §1798.82 |
| Neighbours | Federal sectoral rules (HIPAA, GLBA/FTC Safeguards, SEC Item 1.05) do not preempt state law; several states deem HIPAA/GLBA-compliant entities compliant but still require a copy of the notice or an AG filing. See [hipaa.md](hipaa.md), [glba-ftc-safeguards.md](glba-ftc-safeguards.md), [sec-cyber-disclosure.md](sec-cyber-disclosure.md), [us-state-privacy.md](us-state-privacy.md) |

## What it is

California's Civ. Code §1798.82 (in force since 2003 — verify) was the first breach notification statute; every other state, DC, Puerto Rico and the other US territories followed, with Alabama (Act 2018-396) and South Dakota (2018 — verify) completing the set. There is still no general federal breach notification law, so a multi-state incident is governed by the statute of every state in which an affected individual resides. The statutes share one design — because most were copied from California's — but diverge in the details that matter operationally: what counts as personal information, whether a risk-of-harm analysis can excuse notice, how many days you have, and who else must be told.

The second-generation amendments (2018 onward) added three things that security teams must now plan for: **fixed outer deadlines** (30/45/60 days) replacing open-ended "without unreasonable delay"; **AG or regulator notice** above resident-count thresholds (250 in Texas and Oregon, 500 in most others, 1,000 in Arizona and Virginia, *any* notification in Montana, Maine and Connecticut); and **broader personal-information definitions** covering medical, health-insurance, biometric, genetic, passport, military and online-credential data. A parallel trend layers **reasonable-security duties** (Massachusetts 201 CMR 17.00, Colorado C.R.S. 6-1-713.5, Delaware 6 Del. C. §12B-100, Louisiana R.S. 51:3074) and **cybersecurity safe-harbor statutes** (Utah 78B-4-702; Ohio and Connecticut — verify current text) on top of notification.

## Who it covers / Scope

- **Applicability test:** you hold computerized data containing a covered element about a resident of the state, and the data was (or is reasonably believed to have been) acquired by an unauthorized person. Doing business in the state is the nominal hook; in practice residency of the data subject controls. Governmental entities are covered by parallel provisions (e.g. Colorado C.R.S. 24-73-103; Utah 63A-19-405; Cal. Civ. Code §1798.29).
- **Owners/licensees vs maintainers:** the entity that *owns or licenses* the data notifies individuals and regulators; a **service provider that merely maintains** the data must notify the owner — "immediately following discovery" (California, Vermont), within 10 days (Maryland, Oregon vendors), "as soon as practicable" (Arizona) or "without unreasonable delay" (Virginia). Oregon vendors must also notify the AG directly if more than 250 consumers are affected and the covered entity has not. Contract for shorter windows; the statutory owner clock does not pause while the vendor investigates.
- **Personal information (baseline):** first name or initial plus last name, combined with an unencrypted SSN, driver's license or state ID number, or financial account/card number with any required access code. **Expansions now common:** passport and military ID (California, Colorado, Delaware, Virginia, Washington), tax ID (California), medical and health-insurance information (California, Colorado, Delaware, Florida, New York, Pennsylvania, Washington), biometric data (California, Colorado, Delaware, New York, Washington, Oklahoma from 2026), genetic data and DNA profile (California, Delaware), full date of birth (Washington), and **username or email plus password/security answers** as a standalone element (California, Washington, Vermont "login credentials").
- **Encryption safe harbor:** universal, but conditional — notice is required if the key or credential was also acquired (California, Colorado, Delaware, Pennsylvania, Texas, Virginia, Washington). Washington defines "secured" as encryption meeting or exceeding the NIST standard; Tennessee's safe harbor references FIPS 140-2. Publicly available government records are excluded.
- **Risk-of-harm gate:** many states allow no notice where a documented investigation finds no reasonable likelihood of misuse or harm (Arizona "substantial economic loss"; Florida "identity theft or any other financial harm"; Maryland, Utah, Maine "misuse"; Rhode Island "significant risk of identity theft"; Washington "risk of harm"). Several make the determination itself reportable or retainable: Florida (written determination to the department within 30 days, retained 5 years), Vermont (determination plus detailed explanation to the AG/DFR), Louisiana (retain 5 years, send to AG within 30 days of request), Maryland (retain records 3 years). California and Texas have **no** harm threshold — acquisition of covered data is enough.
- **Sector overlays:** entities compliant with HIPAA or GLBA breach procedures are deemed compliant in Delaware, Oregon, Utah and (for HIPAA) California, but Oregon still requires a copy of the notice to the AG and Colorado's AG notice still applies. New York DFS licensees must also notify DFS under §899-aa when covered by 23 NYCRR 500.

## Core obligations

### State-by-state matrix (verified against statute or the regulator's own page unless marked)

| State | Consumer deadline (clock start) | AG / regulator notice | CRA notice | Notable specifics |
|---|---|---|---|---|
| California (§1798.82, SB 446 eff. 1 Jan 2026) | 30 calendar days from discovery/notification | Sample notice to AG within 15 calendar days of notifying individuals if >500 residents | None in statute | Prescribed "Notice of Data Breach" template (What Happened? / What Information Was Involved? / What We Are Doing / What You Can Do / For More Information); biometric-breach instructions; substitute notice >$250k cost or >500,000 persons |
| Washington (RCW 19.255.010/.005) | 30 calendar days from discovery | AG within 30 days of discovery if >500 residents; update if facts unknown | None in statute | Broadest PI list (DOB, student/military/passport ID, health insurance, medical, biometric, credentials); "secured" = NIST-grade encryption |
| Florida (§501.171) | 30 days from determination | Department of Legal Affairs within 30 days if ≥500 (15-day extension for good cause in writing) | >1,000 | Trigger is unauthorized *access*; penalties $1,000/day (first 30 days), then $50,000 per 30-day period, max $500,000 per breach; harm waiver needs documented determination |
| Texas (§521.053, amended 2023) | 60th day after determination | AG within 30 days of determination if ≥250 residents (electronic form; AG publishes a public list) | >10,000 | Encrypted data in scope if intruder holds the key; no harm threshold |
| New York (GBL §899-aa, amended Dec 2024) | 30 days from discovery | AG, Department of State and State Police for every notified breach; DFS if a 23 NYCRR 500 covered entity | >5,000 | Medical and health-insurance data added; knowing/reckless failure: greater of $5,000 or $20 per failed notice, cap $250,000; 3-year limitation (6-year absolute) |
| Colorado (C.R.S. 6-1-716) | 30 days from determination | AG within 30 days of determination if ≥500 residents | >1,000 | "Determination" = sufficient evidence to conclude a breach occurred; AG notice applies even to HIPAA/GLBA entities; substitute notice >$250k or >250,000 residents |
| Maryland (Com. Law §14-3504) | 45 days from discovery/notification | AG **before** notifying individuals (any size) | Contact info only | Maintainer must notify owner within 10 days; no-notice determination records kept 3 years |
| Oregon (ORS 646A.604) | 45 days from discovery | AG if >250 consumers; vendors notify AG directly if >250 and the covered entity has not | >1,000 | Vendor-to-covered-entity notice within 10 days; HIPAA/GLBA entities exempt but must send the AG a copy of any notice |
| Rhode Island (§11-49.3-4) | 45 calendar days from confirmation (30 for state/municipal agencies) | AG if >500 residents | >500 | Trigger: "significant risk of identity theft"; public agencies also notify affected employees' bargaining agent |
| Vermont (9 V.S.A. §2435) | 45 days from discovery | AG (DFR for licensees): preliminary description within 14 business days of discovery or consumer notice, whichever sooner | >1,000 | Pre-sworn security-policy filing shortens AG step to "before consumer notice"; no-harm determinations must be filed with explanation |
| Arizona (A.R.S. §18-552) | 45 days from determination | AG and Dept of Homeland Security if >1,000 | >1,000 (three largest) | No notice if no reasonable likelihood of substantial economic loss; penalty lesser of $10,000 per individual or actual loss, max $500,000 per breach/series; substitute >$50k or >100,000 |
| Tennessee (§47-18-2107, 2017 amendment) | 45 days from discovery | None in statute | (verify) | Encryption safe harbor keyed to FIPS 140-2; "unauthorized person" expressly includes employees |
| Alabama (Act 2018-396) | 45 days (verify — AG page fetched, statute not) | AG where breach reasonably likely to cause substantial harm (threshold: verify) | (verify) | Data Breach Notification Act includes a reasonable-security duty (verify) |
| Indiana (IC 24-4.9) | Without unreasonable delay; 45-day outer limit from 2022 amendment (verify) | AG for every notified breach (form to DataBreach@atg.in.gov) | >1,000 | Penalty up to $150,000 per deceptive act; substitute >$250k or >500,000 |
| Connecticut (§36a-701b) | 60 days from discovery | AG no later than residents | (verify) | 24 months of credit monitoring where SSN/TIN compromised; violation = CUTPA offence |
| Delaware (6 Del. C. §12B-102) | 60 days from determination | AG if >500 residents, no later than resident notice | (verify) | 1 year free credit monitoring if SSN involved; PI includes passport, DNA profile, biometric, health insurance; reasonable-procedures duty (§12B-100) |
| Louisiana (R.S. 51:3074) | 60 days from discovery | Written reasons for any delay to AG within the 60 days; no-harm determination on AG request | (verify) | Reasonable-security duty in the same chapter; determinations retained 5 years |
| Pennsylvania (BPINA, Act 151 of 2022 eff. 2 May 2023) | Without unreasonable delay after determination; **7 business days** for state agencies, contractors, counties, public schools, municipalities | AG concurrently if >500 residents (state agencies always) | >500 | Adds medical (state-agency context) and health-insurance data; encryption mandated for state-agency data; AG has exclusive UTPCPL enforcement |
| Virginia (§18.2-186.6) | Without unreasonable delay | AG if >1,000; payroll/employer tax-withholding compromises always to AG | >1,000 | PI includes passport and military ID; penalty up to $150,000 per breach or series |
| Maine (10 M.R.S. §1348) | 30 days after becoming aware (absent law-enforcement delay) | DPFR regulators, or AG if unregulated — every notified breach | >1,000 | Law-enforcement delay capped at 7 business days after clearance |
| Montana (§30-14-1704) | Without unreasonable delay (no outer limit) | Electronic copy to AG Consumer Protection Office **simultaneously** with any notification | Coordination if notice references CRA files | Own-policy notification procedures deemed compliant if not unreasonably delayed |
| Utah (§13-44-202, amended 1 May 2024) | Most expedient time without unreasonable delay (no outer limit) | AG **and** Utah Cyber Center if ≥500 residents, with prescribed content (dates, counts, data types, description) | ≥1,000 | Governmental entities: Cyber Center + AG within 5 days of discovery (63A-19-405); safe harbor for written cybersecurity programs (78B-4-702) |
| Massachusetts (c. 93H; 201 CMR 17.00) | As soon as practicable and without unreasonable delay (verify exact text) | AG and Office of Consumer Affairs for every breach (verify) | — | 201 CMR 17.03 mandates a written information security program (WISP); 17.04 sets technical minima |
| Oklahoma (SB 626 eff. 1 Jan 2026 — secondary source) | Without unreasonable delay (verify) | AG within 60 days of notifying individuals if ≥500 residents | (verify) | First amendment since 2008; adds government ID numbers, unique electronic identifiers and biometrics to PI |
| Puerto Rico (Act 111-2005) | "Most expedite manner possible" | Department of Consumer Affairs within a **non-extendable 10 days** of detection; department publicises within 24 hours | — | Fines $500–$5,000 per violation, without prejudice to consumer damages claims |

### Content, method and substitute notice

- **Method:** written notice by mail is the default; electronic notice is accepted where consistent with the federal E-SIGN consent rules (15 U.S.C. §7001) or where email is the primary channel; some states allow telephone (Utah, Indiana).
- **Substitute notice** (email plus conspicuous website posting plus statewide media) is available when direct notice is infeasible; the thresholds vary — cost >$250,000 or >500,000 persons (California, Washington, Texas, Florida, Indiana), >$250,000 or >250,000 residents (Colorado), >$250,000 or >350,000 (Oregon), >$75,000 or >100,000 (Delaware), >$50,000 or >100,000 (Arizona, Virginia). Arizona also requires a letter to the AG justifying substitute notice and a 45-day website posting.
- **Content:** most statutes require date/estimated date of breach, categories of data, a description in general terms, contact information, and toll-free numbers for the FTC, the AG and the three nationwide CRAs. California prescribes headings and a title; Pennsylvania and Colorado prescribe AG-notice content; Utah prescribes AG/Cyber Center content. Delaware and Connecticut add mandatory credit-monitoring offers (1 year and 24 months respectively) when SSNs are involved.
- **Law-enforcement delay:** universal, on request of an agency that determines notice would impede a criminal investigation; Maine caps the post-clearance window at 7 business days; Louisiana requires written reasons to the AG for any delay.

### Reasonable security and safe-harbor statutes

- **Massachusetts 201 CMR 17.00:** every person holding a Massachusetts resident's PI must maintain a comprehensive written information security program (17.03) with a designated owner, risk assessment, third-party service-provider diligence and contract terms, at least annual review, and post-incident review; 17.04 requires secure authentication, encryption of PI in transit over public networks and on portable devices, monitoring, firewalls and patching, malware protection and training.
- **Statutory reasonable-security duties** sit beside the breach law in Colorado (6-1-713.5, plus disposal policy under 6-1-713 and third-party provider flow-down), Delaware (§12B-100), Louisiana (R.S. 51:3074) and New York (§899-bb SHIELD Act — verify current text). California's duty lives in Civ. Code §1798.81.5 (verify) and is the hook for CCPA §1798.150 statutory damages.
- **Affirmative-defense ("safe harbor") statutes:** Utah 78B-4-702 (2021) gives a defence to failure-to-secure, failure-to-respond and failure-to-notify claims where a written cybersecurity program reasonably conforms to a recognised framework listed in 78B-4-703 and is scaled to the entity; the defence is lost if the entity had actual notice of a threat and did not remediate in a reasonable time. Ohio's Data Protection Act (ORC 1354) and Connecticut's 2021 act follow the same pattern (verify current framework lists). Recognised frameworks generally include NIST CSF, NIST SP 800-53/171, ISO/IEC 27000 series, CIS Controls and, for regulated entities, HIPAA/GLBA/PCI DSS (verify each statute's list) — see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md).

## Enforcement and penalties

- **Who enforces:** the AG in nearly every state (Pennsylvania and Arizona make this exclusive), typically by treating a violation as an unfair or deceptive trade practice (Louisiana, Connecticut, Pennsylvania, Arizona) with the penalties of that statute; Florida's department and Puerto Rico's DACO enforce their own schedules.
- **Penalty ceilings verified in this pack:** Florida $500,000 per breach (daily accrual); Arizona $500,000 per breach or series; Virginia $150,000 per breach or series; Indiana $150,000 per deceptive act; New York $250,000 cap (knowing/reckless, $20 per failed notice); Puerto Rico $500–$5,000 per violation. Elsewhere the unfair-trade-practice statute's per-violation penalty applies and multiplies per affected resident.
- **Private actions:** most breach statutes are AG-only; California's CCPA §1798.150 ($100–$750 per consumer per incident for breaches caused by unreasonable security) is the main class-action driver; Puerto Rico and Virginia expressly preserve individual damages claims. Late or defective notices are routinely pleaded as evidence in negligence suits regardless of the statute.
- **Public disclosure:** AG postings (California, Texas — Texas maintains a public list updated within 30 days of each filing) and Puerto Rico's 24-hour public announcement mean regulator notices are effectively press releases; prepare communications accordingly.

## Timeline and status

| Date | Event |
|---|---|
| 2003 | California Civ. Code §1798.82 in force (verify date) — template for all later statutes |
| 2005 | Pennsylvania BPINA (Act 94); Puerto Rico Act 111 |
| 2015–2020 | Fixed outer limits and AG thresholds spread (Washington 2015 c 64 strengthened AG notice; Texas H.B. 4390 eff. 1 Jan 2020) |
| 2018 | Alabama Act 2018-396 (and South Dakota — verify) enact statutes — all 50 states covered |
| Nov 2022 → 2 May 2023 | Pennsylvania Act 151: 7-business-day clock for public bodies and contractors, AG notice >500, expanded PI |
| 1 Sept 2023 | Texas S.B. 768 amendment to §521.053 in force (current text: AG notice within 30 days of determination for ≥250 residents) |
| 1 May 2024 | Utah 2024 amendment (ch. 426, SB 98): AG and Cyber Center notice ≥500; governmental 5-day Cyber Center notice |
| Dec 2024 | New York §899-aa amendment: 30-day consumer clock, DFS added, medical/health-insurance data added |
| 3 Oct 2025 | California SB 446 signed (Stats. 2025 ch. 319) |
| 1 Jan 2026 | California 30-day/15-day clocks and Oklahoma SB 626 in force |
| Sept 2026 | No federal preemptive statute; state amendment cycle continues — re-verify each state at incident time |

## Key obligations for security/GRC teams

1. **Build the per-incident state grid from current statutes**, not from a static table: residency counts per state drive deadline, AG and CRA thresholds. Use [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and log every clock in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
2. **Fix the clock-start event in the incident record** — discovery (California, New York, Washington, Maryland, Oregon, Vermont, Louisiana, Tennessee), determination (Texas, Florida, Colorado, Arizona, Delaware), or confirmation (Rhode Island) — and timestamp it; "determination" states expect evidence that the investigation was prompt.
3. **Plan for the shortest clocks first:** Puerto Rico 10 days to DACO; Utah governmental 5 days; Pennsylvania public bodies 7 business days; Vermont AG 14 business days; California AG 15 days after consumer notice; 30-day states (California, Washington, Florida, New York, Colorado, Maine, Rhode Island public agencies). Maryland and Montana require the AG copy **before or simultaneously with** consumer notice.
4. **Map the expanded PI elements** (medical, health-insurance, biometric, genetic, passport, credentials) in the data inventory so scoping does not miss a triggering element — see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
5. **Maintain a documented risk-of-harm methodology** for states with a harm gate, and be ready to file the no-notice determination (Florida, Vermont, Louisiana) or retain it (Maryland 3 years, Louisiana 5 years).
6. **Flow vendor notice clocks into contracts** (Oregon 10 days, Maryland 10 days, "immediately" in California/Vermont) and require cooperation and information sharing — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
7. **Pre-approve notice templates** that satisfy California's headings and the strictest content rules, plus credit-monitoring offers for Connecticut (24 months) and Delaware (1 year) when SSNs are involved.
8. **Evidence a reasonable-security program** against a recognised framework to satisfy Massachusetts 201 CMR 17.00, Colorado 6-1-713.5 and the safe-harbor statutes — see [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
9. **Track amendments annually** (2024–2026 changed California, New York, Utah, Oklahoma, Pennsylvania, Texas) via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md); run [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md) as the playbook.

## Interplay

- **HIPAA:** a breach of PHI triggers the federal 60-day rule *and* state law; California, Delaware, Oregon and Utah deem HIPAA-compliant notice sufficient for individuals, but Oregon (copy to AG) and Colorado (AG notice ≥500) keep regulator filings alive. State PI definitions now reach medical and health-insurance data held by non-HIPAA entities. See [hipaa.md](hipaa.md).
- **GLBA / FTC Safeguards Rule:** the FTC's notification-event reporting runs alongside state law; Delaware, Oregon and Utah deem GLBA-compliant entities compliant for consumer notice. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- **SEC Item 1.05 and NYDFS Part 500:** public companies and New York financial licensees carry separate materiality-based and event-based regimes; the New York breach law now explicitly requires DFS notice for Part 500 covered entities. See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **State comprehensive privacy laws:** breach statutes predate and survive the CCPA-style laws; the CCPA's private right of action for breaches and its reasonable-security hook are separate from §1798.82. See [us-state-privacy.md](us-state-privacy.md).
- **Cross-regime clocks:** the full deadline comparison (GDPR 72 hours, NIS2, DORA, HIPAA, SEC, banking 36-hour rule) is in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## Primary sources

- Cal. Civ. Code §1798.82 (legal text, as amended by SB 446): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.82.&lawCode=CIV — California AG breach reporting page (regulator guidance): https://oag.ca.gov/privacy/databreach/reporting
- RCW 19.255.010 and 19.255.005 (legal text): https://app.leg.wa.gov/RCW/default.aspx?cite=19.255.010 ; https://app.leg.wa.gov/RCW/default.aspx?cite=19.255.005
- Fla. Stat. §501.171 (legal text): https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.171.html
- Tex. Bus. & Com. Code §521.053 (legal text via texas.public.law mirror; statutes.capitol.texas.gov returned navigation only): https://texas.public.law/statutes/tex._bus._and_com._code_section_521.053
- N.Y. Gen. Bus. Law §899-aa (legal text): https://www.nysenate.gov/legislation/laws/GBS/899-AA — NY AG breach reporting page: https://ag.ny.gov/resources/organizations/data-breach-reporting
- C.R.S. 6-1-716 (legal text via colorado.public.law): https://colorado.public.law/statutes/crs_6-1-716 — Colorado AG FAQ (regulator guidance): https://coag.gov/resources/data-protection-laws/
- Md. Com. Law §14-3504 (legal text): https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3504&enactments=false
- ORS 646A.604 (legal text via oregon.public.law): https://oregon.public.law/statutes/ors_646a.604
- R.I. Gen. Laws §11-49.3-4 (legal text): https://webserver.rilegislature.gov/Statutes/TITLE11/11-49.3/11-49.3-4.htm
- 9 V.S.A. §2435 (legal text): https://legislature.vermont.gov/statutes/section/09/062/02435
- A.R.S. §18-552 (legal text): https://www.azleg.gov/ars/18/00552.htm
- Tenn. Public Chapter via SB 547 (2017) bill text: https://www.capitol.tn.gov/Bills/110/Bill/SB0547.pdf (current code section not fetched)
- Alabama AG breach notification page (regulator guidance; statute not fetched): https://www.alabamaag.gov/data-breach-notification/
- Indiana AG breach FAQ (regulator guidance; statute not fetched): https://www.in.gov/attorneygeneral/consumer-protection-division/id-theft-prevention/security-breaches/security-breach-faqs-and-notification-form-for-businesses/
- Connecticut AG reporting page (regulator guidance; cga.ct.gov unreachable): https://portal.ct.gov/AG/Sections/Privacy/Reporting-a-Data-Breach
- 6 Del. C. ch. 12B (legal text): https://delcode.delaware.gov/title6/c012b/index.html
- La. R.S. 51:3074 (legal text): https://legis.la.gov/legis/Law.aspx?d=322030
- Pennsylvania BPINA, Act 94 of 2005 as amended (legal text): https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2005/0/0094..HTM — PA AG BPINA page: https://www.attorneygeneral.gov/report-a-data-breach/bpina/
- Va. Code §18.2-186.6 (legal text): https://law.lis.virginia.gov/vacode/title18.2/chapter6/section18.2-186.6/
- 10 M.R.S. §1348 (legal text): https://www.mainelegislature.org/legis/statutes/10/title10sec1348.html
- Mont. Code Ann. 30-14-1704 (legal text): https://archive.legmt.gov/bills/mca/title_0300/chapter_0140/part_0170/section_0040/0300-0140-0170-0040.html
- Utah Code 13-44-202, 63A-19-405, 78B-4-702 (legal text): https://le.utah.gov/xcode/Title13/Chapter44/13-44-S202.html ; https://le.utah.gov/xcode/Title63A/Chapter19/63A-19-S405.html ; https://le.utah.gov/xcode/Title78B/Chapter4/78B-4-S702.html
- 201 CMR 17.03 and 17.04 (regulation text via Cornell LII; mass.gov and malegislature.gov unreachable): https://www.law.cornell.edu/regulations/massachusetts/201-CMR-17-03 ; https://www.law.cornell.edu/regulations/massachusetts/201-CMR-17-04
- Puerto Rico Act 111-2005 (legal text, Spanish, LexJuris): https://www.lexjuris.com/lexlex/leyes2005/lexl2005111.htm
- Oklahoma SB 626 / California SB 446 summary (secondary — law-firm article; Oklahoma statute not fetched): https://natlawreview.com/article/2026-data-breach-law-updates-california-and-oklahoma
- Not reachable in this review: NCSL 50-state compilation (https://www.ncsl.org/technology-and-communication/security-breach-notification-laws), Mass. Gen. Laws c. 93H, Ohio Rev. Code 1349.19 and 1354, Illinois 815 ILCS 530, Wisconsin §134.98 — treat those states' specifics as unverified here.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
