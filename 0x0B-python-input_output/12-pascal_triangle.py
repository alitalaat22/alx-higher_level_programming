#!/usr/bin/python3
"""this module"""


def pascal_triangle(n):
    """dsfsfasdf"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        now = [1]
        for cal in range(1, len(prev)):
            now.append(prev[cal - 1] + prev[cal])
        now.append(1)
        triangle.append(now)

    return triangle
