#!/usr/bin/env python3

"""
This module defines an asynchronous generator coroutine that
yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    An asynchronous generator coroutine that yields random numbers
    between 0 and 10.

    Yields:
        int: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def main():
    async for num in async_generator():
        print(num)


def entry_point():
    asyncio.run(main())


if __name__ == "__main__":
    entry_point()
