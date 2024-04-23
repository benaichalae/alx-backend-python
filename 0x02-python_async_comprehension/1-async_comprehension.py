#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using
an async comprehensing over async_generator,
then return the 10 random numbers.
"""

import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random numbers between 0 and 10
    after waiting for 1 second each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
