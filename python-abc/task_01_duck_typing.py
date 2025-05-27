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
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area using the formula πr²
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter using the formula 2πr
        """
        return 2 * math.pi * self.radius


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
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area using the formula width × height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter using the formula 2(width + height)
        """
        return 2 * (self.width + self.height)


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


class Triangle:
    """
    Class representing a triangle shape.

    This class does NOT inherit from Shape but still works with shape_info()
    because it implements area() and perimeter() - pure duck typing.
    """

    def __init__(self, a, b, c):
        """
        Initialize a triangle with three sides.

        Args:
            a (float): Length of first side
            b (float): Length of second side
            c (float): Length of third side
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle
        """
        # Semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Heron's formula
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.

        Returns:
            float: The sum of all three sides
        """
        return self.a + self.b + self.c


# Testing code
if __name__ == "__main__":
    # Create shape instances
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)  # A 3-4-5 right triangle

    print("Circle information:")
    shape_info(circle)

    print("\nRectangle information:")
    shape_info(rectangle)

    print("\nTriangle information:")
    # This works even though Triangle doesn't inherit from Shape!
    shape_info(triangle)
