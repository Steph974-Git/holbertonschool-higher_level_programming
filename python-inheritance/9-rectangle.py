#!/usr/bin/python3
"""
Module that defines the Rectangle class inheriting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of Rectangle

        Returns:
            str: Formatted rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
