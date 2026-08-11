"""
Lesson 06 — Virtual Environments

This lesson demonstrates how Python can detect
whether the current program is running inside
a virtual environment.
"""

import sys


print("=== PYTHON ENVIRONMENT CHECK ===")

print(f"Python executable: {sys.executable}")
print(f"Current environment: {sys.prefix}")
print(f"Base Python installation: {sys.base_prefix}")

print()


# Compare the current environment with the main Python installation.
inside_virtual_environment = sys.prefix != sys.base_prefix


if inside_virtual_environment:
    print("Status: Virtual environment is ACTIVE.")
else:
    print("Status: Using the GLOBAL Python environment.")
