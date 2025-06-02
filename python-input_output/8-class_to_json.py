#!/usr/bin/python3
"""
Module for converting class instances to JSON dictionaries.

This module provides a function that returns the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return a dictionary description of an object for JSON serialization.

    Returns the dictionary of all attributes that are serializable:
    list, dictionary, string, integer and boolean.

    Args:
        obj: An instance of a Class

    Returns:
        dict: A dictionary representation of the object
    """
    return obj.__dict__
