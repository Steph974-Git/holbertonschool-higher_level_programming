#!/usr/bin/python3
"""
Module for saving Python objects to JSON files
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: Python object to be serialized
        filename (str): Path to the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
