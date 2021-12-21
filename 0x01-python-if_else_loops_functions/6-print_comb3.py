#!/usr/bin/python3
for i in range(0, 100):
    k = i % 10
    p = i / 10
    if p < k and i != 89:
        print("{:02d},".format(i), end=' ')
    elif i == 89:
        print("{:02d}".format(i))
