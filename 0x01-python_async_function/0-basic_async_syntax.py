#!/usr/bin/env python3
'''The basics of async'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds multiplied by numbers 0-10
    and returns float'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
