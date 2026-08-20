"""
Lesson 17 — User Input for Security Analysis

This lesson demonstrates how Python can receive
information directly from the user and use it
inside a cybersecurity decision.
"""


print("=== LOGIN SECURITY CHECK ===")
print()


# Ask the analyst for information.
username = input("Enter username: ")

failed_attempts = int(
    input("Enter number of failed attempts: ")
)

trusted_answer = input(
    "Is the device trusted? (yes/no): "
).lower()


# Convert the yes/no answer into a Boolean.
trusted_device = trusted_answer == "yes"


# Analyze the login.
suspicious = (
    failed_attempts >= 5
    or not trusted_device
)


print()
print("=== ANALYSIS RESULT ===")

print(f"Username: {username}")
print(f"Failed attempts: {failed_attempts}")
print(f"Trusted device: {trusted_device}")


if suspicious:
    print("Result: Suspicious login detected.")
else:
    print("Result: Login appears normal.")
