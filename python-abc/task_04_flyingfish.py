#!/usr/bin/python3
"""
Module demonstrating multiple inheritance with a FlyingFish.

This module shows how a class can inherit from multiple parent classes
and override methods to create a specialized behavior, while also showing
method resolution order (MRO) in Python's multiple inheritance system.
"""


class Fish:
    """
    Class representing a fish with aquatic abilities.

    Provides basic fish behaviors including swimming and habitat information.
    """

    def swim(self):
        """
        Make the fish swim.

        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Describe the fish's habitat.

        Prints a message about where fish typically live.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird with aerial abilities.

    Provides basic bird behaviors including flying and habitat information.
    """

    def fly(self):
        """
        Make the bird fly.

        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Describe the bird's habitat.

        Prints a message about where birds typically live.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish with both aquatic and aerial abilities.

    Inherits from both Fish and Bird classes, demonstrating multiple
    inheritance,
    and overrides methods to provide specialized behaviors.
    """

    def swim(self):
        """
        Make the flying fish swim.

        Overrides the Fish swim method with flying fish specific behavior.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Make the flying fish fly.

        Overrides the Bird fly method with flying fish specific behavior.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Describe the flying fish's habitat.

        Overrides habitat methods from both parent classes to describe
        the flying fish's dual habitat.
        """
        print("The flying fish lives both in water and the sky!")

    def mro(self):
        """
        Display the Method Resolution Order for the FlyingFish class.

        Prints the inheritance hierarchy that Python uses to resolve
        method calls in this multiple inheritance scenario.
        """
        print(FlyingFish.mro())
