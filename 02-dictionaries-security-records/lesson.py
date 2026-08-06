"""
Lesson 02 — Dictionaries for Security Records

This lesson demonstrates how dictionaries can store,
read, update, and analyze cybersecurity information.
"""


# Create a dictionary representing one login event.
login_event = {
    "username": "Admin",
    "ip_address": "192.168.1.50",
    "failed_attempts": 7,
    "trusted_device": False
}


# Read values using their keys.
print("=== LOGIN EVENT ===")
print(f"Username: {login_event['username']}")
print(f"IP address: {login_event['ip_address']}")
print(f"Failed attempts: {login_event['failed_attempts']}")
print(f"Trusted device: {login_event['trusted_device']}")

print()


# Update an existing value.
login_event["failed_attempts"] = 8


# Add a new key and value.
login_event["status"] = "Under investigation"


# Make a security decision using dictionary values.
if (
    login_event["failed_attempts"] >= 5
    or not login_event["trusted_device"]
):
    login_event["alert"] = True
else:
    login_event["alert"] = False


# Display the updated security record.
print("=== UPDATED SECURITY RECORD ===")

for key, value in login_event.items():
    print(f"{key}: {value}")
