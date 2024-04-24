#!/usr/bin/env python3
"""Module containing the wait_n coroutine."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for n random delays concurrently and returns them in ascending order.

    Args:
        n: The number of concurrent wait operations.
        max_delay: The upper bound for the random delays in seconds.

    Returns:
        List[float]: A list of the random delays in ascending order.
    """

    tasks = []
    for _ in range(n):
        # Create tasks for each wait_random call
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Wait for all tasks to finish concurrently
    delays = await asyncio.gather(*tasks)

    # Sort delays in ascending order using list comprehension
    sorted_delays = [delay for delay in sorted(delays)]

    return sorted_delays
