# Lesson 01: Boolean security logic
# This program simulates a simple access-control decision.

# Authentication conditions
password_correct = True
mfa_correct = True

# Danger indicators
failed_login_detected = True
suspicious_ip_detected = False

# One danger signal is enough to activate the alert
danger_detected = (
    failed_login_detected
    or suspicious_ip_detected
)

# Access requires every safe condition to be satisfied
access_granted = (
    password_correct
    and mfa_correct
    and not danger_detected
)

# Display the final security decision
print("Danger detected:", danger_detected)
print("Access granted:", access_granted)
