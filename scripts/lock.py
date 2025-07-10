from panda_desk import Desk
import trio
import os
import json
import tyro
from dataclasses import dataclass
from typing import Literal

@dataclass
class Params:
    ip: str = os.environ.get("PANDA_IP", "172.16.0.2")  # Default IP, change as needed
    platform: Literal['panda', 'fr3']  = os.environ.get("PANDA_PLATFORM", "panda")  # Default platform, change as needed
    username: str = os.environ.get("PANDA_USERNAME", "franka")  # Default username, change as needed
    password: str = os.environ.get("PANDA_PASSWORD", "")  # Default password, change as needed

async def main():
    print("Locking the robot...")
    params = tyro.cli(Params)
    robot_ip = params.ip
    platform = params.platform
    username = params.username
    password = params.password

    desk = Desk(robot_ip, platform=platform)
    await desk.login(username=username, password=password)
    await desk.take_control(force=True)
    await desk.activate_fci()
    await desk.lock()

if __name__ == "__main__":
    trio.run(main)