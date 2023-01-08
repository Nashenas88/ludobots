import numpy
import pybullet as p
import pybullet_data
from pyrosim import pyrosim
import time


ITERATIONS = 1000
MOTOR_FORCE = 25

BACK_LEG_AMPLITUDE = numpy.pi/4
BACK_LEG_FREQUENCY = 25
BACK_LEG_PHASE_OFFSET = 0

backLegTargetAngles = [BACK_LEG_AMPLITUDE * numpy.sin(BACK_LEG_FREQUENCY * x + BACK_LEG_PHASE_OFFSET)
                       for x in numpy.linspace(0, 2*numpy.pi, 1000)]
FRONT_LEG_AMPLITUDE = numpy.pi / 4
FRONT_LEG_FREQUENCY = 5
FRONT_LEG_PHASE_OFFSET = numpy.pi/4

frontLegTargetAngles = [FRONT_LEG_AMPLITUDE * numpy.sin(FRONT_LEG_FREQUENCY * x + FRONT_LEG_PHASE_OFFSET)
                        for x in numpy.linspace(0, 2*numpy.pi, 1000)]
# numpy.save('data/backAngles.npy', backLegTargetAngles,
#            allow_pickle=False, fix_imports=False)
# numpy.save('data/frontAngles.npy', frontLegTargetAngles,
#            allow_pickle=False, fix_imports=False)
# exit()

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("../assets/body.urdf")
p.loadSDF("../assets/box.sdf")
p.setGravity(0, 0, -9.8)

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(ITERATIONS)
frontLegSensorValues = numpy.zeros(ITERATIONS)
for i in range(ITERATIONS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],
        maxForce=MOTOR_FORCE)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],
        maxForce=MOTOR_FORCE)
    time.sleep(1.0/60.0)

p.disconnect()
numpy.save("data/backLegSensorValues.npy", backLegSensorValues,
           allow_pickle=False, fix_imports=False)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues,
           allow_pickle=False, fix_imports=False)
