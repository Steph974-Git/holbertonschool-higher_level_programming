#!/usr/bin/python3
"""
Module for converting CSV files to JSON format.

This module provides functionality to read data from CSV files
and convert it to JSON format, saving the result to a file.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert data from a CSV file to JSON format.

    This function reads data from a CSV file, converts it to a list of
    dictionaries, and saves the result as a JSON file named 'data.json'.

    Args:
        filename (str): Path to the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    try:
        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f)
        return True
    except BaseException:
        return False
