from dataclasses import dataclass
from typing import Literal
import os

import trio
import tyro
import numpy as np
import panda_py

@dataclass
class Params:
    speed: tyro.conf.Positional[float] = 0.1  # Default speed as a percentage of max speed
    ip: str = os.environ.get("PANDA_IP", "172.16.0.2")
    platform: Literal['panda', 'fr3'] = os.environ.get("PANDA_PLATFORM", "panda") 

async def main():
    params = tyro.cli(Params)
    r = panda_py.Panda(params.ip, name=params.platform)

    r.recover() # Recover from any previous state
    speed = params.speed  # Use the speed from params
    q = [0.0, -np.pi / 4, 0.0, -3 * np.pi / 4, 0.0, np.pi / 2, np.pi / 4]
    await r.movej(q, speed=speed)
    

if __name__ == "__main__":
    trio.run(main)