#!/usr/bin/env python3
"""task 4"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of all delays"""
    list_delays = []
    for i in range(n):
        list_delays.append(await task_wait_random(max_delay))
    return sorted(list_delays)
