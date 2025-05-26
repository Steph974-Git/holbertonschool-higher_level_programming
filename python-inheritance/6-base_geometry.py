#!/usr/bin/python3
"""
Module for geometric shape base class.

This module defines the BaseGeometry class which serves as a foundation
for implementing various geometric shapes.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.

    This class provides a framework for geometry calculations
    with methods to be implemented by subclasses.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method is not implemented in the base class and
        should be overridden by subclasses.

        Raises:
            Exception: Always raises an exception indicating
                      that the method is not implemented.
        """
        raise Exception("area() is not implemented")
