import pybullet as p
import time

p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    time.sleep(1.0/60.0)

p.disconnect()
