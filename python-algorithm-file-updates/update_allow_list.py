# =============================================================
# update_allow_list.py
# Author  : Ahmed Sayuti Kamel
# Purpose : Automate the removal of revoked IP addresses from
#           an access control allow list for a restricted
#           healthcare subnetwork.
# Course  : Google Cybersecurity Professional Certificate
#           Course 7 - Automate Cybersecurity Tasks with Python
# =============================================================


# ── CONFIGURATION ─────────────────────────────────────────────

# Name of the file containing permitted IP addresses
import_file = "allow_list.txt"

# IP addresses to be removed from the allow list
remove_list = [
    "192.168.97.105",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]


# ── STEP 1: Open and read the allow list file ──────────────────
# The 'with' statement ensures the file is automatically closed
# after the block executes, preventing resource leaks.
# Mode "r" opens the file in read-only mode.

with open(import_file, "r") as file:

    # ── STEP 2: Read file contents into a string ───────────────
    # .read() returns the entire file as a single string,
    # with each IP address separated by whitespace/newlines.
    ip_addresses = file.read()


# ── STEP 3: Convert the string into a list ────────────────────
# .split() breaks the string into a list using whitespace as the
# delimiter, so each IP address becomes an individual list element.
# Example: "192.168.1.1\n192.168.1.2" → ["192.168.1.1", "192.168.1.2"]

ip_addresses = ip_addresses.split()


# ── STEP 4 & 5: Iterate through remove list and remove matches ─
# The for loop processes each IP address in remove_list one by one.
# The conditional check (if element in ip_addresses) prevents a
# ValueError in case the IP is not found in the allow list.
# .remove() is safe here because the allow list contains no
# duplicates — each IP address appears at most once.

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
        print(f"  [REMOVED] {element}")
    else:
        print(f"  [NOT FOUND] {element} was not in the allow list")


# ── STEP 6: Convert list back to string and update the file ───
# "\n".join() reassembles the list into a single string with each
# IP address on its own line, matching the original file format.
# Mode "w" overwrites the file entirely with the updated content.

ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)

print("\n[DONE] allow_list.txt has been updated successfully.")


# ── OPTIONAL VERIFICATION: Print updated allow list ───────────
# Re-open the file to confirm the changes were written correctly.

print("\n── Updated Allow List ────────────────────────────────")
with open(import_file, "r") as file:
    print(file.read())
print("─────────────────────────────────────────────────────")
