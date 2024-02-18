#!/usr/bin/env python3
"""
    Takes a list of strings lst as input and returns a list of tuples,
    where each tuple contains an element from lst and its corresponding length

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing
        elements from lst and their corresponding lengths.
    """

import typing


def element_length('lst': typing.Iterable[typing.Sequence]) -> \ 
        typing.List[typing.Tuple[typing.Sequence, int]]
    return [(i, len(i)) for i in lst]
