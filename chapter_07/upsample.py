# upsample to daily intervals
from pandas import read_csv
from pandas import datetime

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
upsampled = series.resample('D').mean()
print(upsampled.head(32))