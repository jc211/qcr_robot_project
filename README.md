# QUT Robot Project

This project provides tools and scripts for controlling a Franka Panda robot using [pixi](https://pixi.sh/) and Python.

---

## Prerequisites

### 1. Install Pixi

If you don't have pixi installed, run:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone https://github.com/jc211/qcr_robot_project
cd qcr_robot_project
```

### 3. Configure Robot Credentials

Edit `pixi.toml` to set your robot's connection details:

```toml
// pixi.toml
[activation.env]
PANDA_IP = "172.16.0.2"
PANDA_USERNAME = "myusername"
PANDA_PASSWORD = "mypassword"
PANDA_PLATFORM = "panda"
```

You can also override these credentials using command-line arguments.

---

## Hardware Setup

- Connect the Panda robot controller directly to your computer via Ethernet.
- Avoid using a router to prevent packet loss and unexpected robot stops.

---

## Pixi Shortcut Commands

From the project directory, you can use the following commands (The first time you run any of these commands, it may take a while because it has to pull the dependencies needed):

### Unlock the Robot

Unlocks the robot, takes control of the admin panel, and enables FCI.

```bash
pixi r unlock
```

To specify custom credentials:

```bash
pixi r unlock --ip <IP> --username <USERNAME> --password <PASSWORD> --platform <PLATFORM>
```

### Lock the Robot

```bash
pixi r lock
```

### Home the Robot

Moves the robot to its home position (facing front). Ensure your setup allows for this movement.

```bash
pixi r home
```

To home at 100% speed
```bash
pixi r home 1.0
```

### Query Robot State

Prints commands to assign current robot state to variables for easy copy-pasting.

- **Joints:**  
  ```bash
  pixi r q
  pixi r q my_var  # custom variable name
  ```
- **Pose:**  
  ```bash
  pixi r x
  ```
- **Rotation:**  
  ```bash
  pixi r r
  ```
- **Position:**  
  ```bash
  pixi r p
  ```

---

## Example Python Scripts

### Create a Robot Object

```python
import panda_py
import trio

async def main():
    robot = panda_py.Panda("172.16.0.2")
    state = robot.get_state()
    print(state)

trio.run(main)
```

### Move the Robot Using Joint Commands

```python
import panda_py
import trio

async def main():
    robot = panda_py.Panda("172.16.0.2")
    q = [-0.457, -0.794, 0.284, -2.589, 0.309, 1.888, 0.766]
    await robot.movej(q, speed=0.1)  # speed is a percentage of max speed (10% here)

trio.run(main)
```

To run these scripts, enter the pixi shell first:

```bash
cd qcr_robot_project
pixi shell
python main.py
```

---

## Notes

- For more advanced usage, refer to the example scripts.
- Always ensure the robot's workspace is clear before running movement commands.
- If you encounter connection issues, double-check your Ethernet setup and credentials.

---




