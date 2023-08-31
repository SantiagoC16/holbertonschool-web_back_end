#!/usr/bin/env python3
"""task 1"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """a function that collect 10 random numbers and return them"""
    nums_to_return = [x async for x in async_generator()]
    return nums_to_return
