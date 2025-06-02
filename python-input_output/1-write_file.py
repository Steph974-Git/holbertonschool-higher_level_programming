#!/usr/bin/python3
"""
Module for writing to text files
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename (str): Path to the file to write to
        text (str): Text to write to the file

    Returns:
        int: Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
