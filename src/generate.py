import pyrosim.pyrosim as pyrosim


def Create_World():
    length = 1
    width = 1
    height = 1

    x = -3
    y = 3
    z = height / 2

    pyrosim.Start_SDF("assets/box.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


def Create_Body():
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


def Create_Brain():
    pyrosim.Start_NeuralNetwork("assets/brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')
    pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLeg')
    pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
    pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
    pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')
    pyrosim.End()


Create_World()
Create_Body()
Create_Brain()
