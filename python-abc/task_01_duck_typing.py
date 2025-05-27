#!/usr/bin/python3
"""
Module demonstrating duck typing with geometric shapes.

This module shows how different shape classes can be used interchangeably
through a common interface, illustrating Python's duck typing principles.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class defining the interface for geometric shapes.

    This class establishes the contract that all shape implementations
    must provide methods to calculate area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Class representing a circle shape.

    Implements the Shape interface with calculations specific to circles.
    """

    def __init__(self, radius):
        """
        Initialize a circle with given radius.

        Args:
            radius (float): The radius of the circle
        """
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area using the formula πr²
        """
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter using the formula 2πr
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Class representing a rectangle shape.

    Implements the Shape interface with calculations specific to rectangles.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area using the formula width × height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter using the formula 2(width + height)
        """
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """
    Print area and perimeter information for any shape object.

    This function demonstrates duck typing by working with any object
    that implements area() and perimeter() methods, regardless of its type.

    Args:
        obj: Any object with area() and perimeter() methods
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
