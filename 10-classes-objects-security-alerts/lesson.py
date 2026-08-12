"""
Lesson 10 — Classes & Objects for Security Alerts

This lesson demonstrates how Python classes can
represent cybersecurity alerts as reusable objects.
"""


class SecurityAlert:

    def __init__(self, username, source_ip, failed_attempts):
        self.username = username
        self.source_ip = source_ip
        self.failed_attempts = failed_attempts

        self.suspicious = failed_attempts >= 5


    def display_alert(self):
        print(f"User: {self.username}")
        print(f"Source IP: {self.source_ip}")
        print(f"Failed attempts: {self.failed_attempts}")

        if self.suspicious:
            print("Status: Suspicious activity detected.")
        else:
            print("Status: Activity appears normal.")

        print()


print("=== SECURITY ALERT SYSTEM ===")
print()


# Create individual SecurityAlert objects.
alert_one = SecurityAlert(
    "Thomas",
    "192.168.1.10",
    1
)

alert_two = SecurityAlert(
    "Admin",
    "10.0.0.25",
    7
)

alert_three = SecurityAlert(
    "UnknownUser",
    "172.16.0.50",
    9
)


# Store the objects together.
alerts = [
    alert_one,
    alert_two,
    alert_three
]


# Ask each object to display itself.
for alert in alerts:
    alert.display_alert()
