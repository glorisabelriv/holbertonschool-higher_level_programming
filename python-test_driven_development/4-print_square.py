#!/usr/bin/python3
"""
This module imports a function
that prints a square of a specified size
"""


def print_square(size):
    """
    Function that prints a square with
    dimensions of size and with character #
        Args:
            size (int): length of sides of square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
