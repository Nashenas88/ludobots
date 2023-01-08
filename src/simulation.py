from robot import ROBOT
from world import WORLD

import constants as c
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self):
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAVITY)
        self.world = WORLD()
        self.robot = ROBOT("../assets/body.urdf")
        self.robot.motors[b'Torso_FrontLeg'].Set_Frequency(
            self.robot.motors[b'Torso_BackLeg'].frequency/2)
        self.save_data = True

    def Set_Save_Data(self, save_data):
        self.save_data = save_data

    def Save_Motor_Targets(self):
        self.robot.Save_Motor_Targets

    def __del__(self):
        if self.save_data:
            self.robot.Save_Sensor_Data()
        p.disconnect()

    def Run(self):
        for i in range(c.ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(c.LOOP_DELAY)
