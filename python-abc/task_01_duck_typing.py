#!/usr/bin/python3
"""Module demonstrating duck typing with shapes"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate shape area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate shape perimeter"""
        pass


class Circle(Shape):
    """Circle implementation"""

    def __init__(self, radius):
        """Initialize with radius"""
        self.radius = radius

    def area(self):
        """Calculate circle area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate circle circumference"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation"""

    def __init__(self, width, height):
        """Initialize with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Display shape information using duck typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Create objects that inherit from Shape
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    # Create a simple class that doesn't inherit from Shape
    class NonShape:
        def area(self):
            return 100

        def perimeter(self):
            return 40

    # Create an instance of the non-Shape class
    non_shape = NonShape()

    # Test all objects with shape_info
    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)

    print("\nNon-Shape object:")
    shape_info(non_shape)  # Works due to duck typing!
