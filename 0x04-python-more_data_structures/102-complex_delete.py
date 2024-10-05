#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in list(_dictionary.items()):
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
