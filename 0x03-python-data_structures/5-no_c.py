#!/usr/bin/python3
def no_c(my_string):
    n = ''
    for i in range(len(my_string)):
        if my_string[i].lower() != 'c':
            n += my_string[i]
    return n
