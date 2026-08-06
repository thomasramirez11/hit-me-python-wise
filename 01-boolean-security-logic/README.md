# Lesson 01 — Boolean Security Logic

## Lesson objective

This lesson demonstrates how Python Boolean values and logical
operators can be used to simulate a basic cybersecurity access-control
decision.

## Python concepts practiced

- Variables
- Boolean values: `True` and `False`
- The `or` operator
- The `and` operator
- The `not` operator
- The `print()` function

## Cybersecurity scenario

A security system evaluates several conditions before granting access:

- Is the password correct?
- Is multi-factor authentication correct?
- Was a failed login detected?
- Was a suspicious IP address detected?

A correct password alone is not always enough. The system must evaluate
all security conditions before making its final decision.

## Important security logic

```python
danger_detected = (
    failed_login_detected
    or suspicious_ip_detected
)
```

The `or` operator means that one danger signal is enough to activate
the alert.

```python
access_granted = (
    password_correct
    and mfa_correct
    and not danger_detected
)
```

Access is granted only when:

1. The password is correct.
2. MFA is correct.
3. No danger has been detected.

## Expected output

```text
Danger detected: True
Access granted: False
```

## Why access is denied

The password and MFA are correct, but a failed login was detected.

Therefore:

```text
True or False = True
```

This makes `danger_detected` equal to `True`.

Python then reverses that value:

```text
not True = False
```

The final access decision becomes:

```text
True and True and False = False
```

Therefore, access is denied.

## Memory hooks

- `or` = one alarm is enough
- `and` = every security guard must approve
- `not` = reverse the answer

## What I learned

I learned that Python can combine several Boolean conditions to make a
security decision.

I also learned that a user can provide the correct password and MFA but
still be denied access when suspicious activity is detected.

## Ethical-use statement

This code is a safe educational simulation. It does not connect to a
real authentication system or collect real user information.
