import sys
import pandas as pd 
import datetime

import pandas_datareader.data as web

import matplotlib.pyplot as plt
from matplotlib import style

#pip install pandas-datareader
#pip install matplotlib
#pip install pandas


style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 5, 12)

df = web.DataReader("XOM", "yahoo", start, end)

print(df)

print(df.head())

print(df.tail())




#style.use('fivethirtyeight')


df['High'].plot()
plt.legend()
plt.show()
