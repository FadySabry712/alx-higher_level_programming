#!/usr/bin/python3
"""Make a read file function """

def read_file(filename=""):
    """Reads file name with UTF-8 encoding """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
