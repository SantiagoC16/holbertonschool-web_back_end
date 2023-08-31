#!/usr/bin/env python3
"""task 0"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """return a list with 10 generated numbers"""
    for i in range(11):
        await asyncio.sleep(1)
        yield uniform(0, 10)
