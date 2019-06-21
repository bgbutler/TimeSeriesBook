# reframe precision of regression forecast
from pandas import Series
from pandas import DataFrame
from pandas import concat
# load data
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
# create lagged dataset
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t', 't+1']
# round forecast to nearest 5
for i in range(len(dataframe['t+1'])):
	dataframe['t+1'][i] = int(dataframe['t+1'][i] / 5) * 5.0
print(dataframe.head(5))