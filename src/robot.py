from sensor import SENSOR
from motor import MOTOR
from neuralNetwork import NEURAL_NETWORK
import constants as c

import numpy
import os
import pybullet as p
from pyrosim import pyrosim


class ROBOT:
    def __init__(self, id, bodyFile, brainFile):
        self.id = id
        self.robotId = p.loadURDF(bodyFile)
        self.nn = NEURAL_NETWORK(brainFile)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordOfLinkZero = positionOfLinkZero[0]
        tmpPath = f'data/tmp{self.id}.npy'
        numpy.save(tmpPath, xCoordOfLinkZero,
                   allow_pickle=False, fix_imports=False)
        os.rename(tmpPath, f'data/fitness{self.id}.npy')

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Think(self):
        self.nn.Update()

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuron in self.nn.Get_Neurons():
            if neuron.Is_Motor_Neuron():
                jointName = neuron.Get_Joint_Name()
                self.motors[jointName.encode('ascii')].Set_Value(self.robotId,
                                                                 neuron.Get_Value() * c.MOTOR_JOINT_RANGE)

    def Save_Motor_Targets(self):
        for motor in self.motors.values():
            motor.Save_Data()

    def Save_Sensor_Data(self):
        for sensor in self.sensors.values():
            sensor.Save_Data()
