"""
Lesson 11 — Decorators for Security Logging

This lesson demonstrates how a decorator can add
security logging around existing Python functions.
"""

from functools import wraps


# Create the decorator.
def security_log(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(
            f"[SECURITY LOG] Starting: {function.__name__}"
        )

        result = function(*args, **kwargs)

        print(
            f"[SECURITY LOG] Finished: {function.__name__}"
        )

        return result

    return wrapper


# Apply the decorator to a function.
@security_log
def check_login(username, failed_attempts):

    print(f"Checking login for: {username}")

    if failed_attempts >= 5:
        return "Suspicious login detected."

    return "Login appears normal."


print("=== SECURITY FUNCTION MONITOR ===")
print()

result = check_login("Admin", 7)

print()
print(f"Final result: {result}")
