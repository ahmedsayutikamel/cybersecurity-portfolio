# Incident Handler's Journal

## Overview
Maintained a structured incident handler's journal throughout the 
Google Cybersecurity Professional Certificate — Course 6: Sound the 
Alarm: Detection and Response. The journal documents real hands-on 
investigations, tool usage, and reflections across multiple cybersecurity 
incidents and lab activities, demonstrating practical detection and 
response skills aligned with the NIST Incident Response Lifecycle.

## Journal Structure
Each entry contains:
- **Date & Entry Number** — chronological record of activity
- **Description** — summary of the incident or task (20–50 words)
- **The 5 W's** — Who, What, Where, When, Why for incident entries
- **Tools Used** — specific cybersecurity tools applied during the entry
- **Reflections/Notes** — key takeaways and learning observations

---

## NIST Incident Response Lifecycle

All journal entries are mapped to the relevant phase(s):

| Phase | Description |
|-------|-------------|
| **Preparation** | Establishing tools, playbooks, and team readiness |
| **Detection & Analysis** | Identifying and investigating potential incidents |
| **Containment, Eradication & Recovery** | Stopping the threat and restoring systems |
| **Post-Incident Activity** | Reviewing the incident and improving processes |

---

## Journal Entries Summary

---

### Entry 1 — Documenting a Ransomware Incident
**Phase:** Detection and Analysis; Containment, Eradication and Recovery

**Description:**
Investigated a ransomware attack on a small healthcare clinic. Analysed 
the attack vector, affected systems, and business impact, documenting 
findings using the 5 W's framework to structure the incident report.

**The 5 W's:**
- **Who:** An organised cybercriminal group targeting healthcare 
  organisations
- **What:** Ransomware deployed via a malicious email attachment, 
  encrypting critical patient files and demanding payment
- **Where:** The clinic's internal network; multiple employee workstations 
  affected
- **When:** A Tuesday morning at approximately 09:00 during business hours
- **Why:** The attack exploited employees' lack of phishing awareness and 
  the absence of email filtering controls

**Tools Used:** N/A — focused on incident documentation and analysis

---

### Entry 2 — Packet Analysis with Wireshark / tcpdump
**Phase:** Detection and Analysis

**Description:**
Captured and analysed network packets using tcpdump and Wireshark to 
identify suspicious traffic patterns, examine protocol behaviour, and 
practise isolating potentially malicious communications from normal traffic.

**Tools Used:**
- **tcpdump** — command-line packet capture tool used to capture live 
  network traffic and save it to a `.pcap` file for analysis
- **Wireshark** — GUI-based packet analyser used to inspect captured 
  traffic, filter by protocol, and identify anomalies including unusual 
  DNS queries and unexpected outbound connections
- Examined TCP handshake sequences, HTTP requests, and DNS resolution 
  patterns to distinguish normal from suspicious behaviour

---

### Entry 3 — Investigating a Suspicious File Hash
**Phase:** Detection and Analysis

**Description:**
Used VirusTotal to investigate a suspicious file hash flagged during an 
incident triage. Correlated the hash against known threat intelligence 
databases to determine whether the file was associated with known malware.

**The 5 W's:**
- **Who:** An unknown external threat actor who delivered a malicious file
- **What:** A file hash flagged as potentially malicious during endpoint 
  triage following an alert from the SIEM
- **Where:** An employee's workstation within the organisation's network
- **When:** Detected during a routine alert review within the SOC
- **Why:** The file had been delivered via a phishing email and executed 
  by the user, triggering an endpoint detection alert

**Tools Used:**
- **VirusTotal** — submitted the file hash to cross-reference against 
  70+ antivirus engines and threat intelligence feeds; the hash returned 
  multiple vendor detections confirming the file as a known Trojan variant

---

### Entry 4 — SIEM Queries with Splunk and Chronicle
**Phase:** Detection and Analysis; Post-Incident Activity

**Description:**
Performed structured queries in both Splunk and Chronicle SIEM platforms 
to search log data, identify suspicious login patterns, and investigate 
a potential brute-force attack against employee accounts.

**Tools Used:**
- **Splunk** — used SPL (Search Processing Language) to query log 
  events, filter by source IP, username, and time range, and identify 
  repeated failed login attempts indicative of a brute-force attack
- **Chronicle (Google SecOps)** — used UDM (Unified Data Model) search 
  to correlate events across data sources, investigate asset histories, 
  and timeline suspicious activity across the organisation's network
- Both platforms were used to validate findings against each other, 
  reinforcing the value of multi-tool investigation workflows in a SOC 
  environment

---

### Entry 5 — Playbook Response to a Phishing Alert
**Phase:** Preparation; Detection and Analysis; Containment, 
Eradication and Recovery

**Description:**
Applied a structured incident response playbook to triage and respond 
to a phishing alert, following decision-tree steps to assess severity, 
escalate appropriately, and contain the threat.

**The 5 W's:**
- **Who:** An external attacker impersonating a trusted vendor
- **What:** A phishing email containing a malicious link designed to 
  harvest employee credentials
- **Where:** Delivered to multiple employee inboxes within the 
  organisation
- **When:** Detected at 14:32 via an automated SIEM alert on a Wednesday
- **Why:** The attacker exploited the absence of email authentication 
  controls (SPF/DKIM/DMARC) to spoof a legitimate sender address

**Tools Used:**
- **Incident Response Playbook** — followed documented escalation and 
  containment procedures; blocked the malicious URL at the proxy, 
  reset compromised credentials, and notified affected users

---

## Reflections & Notes

**Were there any specific activities that were challenging?**
The most challenging activity was performing SIEM queries in Splunk 
using SPL syntax, as the query language required careful attention to 
field names and operators. However, working through real log datasets 
made the learning process highly practical and directly applicable to 
SOC analyst work.

**Has your understanding of incident detection and response changed?**
Yes, significantly. Before this course, I understood incident response 
conceptually, but working through the NIST Incident Response Lifecycle 
phases hands-on demonstrated how structured documentation and clear 
communication are just as critical as technical skills during an active 
incident. I now appreciate the operational value of playbooks and 
escalation procedures.

**Was there a specific tool or concept you enjoyed the most?**
Chronicle (Google SecOps) stood out as the most impressive tool due to 
its ability to correlate events across multiple data sources using 
UDM search. Its timeline view made it significantly easier to 
reconstruct the sequence of events during an investigation, which I 
found both intuitive and powerful for threat hunting.

---

## Skills Demonstrated
`Incident Documentation` `NIST Incident Response Lifecycle`  
`The 5 W's Framework` `Splunk (SPL)` `Chronicle / Google SecOps`  
`Wireshark` `tcpdump` `VirusTotal` `Threat Intelligence`  
`Phishing Analysis` `Brute-Force Detection` `Playbook Execution`  
`SIEM Querying` `Log Analysis` `SOC Operations` `Packet Analysis`

## Files
- [`incident-handlers-journal.pdf`](./incident-handler-s-journal.pdf) — 
  Completed incident handler's journal with all entries
