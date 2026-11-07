#!/usr/bin/env python3
"""Async comprehension on an async gen"""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """collect 10 random numbers form async_gen using async comprehension"""
    return [i async for i in async_generator()]
