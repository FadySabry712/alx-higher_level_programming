#!/usr/bin/python3

def safe_print_integer(value):
    value = isdigit()
    try:
        if value == True:
            print("{:d}".format(value))
            return True
    except (TypeError, ValueError):
            return False

