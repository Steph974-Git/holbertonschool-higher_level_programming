#!/usr/bin/python3
"""
Module implementing a Dragon class with swimming and flying capabilities.

This module demonstrates the use of mixins to compose behaviors
that can be reused across different classes.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.

    This mixin can be used with any class that needs to be able to swim.
    """

    def swim(self):
        """
        Make the creature swim.

        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.

    This mixin can be used with any class that needs to be able to fly.
    """

    def fly(self):
        """
        Make the creature fly.

        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon with multiple abilities.

    Dragon inherits swimming ability from SwimMixin and flying ability
    from FlyMixin, demonstrating multiple inheritance and composition.
    """

    def roar(self):
        """
        Make the dragon roar.

        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")


draco = Dragon()
