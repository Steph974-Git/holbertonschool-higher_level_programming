#!/usr/bin/python3
"""
Module defining Square class that inherits from Rectangle.

This module creates a Square class as a special case of Rectangle
where all sides have equal length.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    A square is a special rectangle where all sides are of equal length.
    This class provides specific implementation for such shapes.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (length of each side).
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

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A formatted string with the square's dimensions.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
