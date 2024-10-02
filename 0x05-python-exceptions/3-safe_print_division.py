#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
        return c
    except:
        None
    finally:
        if c != 0:
            print("Inside Result: {}".format(c))
        else:
            print("Inside Result: None")
