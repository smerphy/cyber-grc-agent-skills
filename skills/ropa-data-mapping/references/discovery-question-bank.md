# Discovery Question Bank — Interviews, System Sweeps, Shadow IT

Question sets and sweep tactics for finding the processing activities that actually exist. Use during Step 2 of the RoPA skill procedure. Interview the people who do the work; managers describe the org chart, practitioners describe the data.

## Interview technique (all functions)

- Open with **workflows, not data**: "walk me through what happens when a new employee joins / a lead comes in / a ticket arrives." People forget data; they do not forget their own process. Extract the data from the narrative.
- Always close with the four catch-alls:
  1. "What spreadsheets or exports do you keep outside the main system?"
  2. "What tools do you use that IT didn't give you?"
  3. "What do you do with the data when you're done with it?" (retention reality check)
  4. "Who outside your team — or outside the company — ever sees this data?"
- Ask for a screen-share of the actual tool over a verbal description whenever possible; the fields on screen beat the fields people remember.

## HR / People

- End-to-end hires: sourcing, ATS, referee checks, background screening (which vendor? which countries?), offer, onboarding. What happens to **rejected candidates'** data, and after how long?
- Payroll and benefits: which providers, which group entities, which countries? Beneficiary and dependant data (that's family members — a distinct data-subject category)?
- Absence and health: sickness records, occupational health, accommodations — Art. 9 data almost certainly present. Who can see it?
- **Employee monitoring**: endpoint agents, DLP, email scanning, call recording, badge/entry logs, productivity analytics, vehicle telematics. (Ask IT/security the same question — answers frequently differ.)
- Performance, disciplinary, grievance, and whistleblowing records; works-council or union data.
- Training records, photos on the intranet, emergency contacts, offboarding and post-employment retention.

## Marketing

- Every list: where did the addresses come from (forms, purchases, events, scraping, purchased lists)? Consent or legitimate-interest records per source?
- Website and product marketing tech: analytics, tag managers, pixels, session replay, A/B tools. Cross-site tracking and ad-platform audience uploads ("customer match" style uploads are disclosures — several US state laws treat them as sales/shares).
- CRM enrichment: any third-party data appended to contacts? Which vendor?
- Events and webinars: registration platforms, badge scans, attendee lists shared with sponsors?
- Suppression lists (ironic but real: the do-not-contact list is itself a processing activity).

## Product / Engineering

- Product telemetry and usage analytics: what events are captured, are user identifiers in them, where do they land (warehouse, third-party analytics)?
- **ML/AI training and evaluation datasets**: what production or customer data feeds model training, fine-tuning, or prompt logs? Retention of prompts/outputs? Vendor LLM APIs in the pipeline?
- Logs and observability: personal data in application logs, crash reports, APM traces? Retention?
- Production data in non-production: test databases seeded from production, developer laptop copies, support tooling with production access.
- Data warehouse/lake: which sources sync in, who has query access, are there derived datasets nobody owns?

## Finance

- Accounts payable/receivable: sole traders and contractor bank details are personal data. Credit checks on customers?
- Expense systems: receipts contain third-party personal data (travel companions, client entertainment).
- Fraud prevention and sanctions/AML screening: which lists, which vendor, what happens on a match?
- Statutory disclosures: tax authorities, auditors — routine recipient categories people forget to record.

## Support / Customer Service

- Ticketing and live chat: free-text fields collect whatever users paste — is there a redaction or handling procedure?
- Call recording and transcription (consent/notice? analytics on recordings? AI summarization vendors?).
- Remote-access/screen-share sessions into customer environments; support staff locations (third-country access = transfer).
- CRM case history retention; escalation exports to spreadsheets or chat channels.

## Security / IT (yes, security processes personal data too)

- SIEM and log aggregation: identities, IPs, URLs visited; retention period?
- Endpoint agents, EDR, DLP, CASB: what employee activity is captured?
- **CCTV**: locations, retention, who views, any analytics; visitor management systems.
- Access reviews, phishing-simulation results, insider-risk tooling, background-check involvement.
- Breach and incident records themselves (they contain data-subject information).

## System-sweep checklist

Run every sweep; each finds systems the interviews miss:

1. **SSO / identity provider application list** — every app integrated with Okta/Entra/etc.
2. **Procurement and vendor payment ledger** — every vendor invoice over 12–24 months; SaaS subscriptions bought on cards surface here.
3. **Expense reports** — the classic shadow-SaaS channel (individual subscriptions expensed monthly).
4. **DNS / secure web gateway / CASB logs** — SaaS domains with real traffic that appear in no register.
5. **DPA repository and contract system** — signed DPAs imply processing activities; reconcile both directions.
6. **Corporate app-store/marketplace installs** — browser extensions, Slack/Teams apps, CRM marketplace add-ons with data access.
7. **Cloud consoles** — projects/accounts and their data stores; orphaned buckets and forgotten databases.
8. **Email domain sweep** — automated senders (noreply@vendor) hitting the whole company reveal tools in active use.

## Shadow-IT and SaaS discovery tactics

- Reconcile the four lists against each other: SSO apps vs. finance ledger vs. CASB-observed domains vs. the current RoPA. Anything on one list but not the others is a lead.
- Announce an **amnesty**: ask teams to self-declare unofficial tools with no blame attached — discovery beats punishment, and punitive framing drives tools further underground.
- Watch for free-tier tools (no invoice, no SSO, real data): survey platforms, file converters, transcription and AI note-takers are the usual suspects.
- Re-run the sweeps on the review cadence, not once — shadow IT regrows at the rate of roughly one tool per team per quarter.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
