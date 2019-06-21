# load dataset using Series.from_csv()
from pandas import Series
series = Series.from_csv('daily-total-female-births.csv', header=0)
print(series.head())