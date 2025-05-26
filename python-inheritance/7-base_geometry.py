#!/usr/bin/python3
"""
Module for geometric shape calculations.

This module provides a base class for various geometric shapes,
with methods for calculating area and validating integers.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.

    This class serves as a foundation for creating geometry-related classes,
    providing common functionality like area calculation and value validation.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: Always raises an exception as this method
                       is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
