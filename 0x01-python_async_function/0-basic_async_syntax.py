#!/usr/bin/env python3
'''module for task 0.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number.
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
