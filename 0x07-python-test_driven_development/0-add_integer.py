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
    """

    
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
        
if __name__ == "__main__":
    import doctest
     doctest.testfile("tests/0-add_integer.txt")
