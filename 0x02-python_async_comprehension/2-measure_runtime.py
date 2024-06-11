#!/usr/bin/env python3

""" module for task 2 """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for parallel comprehensions """
    s = time()
    t = [async_comprehension() for i in range(4)]
    await gather(*t)
    e = time()
    return (e - s)
