# Lesson 10 — Classes & Objects for Security Alerts

## Lesson objective

Learn how Python classes and objects can organize related
information and behavior together.

This lesson creates reusable security alert objects containing:

- Username
- Source IP address
- Failed login attempts
- Suspicious activity status

---

## Python concepts

- Classes
- Objects
- `class`
- `__init__()`
- `self`
- Attributes
- Methods
- Object creation
- Lists of objects

---

## Cybersecurity scenario

A security system receives many alerts.

Every alert should contain similar information:

```text
Username
Source IP
Failed attempts
Security status
```

Instead of creating separate variables for every alert, we create
a `SecurityAlert` class.

The class acts as the blueprint for every alert object.

---

## What This Lesson Demonstrates

### Creating a class

```python
class SecurityAlert:
```

The keyword:

```python
class
```

creates a new type of object.

`SecurityAlert` describes what every security alert should contain
and what actions it can perform.

### Memory hook

```text
Class  = Blueprint
Object = Actual thing built from the blueprint
```

Think of:

```text
Class  → Security alert design
Object → One actual security alert
```

---

### The `__init__()` method

```python
def __init__(self, username, source_ip, failed_attempts):
```

`__init__()` runs automatically when a new object is created.

For example:

```python
alert_one = SecurityAlert(
    "Thomas",
    "192.168.1.10",
    1
)
```

Python automatically sends those values into `__init__()`.

The parameters receive:

```text
username        → Thomas
source_ip       → 192.168.1.10
failed_attempts → 1
```

---

### Understanding `self`

Inside the class we use:

```python
self.username = username
```

`self` means:

```text
This specific object.
```

So:

```python
self.username
```

means:

```text
The username belonging to this particular security alert.
```

Different objects can therefore store different values.

Example:

```text
alert_one.username   → Thomas
alert_two.username   → Admin
alert_three.username → UnknownUser
```

### Memory hook

> `self` means “this object right here.”

---

### Object attributes

These lines create attributes:

```python
self.username = username
self.source_ip = source_ip
self.failed_attempts = failed_attempts
```

Attributes are information stored inside an object.

Think:

```text
SecurityAlert object
│
├── username
├── source_ip
├── failed_attempts
└── suspicious
```

---

### Creating the security status

```python
self.suspicious = failed_attempts >= 5
```

Python evaluates whether the alert contains five or more failed
login attempts.

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
9 >= 5 → True
```

Each object stores its own result.

---

### Creating a method

```python
def display_alert(self):
```

A function inside a class is called a:

```text
method
```

This method knows how to display the information belonging to
the current security alert.

We call it using:

```python
alert_one.display_alert()
```

The dot means:

```text
Use something belonging to this object.
```

---

### Creating objects

```python
alert_one = SecurityAlert(
    "Thomas",
    "192.168.1.10",
    1
)
```

This creates an object from the `SecurityAlert` blueprint.

We repeat the process for several alerts.

Each object follows the same structure but contains different data.

---

### Looping through objects

```python
for alert in alerts:
    alert.display_alert()
```

The list contains three `SecurityAlert` objects.

The `for` loop takes one object at a time and calls:

```python
display_alert()
```

This combines concepts from earlier lessons:

```text
Classes
+
Objects
+
Lists
+
For loops
+
Conditions
```

---

## Expected output

```text
=== SECURITY ALERT SYSTEM ===

User: Thomas
Source IP: 192.168.1.10
Failed attempts: 1
Status: Activity appears normal.

User: Admin
Source IP: 10.0.0.25
Failed attempts: 7
Status: Suspicious activity detected.

User: UnknownUser
Source IP: 172.16.0.50
Failed attempts: 9
Status: Suspicious activity detected.
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
Class     = Blueprint
Object    = Thing built from blueprint
Attribute = Information belonging to object
Method    = Action the object can perform
self      = This specific object
```

---

## Cybersecurity connection

Classes are useful when a program contains many similar security
entities.

Examples could include:

```python
SecurityAlert()
UserAccount()
NetworkDevice()
MalwareSample()
Vulnerability()
LogEntry()
```

Each class can contain both:

```text
DATA
+
BEHAVIOR
```

This makes larger cybersecurity programs much easier to organize.
