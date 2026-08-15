# Lesson 14 — Lambda Functions for Security Filtering

## Lesson objective

Learn how Python lambda functions create small functions using
compact one-line syntax.

This lesson uses lambda functions to:

- Detect suspicious failed-login activity
- Sort security events by failed-attempt count

---

## Python concepts

- Lambda functions
- Function arguments
- Boolean expressions
- `sorted()`
- `key=`
- `reverse=True`
- Lists
- Dictionaries

---

## Cybersecurity scenario

A security system contains several login events.

The program needs to:

1. Determine whether each event is suspicious
2. Rank events from highest to lowest failed-login count

A lambda function can handle small pieces of logic without
creating a larger named function.

---

## What This Lesson Demonstrates

### Normal function vs lambda

A normal function could be written as:

```python
def is_suspicious(attempts):
    return attempts >= 5
```

The lambda version is:

```python
is_suspicious = lambda attempts: attempts >= 5
```

Both perform the same basic job.

The lambda is simply more compact.

### Memory hook

```text
def    = Full reusable function
lambda = Quick one-line function
```

---

### Understanding the lambda

```python
lambda attempts: attempts >= 5
```

Break it into pieces:

```text
lambda
```

means:

```text
Create a small function.
```

Then:

```text
attempts
```

is the parameter.

Finally:

```text
attempts >= 5
```

is the value Python evaluates and automatically returns.

So if:

```python
attempts = 7
```

Python evaluates:

```text
7 >= 5 → True
```

---

### Calling the lambda

```python
suspicious = is_suspicious(
    event["failed_attempts"]
)
```

For Thomas:

```text
1 >= 5 → False
```

For Admin:

```text
7 >= 5 → True
```

For UnknownUser:

```text
10 >= 5 → True
```

---

### Lambda inside `sorted()`

The lesson also uses:

```python
sorted_events = sorted(
    security_events,
    key=lambda event: event["failed_attempts"],
    reverse=True
)
```

The `sorted()` function needs to know:

```text
What value should I use to sort each event?
```

This lambda answers:

```python
lambda event: event["failed_attempts"]
```

For each dictionary, Python extracts the failed-attempt count.

Conceptually:

```text
Thomas      → 1
Admin       → 7
UnknownUser → 10
Maria       → 3
```

---

### Understanding `key=`

```python
key=lambda event: event["failed_attempts"]
```

`key=` tells `sorted()`:

> Use this value when deciding the order.

Without `key=`, Python would not know which dictionary value
should determine the ranking.

---

### Understanding `reverse=True`

```python
reverse=True
```

normally changes:

```text
Lowest → Highest
```

into:

```text
Highest → Lowest
```

For security analysis, this means the events with the most failed
attempts appear first.

The final order becomes:

```text
UnknownUser → 10
Admin       → 7
Maria       → 3
Thomas      → 1
```

---

## Expected output

```text
=== SECURITY EVENT CHECK ===

Thomas | Failed attempts: 1 | Suspicious: False
Admin | Failed attempts: 7 | Suspicious: True
UnknownUser | Failed attempts: 10 | Suspicious: True
Maria | Failed attempts: 3 | Suspicious: False

=== EVENTS SORTED BY RISK ===

UnknownUser | Failed attempts: 10
Admin | Failed attempts: 7
Maria | Failed attempts: 3
Thomas | Failed attempts: 1
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
lambda = Small one-line function
```

Basic structure:

```python
lambda input: result
```

Example:

```python
lambda attempts: attempts >= 5
```

Think:

```text
Receive attempts
        ↓
Check security rule
        ↓
Return True or False
```

---

## Cybersecurity connection

Lambda functions can be useful for small operations such as:

```text
Sorting alerts by severity
Filtering suspicious events
Ranking vulnerability scores
Extracting timestamps
Checking simple conditions
```

They are especially useful when another Python function needs a
small piece of logic temporarily.

For larger or more complicated security logic, a normal `def`
function is usually easier to read and maintain.
