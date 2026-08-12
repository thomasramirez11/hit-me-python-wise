"""
Lesson 08 — JSON for Security Data

This lesson demonstrates how Python can convert
cybersecurity information between dictionaries
and JSON data.
"""

import json


# Create a Python dictionary representing a security alert.
security_alert = {
    "username": "Admin",
    "source_ip": "192.168.1.50",
    "failed_attempts": 7,
    "trusted_device": False,
    "severity": "High"
}


print("=== PYTHON DICTIONARY ===")
print(security_alert)

print()


# Convert the Python dictionary into JSON text.
json_alert = json.dumps(
    security_alert,
    indent=4
)

print("=== JSON DATA ===")
print(json_alert)

print()


# Convert the JSON text back into a Python dictionary.
restored_alert = json.loads(json_alert)


print("=== RESTORED SECURITY DATA ===")
print(f"Username: {restored_alert['username']}")
print(f"Source IP: {restored_alert['source_ip']}")
print(f"Severity: {restored_alert['severity']}")
print(f"Trusted device: {restored_alert['trusted_device']}")
