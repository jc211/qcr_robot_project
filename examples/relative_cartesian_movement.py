from dataclasses import dataclass
from typing import Literal
import os

import trio
import tyro
import panda_py

@dataclass
class Params:
    ip: str = os.environ.get("PANDA_IP", "172.16.0.2")
    platform: Literal['panda', 'fr3'] = os.environ.get("PANDA_PLATFORM", "panda") 

async def main():
    params = tyro.cli(Params)
    r = panda_py.Panda(params.ip, name=params.platform)

    r.recover() # Recover from any previous state
    speed = 1.0 # percent of max speed where 0.1 is 10% of the maximum speed

    # movepr is a relative cartesian movement command
    # The first argument is a list of [x, y, z] offsets in meters relative to the current position.
    await r.movepr([0.0, 0.0, 0.1], speed=speed)
    await r.movepr([0.0, 0.0, -0.1], speed=speed)

    # You can also pass a list of lists to movepr for multiple movements
    await r.movepr(
        [[0.0, 0.0, 0.1],
         [0.0, 0.0, -0.1]], speed=speed)

    # You can also specify different speeds for each movement
    await r.movepr(
        [[0.0, 0.0, 0.1],
         [0.0, 0.0, -0.1]], speed=[0.1, 1.0])


if __name__ == "__main__":
    trio.run(main)