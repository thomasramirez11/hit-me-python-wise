# Lesson 05 — Functions for Security Checks

## Lesson objective

Learn how Python functions organize reusable pieces of code.

Instead of writing the same security logic repeatedly, we create
one function and use it for several login events.

---

## Python concepts

- `def`
- Functions
- Function calls
- Parameters
- Indentation
- Reusable code
- Boolean conditions
- `if` and `else`

---

## Cybersecurity scenario

A security system needs to analyze several login attempts.

Each login contains:

- A username
- Number of failed attempts
- Whether the device is trusted

Instead of rebuilding the security check for every user, one
function performs the investigation repeatedly.

---

## What This Lesson Demonstrates

### Creating a function

```python
def analyze_login(username, failed_attempts, trusted_device):
```

The keyword:

```python
def
```

means:

```text
Define a function.
```

The function is named:

```text
analyze_login
```

Think of a function as a reusable security tool.

### Memory hook

```text
def = Build the tool
function call = Use the tool
```

---

### Function parameters

The function receives:

```python
username
failed_attempts
trusted_device
```

These are parameters.

They act like temporary variables that receive information when
the function is called.

For example:

```python
analyze_login("Admin", 6, True)
```

Python effectively gives the function:

```text
username       → "Admin"
failed_attempts → 6
trusted_device → True
```

---

### Creating the security decision

```python
suspicious = (
    failed_attempts >= 5
    or not trusted_device
)
```

The login becomes suspicious when:

```text
Failed attempts are 5 or higher
OR
The device is not trusted
```

Because `or` is used, only one danger condition must be true.

---

### Calling the function

Writing:

```python
def analyze_login(...):
```

does not run the function.

It only creates it.

The function runs when Python reaches:

```python
analyze_login("Thomas", 1, True)
```

Then it runs again here:

```python
analyze_login("Admin", 6, True)
```

And again here:

```python
analyze_login("UnknownUser", 2, False)
```

The same security logic is reused three times.

---

### Why functions are useful

Without a function, we might copy the same code for every user.

That creates:

```text
Repeated code
More lines
More opportunities for mistakes
Harder maintenance
```

With a function:

```text
Write security logic once
        ↓
Reuse it many times
```

If the security rule changes later, we only need to update the
function in one place.

---

### How each login is evaluated

Thomas:

```text
1 >= 5       → False
not True     → False

False OR False → False
```

Result:

```text
Login appears normal.
```

Admin:

```text
6 >= 5       → True
not True     → False

True OR False → True
```

Result:

```text
Suspicious login detected.
```

UnknownUser:

```text
2 >= 5       → False
not False    → True

False OR True → True
```

Result:

```text
Suspicious login detected.
```

---

## Expected output

```text
=== SECURITY LOGIN ANALYZER ===

Checking user: Thomas
Failed attempts: 1
Trusted device: True
Result: Login appears normal.

Checking user: Admin
Failed attempts: 6
Trusted device: True
Result: Suspicious login detected.

Checking user: UnknownUser
Failed attempts: 2
Trusted device: False
Result: Suspicious login detected.
```

---

## How to run

Open a terminal inside this lesson folder and run:

```bash
python lesson.py
```

---

## Memory hooks

```text
def = Define/build the function
```

```text
function() = Run the function
```

```text
Parameters = Information entering the function
```

```text
Function = Reusable mini-program
```

---

## Cybersecurity connection

Functions are used constantly in cybersecurity programs.

Examples could include:

```python
scan_ip()
check_password()
analyze_log()
calculate_hash()
detect_alert()
```

Each function can specialize in one job.

Large security programs are often built from many smaller
functions working together.
