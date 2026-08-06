"""
Lesson 01 — Boolean Security Logic

This lesson demonstrates how Python Boolean values and
logical operators can be used to make basic cybersecurity
access-control and threat-detection decisions.
"""


# --------------------------------------------------
# LOGIN CONDITIONS
# --------------------------------------------------

password_correct = True
mfa_approved = False
account_active = True


# --------------------------------------------------
# SECURITY CONDITIONS
# --------------------------------------------------

failed_attempts = 6
unknown_device = True


# --------------------------------------------------
# ACCESS-CONTROL DECISION
# --------------------------------------------------

access_granted = all([
    password_correct,
    mfa_approved,
    account_active
])


# --------------------------------------------------
# THREAT-DETECTION DECISION
# --------------------------------------------------

danger_detected = any([
    failed_attempts >= 5,
    unknown_device,
    not account_active
])


# --------------------------------------------------
# DISPLAY THE SECURITY CHECK
# --------------------------------------------------

print("=== SECURITY LOGIN CHECK ===")

print(f"Password correct: {password_correct}")
print(f"MFA approved: {mfa_approved}")
print(f"Account active: {account_active}")
print(f"Failed attempts: {failed_attempts}")
print(f"Unknown device: {unknown_device}")

print()

print(f"Access granted: {access_granted}")
print(f"Danger detected: {danger_detected}")

print()


# --------------------------------------------------
# RESPOND TO THE FINAL RESULTS
# --------------------------------------------------

if access_granted:
    print("Decision: Allow the login.")
else:
    print("Decision: Deny the login.")

if danger_detected:
    print("Security action: Send an alert to the analyst.")
else:
    print("Security action: No alert is necessary.")
