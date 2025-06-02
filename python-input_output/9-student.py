#!/usr/bin/python3
"""
Module containing the Student class.

This module defines a Student class with first name, last name, and age
attributes, and a method to convert the object to a JSON dictionary.
"""


class Student:
    """
    Class representing a student.

    This class stores student personal information and provides methods
    to convert the object to a JSON-serializable dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary representation of the Student instance.

        Returns:
            dict: Dictionary representation of the student
        """
        return self.__dict__
