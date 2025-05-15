#!/usr/bin/python3
"""
Mathematical operations module for matrix manipulation.
This module contains functions for performing arithmetic
operations on matrices of numbers.
"""


def matrix_divided(matrix, div):
    """
    Performs element-wise division on a matrix with precision control.

    Each element in the input matrix will be divided by the specified
    divisor and rounded to 2 decimal places for numerical stability.

    Args:
        matrix: A 2D array (list of lists) containing only numbers
        div: The divisor to apply to each matrix element

    Returns:
        A fresh matrix containing the division results, with original
        matrix left unmodified

    Raises:
        TypeError: For invalid matrix structure or non-numeric values
        ZeroDivisionError: When attempting division by zero
    """
    if not isinstance(
        matrix,
        list) or matrix == [] or not all(
        isinstance(
            row,
            list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
