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
    q1 = [-0.457, -0.794, 0.284, -2.589, 0.309, 1.888, 0.766]
    q2 = [-0.99, -0.304, -0.174, -2.302, -0.144, 1.942, 0.686]

    await r.movej(q1, speed=speed)
    await r.movej(q2, speed=speed)




if __name__ == "__main__":
    trio.run(main)