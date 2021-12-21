#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        c = 1
        d = a
        while c < b:
            d *= a
            c += 1
        return d
    else:
        c = 1
        if a < 0:
            d = -1
        else:
            d = 1
        while c <= -b:
            d /= a
            c += 1
        return d
