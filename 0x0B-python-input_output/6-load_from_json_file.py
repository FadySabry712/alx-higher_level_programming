#!/usr/bin/python3
""" Make load_from_json_file function """


import json


def load_from_json_file(filename):
    """Load object from json file """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
