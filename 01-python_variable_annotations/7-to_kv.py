#!/usr/bin/env python3
"""task 7"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple with an str and int/float"""
    return (k, float(v**2))
