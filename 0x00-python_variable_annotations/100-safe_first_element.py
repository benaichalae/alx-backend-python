#!/usr/bin/env python3
"""
This module defines a function 'safe_first_element'
that handles lists of unknown element types.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list if it exists, otherwise None.

    This function uses duck-typing to check if the list can be indexed
    without raising an exception.

    Args:
        lst: The list to get the first element from.

    Returns:
        The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
