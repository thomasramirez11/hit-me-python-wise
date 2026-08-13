# Lesson 11 — Decorators for Security Logging

## Lesson objective

Learn how Python decorators add extra behavior to functions
without modifying the original function's main logic.

This lesson uses a decorator to automatically log when a
security function starts and finishes.

---

## Python concepts

- Decorators
- Functions inside functions
- `@decorator`
- `*args`
- `**kwargs`
- Return values
- `functools.wraps`
- `function.__name__`

---

## Cybersecurity scenario

Imagine a security application contains many functions:

```text
check_login()
scan_file()
analyze_ip()
verify_user()
```

We want every important function to create an audit message
when it runs.

Instead of manually adding logging code to every function,
we create one decorator and reuse it.

---

## What This Lesson Demonstrates

### Creating the decorator

```python
def security_log(function):
```

A decorator is itself a function.

It receives another function as its input.

In this lesson:

```text
security_log
        ↓
receives
        ↓
check_login
```

### Memory hook

```text
Decorator = Wrapper around another function
```

Think of the original function as a package.

The decorator adds another layer around that package.

---

### The wrapper function

Inside the decorator we create:

```python
def wrapper(*args, **kwargs):
```

The wrapper becomes the new function that Python runs.

It allows us to execute code:

```text
BEFORE the original function
        ↓
ORIGINAL function
        ↓
AFTER the original function
```

In our example:

```text
Security log: Starting
        ↓
check_login()
        ↓
Security log: Finished
```

---

### Understanding `*args`

```python
*args
```

collects positional arguments.

For:

```python
check_login("Admin", 7)
```

the values are essentially:

```text
"Admin"
7
```

This allows the wrapper to accept different function arguments
without knowing all of them in advance.

---

### Understanding `**kwargs`

```python
**kwargs
```

collects keyword arguments.

For example:

```python
check_login(
    username="Admin",
    failed_attempts=7
)
```

Keyword arguments have names connected to their values.

Together:

```python
*args, **kwargs
```

make the decorator flexible enough to work with many functions.

---

### Calling the original function

```python
result = function(*args, **kwargs)
```

The variable:

```python
function
```

contains the original function being decorated.

Python passes the original arguments into it.

For this lesson, that means Python eventually runs:

```python
check_login("Admin", 7)
```

The returned value is stored inside:

```python
result
```

---

### Returning the original result

```python
return result
```

The decorator should not lose the value returned by the
original function.

Our security function returns:

```text
Suspicious login detected.
```

The wrapper receives that value and returns it to the rest
of the program.

---

### Applying the decorator

```python
@security_log
def check_login(username, failed_attempts):
```

The `@` syntax tells Python:

```text
Take check_login
and wrap it with security_log.
```

Conceptually, this is similar to writing:

```python
check_login = security_log(check_login)
```

The `@` syntax is simply cleaner.

### Memory hook

```text
@decorator
=
Put this function through the wrapper
```

---

### Logging the function name

```python
function.__name__
```

Python functions contain information about themselves.

The special attribute:

```python
__name__
```

stores the function's name.

For our function:

```text
check_login
```

Therefore the decorator can automatically print:

```text
[SECURITY LOG] Starting: check_login
```

without manually writing the function name.

---

### Why `@wraps(function)` is used

```python
@wraps(function)
```

helps preserve information about the original function.

Without it, Python may treat the decorated function as if its
name were:

```text
wrapper
```

instead of:

```text
check_login
```

`wraps()` helps the decorated function keep its original identity.

---

### The execution flow

When Python reaches:

```python
result = check_login("Admin", 7)
```

the actual flow becomes:

```text
Call check_login
        ↓
Decorator wrapper starts
        ↓
Print security START log
        ↓
Run original check_login()
        ↓
Return suspicious result
        ↓
Print security FINISH log
        ↓
Return the original result
        ↓
Store result
```

---

## Expected output

```text
=== SECURITY FUNCTION MONITOR ===

[SECURITY LOG] Starting: check_login
Checking login for: Admin
[SECURITY LOG] Finished: check_login

Final result: Suspicious login detected.
```

---

## How to run

Run:

```bash
python lesson.py
```

No additional packages are required.

---

## Memory hooks

```text
Decorator = Add behavior around a function
```

```text
@security_log
= Wrap this function with security logging
```

```text
wrapper()
= Code surrounding the original function
```

```text
*args
= Positional arguments
```

```text
**kwargs
= Keyword arguments
```

---

## Cybersecurity connection

Decorators are useful for adding repeated security behavior such as:

```text
Logging
Authentication
Authorization
Audit trails
Timing
Error handling
Permission checks
```

Instead of rewriting that logic inside every function, one
decorator can apply the same rule consistently across many
parts of a security application.
