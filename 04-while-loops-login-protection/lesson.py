"""
Lesson 04 — While Loops for Login Protection

This lesson demonstrates how a while loop can track
failed login attempts and lock an account after the
maximum number of attempts is reached.
"""


# Starting security information
failed_attempts = 0
maximum_attempts = 5
account_locked = False


print("=== LOGIN ATTEMPT MONITOR ===")


# Repeat while the number of failed attempts
# remains below the allowed maximum.
while failed_attempts < maximum_attempts:
    failed_attempts += 1

    print(f"Failed login attempt: {failed_attempts}")

    if failed_attempts == 3:
        print("Warning: Suspicious login activity detected.")

    if failed_attempts == maximum_attempts:
        account_locked = True
        print("Security action: Account locked.")


print()

print("=== FINAL SECURITY STATUS ===")
print(f"Total failed attempts: {failed_attempts}")
print(f"Account locked: {account_locked}")
