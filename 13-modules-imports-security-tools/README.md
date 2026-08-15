# Lesson 13 — Modules & Imports for Security Tools

## Lesson objective

Learn how Python modules allow code to be separated into multiple
files and reused through imports.

This lesson creates a security module containing reusable login
risk functions.

---

## Python concepts

- Modules
- `import`
- Functions
- Reusable code
- Dot notation
- Return values
- File organization

---

## Cybersecurity scenario

A security application needs several reusable checks:

- Detect excessive failed login attempts
- Detect untrusted devices
- Calculate a login risk level

Instead of placing all the code in one large file, the security
functions are stored inside:

```text
security_tools.py
```

The main program imports and uses them.

---

## What This Lesson Demonstrates

### What is a module?

A Python file can act as a module.

Our file:

```text
security_tools.py
```

contains reusable security functions.

Think of it as a toolbox:

```text
security_tools.py
│
├── check_failed_attempts()
├── check_device()
└── calculate_risk()
```

### Memory hook

```text
Module = Python toolbox
Import = Bring the toolbox into the program
```

---

### Importing the module

```python
import security_tools
```

Python searches for the module and makes its contents available.

Because `security_tools.py` is in the same folder as `lesson.py`,
Python can import it directly.

---

### Using dot notation

```python
security_tools.calculate_risk(
    failed_attempts,
    trusted_device
)
```

The dot:

```text
.
```

means:

```text
Use something belonging to this module.
```

So:

```python
security_tools.calculate_risk
```

means:

```text
Use calculate_risk() from security_tools.py
```

---

### Functions calling other functions

Inside the module:

```python
if check_failed_attempts(attempts) and check_device(trusted_device):
```

`calculate_risk()` calls two other functions.

For this login:

```text
failed_attempts = 7
trusted_device = False
```

Python evaluates:

```text
7 >= 5
→ True
```

and:

```text
not False
→ True
```

Both danger conditions are true.

Therefore:

```python
return "High"
```

---

### Why separate files?

Without modules:

```text
One giant Python file
↓
Harder to read
Harder to maintain
Harder to reuse
```

With modules:

```text
Main program
     ↓
Imports specialized tools
     ↓
Cleaner organization
```

This becomes increasingly important as projects grow.

---

## Expected output

```text
=== LOGIN RISK ANALYSIS ===
Username: Admin
Failed attempts: 7
Trusted device: False
Risk level: High
```

---

## How to run

Make sure both Python files are in the same folder:

```text
lesson.py
security_tools.py
```

Then run:

```bash
python lesson.py
```

---

## Memory hooks

```text
Module = Another Python file containing useful code
```

```python
import security_tools
```

means:

```text
Make that module available here.
```

```python
security_tools.calculate_risk()
```

means:

```text
Run calculate_risk() from that module.
```

---

## Cybersecurity connection

Larger cybersecurity programs can separate responsibilities into
different modules.

For example:

```text
scanner.py
logging_tools.py
network_tools.py
file_analysis.py
authentication.py
```

Then a main program can import only the tools it needs.

This makes security software easier to organize, test, maintain,
and expand.
