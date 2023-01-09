from robot import ROBOT
from world import WORLD

import constants as c
import os
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self, mode, id):
        if mode == 'GUI':
            self.mode = p.GUI
        else:
            self.mode = p.DIRECT
        p.connect(self.mode)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAVITY)
        self.world = WORLD(id)
        bodyFile = f"assets/body{id}.urdf"
        brainFile = f"assets/brain{id}.nndf"
        self.robot = ROBOT(id, "../" + bodyFile, brainFile)
        os.remove(bodyFile)
        os.remove(brainFile)
        self.save_data = True

    def Set_Save_Data(self, save_data):
        self.save_data = save_data

    def Save_Motor_Targets(self):
        self.robot.Save_Motor_Targets

    def __del__(self):
        if self.save_data:
            self.robot.Save_Sensor_Data()
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def Run(self):
        for i in range(c.ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            if self.mode == p.GUI:
                time.sleep(c.LOOP_DELAY)
