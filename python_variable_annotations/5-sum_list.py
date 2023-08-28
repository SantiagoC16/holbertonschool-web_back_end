#!/usr/bin/env python3
"""task 5"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list"""
    num_float = 0.0
    for num in input_list:
        num_float += num
    return num_float
