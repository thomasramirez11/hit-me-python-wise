"""
Lesson 09 — List Comprehensions for Security Filtering

This lesson demonstrates how list comprehensions can
filter cybersecurity data using compact Python syntax.
"""


# Login records collected by a security system.
login_events = [
    {
        "username": "Thomas",
        "failed_attempts": 1
    },
    {
        "username": "Admin",
        "failed_attempts": 6
    },
    {
        "username": "UnknownUser",
        "failed_attempts": 9
    },
    {
        "username": "Maria",
        "failed_attempts": 2
    }
]


print("=== ALL LOGIN EVENTS ===")

for event in login_events:
    print(
        f"{event['username']} "
        f"| Failed attempts: {event['failed_attempts']}"
    )


# Create a new list containing only suspicious events.
suspicious_events = [
    event
    for event in login_events
    if event["failed_attempts"] >= 5
]


print()
print("=== SUSPICIOUS LOGIN EVENTS ===")

for event in suspicious_events:
    print(
        f"ALERT: {event['username']} "
        f"has {event['failed_attempts']} failed attempts."
    )


# Create a list containing only the suspicious usernames.
suspicious_users = [
    event["username"]
    for event in suspicious_events
]


print()
print(f"Suspicious users: {suspicious_users}")
