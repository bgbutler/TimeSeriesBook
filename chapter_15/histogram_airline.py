# plot a histogram of a time series
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('airline-passengers.csv', header=0)
series.hist()
pyplot.show()