#!/usr/bin/env python3

from typing import Any, Union, List


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if it exists, otherwise returns None.

    Args:
        lst (List[Any]): The input list.

    Returns:
        Union[Any, None]: The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
