# Lesson 03 — For Loops for Security Log Analysis

## Lesson objective

Learn how a Python `for` loop can process several cybersecurity
records automatically.

This lesson examines multiple login events and decides whether
each login appears normal or suspicious.

---

## Python concepts

- Lists
- Dictionaries
- `for` loops
- Loop variables
- Accessing dictionary values
- Boolean conditions
- `if` and `else`
- F-strings

---

## Cybersecurity scenario

A security system has collected several login records.

Each record contains:

- A username
- The number of failed login attempts
- Whether the device is trusted

The program uses a `for` loop to examine every login event.

A login is considered suspicious when:

- There are five or more failed attempts
- The device is not trusted

---

## What This Lesson Demonstrates

### A list of security records

```python
login_events = [
    {
        "username": "Thomas",
        "failed_attempts": 1,
        "trusted_device": True
    },
    {
        "username": "Admin",
        "failed_attempts": 6,
        "trusted_device": True
    }
]
```

The outer square brackets create a list.

```text
[ ]
```

Each item inside the list is a dictionary containing information
about one login event.

The structure can be imagined as:

```text
login_events
│
├── Login record 1
├── Login record 2
└── Login record 3
```

This allows one variable to store several related records.

---

### Starting the `for` loop

```python
for event in login_events:
```

The loop takes one item from `login_events` during each repetition.

The temporary variable:

```python
event
```

represents the current dictionary being examined.

During the first repetition, `event` contains Thomas's record.

During the second repetition, it contains Admin's record.

During the third repetition, it contains UnknownUser's record.

### Memory hook

> A `for` loop is a security analyst checking one report at a time.

---

### Reading the current event

```python
username = event["username"]
failed_attempts = event["failed_attempts"]
trusted_device = event["trusted_device"]
```

These lines extract values from the current dictionary.

For the Admin record, Python creates:

```python
username = "Admin"
failed_attempts = 6
trusted_device = True
```

When the loop repeats, these variables receive values from the
next login event.

---

### Creating the security decision

```python
suspicious = (
    failed_attempts >= 5
    or not trusted_device
)
```

Python checks two conditions.

The first asks:

```text
Are there five or more failed attempts?
```

The second asks:

```text
Is the device not trusted?
```

Because the conditions use `or`, only one must be true for the
login to be classified as suspicious.

---

### Thomas's login

Thomas has:

```python
failed_attempts = 1
trusted_device = True
```

Python evaluates:

```text
1 >= 5            → False
not True          → False
False or False    → False
```

Therefore:

```python
suspicious = False
```

His login appears normal.

---

### Admin's login

Admin has:

```python
failed_attempts = 6
trusted_device = True
```

Python evaluates:

```text
6 >= 5            → True
not True          → False
True or False     → True
```

Therefore:

```python
suspicious = True
```

The repeated failed attempts trigger the alert.

---

### UnknownUser's login

UnknownUser has:

```python
failed_attempts = 3
trusted_device = False
```

Python evaluates:

```text
3 >= 5            → False
not False         → True
False or True     → True
```

Therefore:

```python
suspicious = True
```

The unknown device triggers the alert.

---

### Repeating the indented code

Everything indented beneath:

```python
for event in login_events:
```

runs once for every login record.

The loop performs this process:

```text
Take one login event
        ↓
Read its values
        ↓
Evaluate the security conditions
        ↓
Print the result
        ↓
Move to the next event
```

When no events remain, the loop ends.

---

## Expected output

```text
=== LOGIN EVENT ANALYSIS ===

User: Thomas
Failed attempts: 1
Trusted device: True
Result: Login appears normal.

User: Admin
Failed attempts: 6
Trusted device: True
Result: Suspicious login detected.

User: UnknownUser
Failed attempts: 3
Trusted device: False
Result: Suspicious login detected.
```

---

## How to run

Open a terminal inside the lesson folder and run:

```bash
python lesson.py
```

---

## Memory hooks

```text
List      = Collection of security records
Dictionary = One organized security record
for loop  = Examine every record automatically
event     = Current record being examined
```

```python
for event in login_events:
```

means:

```text
For every login event, run the indented instructions.
```

---

## Cybersecurity connection

Security analysts rarely examine only one event.

A real security tool may process:

- Thousands of login attempts
- Network connections
- Firewall alerts
- Malware hashes
- User accounts
- Files
- IP addresses

A `for` loop allows Python to repeat the same investigation logic
for every item without copying the code many times.
