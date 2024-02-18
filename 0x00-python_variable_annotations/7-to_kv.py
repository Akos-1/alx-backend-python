#!/usr/bin/env python3

"""
This module defines a function to_kv that takes a string k and an int
OR float v as arguments and returns a tuple with the first element
as the string k and the second element as the square of the int/float v
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments and returns a
    tuple with the first element as the string k and the second element
    as the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k
        and the square of v as a float.
    """
    return (k, v ** 2.0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
