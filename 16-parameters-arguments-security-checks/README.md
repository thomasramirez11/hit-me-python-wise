# Lesson 16 — Parameters & Arguments for Security Checks

## Lesson objective

Understand the difference between parameters and arguments
when working with Python functions.

This lesson uses a reusable login-analysis function to process
different security events.

---

## Python concepts

- Functions
- Parameters
- Arguments
- Positional arguments
- Keyword arguments
- Boolean conditions
- Function calls

---

## Cybersecurity scenario

A security function analyzes login activity.

For every login, it needs three pieces of information:

- Username
- Number of failed attempts
- Whether the device is trusted

The function defines where that information belongs using
parameters.

The actual login information is supplied using arguments.

---

## What This Lesson Demonstrates

### Parameters

Look at the function definition:

```python
def analyze_login(username, failed_attempts, trusted_device):
```

These are the parameters:

```text
username
failed_attempts
trusted_device
```

Parameters are variables created by the function definition.

Think of them as empty security-report fields:

```text
Username:        ________
Failed attempts: ________
Trusted device:  ________
```

They are waiting to receive values.

### Memory hook

```text
Parameter = Placeholder
```

---

### Arguments

Now look at the function call:

```python
analyze_login(
    "Thomas",
    1,
    True
)
```

These are the arguments:

```text
"Thomas"
1
True
```

Arguments are the actual values sent into the function.

Python connects them to the parameters:

```text
PARAMETER           ARGUMENT

username        ←   "Thomas"
failed_attempts ←   1
trusted_device  ←   True
```

### Memory hook

```text
Argument = Actual value
```

---

### The values enter the function

When Python runs:

```python
analyze_login("Thomas", 1, True)
```

you can mentally imagine:

```python
username = "Thomas"
failed_attempts = 1
trusted_device = True
```

Those values are now available inside that function call.

The original arguments are not renamed.

The parameters simply receive their values.

---

### Positional arguments

This call uses positional arguments:

```python
analyze_login(
    "Thomas",
    1,
    True
)
```

Python matches values based on their position:

```text
1st argument → username
2nd argument → failed_attempts
3rd argument → trusted_device
```

Order therefore matters.

If the arguments were placed in the wrong positions,
the function could receive incorrect information.

---

### Keyword arguments

The second call uses:

```python
analyze_login(
    username="Admin",
    failed_attempts=7,
    trusted_device=False
)
```

These are keyword arguments.

Instead of relying only on position, we explicitly tell Python
which parameter receives each value.

```text
username       = "Admin"
failed_attempts = 7
trusted_device = False
```

This can make function calls easier to understand.

---

### Making the security decision

Inside the function:

```python
suspicious = (
    failed_attempts >= 5
    or not trusted_device
)
```

For Thomas:

```text
1 >= 5      → False
not True    → False

False OR False → False
```

Result:

```text
Login appears normal.
```

For Admin:

```text
7 >= 5       → True
not False    → True

True OR True → True
```

Result:

```text
Suspicious login detected.
```

---

## Expected output

```text
=== LOGIN SECURITY ANALYSIS ===

User: Thomas
Failed attempts: 1
Trusted device: True
Result: Login appears normal.

User: Admin
Failed attempts: 7
Trusted device: False
Result: Suspicious login detected.
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
Parameter = Empty slot defined by the function
Argument  = Actual value sent into that slot
```

Think of a security form:

```text
PARAMETERS

Username:        ______
Failed attempts: ______
Trusted device:  ______
```

Then a login event provides the:

```text
ARGUMENTS

Thomas
1
True
```

---

## Cybersecurity connection

Security functions often need information before they can
perform an analysis.

Examples:

```python
scan_ip(ip_address)
```

```python
check_hash(file_hash)
```

```python
analyze_login(username, attempts, device)
```

The parameters define what information the security tool needs.

The arguments provide the actual evidence being analyzed.
