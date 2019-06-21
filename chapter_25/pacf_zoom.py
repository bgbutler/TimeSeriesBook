# PACF plot of time series
from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
plot_pacf(series, lags=50)
pyplot.show()