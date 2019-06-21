# load the sunspots dataset
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('sunspots.csv', header=0)
print(series.head())
series.plot()
pyplot.show()