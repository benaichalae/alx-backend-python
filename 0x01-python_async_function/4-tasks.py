#!/usr/bin/env python3
"""Module containing the task_wait_n function."""

import asyncio
import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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

    delay = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay)
