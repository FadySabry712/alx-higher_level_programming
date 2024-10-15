#!/usr/bin/python3
'''Modue for 1-my_list.py
'''


class MyList(list):
    ''' inherits from list() '''

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
