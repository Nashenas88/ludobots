from sensor import SENSOR
from motor import MOTOR

import pybullet as p
from pyrosim import pyrosim
from neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self, bodyFile, brainFile):
        self.robotId = p.loadURDF(bodyFile)
        self.nn = NEURAL_NETWORK(brainFile)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
                                                                 neuron.Get_Value())

    def Save_Motor_Targets(self):
        for motor in self.motors.values():
            motor.Save_Data()

    def Save_Sensor_Data(self):
        for sensor in self.sensors.values():
            sensor.Save_Data()
