import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

style.use('ggplot')



end = dt.datetime(2021, 1, 1)
start = end - dt.timedelta(days=180)

df = web.get_data_yahoo('TSLA', start, end)
df = web.DataReader('TSLA', 'yahoo', start, end) 
df.to_csv('tsla.csv')

# df = pd.read_csv('tsla.csv')
print(df.head())


