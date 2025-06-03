#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.

This module provides functions to serialize Python data structures to JSON
format and save them to files, as well as deserialize JSON data from files
back into Python objects.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize data to JSON and save it to a file.

    Args:
        data: Python data structure to serialize (must be JSON-serializable)
        filename (str): Path to the file where JSON data will be saved

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it.

    Args:
        filename (str): Path to the JSON file to read

    Returns:
        The Python data structure represented by the JSON in the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
