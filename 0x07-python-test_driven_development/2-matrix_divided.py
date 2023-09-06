#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.
    
    Args:
        matrix (list of lists): A matrix of numbers (int or float).
        div (int, float): The divisor.
        
    Returns:
        list of lists: A new matrix with the results.
        
    Raises:
        TypeError: If matrix is not a list of lists of ints/floats, 
                   if div is not a number, or if rows have different sizes.
        ZeroDivisionError: If div is zero.
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(not all(isinstance(n, (int, float)) for n in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]

