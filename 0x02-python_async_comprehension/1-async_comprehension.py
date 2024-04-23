#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using
an async comprehensing over async_generator,
then return the 10 random numbers.
"""

from typing import List


async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 random numbers using
    async comprehension from the async_generator coroutine.
    """
    from . import async_generator

    return [await num async for num in async_generator()]
