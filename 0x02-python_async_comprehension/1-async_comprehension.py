#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using
an async comprehensing over async_generator,
then return the 10 random numbers.
"""

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    """
    return [num async for num in async_generator()]
