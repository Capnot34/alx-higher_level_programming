#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy

    Args:
    m_a (list of lists): First matrix
    m_b (list of lists): Second matrix

    Returns:
    Resultant matrix after multiplication
    """
    return np.matmul(m_a, m_b)

