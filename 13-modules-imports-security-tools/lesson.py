"""
Lesson 13 — Modules & Imports

This lesson demonstrates how Python can import
reusable cybersecurity functions from another file.
"""


import security_tools


username = "Admin"
failed_attempts = 7
trusted_device = False


risk_level = security_tools.calculate_risk(
    failed_attempts,
    trusted_device
)


print("=== LOGIN RISK ANALYSIS ===")

print(f"Username: {username}")
print(f"Failed attempts: {failed_attempts}")
print(f"Trusted device: {trusted_device}")
print(f"Risk level: {risk_level}")
