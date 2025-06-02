#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object

    Args:
        my_obj: Python object to serialize

    Returns:
        str: JSON string representation
    """
    return json.dumps(my_obj)
