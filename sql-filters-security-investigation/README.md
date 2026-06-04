# SQL Filters for Security Investigation

## Overview
Applied SQL filtering techniques to investigate potential security incidents 
involving suspicious login attempts and employee machine vulnerabilities. 
This activity was completed as part of the Google Cybersecurity Professional 
Certificate — Course 4: Tools of the Trade: Linux and SQL.

## Scenario Summary
As a security professional at a large organisation, I was tasked with 
querying two database tables — `log_in_attempts` and `employees` — to 
investigate after-hours login anomalies, suspicious activity on specific 
dates, unauthorised access attempts from outside a known region, and to 
identify employee machines requiring targeted security updates.

## Database Tables Used

### `log_in_attempts`
| Column | Description |
|--------|-------------|
| `event_id` | Unique ID for each login event |
| `username` | Username of the login attempt |
| `login_date` | Date of the attempt (YYYY-MM-DD) |
| `login_time` | Time of the attempt (HH:MM:SS) |
| `country` | Country where the attempt originated |
| `ip_address` | IP address used |
| `success` | 1 = success, 0 = failed |

### `employees`
| Column | Description |
|--------|-------------|
| `employee_id` | Unique employee ID |
| `device_id` | Assigned machine ID |
| `username` | Employee username |
| `department` | Department name |
| `office` | Office location code |

---

## Queries Performed

### 1. Retrieve After-Hours Failed Login Attempts
**Objective:** Identify all failed login attempts that occurred after 18:00.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00' AND success = 0;
```

**Explanation:** The `WHERE` clause uses `AND` to combine two conditions — 
filtering for login times after 18:00 and only returning records where 
`success = 0` (failed attempts). This isolates suspicious after-hours 
activity for investigation.

---

### 2. Retrieve Login Attempts on Specific Dates
**Objective:** Investigate all login attempts on 2022-05-09 and the day 
before (2022-05-08) following a suspicious event.

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

**Explanation:** The `OR` operator returns records matching either date, 
ensuring all activity across the two-day window is captured for review.

---

### 3. Retrieve Login Attempts Outside of Mexico
**Objective:** Identify login attempts that did not originate in Mexico, 
accounting for both `MEX` and `MEXICO` as country values.

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

**Explanation:** `LIKE 'MEX%'` matches any country value beginning with 
"MEX" (covering both `MEX` and `MEXICO`). The `NOT` operator excludes 
these, returning all attempts from every other country.

---

### 4. Retrieve Employees in the Marketing Department (East Building)
**Objective:** Identify Marketing department employees located in any 
East building office for a targeted security update.

```sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
```

**Explanation:** `AND` combines an exact match on `department` with a 
pattern match on `office` using `LIKE 'East%'`, which captures all 
East building office codes (e.g., East-170, East-320).

---

### 5. Retrieve Employees in Finance or Sales
**Objective:** Identify all employees in either the Sales or Finance 
departments for a separate security update rollout.

```sql
SELECT *
FROM employees
WHERE department = 'Sales' OR department = 'Finance';
```

**Explanation:** The `OR` operator returns employees belonging to either 
department, producing a combined list for the update team to action.

---

### 6. Retrieve All Employees Not in IT
**Objective:** Identify all employees outside the Information Technology 
department, who still require a pending machine update.

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

**Explanation:** The `NOT` operator excludes IT department employees, 
returning all remaining staff whose machines need to be updated.

---

## Project Description
This project involved using SQL to support a security investigation at a 
large organisation by querying login attempt logs and employee records. 
Using filtering operators including `AND`, `OR`, `NOT`, and `LIKE`, I 
isolated suspicious login activity by time, date, and geography, and 
identified specific employee machines requiring security updates across 
targeted departments.

## Summary
Across six structured queries, I applied SQL filters to investigate 
after-hours failed logins, date-specific suspicious events, and 
geographically anomalous access attempts. I also retrieved targeted 
employee subsets by department and office location to support security 
update deployment. Each query demonstrated practical application of 
`AND`, `OR`, `NOT`, and `LIKE` operators in a real-world security 
context.

---

## Skills Demonstrated
`SQL` `Database Querying` `Security Investigation` `Log Analysis`  
`AND / OR / NOT Operators` `LIKE & Pattern Matching` `Date & Time Filtering`  
`Access Control Auditing` `Employee Data Management` `Threat Detection`

## Files
- [`sql-filters-security-investigation.pdf`](./sql-filters-security-investigation.pdf) — 
  Completed portfolio document with queries and outputs
