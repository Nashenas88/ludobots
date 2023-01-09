import numpy
import os
from pyrosim import pyrosim
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, id):
        self.id = id
        self.weights = numpy.random.rand(
            c.NUM_SENSOR_NEURONS, c.NUM_MOTOR_NEURONS) * 2 - 1

    def Show(self):
        if hasattr(self, 'fitness'):
            print(f'Id: {self.id} Fitness: {self.fitness}')
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 src/simulate.py GUI {self.id} >/dev/null 2>&1 &")

    def Start_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(
            f"python3 src/simulate.py DIRECT {self.id} >/dev/null 2>&1 &")

    def Wait_For_Simulation(self):
        fitnessFile = f'data/fitness{self.id}.npy'
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        self.fitness = numpy.load(
            fitnessFile, allow_pickle=False, fix_imports=False)
        os.remove(fitnessFile)

    def Mutate(self):
        self.weights[random.randint(0, c.NUM_SENSOR_NEURONS-1)][random.randint(
            0, c.NUM_MOTOR_NEURONS-1)] = random.random() * 2 - 1

    def Create_World(self):
        length = 1
        width = 1
        height = 1

        x = -3
        y = 3
        z = height / 2

        pyrosim.Start_SDF(f"assets/box{self.id}.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[
                          length, width, height])
        pyrosim.End()

    def Create_Body(self):
        length = 1
        width = 1
        height = 1

        pyrosim.Start_URDF(f"assets/body{self.id}.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[
            length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis='1 0 0')
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[
            0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis='1 0 0')
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[
            0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",
                           type="revolute", position=[-0.5, 0, 1], jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[
            1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",
                           type="revolute", position=[0.5, 0, 1], jointAxis='0 1 0')
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[
            1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_LowerBackLeg", parent="BackLeg", child="LowerBackLeg",
                           type="revolute", position=[0, -1, 0], jointAxis='1 0 0')
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[
            0.2, 0.2, 1])
        pyrosim.Send_Joint(name="Torso_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg",
                           type="revolute", position=[0, 1, 0], jointAxis='1 0 0')
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[
            0.2, 0.2, 1])
        pyrosim.Send_Joint(name="Torso_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg",
                           type="revolute", position=[-1, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[
            0.2, 0.2, 1])
        pyrosim.Send_Joint(name="Torso_LowerRightLeg", parent="RightLeg", child="LowerRightLeg",
                           type="revolute", position=[1, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[
            0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"assets/brain{self.id}.nndf")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')
        # pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLeg')
        # pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
        # pyrosim.Send_Sensor_Neuron(name=3, linkName='LeftLeg')
        # pyrosim.Send_Sensor_Neuron(name=4, linkName='RightLeg')
        pyrosim.Send_Sensor_Neuron(name=0, linkName='LowerBackLeg')
        pyrosim.Send_Sensor_Neuron(name=1, linkName='LowerFrontLeg')
        pyrosim.Send_Sensor_Neuron(name=2, linkName='LowerLeftLeg')
        pyrosim.Send_Sensor_Neuron(name=3, linkName='LowerRightLeg')
        pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=5, jointName='Torso_FrontLeg')
        pyrosim.Send_Motor_Neuron(name=6, jointName='Torso_LeftLeg')
        pyrosim.Send_Motor_Neuron(name=7, jointName='Torso_RightLeg')
        pyrosim.Send_Motor_Neuron(name=8, jointName='Torso_LowerBackLeg')
        pyrosim.Send_Motor_Neuron(name=9, jointName='Torso_LowerFrontLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='Torso_LowerLeftLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_LowerRightLeg')
        for currentRow in range(c.NUM_SENSOR_NEURONS):
            for currentColumn in range(c.NUM_MOTOR_NEURONS):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
