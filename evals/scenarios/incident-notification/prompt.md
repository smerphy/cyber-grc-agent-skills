# Scenario: multi-regime incident notification

Load and follow: `skills/incident-regulatory-reporting/SKILL.md`, with `context/crosswalks/breach-notification-timelines.md` as reference. Produce the skill's notification decision table deliverable.

## Task

We have an active incident and need to know what to file, where, and by when.

- Company: Tarn Health Analytics — US company, HIPAA **business associate** processing patient data for 40 US hospital systems (covered entities). Also operates a direct-to-consumer wellness app (not offered in the EU) with 1.2M US users, including ~210,000 California residents. NYSE-listed.
- Incident: attacker accessed a misconfigured analytics bucket. Detected **Mon 6 July 2026, 14:00 UTC**; forensics confirmed on **8 July 18:00 UTC** that the bucket contained unencrypted PHI for ~620,000 patients across 12 hospital-system clients, plus wellness-app account data (emails, hashed passwords, weight/sleep logs) for ~300,000 app users.
- The wellness app is not connected to any covered entity — Tarn is the business operating it directly.
- Materiality committee meets 9 July; no determination yet. No ransomware, no operational outage. Cyber insurance policy in force.

Identify every notification obligation, the correct clock-start event and deadline for each, the recipient, and what is NOT triggered (with rationale). Flag anything requiring counsel.
