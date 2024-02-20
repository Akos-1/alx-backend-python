#!/usr/bin/env python3

"""
This module defines an asynchronous generator coroutine
and an asynchronous comprehension coroutine.
"""
import asyncio
from random import randint
from typing import AsyncGenerator, List


async def async_generator() -> 'async_generator':
    """
    An asynchronous generator coroutine that yields random
    numbers between 0 and 10.

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


# Example usage:
async def main():
    result = await async_comprehension()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
