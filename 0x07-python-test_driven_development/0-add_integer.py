#!/usr/bin/python3

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

    Doctests:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    # Check if a or b is NaN
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    # Check if a is neither an integer nor a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if b is neither an integer nor a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast the numbers to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
