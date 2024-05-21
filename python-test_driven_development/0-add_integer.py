#!/usr/bin/python3
"""
Functions that adds two integers.
a and b must be integers or floats, otherwise raise a TypeError exception
a and b must be first casted to integers if they are float

"""


def add_integer(a, b=98):
    """
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(0, 0)
    0
    >>> add_integer(3, 5)
    8
    >>> add_integer(5, 5)
    10
    >>> add_integer(120, -20)
    100
    >>> add_integer(200, -100)
    100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)

    return a + b
