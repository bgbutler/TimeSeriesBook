# reframe time horizon of forecast
from pandas import Series
from pandas import DataFrame
from pandas import concat
# load data
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
# create lagged dataset
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values, values.shift(-1),
	values.shift(-2), values.shift(-3), values.shift(-4), values.shift(-5),
	values.shift(-6)], axis=1)
dataframe.columns = ['t', 't+1', 't+2', 't+3', 't+4', 't+5', 't+6', 't+7']
print(dataframe.head(14))