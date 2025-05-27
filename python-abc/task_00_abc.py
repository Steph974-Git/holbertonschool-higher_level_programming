#!/usr/bin/python3
"""
Module implementing abstract animal classes.

This module defines an abstract Animal class and concrete implementations
for different animal types using Python's ABC (Abstract Base Class).
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing generic animal behavior.

    This class serves as a contract that ensures all animal subclasses
    implement required methods like sound production.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method representing the sound an animal makes.

        This method must be implemented by all concrete animal subclasses.

        Returns:
            str: The sound representation as a string
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.

    Implements the Animal abstract class with dog-specific behaviors.
    """

    def sound(self):
        """
        Return the sound a dog makes.

        Returns:
            str: The string "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.

    Implements the Animal abstract class with cat-specific behaviors.
    """

    def sound(self):
        """
        Return the sound a cat makes.

        Returns:
            str: The string "Meow"
        """
        return "Meow"
