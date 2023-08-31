#!/usr/bin/env python3
"""task 3"""
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


async def measure_time(n: int, max_delay: int) -> float:
    """a function that measures the total execution time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
