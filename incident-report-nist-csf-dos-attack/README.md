# Incident Report Analysis — DoS Attack (NIST CSF)

## Overview
Analysed a real-world DoS attack scenario affecting a multimedia company's 
internal network, using the National Institute of Standards and Technology 
Cybersecurity Framework (NIST CSF) as the structured response methodology. 
This activity was completed as part of the Google Cybersecurity Professional 
Certificate — Course 3: Connect and Protect: Networks and Network Security.

## Scenario Summary
A malicious actor launched a flood of ICMP ping packets through an 
unconfigured firewall, overwhelming the company's network in a Denial of 
Service (DoS) attack. Internal network services were unavailable for 
approximately two hours. The incident management team responded by blocking 
ICMP traffic, taking non-critical services offline, and restoring critical 
services.

## Framework Applied
**NIST Cybersecurity Framework (CSF)** — Five core functions:

| Function | Focus |
|----------|-------|
| Identify | Recognise assets at risk and the nature of the attack |
| Protect  | Implement safeguards to limit future impact |
| Detect   | Establish monitoring to identify incidents faster |
| Respond  | Contain, analyse, and neutralise the incident |
| Recover  | Restore affected systems and refine processes |

---

## My Analysis

### Identify
- **Attack type:** ICMP flood — Denial of Service (DoS)
- **Attack vector:** Unconfigured firewall with no ICMP rate limiting
- **Systems affected:** Entire internal network; all network resources 
  were unreachable during the attack
- **Root cause:** Absence of firewall rules to limit incoming ICMP packet 
  rate and no source IP verification to detect spoofed addresses

### Protect
Immediate and long-term protective measures recommended and implemented:
- Configured firewall rule to rate-limit incoming ICMP packets
- Enabled source IP address verification on the firewall to detect and 
  block spoofed IP addresses
- Established network access control policies to restrict unauthorised 
  traffic
- Recommended staff training on recognising and escalating network 
  anomalies promptly

### Detect
Detection improvements identified:
- Deployed network monitoring software to establish traffic baselines 
  and flag abnormal volume spikes
- Implemented an IDS/IPS system configured to filter suspicious ICMP 
  traffic based on known attack signatures
- Recommended regular firewall configuration audits to close future 
  misconfigurations before exploitation

### Respond
Response plan for future incidents:
- Isolate affected network segments immediately upon detection to 
  contain the incident
- Block malicious traffic at the firewall as the first line of response
- Take non-critical services offline to reduce load and protect 
  critical systems
- Conduct root cause analysis post-incident and document findings
- Notify relevant stakeholders with timely, transparent communications
- Report to appropriate authorities if the attack meets reportable 
  thresholds

### Recover
Recovery procedures established:
- Restore critical network services first; bring non-critical services 
  back online in a controlled, prioritised sequence
- Verify system integrity before reconnecting any isolated segments
- Review and update the incident response playbook based on lessons 
  learnt from this event
- Conduct a post-incident review with the security team to identify 
  any further gaps

---

## Skills Demonstrated
`Incident Report Analysis` `NIST CSF` `DoS/DDoS Attack Response`  
`Network Security` `Firewall Configuration` `IDS/IPS`  
`ICMP Flood Analysis` `Threat Detection` `Security Documentation`  
`Business Continuity Planning`

## Files
- [`incident-report-analysis.pdf`](./incident-report-analysis.pdf) — 
  Completed NIST CSF incident report
