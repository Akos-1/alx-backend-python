#!/usr/bin/env python3

"""
This module defines a function make_multiplier that takes a float multiplier
as an argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function
    that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float
        by the given multiplier.
    """
    def multiplier_func(num: float) -> float:
        """
        Inner function that multiplies a float by the multiplier.

        Args:
            num (float): The input number to be multiplied.

        Returns:
            float: The result of multiplying the input number by
            the multiplier.
        """
        return num * multiplier

    return multiplier_func


if __name__ == "__main__":
    import doctest
    doctest.testmod()
