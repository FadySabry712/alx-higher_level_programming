#!/usr/bin/python3
""" Make append_file function """


def append_write(filename="", text=""):
    """ Reads file name with UTF-8 encoding """
    with open(filename, "a", encoding='UTF-8') as f:
        return f.write(text)
