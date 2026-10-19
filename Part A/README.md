# Unitree G1 Motion Playback in MuJoCo

## Project Overview

This project demonstrates a waving motion for the Unitree G1 humanoid robot. The motion was generated using UltimateBots Studio, exported as a CSV file, and reproduced using Python and MuJoCo.

The final motion is rendered as an MP4 video.

## Project Files

- `motion.csv` - Generated motion data
- `motion.mp4` - Rendered video of the robot waving
- `prompt.txt` - Text prompt used in UltimateBots Studio
- `robot_motion.py` - Displays the motion in the MuJoCo viewer
- `render_motion.py` - Renders the motion into an MP4 video
- `g1_description/` - Unitree G1 robot model and its required files

## Requirements

- Python
- MuJoCo
- imageio
- imageio-ffmpeg
- Unitree G1 29-DOF robot model from [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)

Install the required Python packages:

```bash
pip install mujoco imageio imageio-ffmpeg
```

## How to Reproduce

1. Download or clone this repository.
2. Make sure the `g1_description` folder is inside the project folder.
3. Install the required Python packages.
4. Keep `motion.csv` in the same folder as the Python scripts.
5. Run `python robot_motion.py` to view the motion interactively.
6. Run `python render_motion.py` to generate `motion.mp4`.

The motion contains 240 frames at 30 FPS, giving approximately 8 seconds of animation.

## How did you determine what the columns in the CSV represent?

I inspected the CSV using Python and found that it contained 240 rows and 36 columns. I then compared this with the Unitree G1 model in MuJoCo, which has 36 position values: 7 for the floating base and 29 for the robot's joints.

From this comparison, I inferred that the first three columns represent the robot's root position (x, y, z), the next four represent its orientation as a quaternion, and the remaining 29 represent joint positions.

The quaternion appeared to use the order (x, y, z, w), so I converted it to MuJoCo's required order (w, x, y, z).

Finally, I applied the values to the robot in MuJoCo and observed that the right arm performed the expected waving motion. This helped me visually validate the interpretation of the CSV data.

The mapping was inferred through inspection and testing rather than an official CSV column specification.