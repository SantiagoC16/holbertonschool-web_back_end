#!/usr/bin/env python3
"""task 0"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return a random number after delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
