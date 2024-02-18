#!/usr/bin/env python3

"""
    Safely retrieves a value from a dictionary based on a key.

    Args:
        dct (Dict[str, T]): The dictionary to retrieve the value from.
        key (str): The key to search for in the dictionary.
        default (Optional[T]): The default value to return if the key is not
        found (default is None).

    Returns:
        Optional[T]: The value associated with the key in the dictionary
        if it exists,otherwise returns the default value.
"""
import typing import

# Define a type variable for the value
T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
