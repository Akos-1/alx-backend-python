#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine wait_random that waits
for a random delaybetween 0 and max_delay seconds (inclusive)
and eventually returns it.
"""

import asyncio
import random

random.seed(0)


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds (inclusive) and eventually returns it.

    Args:
        max_delay (float, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
