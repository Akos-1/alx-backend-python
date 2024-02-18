#!/usr/bin/env python3

from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on the given tuple by repeating each element
    according to the specified factor.

    Args:
        lst (Tuple[Any, ...]): The tuple to zoom in on.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in tuple.
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
