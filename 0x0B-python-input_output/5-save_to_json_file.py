#!/usr/bin/python3
""" Make save_to_json_string function """


import json


def save_to_json_file(my_obj, filename):
    """Write json object to text file """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
