#!/usr/bin/python3
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last = triangle[-1]
            row.extend(last[j] + last[j + 1] for j in range(len(last) - 1))
            row.append(1)
        triangle.append(row)
    return triangle
