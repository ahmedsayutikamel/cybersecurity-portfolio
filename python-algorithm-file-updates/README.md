# Python Algorithm — Automated Allow List File Updates

## Overview
Developed a Python algorithm to automate the management of an IP address 
allow list for a healthcare company's restricted network. The algorithm 
reads a file of permitted IP addresses, cross-references it against a 
remove list, and rewrites the file with unauthorised addresses removed. 
This activity was completed as part of the Google Cybersecurity 
Professional Certificate — Course 7: Automate Cybersecurity Tasks 
with Python.

## Scenario Summary
As a security professional at a healthcare company, I was responsible 
for maintaining an allow list of IP addresses permitted to access 
restricted content containing personal patient records. When employees 
no longer required access, their IP addresses needed to be removed 
promptly. I developed a Python algorithm to automate this process, 
reducing manual effort and the risk of human error in access control 
management.

## Files
| File | Description |
|------|-------------|
| `allow_list.txt` | Text file containing permitted IP addresses (one per line) |
| `update_allow_list.py` | Python script implementing the allow list update algorithm |
| `algorithm-file-updates-python.pdf` | Completed portfolio document |

---

## The Algorithm

### Full Script

```python
# Assign the allow list file name to a variable
import_file = "allow_list.txt"

# Define the list of IP addresses to remove
remove_list = ["192.168.97.105", "192.168.158.170", 
               "192.168.201.40", "192.168.58.57"]

# Step 1: Open the file containing the allow list
with open(import_file, "r") as file:

    # Step 2: Read the file contents into a string
    ip_addresses = file.read()

# Step 3: Convert the string into a list
ip_addresses = ip_addresses.split()

# Step 4 & 5: Iterate through the remove list and remove matches
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Step 6: Convert the list back to a string and update the file
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

---

## Step-by-Step Explanation

### Step 1 — Open the File Containing the Allow List
```python
with open(import_file, "r") as file:
```

**Syntax & keywords explained:**
- `open()` — built-in Python function that opens a file; takes the 
  file name and mode as arguments
- `"r"` — read mode; opens the file for reading only
- `with` — context manager keyword that automatically closes the file 
  once the indented block completes, preventing resource leaks
- `as file` — assigns the opened file object to the variable `file` 
  for use within the `with` block

---

### Step 2 — Read the File Contents
```python
ip_addresses = file.read()
```

**Syntax & keywords explained:**
- `.read()` — method called on the file object that reads the entire 
  contents of the file and returns them as a single string
- The result is stored in `ip_addresses`, which at this point contains 
  all IP addresses as one continuous string with whitespace separating 
  each address

---

### Step 3 — Convert the String into a List
```python
ip_addresses = ip_addresses.split()
```

**Syntax & keywords explained:**
- `.split()` — string method that splits the string into a list of 
  substrings based on whitespace (spaces, newlines) by default
- After this step, `ip_addresses` is a Python list where each element 
  is a single IP address string, enabling individual item manipulation
- Example: `"192.168.1.1\n192.168.1.2"` → 
  `["192.168.1.1", "192.168.1.2"]`

---

### Step 4 — Iterate Through the Remove List
```python
for element in remove_list:
```

**Syntax & keywords explained:**
- `for` — keyword that initiates an iterative loop
- `element` — the loop variable that holds the current item from 
  `remove_list` on each iteration
- `in` — keyword that specifies the iterable being looped through
- The loop runs once for each IP address in `remove_list`, allowing 
  each one to be checked and removed individually

---

### Step 5 — Remove Matching IP Addresses
```python
    if element in ip_addresses:
        ip_addresses.remove(element)
```

**Syntax & keywords explained:**
- `if element in ip_addresses` — conditional check that evaluates 
  whether the current `remove_list` IP address exists in 
  `ip_addresses` before attempting removal
- This check prevents a `ValueError` that would occur if `.remove()` 
  was called on a value not present in the list
- `.remove()` — list method that removes the first occurrence of the 
  specified value from the list
- This approach is safe because the `ip_addresses` list contains no 
  duplicate entries; each IP address appears at most once, so 
  `.remove()` will always target the correct single entry

---

### Step 6 — Update the File with the Revised Allow List
```python
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

**Syntax & keywords explained:**
- `"\n".join(ip_addresses)` — joins all list elements back into a 
  single string, inserting a newline character `\n` between each IP 
  address so each one appears on its own line in the file
- `open(import_file, "w")` — reopens the file in write mode `"w"`, 
  which overwrites the existing file contents entirely with the 
  updated data
- `.write()` — method that writes the provided string to the open 
  file, replacing the previous allow list with the revised version

---

## Project Description
This project involved designing a Python algorithm to automate IP 
address access control management for a healthcare organisation's 
restricted subnetwork. Using file handling functions, string and list 
methods, and iterative logic, I built a script that opens an allow 
list file, identifies and removes IP addresses flagged for revocation, 
and rewrites the updated list back to the file — ensuring only 
authorised personnel retain access to sensitive patient data.

## Summary
The algorithm follows a clear six-step process: opening the allow list 
file with a `with` statement and `open()`, reading its contents into a 
string using `.read()`, converting that string to a list with 
`.split()` for individual item manipulation, iterating through the 
remove list using a `for` loop, conditionally removing flagged 
addresses with `.remove()`, and finally rejoining the list into a 
string with `.join()` before writing it back to the file using 
`.write()`. This solution automates a critical access control task, 
reduces manual error, and demonstrates practical Python scripting 
applied directly to a cybersecurity use case.

---

## Skills Demonstrated
`Python` `File Handling` `Security Automation` `Access Control`  
`with Statement` `open()` `.read()` `.write()` `.split()` `.join()`  
`.remove()` `for Loops` `Conditional Logic` `List Manipulation`  
`Algorithm Development` `Least Privilege Enforcement`  
`Healthcare Data Security`

## Files
- [`update_allow_list.py`](./update_allow_list.py) — 
  Python script implementing the algorithm
- [`algorithm-file-updates-python.pdf`](./algorithm-file-updates-python.pdf) — 
  Completed portfolio document with code and explanations
