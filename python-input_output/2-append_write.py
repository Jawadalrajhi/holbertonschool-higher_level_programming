#!/usr/bin/python3
"""Module that defines append_write to add text at the end of a UTF-8 file.

This module provides a function that appends a given string to the end of a
text file using the with statement and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF-8) and return added char count.

    If the file does not exist, it is created. Permission or existence
    exceptions are not managed, per the requirements.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
