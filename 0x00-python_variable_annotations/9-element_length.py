#!/usr/bin/env python3
"""Calculates length of elements in an iterable of sequences."""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their lengths.

    Args:
        lst: An iterable containing sequences (strings, lists, etc.).

    Returns:
        A list of tuples where each tuple has (element, length).
    """
    return [(i, len(i)) for i in lst]
