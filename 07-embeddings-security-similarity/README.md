# Lesson 07 — Embeddings and Security Similarity

## Lesson objective

Understand the basic idea behind embeddings.

Embeddings represent information as groups of numbers called
vectors.

Those vectors can then be compared to determine how similar
two pieces of information are.

---

## Python concepts

- Lists
- Functions
- `zip()`
- `sum()`
- Generator expressions
- `math.sqrt()`
- Return values
- Floating-point numbers

---

## Cybersecurity scenario

Imagine an AI security system analyzing alerts such as:

- Failed login
- Brute-force attack
- Malware detection

Instead of comparing only the words, an AI system can represent
their meaning using numerical vectors.

Events with similar meanings may produce vectors that are closer
to each other.

---

## What This Lesson Demonstrates

### What is an embedding?

An embedding is a numerical representation of information.

For this lesson:

```python
failed_login = [0.9, 0.8, 0.1]
```

The list represents a simplified vector.

Real AI embeddings may contain hundreds or thousands of numbers.

Our vectors are manually created only to demonstrate the concept.

### Memory hook

```text
Text or information
        ↓
Numbers
        ↓
Vector
        ↓
Compare meaning
```

---

### Comparing vectors

The program uses:

```python
cosine_similarity(vector_a, vector_b)
```

This function compares two vectors.

A similarity score closer to:

```text
1
```

means the vectors point in similar directions.

A lower score means they are less similar.

---

### Using `zip()`

```python
zip(vector_a, vector_b)
```

pairs matching positions.

Example:

```text
[0.9, 0.8, 0.1]
[0.8, 0.9, 0.2]
```

becomes pairs like:

```text
0.9 ↔ 0.8
0.8 ↔ 0.9
0.1 ↔ 0.2
```

Python then multiplies each pair.

---

### The dot product

```python
dot_product = sum(
    a * b for a, b in zip(vector_a, vector_b)
)
```

Python:

1. Pairs the numbers
2. Multiplies each pair
3. Adds the results

The dot product helps measure how much two vectors point in
the same direction.

---

### Vector magnitude

```python
math.sqrt(
    sum(a * a for a in vector_a)
)
```

This calculates the length of a vector.

The similarity calculation uses both:

```text
Direction
and
Length
```

to compare the vectors correctly.

---

### Returning the similarity

```python
return dot_product / (magnitude_a * magnitude_b)
```

The function returns the final similarity score.

That result is stored in variables such as:

```python
login_vs_bruteforce
```

and:

```python
login_vs_malware
```

---

### Why the results are different

The vectors for:

```text
Failed login
Brute-force attack
```

contain similar numbers.

Therefore their similarity score should be relatively high.

The malware vector is very different.

Therefore:

```text
Failed login ↔ Brute force
```

should be more similar than:

```text
Failed login ↔ Malware
```

---

## Expected output

The exact values come from the mathematical calculation, but
the result will look similar to:

```text
=== SECURITY EVENT SIMILARITY ===
Failed login vs brute force: 0.990
Failed login vs malware: 0.324
```

The important idea is not memorizing the numbers.

The important idea is:

```text
Higher similarity score
=
More similar vectors
```

---

## How to run

Run:

```bash
python lesson.py
```

No extra Python packages are required.

---

## Memory hooks

```text
Embedding = Meaning represented as numbers
```

```text
Vector = List of numerical features
```

```text
Similarity = How closely two vectors match
```

```text
Closer to 1 = More similar
```

---

## Cybersecurity connection

AI-powered security systems can use embeddings to help compare:

- Security alerts
- Log messages
- Malware descriptions
- Threat reports
- Incident reports
- Vulnerability descriptions

For example, two alerts may use different words but describe
similar behavior.

Embeddings can help a system recognize that their meanings are
related.
