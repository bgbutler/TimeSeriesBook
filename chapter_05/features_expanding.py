# create expanding window features
from pandas import Series
from pandas import DataFrame
from pandas import concat
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
temps = DataFrame(series.values)
window = temps.expanding()
dataframe = concat([window.min(), window.mean(), window.max(), temps.shift(-1)], axis=1)
dataframe.columns = ['min', 'mean', 'max', 't+1']
print(dataframe.head(5))