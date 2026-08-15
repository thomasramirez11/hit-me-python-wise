# Lesson 15 — Recursion for Nested Security Scanning

## Lesson objective

Learn how recursion allows a Python function to call itself.

This lesson uses recursion to scan folders that may contain
other folders.

---

## Python concepts

- Recursion
- Recursive functions
- Base cases
- Function calls
- Return values
- Dictionaries
- Lists
- `for` loops
- `.endswith()`

---

## Cybersecurity scenario

A computer may contain folders inside other folders.

For example:

```text
root
├── downloads
└── documents
    └── archive
```

A security scanner cannot assume every file exists in only
one folder.

It may need to:

```text
Scan current folder
        ↓
Find another folder
        ↓
Scan that folder
        ↓
Find another folder
        ↓
Scan again
```

Recursion is useful for this type of nested structure.

---

## What This Lesson Demonstrates

### What is recursion?

Recursion happens when a function calls itself.

Our function is:

```python
def scan_folder(folder):
```

Later, inside that same function, Python runs:

```python
scan_folder(subfolder)
```

So:

```text
scan_folder()
     ↓
calls
     ↓
scan_folder()
```

### Memory hook

> Recursion = "Do the same job again on the smaller thing inside."

---

### Scanning the current folder

```python
for filename in folder["files"]:
```

Python examines every file belonging to the current folder.

Then:

```python
if filename.endswith(suspicious_extensions):
```

checks whether the filename ends with:

```text
.exe
.bat
.ps1
```

These extensions are used only as simplified learning examples.

A file extension alone does not prove that a file is malicious.

---

### Counting suspicious files

```python
suspicious_count += 1
```

Every time a suspicious example file is found, the counter
increases.

For example:

```text
payload.exe
```

causes:

```text
0 → 1
```

---

### The recursive call

This is the most important part:

```python
for subfolder in folder["folders"]:
    suspicious_count += scan_folder(subfolder)
```

Python finds each folder inside the current folder.

Then:

```python
scan_folder(subfolder)
```

calls the same function again.

For this lesson, the flow becomes:

```text
scan root
    ↓
scan downloads
    ↓
return to root
    ↓
scan documents
        ↓
    scan archive
```

The function keeps moving deeper until no more subfolders exist.

---

### The base case

Every recursive process needs a point where it stops.

Our stopping point happens when:

```python
folder["folders"]
```

is empty.

For example:

```python
"folders": []
```

The loop:

```python
for subfolder in folder["folders"]:
```

has nothing to process.

Therefore, Python does not call `scan_folder()` again.

That naturally stops the recursion.

### Memory hook

```text
Recursive case = Go deeper
Base case      = Nothing deeper remains
```

Without a stopping condition, recursion could continue forever
and eventually cause an error.

---

### Returning results upward

The function ends with:

```python
return suspicious_count
```

A nested folder returns its result to the folder that called it.

Imagine:

```text
archive finds 1
       ↓
returns 1 to documents
       ↓
documents returns its total
       ↓
root receives the total
```

This allows the final program to calculate:

```python
total_suspicious
```

across the entire folder structure.

---

## Expected output

```text
=== RECURSIVE SECURITY SCAN ===

Scanning folder: root
Scanning folder: downloads
  ALERT: Suspicious file found: payload.exe
Scanning folder: documents
Scanning folder: archive
  ALERT: Suspicious file found: backdoor.exe

Total suspicious files: 2
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
Recursion = Function calls itself
```

```text
Recursive case = Continue deeper
```

```text
Base case = Stop going deeper
```

Think of it like opening folders:

```text
Open folder
   ↓
See another folder
   ↓
Open that folder
   ↓
Repeat
```

---

## Cybersecurity connection

Recursive techniques can help security tools examine:

- Nested folders
- Directory trees
- Nested JSON
- Process trees
- Organizational structures
- Network relationships

For example, a forensic tool may need to scan:

```text
C:
└── Users
    └── User
        └── Downloads
            └── suspicious_file.exe
```

Instead of knowing exactly how deeply the file is stored,
a recursive function can keep exploring until there are no
more folders to inspect.
