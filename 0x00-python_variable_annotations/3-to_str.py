#!/usr/bin/env python3

"""
This module defines a function to_str that
converts a float to its string representation.
"""


def to_str(n: float) -> str:
    """
    Converts a float to its string representation.

    Args:
        n (float): The float number.

    Returns:
        str: The string representation of the float.
    """
    return str(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
