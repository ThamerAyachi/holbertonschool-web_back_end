#!/usr/bin/env python3
""" wait_random Fonction """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random Fonction """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
