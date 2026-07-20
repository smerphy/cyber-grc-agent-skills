# ePrivacy Directive (2002/58/EC, as amended by 2009/136/EC)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Directive 2002/58/EC ("ePrivacy Directive"), amended 2009 (the "Cookie Directive" amendments) — binds via each member state's national implementing law |
| In force | Original directive 2002; the 2009 amendments were due in national law by May 2011 |
| Who is covered | Cookie/terminal-equipment rules and direct-marketing rules apply to **anyone** targeting users in the EU, not just telecoms; confidentiality and traffic/location-data rules apply to providers of electronic communications services |
| Core obligations | Confidentiality of communications, consent for storing/accessing information on terminal equipment (Art. 5(3)), traffic and location data limits, opt-in electronic direct marketing (Art. 13) |
| Consent standard | GDPR-grade consent (freely given, specific, informed, unambiguous) — the directive imports the GDPR definition |
| Maximum fines | Set nationally — ranges from modest fixed sums to GDPR-level percentages depending on member state; French CNIL cookie fines have reached hundreds of millions of euros under national law |
| Regulators | Varies by member state: data protection authorities in most, telecom or consumer regulators for some provisions in others |
| Replacement | The proposed ePrivacy Regulation stalled for years; the Commission signalled withdrawal of the proposal in its 2025 work programme — verify current status |

## What it is

The ePrivacy Directive is the EU's *lex specialis* for privacy in electronic communications. It predates the GDPR and survives it: where both could apply, ePrivacy's specific rules take precedence, with the GDPR filling the gaps (including supplying the definition of consent and the sanctions regime in many member states). For most organizations outside telecoms, its practical footprint is two things: **cookie/tracking consent** and **electronic direct-marketing rules**.

Because it is a directive implemented 27+ different ways, there is no single "ePrivacy law" to comply with — there are national laws (Germany's TDDDG, France's Loi Informatique et Libertés provisions enforced by CNIL, Spain's LSSI, the UK's PECR — see [./uk-data-protection.md](./uk-data-protection.md)), with real variance in exemptions, enforcement style, and penalties. A multi-country cookie or marketing program must be built to the strictest applicable interpretation or localized per market.

## Core provisions

### Confidentiality of communications (Art. 5(1))

Listening, tapping, storage, or other interception or surveillance of communications and related traffic data is prohibited without the consent of the users concerned, except where legally authorised. This is the hook regulators have used against communications scanning and some analytics practices that touch message content.

### Terminal equipment: the cookie rule (Art. 5(3))

Storing information, or gaining access to information already stored, in a user's terminal equipment requires that the user **has given consent, having been provided with clear and comprehensive information**. Key points practitioners get wrong:

- **Technology-neutral.** It covers cookies, localStorage, pixels, SDKs, fingerprinting techniques that access device information, and any other storage/access on the device — not just cookies.
- **Not limited to personal data.** The rule protects the terminal equipment; it applies even where the data accessed is not personal data under the GDPR.
- **Two exemptions only:** (a) storage/access for the sole purpose of carrying out the transmission of a communication, and (b) storage/access **strictly necessary** to provide an information-society service **explicitly requested** by the user. Analytics, advertising, and most personalization do not qualify. A few member states have carved out narrow first-party low-risk analytics exemptions in national law or regulator guidance (e.g., CNIL's exempted-analytics conditions) — verify per country.
- **Consent = GDPR consent.** Since the GDPR replaced Directive 95/46/EC, Art. 5(3) consent must meet the GDPR standard. The CJEU's *Planet49* judgment (C-673/17) confirmed pre-ticked boxes are invalid and information must cover cookie lifespan and third-party access. Scrolling, continued browsing, and cookie walls that offer no genuine choice are not valid consent under EDPB guidance (cookie-wall acceptability varies by national regulator — verify).

### Traffic and location data (Arts. 6 and 9)

Providers of public electronic communications services must erase or anonymise traffic data when no longer needed for transmission, with limited retention for billing; location data other than traffic data requires anonymisation or consent. Primarily a telecom-operator concern, but relevant to OTT communications services brought into scope by the European Electronic Communications Code's expanded definitions.

### Security and breach notification (Art. 4)

Providers of publicly available electronic communications services must take appropriate security measures and notify **personal data breaches** to the competent national authority — under Regulation (EU) 611/2013, within **24 hours** of detection where feasible — and affected subscribers where the breach is likely to adversely affect them. This sits alongside, and for telecom providers predates, GDPR Art. 33. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

### Direct marketing (Art. 13)

- **Opt-in** consent is required for unsolicited direct marketing by email, SMS, automated calling machines, and fax.
- **Soft opt-in exception:** a company may email existing customers about its **own similar products or services** using contact details obtained in the context of a sale, provided the customer was given a clear, free opt-out at collection and in every message.
- Marketing emails must not disguise or conceal the sender's identity and must include a valid opt-out address.
- Live voice calls follow national opt-in or opt-out choices (member states chose different models; several run do-not-call registries).

B2B treatment varies by member state — some national laws exempt corporate subscribers from parts of Art. 13. Verify per market before running B2B email campaigns.

## Enforcement

Enforcement authority is nationally assigned: most member states give the cookie and marketing rules to the data protection authority, but some split them with telecom or consumer-protection regulators. Two practical consequences:

- **Penalty exposure varies widely.** Some states apply GDPR-style fine ceilings to ePrivacy breaches via national law; France's CNIL has issued its largest fines ever under the national cookie rules (against major platforms, in the hundreds of millions of euros) — notably *without* needing GDPR's one-stop-shop, because ePrivacy has no lead-authority mechanism.
- **No one-stop-shop.** Unlike the GDPR, each national regulator can enforce independently against a company targeting its market. Pan-EU operators can face parallel proceedings in multiple countries over the same banner.

## The stalled ePrivacy Regulation

The Commission proposed an ePrivacy Regulation in January 2017 to replace the directive, harmonise the rules, and align them fully with the GDPR. It never cleared trilogue: member states could not agree on data retention, browser-level consent, and machine-to-machine scope. After eight years of deadlock, the Commission's 2025 work programme listed the proposal for **withdrawal**, citing no foreseeable agreement. As of mid-2026, the directive-plus-national-laws patchwork remains the operative regime, and any successor initiative (potentially folded into a broader digital-rules review) should be tracked rather than assumed — verify current status before making roadmap bets on harmonisation.

## Key obligations for security/GRC teams

A defensible cookie/tracking compliance program contains:

1. **A maintained tracker inventory.** Regular automated scans of web properties and apps for cookies, pixels, SDKs, and fingerprinting scripts; each tracker mapped to purpose, duration, first/third party, and legal basis (exempt vs consent-required). Untagged marketing scripts are the most common audit finding.
2. **Prior consent, technically enforced.** Non-exempt trackers must not fire before consent — banner presence is not compliance; tag-manager gating is. Test with the banner rejected and cleared.
3. **A compliant banner/CMP:** clear information (purposes, third parties, duration), **reject as easy as accept** at the first layer (explicit regulator position in France, Germany, and others — verify per market), granular per-purpose choices, no pre-ticked boxes, no dark patterns, and easy withdrawal (persistent icon or settings link).
4. **Consent records and signal propagation.** Store consent state as evidence (who, when, what version of the notice); propagate it downstream (e.g., via IAB TCF or equivalent) and honour withdrawal within the stack. Reconcile with GDPR records of processing — see [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
5. **Marketing-consent hygiene:** opt-in capture with soft-opt-in eligibility flags, suppression-list management honoured across ESPs, opt-out in every message, and B2B/B2C rules localized per member state.
6. **Per-market variance register.** Track national analytics exemptions, cookie-wall positions, and regulator guidance (CNIL, the German DSK, Garante, AEPD each publish detailed cookie guidance) as part of horizon scanning — see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **GDPR:** ePrivacy is *lex specialis* — for storing/accessing data on devices and for electronic marketing, Art. 5(3)/Art. 13 govern the trigger, and the GDPR governs everything downstream (the subsequent processing of personal data collected via the tracker needs its own Art. 6 basis, usually the same consent). Consent standard, transparency, and data-subject rights all come from the GDPR. One banner therefore does double duty; design it to satisfy both. See [./gdpr.md](./gdpr.md).
- **UK PECR:** the UK's implementation of the ePrivacy Directive survives Brexit and continues to evolve independently (including reform via the Data (Use and Access) Act 2025). See [./uk-data-protection.md](./uk-data-protection.md).
- **EU AI Act:** ad-tech profiling built on tracker data can intersect with AI Act transparency duties where AI systems are involved; no direct mechanical overlap, but consent provenance becomes training-data governance input. See [./eu-ai-act.md](./eu-ai-act.md).
- **Digital Services Act / Digital Markets Act:** dark-pattern prohibitions and consent-or-pay scrutiny for large platforms overlap the same banner design choices — coordinate legal review rather than treating ePrivacy in isolation.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
