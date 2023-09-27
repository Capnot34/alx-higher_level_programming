#!/usr/bin/python3
"""
This module provides a function to multiply two matrices together.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b together.

    Args:
    - m_a: List of lists of integers/floats representing the first matrix.
    - m_b: List of lists of integers/floats representing the second matrix.

    Returns:
    List of lists of integers/floats representing the resultant matrix.

    Raises:
    - TypeError: If m_a or m_b is not a list.
        If m_a or m_b is not a list of lists.
        If an element of m_a or m_b is not an integer or float.
        If m_a or m_b is not rectangular.
    - ValueError: If m_a or m_b is empty.
        If m_a and m_b cannot be multiplied.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be a list of lists")

    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("m_a or m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a and m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    row_len_b = len(m_b[0])

    if not all(len(row) == row_len_a for row in m_a) or not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_a and m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
