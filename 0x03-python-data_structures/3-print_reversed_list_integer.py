#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return None
    k = len(my_list)
    for i in range(0, k):
        print("{:d}".format(my_list[k - i - 1]))
