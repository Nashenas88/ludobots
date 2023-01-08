import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
p.setGravity(0, 0, -9.8)


for i in range(1000):
    p.stepSimulation()
    time.sleep(1.0/60.0)

p.disconnect()
