#!/usr/bin/env python3
"""
This module defines a function 'zoom_array' that
zooms in on a tuple by repeating its elements.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on a tuple by repeating its elements a specified number of times.

    Args:
        lst: The tuple to zoom in on.
        factor: The number of times to repeat each element (default is 2).

    Returns:
        A new tuple containing the zoomed-in elements.
    """
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
