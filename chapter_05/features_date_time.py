# create date time features of a dataset
from pandas import Series
from pandas import DataFrame
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
dataframe = DataFrame()
dataframe['month'] = [series.index[i].month for i in range(len(series))]
dataframe['day'] = [series.index[i].day for i in range(len(series))]
dataframe['temperature'] = [series[i] for i in range(len(series))]
print(dataframe.head(5))