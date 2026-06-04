# Linux File Permissions Management

## Overview
Demonstrated the use of Linux command-line tools to audit and manage file 
system permissions within a research team environment. This activity was 
completed as part of the Google Cybersecurity Professional Certificate — 
Course 4: Tools of the Trade: Linux and SQL.

## Scenario Summary
As a security professional supporting a research team at a large organisation, 
I was tasked with reviewing existing file and directory permissions, identifying 
any misconfigurations or unauthorised access, and applying the principle of 
least privilege by modifying permissions to match the organisation's 
authorisation policy.

## Skills & Tools Used
- Linux CLI (Bash)
- `ls -la` — auditing file and directory permissions including hidden files
- `chmod` — modifying read, write, and execute permissions
- Understanding and interpreting the 10-character permission string
- Managing hidden files and directory-level access control

---

## Tasks Performed

### 1. Check File and Directory Details
Used `ls -la` to list all files and directories in the `projects/` directory, 
including hidden files, and display their full permission strings.

```bash
ls -la /home/researcher2/projects
```

**Sample output:**

drwx--x--- 2 researcher2 research_team 4096 Feb 12 13:42 drafts
-rw-rw-rw- 1 researcher2 research_team  46  Feb 12 13:42 project_k.txt
-rw-r----- 1 researcher2 research_team  46  Feb 12 13:42 project_m.txt
-rw-rw-r-- 1 researcher2 research_team  46  Feb 12 13:42 project_r.txt
-rw-rw-r-- 1 researcher2 research_team  46  Feb 12 13:42 project_t.txt
-rw--w---- 1 researcher2 research_team  46  Feb 12 13:42 .project_x.txt


---

### 2. Interpret the Permission String
**Example:** `-rw-rw-rw-` for `project_k.txt`

| Character(s) | Position | Meaning |
|---|---|---|
| `-` | 1 | Regular file (not a directory) |
| `rw-` | 2–4 | User (owner): read & write, no execute |
| `rw-` | 5–7 | Group: read & write, no execute |
| `rw-` | 8–10 | Others: read & write, no execute |

**Issue identified:** Others have write access — this violates the 
organisation's policy.

---

### 3. Change File Permissions — Remove Other Write Access
The organisation does not permit `other` users to have write access to 
any files. Removed write permission from `other` on `project_k.txt`:

```bash
chmod o-w project_k.txt
```

**Verified result:**
```bash
ls -la project_k.txt
-rw-rw-r-- 1 researcher2 research_team 46 Feb 12 13:42 project_k.txt
```

---

### 4. Change Permissions on a Hidden File
The archived hidden file `.project_x.txt` should be readable by the 
user and group but not writable by anyone:

```bash
chmod u-w,g-w,g+r .project_x.txt
```

**Verified result:**
```bash
ls -la .project_x.txt
-r--r----- 1 researcher2 research_team 46 Feb 12 13:42 .project_x.txt
```

---

### 5. Change Directory Permissions
Only `researcher2` should be able to access the `drafts/` directory and 
its contents. Removed execute permission from the group:

```bash
chmod g-x drafts
```

**Verified result:**
```bash
ls -la
drwx------ 2 researcher2 research_team 4096 Feb 12 13:42 drafts
```

---

## Project Description
This project involved auditing and correcting file system permissions for a 
research team's project directory in Linux. Using `ls -la` and `chmod`, I 
identified files where permissions exceeded the organisation's policy, 
including world-writable files and improperly configured hidden files, and 
applied the principle of least privilege to restrict access appropriately.

## Summary
By examining the 10-character permission strings for all files and 
directories — including hidden files — I identified three permission 
violations: a file with write access granted to `other`, a hidden 
archive file with improper write permissions, and a directory accessible 
to the group beyond what was authorised. I used `chmod` to remediate each 
issue, ensuring the file system matched the organisation's access control 
requirements.

---

## Skills Demonstrated
`Linux CLI` `Bash` `File Permission Management` `chmod` `ls -la`  
`Principle of Least Privilege` `Access Control` `Hidden File Management`  
`Directory Permissions` `Security Hardening` `Authorization Auditing`

## Files
- [`file-permissions-linux.pdf`](./file-permissions-linux.pdf) — 
  Completed portfolio document with commands and screenshots
