import numpy
import pybullet as p
import pybullet_data
import time
from pyrosim import pyrosim

iterations = 1000

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("../assets/body.urdf")
p.loadSDF("../assets/box.sdf")
p.setGravity(0, 0, -9.8)

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)
for i in range(iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    time.sleep(1.0/60.0)

p.disconnect()
numpy.save("data/backLegSensorValues.npy", backLegSensorValues,
           allow_pickle=False, fix_imports=False)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues,
           allow_pickle=False, fix_imports=False)
