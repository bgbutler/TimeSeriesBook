# calculate descriptive statistics
from pandas import Series
series = Series.from_csv('daily-total-female-births.csv', header=0)
print(series.describe())