import pybullet as p
import time

p.connect(p.GUI)
p.loadSDF("box.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1.0/60.0)

p.disconnect()
