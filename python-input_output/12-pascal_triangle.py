#!/usr/bin/python3
"""
Module that provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    In Pascal's triangle, each number is the sum of the two numbers
    directly above it.

    Args:
        n (int): The number of rows to generate

    Returns:
        list: A list of lists representing Pascal's triangle
              Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    else:
        my_list = [[1]]
        for i in range(1, n):
            tri = [1]
            for j in range(len(my_list[i - 1]) - 1):
                tri.append(my_list[i - 1][j] + my_list[i - 1][j + 1])

            tri.append(1)
            my_list.append(tri)

        return my_list
