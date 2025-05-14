#!/usr/bin/python3
"""
Module for integer addition operations.
This module provides a function to add two integers.
The function can also handle floats, but they will
be cast to integers before the operation.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result.
    If a or b is a float, they are first cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
