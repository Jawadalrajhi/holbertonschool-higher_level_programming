#!/usr/bin/python3
"""Module for converting class instances to dictionaries.

This module provides a function to convert class instances
to dictionary representation for JSON serialization.
"""


def class_to_json(obj):
    """Return dictionary description for JSON serialization.

    Args:
        obj: Instance of a class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object.
    """
    return obj.__dict__
