#!/usr/bin/python3
"""
Module for XML serialization and deserialization.

This module provides functions to convert between Python dictionaries
and XML format, allowing data to be serialized to files and deserialized
back into Python objects.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): Path where the XML file will be saved

    Returns:
        None
    """
    root = ET.Element('root')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back to a Python dictionary.

    Args:
        filename (str): Path to the XML file to deserialize

    Returns:
        dict: Dictionary containing the data from the XML file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
