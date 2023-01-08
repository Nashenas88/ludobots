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
        self.Prepare_To_Act()

    def Set_Amplitude(self, amplitude, update=True):
        self.amplitude = amplitude
        if update:
            self.Prepare_To_Act()

    def Set_Frequency(self, frequency, update=True):
        self.frequency = frequency
        if update:
            self.Prepare_To_Act()

    def Set_Phase_Offset(self, phase_offset, update=True):
        self.phase_offset = phase_offset
        if update:
            self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = [self.amplitude * numpy.sin(self.frequency * x + self.phase_offset)
                            for x in numpy.linspace(c.SIN_START, c.SIN_END, c.ITERATIONS)]

    def Set_Value(self, robotId, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=self.motor_force)

    def Save_Data(self):
        numpy.save(f'data/{self.jointName}Angles.npy', self.motorValues,
                   allow_pickle=False, fix_imports=False)
