#!/usr/bin/env python3
"""Module for converting CSV data to JSON format.

This module provides functionality to read CSV files and convert
them to JSON format for easier data interchange.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format.

    Args:
        csv_filename (str): Name of the CSV file to convert.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
