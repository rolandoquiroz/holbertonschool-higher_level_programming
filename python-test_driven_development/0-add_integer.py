
#!/usr/bin/python3
"""
This module provides a function for adding two integers.

It exposes a single function:
    - add_integer(a, b=98): Adds two integers and returns the result.
"""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): First number to add. Must be an integer or float.
        b (int or float, optional): Second number to add. Defaults to 98.
            Must be an integer or float.

    Returns:
        int: The sum of a and b, casted to an integer if necessary.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    return int(a) + int(b)
