# multiplicative decompose time series
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = Series.from_csv('airline-passengers.csv', header=0)
result = seasonal_decompose(series, model='multiplicative')
result.plot()
pyplot.show()