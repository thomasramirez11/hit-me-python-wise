# Lesson 08 — JSON for Security Data

## Lesson objective

Learn how Python converts structured cybersecurity information
between Python dictionaries and JSON.

JSON is commonly used to store and exchange information between:

- Applications
- APIs
- Security tools
- Cloud services
- Configuration files
- AI systems

---

## Python concepts

- JSON
- Dictionaries
- `import`
- `json.dumps()`
- `json.loads()`
- Variables
- F-strings

---

## Cybersecurity scenario

A security system detects a suspicious login.

Python stores the alert as a dictionary containing:

- Username
- Source IP
- Failed login attempts
- Device trust status
- Severity

The program converts the dictionary into JSON so the information
could be shared with another system.

---

## What This Lesson Demonstrates

### Starting with a Python dictionary

```python
security_alert = {
    "username": "Admin",
    "source_ip": "192.168.1.50",
    "failed_attempts": 7,
    "trusted_device": False,
    "severity": "High"
}
```

This is normal Python data.

It contains keys and values describing one security alert.

```text
username        → Admin
source_ip       → 192.168.1.50
failed_attempts → 7
trusted_device  → False
severity        → High
```

---

### Importing the JSON module

```python
import json
```

Python includes a built-in module named `json`.

It provides tools for converting between Python objects and JSON.

### Memory hook

```text
Python dictionary ↔ JSON
```

Think of the `json` module as the translator between them.

---

### Converting Python into JSON

```python
json_alert = json.dumps(
    security_alert,
    indent=4
)
```

`json.dumps()` converts a Python object into a JSON string.

The name can be remembered as:

```text
dump s
     ↓
dump to string
```

The option:

```python
indent=4
```

formats the JSON so humans can read it more easily.

Python:

```python
False
```

becomes JSON:

```json
false
```

Notice the lowercase letters.

---

### JSON representation

The security alert becomes:

```json
{
    "username": "Admin",
    "source_ip": "192.168.1.50",
    "failed_attempts": 7,
    "trusted_device": false,
    "severity": "High"
}
```

JSON looks similar to a Python dictionary, but JSON is a
data format rather than a Python object.

This allows programs written in different languages to exchange
the same information.

---

### Converting JSON back into Python

```python
restored_alert = json.loads(json_alert)
```

`json.loads()` reads JSON text and converts it back into
Python data.

Memory trick:

```text
loads = load from string
```

After conversion:

```python
restored_alert
```

is once again a Python dictionary.

We can therefore access:

```python
restored_alert["username"]
```

just like any other dictionary.

---

### The full data journey

```text
Python dictionary
        ↓
json.dumps()
        ↓
JSON string
        ↓
json.loads()
        ↓
Python dictionary
```

The information remains the same.

Only its representation changes.

---

## Expected output

```text
=== PYTHON DICTIONARY ===
{'username': 'Admin', 'source_ip': '192.168.1.50', 'failed_attempts': 7, 'trusted_device': False, 'severity': 'High'}

=== JSON DATA ===
{
    "username": "Admin",
    "source_ip": "192.168.1.50",
    "failed_attempts": 7,
    "trusted_device": false,
    "severity": "High"
}

=== RESTORED SECURITY DATA ===
Username: Admin
Source IP: 192.168.1.50
Severity: High
Trusted device: False
```

---

## How to run

Run:

```bash
python lesson.py
```

The `json` module is included with Python, so no additional
packages are required.

---

## Memory hooks

```text
Dictionary = Python's structured data
JSON       = Portable structured data
```

```text
json.dumps()
Python → JSON string
```

```text
json.loads()
JSON string → Python
```

---

## Cybersecurity connection

Cybersecurity tools frequently exchange JSON data.

For example, a security API might return:

```json
{
    "ip": "10.0.0.25",
    "risk": "high",
    "blocked": true
}
```

Python can receive this JSON, convert it into a dictionary,
analyze the values, and make a security decision.

JSON is commonly encountered when working with:

- SIEM platforms
- Threat-intelligence APIs
- Cloud-security tools
- Vulnerability scanners
- Authentication systems
- Security automation
