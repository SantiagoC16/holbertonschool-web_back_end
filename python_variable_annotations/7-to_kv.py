#!/usr/bin/env python3
"""task 7"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """return a tuple with an str and int/float"""
    return (k, float(v**2))
