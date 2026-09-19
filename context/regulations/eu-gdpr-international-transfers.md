# GDPR International Data Transfers (GDPR Chapter V, Arts. 44–50: adequacy, SCCs, BCRs, the EU-US Data Privacy Framework and transfer impact assessments)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Chapter V (Arts. 44–50) of Regulation (EU) 2016/679, plus the Commission implementing acts that hang off it: adequacy decisions (Art. 45(3)) and the standard contractual clauses in Implementing Decision (EU) 2021/914 (Art. 46(2)(c)) |
| Publisher / regulators | European Commission (adequacy findings, SCCs, periodic reviews); national supervisory authorities and the EDPB (BCR approval under the Art. 63 consistency mechanism, enforcement, guidance); Court of Justice of the EU (Schrems I C-362/14, Schrems II C-311/18) |
| Status and key dates | Chapter V applicable with the rest of the GDPR since 25 May 2018; new SCCs adopted 4 June 2021 (old SCCs repealed 27 September 2021, grandfathering ended 27 December 2022); EU-US Data Privacy Framework (DPF) adequacy decision adopted 10 July 2023, upheld by the General Court on 3 September 2025 (T-553/23) and now under appeal (C-703/25 P, lodged 31 October 2025); UK adequacy renewed 19 December 2025 to 27 December 2031; Brazil adequacy adopted 26 January 2026 |
| Who is covered | Any controller or processor whose processing is subject to the GDPR (Art. 3) and that discloses personal data to a separate controller or processor located in a third country or international organisation — including intra-group disclosures and remote access from outside the EEA (EDPB Guidelines 05/2021) |
| Structure | Art. 44 general principle (covers onward transfers) → Art. 45 adequacy → Art. 46 appropriate safeguards (SCCs, BCRs under Art. 47, codes, certifications, ad hoc clauses with SA authorisation) → Art. 49 derogations for specific situations; Art. 48 restricts compliance with third-country court/authority orders |
| Penalties / enforcement | Infringements of Arts. 44–49 fall in the top fine tier: up to EUR 20 million or 4% of total worldwide annual turnover, whichever is higher (Art. 83(5)(c)); SAs can order the suspension of data flows to a third-country recipient (Art. 58(2)(j)); the CJEU has twice invalidated a US adequacy decision |
| Assessment model | No certification of the exporter. Documented, exporter-led case-by-case assessment ("transfer impact assessment", TIA) is mandated by SCC Clause 14 and EDPB Recommendations 01/2020; adequacy decisions are the only route that dispenses with it |
| Relationship to neighbours | Sits on top of the core GDPR obligations in [gdpr.md](gdpr.md) (Art. 28 processor terms, Art. 30 records, Arts. 13–15 transparency all carry transfer-specific content); mirrored by the UK regime (IDTA / UK Addendum, UK Extension to the DPF) and the Swiss-US DPF, summarised in [other-jurisdictions.md](other-jurisdictions.md) |

## What it is

Chapter V exists so that the protection the GDPR gives natural persons is "not undermined" when personal data leaves the EU/EEA (Art. 44). It does not prohibit transfers; it makes every transfer conditional on one of three gates — an adequacy decision, an appropriate-safeguard instrument, or a narrow derogation — and it applies the same conditions to onward transfers from the importer to anyone else.

The Court of Justice has shaped the regime more than the legislator. Schrems I (C-362/14, 6 October 2015) invalidated the Safe Harbour decision; Schrems II (C-311/18, 16 July 2020) invalidated the Privacy Shield decision (2016/1250) because US surveillance law and the lack of an effective judicial remedy did not meet the "essentially equivalent" standard, while upholding SCCs on condition that exporters verify, transfer by transfer, that the clauses can actually be honoured in the destination country and add supplementary measures where they cannot. The Commission's 2021 SCCs, the EDPB's Recommendations 01/2020 and the 2023 EU-US DPF decision (built on Executive Order 14086 of 7 October 2022 and the Data Protection Review Court) are all direct responses to that judgment.

## Who it covers / Scope

The GDPR does not define "transfer". EDPB Guidelines 05/2021 (final version adopted 14 February 2023) set three cumulative criteria: (1) the exporter (controller or processor) is subject to the GDPR for the processing in question; (2) the exporter discloses by transmission or otherwise makes the data available to another controller, joint controller or processor (the importer); (3) the importer is in a third country or is an international organisation, whether or not the importer is itself subject to the GDPR under Art. 3(2).

| Situation | Transfer under Chapter V? | Source |
|---|---|---|
| EU subsidiary sends employee data to a non-EEA parent's central HR database | Yes — intra-group disclosures between separate legal entities are transfers | Guidelines 05/2021, Example 9 |
| Non-EEA processor is given remote access to data held on EU controllers' systems | Yes — remote access is "making available" | Guidelines 05/2021, Example 11 |
| Employee of an EU controller accesses the company database while travelling in a third country | No — same controller, internal processing (the controller still owes Art. 32 security for that access) | Guidelines 05/2021, Example 8 |
| Data subject in the EU submits their own data directly to a third-country website | No — disclosure by the data subject, not by a controller/processor exporter; the recipient may nevertheless be directly subject to the GDPR under Art. 3(2) | Guidelines 05/2021 |
| Non-EU controller subject to Art. 3(2) sends data to a non-EU processor | Yes — the exporter is subject to the GDPR even though it has no EU establishment; the 2021 SCCs may be used (recital 7 of Decision 2021/914) | Guidelines 05/2021; Decision 2021/914 |

Onward transfers count (Art. 44). Transit through a third country without processing there is not itself a transfer, but the EDPB expects exporters to consider access risk "during the transit of data" in the TIA (Recommendations 01/2020, para. 29). The UK and Switzerland are third countries for EU exporters but benefit from adequacy decisions.

## Core obligations

### The three gates (Arts. 45–49)

| Provision | What it requires | Practitioner notes |
|---|---|---|
| Art. 45 — adequacy | Transfer permitted without specific authorisation to a country, territory, sector or international organisation the Commission has found adequate. Elements assessed: rule of law and public-authority access to data, an independent supervisory authority, international commitments (Art. 45(2)). Decisions must be reviewed at least every four years (Art. 45(3)); the Commission monitors continuously and may repeal, amend or suspend (Art. 45(4)–(5)); Art. 46–49 routes remain available if a decision falls (Art. 45(7)) | Pre-GDPR decisions under Directive 95/46/EC remain in force (Art. 45(9)). Adequacy covers the destination, not the importer's own compliance — Art. 28 terms are still needed for a processor |
| Art. 46 — appropriate safeguards | Without SA authorisation: binding instruments between public bodies; BCRs; Commission SCCs; SA-adopted clauses approved by the Commission; approved codes of conduct (Art. 40) or certifications (Art. 42) with binding importer commitments. With SA authorisation (consistency mechanism): ad hoc contractual clauses; administrative arrangements between public bodies (Art. 46(3)–(4)). Enforceable data subject rights and effective remedies must be available (Art. 46(1)) | EDPB Guidelines 04/2021 (22 February 2022) and 07/2022 (version 2.0, 24 February 2023) explain how codes and certifications work as transfer tools; neither has yet displaced SCCs in practice |
| Art. 47 — BCRs | Group-wide rules approved by the competent SA under Art. 63; must be legally binding on every member including employees, confer enforceable rights on data subjects, and contain the fourteen elements in Art. 47(2)(a)–(n): group structure; transfers covered; binding nature; data protection principles including onward-transfer rules; data subject rights; acceptance of liability by an EU member; information to data subjects; DPO/compliance function; complaint procedures; audit/verification mechanisms reporting to the board and available to the SA; change reporting; SA cooperation; reporting of conflicting third-country legal requirements; training | EDPB Recommendations 1/2022 (controller BCRs; final version adopted after the consultation that closed 10 January 2023) set the application form and referential; Recommendations 1/2026 on processor BCRs were published for consultation in January 2026 (feedback closed 2 March 2026) — check for the final version before drafting new BCR-P |
| Art. 48 — foreign orders | A third-country court judgment or administrative decision requiring disclosure is recognisable or enforceable only if based on an international agreement (e.g. an MLAT), without prejudice to other Chapter V grounds | EDPB Guidelines 02/2024 (version 2.1, 4 June 2025): a disclosure in response to such a request is a transfer that needs both an Art. 6 legal basis and a Chapter V ground; an international agreement can supply both (Art. 6(1)(c)/(e) and Art. 46(2)(a)) |
| Art. 49 — derogations | Absent adequacy or safeguards, transfer only if: explicit informed consent; contract necessity (data subject's contract, or a contract in the data subject's interest); important public interest recognised in EU/Member State law; legal claims; vital interests; public register. Residual ground for non-repetitive transfers of a limited number of data subjects on compelling legitimate interests, with SA notification, data subject information and documentation of the assessment in the Art. 30 record (Art. 49(1) second subparagraph, Art. 49(6)). Consent/contract grounds are unavailable to public authorities exercising public powers (Art. 49(3)) | EDPB Guidelines 2/2018 (25 May 2018): derogations are exceptions, to be read narrowly and reserved for occasional transfers; not a basis for a systematic vendor relationship |

### Adequacy decisions in force (Commission list, September 2026)

| Destination | Notes |
|---|---|
| Andorra, Argentina, Canada (commercial organisations), Faroe Islands, Guernsey, Isle of Man, Israel, Jersey, New Zealand, Switzerland, Uruguay | Adopted under Directive 95/46/EC; first review report published 15 January 2024 |
| Japan | First periodic review report 4 April 2023 |
| Republic of Korea | First review of the 2021 decision concluded 23 July 2026 — Korea continues to be adequate |
| United Kingdom (GDPR and LED decisions) | Decision (EU) 2021/1772 of 28 June 2021; extended six months by Decision (EU) 2025/1226 (24 June 2025); renewed by Decision (EU) 2025/2574 (19 December 2025) after assessment of the Data (Use and Access) Act 2025; now expires 27 December 2031 unless extended; the former immigration-exemption carve-out was removed |
| United States — organisations on the Data Privacy Framework List | Decision (EU) 2023/1795 of 10 July 2023; see below |
| Brazil — controllers and processors subject to the LGPD | Decision (EU) 2026/179 of 26 January 2026; first evaluation after four years, then at least every four years (Art. 3(4)); adopted alongside a reciprocal Brazilian adequacy finding for the EU |
| European Patent Organisation | Only international organisation with a decision |

Except for the UK, these decisions do not cover law-enforcement transfers under Directive (EU) 2016/680.

### Standard contractual clauses — Implementing Decision (EU) 2021/914

| Element | Content |
|---|---|
| Scope (Art. 1) | Transfers from an exporter whose processing is subject to the GDPR to an importer whose processing is *not* subject to the GDPR; also satisfies Art. 28(3)–(4) for controller-to-processor and processor-to-sub-processor transfers. The Commission's SCC page states it is still developing an additional set for importers directly subject to the GDPR (Art. 3(2)) — none adopted as of September 2026 |
| Modules | Module One controller→controller; Two controller→processor; Three processor→processor; Four processor→controller |
| Clause 7 (optional docking) | New parties may accede by completing the Appendix and signing Annex I.A |
| Clause 9 (Modules Two/Three) | Sub-processor engagement under either specific prior authorisation or general written authorisation with an agreed list and a notice period the parties must specify; Annex III lists authorised sub-processors |
| Clause 13 | Competent SA named in Annex I.C; for Art. 3(2) exporters, the SA of the Art. 27 representative's Member State or of a Member State where affected data subjects are; importer submits to that SA's jurisdiction, audits and remedial measures |
| Clause 14 | Parties warrant they have no reason to believe destination laws and practices prevent the importer from complying; the warranty must account for the specific circumstances of the transfer, the destination laws on public-authority access, and any supplementary safeguards (Clause 14(b)); the assessment must be documented and made available to the SA on request (Clause 14(d)); importer must notify changes; exporter must suspend where safeguards cannot be ensured (Clause 14(e)–(f)) |
| Clause 15 | Importer must notify legally binding public-authority requests and direct access where possible, seek waivers of gagging orders, review legality and challenge unlawful requests, disclose the minimum, and keep records for the SA |
| Clauses 17–18 | Governing law of an EU Member State allowing third-party beneficiary rights (Module Four: any country allowing such rights); disputes before EU Member State courts |
| Annexes | I.A parties, I.B description of transfer, I.C competent SA; II technical and organisational measures; III sub-processors |
| Transition (Art. 4) | Decisions 2001/497/EC and 2010/87/EU repealed 27 September 2021; contracts concluded before that date stayed valid until 27 December 2022 if the processing was unchanged |

The SCCs do not replace the exporter's own duties (recital 3): Art. 13(1)(f)/14(1)(f) require notices to state the intention to transfer, whether an adequacy decision exists and how to obtain a copy of the safeguards; Art. 15(2) gives data subjects a right to be informed of the Art. 46 safeguards; Art. 30(1)(e) records must identify third countries and, for Art. 49 residual transfers, document the safeguards.

### EU-US Data Privacy Framework — Implementing Decision (EU) 2023/1795

| Element | Detail |
|---|---|
| Finding (Art. 1) | The US ensures adequate protection for data transferred to organisations on the Data Privacy Framework List maintained by the US Department of Commerce (DoC) |
| Eligibility and mechanics | Voluntary self-certification to the DoC by organisations subject to FTC or Department of Transportation jurisdiction; public privacy policy adhering to the Principles; annual re-certification, failing which the organisation is removed from the List; HR data must be expressly opted into. Removed organisations must keep applying the Principles, protect the data by another authorised means (e.g. SCCs) or return/delete it |
| Principles | Notice; Choice; Accountability for Onward Transfer (contract requiring the same level of protection, limited purposes); Security; Data Integrity and Purpose Limitation; Access; Recourse, Enforcement and Liability (independent recourse mechanism free to the individual; binding arbitration panel as last resort) |
| Government access safeguards | EO 14086 (7 October 2022) necessity/proportionality limits on signals intelligence; two-tier redress: ODNI Civil Liberties Protection Officer, then the Data Protection Review Court (DPRC), complaints routed via EU DPAs; EU/EEA designated a "qualifying state" on 30 June 2023 |
| Enforcement | FTC Act Section 5 (15 U.S.C. § 45) or 49 U.S.C. § 41712; DoC compliance questionnaires, spot checks and referrals; Member States must inform the Commission when they suspend DPF transfers (Art. 2) |
| Review (Art. 3) | Continuous monitoring; first evaluation one year after notification; Commission may suspend, amend or repeal under Art. 45(5). First review report COM(2024) 451 (9 October 2024) concluded the framework functions effectively and set the next periodic review after three years; EDPB report of 4 November 2024 asked for the next review "within three years or less" |
| Sister arrangements | UK Extension ("UK-US data bridge"): Data Protection (Adequacy) (United States of America) Regulations 2023, SI 2023/1028, in force 12 October 2023 — importer must be on the DPF List *and* certified to the UK Extension; journalistic data excluded. Swiss-US DPF: Federal Council decision 14 August 2024, Annex 1 of the Swiss Data Protection Ordinance amended with effect from 15 September 2024 |

### Transfer impact assessment — the facts a TIA must cover

Neither the GDPR nor Schrems II uses the term "TIA". The obligation is the combination of SCC Clause 14 and EDPB Recommendations 01/2020 (version 2.0, 18 June 2021), whose six steps are: (1) know your transfers (map them, including onward transfers, and check minimisation); (2) identify the transfer tool relied on; (3) assess whether that tool is effective in light of the destination's law *and practice* on public-authority access, focusing on legislation relevant to the specific data transferred; (4) adopt supplementary measures (technical, contractual, organisational) where it is not; (5) complete procedural steps (no SA authorisation is needed to add measures to SCCs, provided they do not contradict the clauses); (6) re-evaluate at appropriate intervals and suspend where the importer cannot honour its commitments.

| EDPB use case (Annex 2) | Effective technical measure? |
|---|---|
| 1 — Backup/storage with no access needed in the destination, strong encryption, keys held by exporter in the EEA | Yes |
| 2 — Transfer of pseudonymised data where additional information stays in the EEA | Yes |
| 3 — Encrypted transit through a third country | Yes |
| 4 — Importer specifically protected by destination law (e.g. professional privilege) | Yes |
| 5 — Split or multi-party processing with no party able to reconstruct the data | Yes |
| 6 — Cloud provider or processor needing access to data in the clear | No — the EDPB "is incapable of envisioning an effective technical measure"; encryption at rest with importer-held keys does not suffice |
| 7 — Business use or remote access to data in the clear (e.g. shared HR or CRM systems) | No |

Contractual and organisational measures (transparency reports, request-challenge commitments, internal policies) support but cannot by themselves cure a problematic legal environment. The assessment must be documented and producible to the SA (Clause 14(d)); for DPF-listed importers no TIA is required because the adequacy decision covers the destination.

## Enforcement and penalties

| Lever | Detail |
|---|---|
| Administrative fines | Arts. 44–49 infringements: up to EUR 20 million or 4% of worldwide annual turnover (Art. 83(5)(c)); non-compliance with an SA order to suspend data flows sits in the same tier (Art. 83(5)(e)) |
| Corrective powers | Suspension of data flows to a third-country recipient (Art. 58(2)(j)); processing bans; SCC Decision Art. 2 and DPF Decision Art. 2 oblige Member States to inform the Commission of such suspensions |
| Judicial invalidation | Safe Harbour (2015) and Privacy Shield (2020) were struck down with immediate effect; Art. 45(7) preserves Art. 46–49 routes when a decision falls, which is why exporters keep SCCs as a fallback for DPF importers |
| Importer-side enforcement | DPF: FTC/DoT deceptive-practice enforcement, DoC removal from the List and obligation to return or delete data; SCCs: third-party beneficiary rights for data subjects, importer submission to the EU SA and EU courts |
| Civil liability | Art. 82 compensation and Art. 79 remedies apply to unlawful transfers as to any other infringement — see [gdpr.md](gdpr.md) |

## Timeline and status

| Date | Event |
|---|---|
| 6 Oct 2015 | Schrems I (C-362/14) invalidates Safe Harbour |
| 25 May 2018 | GDPR applies; EDPB Guidelines 2/2018 on Art. 49 derogations adopted the same day |
| 16 Jul 2020 | Schrems II (C-311/18) invalidates Privacy Shield, upholds SCCs subject to case-by-case assessment |
| 4 Jun 2021 | Implementing Decision (EU) 2021/914 (new SCCs); old SCCs repealed 27 Sep 2021, grandfathering ends 27 Dec 2022 |
| 18 Jun 2021 | EDPB Recommendations 01/2020 on supplementary measures, version 2.0 |
| 28 Jun 2021 | UK adequacy decisions (EU) 2021/1772 (GDPR) and LED equivalent, with four-year sunset |
| Mar 2022 | UK IDTA and Addendum to the EU SCCs take effect (laid before Parliament 2 February 2022 under s.119A DPA 2018) |
| 7 Oct 2022 | US Executive Order 14086 on signals-intelligence safeguards, later supplemented by the Attorney General regulation establishing the DPRC |
| 14 Feb 2023 | EDPB Guidelines 05/2021 (Art. 3 / Chapter V interplay) final version; Guidelines 07/2022 on certification as a transfer tool follow on 24 Feb 2023 |
| 10 Jul 2023 | EU-US DPF adequacy decision (EU) 2023/1795 |
| 12 Oct 2023 | UK Extension to the DPF in force (SI 2023/1028) |
| 15 Sep 2024 | Swiss-US DPF in force |
| 9 Oct 2024 / 4 Nov 2024 | Commission first DPF review report COM(2024) 451; EDPB report; next review after three years (indicatively 2027) |
| 4 Jun 2025 | EDPB Guidelines 02/2024 on Art. 48 (version 2.1) |
| 19 Jun 2025 / 24 Jun 2025 | UK Data (Use and Access) Act Royal Assent; Commission extends UK adequacy to 27 Dec 2025 |
| 3 Sep 2025 | General Court dismisses Latombe v Commission (T-553/23): DPRC sufficiently independent, bulk collection subject to ex post review acceptable |
| 31 Oct 2025 | Latombe appeal lodged (C-703/25 P, four grounds); pending before the Court of Justice as of September 2026 — no judgment located (verify) |
| 19 Dec 2025 | Decision (EU) 2025/2574 renews UK adequacy to 27 Dec 2031 |
| 15 Jan 2026 | ICO republishes its international-transfers guidance for the Data (Use and Access) Act "data protection test" (standard in the destination "not materially lower" than the UK's — new Arts. 45B and 46(1A) UK GDPR); ICO states it plans to update the IDTA and Addendum during 2026; the transfer provisions commenced 5 February 2026 (verify) |
| Jan–Mar 2026 | EDPB draft Recommendations 1/2026 on processor BCRs; consultation closed 2 March 2026 |
| 26 Jan 2026 | Brazil adequacy decision (EU) 2026/179 |
| 29 Jun 2026 | US Supreme Court, Trump v. Slaughter (No. 25-332): FTC commissioners' for-cause removal protection unconstitutional, Humphrey's Executor overruled |
| 31 Jul 2026 | EDPB letter asks the Commission to "closely assess" whether Slaughter affects Decision (EU) 2023/1795, noting recitals 58–60 relied on FTC independence and Art. 45(2)(b) requires an independent supervisory authority; the Commissioner publicly stated the EU "remains committed" to the DPF (July 2026, secondary reporting — verify) |
| Pending | Latombe appeal; Commission's additional SCCs for Art. 3(2) importers (announced, not adopted); final BCR-P recommendations; ICO IDTA/Addendum refresh; DPF second review (~2027); reported loss of PCLOB quorum since January 2025 (secondary reporting — verify) |

Practical reading as of September 2026: the DPF is valid and usable, but it carries live legal risk on two fronts (the C-703/25 P appeal and the FTC-independence question). Programs that rely on it should hold executed SCCs and a current TIA for the same importers as a contingency.

## Key obligations for security/GRC teams

1. **Build and maintain a transfer map** from the Art. 30 record: every disclosure to a non-EEA entity (including group companies, sub-processors and remote support access), destination country, transfer tool, and onward transfers. Applicability screening: [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Assign a gate to every transfer** in priority order — adequacy (check the importer is on the DPF List and certified for the data type), then SCCs/BCRs, then derogations only for genuinely occasional cases with Art. 49(6) documentation.
3. **Execute and manage the 2021 SCCs correctly**: right module, Annex I.B description, Annex II TOMs that match what is actually deployed, sub-processor notice period in Clause 9, competent SA in Annex I.C; confirm no pre-27 September 2021 clauses survive in renewed contracts. Vendor diligence: [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
4. **Document a TIA for each SCC/BCR destination** following the EDPB six steps and Clause 14(b) elements; record the supplementary measures (encryption with EEA-held keys, pseudonymisation, split processing) and the legal analysis; keep it producible to the SA. Risk method: [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
5. **Evidence the technical measures** the TIA relies on — key custody, pseudonymisation design, access logs for third-country support — through control testing: [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Run a government-access request procedure** matching SCC Clause 15 / DPF commitments: intake, legality review, challenge, minimum disclosure, exporter notification, and an Art. 48 check against EDPB Guidelines 02/2024 for requests received by EU entities. Reporting overlaps: [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
7. **Track transfer-specific exceptions** (e.g. reliance on derogations, importers with unresolved TIA findings) with owners and expiry dates: [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
8. **Horizon-scan the moving parts** — the Latombe appeal, Commission monitoring of the DPF after Trump v. Slaughter, additional SCCs, BCR-P recommendations, ICO IDTA refresh, adequacy reviews — and pre-plan the SCC fallback for DPF importers: [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
9. **Fold transfers into DPIAs and policy**: a DPIA for processing involving third-country importers must reference the transfer tool and TIA outcome ([../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md)); the data protection policy should fix the gate hierarchy and approval roles ([../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md)).

## Interplay

- **Core GDPR** ([gdpr.md](gdpr.md)): Art. 28(3)(a) requires processors to follow documented instructions "including with regard to transfers"; Art. 32 security measures are the raw material for supplementary measures; Art. 13/14/15 notices and access responses must describe transfers and safeguards; Art. 35 DPIAs should capture transfer risk.
- **UK regime** ([other-jurisdictions.md](other-jurisdictions.md)): UK GDPR Chapter V is close to the EU text but now applies the DUAA "data protection test"; tools are the IDTA, the UK Addendum to the EU SCCs, UK BCRs and the UK Extension to the DPF. EU→UK flows rely on the renewed EU adequacy decision (to 27 December 2031); UK→EU flows rely on the UK's own adequacy regulations.
- **Switzerland**: Swiss exporters use the Swiss-US DPF (from 15 September 2024); EU exporters transferring to Switzerland rely on the EU adequacy decision.
- **DORA and NIS2** ([dora.md](dora.md), [nis2.md](nis2.md)): DORA Art. 30 contract terms on data-processing locations and NIS2 supply-chain duties overlap with the transfer map — maintain one register that serves the Art. 30 GDPR record, the DORA register of information and the TIA inventory.
- **EU AI Act** ([eu-ai-act.md](eu-ai-act.md)): training or inference data sent to non-EEA model providers is a transfer; the AI system intake should capture the transfer tool alongside AI-Act classification ([../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md)).
- **US state privacy laws** ([us-state-privacy.md](us-state-privacy.md)) and the FTC Act underpin importer-side enforcement of DPF commitments but impose no reciprocal export restrictions.
- **Frameworks**: ISO/IEC 27001:2022 and SOC 2 reports are the usual evidence for Annex II TOMs and for the technical supplementary measures ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/soc2-tsc.md](../frameworks/soc2-tsc.md)); map them via [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- Regulation (EU) 2016/679, Chapter V (Arts. 44–50), Arts. 13–15, 28, 30, 58, 83 — legal text (Publications Office, CELEX 32016R0679).
- Commission Implementing Decision (EU) 2021/914 on standard contractual clauses, 4 June 2021 — legal text (CELEX 32021D0914).
- Commission Implementing Decision (EU) 2023/1795 on the EU-US Data Privacy Framework, 10 July 2023 — legal text (CELEX 32023D1795).
- Commission Implementing Decision (EU) 2025/2574 renewing UK adequacy, 19 December 2025 — legal text (CELEX 32025D2574).
- Commission Implementing Decision (EU) 2026/179 on Brazil, 26 January 2026 — legal text (CELEX 32026D0179).
- Appeal notice C-703/25 P, Latombe v Commission, OJ C/2025/6610 — legal text (CELEX 62025CN0703); CJEU press release 106/25 on T-553/23 (curia.europa.eu) — court communication.
- European Commission, adequacy decisions page and SCC page (commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/) — regulator guidance; Report COM(2024) 451 on the first DPF review — regulator report.
- EDPB Recommendations 01/2020 v2.0 (18 June 2021); Guidelines 05/2021 (14 February 2023); Guidelines 02/2024 on Art. 48 v2.1 (4 June 2025); Guidelines 2/2018, 04/2021 and 07/2022 landing pages; Recommendations 1/2022 and 1/2026 (BCR) pages; report of 4 November 2024 on the first DPF review; letter of 31 July 2026 on Trump v. Slaughter — regulator guidance (edpb.europa.eu).
- UK: Data Protection (Adequacy) (United States of America) Regulations 2023, SI 2023/1028 (legislation.gov.uk) — legal text; ICO international-transfers guidance pages (ico.org.uk, updated 15 January 2026) — regulator guidance (some sub-pages could not be retrieved).
- Switzerland: Federal Council media release of 14 August 2024 on the Swiss-US DPF (admin.ch) — government notice.
- US: Supreme Court opinion Trump v. Slaughter, No. 25-332 (29 June 2026) — court text. The Department of Commerce DPF site (dataprivacyframework.gov) could not be retrieved; DPF mechanics above are taken from Annex I of Decision (EU) 2023/1795.
- Secondary (not fetched from the primary publisher): reporting on the Commissioner's July 2026 statement, PCLOB quorum status and the DUAA commencement date — all marked "(verify)" above.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
