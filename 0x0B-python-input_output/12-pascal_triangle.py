#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """ return pascal triangle """
    pascal_list = []
    new_list = []
    pascal_number = 0

    if n <= 0:
        return pascal_list

    for i in range(0, n):
        pascal_number = 11 ** i
        pascal_list.append(str(pascal_number))
    for j in pascal_list:
        new_list.append(j)

    return new_list
