#!/usr/bin/env python3
"""
This module defines a function 'make_multiplier' that
takes a float and returns a function that
multiplies another float by the first float.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a new function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float value used for multiplication.

    Returns:
        A function that takes a float and returns its with the multiplier.
    """
    def inner(num: float) -> float:
        """
        Inner function that performs the multiplication with the multiplier.
        """
        return num * multiplier

    return inner
