import numpy
from matplotlib import pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
pyplot.plot(frontLegSensorValues, label='front leg')
pyplot.legend()
pyplot.show()
