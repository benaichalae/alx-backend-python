#!/usr/bin/env python3
"""
This module defines a function 'sum_mixed_list' that
takes a list of mixed integers and floats
and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of the elements in a list of mixed integers and floats.

    Args:
        mxd_lst: A list containing integers and/or floats.

    Returns:
        The sum of the elements in mxd_lst (as a float).
    """
    return float(sum(mxd_lst))
