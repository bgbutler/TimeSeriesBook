# load the shampoo sales dataset
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('shampoo-sales.csv', header=0)
print(series.head())
series.plot()
pyplot.show()