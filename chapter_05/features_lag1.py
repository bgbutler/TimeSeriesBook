# create a lag feature
from pandas import Series
from pandas import DataFrame
from pandas import concat
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
temps = DataFrame(series.values)
dataframe = concat([temps.shift(1), temps], axis=1)
dataframe.columns = ['t', 't+1']
print(dataframe.head(5))