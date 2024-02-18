#!/usr/bin/env python3
"""
    Returns the first element of a list if it exists, otherwise returns None.

    Args:
        lst (List[Any]): The input list.

    Returns:
        Union[Any, None]: The first element of the list if it exists,
        otherwise None.
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
