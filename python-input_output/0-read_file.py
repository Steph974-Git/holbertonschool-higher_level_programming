#!/usr/bin/python3
"""
Module for reading and printing file contents.

This module provides a function to read text files and print their contents
to the standard output.
"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
                        Defaults to empty string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
