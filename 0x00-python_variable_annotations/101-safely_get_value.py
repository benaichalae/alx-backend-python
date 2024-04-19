#!/usr/bin/env python3
"""
This module defines a function 'safely_get_value'
that retrieves a value from a dictionary with a default value.
"""

from typing import Any, Dict, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Retrieves a value from a dictionary with
    a default value if the key is not found.

    Args:
        dct: The dictionary to get the value from.
        key: The key to look up in the dictionary.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
