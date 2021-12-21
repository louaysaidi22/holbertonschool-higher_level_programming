#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            p = ord(c) - 32
        else:
            p = ord(c)
        print("{:c}".format(p), end='')
    print("")
