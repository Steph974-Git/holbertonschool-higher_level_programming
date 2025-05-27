#!/usr/bin/python3
"""
Module implementing a counting iterator.

This module provides a CountedIterator class which wraps any iterable
and counts how many items have been consumed from it.
"""


class CountedIterator:
    """
    Iterator that keeps track of how many items have been consumed.

    This class wraps any iterable object and maintains a count of how
    many times the __next__ method has successfully returned an item.
    """

    def __init__(self, iterable):
        """
        Initialize a new CountedIterator.

        Args:
            iterable: Any iterable object to be wrapped
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterator

        Raises:
            StopIteration: When the wrapped iterator is exhausted
        """
        try:
            item = next(self.iterator)
            self.count += 1
        except StopIteration:
            raise StopIteration

        return item

    def get_count(self):
        """
        Get the current count of consumed items.

        Returns:
            int: The number of items successfully retrieved so far
        """
        return self.count

    def __iter__(self):
        """
        Return self as an iterator.

        This method enables the CountedIterator to be used in a for loop.

        Returns:
            CountedIterator: Returns self
        """
        return self
