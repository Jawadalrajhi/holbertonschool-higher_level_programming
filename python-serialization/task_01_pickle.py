#!/usr/bin/env python3
"""Module for custom object serialization using pickle.

This module provides a CustomObject class that can serialize and
deserialize itself using Python's pickle module.
"""
import pickle


class CustomObject:
    """A custom class with serialization capabilities.

    Attributes:
        name (str): The name of the object.
        age (int): The age value.
        is_student (bool): Student status.
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age value.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in formatted output."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file.

        Args:
            filename (str): Name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file.

        Args:
            filename (str): Name of the file containing serialized object.

        Returns:
            CustomObject: Deserialized instance, or None if error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
