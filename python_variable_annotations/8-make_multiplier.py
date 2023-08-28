#!/usr/bin/env python3
"""task 8"""
from typing import Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """float and return a multiply of float"""
    def multiply(num_float: float) -> float:
        return num_float * multiplier
    return multiply
