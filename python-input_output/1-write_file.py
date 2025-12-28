#!/usr/bin/python3
"""Module for writing to files.

This module provides a function to write a string to a text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """Write string to file and return character count.

    Args:
        filename (str): Path to the file. Defaults to empty string.
        text (str): Text to write. Defaults to empty string.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
