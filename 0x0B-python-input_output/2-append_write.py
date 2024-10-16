#!/usr/bin/python3
""" Make read_file function """


def append_file(filename="", text=""):
    """ Reads file name with UTF-8 encoding """
    with open(filename, "a", encoding='UTF-8') as f:
        return f.write(text)
