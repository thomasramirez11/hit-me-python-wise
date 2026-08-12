# Lesson 09 — List Comprehensions for Security Filtering

## Lesson objective

Learn how Python list comprehensions create new lists using
existing data and optional conditions.

This lesson uses a list comprehension to identify login events
with five or more failed attempts.

---

## Python concepts

- Lists
- Dictionaries
- `for` loops
- List comprehensions
- Conditional filtering
- Comparison operators
- F-strings

---

## Cybersecurity scenario

A security system receives several login records.

Each record contains:

- A username
- The number of failed login attempts

Instead of manually examining every event, Python creates a new
list containing only suspicious login activity.

---

## What This Lesson Demonstrates

### Starting with several security records

```python
login_events = [
    {
        "username": "Thomas",
        "failed_attempts": 1
    },
    {
        "username": "Admin",
        "failed_attempts": 6
    }
]
```

The outer list stores multiple dictionaries.

Each dictionary represents one login event.

```text
List
│
├── Thomas login record
├── Admin login record
├── UnknownUser login record
└── Maria login record
```

---

### The normal `for` loop idea

We could filter suspicious events using a normal loop:

```python
suspicious_events = []

for event in login_events:
    if event["failed_attempts"] >= 5:
        suspicious_events.append(event)
```

This works correctly.

Python:

1. Creates an empty list
2. Checks every event
3. Tests the failed-attempt count
4. Adds suspicious events to the new list

---

### The list comprehension

Python allows us to express the same idea more compactly:

```python
suspicious_events = [
    event
    for event in login_events
    if event["failed_attempts"] >= 5
]
```

This can be read almost like English:

```text
Give me each event
from login_events
if failed_attempts is 5 or higher.
```

### Memory hook

```text
What do I want?
Where do I get it from?
What condition must it pass?
```

In our code:

```text
event
↓
for event in login_events
↓
if failed_attempts >= 5
```

---

### Filtering the events

Python checks Thomas:

```text
1 >= 5 → False
```

Thomas is not included.

Python checks Admin:

```text
6 >= 5 → True
```

Admin is included.

Python checks UnknownUser:

```text
9 >= 5 → True
```

UnknownUser is included.

Python checks Maria:

```text
2 >= 5 → False
```

Maria is not included.

The new list therefore contains only:

```text
Admin
UnknownUser
```

---

### Creating a different list from the results

The program also uses:

```python
suspicious_users = [
    event["username"]
    for event in suspicious_events
]
```

This time we do not store the entire dictionary.

We extract only:

```python
event["username"]
```

The resulting list becomes:

```python
["Admin", "UnknownUser"]
```

This demonstrates that list comprehensions can both:

```text
Filter information
and
Transform information
```

---

### Normal loop vs list comprehension

Normal version:

```python
suspicious_users = []

for event in suspicious_events:
    suspicious_users.append(event["username"])
```

List comprehension:

```python
suspicious_users = [
    event["username"]
    for event in suspicious_events
]
```

Both can produce the same result.

The list comprehension is simply more compact.

---

### When to use a list comprehension

List comprehensions are useful when the operation is simple and
easy to understand.

Example:

```python
high_risk_ips = [
    ip
    for ip in detected_ips
    if ip in blocked_ips
]
```

However, if the logic becomes very complicated, a normal `for`
loop may be easier to read.

Readable code is more important than making code as short as
possible.

---

## Expected output

```text
=== ALL LOGIN EVENTS ===
Thomas | Failed attempts: 1
Admin | Failed attempts: 6
UnknownUser | Failed attempts: 9
Maria | Failed attempts: 2

=== SUSPICIOUS LOGIN EVENTS ===
ALERT: Admin has 6 failed attempts.
ALERT: UnknownUser has 9 failed attempts.

Suspicious users: ['Admin', 'UnknownUser']
```

---

## How to run

Run:

```bash
python lesson.py
```

---

## Memory hooks

```text
List comprehension = Build a list in one expression
```

Basic structure:

```python
[
    item
    for item in collection
]
```

With a condition:

```python
[
    item
    for item in collection
    if condition
]
```

Think:

```text
SELECT
FROM
WHERE
```

Cybersecurity version:

```text
Select suspicious events
from all login events
where failed attempts >= 5
```

---

## Cybersecurity connection

Security programs often need to filter large amounts of data.

List comprehensions can help extract:

- Failed logins
- Suspicious IP addresses
- High-severity alerts
- Malicious hashes
- Disabled accounts
- Open ports
- Vulnerable systems

Instead of manually processing every result, Python can quickly
create a smaller list containing only the information that needs
attention.
