#!/usr/bin/env python3
"""
This module defines a function 'sum_list' that
takes a list of floats and returns their sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of the elements in a list of floats.

    Args:
        input_list: A list of float numbers.

    Returns:
        The sum of the elements in input_list.
    """
    return float(sum(input_list))
