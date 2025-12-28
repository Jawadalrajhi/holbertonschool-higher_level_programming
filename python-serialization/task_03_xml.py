#!/usr/bin/env python3
"""Module for XML serialization and deserialization.

This module provides functions to serialize Python dictionaries to XML
and deserialize XML files back to Python dictionaries.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML format.

    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): Name of the output XML file.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML file to Python dictionary.

    Args:
        filename (str): Name of the input XML file.

    Returns:
        dict: Deserialized Python dictionary from the XML file.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
