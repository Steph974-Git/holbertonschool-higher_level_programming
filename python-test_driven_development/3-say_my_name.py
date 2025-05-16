#!/usr/bin/python3
"""
Personal identifier module
This module provides functionality for personal name formatting
and presentation in a formal, structured manner.
"""


def say_my_name(first_name, last_name=""):
    """
    Announces a person's complete name with professional formatting.

    Creates a formal introduction string by combining the provided
    name components into a standardized greeting format that can
    be displayed to the user or stored for later use.

    Args:
        first_name (str): The individual's given or personal name
        last_name (str, optional): The family or surname. Defaults to empty.

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
