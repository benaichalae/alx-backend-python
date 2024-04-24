#!/usr/bin/env python3
"""Module containing the task_wait_n function."""

import asyncio
from typing import List

from . import task_wait_random  # Import from current directory


async def task_wait_n(n: int, max_delay: float = 10.0) -> List[float]:
    """
    Creates and waits for n tasks running wait_random concurrently,
    returning their results in ascending order.

    Args:
        n : The number of concurrent wait operations.
        max_delay: The upper bound for the random delays in seconds.

    Returns:
        List: A list of the random delays returned
        by the tasks in ascending order.
    """

    tasks = []
    for _ in range(n):
        # Create tasks for each task_wait_random call
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Wait for all tasks to finish concurrently
    delays = await asyncio.gather(*tasks)

    # Sort delays in ascending order using list comprehension
    sorted_delays = [delay for delay in sorted(delays)]

    return sorted_delays
