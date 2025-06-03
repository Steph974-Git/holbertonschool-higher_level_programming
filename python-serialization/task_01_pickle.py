#!/usr/bin/python3
"""
Module for custom object serialization using pickle.

This module defines a CustomObject class that can be serialized and
deserialized using Python's pickle module, allowing objects to be
saved to files and loaded back into memory.
"""

import pickle


class CustomObject:
    """
    Class representing a custom object with serialization capabilities.

    This class stores basic information about a person and provides methods
    to serialize/deserialize instances using the pickle module.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes to standard output.

        Prints the name, age, and student status in a formatted way.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize this object instance to a file using pickle.

        Args:
            filename (str): Path to the file where the object will be saved
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): Path to the file containing the pickled object

        Returns:
            CustomObject: The deserialized object, or None if an error occurred
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
