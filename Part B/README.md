# Part B - Unitree G1 Walking in a Circle

## Project Overview

In this project, I used the pretrained Unitree G1 walking policy in MuJoCo. My task was to make the robot walk in a circle instead of walking straight.

## What I Did

First, I opened the Unitree RL Gym project and installed the missing Python libraries, including PyTorch and PyYAML.

I ran the walking code using Command Prompt. At first, the robot walked straight.

Then I opened `g1.yaml` and changed the walking command from:

`cmd_init: [0.5, 0, 0]`

to:

`cmd_init: [0.5, 0, 0.4]`

The first number controls forward movement, the second controls sideways movement, and the third controls turning.

By moving forward and turning at the same time, the robot started walking in a circular path.

I also changed `simulation_duration` to `20` so I could record a shorter video.

In `circle_walk.py`, I added video recording using `imageio` and MuJoCo's renderer. I also adjusted the camera to see the robot's full body.

Finally, I saved the video as `circle_walk.mp4`.

## 1. What inputs does the policy receive, and where do they come from?

The policy receives information about the robot's body direction, turning speed, joint positions, joint speeds, previous actions, walking commands, and walking cycle.

Most of this information comes from the MuJoCo simulation. The walking commands come from `g1.yaml`.

## 2. What does the policy output, and how is it converted into joint torques?

The policy outputs actions that are used to calculate the target positions of the robot's joints.

The Python code compares these target positions with the actual joint positions.

A PD controller then calculates the joint torques, which are the turning forces needed to move the joints.

MuJoCo uses these torques to make the robot walk.

## How to Run

I used Command Prompt to run the Python script.

From the main Unitree RL Gym folder, I entered:

`py -3.13 deploy/deploy_mujoco/circle_walk.py g1.yaml`

To reproduce the result, `circle_walk.py` should be placed in the `deploy/deploy_mujoco` folder, and `g1.yaml` in its `configs` folder. The original pretrained policy and robot model files are also required.

## Result

The Unitree G1 robot successfully walked in a circular path, and I recorded the movement in `circle_walk.mp4`.