#!/usr/bin/env python3
"""wait_n function"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function"""
    listTime: List[float] = []

    for i in range(n):
        listTime.append(await wait_random(max_delay))

    return sorted(listTime)
