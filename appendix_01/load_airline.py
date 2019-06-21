# load the airline passengers dataset
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('airline-passengers.csv', header=0)
print(series.head())
series.plot()
pyplot.show()