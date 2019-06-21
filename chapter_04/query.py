# query a dataset using a date-time index
from pandas import Series
series = Series.from_csv('daily-total-female-births.csv', header=0)
print(series['1959-01'])