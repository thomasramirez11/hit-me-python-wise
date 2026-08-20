# Lesson 17 — User Input for Security Analysis

## Lesson objective

Learn how Python receives information from a user with `input()`
and uses that information inside a cybersecurity decision.

Instead of storing every value directly in the code, the analyst
can provide the information while the program is running.

---

## Python concepts

- `input()`
- Variables
- Strings
- `int()`
- `.lower()`
- Boolean comparisons
- `if` and `else`
- F-strings

---

## Cybersecurity scenario

A security analyst wants to investigate a login event.

The program asks for:

- Username
- Number of failed attempts
- Whether the device is trusted

Python then analyzes the information and determines whether the
login should be considered suspicious.

---

## What This Lesson Demonstrates

### Receiving text with `input()`

```python
username = input("Enter username: ")
```

`input()` pauses the program and waits for the user to type
something.

If the analyst enters:

```text
Admin
```

Python stores:

```python
username = "Admin"
```

### Memory hook

```text
input() = Ask the human for information
```

---

### `input()` returns text

Even if the user types:

```text
7
```

Python initially receives it as:

```python
"7"
```

That is a string.

Because we want to compare the number mathematically, we convert it:

```python
failed_attempts = int(
    input("Enter number of failed attempts: ")
)
```

The process becomes:

```text
User types:
"7"
 ↓
input()
 ↓
String "7"
 ↓
int()
 ↓
Integer 7
```

Now Python can evaluate:

```python
7 >= 5
```

---

### Cleaning text with `.lower()`

The program asks:

```python
trusted_answer = input(
    "Is the device trusted? (yes/no): "
).lower()
```

`.lower()` converts uppercase letters into lowercase letters.

For example:

```text
YES
Yes
yes
```

all become:

```text
yes
```

This makes the program easier for a human to use.

---

### Converting the answer into a Boolean

```python
trusted_device = trusted_answer == "yes"
```

Python compares the user's answer with:

```text
"yes"
```

If:

```python
trusted_answer = "yes"
```

then:

```text
"yes" == "yes" → True
```

Therefore:

```python
trusted_device = True
```

If the user enters:

```text
no
```

then:

```text
"no" == "yes" → False
```

Therefore:

```python
trusted_device = False
```

---

### Making the security decision

```python
suspicious = (
    failed_attempts >= 5
    or not trusted_device
)
```

The program considers the login suspicious when:

```text
Five or more failed attempts
OR
The device is not trusted
```

For example:

```text
failed_attempts = 7
trusted_device = False
```

Python evaluates:

```text
7 >= 5        → True
not False     → True

True OR True  → True
```

Therefore:

```python
suspicious = True
```

---

### Hard-coded data vs user input

Earlier lessons often used:

```python
username = "Admin"
```

The programmer decided the value before running the program.

With:

```python
username = input("Enter username: ")
```

the value can change every time the program runs.

This makes the program interactive.

---

## Example run

```text
=== LOGIN SECURITY CHECK ===

Enter username: Admin
Enter number of failed attempts: 7
Is the device trusted? (yes/no): no

=== ANALYSIS RESULT ===
Username: Admin
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

Then answer the questions directly in the terminal.

---

## Memory hooks

```text
input() = Receive information from the user
```

```text
input() normally returns a string
```

```text
int() = Convert text into an integer
```

```text
.lower() = Normalize text to lowercase
```

---

## Cybersecurity connection

Interactive security tools may ask an analyst for information such as:

```text
IP address
Username
File path
Port number
Severity level
Investigation choice
```

For example:

```python
ip_address = input("Enter IP to investigate: ")
```

User input allows a program to work with different evidence
without changing the source code every time.
