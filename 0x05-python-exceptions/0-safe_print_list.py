#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for lens in range(x):
            print(my_list,end='')
            print()
            return x
    except IndexError:
        print()
        return lens
            