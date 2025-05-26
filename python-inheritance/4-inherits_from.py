#!/usr/bin/python3
"""
Module that provides inheritance checking functionality.

This module contains a function to check if an object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class that inherited from
    specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class) and not isinstance(obj, a_class)
