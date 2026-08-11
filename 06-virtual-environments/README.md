# Lesson 06 — Virtual Environments for Safe Python Projects

## Lesson objective

Learn what a Python virtual environment is and why isolated
environments are useful when building Python projects.

A virtual environment allows one project to install packages
without changing the global Python installation.

---

## Python concepts

- Virtual environments
- `venv`
- Python interpreters
- Package isolation
- `sys`
- `sys.prefix`
- `sys.base_prefix`
- Boolean comparisons

---

## Cybersecurity scenario

Imagine two cybersecurity projects.

Project A requires:

```text
Package version 1
```

Project B requires:

```text
Package version 2
```

Installing everything globally could create conflicts.

Virtual environments isolate each project:

```text
Project A
└── its own packages

Project B
└── its own packages
```

This follows an important security principle:

> Isolation limits unintended interaction between systems.

---

## What This Lesson Demonstrates

### The global Python installation

When Python is installed on the computer, there is a main
Python environment.

Programs can install packages into this global environment.

Example:

```bash
pip install requests
```

Without a virtual environment, that package may become available
to many Python projects on the computer.

---

### Creating a virtual environment

From inside the project folder:

```bash
python -m venv .venv
```

Breaking this down:

```text
python
```

Runs Python.

```text
-m
```

Tells Python to run a module.

```text
venv
```

Is Python's built-in virtual-environment module.

```text
.venv
```

Is the folder where the isolated environment will be created.

### Memory hook

```text
venv = private Python workspace
```

---

### Activating the environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal usually shows something similar to:

```text
(.venv)
```

That tells us commands such as:

```bash
python
pip
```

now use the project's virtual environment.

---

### Detecting the environment with Python

The lesson uses:

```python
import sys
```

The `sys` module provides information about the Python interpreter
currently running the program.

---

### `sys.executable`

```python
sys.executable
```

Shows the actual Python executable running the script.

Inside a virtual environment, the path may look similar to:

```text
...\project\.venv\Scripts\python.exe
```

This helps us see which Python interpreter is being used.

---

### `sys.prefix`

```python
sys.prefix
```

Represents the current Python environment.

When a virtual environment is active, this normally points to
the virtual-environment folder.

---

### `sys.base_prefix`

```python
sys.base_prefix
```

Represents the original Python installation used to create
the virtual environment.

---

### Checking whether the environment is active

```python
inside_virtual_environment = sys.prefix != sys.base_prefix
```

The `!=` operator means:

```text
Not equal to
```

If both paths are different:

```text
Current environment != Base environment
```

then Python is running inside a virtual environment.

The result becomes:

```python
True
```

If they are the same:

```python
False
```

Python is using the global environment.

---

### Deactivating the environment

When finished:

```bash
deactivate
```

This returns the terminal to the normal global Python environment.

---

## Expected output

When the virtual environment is active:

```text
=== PYTHON ENVIRONMENT CHECK ===
Python executable: ...\.venv\Scripts\python.exe
Current environment: ...\.venv
Base Python installation: ...

Status: Virtual environment is ACTIVE.
```

Without the virtual environment:

```text
Status: Using the GLOBAL Python environment.
```

---

## How to run

Create the environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```bash
python lesson.py
```

When finished:

```bash
deactivate
```

---

## Memory hooks

```text
Global Python = Shared toolbox
Virtual environment = Private toolbox
```

```text
python -m venv .venv
= Create the private toolbox
```

```text
activate
= Enter the toolbox
```

```text
deactivate
= Leave the toolbox
```

---

## Cybersecurity connection

Virtual environments help separate dependencies between projects.

This is useful when experimenting with tools such as:

```text
Scapy
Flask
Requests
Cryptography libraries
Security APIs
```

If one project needs a different package version, it can remain
isolated from other projects.

The mindset is similar to network segmentation:

```text
Separate things that do not need to interfere with each other.
```
