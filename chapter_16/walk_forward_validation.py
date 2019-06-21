# walk forward evaluation model for time series data
from pandas import Series
series = Series.from_csv('sunspots.csv', header=0)
X = series.values
n_train = 500
n_records = len(X)
for i in range(n_train, n_records):
	train, test = X[0:i], X[i:i+1]
	print('train=%d, test=%d' % (len(train), len(test)))