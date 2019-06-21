# plot a histogram of a time series
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('daily-total-female-births.csv', header=0)
series.hist()
pyplot.show()