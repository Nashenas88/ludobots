import pybullet as p
import os


class WORLD:
    def __init__(self, id):
        self.planeId = p.loadURDF("plane.urdf")
        boxFile = f"assets/box{id}.sdf"
        self.box = p.loadSDF("../" + boxFile)
        os.remove(boxFile)
