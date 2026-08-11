"""
Lesson 05 — Functions for Security Checks

This lesson demonstrates how functions allow Python
to reuse the same cybersecurity logic multiple times.
"""


# Create a reusable security function.
def analyze_login(username, failed_attempts, trusted_device):

    suspicious = (
        failed_attempts >= 5
        or not trusted_device
    )

    print(f"\nChecking user: {username}")
    print(f"Failed attempts: {failed_attempts}")
    print(f"Trusted device: {trusted_device}")

    if suspicious:
        print("Result: Suspicious login detected.")
    else:
        print("Result: Login appears normal.")


print("=== SECURITY LOGIN ANALYZER ===")


# Run the same function with different login information.
analyze_login("Thomas", 1, True)

analyze_login("Admin", 6, True)

analyze_login("UnknownUser", 2, False)
