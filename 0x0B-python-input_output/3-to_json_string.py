#!/usr/bin/python3
""" Make to_json_string function """


import json


def to_json_string(my_obj):
    """Return json string of an object """
    return json.dumps(my_obj)
