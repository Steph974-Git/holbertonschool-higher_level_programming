#!/usr/bin/python3
"""
Advanced text formatting module
This module provides sophisticated text manipulation utilities
for enhancing readability and formatting of natural language
content with proper typographical spacing.
"""


def text_indentation(text):
    """
    Formats text with enhanced readability through strategic line breaks.

    Transforms standard paragraph text into a more structured format by
    inserting double line breaks after punctuation marks that typically
    indicate logical breaks in written discourse. This creates a visual
    hierarchy and improves readability of complex textual content.

    Args:
        text (str): The input content to be reformatted

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
