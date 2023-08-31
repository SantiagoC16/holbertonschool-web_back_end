#!/usr/bin/env python3
"""task 1"""

import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of all delays"""
    list_delays = []
    for i in range(n):
        list_delays.append(await wait_random(max_delay))
    return sorted(list_delays)
