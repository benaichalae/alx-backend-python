#!/usr/bin/env python3
"""Module containing the task_wait_random function."""

from . import wait_random  # Import from current directory
from asyncio import Task  # Explicit import for type annotation


def task_wait_random(max_delay: int) -> Task[float]:
    """
    Creates and returns an asyncio.Task object for the wait_random coroutine.

    Args:
        max_delay: The upper bound for the random delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task object representing
        the wait_random coroutine.
    """

    return asyncio.create_task(wait_random(max_delay))
