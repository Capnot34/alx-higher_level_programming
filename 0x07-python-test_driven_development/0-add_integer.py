#!/usr/bin/python3
"""
This module contains a function to add two numbers: `add_integer`.

The function can add two integers or floats. If the numbers are floats, they
are cast to integers before the addition. If either of the numbers isn't an
integer or a float, the function raises a TypeError.

You can use this module as a script to run doctests or import the `add_integer`
function in other modules.
"""

def add_integer(a, b=98):

    """
    Add two numbers (integers/floats). If they are floats, they are casted to
    integers before addition.

    Args:
    a : int or float
        The first number.
    b : int or float, optional
        The second number (default is 98).

    Returns:
    int
        The sum of a and b.

    Raises:
    TypeError
        If a or b are neither int nor float.

    Returns:
        sum of a and b.

    """


    # Handle NaN by replacing with 89
    if a != a:
        a = 89
    if b != b:
        b = 89

    # Check if a is neither an integer nor a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if b is neither an integer nor a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for float overflow before casting to integers
    result_float = a + b
    if result_float == float('inf') or result_float == -float('inf'):
        raise OverflowError("Float overflow occurred")

    # Cast the numbers to integers after ensuring there's no float overflow
    a = int(a)
    b = int(b)

    # Return the sum
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
