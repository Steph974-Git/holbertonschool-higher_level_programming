#!/usr/bin/python3
"""
Module for appending to text files
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename (str): Path to the file to append to
        text (str): Text to append to the file

    Returns:
        int: Number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
