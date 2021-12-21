    #!/usr/bin/python3
    import random
    number = random.randint(-10000, 10000)
    if number < 0:
        n = -number
    else:
        n = number
    n = n % 10
    if n == 0:
        print("Last digit of {:d} is {:d}".format(number,n), "and is 0")
    elif n < 6:
        print("Last digit of {:d} is {:d}".format(number,n), "and is less than 6 and not 0")
    else:
        print("Last digit of {:d} is {:d}".format(number,n), "and is greater than 5")
