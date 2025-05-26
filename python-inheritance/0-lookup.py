#!/usr/bin/python3
"""
Module providing attribute lookup functionality.

This module defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Return list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods
              available on the given object.
    """
    return dir(obj)
