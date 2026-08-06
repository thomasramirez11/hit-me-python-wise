"""
Lesson 03 — For Loops for Security Log Analysis

This lesson demonstrates how a for loop can examine
multiple cybersecurity records automatically.
"""


# A list containing several login-event dictionaries.
login_events = [
    {
        "username": "Thomas",
        "failed_attempts": 1,
        "trusted_device": True
    },
    {
        "username": "Admin",
        "failed_attempts": 6,
        "trusted_device": True
    },
    {
        "username": "UnknownUser",
        "failed_attempts": 3,
        "trusted_device": False
    }
]


print("=== LOGIN EVENT ANALYSIS ===")


# Examine each login event one at a time.
for event in login_events:
    username = event["username"]
    failed_attempts = event["failed_attempts"]
    trusted_device = event["trusted_device"]

    suspicious = (
        failed_attempts >= 5
        or not trusted_device
    )

    print()
    print(f"User: {username}")
    print(f"Failed attempts: {failed_attempts}")
    print(f"Trusted device: {trusted_device}")

    if suspicious:
        print("Result: Suspicious login detected.")
    else:
        print("Result: Login appears normal.")
