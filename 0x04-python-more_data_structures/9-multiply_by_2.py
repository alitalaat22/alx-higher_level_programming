#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ne = {}
    for i in a_dictionary:
        s = a_dictionary[i]
        ne[i] = s * 2
    return ne
