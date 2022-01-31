#!/usr/bin/python3
"""task1"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
