#!/usr/bin/python3
"""
Geometric pattern generator module
This module provides utilities for creating visual shapes
using ASCII characters for mathematical and artistic purposes.
"""


def print_square(size):
    """
    Generates a perfect square pattern using hash symbols.

    Creates a visual representation of a square with equal sides,
    where each position in the grid is filled with the # character,
    resulting in a solid square visualization in the terminal.

    Args:
            size (int): The side length measurement of the square

    Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
            TypeError: If size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
