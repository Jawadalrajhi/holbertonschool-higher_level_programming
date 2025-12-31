#!/usr/bin/python3

"""
    Module to fetch, print, and save posts from a JSONPlaceholder API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    fetch_and_print_posts
    Fetches and prints the titles of posts from a JSONPlaceholder API.

    Catch the response
    Show the status code
    if Status code is succeed; loop through json and print title
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        json_obj = response.json()

        for item in json_obj:
            print(f"{item['title']}")
        return True

    else:
        return False


def fetch_and_save_posts():
    """
    fetch_and_save_posts Fetch all post and save them in a CSV file

    Catch the resposne
    Show the status code
    Delete useless data
    Define CSV column name
    Write data in CSV file

    Returns:
        _type_: _description_
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:

        json_obj = response.json()
        filename = "posts.csv"

        for item in json_obj:
            del item["userId"]

        field_names = ['id', 'title', 'body']

        try:
            with open(filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(json_obj)
        except IOError:
            return False

    return True
