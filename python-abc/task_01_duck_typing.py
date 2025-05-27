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
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle shape."""

    def __init__(self, radius):
        """Initialize a circle with given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Print area and perimeter information for any shape object.
    
    This function demonstrates duck typing by working with any object
    that implements area() and perimeter() methods, regardless of its type.
    """
    # Note: No isinstance() check here! Pure duck typing.
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))


# A completely non-Shape class that still works with shape_info
class Duck:
    """
    A class completely unrelated to Shape hierarchy.
    
    This class is not a shape at all but still works with shape_info()
    because it implements the required methods - this is duck typing.
    """
    
    def area(self):
        """Calculate arbitrary 'area' value."""
        return 42
    
    def perimeter(self):
        """Calculate arbitrary 'perimeter' value."""
        return 16


# Test code demonstrating duck typing
if __name__ == "__main__":
    # Create instances
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    # Duck has nothing to do with Shape but works with shape_info
    duck = Duck()
    
    # Show that shape_info works with Shape subclasses
    print("Circle information:")
    shape_info(circle)
    
    print("\nRectangle information:")
    shape_info(rectangle)
    
    # Show pure duck typing - Duck isn't a Shape but works anyway!
    print("\nDuck information (not a Shape but works thanks to duck typing):")
    shape_info(duck)
    
    # Explicit demonstration of duck typing concept
    print("\nDUCK TYPING DEMONSTRATION:")
    print("- The Duck class is NOT a Shape or derived from Shape")
    print("- We don't check types in shape_info with isinstance()")
    print("- We just call the methods and expect them to work")
    print("- 'If it walks like a duck and quacks like a duck, it's a duck'")
