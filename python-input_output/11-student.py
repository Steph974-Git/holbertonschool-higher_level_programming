#!/usr/bin/python3
"""
Module containing the Student class.

This module defines a Student class with first name, last name, and age
attributes, and methods to convert the object to and from JSON dictionaries.
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

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes must
        be retrieved.

        Args:
            attrs (list, optional): List of attributes to include.
                                   Defaults to None.

        Returns:
            dict: Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    my_dict[attr] = getattr(self, attr)
            return my_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from json.

        This method updates the instance attributes based on a provided
        dictionary where the keys correspond to attribute names.

        Args:
            json (dict): Dictionary where keys are attribute names and
                        values are attribute values to be set

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
