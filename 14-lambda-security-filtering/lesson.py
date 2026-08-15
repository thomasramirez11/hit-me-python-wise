"""
Lesson 14 — Lambda Functions for Security Filtering

This lesson demonstrates how lambda functions can
perform small security-related calculations and help
sort cybersecurity data.
"""


security_events = [
    {
        "username": "Thomas",
        "failed_attempts": 1
    },
    {
        "username": "Admin",
        "failed_attempts": 7
    },
    {
        "username": "UnknownUser",
        "failed_attempts": 10
    },
    {
        "username": "Maria",
        "failed_attempts": 3
    }
]


# Small function created with lambda.
is_suspicious = lambda attempts: attempts >= 5


print("=== SECURITY EVENT CHECK ===")
print()


for event in security_events:

    suspicious = is_suspicious(
        event["failed_attempts"]
    )

    print(
        f"{event['username']} "
        f"| Failed attempts: {event['failed_attempts']} "
        f"| Suspicious: {suspicious}"
    )


print()


# Sort events from highest to lowest failed attempts.
sorted_events = sorted(
    security_events,
    key=lambda event: event["failed_attempts"],
    reverse=True
)


print("=== EVENTS SORTED BY RISK ===")
print()


for event in sorted_events:
    print(
        f"{event['username']} "
        f"| Failed attempts: {event['failed_attempts']}"
    )
