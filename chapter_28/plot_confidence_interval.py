# plot the confidence intervals for an ARIMA forecast
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
# load data
series = Series.from_csv('daily-total-female-births.csv', header=0)
# split into train and test sets
X = series.values
X = X.astype('float32')
size = len(X) - 1
train, test = X[0:size], X[size:]
# fit an ARIMA model
model = ARIMA(train, order=(5,1,1))
model_fit = model.fit(disp=False)
# plot some history and the forecast with confidence intervals
model_fit.plot_predict(len(train)-10, len(train)+1)
pyplot.legend(loc='upper left')
pyplot.show()