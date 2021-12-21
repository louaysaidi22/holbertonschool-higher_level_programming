#!/usr/bin/python3
c = 97
while c < 123:
    if c != 101 and c != 113:
        print("{:c}".format(c), end='')
    c += 1
