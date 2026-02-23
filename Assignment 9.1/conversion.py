#Lab 9.1
#Problem 4
"""
conversion.py

Utility functions for number system conversions:
- Decimal to Binary
- Binary to Decimal
- Decimal to Hexadecimal
"""

def decimal_to_binary(n):
    """Convert a decimal integer to its binary string representation."""
    if n < 0:
        raise ValueError("Only non-negative integers allowed")
    return bin(n)[2:]


def binary_to_decimal(b):
    """Convert a binary string to its decimal integer representation."""
    if not all(ch in "01" for ch in b):
        raise ValueError("Input must be a binary string")
    return int(b, 2)


def decimal_to_hexadecimal(n):
    """Convert a decimal integer to its hexadecimal string representation."""
    if n < 0:
        raise ValueError("Only non-negative integers allowed")
    return hex(n)[2:].upper()
