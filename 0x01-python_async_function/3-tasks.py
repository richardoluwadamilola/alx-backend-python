#!/usr/bin/env python3
"""import wait_random  from 0-basic_async_syntax"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait.random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Tasks"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
