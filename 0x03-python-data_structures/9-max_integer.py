#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    else:
        b = my_list[0]
        for i in my_list:
            if i > b:
                b = i
        return b
