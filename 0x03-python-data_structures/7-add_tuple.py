#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Padding tuples with 0 if they are smaller than 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Summing corresponding elements from the tuples
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    # Returning a tuple with the sums
    return (sum_1, sum_2)
