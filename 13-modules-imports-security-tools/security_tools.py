"""
Security Tools Module

This module contains reusable cybersecurity functions
that can be imported into other Python programs.
"""


def check_failed_attempts(attempts):
    return attempts >= 5


def check_device(trusted_device):
    return not trusted_device


def calculate_risk(attempts, trusted_device):

    if check_failed_attempts(attempts) and check_device(trusted_device):
        return "High"

    if check_failed_attempts(attempts) or check_device(trusted_device):
        return "Medium"

    return "Low"
