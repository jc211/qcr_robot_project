import trio
import os
import tyro
from dataclasses import dataclass
from typing import Literal
import panda_py

@dataclass
class Params:
    variable_name: tyro.conf.Positional[str] = "r"
    ip: str = os.environ.get("PANDA_IP", "172.16.0.2")  # Default IP, change as needed
    platform: Literal['panda', 'fr3']  = os.environ.get("PANDA_PLATFORM", "panda")  # Default platform, change as needed
    username: str = os.environ.get("PANDA_USERNAME", "franka")  # Default username, change as needed
    password: str = os.environ.get("PANDA_PASSWORD", "")  # Default password, change as needed

async def main():
    params = tyro.cli(Params)
    variable_name = params.variable_name
    r = panda_py.Panda(params.ip, name=params.platform)
    x = r.get_orientation()
    print(f"{variable_name} = {x.round(4).tolist()}")


if __name__ == "__main__":
    trio.run(main)