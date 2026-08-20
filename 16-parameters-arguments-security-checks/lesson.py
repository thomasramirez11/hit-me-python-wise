"""
Lesson 16 — Parameters & Arguments for Security Checks

This lesson demonstrates the difference between
function parameters and function arguments.
"""


def analyze_login(username, failed_attempts, trusted_device):

    suspicious = (
        failed_attempts >= 5
        or not trusted_device
    )

    print(f"User: {username}")
    print(f"Failed attempts: {failed_attempts}")
    print(f"Trusted device: {trusted_device}")

    if suspicious:
        print("Result: Suspicious login detected.")
    else:
        print("Result: Login appears normal.")

    print()


print("=== LOGIN SECURITY ANALYSIS ===")
print()


# Positional arguments
analyze_login(
    "Thomas",
    1,
    True
)


# Keyword arguments
analyze_login(
    username="Admin",
    failed_attempts=7,
    trusted_device=False
)
