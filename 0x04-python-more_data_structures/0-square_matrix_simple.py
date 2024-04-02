#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        list = []
        for clon in row:
            list.append(clon * clon)
        new.append(list)
    return new
