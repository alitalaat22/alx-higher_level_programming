#!/usr/bin/python
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new = list(my_list)
        new[idx] = element
        return new