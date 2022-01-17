#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = [0] * list_length
    for i in range(0, list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
            my_list_3[i] = c
        except TypeError:
            c = 0
            print("wrong type")
        except IndexError:
            c = 0
            print("out of range")
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        finally:
            continue
    return my_list_3
