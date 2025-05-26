#!/usr/bin/python3
"""
Module defining Square class that inherits from Rectangle.

This module implements a Square as a specialized Rectangle
where width and height are equal.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    A square is a rectangle with equal width and height.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): Length of each side of the square.
                        Must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size
