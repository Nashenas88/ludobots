import constants as c
import numpy
from pyrosim import pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motor_force = c.MOTOR_FORCE
        self.amplitude = c.BACK_LEG_AMPLITUDE
        self.frequency = c.BACK_LEG_FREQUENCY
        self.phase_offset = c.BACK_LEG_PHASE_OFFSET

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=self.motor_force)

    def Save_Data(self):
        numpy.save(f'data/{self.jointName}Angles.npy', self.motorValues,
                   allow_pickle=False, fix_imports=False)
