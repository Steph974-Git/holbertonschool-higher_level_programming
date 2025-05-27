#!/usr/bin/python3
"""
Module implementing a verbose list.

This module provides a VerboseList class that extends the built-in list
with additional output messages for common list operations.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when modified.

    This class inherits from the built-in list class and overrides
    several methods to provide feedback when the list is manipulated.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print confirmation.

        Args:
            item: The object to append to the list
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extend the list with items from an iterable and print confirmation.

        Args:
            x: An iterable whose elements are added to the list
        """
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """
        Remove the first occurrence of an item and print confirmation.

        Args:
            item: The object to remove from the list

        Raises:
            ValueError: If the item is not present in the list
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        """
        Remove and return an item at given position and print confirmation.

        Args:
            item (int, optional): The index of the item to remove.
                                  Defaults to -1 (last item).

        Returns:
            The removed item

        Raises:
            IndexError: If the list is empty or index is out of range
        """
        elem = self[item]
        super().pop(item)
        print("Popped [{}] from the list.".format(elem))
        return elem
