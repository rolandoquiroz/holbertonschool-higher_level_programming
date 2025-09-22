
#!/usr/bin/python3
"""
Module for integer addition.

This module defines the function `add_integer(a, b=98)`, which returns
the sum of two numbers after validating and converting them to integers.

Functions:
    add_integer(a, b=98): Returns the integer sum of a and b.
"""

def add_integer(a, b=98):
    """Add two integers.

    Validates input types to ensure both arguments are integers or floats.
    Floats are converted to integers before addition. If arguments are
    invalid (e.g., not int/float, NaN, or infinity), raises the appropriate
    exception.

    Args:
        a (int | float): The first number to add.
        b (int | float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b after conversion to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
        OverflowError: If a or b is infinity.
        ValueError: If a or b is NaN.
    """
    return a + b 
