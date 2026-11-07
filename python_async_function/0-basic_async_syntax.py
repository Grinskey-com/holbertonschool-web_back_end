#!/usr/bin/env python3
"""Async random delay"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """A random delay as a float"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
