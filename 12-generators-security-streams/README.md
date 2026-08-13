# Lesson 12 — Generators for Security Data Streams

## Lesson objective

Learn how Python generators produce information one item at a time
instead of returning everything at once.

This lesson uses a generator to find suspicious login events.

---

## Python concepts

- Generators
- `yield`
- Functions
- `for` loops
- Dictionaries
- Lazy evaluation
- Memory-efficient processing

---

## Cybersecurity scenario

A security system receives login events.

Instead of building another complete list containing every
suspicious event, the program creates a generator.

The generator examines the events and produces suspicious
records one at a time.

A login is considered suspicious when:

```text
failed attempts >= 5
```

---

## What This Lesson Demonstrates

### A normal function with `return`

A normal function might use:

```python
return result
```

Once Python reaches `return`, the function sends the value back
and finishes.

Conceptually:

```text
Function starts
     ↓
Does work
     ↓
return
     ↓
Function ends
```

---

### A generator uses `yield`

Our generator contains:

```python
yield event
```

`yield` behaves differently from `return`.

Instead of permanently ending the function, Python:

```text
Produces one value
       ↓
Pauses the function
       ↓
Remembers its position
       ↓
Continues later
```

### Memory hook

```text
return = Give the answer and go home.

yield = Give one answer, pause, and wait for the next request.
```

---

### Creating the generator

```python
def find_suspicious_events(events):
```

This looks like a normal function.

But because the function contains:

```python
yield
```

Python treats it as a generator function.

---

### Examining each event

```python
for event in events:
```

The generator examines one security event at a time.

Then:

```python
if event["failed_attempts"] >= 5:
```

checks whether the event reaches the suspicious-login threshold.

---

### Producing a suspicious event

```python
yield event
```

If the event is suspicious, Python produces that event.

For Admin:

```text
7 >= 5 → True
```

Python yields the Admin record.

The generator pauses.

When another result is requested, Python continues where it stopped.

---

### Creating the generator object

```python
suspicious_events = find_suspicious_events(
    security_events
)
```

This does not immediately process and return every result.

Instead, Python creates a generator object.

Think:

```text
suspicious_events
        ↓
Security-event dispenser
```

The events are produced when the program asks for them.

---

### Using the generator

```python
for event in suspicious_events:
```

The `for` loop repeatedly asks the generator:

```text
Give me the next suspicious event.
```

The generator continues processing until no events remain.

In this lesson it produces:

```text
Admin
UnknownUser
```

---

### Why generators are useful

Imagine processing:

```text
10 events
```

Storing everything at once is easy.

But imagine:

```text
10,000,000 log entries
```

Creating another giant list may require a large amount of memory.

A generator can process information incrementally:

```text
Read one event
     ↓
Analyze it
     ↓
Produce result if needed
     ↓
Move to next event
```

The program does not necessarily need to hold every processed
result in memory at the same time.

---

## Expected output

```text
=== SUSPICIOUS EVENT STREAM ===

ALERT: Admin has 7 failed attempts.
ALERT: UnknownUser has 10 failed attempts.
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
return = Finish and return a value
```

```text
yield = Produce one value and pause
```

```text
Generator = Produces information when requested
```

Think of a generator like a security-log conveyor belt:

```text
Event
  ↓
Inspect
  ↓
Yield if suspicious
  ↓
Next event
```

---

## Cybersecurity connection

Security systems may process very large amounts of information:

- Authentication logs
- Firewall events
- Network packets
- SIEM alerts
- File records
- Threat-intelligence data

Generators are useful when information can be processed
incrementally instead of loading or creating everything at once.

This allows Python programs to work efficiently with streams
of security data.
