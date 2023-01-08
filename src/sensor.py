import constants as c
import numpy
from pyrosim import pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensorValues = numpy.zeros(c.ITERATIONS)

    def Get_Value(self, t):
        self.sensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            self.linkName)

    def Save_Data(self):
        numpy.save(f'data/{self.linkName}SensorValues.npy', self.sensorValues,
                   allow_pickle=False, fix_imports=False)
