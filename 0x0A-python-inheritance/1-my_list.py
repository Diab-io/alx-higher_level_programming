#!/usr/bin/python3

"""
    module: 1-my_list
"""

class MyList(list):

    """Represents a list"""

    def print_sorted(self):
        """ Prints the represented list in ascending order """
        print(sorted(self))
