from pathlib import Path
import csv
import time
import mujoco
import mujoco.viewer
folder = Path(__file__).resolve().parent
modelpath = folder / "g1_description" / "g1_29dof.xml"
model = mujoco.MjModel.from_xml_path(str(modelpath))
data = mujoco.MjData(model)
csvlocation=folder/"motion.csv"
with open(csvlocation, 'r') as file:
    read = csv.reader(file)
    motion = list(read)
with mujoco.viewer.launch_passive(model,data) as viewer:
           viewer.cam.lookat[:] = [0, 0, 0.8]
           viewer.cam.distance = 3.0
           viewer.cam.azimuth = 180
           viewer.cam.elevation = -10
           viewer.sync()
     #while viewer.is_running():
           for row in motion:
               frame = []
               for value in row:
                    frame.append(float(value))
               data.qpos[0:3] = frame[0:3]
               data.qpos[3:7] =[
                  frame[6],
                  frame[3],
                  frame[4],
                  frame[5]
                ]
               data.qpos[7:36] = frame[7:36]
               mujoco.mj_forward(model, data)
               viewer.sync()
               time.sleep(1/30)
           input("Motion finished! Press Enter to close...")
