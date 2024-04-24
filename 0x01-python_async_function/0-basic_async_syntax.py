#!/usr/bin/env python3
"""Module containing the wait_random coroutine."""

import asyncio
import random


async def wait_random(max_delay: in = 10) -> float:
    """
    Waits for a random number of seconds between 0 and max_delay.

    Args:
        max_delay: The upper bound for the random delay in seconds.

    Returns:
        float: The random delay that the coroutine waited for.
    """

    wait_time = random.random() * max_delay
    await asyncio.sleep(delay)
    return wait_time
