#!/usr/bin/env python3

"""
This module defines a function add that takes two float numbers
and returns their sum.
"""


def add(a: float, b: float) -> float:
    """
    Adds two float numbers and returns their sum.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
