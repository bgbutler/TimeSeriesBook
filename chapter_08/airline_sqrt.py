# square root transform a time series
from pandas import Series
from pandas import DataFrame
from numpy import sqrt
from matplotlib import pyplot
series = Series.from_csv('airline-passengers.csv', header=0)
dataframe = DataFrame(series.values)
dataframe.columns = ['passengers']
dataframe['passengers'] = sqrt(dataframe['passengers'])
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['passengers'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['passengers'])
pyplot.show()