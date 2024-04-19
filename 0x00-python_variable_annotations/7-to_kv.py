#!/usr/bin/env python3
"""
This module defines a function 'to_kv' that takes
a string key and an int or float value
and returns a tuple with the key and the square of the value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string key and the square of the int/float value.

    Args:
        k: The string key.
        v: The integer or float value.

    Returns:
        A tuple containing the key (str) and the square of the value (float).
    """
    return k, v * v
