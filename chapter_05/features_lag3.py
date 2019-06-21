# create lag features
from pandas import Series
from pandas import DataFrame
from pandas import concat
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
temps = DataFrame(series.values)
dataframe = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
dataframe.columns = ['t-2', 't-1', 't', 't+1']
print(dataframe.head(5))