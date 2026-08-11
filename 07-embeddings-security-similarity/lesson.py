"""
Lesson 07 — Embeddings and Security Similarity

This lesson demonstrates the basic idea behind embeddings:
representing information as numbers and comparing how
similar two pieces of information are.
"""

import math


# Example vectors representing security events.
# These are simplified learning examples, not real AI-generated embeddings.

failed_login = [0.9, 0.8, 0.1]
brute_force = [0.8, 0.9, 0.2]
malware_alert = [0.1, 0.2, 0.9]


def cosine_similarity(vector_a, vector_b):
    # Multiply matching positions and add the results.
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    # Calculate the length of each vector.
    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    # Compare the direction of the two vectors.
    return dot_product / (magnitude_a * magnitude_b)


print("=== SECURITY EVENT SIMILARITY ===")

login_vs_bruteforce = cosine_similarity(
    failed_login,
    brute_force
)

login_vs_malware = cosine_similarity(
    failed_login,
    malware_alert
)

print(
    f"Failed login vs brute force: "
    f"{login_vs_bruteforce:.3f}"
)

print(
    f"Failed login vs malware: "
    f"{login_vs_malware:.3f}"
)
