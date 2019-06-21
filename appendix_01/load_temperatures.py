# load the minimum temperatures dataset
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
print(series.head())
series.plot()
pyplot.show()