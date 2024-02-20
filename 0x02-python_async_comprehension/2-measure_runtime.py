#!/usr/bin/env python3

"""
This module defines an asynchronous generator coroutine,
an asynchronous comprehension coroutine,
and a coroutine to measure the runtime.
"""

import asyncio
from typing import List
from time import perf_counter


async def async_generator() -> 'async_generator':
    """
    An asynchronous generator coroutine that yields
    random numbers between 0 and 10.

    Yields:
        int: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)


async def async_comprehension() -> List[int]:
    """
    An asynchronous comprehension coroutine that collects 10
    random numbers using async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers


async def measure_runtime() -> float:
    """
    A coroutine to measure the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime


# Example usage:
async def main():
    total_runtime = await measure_runtime()
    print(f"Total runtime: {total_runtime} seconds")


if __name__ == "__main__":
    asyncio.run(main())
