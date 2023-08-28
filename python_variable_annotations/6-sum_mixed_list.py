#!/usr/bin/env python3
"""task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum int and float and return float"""
    num_float = 0.0
    for num in mxd_lst:
        num_float += num
    return num_float
