#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization.

This module provides functions to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Name of the output JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename (str): Name of the input JSON file.

    Returns:
        dict: Deserialized Python dictionary from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
