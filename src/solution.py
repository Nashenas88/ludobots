import numpy
import os
from pyrosim import pyrosim
import random


class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3, 2) * 2 - 1

    def Show(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 src/simulate.py GUI")

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 src/simulate.py DIRECT")
        self.fitness = numpy.load(
            'data/fitness.npy', allow_pickle=False, fix_imports=False)

    def Mutate(self):
        self.weights[random.randint(0, 2)][random.randint(
            0, 1)] = random.random() * 2 - 1

    def Create_World(self):
        length = 1
        width = 1
        height = 1

        x = -3
        y = 3
        z = height / 2

        pyrosim.Start_SDF("assets/box.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[
                          length, width, height])
        pyrosim.End()

    def Create_Body(self):
        length = 1
        width = 1
        height = 1

        pyrosim.Start_URDF("assets/body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, height * 3 / 2], size=[
            length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[-length/2, 0, height])
        pyrosim.Send_Cube(name="BackLeg", pos=[-length/2, 0, -height/2], size=[
            length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[length/2, 0, height])
        pyrosim.Send_Cube(name="FrontLeg", pos=[length/2, 0, -height/2], size=[
            length, width, height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("assets/brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')
        pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLeg')
        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
        pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
