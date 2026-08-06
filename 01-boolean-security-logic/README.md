# Lesson 01 — Boolean Security Logic

## Lesson objective

Learn how Python uses Boolean values and security conditions to:

- Grant or deny access
- Detect suspicious behavior
- Trigger a security alert

---

## Python concepts

- `True` and `False`
- Variables
- `all()`
- `any()`
- `not`
- Comparisons
- `if` and `else`
- F-strings

---

## Cybersecurity scenario

A user attempts to log in.

The program checks:

- Whether the password is correct
- Whether MFA was approved
- Whether the account is active
- Whether too many failed attempts occurred
- Whether the device is unknown

It then decides whether access should be granted and whether an alert should be generated.

---

## What This Lesson Demonstrates

### Boolean values

```python
password_correct = True
mfa_approved = False
```

Booleans represent two possible states:

```text
True  = Yes / Approved / Active
False = No / Denied / Inactive
```

### Access control with `all()`

```python
access_granted = all([
    password_correct,
    mfa_approved,
    account_active
])
```

`all()` requires every condition to be `True`.

Python evaluates:

```text
True, False, True
```

Because MFA is `False`:

```python
access_granted = False
```

### Threat detection with `any()`

```python
danger_detected = any([
    failed_attempts >= 5,
    unknown_device,
    not account_active
])
```

`any()` requires only one condition to be `True`.

There are six failed attempts and the device is unknown, so:

```python
danger_detected = True
```

### Reversing a value with `not`

```python
not account_active
```

`not` reverses a Boolean:

```text
not True  → False
not False → True
```

### Final decision

The program reaches these results:

```python
access_granted = False
danger_detected = True
```

Therefore:

- The login is denied
- A security alert is generated

---

## Expected output

```text
=== SECURITY LOGIN CHECK ===
Password correct: True
MFA approved: False
Account active: True
Failed attempts: 6
Unknown device: True

Access granted: False
Danger detected: True

Decision: Deny the login.
Security action: Send an alert to the analyst.
```

---

## How to run

Open the terminal inside this folder and run:

```bash
python lesson.py
```

---

## Memory hooks

```text
all() = Every guard must approve
any() = One alarm is enough
not   = Reverse the answer
```
