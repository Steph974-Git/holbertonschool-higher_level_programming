#!/usr/bin/python3
"""
Module for class instance checking.

This module provides a function to check if an object is an instance
of a specified class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance of specified class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a class that
              inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
