#!/usr/bin/env python3

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings lst as input and returns a list of tuples,
    where each tuple contains an element from lst and its corresponding length.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing elements from
        lst and their corresponding lengths.
    """
    return [(i, len(i)) for i in lst]
