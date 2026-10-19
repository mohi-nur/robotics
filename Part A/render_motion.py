from pathlib import Path
import csv
import mujoco
import imageio
folder = Path(__file__).resolve().parent
modelpath = folder / "g1_description" / "g1_29dof.xml"
model = mujoco.MjModel.from_xml_path(str(modelpath))
data = mujoco.MjData(model)
csvlocation = folder/"motion.csv"
with open(csvlocation, "r") as file:
    read = csv.reader(file)
    motion = list(read)
video = imageio.get_writer("motion.mp4", fps=30)
camera = mujoco.MjvCamera()
camera.type = mujoco.mjtCamera.mjCAMERA_FREE
camera.lookat[:] = [0, 0, 0.8]
camera.distance = 3.0
camera.azimuth = 180
camera.elevation = -10
with mujoco.Renderer(model, height=480, width=640) as renderer:
    for row in motion:
        frame = []
        for value in row:
            frame.append(float(value))

        data.qpos[0:3] = frame[0:3]
        data.qpos[3:7] = [frame[6], frame[3], frame[4], frame[5]]
        data.qpos[7:36] = frame[7:36]

        mujoco.mj_forward(model, data)

        renderer.update_scene(data, camera=camera)
        image = renderer.render()
        video.append_data(image)

video.close()
print("Finished! motion.mp4 has been created.")
