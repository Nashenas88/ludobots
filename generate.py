import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = height / 2

pyrosim.Start_SDF("boxes.sdf")
for i in range(5):
    for j in range(5):
        scale = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x + length * i, y + width * j, z + height * k], size=[
                length*scale, width*scale, height*scale])
            scale *= 0.9

pyrosim.End()
