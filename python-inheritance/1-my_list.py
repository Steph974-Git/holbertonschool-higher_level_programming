#!/usr/bin/python3
"""
Module implementing a list subclass with additional functionality.

This module defines MyList, a class that inherits from list and
provides additional methods like printing a sorted version.
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list class.

    This class extends the standard list with additional methods
    for different ways to display or manipulate the list contents.
    """

    def print_sorted(self):
        """
        Print the list elements in sorted ascending order.

        This method does not modify the original list but prints
        a sorted version of it.
        """
        print(sorted(self))
