#!/usr/bin/env python3
"""Module containing the measure_time function."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n
    and returns the average time per wait.

    Args:
        n : The number of concurrent wait operations.
        max_delay: The upper bound for the random delays in seconds.

    Returns:
        float: The average execution time per wait operation.
    """

    start_time = time()
    await wait_n(n, max_delay)
    end_time = time()

    total_time = end_time - start_time
    return total_time / n
