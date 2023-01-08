import pyrosim.neuralNetwork as neuralNetwork
from pyrosim import pyrosim
import math


class NEURAL_NETWORK(neuralNetwork.NEURAL_NETWORK):
    def __init__(self, nnrdfFile):
        super().__init__(nnrdfFile)

    def Update(self):
        for neuron in self.neurons.values():
            if neuron.Is_Sensor_Neuron():
                self.Update_Sensor_Neuron(neuron)
            else:
                self.Update_Hidden_Or_Motor_Neuron(neuron)

    def Get_Neurons(self):
        return self.neurons.values()

    def Update_Sensor_Neuron(self, neuron):
        neuron.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(
            neuron.Get_Link_Name()))

    def Update_Hidden_Or_Motor_Neuron(self, neuron):
        neuron.Set_Value(0)
