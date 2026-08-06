# Lesson 04 — While Loops for Login Protection

## Lesson objective

Learn how a Python `while` loop repeats instructions while a
condition remains `True`.

This lesson simulates a login-monitoring system that:

- Counts failed login attempts
- Displays a warning after repeated failures
- Locks the account after five failed attempts

---

## Python concepts

- `while` loops
- Loop conditions
- Counters
- `+=`
- Comparison operators
- `if` statements
- Boolean values
- Avoiding infinite loops

---

## Cybersecurity scenario

A user repeatedly enters an incorrect password.

The system allows a maximum of five failed attempts.

After three failed attempts, the activity is marked as suspicious.

After five failed attempts, the account is locked to help prevent
unauthorized access or password guessing.

---

## What This Lesson Demonstrates

### Starting the counter

```python
failed_attempts = 0
```

The program begins with zero failed attempts.

This variable acts as a counter.

Every time another failed login occurs, its value increases.

---

### Setting the maximum

```python
maximum_attempts = 5
```

This variable stores the security limit.

Once the number of failed attempts reaches five, the loop must stop
and the account should be locked.

Keeping the number in a variable makes it easier to change later.

---

### Storing the account status

```python
account_locked = False
```

The account begins unlocked.

Later, the program changes this value to:

```python
True
```

when the maximum number of attempts is reached.

---

### Starting the `while` loop

```python
while failed_attempts < maximum_attempts:
```

The `while` loop asks:

```text
Are failed attempts still below the maximum?
```

At the beginning:

```text
0 < 5 → True
```

Because the condition is `True`, Python enters the loop.

Python repeats the indented code until the condition becomes `False`.

### Memory hook

> A `while` loop means: keep going while this condition is true.

---

### Increasing the counter

```python
failed_attempts += 1
```

This is a shorter version of:

```python
failed_attempts = failed_attempts + 1
```

Each time the loop repeats, one failed attempt is added.

```text
0 → 1
1 → 2
2 → 3
3 → 4
4 → 5
```

Updating the counter is important because it allows the loop
condition to eventually become `False`.

---

### Detecting suspicious activity

```python
if failed_attempts == 3:
    print("Warning: Suspicious login activity detected.")
```

The `==` operator checks whether two values are equal.

When the counter reaches three:

```text
3 == 3 → True
```

Python prints the warning.

This warning only appears once because the counter equals three
during only one loop repetition.

---

### Locking the account

```python
if failed_attempts == maximum_attempts:
    account_locked = True
```

When the fifth failed attempt occurs:

```text
5 == 5 → True
```

The account status changes from:

```python
False
```

to:

```python
True
```

The program also prints:

```text
Security action: Account locked.
```

---

### How the loop stops

After the fifth repetition:

```python
failed_attempts = 5
maximum_attempts = 5
```

Python checks the loop condition again:

```text
5 < 5 → False
```

Because the condition is now `False`, Python exits the loop.

The program continues with the code below the loop.

---

### Avoiding an infinite loop

A dangerous version would be:

```python
while failed_attempts < maximum_attempts:
    print("Failed login detected")
```

The value of `failed_attempts` never changes.

Therefore, the condition remains:

```text
0 < 5 → True
```

forever.

This creates an infinite loop.

The correct program includes:

```python
failed_attempts += 1
```

so the loop can eventually finish.

### Memory hook

> A `while` loop needs an exit door.

In this lesson, increasing the counter creates that exit door.

---

## Execution flow

```text
Start with zero failed attempts
        ↓
Check the while condition
        ↓
Add one failed attempt
        ↓
Display the attempt
        ↓
Check for the warning threshold
        ↓
Check for the lockout threshold
        ↓
Repeat until five attempts are reached
        ↓
Exit the loop
        ↓
Display the final account status
```

---

## Expected output

```text
=== LOGIN ATTEMPT MONITOR ===
Failed login attempt: 1
Failed login attempt: 2
Failed login attempt: 3
Warning: Suspicious login activity detected.
Failed login attempt: 4
Failed login attempt: 5
Security action: Account locked.

=== FINAL SECURITY STATUS ===
Total failed attempts: 5
Account locked: True
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
while = Repeat while a condition is true
```

```text
+= 1 = Increase the counter by one
```

```text
Counter changes = Loop can eventually stop
```

```text
Counter never changes = Possible infinite loop
```

---

## Cybersecurity connection

Security systems use repeated monitoring to track events such as:

- Failed login attempts
- Network connection retries
- Repeated authentication failures
- Incoming security alerts
- Device-status checks
- Processes that must remain active

A `while` loop is useful when the program does not simply want to
process a fixed list.

Instead, it continues working until a security condition changes.
