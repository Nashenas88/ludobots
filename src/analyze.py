import numpy
from matplotlib import pyplot

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
# pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
# pyplot.plot(frontLegSensorValues, label='front leg')
backAngles = numpy.load('data/backAngles.npy')
frontAngles = numpy.load('data/frontAngles.npy')
pyplot.plot(backAngles)
pyplot.plot(frontAngles)
pyplot.legend()
pyplot.show()
