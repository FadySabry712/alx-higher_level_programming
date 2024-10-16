#!/usr/bin/python3
"""Make read_file function"""

def read_file(filename=""):
    """Reads file name with UTF-8 encoding"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
