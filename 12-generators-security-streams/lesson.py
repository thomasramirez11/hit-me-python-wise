"""
Lesson 12 — Generators for Security Data Streams

This lesson demonstrates how a generator can examine
security events and produce suspicious events one at a time.
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
        "username": "Maria",
        "failed_attempts": 2
    },
    {
        "username": "UnknownUser",
        "failed_attempts": 10
    }
]


def find_suspicious_events(events):

    for event in events:

        if event["failed_attempts"] >= 5:
            yield event


print("=== SUSPICIOUS EVENT STREAM ===")
print()


suspicious_events = find_suspicious_events(
    security_events
)


for event in suspicious_events:

    print(
        f"ALERT: {event['username']} "
        f"has {event['failed_attempts']} failed attempts."
    )
