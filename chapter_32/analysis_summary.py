# summary statistics of time series
from pandas import Series
series = Series.from_csv('dataset.csv')
print(series.describe())